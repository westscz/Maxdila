import yaml

with open("/home/jarek/Projects/Maxdila/pl.yml", 'r') as stream:
    try:
        Lang = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)