cd /data/ig.tools/run_log/whois.agents/agent.size.1/agent.0.initial
python ../../../get_disk_usage.py > disk_usage
python ../../../parse_whois_agent_log.py /data14/ig.log/dev-analysis-nosql-01.vega.ironport.com.agent.0 > overview.txt
python ../../../generate_average.py

