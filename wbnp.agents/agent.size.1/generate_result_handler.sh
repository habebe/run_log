cd /data/ig.tools/run_log/wbnp.agents/agent.size.1/agent.0.initial.result_handler
python ../../../get_disk_usage.py > disk_usage
python ../../../parse_wbnp_agent_log.py /data14/ig.log/dev-analysis-nosql-01.vega.ironport.com.agent.0 > overview.txt
python ../../../generate_average.py

