cd /data/ig.tools/run_log/wbnp.agents/agent.size.2/agent.0.initial
python ../../../parse_wbnp_agent_log.py /data14/ig.log/dev-analysis-nosql-01.vega.ironport.com.agent.0 > overview.txt
python ../../../generate_average.py

cd /data/ig.tools/run_log/wbnp.agents/agent.size.2/agent.1.initial
python ../../../parse_wbnp_agent_log.py /data14/ig.log/dev-analysis-nosql-01.vega.ironport.com.agent.1 > overview.txt
python ../../../generate_average.py
