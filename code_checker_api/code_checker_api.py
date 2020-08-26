import subprocess
import os

def code_checker(data: dict) -> dict:
    language = data['language']
    code = data['code']
    user = data['user']
    problem = data['problem']
    test_cases = data['test_cases']

    if language.lower() == 'python':
        file_type = 'py'
    elif language.lower() == 'c':
        file_type = 'c'
    elif language.lower() == 'c++':
        file_type = 'cpp'


    if user not in os.listdir():
        os.mkdir(user)

    code_file_path = os.path.join(os.path.abspath('.'),"users", user, problem + '.' + file_type)
    with open(code_file_path, 'w+') as code_file:
        code_file.write(code)

    Prefix = os.environ['PREFIX']

    if language.lower() == 'python':
        args = [Prefix + '/bin/python3', code_file_path]
    elif language.lower() == 'c':
        executable = code_file_path[:-(len(file_type)+1)]
        print(executable)
        subprocess.run(['gcc', code_file_path, '-o', executable])
        args = [str(executable)]

    with subprocess.Popen(
            args,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        ) as proc:
        byte_test_cases = ''
        for test_case in test_cases:
            byte_test_cases += str(test_case)+"\n"
        proc.communicate(bytes(byte_test_cases, 'utf-8'))
        out = proc.communicate()[0]
        err = proc.communicate()[1]

    return dict(
                stdout=str(out, 'utf-8'),
                stderr=str(err, 'utf-8'),
                test_cases=test_cases
        )
