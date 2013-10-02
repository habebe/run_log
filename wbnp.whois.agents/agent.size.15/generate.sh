mkdir -p /data/ig.tools/run_log/wbnp.whois.agents/agent.size.15/agent.0.initial
cd /data/ig.tools/run_log/wbnp.whois.agents/agent.size.15/agent.0.initial
python ../../../parse_agent_log.py /data14/ig.log/dev-analysis-nosql-01.vega.ironport.com.agent.0 > overview.txt
python ../../../generate_average.py

mkdir -p /data/ig.tools/run_log/wbnp.whois.agents/agent.size.15/agent.1.initial
cd /data/ig.tools/run_log/wbnp.whois.agents/agent.size.15/agent.1.initial
python ../../../parse_agent_log.py /data14/ig.log/dev-analysis-nosql-01.vega.ironport.com.agent.1 > overview.txt
python ../../../generate_average.py

mkdir -p /data/ig.tools/run_log/wbnp.whois.agents/agent.size.15/agent.2.initial
cd /data/ig.tools/run_log/wbnp.whois.agents/agent.size.15/agent.2.initial
python ../../../parse_agent_log.py /data14/ig.log/dev-analysis-nosql-01.vega.ironport.com.agent.2 > overview.txt
python ../../../generate_average.py

mkdir -p /data/ig.tools/run_log/wbnp.whois.agents/agent.size.15/agent.3.initial
cd /data/ig.tools/run_log/wbnp.whois.agents/agent.size.15/agent.3.initial
python ../../../parse_agent_log.py /data14/ig.log/dev-analysis-nosql-01.vega.ironport.com.agent.3 > overview.txt
python ../../../generate_average.py

mkdir -p /data/ig.tools/run_log/wbnp.whois.agents/agent.size.15/agent.4.initial
cd /data/ig.tools/run_log/wbnp.whois.agents/agent.size.15/agent.4.initial
python ../../../parse_agent_log.py /data14/ig.log/dev-analysis-nosql-01.vega.ironport.com.agent.4 > overview.txt
python ../../../generate_average.py
