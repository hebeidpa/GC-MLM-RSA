import os
import h5py
import numpy as np
import pandas as pd
import argparse

def extract_mean_features(h5_file):
    with h5py.File(h5_file, 'r') as f:
        # 自动寻找特征矩阵，默认字段名是 'features'
        if 'features' in f:
            features = f['features'][:]
        else:
            # 自动 fallback：如果有多个 key，只取第一个 matrix-like
            keys = list(f.keys())
            features = f[keys[0]][:]

        if features.ndim != 2:
            raise ValueError(f"{h5_file} 中的特征维度不是二维矩阵，无法处理。")

        return np.mean(features, axis=0)

def batch_h5_to_wsi_csv(input_dir, output_csv):
    all_records = []

    for fname in os.listdir(input_dir):
        if fname.endswith(".h5"):
            wsi_name = os.path.splitext(fname)[0]
            h5_path = os.path.join(input_dir, fname)

            try:
                mean_vec = extract_mean_features(h5_path)
                all_records.append([wsi_name] + mean_vec.tolist())
            except Exception as e:
                print(f"[跳过] {fname} 处理失败：{e}")

    # 保存为 CSV
    df = pd.DataFrame(all_records)
    df.columns = ['wsi'] + [f'feat_{i}' for i in range(df.shape[1] - 1)]
    df.to_csv(output_csv, index=False)
    print(f"[完成] 所有WSI均值特征已保存至：{output_csv}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", required=True, help="包含多个h5文件的目录")
    parser.add_argument("--output_csv", default="WSI_feature_summary.csv", help="输出CSV文件名")
    args = parser.parse_args()

    batch_h5_to_wsi_csv(args.input_dir, args.output_csv)
