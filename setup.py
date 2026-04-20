from setuptools import setup, find_packages

# setup.py
setup(
    name='local-ai-assistant',
    version='0.1.0',
    description='A privacy-first AI assistant deeply integrated into Linux OS',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'flask==2.1.1',
        'psutil==5.9.0',
        'SpeechRecognition==3.8.1',
        'pyttsx3==2.90',
        'cryptography==36.0.1',
        'nltk==3.7',
        'scikit-learn==0.24.2',
        'numpy==1.21.0',
        'pillow==8.4.0',
        'requests==2.26.0',
        'Flask-Cors==3.1.1',
    ],
    entry_points={
        'console_scripts': [
            'start-assistant=src.core.assistant:main',  # If you have a main() function in assistant.py
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
