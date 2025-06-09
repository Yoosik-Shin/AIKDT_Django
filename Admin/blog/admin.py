from django.contrib import admin
from django.forms import Textarea
from django.db import models

from .models import Comment, CustomUser, Post

# Register your models here.
"""
  Django Admin에서 모델을 관리하기 위한 설정 파일입니다.
  🔆 관리자 등록 방법
  1. admin.site.register(모델명)
    ✅ 커스텀 : 설정 class를 만들어서 등록할 수 있습니다.
    ✅ class XXXAdmin(설정 클래스)
    ✅ admin.site.register(모델명, XXXAdmin)

  2. @admin.register(모델명) 데코레이터 사용
"""

# 1. 방법 1: admin.site.register(모델명)
# admin.site.register()
class CustomUserAdmin(admin.ModelAdmin):
  # 출력 필드 설정
  list_display = ('username', 'nickname', 'email', 'is_staff', 'is_active')
  # 검색 필드 설정
  search_fields = ('username', 'nickname', 'email')
  # 필터링 설정
  list_filter = ('is_staff', 'is_active')


# class PostAdmin(admin.ModelAdmin):
#   # 출력 필드 설정
#   list_display = ('post_title', 'user_username', 'user_nickname', 'post_created_at', 'post_updated_at')
#   # 읽기 전용 필드 설정
#   readonly_fields = ('created_at', 'updated_at')
#
# # post ➡ user 필드에서 CustomUser 모델의 nickname을 표시하기 위한 메서드
# # ✅ 메소드 이름 : 출력 필드 이름과 동일하게 설정
#   def user_username(self, obj):
#     return obj.user.username if obj.user else 'Unknown'
#
#   def user_nickname(self, obj):
#     return obj.user.nickname if obj.user else 'Unknown'
#
#   def post_title(self, obj):
#     return obj.title[:10] + ('...' if len(obj.title) > 10 else '')
#
#   def post_created_at(self, obj):
#     return obj.created_at.strftime('%Y-%m-%d %H:%M:%S')
#
#   def post_updated_at(self, obj):
#     return obj.updated_at.strftime('%Y-%m-%d %H:%M:%S')
#
# # ✅ 출력 필드 이름 설정
#   user_username.short_description = '아이디'
#   user_nickname.short_description = '닉네임'
#   post_title.short_description = '제목'
#   post_created_at.short_description = '작성일'
#   post_updated_at.short_description = '수정일'
#
#   # 자동 슬러그 생성
#   prepopulated_fields = {"slug": ("title",)}

admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(Post, PostAdmin)
admin.site.register(Comment)


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


# -----------------------------------------------------------------
# -----------------------------------------------------------------

# 방법 2: @admin.register(모델명)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  # 출력 필드 설정
  list_display = ('is_public', 'post_title', 'user_username', 'user_nickname',
                  'post_created_at', 'post_updated_at',
                  'comments_count')
  # 읽기 전용 필드 설정
  readonly_fields = ('created_at', 'updated_at')

# post ➡ user 필드에서 CustomUser 모델의 nickname을 표시하기 위한 메서드
# ✅ 메소드 이름 : 출력 필드 이름과 동일하게 설정
  def user_username(self, obj):
    return obj.user.username if obj.user else 'Unknown'

  def user_nickname(self, obj):
    return obj.user.nickname if obj.user else 'Unknown'

  def post_title(self, obj):
    return obj.title[:10] + ('...' if len(obj.title) > 10 else '')

  def post_created_at(self, obj):
    return obj.created_at.strftime('%Y-%m-%d %H:%M:%S')

  def post_updated_at(self, obj):
    return obj.updated_at.strftime('%Y-%m-%d %H:%M:%S')

  def comments_count(self, obj):
    return obj.comments.count() if obj.comments else 0

# ✅ 출력 필드 이름 설정
  user_username.short_description = '아이디'
  user_nickname.short_description = '닉네임'
  post_title.short_description = '제목'
  post_created_at.short_description = '작성일'
  post_updated_at.short_description = '수정일'
  comments_count.short_description = '댓글 수'


  # 자동 슬러그 생성
  prepopulated_fields = {"slug": ("title",)}

  # 액션 설정
  # ✅ 정의한 액션 메소드를 actions에 추가하여
  #     관리자 페이지에서 사용할 수 있도록 합니다.
  actions = ['make_public']

  @admin.action(description='일괄 공개 처리')
  def make_public(self, request, queryset):
    queryset.update(is_public=True)

  # 위젯 커스터마이징
  formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 60})},
    }

  inlines = [CommentInline]