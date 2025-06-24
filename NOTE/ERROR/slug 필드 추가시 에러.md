It is impossible to add a non-nullable field 'slug' to post without specifying a default. 
This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for 
this column)
 2) Quit and manually define a default value in models.py.

---
slug라는 널(null) 허용하지 않는 필드를 post 모델에 추가하는 것은 불가능합니다.
데이터베이스에 이미 존재하는 행들에 대해 이 컬럼(slug)을 어떻게 채울지 알아야 하기 때문입니다.
해결 방법을 선택하세요:

1. 지금 임시 기본값을 제공합니다.
(null 값이 있는 모든 기존 행에 적용됨)

2. 종료하고, models.py에 기본값을 직접 지정하세요.

---
## 해결
```
  slug = models.SlugField(max_length=200, unique=True, null=True)
```

우선적으로, null 허용 지정하고 마이그레이션 후, null=False 를 변경하는 방법으로 해결!