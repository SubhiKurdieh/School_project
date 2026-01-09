class BusLog(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10,
        choices=[('up', 'Boarded'), ('down', 'Dropped')]
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    manual_reason = models.TextField(null=True, blank=True)