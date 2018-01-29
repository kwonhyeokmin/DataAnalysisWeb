from django.db import models, IntegrityError
from django.contrib import admin
import datetime
from django.utils.timezone import now

# File model
class BaseDataFile(models.Model):
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
    fruit_n = models.IntegerField(default=0)
    group_harvest = models.FloatField(default=0)
    ped = models.FloatField(default=0)
    light = models.FloatField(default=0)

    class Meta:
        unique_together = ('date', 'sampleNo')
        ordering  = ['date']

    def dic(self):
        fields = [
                'date', 'week', 'sampleNo', 'location', 'plant_len', 'stem_width', 'leaf_len',
                'leaf_width', 'leaf_n', 'group_blossoming', 'group_fruit', 'fruit_n', 'group_harvest', 'ped',
                'light'
        ]
        result = {}
        for field in fields:
            result[field] = self.__dict__[field]
        return result

class StandardDataFile(models.Model):
    id = models.IntegerField(primary_key=True)
    plant_len_min = models.FloatField(default=0)
    plant_len_optimal = models.FloatField(default=0)
    plant_len_max = models.FloatField(default=0)

    stem_min = models.FloatField(default=0)
    stem_optimal = models.FloatField(default=0)
    stem_max = models.FloatField(default=0)

    leaf_len_min = models.FloatField(default=0)
    leaf_len_optimal = models.FloatField(default=0)
    leaf_len_max = models.FloatField(default=0)

    leaf_width_min = models.FloatField(default=0)
    leaf_width_optimal = models.FloatField(default=0)
    leaf_width_max = models.FloatField(default=0)

    leaf_n_min = models.FloatField(default=0)
    leaf_n_optimal = models.FloatField(default=0)
    leaf_n_max = models.FloatField(default=0)

    joint_interval_min = models.FloatField(default=0)
    joint_interval_optimal = models.FloatField(default=0)
    joint_interval_max = models.FloatField(default=0)

    fcluster_interval_min = models.FloatField(default=0)
    fcluster_interval_optimal = models.FloatField(default=0)
    fcluster_interval_max = models.FloatField(default=0)

    fcluster_n = models.IntegerField(default=0)


    class Meta:
        unique_together = ()
        ordering  = []

    def dic(self):
        fields = [
            'id',
            'plant_len_min', 'plant_len_optimal', 'plant_len_max',
            'stem_min', 'stem_optimal','stem_max',
            'leaf_len_min', 'leaf_len_optimal', 'leaf_len_max',
            'leaf_width_min', 'leaf_width_optimal', 'leaf_width_max',
            'leaf_n_min', 'leaf_n_optimal', 'leaf_n_max',
            'joint_interval_min', 'joint_interval_optimal', 'joint_interval_max',
            'fcluster_interval_min', 'fcluster_interval_optimal', 'fcluster_interval_max',
            'fcluster_n'
        ]
        result = {}
        for field in fields:
            result[field] = self.__dict__[field]
        return result

class InnerSensorData(models.Model):
    sensorId = models.IntegerField(default=0)
    date = models.DateField(default=now)
    time = models.IntegerField(default=0)
    inner_temp = models.FloatField(default=0)
    inner_humidity = models.FloatField(default=0)
    co2 = models.FloatField(default=0)

    class Meta:
        unique_together = ()
        ordering = []

    def dic(self):
        fields = [
            'sensorId', 'date', 'time', 'inner_temp', 'inner_humidity', 'co2'
        ]
        result = {}
        for field in fields:
            result[field] = self.__dict__[field]
        return result

class OutSensorData(models.Model):
    date = models.DateField(default=now)
    time = models.IntegerField(default=0)
    wind_direct = models.FloatField(default=0)
    wind_velocity = models.FloatField(default=0)
    rain = models.FloatField(default=0)
    solar = models.FloatField(default=0)

    class Meta:
        unique_together = ()
        ordering = []

    def dic(self):
        fields = [
            'date', 'time', 'wind_direct', 'wind_velocity', 'rain', 'solar'
        ]
        result = {}
        for field in fields:
            result[field] = self.__dict__[field]
        return result

class InvestigationData(models.Model):
    farm = models.TextField(default="")
    season = models.IntegerField(default=0)
    date = models.DateField(default=now)
    week = models.TextField(default=0)
    sampleNo = models.FloatField(default=0)
    stem_width = models.FloatField(default=0)
    plent_len = models.FloatField(default=0)
    fcluster_n = models.FloatField(default=0)

    class Meta:
        unique_together = ()
        ordering = []

    def dic(self):
        fields = [
            'farm','season', 'date', 'week', 'sampleNo', 'stem_width', 'plent_len', 'fcluster_n'
        ]
        result = {}
        for field in fields:
            result[field] = self.__dict__[field]
        return result

class StandardDataFileAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'plant_len_min', 'plant_len_optimal', 'plant_len_max',
                    'stem_min', 'stem_optimal','stem_max',
                    'leaf_len_min', 'leaf_len_optimal', 'leaf_len_max',
                    'leaf_width_min', 'leaf_width_optimal', 'leaf_width_max',
                    'leaf_n_min', 'leaf_n_optimal', 'leaf_n_max',
                    'joint_interval_min', 'joint_interval_optimal', 'joint_interval_max',
                    'fcluster_interval_min', 'fcluster_interval_optimal', 'fcluster_interval_max',
                    'fcluster_n')
    list_per_page = 30

class InnerSensorDataFileAdmin(admin.ModelAdmin):
    list_display = ('sensorId', 'date', 'time', 'inner_temp', 'inner_humidity', 'co2')
    list_per_page = 30

class OutSensorDataFileAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'wind_direct', 'wind_velocity', 'rain', 'solar')
    list_per_page = 30

class BaseDataFileAdmin(admin.ModelAdmin):
    list_display = ('date', 'week', 'sampleNo', 'location', 'plant_len', 'stem_width', 'leaf_len',
                'leaf_width', 'leaf_n', 'group_blossoming', 'group_fruit', 'fruit_n', 'group_harvest', 'ped',
                'light')
    list_per_page = 30
    search_fields = ('date', 'week', 'location')

class InvestigationDataFileAdmin(admin.ModelAdmin):
    list_display = ('farm','season', 'date', 'week', 'sampleNo', 'stem_width', 'plent_len', 'fcluster_n')
    list_per_page = 30

# File models model
class BasefileUpload(models.Model):
    file = models.FileField()

# File models model
class InnerSensorfileUpload(models.Model):
    file = models.FileField()

# File models model
class OutSensorfileUpload(models.Model):
    file = models.FileField()

# File models model
class StandardfileUpload(models.Model):
    file = models.FileField()

class InvestigationfileUpload(models.Model):
    file = models.FileField()

from django.db import transaction

class OutSensorfileUploadAdmin(admin.ModelAdmin):
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

                dates = fields[0]
                date = datetime.date(year=int(dates[:4]), month=int(dates[4:6]), day=int(dates[6:]))
                time = int(fields[1] if fields[1]!='' else 0)
                wind_direct = float(fields[1] if fields[1]!='' else 0)
                wind_velocity = float(fields[1] if fields[1]!='' else 0)
                rain = float(fields[1] if fields[1]!='' else 0)
                solar = float(fields[1] if fields[1]!='' else 0)


                try:
                    with transaction.atomic():
                        OutSensorData.objects.create(
                            date=date, time=time, wind_direct=wind_direct, wind_velocity=wind_velocity, rain=rain, solar=solar
                        )
                except IntegrityError as e:
                    pass

class InnerSensorfileUploadAdmin(admin.ModelAdmin):
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

                sensorId = int(fields[0] if fields[0]!='' else 0)
                dates = fields[1]
                date = datetime.date(year=int(dates[:4]), month=int(dates[4:6]), day=int(dates[6:]))
                time = float(fields[2] if fields[2]!='' else 0)
                inner_temp = float(fields[3] if fields[3]!='' else 0)
                inner_humidity = float(fields[4] if fields[4]!='' else 0)
                co2 = float(fields[5] if fields[5]!='' else 0)
                try:
                    with transaction.atomic():
                        InnerSensorData.objects.create(
                            sensorId=sensorId, date=date, time=time, inner_temp=inner_temp, inner_humidity=inner_humidity, co2=co2
                        )
                except IntegrityError as e:
                    pass

class StandardfileUploadAdmin(admin.ModelAdmin):
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
                id = int(fields[0] if fields[0]!='' else 0)
                plant_len_min = float(fields[1] if fields[1]!='' else 0)
                plant_len_optimal = float(fields[2] if fields[2]!='' else 0)
                plant_len_max = float(fields[3] if fields[3]!='' else 0)

                stem_min = float(fields[4] if fields[4]!='' else 0)
                stem_optimal = float(fields[5] if fields[5]!='' else 0)
                stem_max = float(fields[6] if fields[6]!='' else 0)

                leaf_len_min = float(fields[7] if fields[7]!='' else 0)
                leaf_len_optimal = float(fields[8] if fields[8]!='' else 0)
                leaf_len_max = float(fields[9] if fields[9]!='' else 0)

                leaf_width_min = float(fields[10] if fields[10]!='' else 0)
                leaf_width_optimal = float(fields[11] if fields[11]!='' else 0)
                leaf_width_max = float(fields[12] if fields[12]!='' else 0)

                leaf_n_min = float(fields[13] if fields[13]!='' else 0)
                leaf_n_optimal = float(fields[14] if fields[14]!='' else 0)
                leaf_n_max = float(fields[15] if fields[15]!='' else 0)

                joint_interval_min = float(fields[16] if fields[16]!='' else 0)
                joint_interval_optimal = float(fields[17] if fields[17]!='' else 0)
                joint_interval_max = float(fields[18] if fields[18]!='' else 0)

                fcluster_interval_min = float(fields[19] if fields[19]!='' else 0)
                fcluster_interval_optimal = float(fields[20] if fields[20]!='' else 0)
                fcluster_interval_max = float(fields[21] if fields[21]!='' else 0)

                fcluster_n = float(fields[22] if fields[22]!='' else 0)

                try:
                    with transaction.atomic():
                        StandardDataFile.objects.create(
                            id=id,
                            plant_len_min=plant_len_min, plant_len_optimal=plant_len_optimal, plant_len_max=plant_len_max,
                            stem_min=stem_min, stem_optimal=stem_optimal, stem_max=stem_max,
                            leaf_len_min=leaf_len_min, leaf_len_optimal=leaf_len_optimal, leaf_len_max=leaf_len_max,
                            leaf_width_min=leaf_width_min, leaf_width_optimal=leaf_width_optimal, leaf_width_max=leaf_width_max,
                            leaf_n_min=leaf_n_min, leaf_n_optimal=leaf_n_optimal, leaf_n_max=leaf_n_max,
                            joint_interval_min=joint_interval_min, joint_interval_optimal=joint_interval_optimal, joint_interval_max=joint_interval_max,
                            fcluster_interval_min=fcluster_interval_min, fcluster_interval_optimal=fcluster_interval_optimal, fcluster_interval_max=fcluster_interval_max,
                            fcluster_n=fcluster_n
                        )
                except IntegrityError as e:
                    pass

class BasefileUploadAdmin(admin.ModelAdmin):
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
                fruit_n = float(fields[13] if fields[13]!='' else 0)
                group_harvest = float(fields[14] if fields[14]!='' else 0)
                ped = float(fields[15] if fields[15]!='' else 0)
                light = float(fields[16] if fields[16]!='' else 0)
                if not(year==0 and month==0 and day==0):
                    try:
                        with transaction.atomic():
                            BaseDataFile.objects.create(
                                                    date=datetime.date(year=year, month=month, day=day),
                                                    week=week, sampleNo=sampleNo, location=location,
                                                    plant_len=plant_len, stem_width=stem_width,
                                                    leaf_len=leaf_len, leaf_width=leaf_width, leaf_n=leaf_n,
                                                    group_blossoming=group_blossoming, group_fruit=group_fruit, fruit_n=fruit_n,
                                                    group_harvest=group_harvest,
                                                    ped=ped,
                                                    light=light)
                    except IntegrityError as e:
                        pass

class InvestigationfileUploadAdmin(admin.ModelAdmin):
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
                farm = fields[0]
                season = int(fields[1] if fields[1] != '' else 0)
                year = int(fields[2] if fields[2] != '' else 0)
                month = int(fields[3] if fields[3] != '' else 0)
                day = int(fields[4] if fields[4] != '' else 0)

                date = datetime.date(year=year, month=month, day=day)
                week = fields[5]
                sampleNo = int(fields[6] if fields[6]!='' else 0)
                stem_width = float(fields[7] if fields[7]!='' else 0)
                plent_len = float(fields[8] if fields[8]!='' else 0)
                fcluster_n = int(fields[9] if fields[9]!='' else 0)


                try:
                    with transaction.atomic():
                        InvestigationData.objects.create(
                            farm=farm, season=season, date=date, week=week, sampleNo=sampleNo, stem_width=stem_width, plent_len=plent_len, fcluster_n=fcluster_n
                        )
                except IntegrityError as e:
                    pass
# file save
def save(self, *args, **kwargs):
    super(BaseDataFile, self).save(*args, **kwargs)
    filename = self.data.url
