from background_task import background
from .models import Post, PostSource
import feedparser

from datetime import date

@background()
def read_sources():
    sources = PostSource.objects.all()

    for source in sources:
        entries = feedparser.parse(source.feed_url).entries
        all_ids = []

        for entry in entries:
            post = Post.objects.filter(external_id=entry.id).first()
            if not post:
                post = Post.objects.create(
                    external=True,
                    external_id=entry.id,
                    external_source=source,
                    published=source.auto_publish,
                )
                for tag in source.auto_tags.all():
                    post.tags.add(tag)

            all_ids.append(post.id)

            if not post.external:
                continue

            post.title=entry.title
            post.description=entry.summary
            post.link=entry.link
            post.date=date(*(entry.published_parsed[0:3]))
            post.save()

        print('Source %s updated successfully!' % (source.name))

        Post.objects \
            .filter(external_source=source) \
            .exclude(id__in=all_ids) \
            .update(published=False)