This is a test version of Diagnostic GUI.

The GUI Folder contains the diagnostic GUI.
The Test Folde contains code for testing each individual compoenent such as pumps, valves, TEC Controller, motors, and bubble sensor



To run the code, first you need to create the python environment. To create the environment, follow the steps in section 1. If you have already created the environment, go to section 2.


## Section 1: Creating the envirnment
  Step 1: Create folder on your computer and copy the file "requirement.yml" in the folder    
  
  Step 2: Open an anaconda power prompt
  
  Step 3: Change the current folder on the anaconda power prompt to the folder you just careated  
  
  Step 4: Use the command below to create the environment:  
            **conda env update --name envname --file environment.yml**            
        Note: "envname" is the name of environment. For example, the command below creates an environment named "Malvaern":        
            **conda env update --name Malvern --file .\environment.yml** 
  

## Section 2: Running the app:
  Step 1: Copy the code in the folder you created for this application 
  
  Step 2: Activate the conda environment using command below:
            conda activate "envname"
        Note envname is the name of environment. 
        For example, to activate an environment called "Malvern" use the command below:
            conda activate Malver
            
  Step 3:
        Run the app using the command below:
            python run_GUI.py
