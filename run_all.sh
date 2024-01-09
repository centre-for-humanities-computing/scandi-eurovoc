pip install datasets huggingface_hub
huggingface-cli login

echo "Cloning repository."
git lfs clone "https://huggingface.co/datasets/EuropeanParliament/Eurovoc"

echo "Selecting Scandinavian entries."
python3 select_scandi.py

echo "Pushing to HuggingFace Hub"
python3 push_data.py

echo "DONE"
