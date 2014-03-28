from django.contrib import admin

from main.models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Poster Information", { 'fields' : ['blog_Poster']}),
        ("Post DateTime Info", {"fields" : ["blog_TimeDate"]}),
        ("Post Information", {"fields": ["blog_Project", "blog_Summary"]}),
        ("Post Content", {"fields" : ["blog_Content"]}),
                 ]
    
    list_display = ("blog_Poster", "blog_TimeDate", "blog_Project", "blog_Summary")
    
    list_filter = ["blog_Poster", "blog_TimeDate", "blog_Project"]
    
    search_fields = ["blog_Poster", "blog_Project", "blog_Summary"]
    



admin.site.register(BlogPost, BlogPostAdmin)