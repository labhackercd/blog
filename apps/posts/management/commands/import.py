from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import csv

from django_comments.models import Comment

from apps.posts.models import Post


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('media/csv/users.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                user = User()
                user.id = int(row['ID'])
                user.username = row['user_login']
                user.email = row['user_email']
                user.date_joined = row['user_registered']
                user.first_name = row['display_name'].split(' ')[0]
                user.last_name = row['display_name'].split(' ')[-1]
                user.save()
        with open('media/csv/posts.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                post = Post()
                post.id = int(row['ID'])
                post.title = row['post_title']
                post.content = row['post_content']
                post.published_at = row['post_date']
                post.slug = row['post_name']
                post.user_id = row['post_author']
                post.save()
        with open('media/csv/comments.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                comment = Comment()
                comment.id = int(row['comment_ID'])
                comment.object_pk = row['comment_post_ID']
                comment.content_type_id = 15
                comment.site_id = 1
                comment.user_name = row['comment_author']
                comment.user_email = row['comment_author_email']
                comment.user_url = row['comment_author_url']
                comment.ip_address = row['comment_author_IP']
                comment.submit_date = row['comment_date']
                comment.comment = row['comment_content']
                if row['comment_content'] != '0':
                    comment.user_id = row['user_id']
                comment.save()


