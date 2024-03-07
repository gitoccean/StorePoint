from django.db import models


# Create your models here.


class db_Product(models.Model):
    db_Product_ID = models.CharField(max_length=100)
    db_Product_Name = models.TextField(max_length=255)
    db_Product_Type = models.TextField(max_length=255)
    db_Product_Category = models.TextField(max_length=255)
    db_Product_Price = models.IntegerField()
    db_Product_status = models.TextField(max_length=255)
    db_Product_Brand = models.TextField(max_length=255)
    db_Product_Size = models.TextField(max_length=255)
    db_Product_Freshnes = models.TextField(max_length=255)
    db_Product_MadeByCountry = models.TextField(max_length=255)
    db_Product_Condition = models.TextField(max_length=255)
    db_Product_Description = models.TextField(max_length=255)
    db_Product_QR_Code = models.TextField(max_length=255)
    db_Product_IssueDate = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return self.__all__
        return str(self.id) + ',' + str(self.db_Product_Category) + ',' + str(self.db_Product_ID) + ',' + str(
            self.db_Product_Name) + ',' + str(self.db_Product_Type)

    def get_user_by_email(Product_ID):
        try:
            return db_Product.objects.get(db_Product_ID=Product_ID)
        except:
            return False

    def isExists(self):
        if db_Product.objects.filter(db_Product_ID=self.db_Product_ID):
            return True
        return False


class db_Mobile(models.Model):
    db_Mobile_ID = models.CharField(max_length=100)
    db_Mobile_Store_RAM = models.TextField(max_length=255)
    db_Mobile_Store_ROM = models.TextField(max_length=255)
    db_Mobile_OS = models.TextField(max_length=255)
    db_Mobile_Camera = models.TextField(max_length=255)
    db_Mobile_Color = models.TextField(max_length=255)
    db_Mobile_BatteryTiming = models.TextField(max_length=255)
    db_Mobile_Card = models.TextField(max_length=255)
    db_Mobile_Charger = models.TextField(max_length=255)
    db_Mobile_Resolution = models.TextField(max_length=255)
    db_Mobile_Extra = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ',' + str(self.db_Mobile_ID) + ',' + str(self.db_Mobile_Store_ROM) + "," + str(
            self.db_Mobile_Store_RAM)

    def get_user_by_email(Mobile_ID):
        try:
            return db_Mobile.objects.get(db_Mobile_ID=Mobile_ID)
        except:
            return False

    def isExists(self):
        if db_Mobile.objects.filter(db_Mobile_ID=self.db_Mobile_ID):
            return True
        return False


class db_Computer(models.Model):
    db_Computer_ID = models.CharField(max_length=100)
    db_Computer_Store_RAM = models.TextField(max_length=255)
    db_Computer_Store_ROM = models.TextField(max_length=255)
    db_Computer_OS = models.TextField(max_length=255)
    db_Computer_Camera = models.TextField(max_length=255)
    db_Computer_Color = models.TextField(max_length=255)
    db_Computer_BatteryTiming = models.TextField(max_length=255)
    db_Computer_Card = models.TextField(max_length=255)
    db_Computer_Charger = models.TextField(max_length=255)
    db_Computer_Resolution = models.TextField(max_length=255)
    db_Computer_Extra = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    db_photo = models.ImageField(upload_to='media/computer/', width_field=None, height_field=None, max_length=255,
                                 blank=True)

    # db_Mobile_ID = models.ForeignKey(db_Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ',' + str(self.db_Computer_ID) + ',' + str(self.db_Computer_Store_RAM) + ',' + str(
            self.db_Computer_Store_ROM)

    def get_user_by_email(Comuter_ID):
        try:
            return db_Computer.objects.get(db_Computer_ID=Comuter_ID)
        except:
            return False

    def isExists(self):
        if db_Computer.objects.filter(db_Computer_ID=self.db_Computer_ID):
            return True
        return False


class db_Shoes(models.Model):
    db_Shoes_ID = models.CharField(max_length=100)
    db_Shoes_Color = models.TextField(max_length=255)
    db_Shoes_GenderBase = models.TextField(max_length=255)
    db_Shoes_AgeBase = models.TextField(max_length=255)
    db_Shoes_Extra = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ',' + str(self.db_Shoes_ID)

    def get_user_by_ID(Shoes_ID):
        try:
            return db_Shoes.objects.get(db_Shoes_ID=Shoes_ID)
        except:
            return False

    def isExists(self):
        if db_Shoes.objects.filter(db_Shoes_ID=self.db_Shoes_ID):
            return True
        return False


class db_Cloth(models.Model):
    db_Cloth_ID = models.CharField(max_length=100)
    db_Cloth_Color = models.TextField(max_length=255)
    db_Cloth_GenderBase = models.TextField(max_length=255)
    db_Cloth_AgeBase = models.TextField(max_length=255)
    db_Cloth_Extra = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ',' + str(self.db_Cloth_ID)

    def get_user_by_ID(Cloth_ID):
        try:
            db_Cloth.objects.get(db_Cloth_ID=Cloth_ID)
        except:
            False

    def isExists(self):
        if db_Cloth.objects.filter(db_Cloth_ID=self.db_Cloth_ID):
            return True
        return False


class db_Watch(models.Model):
    db_Watch_ID = models.CharField(max_length=100)
    db_Watch_Color = models.TextField(max_length=255)
    db_Watch_GenderBase = models.TextField(max_length=255)
    db_Watch_AgeBase = models.TextField(max_length=255)
    db_Watch_Extra = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ',' + str(self.db_Watch_ID)

    def get_user_by_ID(Watch_ID):
        try:
            db_Watch.objects.get(db_Watch_ID=Watch_ID)
        except:
            return False

    def isExists(self):
        if db_Watch.objects.filter(db_Watch_ID=self.db_Watch_ID):
            return True
        return False


class db_TV(models.Model):
    db_TV_ID = models.CharField(max_length=100)
    db_TV_Inches = models.TextField(max_length=255)
    db_TV_Color = models.TextField(max_length=255)
    db_TV_Resolution = models.TextField(max_length=255)
    db_TV_Extra = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ',' + str(self.db_TV_ID)

    def get_user_by_ID(TV_ID):
        try:
            db_TV.objects.get(db_TV_ID=TV_ID)
        except:
            return False

    def isExists(self):
        if db_TV.objects.filter(db_TV_ID=self.db_TV_ID):
            return True
        return False


class db_Product_Image(models.Model):
    db_Image_ID = models.CharField(max_length=100)
    db_Product_photo = models.ImageField(upload_to='Product/', width_field=None, height_field=None, max_length=255,
                                         blank=True)
    list1_img = models.ImageField(upload_to='Product/', width_field=None, height_field=None, max_length=255, blank=True)
    list2_img = models.ImageField(upload_to='Product/', width_field=None, height_field=None, max_length=255, blank=True)
    list3_img = models.ImageField(upload_to='Product/', width_field=None, height_field=None, max_length=255, blank=True)
    list4_img = models.ImageField(upload_to='Product/', width_field=None, height_field=None, max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ',' + str(self.db_Image_ID)

    def get_user_by_ID(Image_ID):
        try:
            db_Product_Image.objects.get(db_Image_ID=Image_ID)
        except:
            return False

    def isExists(self):
        if db_Product_Image.objects.filter(db_Image_ID=self.db_Image_ID):
            return True
        return False


class db_Product_Order(models.Model):
    db_Order_ID = models.CharField(max_length=100)
    db_Order_Email = models.EmailField(max_length=255, blank=True)
    db_Order_Quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ',' + str(self.db_Order_ID) + ',' + str(self.db_Order_Email)

    def get_user_by_ID(Order_ID):
        try:
            return db_Product_Order.objects.get(db_Order_ID=Order_ID)
        except:
            return False

    def isExists(self):
        if db_Product_Order.objects.filter(db_Order_ID=self.db_Order_ID):
            return True
        return False


class db_Place_Order(models.Model):
    product_id_order = models.CharField(max_length=100)
    email_user = models.EmailField(blank=True)
    email_order = models.EmailField(blank=True)
    fname_order = models.TextField(max_length=100)
    lname_order = models.TextField(max_length=100)
    company_name_order = models.TextField(max_length=100)
    country_order = models.TextField(max_length=100)
    street_address_order = models.TextField(max_length=100)
    appartment_order = models.TextField(max_length=100)
    city_address_order = models.TextField(max_length=100)
    state_order = models.TextField(max_length=100)
    phone_order = models.IntegerField()
    postCode_order = models.IntegerField()
    cash_on = models.IntegerField()


    status_order = models.TextField(max_length=100)  # (Passed/Pending/on_way/Cancel)
    price_order = models.IntegerField()
    quantity_order = models.IntegerField()

    card_number = models.CharField(max_length=100)
    card_Holder_name = models.CharField(max_length=100)
    card_expDate = models.CharField(max_length=100)
    card_ccv = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ',' + str(self.product_id_order) + ',' + str(self.email_order) + ',' + str(
            self.fname_order) + ',' + str(self.lname_order)

    def get_user_by_ID(order_ID):
        try:
            db_Place_Order.objects.get(product_id_order=order_ID)
        except:
            return False

    def isExists(self):
        if db_Place_Order.objects.filter(product_id_order=self.product_id_order):
            return True
        return False


class db_Accessories(models.Model):
    db_Access_ID = models.CharField(max_length=100)
    db_Access_UseFor = models.TextField(max_length=255)
    db_Access_Category = models.TextField(max_length=255)
    db_Access_GenderBase = models.TextField(max_length=255)
    db_Access_AgeBase = models.TextField(max_length=255)
    db_Access_Color = models.TextField(max_length=255)
    db_Access_Extra = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ',' + str(self.db_Access_ID)

    def get_user_by_ID(Access_ID):
        try:
            db_Accessories.objects.get(db_Access_ID=Access_ID)
        except:
            return False

    def isExists(self):
        if db_Accessories.objects.filter(db_Access_ID=self.db_Access_ID):
            return True
        return False


class db_Wishlist(models.Model):
    db_Wishlist_ID = models.CharField(max_length=100)
    db_Wishlist_Email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ',' + str(self.db_Wishlist_ID) + ',' + str(self.db_Wishlist_Email)

    def get_user_by_ID(Wishlist_ID):
        try:
            db_Wishlist.objects.get(db_Wishlist_ID=Wishlist_ID)
        except:
            return False

    def isExists(self):
        if db_Wishlist.objects.filter(db_Wishlist_ID=self.db_Wishlist_ID):
            return True
        return False


class db_Review(models.Model):
    db_Review_ID = models.CharField(max_length=100)
    db_Review_Email = models.EmailField(blank=True)
    db_Review_Text = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ',' + str(self.db_Review_ID) + ',' + str(self.db_Review_Email)

    def get_user_by_ID(Review_ID):
        try:
            db_Review.objects.get(db_Review_ID=Review_ID)
        except:
            return False

    @property
    def total_Review(self):
        sum = 0
        sum = sum + self.db_Review_Text
        return sum

    def isExists(self):
        if db_Review.objects.filter(db_Review_ID=self.db_Review_ID):
            return True
        return False


class db_Message_Admin(models.Model):
    db_Message_Sender = models.CharField(max_length=100)
    db_Message_Reciever = models.CharField(max_length=100)
    db_Messsage_Email = models.EmailField(blank=True)
    db_Message_Text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ',' + str(self.db_Message_Sender) + ',' + str(self.db_Message_Reciever)

    def get_user_by_ID(Message_ID):
        try:
            db_Message_Admin.objects.get(db_Message_Sender=Message_ID)
        except:
            return False

    def isExists(self):
        if db_Message_Admin.objects.filter(db_Message_Sender=self.db_Message_Sender):
            return True
        return False


class db_Comment(models.Model):
    db_Comment_ID = models.CharField(max_length=100)
    db_Comment_Sender = models.CharField(max_length=100)
    db_Comment_Text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ',' + str(self.db_Comment_ID) + str(self.db_Comment_Sender)

    def get_user_by_ID(Comment_ID):
        try:
            db_Comment.objects.get(db_Comment_ID=Comment_ID)
        except:
            return False

    def isExists(self):
        if db_Comment.objects.filter(db_Comment_ID=self.db_Comment_ID):
            return True
        return False
