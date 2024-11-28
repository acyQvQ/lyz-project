from setuptools import find_packages, setup
import os
from glob import glob

package_name = "learning_tf2_py"

# 正确地定义 data_files 列表
data_files = [
    ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
    ("share/" + package_name, ["package.xml"]),
    # 添加 launch 文件的条目
    (
        os.path.join("share", package_name, "launch"),
        glob(os.path.join("launch", "*launch.[pxy][yma]*")),
    ),
]

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=data_files,  # 使用上面定义的 data_files 列表
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="acy",
    maintainer_email="acy@todo.todo",
    description="TODO: Package description",
    license="Apache-2.0",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "turtle_tf2_broadcaster = learning_tf2_py.turtle_tf2_broadcaster:main",
        ],
    },
)
