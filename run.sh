#!/bin/bash
if ! command -v python3 &> /dev/null; then
    echo "Python is not installed. Please install Python before running this script."
    exit 1
fi
if ! command -v pip3 &> /dev/null; then
    echo "pip is not installed. Please install pip before running this script."
    exit 1
fi
if ! pip3 install -r requirements.txt; then
    echo "Failed to install required packages. Please check the requirements file or install the packages manually."
    exit 1
fi
python3 main.py