echo [$(date)]: "START"
#export _VERSION_ = 3.8
#echo [$(date)]: "Creating environment with python ${_VERSION_}"
#conda create --prefix ./env python=${_VERSION_} -y
echo [$(date)]: "Activating Environment"
souce activate rl
echo [$(date)]: "Installing Requirements"
pip install -r requirements.txt
echo [$(date)]: "END"