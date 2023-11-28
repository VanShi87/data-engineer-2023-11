# import the python subprocess module
import subprocess


def run_cmd(args_list):
    """
        run linux commands
    """
    # import subprocess
    print('Running system command: {0}'.format(' '.join(args_list)))
    proc = subprocess.Popen(args_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    s_output, s_err = proc.communicate()
    s_return = proc.returncode
    return s_return, s_output, s_err


(ret, out, err) = run_cmd(['hdfs', 'dfs', '-ls', 'hdfs_file_path'])
lines = out.split('\n')

(ret, out, err) = run_cmd(['hdfs', 'dfs', '-get', 'hdfs_file_path', 'local_path'])

(ret, out, err) = run_cmd(['hdfs', 'dfs', '-put', 'local_file', 'hdfs_file_path'])

(ret, out, err) = run_cmd(['hdfs', 'dfs', '-copyFromLocal', 'local_file', 'hdfs_file_path'])

(ret, out, err) = run_cmd(['hdfs', 'dfs', '-copyToLocal', 'hdfs_file_path', 'local_file'])

(ret, out, err) = run_cmd(['hdfs', 'dfs', '-rm', 'hdfs_file_path'])
(ret, out, err) = run_cmd(['hdfs', 'dfs', '-rm', '-skipTrash', 'hdfs_file_path'])

(ret, out, err) = run_cmd(['hdfs', 'dfs', '-rm', '-r', 'hdfs_file_path'])
(ret, out, err) = run_cmd(['hdfs', 'dfs', '-rm', '-r', '-skipTrash', 'hdfs_file_path'])

hdfs_file_path = '/tmpo'
cmd = ['hdfs', 'dfs', '-test', '-e', hdfs_file_path]
(ret, out, err) = run_cmd(cmd)
print(ret, out, err)
if ret:
    print('file does not exist')
