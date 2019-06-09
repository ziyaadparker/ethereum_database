from django.db import models

class EthereumKeys(models.Model):

    public_key = models.CharField(default='', max_length=64)
    private_key = models.CharField(default='', max_length=42)

    def __unicode__(self):
        return self.public_key
    def __repr__(self):
        return self.public_key
    def __str__(self):
        return self.public_key

    class Meta:
        db_table = "EthereumKeys"
