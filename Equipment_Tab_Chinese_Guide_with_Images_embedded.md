# 设备选项卡 (Equipment Tab) 完整指南 - 含嵌入式图片

## 目录

1. [基本功能](#基本功能)
2. [用户界面基础](#用户界面基础)
3. [特殊参数类型](#特殊参数类型)
4. [负载设备](#负载设备)
5. [外部能源网络](#外部能源网络)
6. [电气设备](#电气设备)
7. [热力设备](#热力设备)
8. [氢能设备](#氢能设备)
9. [中央设备](#中央设备)

---

## 基本功能

设备选项卡允许用户：
- 查看不同技术类型的资产库
- 通过连接资产来创建能源系统
- 通过设置参数值来自定义资产

---

## 用户界面基础

### 资产库 (Asset Library)

资产库部分显示可用资产的表格，包含以下数据：

- **资产类型 (Asset type)**: 资产的类型
- **库资产 (Library asset)**: 资产的名称，标识特定的库资产

**许可证说明**:
- 小型许可证 (S): 仅包含电气资产类型
- 中型许可证 (M): 包含电气和热力资产类型  
- 大型许可证 (L): 包含电气、热力和氢能资产类型

#### 支持的资产类别

**负荷 (Loads)**
- Load (电气负载) - (S)(M)(L)
- DeferrableLoad (可延迟负载) - (S)(M)(L)
- SteamLoad (蒸汽负载) - (M)(L)
- HotWaterLoad (热水负载) - (M)(L)
- ColdWaterLoad (冷水负载) - (M)(L)
- H2Load (HP/LP 氢气负载) - (L)

**电动汽车充电站 (Electric Vehicle Charging Stations)**
- EVStation - (S)(M)(L)

**外部能源网络 (External Energy Networks)**
- Grid (电网) - (S)(M)(L)
- DistrictSteam (区域蒸汽) - (M)(L)
- DistrictCooling (区域冷却) - (M)(L)
- DistrictHeating (区域供热) - (M)(L)
- H2Network (HP/LP 氢气网络) - (L)

**风力涡轮机 (Wind Turbines)**
- ImportedWT (导入风力涡轮机) - (S)(M)(L)
- WindTurbine (风力涡轮机) - (S)(M)(L)

**光伏系统 (Photovoltaic Systems)**
- ImportedPV (导入光伏) - (S)(M)(L)
- InternalPV (内部光伏) - (S)(M)(L)

**电能储存系统 (Electric Energy Storage System)**
- Energy Storage System (ESS) - (S)(M)(L)
- LithiumIonBatter (锂离子电池) - (S)(M)(L)

**往复式发动机 (Reciprocating Engines)**
- GenSet (发电机组) - (S)(M)(L)
- DualFuelGenset (双燃料发电机组) - (S)(M)(L)
- CHP (热电联产) - (M)(L)

**燃气轮机 (Gas Turbines)**
- AeroderivativeGT (航空衍生燃气轮机) - (M)(L)
- IndustrialGT (工业燃气轮机) - (M)(L)
- LargeFrameGT (大型燃气轮机) - (M)(L)
- GenericGT (通用燃气轮机) - (M)(L)
- H2Turbine (氢气涡轮机) - (L)

**蒸汽系统 (Steam Systems)**
- SteamLoad (蒸汽负载) - (M)(L)
- SteamTurbine (蒸汽涡轮机) - (M)(L)
- SteamBoiler (蒸汽锅炉) - (M)(L)
- CoalFiredSteamBoiler (燃煤蒸汽锅炉) - (M)(L)
- ElectricSteamBoiler (电蒸汽锅炉) - (M)(L)
- HighTemperatureStorage (高温储存) - (M)(L)
- SteamValve (蒸汽阀) - (M)(L)
- SteamVent (蒸汽排气) - (M)(L)

**热水系统 (Hot Water Systems)**
- HotWaterLoad (热水负载) - (M)(L)
- DistrictHeating (区域供热) - (M)(L)
- HotWaterBoiler (热水锅炉) - (M)(L)
- CoalFiredHotWaterBoiler (燃煤热水锅炉) - (M)(L)
- ElectricHotWaterBoiler (电热水锅炉) - (M)(L)
- HeatPump (热泵) - (M)(L)
- HotWaterStorage (热水储存) - (M)(L)
- HotWaterValve (热水阀) - (M)(L)
- HotWaterVent (热水排气) - (M)(L)

**冷水系统 (Cold Water Systems)**
- ColdWaterLoad (冷水负载) - (M)(L)
- DistrictCooling (区域冷却) - (M)(L)
- AbChiller (吸收式冷机) - (M)(L)
- CompressionChiller (压缩式冷机) - (M)(L)
- ColdWaterStorage (冷水储存) - (M)(L)
- ColdWaterValve (冷水阀) - (M)(L)
- ColdWaterVent (冷水排气) - (M)(L)

**电缆、阀门和排气 (Cable, Valves, and Vents)**
- Cable (电缆) - (S)(M)(L)
- ElectricLoadBank (电负载库) - (S)(M)(L)
- H2Compressor (氢气压缩机) - (L)
- H2Valve (氢气阀) - (L)

**氢能系统 (Hydrogen Systems)**
- H2Load (HP/LP 氢气负载) - (L)
- H2Network (HP/LP 氢气网络) - (L)
- Electrolyzer (电解槽) - (L)
- H2Turbine (氢气涡轮机) - (L)
- H2FuelCell (燃料电池) - (L)
- H2Compressor (氢气压缩机) - (L)
- H2Valve (氢气阀) - (L)
- Process Plant (氨厂/内热厂) - (L)

**氢能储存系统 (Hydrogen Storage Systems)**
- H2Storage (氢气储存) - (L)

**中央设备 (Central Equipment)**
- FixedCosts (固定成本) - (S)(M)(L)
- MGC (多代理控制) - (S)(M)(L)
- Multi-Step (多步) - (S)(M)(L)

### 资产部分 (Assets Section)

已部署和配置的资产显示在此部分。表格包含以下列：

- **资产类型 (Asset type)**: 资产的类型
- **资产名称 (Asset name)**: 资产的名称（可编辑，必须在项目内唯一）
- **参考 (Reference)**: 标记为参考的资产包含在参考配置中（在拓扑选项卡中显示绿色背景）
- **替换 (Replacement)**: 标记为替换的资产在模拟开始时不安装，而是在另一个资产达到使用寿命后安装（显示紫色背景）
- **所有者 (Owner)**: 分配给资产的所有者
- **摘要 (Summary)**: 显示每个资产的重要KPI摘要

### 参数部分 (Parameters Section)

参数部分显示所选资产的参数及其值。

**参数类别**:
- **Base**: 显示基础参数
- **其他类别**: 可以启用或禁用以显示特定类别的参数

**参数表列**:
- **参数 (Parameter)**: 参数名称
- **Base**: 此配置的基础参数值
- **Variation**: 包含在搜索空间中的参数的所有变化

---

## 特殊参数类型

### 价格矩阵 (Price Matrix)

价格矩阵对所有资产都很常见，描述资产的主要经济方面：

- **Size (尺寸)**: 设置价格的尺寸
- **CAPEX**: 资产的初始价格
- **OPEX**: 资产的小时成本
- **Replacement Price (替换价格)**: 替换资产的价格
- **Annual Multiplier (年度乘数)**: 替换成本的乘数
- **Year (年份)**: 应用乘数的年份

价格矩阵可以有多行，每行列出特定的尺寸及其对应的CAPEX、OPEX和替换价格。其他尺寸的价格可以通过插值或外推计算。

### 热平衡表 (Heat Balance Table - HBT)

某些资产允许用户直接输入资产内所有功率和燃料流的一系列设定点。

**关键概念**:
- 如果"额定功率"参数与热平衡表最后一行的输出功率值不同，则所有值（功率、燃料消耗、氢气等）按因子 Rated power / Output power 缩放
- 这确保效率保持不变

**对称性破缺**:
当配置中有两个或多个相同的资产时，可能会出现无限数量的不同功率调度解决方案。ISED使用对称性破缺技术来加快找到最优解的速度。

### 最小或最大功率输出

许多具有热平衡表的资产包含描述最小和最大输出功率（作为时间函数）的参数。

**对于具有启动模式的资产** (燃气轮机、燃气发动机、蒸汽涡轮机):
- 最小输出功率 < 热平衡表第一行 → 使用热平衡表第一行
- 最小输出功率 > 热平衡表第一行 → 使用最小输出功率
- 最大输出功率 < 热平衡表最后一行 → 使用最大输出功率
- 最大输出功率 > 热平衡表最后一行 → 使用热平衡表最后一行

**对于没有启动模式的资产** (锅炉、压缩式冷机、热泵、电解槽、燃料电池):
- 最小和最大输出功率始终有效（只要它们在0-100%之间）

### 停机计划 (Outages Schedule)

许多资产有停机计划，反映资产的计划/非计划停机时间。在这些时期，资产可能无法生产或消耗功率。

**定义停机时间**:
- 用户选择一年并切换到"Definition Max"选项卡
- 在此处，用户可以通过将相应的停机小时标记为"0"（默认颜色=蓝色）来定义每个月中每一天的停机时间
- 用户可以将定义的任何月份的停机时间应用到任何其他月份
- 切换回概览时，一年的停机计划也可以应用到其他年份

### 可用性 (Availability)

许多资产有可用性参数，允许用户包含计划或非计划停机时间。

**定义非计划停机时间**:
- 定义全年每个月的预期故障次数
- 设置每次发生的最小和最大停机时间

**定义计划停机时间**:
- 通过文本文件加载配置文件
- 有效文件每行有两个值：(时间戳) (值)
- 时间戳是从年初开始的秒数
- 值=0表示停机，值=1表示不停机

### 替换策略 (Replacement Strategy)

许多资产有替换策略参数，允许用户指定资产达到使用寿命后会发生什么。

**三种替换策略**:

1. **默认策略**: 资产被相同配置的相同资产替换，但生命周期计数器重置为最大生命周期

2. **移除策略**: 资产在达到使用寿命后从部署中移除

3. **替换为其他资产**: 资产在达到使用寿命后被移除，并安装一个或多个其他替换资产

### 其他常见参数

- **Must Run (必须运行)**: 如果设置为"true"，则始终强制执行最小允许功率。如果最小允许功率不为零，这意味着该单元必须运行，不能关闭

- **Maximum annual full load hours (最大年度满负荷小时数)**: 每个单元在一年内允许运行的满负荷小时数

- **Maximum annual running hours (最大年度运行小时数)**: 每个单元在一年内允许运行的小时数

- **Full load scaling factor (满负荷缩放因子)**: 与资产额定容量成比例的值，用于确定资产在一年内运行的"满负荷小时数"

---

## 负载设备

### 电气负载 (Electric Load)

**概述**:
电气负载是满足DES客户需求的负载。通常不包含损耗。电气负载可能被分配不满足它的成本。

**参数 - 按类别**:

**容量 (Capacity)**
- **Load [kW]**: 描述请求负载的时间序列 [kW]
- **Default load [kW]**: 未设置"Load[kW]"时间序列时使用的值

**稳定性 (Stability - Grid, OR)**
- **Operating reserve**: 调度员必须确保可用的额外能量
- **Relative Operating reserve [pu]**: 所需相对运行备用的时间序列
- **Default relative operating reserve [pu]**: 未设置时间序列时使用的值
- **Peak Operating Reserve [pu]**: 所需峰值运行备用的时间序列
- **Default Peak Operating Reserve [pu]**: 未设置时间序列时使用的值
- **Requires redundancy**: 如果为true，负载需要冗余发电能力

**脱落 (Shedding)**
- **Shedding priority**: 脱落优先级（-1为主要负载）
- **Starting priority**: 启动优先级
- **Shedding event cost [EUR]**: 负载脱落时的一次性成本
- **Shedding time cost [EUR/h]**: 负载脱落时的小时成本
- **Minimum shedding duration [s]**: 安全运行恢复前的最小停机时间
- **Ramp rate after shedding [%/s]**: 脱落事件后的负载上升速率

**时间 (Time)**
- **Installation delay [y]**: 模拟开始后资产安装的时间延迟（年）

### 可延迟负载 (Deferrable Load)

**概述**:
这是一种可以连接到储存库的负载。负载和储存库一起允许配置可延迟负载，即必须在某个时刻满足但由存储解耦的负载。

**参数 - 按类别**:

**经济 (Economics)**
- **Charging incentive [EUR/kWh]**: 可延迟负载仅在功率成本低于此值时增加存储

**容量 (Capacity)**
- **Load [m³/h]**: 可延迟负载存储的出口流量时间序列
- **Default load [m³/h]**: 未设置时间序列时使用的值
- **Conversion curve [x: kW, y:m³/h]**: 定义从电输入功率到入口流量的传递函数
- **Storage capacity [m³]**: 可延迟负载的最大容量
- **Maximum capacity timeseries [%]**: 定义最大允许存储容量分数的时间序列
- **Default maximum capacity [%]**: 未设置时间序列时使用的值
- **Minimum capacity timeseries [%]**: 定义最小允许存储容量分数的时间序列
- **Default minimum capacity [%]**: 未设置时间序列时使用的值

**稳定性 (Stability)**
- **Relative Operating reserve [pu]**: 所需相对运行备用的时间序列
- **Default relative operating reserve [pu]**: 未设置时间序列时使用的值
- **Peak Operating Reserve [pu]**: 所需峰值运行备用的时间序列
- **Default Peak Operating Reserve [pu]**: 未设置时间序列时使用的值
- **Requires redundancy**: 如果为true，负载需要冗余发电能力

---

## 外部能源网络

### 电网 (Grid)

电网资产代表与外部电力系统的连接。

**主要参数**:
- 电网连接功率限制
- 电价和费率
- 导入/导出限制
- 碳排放因子

### 区域供热/冷却 (District Heating / Cooling)

代表与区域供热或冷却网络的连接。

**主要参数**:
- 供热/冷却功率限制
- 温度设定点
- 成本参数

### 氢气网络 (Hydrogen Network)

代表与外部氢气网络的连接（高压和低压）。

**主要参数**:
- 氢气流量限制
- 压力设定点
- 成本参数

---

## 电气设备

### 电动汽车充电站 (EVStation)

电动汽车充电站管理电动汽车的充电。

**主要参数**:
- 充电功率
- 车辆类型和电池容量
- 充电计划和优先级
- 成本参数

### 内部光伏 (InternalPV)

内部光伏系统基于位置的太阳辐射数据生成功率。

**主要参数**:
- 额定功率 [kW]
- 倾斜角和方位角
- 温度系数
- 效率参数

### 导入光伏 (ImportedPV)

使用导入的时间序列数据的光伏系统。

**主要参数**:
- 额定功率 [kW]
- 导入的功率时间序列

### 风力涡轮机 (Wind Turbine)

风力涡轮机基于位置的风速数据生成功率。

**主要参数**:
- 额定功率 [kW]
- 轮毂高度
- 风速曲线
- 功率曲线

### 导入风力涡轮机 (ImportedWT)

使用导入的时间序列数据的风力涡轮机。

**主要参数**:
- 额定功率 [kW]
- 导入的功率时间序列

### 能源储存系统 (Energy Storage System - ESS)

电能储存系统（如电池）存储电能以供后续使用。

**主要参数**:
- 容量 [kWh]
- 功率 [kW]
- 充放电效率
- 循环寿命
- 成本参数

### 发电机组 (GenSet)

往复式发动机发电机组。

**主要参数**:
- 额定功率 [kW]
- 热平衡表
- 燃料类型
- 启动成本和时间
- 最小/最大功率

### 电缆 (Cable)

电缆连接系统中的不同组件。

**主要参数**:
- 电阻
- 容量
- 成本参数

---

## 热力设备

### 热电联产 (CHP - Combined Heat and Power)

热电联产系统同时生成电力和热力。

**主要参数**:
- 额定电功率 [kW]
- 热平衡表
- 燃料类型
- 热效率
- 电效率

### 燃气轮机 (Gas Turbine)

燃气轮机生成电力。

**主要参数**:
- 额定功率 [kW]
- 热平衡表
- 启动模式
- 温度修正
- 最小/最大功率

### 蒸汽涡轮机 (Steam Turbine)

蒸汽涡轮机从蒸汽生成电力。

**主要参数**:
- 额定功率 [kW]
- 热平衡表
- 蒸汽压力和温度
- 最小/最大功率

### 锅炉 (Boiler)

锅炉使用燃料生成热力。

**主要参数**:
- 额定热功率 [kW]
- 热平衡表
- 燃料类型
- 效率
- 最小/最大功率

### 热泵 (Heat Pump)

热泵使用电力从低温源提取热量并将其传递到高温。

**主要参数**:
- 额定热功率 [kW]
- 热平衡表
- COP (性能系数)
- 源和汇温度
- 最小/最大功率

### 吸收式冷机 (Absorption Chiller)

吸收式冷机使用热力生成冷却。

**主要参数**:
- 额定冷功率 [kW]
- 热平衡表
- 热源温度
- COP
- 最小/最大功率

### 压缩式冷机 (Compression Chiller)

压缩式冷机使用电力生成冷却。

**主要参数**:
- 额定冷功率 [kW]
- 热平衡表
- COP
- 最小/最大功率

### 热储存 (Thermal Storage)

热储存系统存储热能或冷能以供后续使用。

**主要参数**:
- 容量 [kWh]
- 功率 [kW]
- 充放热效率
- 热损耗
- 成本参数

### 热排气 (Thermal Vent)

热排气允许系统释放多余的热力。

**主要参数**:
- 最大排气功率 [kW]
- 成本参数

### 热阀 (Thermal Valve)

热阀控制热流在系统中的流向。

**主要参数**:
- 最大流量
- 压力降
- 成本参数

---

## 氢能设备

### 电解槽 (Electrolyzer)

电解槽使用电力将水分解为氢气和氧气。

**主要参数**:
- 额定氢气产量 [kg/h]
- 热平衡表
- 电效率
- 最小/最大功率
- 启动时间

### 氢气压缩机 (Hydrogen Compressor)

氢气压缩机将氢气压缩到更高的压力。

**主要参数**:
- 额定流量 [kg/h]
- 热平衡表
- 压缩比
- 效率
- 最小/最大功率

### 氢气储存 (Hydrogen Storage)

氢气储存系统存储氢气以供后续使用。

**主要参数**:
- 容量 [kg]
- 功率 [kg/h]
- 充放气效率
- 泄漏率
- 成本参数

### 氢气阀 (Hydrogen Valve)

氢气阀控制氢气在系统中的流向。

**主要参数**:
- 最大流量 [kg/h]
- 压力降
- 成本参数

### 燃料电池 (Fuel Cell)

燃料电池使用氢气生成电力。

**主要参数**:
- 额定功率 [kW]
- 热平衡表
- 效率
- 最小/最大功率
- 启动时间

### 氢气涡轮机 (Hydrogen Turbine)

氢气涡轮机使用氢气生成电力。

**主要参数**:
- 额定功率 [kW]
- 热平衡表
- 效率
- 最小/最大功率
- 启动时间

### 工艺厂 (Process Plant)

工艺厂（如氨厂）使用氢气作为原料进行化学过程。

**主要参数**:
- 额定产量
- 热平衡表
- 原料消耗
- 热需求
- 成本参数

### 其他氢能设备

包括各种辅助设备和专用应用。

---

## 中央设备

### 固定成本 (Fixed Costs)

固定成本资产用于表示与项目相关的固定成本。

**主要参数**:
- 年度固定成本 [EUR/year]
- 成本类别

### 多代理控制 (MGC)

多代理控制系统用于高级调度和控制策略。

**主要参数**:
- 控制参数
- 优先级设置
- 成本参数

### 多步 (Multi-Step)

多步调度器用于复杂的多步优化。

**主要参数**:
- 步长参数
- 优化设置
- 成本参数

---

## 总结

设备选项卡是ISED中配置能源系统的核心。通过理解各种设备类型及其参数，用户可以创建准确反映其特定能源系统的模型。关键是：

1. 选择适当的设备类型
2. 正确配置参数
3. 定义经济参数（CAPEX、OPEX）
4. 设置运行约束和限制
5. 定义替换和维护策略

有关更多详细信息，请参考原始HTML文档或ISED用户手册。
