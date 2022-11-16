import setuptools

setuptools.setup(
    name="face_detection_dsfd",
    version="1.0",
    author="Håkon Hukkelås",
    description="A simple and lightweight package for state of the art face detection with GPU support.",
    long_description_content_type="text/markdown",
    package_data={'': ['license.txt']},
    include_package_data=True,
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
