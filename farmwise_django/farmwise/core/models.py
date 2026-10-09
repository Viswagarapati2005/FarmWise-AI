from django.db import models

class District(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=50, default='Andhra Pradesh')
    top_crop = models.CharField(max_length=200)
    avg_yield = models.CharField(max_length=50)
    active_farmers = models.IntegerField(default=0)
    common_pest = models.CharField(max_length=200)
    review_count = models.IntegerField(default=0)
    crop_density = models.CharField(max_length=10, choices=[('high','High'),('medium','Medium'),('low','Low')], default='medium')

    def __str__(self):
        return self.name


class Crop(models.Model):
    SEASON_CHOICES = [('kharif','Kharif'),('rabi','Rabi'),('summer','Summer')]
    name = models.CharField(max_length=100)
    variety = models.CharField(max_length=100)
    season = models.CharField(max_length=10, choices=SEASON_CHOICES)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=4.0)
    review_count = models.IntegerField(default=0)
    water_need = models.CharField(max_length=10, choices=[('low','Low'),('medium','Medium'),('high','High')], default='medium')
    temp_min = models.IntegerField(default=20)
    temp_max = models.IntegerField(default=35)
    rainfall_min = models.IntegerField(default=500)
    rainfall_max = models.IntegerField(default=1000)
    humidity_min = models.IntegerField(default=50)
    humidity_max = models.IntegerField(default=75)
    growing_period = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.variety})"


class CropReview(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE, related_name='reviews')
    farmer_name = models.CharField(max_length=100)
    farmer_initials = models.CharField(max_length=3)
    location = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
    review_text = models.TextField()
    yield_rating = models.IntegerField(default=4)
    pest_rating = models.IntegerField(default=4)
    water_rating = models.IntegerField(default=4)
    profit_rating = models.IntegerField(default=4)
    upvotes = models.IntegerField(default=0)
    tags = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    avatar_color = models.CharField(max_length=7, default='#3B6D11')

    def get_tags_list(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()]

    def __str__(self):
        return f"{self.farmer_name} - {self.crop.name}"


class PestAlert(models.Model):
    SEV_CHOICES = [('high','High'),('medium','Medium'),('low','Low')]
    name = models.CharField(max_length=100)
    severity = models.CharField(max_length=10, choices=SEV_CHOICES)
    affected_districts = models.CharField(max_length=300)
    acres_affected = models.IntegerField(default=0)
    report_count = models.IntegerField(default=0)
    remedy = models.TextField()
    remedy_rating = models.DecimalField(max_digits=3, decimal_places=1, default=4.0)
    remedy_votes = models.IntegerField(default=0)
    severity_pct = models.IntegerField(default=50)

    def __str__(self):
        return self.name


class ForumPost(models.Model):
    question = models.TextField()
    author_name = models.CharField(max_length=100)
    author_role = models.CharField(max_length=100)
    badge_type = models.CharField(max_length=20, choices=[('expert','Expert'),('trusted','Trusted Advisor'),('none','None')], default='none')
    topic = models.CharField(max_length=50, default='General')
    views = models.IntegerField(default=0)
    answers = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question[:60]


class Notification(models.Model):
    TYPE_CHOICES = [('pest','Pest'),('weather','Weather'),('policy','Policy'),('reply','Reply'),('community','Community')]
    title = models.CharField(max_length=200)
    body = models.TextField()
    notif_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    is_unread = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
