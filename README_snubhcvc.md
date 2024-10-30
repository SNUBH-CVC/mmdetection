## Installation
```
python setup.py develop

wandb init  # set project name and log in
```

Download MAE pretrained model from [here](https://dl.fbaipublicfiles.com/mae/pretrain/mae_pretrain_vit_base.pth)

## Training
```bash
# Arcade Stenosis Detection
CUDA_VISIBLE_DEVICES=0,1 PORT=29500 tools/dist_train.sh configs/detr/detr_r50_8xb2-150e_arcade-stenosis.py 2
CUDA_VISIBLE_DEVICES=0,1 PORT=29500 tools/dist_train.sh projects/ViTDet/configs/vitdet_mask-rcnn_vit-b-mae_lsj-100e_arcade-stenosis-instance.py 2
```

## Dataset
### Arcade Stenosis Detection
- Download from [here](https://zenodo.org/records/10390295)
- 서로 다른 image_id에 대한 annotation id 중복이 발생해서 `annotation file is not unique` 에러가 발생한다. 
- 이를 해결하기 위해 `tools/dataset_converters/arcade_stenosis.py`를 실행.

## Issues
DETR 학습 시 mAP가 0이 되는 문제 발생. [issue](https://github.com/open-mmlab/mmdetection/issues/8222)

ViTDet 학습을 위해서 mmcv GPU compilation을 해야 한다. [issue](https://github.com/open-mmlab/mmdetection/issues/11454), [compilation 방법](https://mmcv.readthedocs.io/en/latest/get_started/build.html#build-mmcv-from-source)
```
git clone https://github.com/open-mmlab/mmcv.git
cd mmcv && git checkout v2.1.0
pip install -v -e .
```

## References
- [iBOT evaluation code - ViTDet](https://github.com/bytedance/ibot/tree/main/evaluation)
