from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxLengthValidator, MinValueValidator
# Create your models here.

class User(models.Model):
    GENDER_CHOICES = (
        (1, 'male'),
        (2, 'female'),
    )
    name = models.CharField(_('user name'),max_length=150)
    password = models.CharField(_('user password'),max_length=12)
    mobile = models.CharField(_('user mobile'),max_length=20)
    email = models.CharField(_('user email'),max_length=50)
    gender = models.IntegerField(_('gender'),choices=GENDER_CHOICES,default=1)
    birth_date = models.DateTimeField(_('user birthdate'), null=True)
    photo = models.ImageField(_('user photo'), null=True)

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.name

class Provider(models.Model):
    name = models.CharField(_('provider name'), max_length=50)
    icon = models.ImageField(_('provider icon'),null=True)

    class Meta:
        db_table = 'providers'
        verbose_name = 'Provider'
        verbose_name_plural = 'Providers'

    def __str__(self):
        return self.name


class CategoryLiveManager(models.Manager):
    def get_queryset(self):
        return super(CategoryLiveManager, self).get_queryset().filter(is_enable=True)

class Category(models.Model):
    name = models.CharField(_('category name'), max_length=50)
    parent = models.ForeignKey('self', blank=True, null=True)
    is_enable = models.BooleanField(default=False)
    objects = models.Manager()
    live = CategoryLiveManager()
    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    @classmethod
    def category_tree(cls, cat_parent=None):
        queryset = cls.live
        if cat_parent is None:
            queryset = queryset.filter(parent__isnull=True)
        else:
            queryset = queryset.filter(parent=cat_parent)
        queryset = queryset.order_by("name")
        # print(queryset.query)

        cat_list = []
        for cat in queryset:
            cat_dict = {wk: getattr(cat, wk) for wk in ['id', 'name']}
            cat_dict["subs"] = cls.category_tree(cat_dict["id"])
            cat_list.append(cat_dict)
        return cat_list

class Package(models.Model):
    LEVEL_CHOICES = (
        (1, 'beginer'),
        (2, 'very easy'),
        (3, 'easy'),
        (4, 'hard'),
        (5, 'very hard'),
    )
    name = models.CharField(_('Package name'), max_length=150)
    photo = models.ImageField(_('Package photo'), blank=True)
    price = models.IntegerField(_('Package price'), default=0)
    discount = models.IntegerField(_('Package name'), default=0)
    category = models.ManyToManyField(Category)
    provider = models.ForeignKey(Provider, verbose_name=_('Provider'),null=True)
    description = models.TextField(_('Package description'), blank=True)
    level = models.IntegerField(_('Package level'), choices=LEVEL_CHOICES,default=1)
    is_enable = models.BooleanField(_('Package enable'), default=False)
    class Meta:
        db_table = 'packages'
        verbose_name = 'Package'
        verbose_name_plural = 'Packages'

    def __str__(self):
        return self.name

class Comment(models.Model):
    RATE_CHOICES = (
        (1, '1 star'),
        (2, '2 star'),
        (3, '3 star'),
        (4, '4 star'),
        (5, '5 star'),
    )
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    package = models.ForeignKey(Package)
    user = models.ForeignKey(User)
    rate = models.IntegerField(choices=RATE_CHOICES,default=1)
    is_moderated = models.BooleanField(default=False)
    #TODO change choice to min and max
    class Meta:
        db_table = 'comments'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.text


class Lesson(models.Model):
    ORDER_CHOICES = (
        (1, 'order 1'),
        (2, 'order 2'),
        (3, 'order 3'),
        (4, 'order 4'),
        (5, 'order 5'),
    )
    name = models.CharField(_('lesson name'), max_length=150)
    package = models.ForeignKey(Package)
    order = models.IntegerField(choices=ORDER_CHOICES,default=1)
    #TODO change choice to min and max in lesson
    class Meta:
        db_table = 'lessons'
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'

    def __str__(self):
        return self.name

class Card(models.Model):
    title = models.CharField(_('card title'), max_length=150)
    description = models.TextField(_('card description'))
    additonal_info = models.CharField(_('card additonal_info'), max_length=50)
    hard_ship = models.CharField(_('card hard_ship'), max_length=50)
    lesson = models.ForeignKey(Lesson, default=1)
    #TODO question about hard_ship and additional_info
    class Meta:
        db_table = 'cards'
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'

    def __str__(self):
        return self.title

class UserPackage(models.Model):
    user = models.ForeignKey(User)
    package = models.ForeignKey(Package)
    price = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    finish_time = models.DateTimeField(null=True)
    is_archive = models.BooleanField(default=False)

    class Meta:
        db_table = 'user_packages'
        verbose_name = 'UserPackage'
        verbose_name_plural = 'userpackages'

    def __str__(self):
        return '%s - %s ' % (self.user,self.package)

class CardState(models.Model):
    # TODO: add state max and min
    card = models.ForeignKey(Card)
    user = models.ForeignKey(User)
    last_view_time = models.DateTimeField(auto_now_add=True)
    state = models.IntegerField()

    class Meta:
        db_table = 'card_states'
        verbose_name = 'Card_State'
        verbose_name_plural = 'Card_States'

    def __str__(self):
        pass

class CardLog(models.Model):
    card_state = models.ForeignKey(CardState)
    log_time = models.DateTimeField(auto_now_add=True)
    answer_state = models.BooleanField()

    class Meta:
        db_table = 'card_logs'
        verbose_name = 'Card_Log'
        verbose_name_plural = 'Card_Logs'

    def __str__(self):
        pass

class CardMedia(models.Model):
    TYPE_CHOICES = (
        (1, 'text'),
        (2, 'image'),
        (3, 'sound'),
        (4, 'video'),
    )
    card = models.ForeignKey(Card)
    media_type = models.IntegerField(choices=TYPE_CHOICES)
    content = models.CharField(max_length=250)

    class Meta:
        db_table = 'card_informations'
        verbose_name = 'Information_Card'
        verbose_name_plural = 'Information_Cards'

    def __str__(self):
        pass
