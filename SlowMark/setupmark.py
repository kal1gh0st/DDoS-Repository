from distutils.core import setup

setup(
    name="SlowMark",
    py_modules=["slowloris"],
    entry_points={"console_scripts": ["slowloris=slowloris:main"]},
    version="0.2.3",
    description="Low bandwidth DoS tool. Slowloris rewrite in Python.",
    author="kal1gh0st",
    author_email="f.fedele@produceict.it",
    url="https://github.com/kal1gh0st/SlowMark",
    keywords=["dos", "http", "slowloris"],
#   license="Custom",
)