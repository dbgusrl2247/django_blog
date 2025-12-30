from django.shortcuts import render
import feedparser

# ✅ 원하면 RSS 소스는 여기서 바꾸면 됨
RSS_SOURCES = [
    # Hacker News Front Page (공식 RSS)
    ("Hacker News", "https://hnrss.org/frontpage"),
    # Reddit r/programming (RSS)
    ("r/programming", "https://www.reddit.com/r/programming/.rss"),
    # Dev.to Top (RSS)
    ("Dev.to", "https://dev.to/feed"),
]

def home(request):
    news_items = []

    # 여러 RSS에서 최신 글 조금씩 섞어오기
    for source_name, url in RSS_SOURCES:
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:5]:  # 소스당 5개
                news_items.append({
                    "source": source_name,
                    "title": getattr(entry, "title", "(no title)"),
                    "link": getattr(entry, "link", "#"),
                    "published": getattr(entry, "published", ""),
                })
        except Exception:
            # 피드 하나가 실패해도 메인페이지가 터지지 않게 무시
            continue

    # 간단 정렬(발행일 문자열이 제각각이라 완벽하진 않지만 OK)
    news_items = news_items[:12]  # 전체 12개만 표시

    return render(request, "pages/home.html", {"news_items": news_items})

def about(request):
    return render(request, "pages/about.html")

def contact(request):
    return render(request, "pages/contact.html")
