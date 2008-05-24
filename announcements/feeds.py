from atom import Feed

from models import NewsItem


class AnnouncementsBase(Feed):
    
    # subclass and set:
    #   feed_id = "..."
    #   feed_title = "..."
    #   feed_links = [
    #     {"rel": "self", "href": "..."},
    #     {"rel": "alternate", "href": "..."},
    #   ]
    #   def item_id
    #   def item_links
    
    def items(self):
        return NewsItem.objects.order_by("-creation_date")[:10]
    
    def item_title(self, item):
        return item.title
    
    def item_content(self, item):
        return item.content
    
    def item_authors(self, item):
        return [{"name": str(item.creator)}]
    
    def item_updated(self, item):
        return item.creation_date


