pip install datasets huggingface_hub[clie]
huggingface-hub login

echo "Cloning repository."
git clone "https://huggingface.co/datasets/EuropeanParliament/Eurovoc"

echo "Selecting Scandinavian entries."
python3 select_scandi.py

echo "Pushing to HuggingFace Hub"
python3 push_data.py

echo "DONE"
