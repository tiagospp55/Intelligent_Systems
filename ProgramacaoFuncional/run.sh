echo "Starting..."

source venv/bin/activate
   tmux new-session -d -s mysession
tmux split-window -h -t mysession
tmux split-window -v -t mysession

tmux send-keys -t mysession:0.0 "python3 server.py" C-m
tmux send-keys -t mysession:0.1 "python3 viewer.py" C-m
tmux send-keys -t mysession:0.2 "python3 student.py " C-m 

tmux attach-session -t mysession 


tmux send-keys -t mysession:0.2 " tmux kill-server " C-m 
