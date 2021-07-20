# 大喜利チャットbot
https://togetter.com/li/1290630

# 使用技術

## AWS Sagemaker
https://aws.amazon.com/jp/sagemaker/?hp=tile&so-exp=below

## AWS Lambda
https://aws.amazon.com/jp/getting-started/hands-on/build-web-app-s3-lambda-api-gateway-dynamodb/

## AWS Comprehend




# 6/29

## lambda tutorial

https://aws.amazon.com/jp/getting-started/hands-on/build-web-app-s3-lambda-api-gateway-dynamodb/

うまくいった．webから入力を受け取る枠組みが作れそう．

## キーワード抽出

### aws comprehend

```
{
    "KeyPhrases": [
        {
            "Score": 0.9996695518493652,
            "Text": "このパラメータに対するクエリ文字列パラメータ",
            "BeginOffset": 0,
            "EndOffset": 22
        },
        {
            "Score": 0.9999149441719055,
            "Text": "メソッドリクエスト",
            "BeginOffset": 30,
            "EndOffset": 39
        }
    ]
}
```

```
❯❯❯ aws comprehend detect-key-phrases \
            --region us-east-1 \
            --language-code "ja" \
            --text "犯罪者だらけのバスツアーの感想はどうでした？"
{
    "KeyPhrases": [
        {
            "Score": 0.9998466968536377,
            "Text": "犯罪者だらけのバスツアーの感想",
            "BeginOffset": 0,
            "EndOffset": 15
        }
    ]
}
```

抽出の精度がいまいち．

### TermExtract

https://qiita.com/EastResident/items/0cdc7c5ac1f0a6b3cf1d
http://gensen.dl.itc.u-tokyo.ac.jp/pytermextract/

<details><summary>堀川のM1macではエラー．</summary><div>

```
~/M/o/p/tests (main ⚡☡=)
❯❯❯ python3 -m unittest
........E
======================================================================
ERROR: test (test_nlpir.nlpir)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/kyohei/MyWork/ogiri/pytermextract-0_01/tests/test_nlpir.py", line 9, in test
    import pynlpir
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pynlpir/__init__.py", line 26, in <module>
    from . import nlpir, pos_map
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pynlpir/nlpir.py", line 119, in <module>
    libNLPIR = load_library(sys.platform, is_64bit)  # noqa: N816
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pynlpir/nlpir.py", line 111, in load_library
    lib_nlpir = cdll.LoadLibrary(lib if is_python3 else lib.encode('utf-8'))
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/ctypes/__init__.py", line 452, in LoadLibrary
    return self._dlltype(name)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/ctypes/__init__.py", line 374, in __init__
    self._handle = _dlopen(self._name, mode)
OSError: dlopen(/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pynlpir/lib/libNLPIRios.so, 6): no suitable image found.  Did find:
	/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pynlpir/lib/libNLPIRios.so: mach-o, but wrong architecture
	/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pynlpir/lib/libNLPIRios.so: mach-o, but wrong architecture

----------------------------------------------------------------------
Ran 9 tests in 1.844s

FAILED (errors=1)

```
</div></details>



testは失敗したけど，，

```
$ cd pytermex
$ echo "犯罪者だらけのバスツアーの感想はどうでした？" >> japanese_text.txt
$ python3 termex_janome.py japanese_text.txt
$ cat janome_extracted.txt

犯罪者だらけ	1.5874010519681994
バスツアー	1.4142135623730951
感想	1.0
```

いけた．いい感じに取り出せている．
