import os
import random
import student

class ExamSys:
    def __init__(self):
            self.students = student.Student.load_students()#属性为student类，并且加载文件内容

    def run(self):
        print("\n====== 学生信息与考场管理系统 ======")
        print("1. 查询学生信息")
        print("2. 随机点名")
        print("3. 生成考场安排表")
        print("4. 生成准考证文件")
        print('+',"-" * 35)
        print("0. 退出系统")
        while True:
            try:
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
            except Exception as e:print(f"菜单操作出现异常：{e}")

    def find_student(self):
        search_id = input("请输入要查询的学号: ").strip()
        found = False#标记是否找到了学号
        for stu in self.students:
            if stu.student_id == search_id:#打印详细信息
                print("\n查询结果：")
                print(f"序号: {stu.id}  姓名: {stu.name}  性别: {stu.gender}  班级: {stu.class_id}  学号: {stu.student_id}  学院: {stu.college}")
                found = True#改变found的值
                break
        if not found:
            print(f"未找到该学号对应的学生，请检查输入是否正确。")
    def random_roll_call(self):
        total_students = len(self.students)
        if total_students == 0:
            print("当前没有学生数据，无法进行点名。")
            return
        while True:#允许失败后多次点名
            user_input = input(f"请输入需要点名的学生数量（共 {total_students} 名学生）：")
            try:
                num = int(user_input)
                if num <= 0:
                    print("[输入错误] 点名人数必须大于 0。")
                    continue
                elif num > total_students:
                    print(f"[输入错误] 点名人数 ({num}) 超过学生总人数 ({total_students})，请重新输入。")
                    continue
                selected_students = random.sample(self.students, num)#sample函数从student列表内抽取num个
                print("\n本次随机点名结果：")
                for i, stu in enumerate(selected_students, start=1):
                    print(f"{i}. {stu.name} {stu.student_id}")

                break#点名成功后回到主界面
            except ValueError:
                print(f"[输入错误] 请输入整数类型的数据并且小于等于10'{user_input}'")
    def generate_exam_arrangement(self):
        if not self.students:
            print("当前没有学生数据，无法生成安排表。")#查询属性student是否存在，不存在不会生成文件占用空间
            return
        temp_students = self.students[:]#保存临时列表，以免shuffle的时候把自身属性改变
        random.shuffle(temp_students)#打乱学生列表
        filename = "考场安排表.txt"#设定变量名
        try:#防止异常崩溃
            with open(filename, "w", encoding="utf-8") as f:#打开filename同名文件，如果没有就创建，使用utf8防止中文乱码
                for seat_num, stu in enumerate(temp_students, 1):#使用enumerate迭代产生带有索引序号的元组，并且创建临时的student类stu
                    if not hasattr(stu, 'name') or not hasattr(stu, 'student_id'):#使用hasattr检查是否有属性
                        print(f"[警告] 跳过一名属性不全的学生数据。")
                        continue
                    line = f"{seat_num},{stu.name},{stu.student_id}\n"#将索引seatnum和迭代的变量stu化为字符串
                    f.write(line)#写入字符串
            print(f"成功生成考场安排表：{filename}")
        except Exception as e:#返回异常原因
            print(f"生成文件时发生错误：{e}")
    @staticmethod
    def generate_admission_tickets():
        folder_name = "准考证"
        os.makedirs(folder_name, exist_ok=True)#检查是否已经创建准考证文件夹，makedirs不允许重复创建/覆盖录入
        try:
            with open("考场安排表.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("错误：找不到【考场安排表.txt】，请先按3生成考场安排表！")
            return
        if not lines:#防止整个文件内容为空
            print("错误：考场安排表为空，无法生成准考证！")
            return
        print("正在生成准考证...")
        for i, line in enumerate(lines):#让
            line = line.strip()#去除空白
            if not line:#保障每一行不要有空信息
                continue
            parts = line.split(',')#分割信息为列表
            if len(parts) != 3:#防止改动考场安排格式
                print(f"[警告] 第 {i + 1} 行数据格式错误，已跳过：{line}")
                continue
            seat_num, name, student_id = parts[0], parts[1], parts[2]#将parts列表的信息赋值给临时变量
            filename = f"{i + 1:02d}.txt"
            filepath = os.path.join(folder_name, filename)
            try:
                with open(filepath, "w", encoding="utf-8") as f:#如果没有就创建
                    f.write(f"考场座位号:{seat_num}\n")#登记信息
                    f.write(f"姓名:{name}\n")
                    f.write(f"学号:{student_id}\n")
            except Exception as e:
                print(f"生成文件 {filename} 时发生错误：{e}")

        print("准考证生成完毕！")

