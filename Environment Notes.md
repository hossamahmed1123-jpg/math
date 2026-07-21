# Check Environment Information
conda info --env
conda --version
python --version

# To Create New Environment
conda create --name py3-math python=3

#Then Activate the environment
conda activate py3-math


(base) C:\Users\hamostafa>conda activate py3-math

(py3-math) C:\Users\hamostafa>python --version
Python 3.14.6
***************************************************
# To Remove environment
> conda env list
> conda env remove --name py3-ml
> conda remove --name py3-ml --all

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

open jupyter_notebook_config.py by notepad and then search for
### DEPRECATED, use root_dir.
### Default: ''

c.ServerApp.notebook_dir = r'D:\hossam\Git\GitHub\math\notebooks'
c.ServerApp.notebook_dir = r'D:\hossam\Git\GitHub\math\notebooks'

# Note to change Jupyter Kernal to new Environment py3-math
*************************************************

Open Anaconda prompt
activate the environment
(base) C:\Users\hamostafa>conda activate py3-math
and then install the ipykernel
(py3-math) C:\Users\hamostafa>conda install ipykernel
Confiler the name
python -m ipykernel install --user --name py3-math --display-name "Python (py3-math)"

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