from django.contrib import admin
from blog.models import Post
from payment.models import TransactionResult,Transaction

admin.site.register(Post)
admin.site.register(Transaction)
admin.site.register(TransactionResult)


