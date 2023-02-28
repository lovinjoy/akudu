# akudu
Async Kudu Client. Graceful way for Python to async connect to Kudu database (data storage engine).

## Quick start

It is recommanded to use Python == 3.10, others are not tested.


1. Install *akudu* from Pypi.
    ``` bash
    pip install akudu
    ```

2. Test your Kudu server, such as 192.168.0.111:7051 with code here:
    ``` python
        import asyncio
        import akudu
        cli = akudu.Kudu('192.168.0.111', 7051)

        async def op():
            tables = await cli.list_tables()
            print tables

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

* This client is not thread-safety, use one instance of Kudu() for each threads.


## To contribute

### TODO

* test all calls
* benchmark test
* support RPC Sidecars
* support TLS
* fully support SASL

### Base on

* https://github.com/apache/kudu/tree/1.16.0
* libprotoc 3.12.4

### Generate protobuf files

``` bash
find ./kudu-master/src/ -name "*.proto" | xargs protoc -I=kudu-master/src --python_out=kudu
```

### Ref

* https://github.com/apache/kudu
* https://github.com/apache/kudu/blob/master/docs/design-docs/rpc.md
* https://github.com/cyrusimap/cyrus-sasl/blob/master/plugins/plain.c
* https://www.rfc-editor.org/rfc/rfc4616.html
