from django.db import transaction
from django_redis import get_redis_connection
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from django_redis import get_redis_connection

# 购物车相关接口
from course.models import Course
from edu_drf.utils.use_url.useUrl import IMG_URL


class CartViewSet(ViewSet):
    # 第一步，检验用户信息是否合法，只有合法用户才能进入该接口进行操作
    # 判断用户是否合法（区分游客和合法用户）
    # permission_classes = [IsAuthenticated,]

    def add_cart(self, request):
        # 从前端获取信息：course_id, user_id, 课程有效期, 是否勾选
        print(18888,request.data)
        course_id = request.data.get('course_id')
        # user_id = request.user.id
        user_id = request.data.get('user_id')
        # print(22,course_id)
        # print(23,user_id)
        select =True    #默认设置为勾选上
        expire = 0   #默认有效期设置为永久有效

        # 校验前端传递的参数
        try:
            # 判断前端传过来的课程是否存在、是否可加入购物车
            Course.objects.get(is_show=True, is_delete=False, id=course_id)
        except Course.DoesNotExist:
            return Response({"message": "您添加课程不存在"}, status=status.HTTP_400_BAD_REQUEST)

        try:
        # with transaction.atomic():
            # 获取redis链接
            redis_connection = get_redis_connection("cart")

            # redis_connection.set('textname', 'Tom')

            # 使用管道操作redis
            pipeline = redis_connection.pipeline()
            # 开启管道
            pipeline.multi()
            # 将数据保存到redis 购物车商品的信息 以及 该商品对应的有效期
            # 选用哈希字典保存商品及其有效期
            pipeline.hset("cart_%s" % user_id, course_id, expire)
            # 被勾选的商品
            # 选用集合保存多个课程商品
            pipeline.sadd("selected_%s" % user_id, course_id)

            # 执行操作，在此条语句执行后才执行保存操作
            pipeline.execute()

            # 获取购物车商品总数量
            course_len = redis_connection.hlen("cart_%s" % user_id)
        except:
            # log.error("购物储存数据失败")
            return Response({"message": "参数有误,添加购物车失败"},
                            status=status.HTTP_507_INSUFFICIENT_STORAGE)

        # 正常保存后，将当前的购物车数量传给前端
        print(64,course_len)
        return Response({
            "message": "添加课程成功",
            "cart_length": course_len
        },status=status.HTTP_201_CREATED)

    def get_list_cart(self, request):
        # 获取购物车数据
        user_id = request.query_params.get('user_id')  #前端传递 用户id
        print(75, user_id)
        redis_connection = get_redis_connection("cart")
        cart_list_bytes = redis_connection.hgetall('cart_%s' % user_id)
        select_list_bytes = redis_connection.smembers('selected_%s' % user_id)

        # 查询商品信息,存入一个新建的列表中（使用mysql）
        data = []
        for course_id_byte, expire_id_byte in cart_list_bytes.items():
            course_id = int(course_id_byte)
            expire_id = int(expire_id_byte)

            try:
                course = Course.objects.get(is_show=True, is_delete=False, pk=course_id)
            except Course.DoesNotExist:
                continue
                # 将购物车所需的信息返回
            data.append({
                "selected": True if course_id_byte in select_list_bytes else False,#勾选状态
                "course_img": IMG_URL + course.course_img.url, #课程图片
                "name": course.name,    #课程名字
                "id": course.id,    #课程id
                # "price": course.discount_price,
                "price": course.price,  #课程价格
                "expire_id": expire_id,
                # "expire_list": course.expire_list,
                # "final_price": ""  # 根据有效期价格计算出的最终价格
            })
        print(data,103)
        return Response(data)


class CartItemViewSet(ViewSet):
    # 验证用户是否合法
    # permission_classes = [IsAuthenticated,]

    def create_set(self, request):
        try:
            user_id =request.data.get('user_id')
            course_id =request.data.get('course_id')
            # print(113,user_id)
            # print(114,course_id)
            # 获取redis链接对象
            redis_connection = get_redis_connection('cart')
            # 将course_id加入set集合中
            redis_connection.sadd("selected_%s" % user_id, course_id)

            return Response({
                'message':'勾选成功'
            },status=status.HTTP_201_CREATED)
        except:
            return Response({
                'message':'勾选失败'
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete_set(self, request):
        try:
            user_id = request.query_params.get('user_id')
            course_id = request.query_params.get('course_id')
            # print(134,user_id)
            # print(135,course_id)
            # 获取redis链接对象
            redis_connection = get_redis_connection('cart')
            # # 将course_id从set集合中删除
            redis_connection.srem("selected_%s" % user_id, course_id)
            return Response({
                'message': '取消勾选成功'
            }, status=status.HTTP_200_OK)
        except:
            return Response({
                'message': '取消勾选失败'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CartCourseViewSet(ViewSet):
    # 验证用户是否合法
    # permission_classes = [IsAuthenticated,]

    def delete_course(self, request):
        try:
            user_id = request.query_params.get('user_id')
            course_id = request.query_params.get('course_id')
            print(156,user_id)
            print(157,course_id)
            # 获取redis链接对象
            redis_connection = get_redis_connection('cart')
            # # 将course_id从set集合中删除
            redis_connection.srem("selected_%s" % user_id, course_id)
            # # 将course_id从hash中删除
            redis_connection.hdel("cart_%s" % user_id, course_id)
            return Response({
                'message': '删除购物车课程成功'
            }, status=status.HTTP_200_OK)
        except:
            return Response({
                'message': '删除购物车课程失败'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
