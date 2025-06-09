import uuid
from django.db import models

# 🔰 모델 정의 시, id(PK) - AUTO_INCREMENT 자동 생성 (따로 id컬럼을 쓸 필요 없음)
# - no(PK) - AI(auto_increment)
# - id     - UUID
class Post(models.Model):
  no = models.AutoField(primary_key=True)
  id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
  title = models.CharField(max_length=100)
  writer = models.CharField(max_length=100)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True) # 등록 시 현재 시간
  updated_at = models.DateTimeField(auto_now=True)     # 수정 시마다 갱신

  def __str__(self):
    return "{}. {} / {} / {} / {}".format(self.no, self.title, self.writer, self.content, self.created_at)