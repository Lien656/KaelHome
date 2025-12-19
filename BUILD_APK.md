name: Build APK

on:
  push:
    branches:
      - main

jobs:
  build:
    name: Build with Buildozer
    runs-on: ubuntu-latest

    steps:
      - name: Check out code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Set up dependencies
        run: |
          sudo apt update
          sudo apt install -y zip unzip openjdk-17-jdk python3-pip git
          python3 -m pip install --upgrade pip
          pip install --upgrade Cython virtualenv
          pip install buildozer

      - name: Build APK
        run: |
          cd ${{ github.workspace }}
          buildozer android debug

      - name: Upload APK
        uses: actions/upload-artifact@v3
        with:
          name: KaelHomeAPK
          path: bin/*.apk