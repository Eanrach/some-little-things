import paramiko
import threading

#限制进程数量
thread_pool = threading.BoundedSemaphore(20)

def sftp(
        hostname:str,
        username:str,
        password:str,
        local_path:str,
        remote_path:str,
        func:str
    ):
    try:
        #进程数占用
        thread_pool.acquire()
        #sftp模块
        tran = paramiko.Transport((hostname, 22))
        #设置目标地址
        tran.connect(username=username,password=password)
        #设置用户名密码登录并连接
        print("connected")
        sftp1 = paramiko.SFTPClient.from_transport(tran) 
        print("start sftp")
        if func == "up":
            sftp1.put(local_path, remote_path)
            print("upload active")
        else:
            sftp1.get(remote_path, local_path) 
            print("download active")
        tran.close()
        #关闭连接
        print("Transport close")
        #进程数释放
        thread_pool.release()
    except Exception as error:
        print(hostname.replace("\n","")+"\t error:"+str(error))
        thread_pool.release()

def ssh_client_con(
        hostname:str,
        username:str,
        password:str,
        shell_command:str
    ):
    try:
        #进程数占用
        thread_pool.acquire()
        ssh_client = paramiko.SSHClient()
        #实体化sshclient
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        #第一次登录免yes/no选项
        ssh_client.connect(
            port=22,
            hostname=hostname,
            username=username,
            password=password
        )
        #配置用户名密码

        stdin, stdout, stderr = ssh_client.exec_command(shell_command)
        #获取返回信息
        stdout_info = stdout.read().decode('utf8')
        print(hostname.replace("\n","")+":\t"+stdout_info)
        stderr_info = stderr.read().decode('utf8')
        print(stderr_info)
        ssh_client.close()
        #进程数释放
        thread_pool.release()
    except Exception as error:
        print(hostname.replace("\n","")+"\t error:"+str(error))
        thread_pool.release()


def dispatchOptions(argv):
    import getopt
    prompt = '''
            --hostname=<ip/PATH_TO_FILE>\t Hostname is NECESSARY
            --username=<user>
            --password=<pass>
            --local_path=<PATH_TO_FILE>\t If use --func=sftp, THIS PATH MUST CONTAINS FILENAME!!!!
            --remote_path=<PATH_TO_FILE>\t If use --func=sftp, THIS PATH MUST CONTAINS FILENAME!!!!
            --func=<ssh/sftp>
            --shell_command=<string>\t If use --func=ssh
            --sftp_func=<up/down>\t Put or get thing to/from target
            '''
    #提示信息
    #以下配置参数
    try:
        opts, args = getopt.getopt(argv,
                        "h",
                        ["help","hostname=","username=","password=","local_path=","remote_path=","func=","shell_command=","sftp_func="])
    except getopt.GetoptError:
        print(prompt)
    
    for opt,arg in opts:
        if opt in ("--hostname"):
            hostname = arg
        elif opt in ("--username"):
            username = arg
        elif opt in ("--password"):
            password = arg
        elif opt in ("--local_path"):
            local_path = arg 
        elif opt in ("--remote_path"):
            remote_path = arg
        elif opt in ("--func"):
            func = arg
        elif opt in ("--shell_command"):
            shell_command = arg
        elif opt in ("--sftp_func"):
            sftp_func = arg

    try:
        # 无缺失参数开始调度
        if "/" in hostname:
            # 目标列表调度逻辑
            try:
                with open(hostname,'r') as f:
                    for i in f.readlines():
                        try:
                            if func == 'ssh':
                                #配置线程
                                thread = threading.Thread(target=ssh_client_con,kwargs={"hostname":i,"username":username,
                                                                        "password":password,"shell_command":shell_command})
                                #线程启动
                                thread.start()
                                #ssh_client_con(hostname=i,username=username,password=password,shell_command=shell_command)
                                
                            elif func == 'sftp':
                                #配置线程
                                thread = threading.Thread(target=sftp,kwargs={"hostname":i,"username":username,
                                    "password":password,"local_path":local_path,
                                    "remote_path":remote_path,"func":sftp_func})
                                #线程启动
                                thread.start()
                                # sftp(hostname=i,username=username,
                                #     password=password,local_path=local_path,
                                #     remote_path=remote_path,func=sftp_func)
                        except Exception as error:
                            print(i.replace("\n","")+"\t error:"+str(error))
                            continue
            except FileNotFoundError:
                print("This file is not exist,try again.")
                print(prompt)
        else:
            #单一目标调度逻辑
            if func == 'ssh':
                ssh_client_con(hostname=hostname,username=username,password=password,shell_command=shell_command)
            elif func == 'sftp':
                sftp(hostname=hostname,username=username,
                                password=password,local_path=local_path,
                                remote_path=remote_path,func=sftp_func)
    except UnboundLocalError:
        # 参数缺失
        print("lack args ")
        print(prompt)

                

    

import sys
dispatchOptions(sys.argv[1:])
