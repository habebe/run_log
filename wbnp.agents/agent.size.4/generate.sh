cd /data/ig.tools/run_log/wbnp.agents/agent.size.4/agent.0.initial
python ../../../parse_wbnp_agent_log.py /data14/ig.log/dev-analysis-nosql-01.vega.ironport.com.agent.0 > overview.txt
python ../../../generate_average.py
python ../../../get_disk_usage.py > disk_usage

cd /data/ig.tools/run_log/wbnp.agents/agent.size.4/agent.1.initial
python ../../../parse_wbnp_agent_log.py /data14/ig.log/dev-analysis-nosql-01.vega.ironport.com.agent.1 > overview.txt
python ../../../generate_average.py
python ../../../get_disk_usage.py > disk_usage

cd /data/ig.tools/run_log/wbnp.agents/agent.size.4/agent.2.initial
python ../../../parse_wbnp_agent_log.py /data14/ig.log/dev-analysis-nosql-01.vega.ironport.com.agent.2 > overview.txt
python ../../../generate_average.py
python ../../../get_disk_usage.py > disk_usage

cd /data/ig.tools/run_log/wbnp.agents/agent.size.4/agent.3.initial
python ../../../parse_wbnp_agent_log.py /data14/ig.log/dev-analysis-nosql-01.vega.ironport.com.agent.3 > overview.txt
python ../../../generate_average.py
python ../../../get_disk_usage.py > disk_usage
