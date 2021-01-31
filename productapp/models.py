from django.db import models

class Product(models.Model):
    Name = models.CharField(max_length=40)
    Description = models.CharField(max_length=100)
    Amount = models.IntegerField(default=0)
    Price = models.DecimalField(decimal_places=2, max_digits=4)
    Image = models.ImageField(null = True, blank= True, upload_to="images")
    Category = models.CharField(max_length=40)

    def __str__(self):
        p = "Tên sản phẩm là : " + str(self.Name) + ", Mô tả : " + str(self.Description)+ ", Số lượng" + str(self.Amount) + ", Giá : " + str(self.Price) + ", Thể loại : " + str(self.Category)

        return p