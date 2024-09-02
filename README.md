# 一些函数的用法详解

>## 基本函数<`nest.Create()`>

>>### [generator : 生成](https://nest-simulator.readthedocs.io/en/stable/devices/stimulate_the_network.html#stimulate-network)
>>#### 'generator' 用法
>>基本格式 `nest.Create()`  
以‘dc_generator’为例, 创建一个恒定直流输入：  
`dc_generator = nest.Create('dc_generator', params={})`




---
>>### 生成1： 电流/尖峰发生器
---
>>#### 'ac_generator': *[生成交流电](https://nest-simulator.readthedocs.io/en/stable/models/ac_generator.html)*
```
ac_generator = nest.Create(
    'ac_generator',
    params = {
        'label': XXX,
        'origin': XXX,
        'start': XXX,
        'stop': XXX,
        'stimulus_source': XXX,
        'amplitude': XXX,
        'offset': XXX,
        'frequency': XXX,
        'phase': XXX
    }
)
```
---
>>#### 'dc_generator': *[生成直流电](https://nest-simulator.readthedocs.io/en/stable/models/dc_generator.html)*
---
#### 'noise_generator': *[生成高斯白噪声电流(Gaussian white noise current)](https://nest-simulator.readthedocs.io/en/stable/models/noise_generator.html)*
---
#### 'step_current_generator': *[生成分段恒定直流电流](https://nest-simulator.readthedocs.io/en/stable/models/step_current_generator.html)*
---
#### 'poisson_generator': *[生成泊松尖峰(Poisson spikes)](https://nest-simulator.readthedocs.io/en/stable/models/poisson_generator.html)*
---
#### 'spike_generator': *[根据给定尖峰时间生成尖峰](https://nest-simulator.readthedocs.io/en/stable/models/spike_generator.html)*

---
#### 'spike_train_injector': *[发出规定尖峰序列的神经元](https://nest-simulator.readthedocs.io/en/stable/models/spike_train_injector.html)*

---  
---
\
**参数表**
| `ac_generator` | | `dc_generator` || | `noise_generator` | | `step_current_generator` | | `poisson_generator` | | `spike_generator` | | `spike_train_injector` | |
|:--------------:|:-:|:--------------:|:---:|:---:|:-----------------:|:-:|:------------------------:|:-:|:-------------------:|:-:|:------------------:|:-:|:------------------------:|:-:|
| 参数 | 说明 | 参数 | 说明 |数据类型/数据单位| 参数 | 说明 | 参数 | 说明 | 参数 | 说明 | 参数 | 说明 | 参数 | 说明 |
| label | × | label | × || label | * | label | * | label | * | label | * | label | * |
| origin | × | origin | ×| | origin | * | origin | * | origin | * | origin | * | origin | * |
| start | 刺激开始时间，以`nest.Simulate()`时间为标准 | start | 刺激开始时间，以`nest.Simulate()`时间为标准 || start | 刺激开始时间，以`nest.Simulate()`时间为标准 | start | 刺激开始时间，以`nest.Simulate()`时间为标准 | start | 刺激开始时间，以`nest.Stimulate()`时间为标准 | start | 刺激开始时间，以`nest.Simulate()`时间为标准 | start | 刺激开始时间，以`nest.Simulate()`时间为标准 |
| stop | 刺激结束时间，以`nest.Simulate()`时间为标准 | stop | 刺激结束时间，以`nest.Simulate()`时间为标准 || stop | 刺激结束时间，以`nest.Simulate()`时间为标准 | stop | 刺激结束时间，以`nest.Simulate()`时间为标准 | stop | 刺激结束时间，以`nest.Simulate()`时间为标准 | stop | 刺激结束时间，以`nest.Simulate()`时间为标准 | stop | 刺激结束时间，以`nest.Simulate()`时间为标准 |
| stimulus_source | × | stimulus_source | × || stimulus_source | * | stimulus_source | * | stimulus_source | * | stimulus_source | * | stimulus_source | * |
| amplitude | × | amplitude | 设置输入的电流大小 |pA| mean | * | amplitude_times | * | rate | * | spike_times | * | spike_times | * |
| offset | × | × | × || std | * | amplitude_values | * | * | * | spike_weights | * | × | * |
| frequency | × | × | × || dt | * | allow_offgrid_times | * | * | * | spike_multiplicities | * | spike_multiplicities | * |
| phase | × | × | × || std_mod | * | | | | | precise_times | * | precise_times | * |
| | | | || frequency | * | | | | | allow_offgrid_times | * | allow_offgrid_times | * |
| | | | | |phase | * | | | | | shift_now_spikes | * | shift_now_spikes | * |
---


>>### 生成2： 记录器
#### multimeter: *[记录连续量：电压、电流等](https://nest-simulator.readthedocs.io/en/stable/models/multimeter.html#models-multimeter--page-root)*
```
multimeter = nest.Create(
    'multimeter',
    1,
    params = {
        'label': XXX,
        'n_events': XXX,
        'origin': XXX,
        'record_to': XXX,
        'start': XXX,
        'stop': XXX,
        'record_from': XXX,
        'interval': XXX,

    }
)
```
---
#### spike_recorder: *[记录尖峰](https://nest-simulator.readthedocs.io/en/stable/models/spike_recorder.html)*
---
#### weight_recorder *[记录突触权重](https://nest-simulator.readthedocs.io/en/stable/models/weight_recorder.html)*
---
---
**参数表**
|`multimeter`||`spike_recorder`||`weight_recorder`||
|:---:|:---:|:---:|:---:|:---:|:---:|
|参数|说明|参数|说明|参数|说明|
|label||label||label||
|n_events||n_events||n_events||
|origin|正浮点数，启动和停止的参考时间，默认为0.0|origin|正浮点数，启动和停止的参考时间，默认为0.0|origin|正浮点数，启动和停止的参考时间，默认为0.0|
|record_to||record_to||record_to||
|start|记录开始时间，以`nest.Simulate()`时间为标准|start|记录开始时间，以`nest.Simulate()`时间为标准|start|记录开始时间，以`nest.Simulate()`时间为标准|
|stop|记录结束时间，以`nest.Simulate()`时间为标准|stop|记录结束时间，以`nest.Simulate()`时间为标准|stop|记录结束时间，以`nest.Simulate()`时间为标准|
|record_from|选择要记录的连续量，获取可记录的连续量类型可参照表下，**格式：list**, 举例：`{'record_from': ['V_m, 'g_ex']}`||||
|interval|记录的采样间隔，可使用`{'interval': 0.1}`或`nest.SetStatus(multimeter, {'interval': 0.1})`来指定||||
---
\
如何获得可以记录的连续量，
以模型`iaf_cond_alpha`为例
```
>>> nest.GetDefaults('iaf_cond_alpha')['recordables']
['g_ex', 'g_in', 't_ref_remaining', 'V_m']
```
*注意：`nest.GetDefaults()['']`形式（目前据我所知）只对模型参数（`iaf_cond_alpha`之类）有效，若已经创建了`neuron = nest.Create()`，可使用`nest.GetStatus(neuron, 'recordables')`来获取可记录的连续量，若要获取其他参数，替换`recordables`即可。*

---


## List of Synapse Models

- bernoulli_synapse
- clopath_synapse
- cont_delay_synapse
- diffusion_connection
- eprop_synapse_bsshslm_2020
- gap_junction
- ht_synapse
- jonke_synapse
- quantal_stp_synapse
- rate_connection_delayed
- rate_connection_instantaneous
- sic_connection
- static_synapse
- static_synapse_hom_w
- stdp_dopamine_synapse
- stdp_facetshw_synapse_hom
- stdp_nn_pre_centered_synapse
- stdp_nn_restr_synapse
- stdp_nn_symm_synapse
- stdp_pl_synapse_hom
- [stdp_synapse](https://nest-simulator.readthedocs.io/en/stable/models/stdp_synapse.html): Synapse type for spike-timing dependent plasticity  
>Parameters

>|参数|数据类型/数据单位|说明|
>|:---:|:---:|:---:|
>|tau_plus|ms|Time constant of STDP window, potentiation (tau_minus defined in postsynaptic neuron)|
>|lambda|real|Step size|
>|alpha|real|Asymmetry parameter (scales depressing increments as alpha*lambda)|
>|mu_plus|real|Weight dependence exponent, potentiation|
>|mu_minus|real|Weight dependence exponent, depression|
>|Wmax|real|Maximum allowed weight|
- stdp_synapse_hom
- stdp_triplet_synapse
- tsodyks2_synapse
- tsodyks_synapse
- tsodyks_synapse_hom
- urbanczik_synapse
- vogels_sprekeler_synapse


# Example of how to use functions in NEST  



| Function_name | associated_file in Python | original_name | file_link |
| :---: | :------: | :------: | :---: |
multimeter |[Example of multimeter recording to file](TutorialExample_of_multimeter_recording_to_file.ipynb) |Example of multimeter recording to file| [original link in NEST](https://nest-simulator.readthedocs.io/en/stable/auto_examples/multimeter_file.html)|Example of multimeter recording to file|
|

