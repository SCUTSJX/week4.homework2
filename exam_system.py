import os
import random
import student

class ExamSys:
    def __init__(self):
        self.students = student.Student.load_students()#列表内存储学生类
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
    def find_student(self):
        # 1. 获取用户输入的学号
        search_id = input("请输入要查询的学号: ").strip()
        # 2. 设置一个标记，用来记录是否找到了学生
        found = False
        # 3. 遍历 self.students 列表进行查找
        for stu in self.students:
            if stu.student_id == search_id:
                #打印详细信息
                print("\n查询结果：")
                # 这里利用了你之前写的 __str__ 方法，或者你可以手动格式化打印
                print(f"序号: {stu.id}  姓名: {stu.name}  性别: {stu.gender}  班级: {stu.class_id}  学号: {stu.student_id}  学院: {stu.college}")
                found = True
                break  # 找到了就不用继续找了

        # 4. 如果循环结束后标记仍然是 False，说明没找到
        if not found:
            print(f"未找到该学号对应的学生，请检查输入是否正确。")
    def random_roll_call(self):
        """功能4：随机点名"""
        total_students = len(self.students)
        # 如果列表为空，直接提示并返回
        if total_students == 0:
            print("当前没有学生数据，无法进行点名。")
            return
        while True:
            try:
                # 1. 获取输入
                user_input = input(f"请输入需要点名的学生数量（共 {total_students} 名学生）：")
                # 尝试将输入转换为整数
                num = int(user_input)
                # 2. 逻辑判断 (在 try 块内部处理逻辑异常)
                # 情况(2)：输入人数小于或等于0
                if num <= 0:
                    print("[输入错误] 点名人数必须大于 0。")
                    continue  # 继续循环，让用户重新输入
                # 情况(3)：输入人数超过学生总人数
                elif num > total_students:
                    print(f"[输入错误] 点名人数 ({num}) 超过学生总人数 ({total_students})，请重新输入。")
                    continue  # 继续循环
                # 使用 random.sample 进行不重复随机抽取
                selected_students = random.sample(self.students, num)
                print("\n本次随机点名结果：")
                for i, stu in enumerate(selected_students, start=1):
                    # 格式化输出：序号. 姓名 学号
                    print(f"{i}. {stu.name} {stu.student_id}")

                break  # 任务完成，跳出 while 循环

            except ValueError:
                # 情况(1)：输入非数字字符的异常
                print(f"[输入错误] 请输入整数类型的数据并且小于等于10'{user_input}'")
    def generate_exam_arrangement(self):
        """功能5：生成考场安排表"""
        if not self.students:
            print("当前没有学生数据，无法生成安排表。")
            return
        # 2. 复制一份学生列表并打乱顺序
        temp_students = self.students[:]
        random.shuffle(temp_students)

        # 3. 打开文件准备写入 (使用 utf-8 防止中文乱码)
        filename = "考场安排表.txt"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                # 4. 遍历打乱后的列表
                # enumerate 的第二个参数 1 表示索引从 1 开始（即座位号）
                for seat_num, stu in enumerate(temp_students, 1):
                    # 5. 按照 "座位号,姓名,学号" 的格式拼接字符串
                    line = f"{seat_num},{stu.name},{stu.student_id}\n"
                    # 6. 写入文件
                    f.write(line)
            print(f"成功生成考场安排表：{filename}")
        except Exception as e:
            print(f"生成文件时发生错误：{e}")
    def generate_admission_tickets(self):
        """功能6：打印准考证（含文件格式校验）"""
        folder_name = "准考证"

        # 1. 创建文件夹（如果已存在则不报错）
        os.makedirs(folder_name, exist_ok=True)

        # 2. 读取考场安排表
        try:
            with open("考场安排表.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("错误：找不到【考场安排表.txt】，请先按3生成考场安排表！")
            return
        print("正在生成准考证...")
        # 3. 遍历并解析数据
        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            # 校验逻辑：正常的安排表每一行 split 后应该正好有 3 个元素 [座位号, 姓名, 学号]
            if len(parts) != 3:
                print(f"[警告] 第 {i + 1} 行数据格式错误，已跳过：{line}")
                continue
            seat_num, name, student_id = parts[0], parts[1], parts[2]
            # 4. 生成文件名（保持两位数格式，如 01.txt）
            # 这里使用 seat_num 作为文件名依据，或者使用循环变量 i+1 也可以
            # 为了稳妥，我们用循环变量 i+1 来命名文件，保证顺序
            filename = f"{i + 1:02d}.txt"
            filepath = os.path.join(folder_name, filename)

            # 5. 写入准考证内容
            try:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(f"考场座位号:{seat_num}\n")
                    f.write(f"姓名:{name}\n")
                    f.write(f"学号:{student_id}\n")
            except Exception as e:
                print(f"生成文件 {filename} 时发生错误：{e}")

        print("准考证生成完毕！")
sys=ExamSys()
print(sys.students)
sys.run()
