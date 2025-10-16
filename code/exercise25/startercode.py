"""
mock_model.py - Mock model module for checkpoint management exercise
"""
from mockmodel import MockModel

# ============================================================================
# STUDENT STARTER CODE - Complete this implementation
# ============================================================================

# add your new functions here
# you might need new imports, add them to the begining of the file

# ============================================================================
# TRAINING LOOP - Students should add checkpoint saving here
# ============================================================================

def train_model():
    """
    Basic training loop.
    """
    # Initialize the mock model
    model = MockModel(seed=42)
    
    # Training configuration
    num_epochs = 80
    checkpoint_dir = "model_checkpoints"
    
    print("=" * 70)
    print("TRAINING NEURAL NETWORK")
    print("=" * 70)
    print(f"\nTraining for {num_epochs} epochs...")
    print(f"Checkpoints will be saved to: {checkpoint_dir}/\n")
    
    # TODO: Create checkpoint directory if it doesn't exist
    # hint: look for the mkdir() method in pathlib, check what
    #       what the argument 'parents' and 'exist_ok' do.
    #       https://docs.python.org/3/library/pathlib.html
    
    # Training loop
    for epoch in range(1, num_epochs + 1):
        # Run one training iteration
        train_acc, train_loss, val_acc, val_loss = model.train_eval_model_iteration()
        
        # TODO: Save checkpoint with metrics and model state

    print(f"\nTraining complete! {num_epochs} epochs finished.")
    
    # TODO: After training, demonstrate checkpoint loading and analysis

train_model()