class Invoice(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=[('paid', 'Paid'), ('late', 'Late')]
    )
    created_at = models.DateTimeField(auto_now_add=True)