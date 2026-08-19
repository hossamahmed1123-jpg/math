# Recommended: recreate py3-math with Python 3.12

This deletes and rebuilds the environment, so run it only when you do not need to preserve its current packages.

1. Remove the current environment

Open Anaconda Prompt:

> conda deactivate

> conda env remove --name py3-math

Confirm:

conda env list

2. Recreate it with Python 3.12

conda create --name py3-math python=3.12 -y

conda activate py3-math

Confirm:

python --version

Expected:

Python 3.12.x

3. Upgrade pip

> python -m pip install --upgrade pip setuptools wheel

4. Install TensorFlow

For your work PC without NVIDIA, install the Windows CPU version:

python -m pip install tensorflow

Or install the current specific release:

python -m pip install tensorflow==2.21.0

TensorFlow 2.21 provides Windows wheels for supported Python versions, including Python 3.12 and 3.13.

5. Install CPU PyTorch in the same environment

python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

7. Verify both libraries

python -c "import torch; import tensorflow as tf; print('PyTorch:', torch.__version__); print('TensorFlow:', tf.__version__); print('PyTorch CUDA:', torch.cuda.is_available()); print('TensorFlow GPUs:', tf.config.list_physical_devices('GPU'))"

On the work PC, this is normal:

PyTorch CUDA: False

TensorFlow GPUs: []

# Register the rebuilt environment in Jupyter

python -m pip install ipykernel

jupyter kernelspec uninstall py3-math -f

python -m ipykernel install --user --name py3-math --display-name "Python (py3-math)"

Restart Jupyter, then select:

Kernel → Change Kernel → Python (py3-math)

Verify inside the notebook:

import sys

import torch

import tensorflow as tf

print(sys.executable)

print("PyTorch:", torch.__version__)

print("TensorFlow:", tf.__version__)

The Python path should be:

C:\Users\hamostafa\anaconda3\envs\py3-math\python.exe

****************************************************

# Check Environment Information
> conda info --env

> conda --version
> python --version

# To Create New Environment
********************************************
conda create --name py3-math python=3

# Then Activate the environment
conda activate py3-math


(base) C:\Users\hamostafa>conda activate py3-math

(py3-math) C:\Users\hamostafa>python --version

Python 3.14.6

# install necessary packages
If you face an issue you can run install command package by package
> conda install numpy pandas matplotlib scikit-learn

**************************************************
# To Remove environment

> conda env list

> conda env remove --name py3-ml

> conda remove --name py3-ml --all

> conda remove --name math --all

> conda remove --name lab --all
***************************************************

I change the setting for This project from Project Setting

File > Setting > Interpreter >
(Add Existing Environment) And Then Choose Conda environment
Path :
C:\Users\hamostafa\AppData\Local\anaconda3\condabin\conda.bat
# To Install Package to environment direct
*****************************************************
From Pycharm Terminal Run the following command

(py3-math) PS D:\hossam\Git\GitHub\math> conda install numpy
## Note to change Jupyter Folder Path
******************************************************
Shut down the Jupyter notebook frist if it is opened

Open Anaconda Prompt
Then run
jupyter notebook --generate-config
The file will be generated in the following path :
Writing default config to:
Ex.
C:\Users\YourName\.jupyter\jupyter_notebook_config.py

C:\Users\hamostafa\.jupyter

On My Laptop Machine 

C:\Users\hossa\.jupyter
open jupyter_notebook_config.py by notepad and then search for

### Inside the file   jupyter_notebook_config.py 

*************************************************
DEPRECATED, use root_dir.

Default: ''

c.ServerApp.notebook_dir = r'D:\hossam\Git\GitHub\math\notebooks'

My Laptop

c.ServerApp.notebook_dir = r'D:\hossam\Git\GitHub\math\notebooks'

*************************************************

# Note to change Jupyter Kernal to new Environment py3-math
*************************************************
### Open Anaconda prompt

### Activate the environment

(base) C:\Users\hamostafa>conda activate py3-math

### install the ipykernel
and then install the ipykernel

> conda install ipykernel

> (py3-math) C:\Users\hamostafa>conda install ipykernel

### Confiler the name

> python -m ipykernel install --user --name py3-math --display-name "Python (py3-math)"

# To Remove its Jupyter kernel
****************************************************************************

1. Remove its Jupyter kernel entry

Sometimes the environment is deleted, but its kernel name still appears in Jupyter.

List registered kernels:

jupyter kernelspec list

Then remove the old kernel:

jupyter kernelspec uninstall py3-ml

Confirm by entering:

y

For your setup, the safest sequence is:

conda deactivate
conda env remove --name py3-ml
jupyter kernelspec uninstall py3-ml
********************************************************************************