## Installation
```
python setup.py develop
```

## Training
```bash
# Arcade Stenosis Detection
CUDA_VISIBLE_DEVICES=1 PORT=29500 tools/dist_train.sh configs/detr/detr_r50_8xb2-150e_arcade-stenosis.py 1
```

## Dataset
### Arcade Stenosis Detection
- Download from [here](https://zenodo.org/records/10390295)
- 서로 다른 image_id에 대한 annotation id 중복이 발생해서 `annotation file is not unique` 에러가 발생한다. 
- 이를 해결하기 위해 `tools/dataset_converters/arcade_stenosis.py`를 실행.