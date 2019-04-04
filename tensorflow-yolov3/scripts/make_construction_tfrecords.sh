python core/convert_tfrecord.py --dataset_txt ./construction_dataset/construction_train.txt --tfrecord_path_prefix ./construction_dataset/construction_train
python core/convert_tfrecord.py --dataset_txt ./construction_dataset/construction_dev.txt  --tfrecord_path_prefix ./construction_dataset/construction_dev
python core/convert_tfrecord.py --dataset_txt ./construction_dataset/construction_test.txt  --tfrecord_path_prefix ./construction_dataset/construction_test
