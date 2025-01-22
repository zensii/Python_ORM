from ctypes.wintypes import HPALETTE
from datetime import datetime, timedelta

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import TextField, IntegerField
from django.templatetags.tz import datetimeobject


# Create your models here.
class BaseCharacter(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        abstract = True

class Mage(BaseCharacter):
    elemental_power = models.CharField(max_length=100)
    spellbook_type = models.CharField(max_length=100)

class Assassin(BaseCharacter):
    weapon_type = models.CharField(max_length=100)
    assassination_technique = models.CharField(max_length=100)

class DemonHunter(BaseCharacter):
    weapon_type = models.CharField(max_length=100)
    demon_slaying_ability = models.CharField(max_length=100)

class TimeMage(Mage):
    time_magic_mastery = models.CharField(max_length=100)
    temporal_shift_ability = models.CharField(max_length=100)


class Necromancer(Mage):
    raise_dead_ability = models.CharField(max_length=100)

class ViperAssassin(Assassin):
    venomous_strikes_mastery = models.CharField(max_length=100)
    venomous_bite_ability = models.CharField(max_length=100)

class ShadowbladeAssassin(Assassin):
    shadowstep_ability = models.CharField(max_length=100)

class VengeanceDemonHunter(DemonHunter):
    vengeance_mastery = models.CharField(max_length=100)
    retribution_ability = models.CharField(max_length=100)

class FelbladeDemonHunter(DemonHunter):
    felblade_ability = models.CharField(max_length=100)

class UserProfile(models.Model):
    username = models.CharField(max_length=70)
    email = models.EmailField()
    bio = models.TextField(blank=True, null=True)

class Message(models.Model):
    sender = models.ForeignKey(to=UserProfile, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(to=UserProfile, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField(default=False)

    def mark_as_read(self):
        self.is_read = True

    def reply_to_message(self, reply_content: str):
        new_message = Message(
            sender=self.receiver,
            receiver=self.sender,
            content=reply_content
        )
        new_message.save()
        return new_message

    def forward_message(self, receiver: UserProfile):
        new_message = Message(
            sender=self.receiver,
            receiver=receiver,
            content=self.content
        )
        new_message.save()
        return new_message

class StudentIDField(models.PositiveIntegerField):
    def to_python(self, value):
        try:
            return int(value)
        except ValueError:
            raise ValueError("Invalid input for student ID")


    def get_prep_value(self, value):
        cleaned_value = self.to_python(value)

        if cleaned_value <= 0:
            raise ValidationError("ID cannot be less than or equal to zero")

        return cleaned_value

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = StudentIDField()


class MaskedCreditCardField(models.CharField):

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 20
        super().__init__(*args, **kwargs)

    def to_python(self, value):

        if not isinstance(value, str):
            raise ValidationError("The card number must be a string")
        if not value.isdigit():
            raise ValidationError("The card number must contain only digits")
        if len(value) != 16:
            raise ValidationError("The card number must be exactly 16 characters long")
        return value

    def get_prep_value(self, value):
        cleaned = self.to_python(value)
        last_four_digits = cleaned[(len(value)-4):]
        masked = f"****-****-****-{last_four_digits}"

        return masked

class CreditCard(models.Model):
    card_owner = models.CharField(max_length=100)
    card_number = MaskedCreditCardField(max_length=20)


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

class Room(models.Model):

    hotel = models.ForeignKey(to=Hotel, on_delete=models.CASCADE)
    number = models.CharField(max_length=100, unique=True)
    capacity = models.PositiveIntegerField()
    total_guests = models.PositiveIntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)

    def clean(self):

        if self.total_guests > self.capacity:
            raise ValidationError("Total guests are more than the capacity of the room")

    def save(self, *args, **kwargs):

        self.clean()
        super().save(*args, **kwargs)
        return f"Room {self.number} created successfully"


class BaseReservation(models.Model):

    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()


    @property
    def is_reserved(self):
        room_reserved = self.__class__.objects.filter(
            room= self.room,
            start_date__range=[self.start_date, self.end_date],
            end_date__range=[self.start_date, self.end_date]
        )

        return room_reserved.exists()

    def clean(self):
        if self.start_date >= self.end_date:
            raise ValidationError("Start date cannot be after or in the same end date")

        if self.is_reserved:
            raise ValidationError(f"Room {self.room.number} cannot be reserved")

    def reservation_period(self):
        duration = self.end_date - self.start_date
        return duration.days

    def calculate_total_cost(self):
        price = self.reservation_period() * self.room.price_per_night
        return round(price, 2)

    class Meta:
        abstract=True

class RegularReservation(BaseReservation):

    def save(self, *args, **kwargs):
        super().clean()
        super().save(*args, **kwargs)

        return f"Regular reservation for room {self.room.number}"

class SpecialReservation(BaseReservation):

    def save(self, *args, **kwargs):
        super().clean()
        super().save(*args, **kwargs)

        return f"Special reservation for room {self.room.number}"

    def extend_reservation(self, days: int):

        new_end_date = self.end_date + timedelta(days=days)
        room_reserved = self.__class__.objects.filter(
            room=self.room,
            start_date__gt=self.end_date,
            start_date__lte=new_end_date
        )

        if room_reserved.exists():
            raise ValidationError("Error during extending reservation")

        self.save()

        return f"Extended reservation for room {self.room.number} with {days} days"


