from setuptools import setup, find_packages

setup(
    name="solscan-my-plugins",
    description="This is an example of detectors and printers to Solscan.",
    url="https://github.com/khulnasoft-lab/solscan-plugins",
    author="Trail of Bits",
    version="0.0",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=["solscan-analyzer==0.1"],
    entry_points={
        "solscan_analyzer.plugin": "solscan my-plugin=solscan_my_plugin:make_plugin",
    },
)
