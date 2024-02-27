import os
import subprocess
import shutil


'''
https://www.autodesk.com.cn/support/technical/article/caas/sfdcarticles/sfdcarticles/CHS/Clean-uninstall.html
'''


def is_autocad_installed():
    try:
        output = subprocess.check_output('where acad', shell=True)
        return True if 'acad.exe' in output.decode('utf-8') else False
    except subprocess.CalledProcessError:
        return False


def get_autocad_dir():
    try:
        output = subprocess.check_output('where acad', shell=True)
        full_path = output.decode('utf-8').strip()
        dir_name = os.path.dirname(full_path)
        return dir_name
    except subprocess.CalledProcessError:
        return None


def check_exists(path):
    return os.path.exists(path)


def delete_directory(path):
    try:
        if os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)
            print(f"已删除: {path}")
        else:
            print(f"路径不存在: {path}")
    except Exception as e:
        print(f"无法删除: {path}, 错误: {str(e)}")


def delete_directories():
    directories_to_delete = [
        "C:\\Autodesk",
        "C:\\Program Files\\Autodesk",
        "C:\\Program Files\\Common Files\\Autodesk Shared",
        "C:\\Program Files (x86)\\Autodesk",
        "C:\\Program Files (x86)\\Common Files\\Autodesk Shared",
        "C:\\ProgramData\\Autodesk",
        os.path.join(os.getenv("LOCALAPPDATA"), "Autodesk"),
        os.path.join(os.getenv("TEMP")),
        os.path.join(os.getenv("APPDATA"), "Autodesk"),
        get_autocad_dir()
    ]

    for directory in directories_to_delete:
        try:
            # delete_directory(directory)
            print(directory, f': {check_exists(directory)}')
        except Exception as e:
            print(f"Failed to delete {directory}: {str(e)}")


delete_directories()


# print(get_autocad_dir())


def delete_registry_entries():
    registry_entries_to_delete = [
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Autodesk",
        "HKEY_CURRENT_USER\\SOFTWARE\\Autodesk"
    ]

    for entry in registry_entries_to_delete:
        try:
            subprocess.run(["reg", "delete", entry, "/f"],
                           stdout=subprocess.PIPE)
        except Exception as e:
            print(f"Failed to delete registry entry {entry}: {str(e)}")


if __name__ == "__main__":
    # uninstall_autodesk_software()
    print("##### 务必以管理员权限运行这个程序。 #####")
    print("##### 运行这个软件前请使用常规方法卸载AutoCAD系列软件，如：Windows自带的卸载工具、Geek Uninstaller、Uninstalltool等工具。 #####")
    print("##### 退出程序后重启电脑务必再次运行这个程序，以确保删除干净。 #####")
    delete_directories()
    delete_registry_entries()
    print("程序执行完毕。")
    input("##### 务必阅读完屏幕输出信息，再按回车退出... #####")
