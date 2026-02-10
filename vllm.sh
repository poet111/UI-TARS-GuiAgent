export PYTHONHASHSEED=42
export PYTHONRANDOMSEED=42
export RANDOM=0
unset http_proxy
unset https_proxy
unset HTTP_PROXY
unset HTTPS_PROXY
export NO_PROXY="localhost,127.0.0.1"
UITARS=''

TP=4
PORT=7770
GPU_MEM_UTIL=0.9
MAX_MODEL_LEN=36864

vllm serve "$UITARS" \
 --host 0.0.0.0 \
 --port $PORT \
 --tensor-parallel-size $TP \
 --gpu-memory-utilization $GPU_MEM_UTIL \
 --served-model-name uitars \
 --limit-mm-per-prompt '{"image": 10}' \
 --trust_remote_code
