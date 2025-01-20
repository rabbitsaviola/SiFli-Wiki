## PCB设计指导

### PCB封装设计

SF32LB52X系列芯片的QFN68L封装，封装尺寸：7mmX7mmx0.85mm；管脚数：68；PIN 间距：0.35mm。 详细尺寸如{numref}`图 {number} <sf32lb52X-B-QFN68L-POD>`所示。
```{figure} assets/sf32lb52X-B-QFN68L-POD.png
:align: center
:scale: 65%
:name: sf32lb52X-B-QFN68L-POD
QFN68L封装尺寸图
```
```{figure} assets/sf32lb52X-B-QFN68L-SHAPE.png
:align: center
:scale: 75%
:name: sf32lb52X-B-QFN68L-XZT
QFN68L封装形状图
```
```{figure} assets/sf32lb52X-B-QFN68L-REF.png
:align: center
:scale: 75%
:name: sf32lb52X-B-QFN68L-VIA
QFN68L封装PCB焊盘设计参考图
```
### PCB叠层设计

SF32LB52X系列芯片布局支持单双面，QFN封装 PCB支持PTH，推荐采用4层PTH，推荐参考叠层结构如{numref}`图 {number} <sf32lb52X-B-PCB-STACK>`所示。
```{figure} assets/sf32lb52X-B-PCB-STACK.png
:align: center
:scale: 100%
:name: sf32lb52X-B-PCB-STACK
参考叠层结构图
```
### PCB通用设计规则
PTH 板PCB通用设计规则如{numref}`图 {number} <sf32lb52X-B-PCB-RULE>`所示。
```{figure} assets/sf32lb52X-B-PCB-RULE.png
:align: center
:scale: 100%
:name: sf32lb52X-B-PCB-RULE
通用设计规则
```
### PCB走线扇出
QFN封装扇出所有管脚全部通过表层扇出，如{numref}`图 {number} <sf32lb52X-B-PCB-FANOUT>`所示
```{figure} assets/sf32lb52X-B-PCB-FANOUT.png
:align: center
:scale: 140%
:name: sf32lb52X-B-PCB-FANOUT
表层扇出参考图
```
### 时钟接口走线
晶体需摆放在屏蔽罩里面，离PCB板框间距大于1mm,尽量远离发热大的器件，如PA，Charge，PMU等电路器件，距离最好大于5mm以上，避免影响晶体频偏，晶体电路禁布区间距大于0.25mm避免有其它金属和器件，如{numref}`图 {number} <sf32lb52X-B-PCB-CRYSTAL>`所示。
```{figure} assets/sf32lb52X-B-PCB-CRYSTAL.png
:align: center
:scale: 100%
:name: sf32lb52X-B-PCB-CRYSTAL
晶体布局图
```
48MHz晶体走线建议走表层长度要求控制在3-10mm区间,线宽0.1mm,必须立体包地处理，并且其走线需远离VBAT，DC/DC及高速信号线。48MHz晶体区域下方表层及临层做禁空处理，禁止其它走线从其区域走，如{numref}`图 {number} <sf32lb52X-B-PCB-48M-SCH>`，{numref}`图 {number} <sf32lb52X-B-PCB-48M-MOD>`，{numref}`图 {number} <sf32lb52X-B-PCB-48M-ROUTE-REF>`所示。
```{figure} assets/sf32lb52X-B-PCB-48M-SCH.png
:align: center
:scale: 140%
:name: sf32lb52X-B-PCB-48M-SCH
48MHz晶体原理图
```
```{figure} assets/sf32lb52X-B-PCB-48M-MOD.png
:align: center
:scale: 160%
:name: sf32lb52X-B-PCB-48M-MOD
48MHz晶体走线模型
```
```{figure} assets/sf32lb52X-B-PCB-48M-ROUTE-REF.png
:align: center
:scale: 130%
:name: sf32lb52X-B-PCB-48M-ROUTE-REF
48MHz晶体走线参考
```
32.768KHz晶体建议走表层，走线长度控制≤10mm,线宽0.1mm,32K_XI/32_XO平行走线间距≥0.15mm,必须立体包地处理，晶体区域下方表层及临层做禁空处理，禁止其它走线从其区域走，如{numref}`图 {number} <sf32lb52X-B-PCB-32K-SCH>`，{numref}`图 {number} <sf32lb52X-B-PCB-32K-MOD>`，{numref}`图 {number} <sf32lb52X-B-PCB-32K-ROUTE-REF>`所示。
```{figure} assets/sf32lb52X-B-PCB-32K-SCH.png
:align: center
:scale: 140%
:name: sf32lb52X-B-PCB-32K-SCH
32.768KHz晶体原理图
```
```{figure} assets/sf32lb52X-B-PCB-32K-MOD.png
:align: center
:scale: 160%
:name: sf32lb52X-B-PCB-32K-MOD
32.768KHz晶体走线模型
```
```{figure} assets/sf32lb52X-B-PCB-32K-ROUTE-REF.png
:align: center
:scale: 130%
:name: sf32lb52X-B-PCB-32K-ROUTE-REF
32.768KHz晶体走线参考
```

### 射频接口走线

射频匹配电路要尽量靠近芯片端放置，不要靠近天线端放置，AVDD_BRF射频电源其滤波电容尽量靠近芯片管脚放置，电容接地PIN脚打孔直接接主地，RF信号的π型网络的原理图和PCB分别如{numref}`图 {number} <sf32lb52X-B-SCH-RF>`，{numref}`图 {number} <sf32lb52X-B-PCB-RF>`所示。
```{figure} assets/sf32lb52X-B-SCH-RF.png
:align: center
:scale: 100%
:name: sf32lb52X-B-SCH-RF
π型网络以及电源电路原理图
```
```{figure} assets/sf32lb52X-B-PCB-RF.png
:align: center
:scale: 100%
:name: sf32lb52X-B-PCB-RF
π型网络以及电源PCB布局
```
射频线建议走表层，避免打孔穿层影响RF 性能，线宽最好大于10mil，需要立体包地处理，避免走锐角和直角，射频线两边多打屏蔽地孔，射频线需做50欧阻抗控制，如{numref}`图 {number} <sf32lb52X-B-SCH-RF-2>`，{numref}`图 {number} <sf32lb52X-B-PCB-RF-ROUTE>`所示。
``{figure} assets/sf32lb52X-B-SCH-RF-2.png
:align: center
:scale: 90%
:name: sf32lb52X-B-SCH-RF-2
RF信号电路原理图

```{figure} assets/sf32lb52X-B-PCB-RF-ROUTE.png
:align: center
:scale: 100%
:name: sf32lb52X-B-PCB-RF-ROUTE
RF信号PCB走线图
```
### 音频接口走线
AVDD33_AUD为音频接口供电的管脚，其滤波电容靠近其对应管脚放置，滤波电容接地脚良好接主地，MIC_BIAS为音频接口麦克风的供电电路，其对应滤波电容靠近对应管脚放置，滤波电容接地脚良好接主地，AUD_VREF滤波电容靠近管脚放置，如{numref}`图 {number} <sf32lb52X-B-SCH-AUDIO-PWR>`，{numref}`图 {number} <sf32lb52X-B-PCB-AUDIO-PWR>`所示。
```{figure} assets/sf32lb52X-B-SCH-AUDIO-PWR.png
:align: center
:scale: 130%
:name: sf32lb52X-B-SCH-AUDIO-PWR
音频电路电源原理图
```
```{figure} assets/sf32lb52X-B-PCB-AUDIO-PWR.png
:align: center
:scale: 150%
:name: sf32lb52X-B-PCB-AUDIO-PWR
音频电路电源滤波电路PCB设计
```

ADCP模拟信号输入，对应电路器件尽量靠近对应管脚放置，走线线长尽量短，走线做立体包地处理，其它接口强干扰信号，远离其走线，如{numref}`图 {number} <sf32lb52X-B-SCH-AUDIO-ADC>`，{numref}`图 {number} <sf32lb52X-B-PCB-AUDIO-ADC>`所示。
```{figure} assets/sf32lb52X-B-SCH-AUDIO-ADC.png
:align: center
:scale: 160%
:name: sf32lb52X-B-SCH-AUDIO-ADC
模拟音频输入原理图
```
```{figure} assets/sf32lb52X-B-PCB-AUDIO-ADC.png
:align: center
:scale: 150%
:name: sf32lb52X-B-PCB-AUDIO-ADC
模拟音频输入PCB设计
```
DACP/DACN 为模拟信号输出，对应电路器件尽量靠近对应管脚放置，每一路P/N需要按照差分线形式走线，走线线长尽量短，走线寄生电容小于10pf, ,差分对走线需做立体包地处理，其它接口强干扰信号，远离其走线，如{numref}`图 {number} <sf32lb52X-B-SCH-AUDIO-DAC>`，{numref}`图 {number} <sf32lb52X-B-PCB-AUDIO-DAC>`所示。
```{figure} assets/sf32lb52X-B-SCH-AUDIO-DAC.png
:align: center
:scale: 150%
:name: sf32lb52X-B-SCH-AUDIO-DAC
模拟音频输出原理图
```
```{figure} assets/sf32lb52X-B-PCB-AUDIO-DAC.png
:align: center
:scale: 150%
:name: sf32lb52X-B-PCB-AUDIO-DAC
模拟音频输出PCB设计
```
### USB接口走线
USB 走线必须先过ESD器件管脚，然后再到芯片端，要保证ESD 器件接地PIN 良好连接主地，PA35(USB DP)/PA36(USB_DN) 按照差分线形式走线，按照90欧差分阻抗控制，并做立体包处理，如图{numref}`图 {number} <sf32lb52X-B-SCH-USB>`，{numref}`图 {number} <sf32lb52X-B-PCB-USB>`，{numref}`图 {number} <sf32lb52X-B-PCB-USB-LAYOUT>`，{numref}`图 {number} <sf32lb52X-B-PCB-USB-ROUTE>`所示。
```{figure} assets/sf32lb52X-B-SCH-USB.png
:align: center
:scale: 160%
:name: sf32lb52X-B-SCH-USB
USB信号原理图
```
```{figure} assets/sf32lb52X-B-PCB-USB.png
:align: center
:scale: 150%
:name: sf32lb52X-B-PCB-USB
USB信号PCB设计
```
```{figure} assets/sf32lb52X-B-PCB-USB-LAYOUT.png
:align: center
:scale: 130%
:name: sf32lb52X-B-PCB-USB-LAYOUT
USB信号器件布局参考
```
```{figure} assets/sf32lb52X-B-PCB-USB-ROUTE.png
:align: center
:scale: 130%
:name: sf32lb52X-B-PCB-USB-ROUTE
USB信号走线模型
```
### SDIO接口走线
SF32LB52X系列芯片提供1个SDIO接口，所有的SDIO信号走线在一起，避免分开走，整个走线长度≤50mm, 组内长度控制≤6mm。SDIO接口时钟信号需立体包地处理，DATA和CMD信号也需要包地处理，如{numref}`图 {number} <sf32lb52X-B-SCH-SDIO>`，{numref}`图 {number} <sf32lb52X-B-PCB-SDIO>`所示。
```{figure} assets/sf32lb52X-B-SCH-SDIO.png
:align: center
:scale: 120%
:name: sf32lb52X-B-SCH-SDIO
SDIO接口电路图
```
```{figure} assets/sf32lb52X-B-PCB-SDIO.png
:align: center
:scale: 100%
:name: sf32lb52X-B-PCB-SDIO
SDIO PCB走线模型
```
### DCDC电路走线
DC-DC电路功率电感和滤波电容必须靠近芯片的管脚放置，BUCK_LX走线尽量短且粗，保证整个DC-DC电路回路电感小，所有的DC-DC输出滤波电容接地脚多打过孔连接到主地平面；BUCK_FB管脚反馈线不能太细，必须大于0.25mm,功率电感区域表层禁止铺铜，临层必须为完整的参考地，避免其它线从电感区域里走线，如{numref}`图 {number} <sf32lb52X-B-SCH-DCDC>`，{numref}`图 {number} <sf32lb52X-B-PCB-DCDC>`所示。
```{figure} assets/sf32lb52X-B-SCH-DCDC.png
:align: center
:scale: 150%
:name: sf32lb52X-B-SCH-DCDC
模拟音频输出原理图
```
```{figure} assets/sf32lb52X-B-PCB-DCDC.png
:align: center
:scale: 150%
:name: sf32lb52X-B-PCB-DCDC
模拟音频输出PCB设计
```
### 电源供电走线

PVDD为芯片内置PMU模块电源输入脚，对应的电容必须靠近管脚放置，走线尽量的粗，不能低于0.4mm，如{numref}`图 {number} <sf32lb52X-B-PCB-PMU>`所示。
```{figure} assets/sf32lb52X-B-PCB-PMU.png
:align: center
:scale: 140%
:name: sf32lb52X-B-PCB-PMU
PVDD电源走线图
```
AVDD33、VDDIOA、VDD_SIP、AVDD33_AUD和AVDD_BRF等管脚滤波电容靠近对应的管脚放置，其走线宽必须满足输入电流要求，走线尽量短粗，从而减少电源纹波提高系统稳定性。
### 其它接口走线

管脚配置为GPADC 管脚信号，必须要求立体包地处理，远离其它干扰信号，如电池电量电路，温度检查电路等。

### EMI&ESD
- 避免屏蔽罩外面表层长距离走线，特别是时钟、电源等干扰信号尽量走内层，禁止走表层。
- ESD保护器件必须靠近连接器对应管脚放置，信号走线先过ESD保护器件管脚，避免信号分叉，没过ESD保护管脚。
- ESD器件接地脚必须保证过孔连接主地，保证地焊盘走线短且粗，减少阻抗提高ESD器件性能。
