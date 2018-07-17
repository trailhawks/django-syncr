from django.contrib import admin

from syncr.flickr.models import Photo, FavoriteList, PhotoSet, PhotoComment


def set_active_to_true(modeladmin, request, queryset):
    queryset.update(active=True)


def set_active_to_false(modeladmin, request, queryset):
    queryset.update(active=False)


def set_active_to_null(modeladmin, request, queryset):
    queryset.update(active=None)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    date_hierarchy = 'taken_date'
    list_display = ('flickr_id', 'title',  'active', 'owner', 'taken_date')
    list_display_links = ('title', 'flickr_id')
    list_filter = ('upload_date', 'taken_date', 'active')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'description']
    actions = [
        set_active_to_true,
        set_active_to_false,
        set_active_to_null,
    ]


@admin.register(FavoriteList)
class FavoriteListAdmin(admin.ModelAdmin):
    list_display = ('owner', 'sync_date', 'numPhotos')
    raw_id_fields = ['primary']


@admin.register(PhotoSet)
class PhotoSetAdmin(admin.ModelAdmin):
    list_display = ('title', 'flickr_id', 'owner')
    list_display_links = ('title',)
    list_select_related = True  # ``get_primary_photo`` uses a ForeignKey


@admin.register(PhotoComment)
class PhotoCommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    list_display = ('author', 'photo', 'get_short_comment', 'pub_date')
    list_display_links = ('author',)
    ordering = ('-pub_date',)
    search_fields = ['comment', 'author', 'photo__title']
    raw_id_fields = ['photo']
