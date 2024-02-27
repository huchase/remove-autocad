import os
import argparse
import psutil


def kill_by_name(name):
    # print('taskkill /F /IM \"%s\" /T' % (name+'.exe'))
    os.system('taskkill /F /IM \"%s\" /T' % (name+'.exe'))


def kill_by_name2(name):
    all_processes = psutil.process_iter()

    for process in all_processes:
        # AdskLicensingService
        if name in process.name():
            process.terminate()
            print(
                f"Stopped process: {process.name()} (PID: {process.pid})")
        else:
            # print(process.name())
            pass


def kill_by_pid(pid):
    os.system(f'taskkill /F /PID {pid} /T')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Kill process by name.')
    parser.add_argument(
        '--name', help='program name', type=str, required=True)
    args = parser.parse_args()
    kill_by_name(args.name)
