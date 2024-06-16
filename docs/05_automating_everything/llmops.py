import fileinput
import sys

github_repo="llmops-project"
model_deployment_name="gpt-4"

def modify_file(filename):
    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            line = line.replace('connection: aoai', 'connection: Default_AzureOpenAI')
            line = line.replace('deployment_name: gpt-35-turbo', f'deployment_name: {model_deployment_name}')
            sys.stdout.write(line)

filenames = [f'{github_repo}/named_entity_recognition/flows/standard/flow.dag.yaml',
                f'{github_repo}/named_entity_recognition/flows/post-production-evaluation/flow.dag.yaml']

list(map(modify_file, filenames))