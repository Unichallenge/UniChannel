from .models import Post, Tags, PostTags

def getPost(tag_name):
    id = Tags.objects.flter(tags__contain = tag_name).values('id')
    post_ids = PostTags.objects.filter(tags_id = id).values('id')
    post_list = []
    for post_id in post_ids:
        post_list.append(Post.objects.filters(id=post_id)).values('title', 'description', 'image', 'link', 'date')

    return post_list