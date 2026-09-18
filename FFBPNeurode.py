"""Creating FFBP class, inheriting from FFNeurode and BPNeurode."""
from BPNeurode import BPNeurode
from FFNeurode import FFNeurode


class FFBPNeurode(FFNeurode, BPNeurode):
    """Feed-forward backpropagation Neurode class."""
