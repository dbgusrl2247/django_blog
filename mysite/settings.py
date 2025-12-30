from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ⚠️ 아래 SECRET_KEY는 예시야. 기존 프로젝트의 SECRET_KEY로 교체!
SECRET_KEY = "django-insecure-change-me"

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # 내 앱
    "blog",
    "pages",
    "notes",
    
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "mysite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        # ✅ 전역 templates 폴더 사용
        "DIRS": [BASE_DIR / "templates"],

        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "blog.context_processors.categories",
                "blog.context_processors.recent_posts",
            ],
        },
    },
]

WSGI_APPLICATION = "mysite.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "ko-kr"
TIME_ZONE = "Asia/Seoul"
USE_I18N = True
USE_TZ = True

# ✅ static 설정
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

# ✅ media 설정(이미지 업로드 대비)
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

import os
import dj_database_url

# ✅ 1) SECRET_KEY는 환경변수로 관리 (로컬은 기본값 사용)
SECRET_KEY = os.environ.get("SECRET_KEY","django-insecure-local-key")

# ✅ 2) DEBUG: 배포에서는 False가 안전함
# Render에서 환경변수(예: RENDER=true)를 넣어두고 판별하는 방식이 깔끔함
DEBUG = os.environ.get("DEBUG","False") =="True"

# ✅ 3) 허용 호스트
# 초보 단계에서는 * 로 해도 되지만, 실제 서비스는 도메인만 넣는 게 안전함
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS","*").split(",")

# ✅ 4) DATABASE_URL이 있으면(Postgres/Neon) 그걸 사용, 없으면 기본(SQLite) 사용
if os.environ.get("DATABASE_URL"):
    DATABASES["default"] = dj_database_url.parse(
        os.environ["DATABASE_URL"],
        conn_max_age=600,
        ssl_require=True,
    )

# ✅ 5) 정적파일(Static) - WhiteNoise
STATIC_URL ="static/"
STATIC_ROOT = os.path.join(BASE_DIR,"staticfiles")

MIDDLEWARE = [
"django.middleware.security.SecurityMiddleware",
"whitenoise.middleware.WhiteNoiseMiddleware",# ✅ 추가(가능하면 위쪽에)
# 나머지 미들웨어들...
] + [mw for mw in MIDDLEWARE if mw not in [
"django.middleware.security.SecurityMiddleware",
"whitenoise.middleware.WhiteNoiseMiddleware",
]]

# WhiteNoise 추천 설정(압축+캐시용)
STATICFILES_STORAGE ="whitenoise.storage.CompressedManifestStaticFilesStorage"



