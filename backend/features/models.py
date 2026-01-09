class FeatureFlag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feature = models.CharField(max_length=100)
    enabled = models.BooleanField(default=True)
    expires_at = models.DateTimeField(null=True, blank=True)