from django.db import models

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












