# -*- encoding: utf-8 -*-
import setuptools

setuptools.setup(
    name="pltb",
    version="1.0.0",
    author="坐公交也用券",
    author_email="liumou.site@qq.com",
    description="这是一个Linux管理脚本的基础库，通过对Linux基本功能进行封装，实现快速开发的效果",
    long_description="这是一个Linux管理脚本的基础库，通过对Linux基本功能进行封装，实现快速开发的效果",
    long_description_content_type="text/markdown",
    url="https://liumou.site",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",

    ],
    # Py版本要求
    python_requires='>=3.0',
    # 依赖
    install_requires=[
     "itsdangerous>=1.1.0",
     "numpy>=1.11.3",
     "opencv-python>=3.4",
     "Pillow>=7.0",
     "rsa>=4.0", ]
)
