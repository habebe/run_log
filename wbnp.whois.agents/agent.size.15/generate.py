import os

def run(log_name,id):
    print log_name,id
    cwd = os.getcwd()
    os.system("mkdir -p /data/ig.tools/run_log/wbnp.whois.agents/agent.size.15/{0}.{1}".format(log_name,id))
    os.chdir("/data/ig.tools/run_log/wbnp.whois.agents/agent.size.15/{0}.{1}".format(log_name,id))
    os.system("python ../../../parse_agent_log.py /data14/ig.log/{0}.{1} > overview.txt".format(log_name,id))
    os.system("python ../../../generate_average.py")
    os.chdir(cwd)
    pass


for log_name in ["dev-analysis-nosql-01.vega.ironport.com.agent","dev-analysis-nosql-03.vega.ironport.com.agent","dev-analysis-nosql-04.vega.ironport.com.agent"]:
    for id in [0,1,2,3,4]:
        run(log_name,id)
        pass
    pass


