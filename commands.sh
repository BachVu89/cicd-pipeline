git clone git@github.com:BachVu89/cicd-pipeline.git
cd cicd-pipeline
make setup
source .cicd-pipeline
make all
az webapp up -n udacity2 -g Azuredevops --sku FREE