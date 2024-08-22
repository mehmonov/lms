# LMS - Learning Management System Powered by Odoo

## O'quv Markazining Avtomatlashtirish Tizimi

Ushbu tizim ikki xil rolni qo‘llab-quvvatlaydi: **Admin** va **Administrator**. Har bir rolning o‘ziga xos vazifalari va huquqlari mavjud.

### Admin

Admin rolidagi foydalanuvchilar quyidagi vazifalarni bajara olad:
- Talabalarni ro‘yxatdan o‘tkazish, o‘chirish va tahrirlash.
- Talabalarni guruhlarga qo‘shish.
- Talabalar to‘lovlarini qabul qilish va boshqarish.
- O‘qituvchilarni ro‘yxatdan o‘tkazish.
- O‘qituvchilarga oylik to‘lashni boshqarish.
- O‘qituvchilarni guruhlarga qo‘shish.
- Kurslar va guruhlar yaratish, tahrirlash va boshqarish va hokazolar

### Administrator

Administrator roli quyidagi imkoniyatlarga ega:
- Admin kabi barcha imkoniyatlar, lekin to‘lovlarni tahrirlash huquqiga ega emas.

## Moduldagi Fayllar Strukturası

Modulning fayllar strukturas:
```
├── __init__.py
├── __manifest__.py
├── models
│   ├── __init__.py
│   └── models.py
├── security
│   ├── ir.model.access.csv
│   └── security.xml
└── views
    ├── menu.xml
    ├── others.xml
    ├── payments.xml
    ├── teacher_payments.xml
    └── teachers.xml
```
- `__init__.py`: Modulni paket sifatida ishlatadigan modul.
- `__manifest__.py`: Modulning manzili va konfiguratsiyasi. Modulning asosiy fayli.
- `models/`: Ma’lumotlar modellarini.
  - `models.py`: Modellar yozilgan fayl .
- `security/`: Xavfsizlik va kirish huquqlari bilan bog‘liq fayllar.
  - `ir.model.access.csv`: Kirish huquqlari ro‘yxati.
  - `security.xml`: Xavfsizlik sozlamalari.
- `views/`: Foydalanuvchiga ko'rinishlarni tuzuvchi fayllar.
  - `menu.xml`: Menu sozlamalari.
  - `others.xml`: Boshqa ko‘rinishlar(Cource, Group, teacher payment).
  - `payments.xml`: To‘lovlar ko‘rinishi.
  - `teacher_payments.xml`: O‘qituvchi to‘lovlari ko‘rinishi.
  - `teachers.xml`: O‘qituvchilar  ko‘rinishi.

## Sozlamalar

Hech qanday qo'shimcha sozlamalar mavjud emas. Modullarni addons fayliga joylashtirib, odoo apps -> lms -> activate ko'rinishida o'rnatish mumkin

* Web responsive app'ni o'rnatish majburiy emas. 


:author: [Mehmonov Husniddin]
