# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
class Student(models.Model):
    _name = 'learning.center.student'
    _description = 'Student'

    name = fields.Char(string='Full Name', required=True)
    birth_date = fields.Date(string='Date of Birth')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone', required=True)
    address = fields.Char(string='Address')
    course_ids = fields.Many2many('learning.center.course', string='Courses')
    payment_ids = fields.One2many('learning.center.payment', 'student_id', string='Payments')
    register_time = fields.Datetime(string='Register Time', default=fields.Datetime.now)
    
class Teacher(models.Model):
    _name = 'learning.center.teacher'
    _description = 'Teacher'

    name = fields.Char(string='Full Name', required=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    groups_ids = fields.One2many('learning.center.group', 'teacher_id', string='Groups')  # Teacher's courses


class Course(models.Model):
    _name = 'learning.center.course'
    _description = 'Course'

    name = fields.Char(string='Course Name', required=True)
    description = fields.Text(string='Description')
    group_ids = fields.One2many('learning.center.group', 'course_id', string='Groups')
    price = fields.Float(string='Price', required=True)

class Day(models.Model):
    _name = 'learning.center.day'
    _description = 'Day'



    name = fields.Selection([
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ], string='Day', required=True, unique=True)

    
class Group(models.Model):
    _name = 'learning.center.group'
    _description = 'Group'

    name = fields.Char(string='Group Name', required=True)
    course_id = fields.Many2one('learning.center.course', string='Course', required=True)
    student_ids = fields.Many2many('learning.center.student', string='Students')
    teacher_id = fields.Many2one('learning.center.teacher', string='Teacher',required=True)
    
    days_ids = fields.Many2many('learning.center.day', string='Days')    
    start_date = fields.Date(string='Start Date', required=True)
    
    end_date = fields.Date(string='End Date')
    custom_price = fields.Float(string='Custom Price', required=False)
    
    
    @api.model
    def create(self, vals):
        if vals['custom_price'] is None:
            course = self.env['learning.center.course'].browse(vals['course_id'])
            vals['custom_price'] = course.price
        return super(Group, self).create(vals)

class Payment(models.Model):
    _name = 'learning.center.payment'
    _description = 'Payment'
    student_id = fields.Many2one('learning.center.student', string='Student', required=True)
    date = fields.Date(string='Payment Date', required=True)
    amount = fields.Float(string='Amount', required=True)
    status = fields.Selection([('pending', 'Pending'), ('paid', 'Paid')], string='Status', default='pending')
    admin_id = fields.Many2one('res.users', string='Admin', readonly=True)
    note = fields.Text(string='Note')
    
    @api.constrains('amount')
    def _check_amount(self):
        if self.amount <= 0:
            raise ValidationError('Amount must be greater than 0')

    @api.constrains('date')
    def _check_date(self):
        if self.date > fields.Date.today():
            raise ValidationError('Payment date cannot be in the future')   
    
    @api.model
    def create(self, vals):
        if 'admin_id' not in vals:
            vals['admin_id'] = self.env.user.id
        return super(Payment, self).create(vals)
    
    

class TeacherPayment(models.Model):
    _name = 'learning.center.teacher.payment'
    _description = 'Teacher Payment'

    teacher_id = fields.Many2one('learning.center.teacher', string='Teacher', required=True)
    date = fields.Date(string='Payment Date', required=True)
    amount = fields.Float(string='Amount', required=True)
    description = fields.Text(string='Description')

    @api.constrains('amount')
    def _check_amount(self):
        if self.amount <= 0:
            raise ValidationError('Amount must be greater than 0')

    @api.constrains('date')
    def _check_date(self):
        if self.date > fields.Date.today():
            raise ValidationError('Payment date cannot be in the future')
