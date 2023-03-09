# akudu
Async Kudu Client. Graceful way for Python to async connect to Kudu database (data storage engine).

## Quick start

```
It is recommanded to use Python == 3.10, others are not tested.

*protobuf>=3.20.0* is required, or you need to compile the protobuf files by yourself.
```


1. Install *akudu* from PyPI.
    ``` bash
    pip install akudu
    ```

2. Test your Kudu server, such as 192.168.0.111:7051 with code here:
    ``` python
    import asyncio
    import akudu
    cli = akudu.Client('192.168.0.111', 7051)

    async def op():
        tables = await cli.list_tables()
        print(tables)

    asyncio.run(op())
    ```

3. Here are some frequently used calls, for more please refer to the documentation.
    ``` python
    cli.ping()
    cli.list_tables()
    cli.insert()
    cli.scan()
    ```


## Caution

* This client is not thread-safety, it is recommended that one instance of Kudu() for each threads.



## More

### TODO

* connect timeout, read timeout, write timeout
* Steady state ping-pong
* call-id used-up
* test all calls
* benchmark test
* support RPC Sidecars
* support TLS
* fully support SASL

### Base on

* https://github.com/apache/kudu/tree/1.16.0
* libprotoc 3.21.6 (or python: grpcio-tools)

### Run test

``` bash
python -m venv env
source env/bin/activate
pip install protobuf
python -m test.test_tcp
```

### Generate protobuf files

``` bash
# kudu-master download from github.com kudu

# Because kudu proto generate .pb2 files in the name space: kudu, we need to change it into akudu.kudu
find kudu-master/src/ -name "*.proto" | xargs sed -i 's/import "kudu/import "akudu\/kudu/g'
mkdir kudu-master/src/akudu
mv kudu-master/src/kudu kudu-master/src/akudu

# Generate
find kudu-master/src/ -name "*.proto" | xargs protoc -I=kudu-master/src --python_out=.
# or
find kudu-master/src/ -name "*.proto" | xargs python -m grpc_tools.protoc -I=kudu-master/src --python_out=.
```

### Ref

* https://github.com/apache/kudu
* https://github.com/apache/kudu/blob/master/docs/design-docs/rpc.md
* https://github.com/cyrusimap/cyrus-sasl/blob/master/plugins/plain.c
* https://www.rfc-editor.org/rfc/rfc4616.html
* https://github.com/vmagamedov/grpclib
