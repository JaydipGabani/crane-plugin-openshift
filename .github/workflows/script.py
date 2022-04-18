import os
import yaml
import sys

os.makedirs('plugins/OpenShift', exist_ok=True)

if os.path.exists("index.yml"):
    file = open("index.yml","r")
    not_present = 1
    index = yaml.safe_load(file)
    for plugin in index['plugins']:
        if plugin['name'] == 'OpenShiftPlugin':
            not_present = 0
            break
    if not_present:
        index['plugins'].append({"name": "OpenShiftPlugin", "path": "https://github.com/%s/crane-plugins/raw/main/plugins/OpenShift/index.yaml"%sys.argv[1]})
    file = open("index.yml","w")
    yaml.dump(index, file)
    file.close()

else:
    file = open("index.yml","a+")

    index = yaml.safe_load(file)

    index = {}
    index['kind'] = 'PluginIndex'
    index['apiServer'] = 'konveyor.io/v1alpha1'
    index['plugins'] = []

    index['plugins'].append({"name": "OpenShiftPlugin", "path": "https://github.com/%s/crane-plugins/raw/main/plugins/OpenShift/index.yaml"%sys.argv[2]})

    yaml.dump(index, file)
    file.close()

# create or append in plugin index
if os.path.exists('plugins/OpenShift/index.yml'):

    file = open("plugins/OpenShift/index.yml","r")

    index = yaml.safe_load(file)

    index['versions'].append({})
    index['versions'][-1] = {
        'name': 'OpenShiftPlugin',
        'shortDescription': 'OpenShiftPlugin',
        'description': 'this is OpenShiftPlugin',
        'version': sys.argv[1],
        'binaries': [
            {
                'os': 'linux',
                'arch': 'amd64',
                'uri': "https://github.com/%s/releases/download/%s/amd64-linux-openshiftplugin-%s"%(sys.argv[3], sys.argv[1],sys.argv[1]),
            },
            {
                'os': 'darwin',
                'arch': 'amd64',
                'uri': "https://github.com/%s/releases/download/%s/amd64-darwin-openshiftplugin-%s"%(sys.argv[3], sys.argv[1],sys.argv[1]),
            },
            {
                'os': 'darwin',
                'arch': 'arm64',
                'uri': "https://github.com/%s/releases/download/%s/arm64-darwin-openshiftplugin-%s"%(sys.argv[3], sys.argv[1],sys.argv[1]),
            },
        ],
    }

    file = open("plugins/OpenShift/index.yml","w")

    yaml.dump(index, file)
    file.close()
    
else:
    file = open("plugins/OpenShift/index.yml","a+")

    index = yaml.safe_load(file)

    index = {}
    index['kind'] = 'Plugin'
    index['apiServer'] = 'konveyor.io/v1alpha1'
    index['versions'] = []

    index['versions'].append({})
    index['versions'][0] = {
        'name': 'OpenShiftPlugin',
        'shortDescription': 'OpenShiftPlugin',
        'description': 'this is OpenShiftPlugin',
        'version': sys.argv[1],
        'binaries': [
            {
                'os': 'linux',
                'arch': 'amd64',
                'uri': "https://github.com/%s/releases/download/%s/amd64-linux-openshiftplugin-%s"%(sys.argv[3], sys.argv[1],sys.argv[1]),
            },
            {
                'os': 'darwin',
                'arch': 'amd64',
                'uri': "https://github.com/%s/releases/download/%s/amd64-darwin-openshiftplugin-%s"%(sys.argv[3], sys.argv[1],sys.argv[1]),
            },
            {
                'os': 'darwin',
                'arch': 'arm64',
                'uri': "https://github.com/%s/releases/download/%s/arm64-darwin-openshiftplugin-%s"%(sys.argv[3], sys.argv[1],sys.argv[1]),
            },
        ],
    }
    
    yaml.dump(index, file)
    file.close()