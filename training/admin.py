from django.contrib import admin

# Register your models here.
from .models import Provider, User, Category, Package, Lesson, Card, UserPackage
class UserPackageAdmin(admin.TabularInline):
    model = UserPackage

# class PackageCategoryAdmin(admin.TabularInline):
#     model = Package

class LessonPackageAdmin(admin.TabularInline):
    model = Lesson

class CardinAdmin(admin.TabularInline):
    model = Card

@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ("name", "icon")


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "mobile", "email", "gender", "birth_date")
    inlines = [UserPackageAdmin]
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent")
    # inlines = [PackageCategoryAdmin]


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ("name", "photo", "price", "discount", "provider", "description", "level", "is_enable")
    inlines = [LessonPackageAdmin]

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("name", "package", "order")
    inlines = [CardinAdmin]


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "additonal_info", "hard_ship", "lesson")
