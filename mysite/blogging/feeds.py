from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post

class LatestPostsFeed(Feed):
    title = "Blog post site feed"
    link = "/"
    description = "List of recent posts."

    def items(self):
        return Post.objects.order_by('-published_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    # item_link is only needed if Post has no get_absolute_url method.
    def item_link(self, item):
        return reverse('blog_detail', args=[item.pk])
