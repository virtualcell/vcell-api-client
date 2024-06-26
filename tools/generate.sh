#!/usr/bin/env bash

generatorCliImage=openapitools/openapi-generator-cli:v7.1.0

scriptDir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
parentDir="$(dirname "$scriptDir")"


docker run --rm -v ${scriptDir}:/local ${generatorCliImage} validate -i /local/openapi.yaml --recommend
if [ $? -ne 0 ]; then
    echo "openapi.yaml is not valid"
    exit 1
fi

docker run --rm -v ${parentDir}:/vcell \
${generatorCliImage} generate \
    -g python \
    -i /vcell/tools/openapi.yaml \
    -o /vcell \
    -c /vcell/tools/python-config.yaml
