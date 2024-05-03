# ReadIt
this is our first blog site with frontend

## Pagination
# Moose-Blog-Site
This is Moose simple blog site with django mvt

## Pagination Django Function-based-view(FBV)
Function-based view (FBV) uchun pagination kodi yozish uchun quyidagi misolni ko'rib chiqamiz. Ushbu misolda Paginator va PageNotAnInteger bilan birlashgan holda, yozuvlar ro'yxatini sahifalarga bo'lish funksiyasi (post_list) kiritilgan.
```python
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from main.forms import CommentForm
from main.models import Article, About, Tag, Comment


def articles_page(request):
    articles = Article.objects.all().order_by('-id')
    tags = Tag.objects.all()
    paginator = Paginator(articles, 3)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    context = {'articles': articles, 'tags': tags}
    return render(request, 'blog.html', context)
```
2. Blog.html pagenation uchun kod
```html
    {% if articles.has_other_pages %}
        <ul class="pagination">
            {% if articles.has_previous %}
                <li><a href="?page=1">&lt;&lt;</a></li>
                <li><a href="?page={{ articles.previous_page_number }}">&lt;</a></li>
            {% endif %}

            {% for i in articles.paginator.page_range %}
                {% if articles.number == i %}
                    <li class="active"><span>{{ i }}</span></li>
                {% else %}
                    <li><a href="?page={{ i }}">{{ i }}</a></li>
                {% endif %}
            {% endfor %}

            {% if articles.has_next %}
                <li><a href="?page={{ articles.next_page_number }}">&gt;</a></li>
                <li><a href="?page={{ articles.paginator.num_pages }}">&gt;&gt;</a></li>
            {% endif %}
        </ul>
    {% endif %}

    <ul>
```
##-------------------------------------------------------------------------
## Djanoda models.py da ishlatiladigan Fieldlar va ularning tariflari
1. models.CharField - bu matnlar bilan ishlashda foydaliniladigan field hisobkanadi. 
Eng ko'pi bilan 255 tagacha belgi qabul qiladi. Belgi bu alifbodagi harflar, 0-9 musbat va manfiy barcha sonlar, va ascii jadvalidagi belgilar hisoblanadi.
```python
class MyModel(models.Model):
    title = models.CharField(min_length=2, max_length=255)

```
2. models.TextField - Bu katta ya'ni 255tadan oshiq belgidan iborat text, matnlar bilan ishlashda foydalanamiz.
```python
class MyModel(models.Model):
    matn = models.TextField()
```
3. DateField:
Ta'rif: DateField - sanani saqlaydi.
Misol: Yozuvlar (Post) yaratilgan sanani saqlaydi.
```python
class MyModel(models.Model):
    created_date = models.DateField(auto_now_add=True)
```
4. EmailField:
Ta'rif: EmailField - e-pochta manzilini saqlaydi.
Misol: Foydalanuvchilar (User) uchun e-pochta manzilini saqlash uchun.
```python
class MyModel(models.Model):
    email = models.EmailField()
```
5. DateTimeField:
Ta'rif: DateTimeField - sana va vaqtni saqlaydi.
Misol: Yozuvlar (Post) yaratilgan vaqt va oxirgi o'zgartirilgan vaqtni saqlaydi.
```python
class MyModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

```

6. ImageField:
Ta'rif: ImageField - rasmni saqlaydi.(svg formatdagi rasmlarni saqlamaydi)
Misol: Yozuvlar (Post) rasmni saqlash uchun.
```python
class MyModel(models.Model):
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
```
7. DecimalField:
Ta'rif: DecimalField - o'nlik sonlarni saqlaydi.
Misol: Maxsus narxlarni saqlash uchun.
```python
class MyModel(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
```
8. URLField:
Ta'rif: URLField - URL manzilini saqlaydi.
Misol: Sayt manzilini saqlash uchun.
```python
class Product(models.Model):
    web_link = models.URLField()
```
9. OneToOneField:
Ta'rif: OneToOneField - bir nechta ob'ektga bog'lanadi, lekin har bir ob'ekt faqatgina bitta boshqa ob'ektga ega bo'ladi.
Misol: Foydalanuvchining profiling ma'lumotlarini saqlash uchun.
```python
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Qolgan profiling ma'lumotlari haqida kodlar...
```
10. ManyToManyField:
Ta'rif: ManyToManyField - bir nechta ob'ektga bog'lanadi.
Misol: Yozuvlarga teglar (tags) ro'yxatini saqlash uchun.
```python
class Post(models.Model):
    tags = models.ManyToManyField(Tag)
    # Qolgan yozuv haqida kodlar...
```
11. ForeignKey:
Ta'rif: ForeignKey - boshqa modelga bog'langan bo'lib, uning identifikatorini saqlaydi.
Misol: Yozuvlar (Post) modeli uchun muallif (Author) modeli bilan bog'langan.
```python
class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # Qolgan yozuv haqida kodlar...
```
12. BooleanField:
Ta'rif: BooleanField - True yoki False qiymatlarini saqlaydi.
Misol: Yozuvlar qo'shganligizda (True) yoki qo'shmaganligizda (False) boolean qiymatlarni saqlaydi.
```python
class Test(models.Model):
    is_published = models.BooleanField(default=False)
```
13. FileField:
Ta'rif: FileField - Bu pdf, svg, img, png, va boshqa turdagi fayllar bilan ishlashda qo'llaniladi
```python
class Books(models.Model):
    book = models.FileField(upload_to='books')
```