"""
mock_model.py - Mock model module for checkpoint management exercise
"""
import numpy as np
from typing import Dict, Tuple


class MockModel:
    """
    A mock neural network model that simulates realistic training behavior
    including overfitting after epoch 40.
    """
    
    def __init__(self, seed: int = 42):
        """
        Initialize the mock model.
        
        Args:
            seed: Random seed for reproducibility
        """
        np.random.seed(seed)
        self.epoch = 0
        self.overfit_start = 50
        
        # Initialize mock model weights
        self.weights = {
            'layer1_weights': np.random.randn(64, 32),
            'layer1_bias': np.random.randn(32),
            'layer2_weights': np.random.randn(32, 16),
            'layer2_bias': np.random.randn(16),
            'layer3_weights': np.random.randn(16, 10),
            'layer3_bias': np.random.randn(10)
        }
    
    def get_model_state(self) -> Dict[str, np.ndarray]:
        """
        Get the current model state (weights).
        
        Returns:
            Dictionary containing model weights
        """
        return self.weights.copy()
    
    def train_eval_model_iteration(self) -> Tuple[float, float, float, float]:
        """
        Simulate one epoch of training and evaluation.
        
        This function simulates realistic training where:
        - Training metrics continuously improve
        - Validation metrics improve until epoch 40, then degrade (overfitting)
        
        Returns:
            Tuple of (train_accuracy, train_loss, val_accuracy, val_loss)
        """
        self.epoch += 1
        epoch = self.epoch
        
        # Training accuracy: continues improving with logistic growth
        train_acc_base = 0.95 / (1 + np.exp(-0.15 * (epoch - 20)))
        train_acc = train_acc_base + np.random.normal(0, 0.01)
        train_acc = np.clip(train_acc, 0.50, 0.99)
        
        # Training loss: continues decreasing exponentially
        train_loss = 0.6 * np.exp(-0.08 * epoch) + np.random.normal(0, 0.02)
        train_loss = max(0.01, train_loss)
        
        # Validation accuracy: improves then plateaus and decreases (overfitting)
        if epoch < self.overfit_start:
            val_acc_base = 0.88 / (1 + np.exp(-0.15 * (epoch - 20)))
            val_acc = val_acc_base + np.random.normal(0, 0.015)
        else:
            # Overfitting phase: accuracy starts decreasing
            peak_val_acc = 0.88 / (1 + np.exp(-0.15 * (self.overfit_start - 20)))
            decay = 0.008 * (epoch - self.overfit_start)
            val_acc = peak_val_acc - decay + np.random.normal(0, 0.015)
        
        val_acc = np.clip(val_acc, 0.50, 0.90)
        
        # Validation loss: decreases then increases (classic overfitting signal)
        if epoch < self.overfit_start:
            val_loss = 0.7 * np.exp(-0.07 * epoch) + np.random.normal(0, 0.025)
        else:
            min_loss = 0.7 * np.exp(-0.07 * self.overfit_start)
            increase = 0.015 * (epoch - self.overfit_start)
            val_loss = min_loss + increase + np.random.normal(0, 0.025)
        
        val_loss = max(0.05, val_loss)
        
        # Update weights slightly (simulate learning)
        for key in self.weights:
            self.weights[key] += np.random.randn(*self.weights[key].shape) * 0.001
        
        return train_acc, train_loss, val_acc, val_loss

