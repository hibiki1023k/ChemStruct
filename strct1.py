import pubchempy as pcp
from rdkit import Chem
from rdkit.Chem import Draw

# アスピリンの構造を取得
aspirin = Chem.MolFromSmiles('CC(=O)OC1=CC=CC=C1C(=O)O')
Draw.MolToFile(aspirin, 'aspirin.png')