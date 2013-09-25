cd /data/ig.tools/run_log/whois.agents/agent.size.5/agent.0.initial
python ../../../get_disk_usage.py > disk_usage
python ../../../parse_whois_agent_log.py /data14/ig.log/dev-analysis-nosql-01.vega.ironport.com.agent.0 > overview.txt
python ../../../generate_average.py

cd /data/ig.tools/run_log/whois.agents/agent.size.5/agent.1.initial
python ../../../get_disk_usage.py > disk_usage
python ../../../parse_whois_agent_log.py /data14/ig.log/dev-analysis-nosql-01.vega.ironport.com.agent.1 > overview.txt
python ../../../generate_average.py

cd /data/ig.tools/run_log/whois.agents/agent.size.5/agent.2.initial
python ../../../get_disk_usage.py > disk_usage
python ../../../parse_whois_agent_log.py /data14/ig.log/dev-analysis-nosql-01.vega.ironport.com.agent.2 > overview.txt
python ../../../generate_average.py

cd /data/ig.tools/run_log/whois.agents/agent.size.5/agent.3.initial
python ../../../get_disk_usage.py > disk_usage
python ../../../parse_whois_agent_log.py /data14/ig.log/dev-analysis-nosql-01.vega.ironport.com.agent.3 > overview.txt
python ../../../generate_average.py


cd /data/ig.tools/run_log/whois.agents/agent.size.5/agent.4.initial
python ../../../get_disk_usage.py > disk_usage
python ../../../parse_whois_agent_log.py /data14/ig.log/dev-analysis-nosql-01.vega.ironport.com.agent.4 > overview.txt
python ../../../generate_average.py
