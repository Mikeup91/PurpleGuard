from setuptools import setup, find_packages

setup(
    name="purpleguard",
    version="2.0.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "dnspython",
    ],
    entry_points={
        "console_scripts": [
            "purpleguard=omnibus:main",
        ],
    },
    author="Your Name/Nexus Dev",
    description="High-performance multi-vector vulnerability swarm engine",
    python_requires=">=3.8",
)
