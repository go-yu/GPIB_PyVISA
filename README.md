# GPIB、PyVISAで完全自動測定

以下のサイトに詳しい説明があります。


実際に使う場合はまず下のコードをターミナルで打ち込んでGPIBのアドレスと測定器の対応を調べてください。
その後、`auto_measure.py`でアドレスを変えてください。

~~~
$ python
>>> import pyvisa
>>> rm = pyvisa.ResourceManager()
>>> rm.list_resources()
('ASRL1::INSTR', 'ASRL2::INSTR', 'GPIB0::12::INSTR')
>>> inst = rm.open_resource('GPIB0::12::INSTR')
>>> print(inst.query("*IDN?"))
(測定器の名前などが出力される)
>>> exit()
~~~
