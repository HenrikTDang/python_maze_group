U
��_S  �                   @   sh   d dl Zd dlm  mZ d dlZd dlmZ d dlZej	dd� �Z
dd� Zdd� Zd	d
� Zdd� ZdS )�    N��Playerc                   C   s   t d�S )z- This is a sample Player object that is valid�Johnr   � r   r   ��c:\Users\hungd\OneDrive - Douglas College\BCIT\Level 2\ACIT 2515- Python 2\labs\assignment2\maze095029\tests\models\test_player_model.py�john   s    r   c                 C   s�   | j }d}||k}|s~t�d|fd||f�dt�� ks@t�| �rJt�| �ndt�|�t�|�d� }dd|i }tt�|���d } }}dS )	z&1001- Tests constructor name attributer   ��==)z.%(py2)s
{%(py2)s = %(py0)s.player
} == %(py5)sr   ��py0�py2�py5�assert %(py7)s�py7N)	�player�
@pytest_ar�_call_reprcompare�@py_builtins�locals�_should_repr_global_name�	_saferepr�AssertionError�_format_explanation�r   �@py_assert1�@py_assert4�@py_assert3�@py_format6�@py_format8r   r   r   �test_constructor_player_name
   s        N   r   c                 C   s�   dddg| _ | j }dddg}||k}|s�t�d|fd||f�dt�� ksRt�| �r\t�| �ndt�|�t�|�d� }dd	|i }tt�|���d
 } }}d
S )z+1002 - Tests constructor backpack attribute�   �   �   r   �z0%(py2)s
{%(py2)s = %(py0)s.backpack
} == %(py5)sr   r
   r   r   N)	�backpackr   r   r   r   r   r   r   r   r   r   r   r   �test_constructor_backpack   s     
   N   r%   c                 C   s   | j t� k dS )z.1003 - Tests if constructor backpack is a listN)r$   �list)r   r   r   r   �!test_constructor_backpack_is_list   s    r'   c                 C   s�   dddg| _ | �d� | j }ddddg}||k}|s�t�d|fd||f�dt�� ks^t�| �rht�| �ndt�|�t�|�d� }dd	|i }tt�	|���d
 } }}d
S )z92001 - Tests if items picked up gets appended to backpack�shieldZswordZhammerr   r#   r   r
   r   r   N)
r$   �pickup_itemr   r   r   r   r   r   r   r   r   r   r   r   �test_pickup_item   s    
    N   r*   )�builtinsr   �_pytest.assertion.rewrite�	assertion�rewriter   �pytestZmodels.playerr   �fixturer   r   r%   r'   r*   r   r   r   r   �<module>   s     
