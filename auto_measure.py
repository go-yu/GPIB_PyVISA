import pyvisa

#設定
rm = pyvisa.ResourceManager()
power = rm.open_resource('GPIB0::0::INSTR') #電源
analyzer = rm.open_resource('GPIB0::1::INSTR') #スペクトラムアナライザ

#電源の電圧を計測
max_volt = power.query('MEAS:VOLT?')
print(max_volt)

#スペクトラムアナライザのピーク周波数を計測
analyzer.write('CALC:MARK:MAX')
peak_freq = analyzer.query('CALC:MARK:X?')
print(peak_freq)
