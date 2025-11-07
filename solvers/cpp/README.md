# installation
# required python3+ version
python -m venv venv

# launch venv
pip install -r requirements.txt

# create profile for current machine  
conan profile detect --force

# update standart version in default conan profile
gnu20

# next install required packaged from conanfile.txt
mkdir build
cd build

# this command will configure build directories and CMakeUserPresets.json used in IDE
conan install .. --build=missing --output-folder=Release-build -s build_type=Release
conan install .. --build=missing --output-folder=Debug-build -s build_type=Debug

