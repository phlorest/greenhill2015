from setuptools import setup


setup(
    name='cldfbench_greenhill2015',
    py_modules=['cldfbench_greenhill2015'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'greenhill2015=cldfbench_greenhill2015:Dataset',
        ]
    },
    install_requires=[
        'phlorest',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
