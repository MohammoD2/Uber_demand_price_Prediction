from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='The Uber Demand Prediction project aims to forecast future cab demand across New York City using advanced machine learning techniques. By analyzing historical ride data, including time-stamped trips, weather patterns, and geographic zones, the goal is to predict ride demand for upcoming time intervals. Accurate demand prediction helps optimize driver availability, reduce passenger wait times, and improve overall operational efficiency. This project will leverage models like XGBoost, LightGBM, and LSTM Neural Networks to capture complex demand patterns. The insights from this work can enhance ride-sharing efficiency, improve customer satisfaction, and support data-driven decision-making. If you're passionate about predictive analytics or working on similar projects, let's connect!',
    author='Mohammod Ibrahim Hossain',
    license='MIT',
)
