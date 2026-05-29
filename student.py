import os
class Student:
    def __init__(self, id_, name, gender, class_id, student_id, college):
        self.id = id_                # 序号
        self.name = name            # 姓名
        self.gender = gender        # 性别
        self.class_id = class_id    # 班级
        self.student_id = student_id  # 学号
        self.college = college      # 学院

    @classmethod
    def load_students(cls, filename="人工智能编程语言学生名单.txt"):
        students = []  # 准备一个空列表来存放即将生成的学生对象
        if not os.path.exists(filename):#确认该文件存在
            print(f"错误：未找到文件 '{filename}'")
            return students
        try:
            # 以 utf-8 编码打开文件，防止中文乱码
            with open(filename, "r", encoding="utf-8") as f:
                lines = f.readlines()  # 读取所有行
                for line in lines[1:]:
                    line = line.strip()  # 去掉每行首尾的换行符和空格
                    if not line:  # 如果遇到空行，直接跳过
                        continue
                    data = line.split()
                    # 确保这一行正好有6个数据（防止文件格式错乱导致报错）
                    if len(data) == 6:
                        # 使用 cls(...) 也就是 Student(...) 来实例化一个学生对象
                        student_obj = cls(data[0], data[1], data[2], data[3], data[4], data[5])
                        students.append(student_obj)  # 把生成的对象加入列表

            print(f"【系统】已成功加载 {len(students)} 名学生信息。")
        except Exception as e:
            print(f"读取文件时发生未知错误: {e}")
        return students
