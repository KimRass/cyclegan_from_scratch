from torch.utils.data import Dataset
import torchvision.transforms as T
import torchvision.transforms.functional as TF
from PIL import Image
from pathlib import Path
import random


class Monet2PhotoDataset(Dataset):
    def __init__(
        self,
        data_dir,
        x_mean,
        x_std,
        y_mean,
        y_std,
        split="train",
    ):
        super().__init__()

        self.x_mean = x_mean
        self.x_std = x_std
        self.y_mean = y_mean
        self.y_std = y_std
        self.split = split

        self.x_paths = list(Path(data_dir).glob(f"""{split}A/*.jpg"""))
    
    def transform(self, x, y):
        if self.split == "train":
            if random.random() > 0.5:
                x = TF.hflip(x)
            if random.random() > 0.5:
                y = TF.hflip(y)

        x = T.ToTensor()(x)
        x = T.Normalize(mean=self.x_mean, std=self.x_std)(x)

        y = T.ToTensor()(y)
        y = T.Normalize(mean=self.y_mean, std=self.y_std)(y)
        return x, y

    def __len__(self):
        return len(self.x_paths)

    def __getitem__(self, idx):
        x_path = self.x_paths[idx]
        y_path = str(x_path).replace(f"/{self.split}A/", f"/{self.split}B/")
        y_path = y_path.replace("_A.jpg", "_B.jpg")

        x = Image.open(x_path).convert("RGB")
        y = Image.open(y_path).convert("RGB")
        x, y = self.transform(x, y)
        return x, y
