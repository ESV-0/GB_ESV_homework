# Домашнеее задание, урок-7, задание-3
import shutil
import os

os.chdir("C:\\Users\\emplo\\Desktop\\GB_ESV_homework\\lesson_7\\my_project")

dir_path = os.path.join('templates', 'mainapp')
if not os.path.exists(dir_path):
    os.makedirs(dir_path, exist_ok=True)
dir_path = os.path.join('templates', 'authapp')
if not os.path.exists(dir_path):
    os.makedirs(dir_path, exist_ok=True)

shutil.copyfile("C:\\Users\\emplo\\Desktop\\GB_ESV_homework\\lesson_7\\my_project\\mainapp\\templates\\mainapp\\base.html",
                "C:\\Users\\emplo\\Desktop\\GB_ESV_homework\\lesson_7\\my_project\\templates\\mainapp\\base.html")
shutil.copyfile("C:\\Users\\emplo\\Desktop\\GB_ESV_homework\\lesson_7\\my_project\\mainapp\\templates\\mainapp\\index.html",
                "C:\\Users\\emplo\\Desktop\\GB_ESV_homework\\lesson_7\\my_project\\templates\\mainapp\\index.html")

shutil.copyfile("C:\\Users\\emplo\\Desktop\\GB_ESV_homework\\lesson_7\\my_project\\authapp\\templates\\authapp\\base.html",
                "C:\\Users\\emplo\\Desktop\\GB_ESV_homework\\lesson_7\\my_project\\templates\\authapp\\base.html")
shutil.copyfile("C:\\Users\\emplo\\Desktop\\GB_ESV_homework\\lesson_7\\my_project\\authapp\\templates\\authapp\\index.html",
                "C:\\Users\\emplo\\Desktop\\GB_ESV_homework\\lesson_7\\my_project\\templates\\authapp\\index.html")