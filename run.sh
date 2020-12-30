#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail
set -o xtrace

PYTHON="python"
SCRIPT="flower.py"
TURTLE_DIR="${HOME}/Library/Python/2.7/lib/python/site-packages/turtle"
PYTHON_PKG_DIR="${HOME}/Library/Python/2.7/lib/python/site-packages/"
if [[ -d "${TURTLE_DIR}" ]]; then
  rm -rf "./turtle"
  TK_SILENCE_DEPRECATION=1 "${PYTHON}" "${SCRIPT}"
else
  if [[ ! -d "${PYTHON_PKG_DIR}" ]]; then
    echo "Something wrong!! Please contact xiao wang for help!!!"
    exit 1
  else
    mv "./turtle" ${PYTHON_PKG_DIR}
    TK_SILENCE_DEPRECATION=1 "${PYTHON}" "${SCRIPT}"
  fi
fi
