from .coco import CocoDataset
from mmdet.registry import DATASETS


@DATASETS.register_module()
class ArcadeStenosisDataset(CocoDataset):
    METAINFO = {
        'classes': ('stenosis'),
        'palette': [(220, 20, 60)]
    }
    pass
