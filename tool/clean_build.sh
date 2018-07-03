# run it at parent dir, not tool dir
rm -rf build
rm -rf dist
rm -rf lixinger_openapi.egg-info
python3 setup.py sdist bdist_wheel
