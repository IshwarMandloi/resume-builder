# from django.db import models
# from django.contrib.auth.models import User


# class Resume(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True) #change
#     title = models.CharField(max_length=50)
#     objective = models.TextField(max_length=400)

#     def __str__(self):
#         return str(self.title)
        

# class UserExtraFields(models.Model):
#     resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
#     user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True)
#     date_of_birth = models.DateField()
#     phone = models.IntegerField()
#     address = models.CharField(max_length=100)
#     photo = models.ImageField(upload_to='images/' ,blank=True)

#     def __str__(self):
#         return str(self.user)


# class Education(models.Model):
#     resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
#     degree_class = models.CharField(max_length=100)
#     year_of_passing = models.CharField(max_length=100)
#     percentage_or_grade = models.CharField(max_length=100)
#     university = models.CharField(max_length=100)

#     def __str__(self):
#         return str(self.resume)


# class Experience(models.Model):
#     resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     company_name = models.CharField(max_length=100)
#     duration = models.CharField(max_length=30)
#     designation = models.CharField(max_length=100)
#     role = models.CharField(max_length=1000)
#     place = models.CharField(max_length=100)

#     def __str__(self):
#         return str(self.resume)


# class Hobbies(models.Model):
#     resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
#     hobbies = models.CharField(max_length=100)

#     def __str__(self):
#         return str(self.resume)


# class Skills(models.Model):
#     resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
#     skills = models.CharField(max_length=100)

#     def __str__(self):
#         return str(self.resume)


# class Certificate(models.Model):
#     resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
#     certificate = models.CharField(max_length=100)

#     def __str__(self):
#         return str(self.resume)


# class Achievements(models.Model):
#     resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
#     achievements = models.CharField(max_length=200)

#     def __str__(self):
#         return str(self.resume)

from django.db import models
from django.contrib.auth.models import User
from .choice import COMPETENCY_CHOICES



class ChooseTemplate(models.Model):
    name = models.CharField(max_length=100, null=True,blank=True)

    def __str__(self):
        return str(self.name)


class Resume(models.Model):
    template = models.ForeignKey(ChooseTemplate, on_delete=models.CASCADE,blank=True,null=True,related_name='template') #change
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True) #change
    title = models.CharField(max_length=50)
    objective = models.TextField(max_length=200)

    def __str__(self):
        return str(self.objective)

        

class ResumeUserDetails(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/' ,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.resume)


class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,null=True)
    qualification_name = models.CharField(max_length=100)
    year_of_passing = models.CharField(max_length=100)
    percentage_or_grade = models.CharField(max_length=100)
    university = models.CharField(max_length=100)

    def __str__(self):
        return str(self.resume)


class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,null=True)
    
    company_name = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    designation = models.CharField(max_length=100)
    role = models.CharField(max_length=1000)
    place = models.CharField(max_length=100)

    def __str__(self):
        return str(self.resume)
    class Meta:
        verbose_name_plural = "Experience"
        ordering = ['-end_date', ]


class WorkSamples(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,null=True)
    project_name =models.CharField(max_length=100)
    project_link = models.CharField(max_length=100)
    technology = models.CharField(max_length=200)
    description =models.TextField(max_length=1000)
    responsibilities =models.TextField(max_length=1000)
    logo = models.ImageField(upload_to='images/logos/')
    date = models.DateField(null=True, blank=True  )


class Hobbies(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,null=True)
    hobbies = models.CharField(max_length=100)

    def __str__(self):
        return str(self.resume)


class Skills(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,null=True)
    skills = models.CharField(max_length=300)

    def __str__(self):
        return str(self.resume)


class Certificate(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,null=True)
    certificate = models.CharField(max_length=300)
    date_obtained = models.DateField(null=True, blank=True)
    def __str__(self):
        return str(self.resume)


class Achievements(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,null=True)
    achievements = models.CharField(max_length=300)

    def __str__(self):
        return str(self.resume)

class Language(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, blank=True,null=True)
    language_name = models.CharField(max_length=255, blank=True)
    competency = models.IntegerField(choices=COMPETENCY_CHOICES, null=True, blank=True)
    def __str__(self):
        return str(self.resume)
