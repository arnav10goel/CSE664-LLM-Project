import papermill as pm

# Define the list of language pairs you want to run
languages = ["tamil", "telugu", "bengali"]

# Path to your Jupyter notebook
notebook_path = "/home/vijay/slim_sense/SHARPax/Python_code/test/NER-Experiments/FineTune-Experiments-OneLang/FineTune-Hindi.ipynb"
output_dir = "/home/vijay/slim_sense/SHARPax/Python_code/test/NER-Experiments/FineTune-Experiments-OneLang/"

for language in languages:
    output_notebook = f"{output_dir}/FineTune-{language}.ipynb"
    print(f"Running notebook for language: {language}")
    
    # Execute the notebook with the specified parameters
    pm.execute_notebook(
        input_path=notebook_path,
        output_path=output_notebook,
        parameters={
            "language": language,
        }
    )

print("All notebooks executed successfully.")

# nohup python notebooks_script.py > output.log 2>&1 &