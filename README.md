# 'Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks'

# 1. How to Use

## 1) Image Generation
```bash
# For example,
python3 generate_images.py\
    --ds_name="monet2photo"\
    --data_dir=".../monet2photo/"\
    --x_or_y="x"\
    --ckpt_path=".../monet_to_photo.pth"\
    --n_cpus=0 # Optional
```

# 2. Pre-trained Models and Generated Images
|  | Pre-trained model | Generated images on test set |
| - | - | - |
| Monet to photo | [cyclegan_monet_to_photo.pth](https://drive.google.com/file/d/17FMHYrDzmaC2fQHcBxxjbS758ifKBiHX/view?usp=sharing) | https://github.com/KimRass/CycleGAN/tree/main/generated_images/monet_to_photo |
| Photo to Monet | [cyclegan_photo_to_monet.pth](https://drive.google.com/file/d/1TW8eOKYU3b_6GlhV2Z1FIDZMGjSbh3lW/view?usp=sharing) | https://github.com/KimRass/CycleGAN/tree/main/generated_images/photo_to_monet |
| Vangogh to photo | [cyclegan_vangogh_to_photo.pth](https://drive.google.com/file/d/1tIktlGXTwPZGb-Zu7y-MSWWO304FivaB/view?usp=sharing) | https://github.com/KimRass/CycleGAN/tree/main/generated_images/vangogh_to_photo |
| Photo to Vangogh | [cyclegan_photo_to_vangogh.pth](https://drive.google.com/file/d/1lIJ5eGpCjGvMOcg93-Vnoqy-2y56JXtT/view?usp=sharing) | https://github.com/KimRass/CycleGAN/tree/main/generated_images/photo_to_vangogh |
| Cezanne to photo | [cyclegan_cezanne_to_photo.pth](https://drive.google.com/file/d/1ndKKMMXycJ3KPzWzOUtCrq8lFNlddy3h/view?usp=sharing) | https://github.com/KimRass/CycleGAN/tree/main/generated_images/cezanne_to_photo |
| Photo to Cezanne | [cyclegan_photo_to_cezanne.pth](https://drive.google.com/file/d/1Gz2rK0dSbxU4xgVc7PXueZYsAdVZkCs4/view?usp=sharing) | https://github.com/KimRass/CycleGAN/tree/main/generated_images/photo_to_cezanne |
| Ukiyo-e to photo | [cyclegan_ukiyoe_to_photo.pth](https://drive.google.com/file/d/1BDuSDpdwtOyFSGyNLHSGFZlYIG9ZFRjQ/view?usp=sharing) | https://github.com/KimRass/CycleGAN/tree/main/generated_images/ukiyoe_to_photo |
| Photo to ukiyo-e | [cyclegan_photo_to_ukiyoe.pth](https://drive.google.com/file/d/1fz-l2B0aSWGeF7GcXBH6Rps6TDdXLEzo/view?usp=sharing) | https://github.com/KimRass/CycleGAN/tree/main/generated_images/photo_to_ukiyoe |
| Horse to zebra | [cyclegan_horse_to_zebra.pth](https://drive.google.com/file/d/1dXuPvCiuIBPB63-bmoxX7kMi819HaECh/view?usp=sharing) | https://github.com/KimRass/CycleGAN/tree/main/generated_images/horse_to_zebra |
| Zebra to horse | [cyclegan_zebra_to_horse.pth](https://drive.google.com/file/d/1XWigILmuk1GZtvnVt19Fj6oLFqm57VD3/view?usp=sharing) | https://github.com/KimRass/CycleGAN/tree/main/generated_images/zebra_to_horse |
| Summer to winter | [cyclegan_summer_to_winter.pth](https://drive.google.com/file/d/1pS5sVKw-xO0GcxgG-hc8wn52DlANCxY6/view?usp=sharing) | https://github.com/KimRass/CycleGAN/tree/main/generated_images/summer_to_winter |
| Winter to summer | [cyclegan_winter_to_summer.pth](https://drive.google.com/file/d/1pUIGSXbz3fIyIP44oBQZdcuP5DmqhLDe/view?usp=sharing) | https://github.com/KimRass/CycleGAN/tree/main/generated_images/winter_to_summer |
- 'horse2zebra' dataset의 경우 이미지 중 일부가 화질이 좋지 않거나 이미지의 비율이 왜곡되어 있고 이미지 내에서 말 또는 얼룩말이 차지하는 영역이 매우 작은 등 개인적으로 데이터셋의 품질 자체가 좋지 않다고 생각합니다. 좀 더 대량의, 고품질 데이터셋을 구축하여 다시 학습시켜보면 더욱 우수한 모델을 얻를 수 있을 것입니다.

## 1) Monet to Photo
- <img src="https://github.com/KimRass/CycleGAN/assets/67457712/e7a9a65e-28d0-49e3-befa-5d6d38121276" width="500">
- <img src="https://github.com/KimRass/CycleGAN/assets/67457712/b035ea97-7026-4953-b2df-1a5c70849501" width="500">

## 2) Photo to Monet
- <img src="https://github.com/KimRass/CycleGAN/assets/67457712/4931f46b-3289-4da2-87fe-6a42ffe3c5ab" width="500">
- <img src="https://github.com/KimRass/CycleGAN/assets/67457712/b15db5b1-99d2-41ea-a47b-4ed1a210b034" width="500">

## 3) Vangogh to Photo
- <img src="https://github.com/KimRass/CycleGAN/assets/67457712/4fb3fe43-348a-4c33-91c1-7b8aec06a4c5" width="500">
- <img src="https://github.com/KimRass/CycleGAN/assets/67457712/19f20bab-a806-4479-a83a-6a7dc05f9b8d" width="500">
## 4) Photo to Vangogh
- <img src="https://github.com/KimRass/CycleGAN/assets/67457712/5b25f493-fe90-4ca9-8bf0-b605bd109644" width="500">
- <img src="https://github.com/KimRass/CycleGAN/assets/67457712/b258bfd9-17d9-4042-a4c2-2d5ce9ce6b15" width="500">

## 5) Cezanne to Photo
- <img src="https://github.com/KimRass/CycleGAN/assets/105417680/bb670df1-bb5a-4c82-9cce-be177f1a117e" width="500">
- <img src="https://github.com/KimRass/CycleGAN/assets/105417680/8d795340-805e-4ba0-9134-94dd7b818f60" width="500">
- <img src="https://github.com/KimRass/CycleGAN/assets/105417680/42d1e1cb-7976-4aaa-a9ba-c78a72ba3b59" width="500">

## 6) Photo to Cezanne
- <img src="https://github.com/KimRass/CycleGAN/assets/105417680/10b94202-d540-4df5-8d53-866222c14909" width="500">
- <img src="https://github.com/KimRass/CycleGAN/assets/105417680/a414b384-b150-4570-90d4-4209ab75972a" width="500">

## 7) Ukiyoe to Photo
- <img src="https://github.com/KimRass/CycleGAN/assets/105417680/94157d1e-816e-4b6b-93bb-b6a6e2fa88e1" width="500">
- <img src="https://github.com/KimRass/CycleGAN/assets/105417680/9b0e7490-224d-4866-86a3-f074998e2e6b" width="500">

## 8) Photo to Ukiyoe
- <img src="https://github.com/KimRass/CycleGAN/assets/67457712/9ec58775-01ce-438f-8c74-1304f84b62c4" width="500">
- <img src="https://github.com/KimRass/CycleGAN/assets/67457712/8a65401f-3d59-4e9f-91b8-f3b8060c511a" width="500">

## 9) Horse to Zebra
- <img src="https://github.com/KimRass/CycleGAN/assets/67457712/cf001a04-8019-4099-bcf0-759f56f61291" width="500">
- <img src="https://github.com/KimRass/CycleGAN/assets/67457712/794003e9-bf04-458e-9d23-31c4654b3909" width="500">
- <img src="https://github.com/KimRass/CycleGAN/assets/67457712/7f222da0-b364-455d-b7e6-ddb849ed3f7c" width="500">
- <img src="https://github.com/KimRass/CycleGAN/assets/67457712/d580a23c-0730-4b5b-bb05-b3c8cbc4a93e" width="500">
- <img src="https://github.com/KimRass/CycleGAN/assets/67457712/678f546f-9a4e-493f-b6d1-d02fb4b7d533" width="500">

## 10) Zebra to Horse
- <img src="https://github.com/KimRass/CycleGAN/assets/67457712/91c2a91e-3460-4186-ac43-7f8283617826" width="500">
- <img src="https://github.com/KimRass/CycleGAN/assets/67457712/dd401699-adf2-4b86-95d0-8d8b1a9218e0" width="500">
- <img src="https://github.com/KimRass/CycleGAN/assets/67457712/3f6c7df9-e47e-4717-b85c-dadea93e281e" width="500">

# 3. Implementation Details
- 논문만 가지고는 정확히 알기 어려운 부분 또는 논문과 공식 저장소가 서로 다른 부분이 많은데, 공식 저장소를 기준으로 구현했습니다.

## 1) Optimizer Merging
- discriminators (Dx와 Dy)와 generators (Gx와 Gy)의 objective는 방향성이 서로 충돌하지만 (adversarial training) Dx와 Dy 그리고 Gx와 Gy는 서로 objective의 방향성이 동일하므로, Dx의 Optimizer와 Dy의 Optimizer를 하나로 합치고, Gx의 Optimizer와 Gy의 Optimizer를 하나로 합쳤습니다.
- As-is:
    ```python
    disc_x_optim = Adam(params=disc_x.parameters(), lr=lr)
    disc_y_optim = Adam(params=disc_y.parameters(), lr=lr)
    gen_x_optim = Adam(params=gen_x.parameters(), lr=lr)
    gen_y_optim = Adam(params=gen_y.parameters(), lr=lr)
    ```
- To-be:
    ```python
    disc_optim = Adam(params=list(disc_x.parameters()) + list(disc_y.parameters()), lr=lr)
    gen_optim = Adam(params=list(gen_x.parameters()) + list(gen_y.parameters()), lr=lr)
    ```

## 2) Padding Mode
- 논문에서는 모든 padding에 대해서 `padding_mode="reflect"`를 사용한 것처럼 쓰여 있으나 공식 저장소를 보면 `padding_mode="zeros"`와 `padding_mode="reflect"`를 혼용하고 있어 이를 따랐습니다.

## 3) Random Image Pairing
- 이미지의 집합 X와 Y의 크기가 서로 다르므로 만약 X의 크기가 Y의 크기보다 크다면 1 epoch 동안 X의 이미지가 한 번씩 모델에 입력으로 들어갈 때 Y의 이미지는 한 번 이상씩 모델에 입력으로 들어가게 됩니다. 즉 X의 크기가 데이터의 크기가 됩니다. 이 점을 간과해 데이터의 크기를 Y의 크기와 같게 했고 X와 Y의 각 원소를 정해진대로 1:1 대응이 되도록 코드를 짰었으나 이를 수정했습니다.
- As-is:
    ```python
    x_path = self.x_paths[idx]
    y_path = self.y_paths[idx]
    ```
- To-be:
    ```python
    if self.x_len >= self.y_len:
        x_path = self.x_paths[idx]
        y_path = random.choice(self.y_paths)
    else:
        y_path = self.y_paths[idx]
        x_path = random.choice(self.x_paths)
    ```

## 4) LSGANs
- 논문에 따르면 objective로서 'negative log likelihood' (`GAN_CRIT = nn.BCEWithLogitsLoss()`) 대신에 'least-squares' (`GAN_CRIT = nn.MSELoss()`)를 사용합니다. [1] 전자를 사용할 경우 금방 mode collapse가 발생하는 것을 관찰할 수 있었습니다.

# 4. Gatys et al. (2016)
- Please refer to my another repository [Gatys et al.](https://github.com/KimRass/Gatys-et-al.)

# 5. References
- [1] [Least Squares Generative Adversarial Networks](https://github.com/KimRass/CycleGAN/blob/main/papers/least_squares_generative_adversarial_networks.pdf)
