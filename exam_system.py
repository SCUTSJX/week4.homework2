import os
import random
import student

class ExamSys:
    def __init__(self):
        students = student.Student.load_students()#列表内存储学生类
    def run(self):
        """功能1：主菜单循环"""
        print("\n====== 学生信息与考场管理系统 ======")
        print("1. 查询学生信息")
        print("2. 随机点名")
        print("3. 生成考场安排表")
        print("4. 生成准考证文件")
        print('+',"-" * 35)
        print("0. 退出系统")
        while True:
            choice = input("请输入功能编号: ").strip()
            if choice == '1':
                self.find_student()
            elif choice == '2':
                self. random_roll_call()
            elif choice == '3':
                self.generate_exam_arrangement()
            elif choice == '4':
                self.generate_admission_tickets()
            elif choice == '0':
                print("感谢使用，系统已退出。再见！")
                break
            else:
                print("功能编号不存在，请正确输入功能编号（0~4）：")
    def find_student(self):print(1)
    def random_roll_call(self):print(2)
    def generate_exam_arrangement(self):print(3)
    def generate_admission_tickets(self):print(4)
sys=ExamSys()
sys.run()