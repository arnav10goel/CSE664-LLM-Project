import papermill as pm

# Define the list of language pairs you want to run
language_pairs = [
    ("hindi", "marathi"),
    ("hindi", "telugu"),
    ("marathi", "bengali"),
    ("marathi", "tamil"),
    ("marathi", "telugu"),
    ("tamil", "bengali"),
    ("tamil", "telugu"),
    ("telugu", "bengali")
]

# Path to your Jupyter notebook
notebook_path = "/home/vijay/slim_sense/SHARPax/Python_code/test/NER-Experiments/FineTune-Experiments-TwoLang/FineTune-Hindi-Bengali.ipynb"
output_dir = "/home/vijay/slim_sense/SHARPax/Python_code/test/NER-Experiments/FineTune-Experiments-TwoLang/"

for lang1, lang2 in language_pairs:
    output_notebook = f"{output_dir}/FineTune-{lang1}-{lang2}.ipynb"
    print(f"Running notebook for lang1: {lang1}, lang2: {lang2}")
    
    # Execute the notebook with the specified parameters
    pm.execute_notebook(
        input_path=notebook_path,
        output_path=output_notebook,
        parameters={
            "lang1": lang1,
            "lang2": lang2
        }
    )

print("All notebooks executed successfully.")

# nohup python notebooks_script.py > output.log 2>&1 &