# snpe

Qualcomm’s SNPE does not run ONNX files directly

converte into SNPE’s internal Deep Learning Container (.dlc) format


## deps

Install SNPE SDK on Host


## step1
 ONNX models, use the snpe-onnx-to-dlc converter.

```

${SNPE_ROOT}/bin/x86_64-linux-clang/snpe-onnx-to-dlc \
    --input_network model.onnx \
    --output_path model.dlc \
    --input_dim 'input_node_name' 1,3,224,224

```



## step2
* Quantize the Model for the Hexagon NPU (DSP Acceleration)
* The Hexagon NPU excels at fixed-point (INT8/INT16) inference for maximum throughput and efficiency. 
* SNPE provides a tool snpe-dlc-quant to quantize the DLC model to INT8 or INT16
* Quantization will reduce model precision (with minimal accuracy impact if calibration is done correctly) in exchange for being able to run on the DSP/NPU



### Prepare Calibration Data


### Run SNPE DLC Quantization

```
${SNPE_ROOT}/bin/x86_64-linux-clang/snpe-dlc-quant \
    --input_dlc model.dlc \
    --output_dlc model_quantized.dlc \
    --input_list calib_list.txt 
```

The output file (e.g. model_quantized.dlc) contains the fixed-point model.



## runtime
* Install/Copy SNPE Runtime:
* SNPE provides a snpe-platform-validator tool to check that the GPU/DSP runtimes are supported on the target. Running this can confirm that the Adreno GPU driver and Hexagon driver are compatible. 
* SNPE can execute models via its C++ API or via provided utilities
* snpe-net-run is a convenient CLI tool that loads a DLC and runs inference.

```
snpe-net-run --container model_quantized.dlc \
             --input_list input_list.txt \
             --output_dir output_dsp \
             --use_dsp 

```


you can run multiple SNPE processes or threads, each bound to a different runtime (one with --use_dsp, another with --use_gpu).