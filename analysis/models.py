from django.db import models, IntegrityError
from django.contrib import admin
import datetime
from django.utils.timezone import now

# File model
class DataFile(models.Model):
    date = models.DateField(default=now)
    week = models.CharField(max_length=2, default='')
    sampleNo = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=20, default='')
    plant_len = models.FloatField(default=0)
    stem_width = models.FloatField(default=0)
    leaf_len = models.FloatField(default=0)
    leaf_width = models.FloatField(default=0)
    leaf_n = models.FloatField(default=0)
    group_blossoming = models.FloatField(default=0)
    group_fruit = models.FloatField(default=0)
    group_harvest = models.FloatField(default=0)
    ped = models.FloatField(default=0)
    light = models.FloatField(default=0)

    class Meta:
        unique_together = ('date', 'sampleNo')
        ordering  = ['date']

    def dic(self):
        fields = [
                'date', 'week', 'sampleNo', 'location', 'plant_len', 'stem_width', 'leaf_len',
                'leaf_width', 'leaf_n', 'group_blossoming', 'group_fruit', 'group_harvest', 'ped',
                'light'
        ]
        result = {}
        for field in fields:
            result[field] = self.__dict__[field]
        return result


class DataFileAdmin(admin.ModelAdmin):
    list_display = ('date', 'week', 'sampleNo', 'location', 'plant_len', 'stem_width', 'leaf_len',
                'leaf_width', 'leaf_n', 'group_blossoming', 'group_fruit', 'group_harvest', 'ped',
                'light')
    list_per_page = 30
    search_fields = ('date', 'week', 'location')

# File upload model
class fileUpload(models.Model):
    file = models.FileField()

from django.db import transaction
class SampleAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        csv_file = request.FILES['file']
        file_data = csv_file.read().decode("utf-8")
        lines = file_data.split("\n")
        count = 0
        columns = []
        for line in lines:
            if count < 1:
                count += 1
                columns = line.split(",")
                continue
            fields = [0 for i in range(len(columns))]
            field = line.split(",")
            if (len(field) > 0):
                for i in range(len(field)):
                    fields[i] = field[i]

                year = int(fields[0] if fields[0]!='' else 0)
                month = int(fields[1] if fields[1]!='' else 0)
                day = int(fields[2] if fields[2]!='' else 0)
                week = fields[3]
                sampleNo = int(fields[4] if fields[4]!='' else 0)
                location = fields[5]
                plant_len = float(fields[6] if fields[6]!='' else 0)
                stem_width = float(fields[7] if fields[7]!='' else 0)
                leaf_len = float(fields[8] if fields[8]!='' else 0)
                leaf_width = float(fields[9] if fields[9]!='' else 0)
                leaf_n = float(fields[10] if fields[10]!='' else 0)
                group_blossoming = float(fields[11] if fields[11]!='' else 0)
                group_fruit = float(fields[12] if fields[12]!='' else 0)
                group_harvest = float(fields[13] if fields[13]!='' else 0)
                ped = float(fields[14] if fields[14]!='' else 0)
                light = float(fields[15] if fields[15]!='' else 0)
                if not(year==0 and month==0 and day==0):
                    try:
                        with transaction.atomic():
                            DataFile.objects.create(
                                                    date=datetime.date(year=year, month=month, day=day),
                                                    week=week, sampleNo=sampleNo, location=location,
                                                    plant_len=plant_len, stem_width=stem_width,
                                                    leaf_len=leaf_len, leaf_width=leaf_width, leaf_n=leaf_n,
                                                    group_blossoming=group_blossoming, group_fruit=group_fruit,
                                                    group_harvest=group_harvest,
                                                    ped=ped,
                                                    light=light)
                    except IntegrityError as e:
                        pass
# file save
def save(self, *args, **kwargs):
    super(DataFile, self).save(*args, **kwargs)
    filename = self.data.url
