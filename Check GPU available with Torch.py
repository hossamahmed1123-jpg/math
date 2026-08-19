import torch

print('PyTorch:', torch.__version__)
print('CUDA available:', torch.cuda.is_available())
print('CUDA runtime:', torch.version.cuda)
print('GPU:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'GPU not detected')
print('------------Device Information------------')
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

x = torch.rand(3, 3, device=device)

print(x)
print("Device:", x.device)
print("GPU:", torch.cuda.get_device_name(0))
