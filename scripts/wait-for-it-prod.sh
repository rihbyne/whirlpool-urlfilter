#!/bin/bash
while ! ((nc -z whirlpool-rmq 5672) &&
             (nc -z $MEMCACHE_ENDPOINT $MEMCACHE_PORT)); do sleep 3; done
echo "urlfilter python evironment is set to: " $PY_ENV
python3 -u ./urlfilter/main.py
