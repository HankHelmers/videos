
# Prepare environment from yaml
# conda env create -f environment.yaml --solver=libmamba

# Activate environment
conda activate manim
echo $CONDA_PREFIX

# Download CRAN R package dependencies 
Rscript setup_r_packages.R


# Useful references
# ------------------------
# Update following additions
# conda env update --file manim.yaml --prune --solver=libmamba

# Remove environment
# conda env remove -n manim

# Install new package example
# conda install conda-forge::r-remotes
