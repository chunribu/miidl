from . import IO, QC, normalization, imputation, reshape, modeling, interpretation, networking
from .utils import run_as_command

__all__ = [IO, QC, normalization, imputation, reshape, modeling, interpretation, networking]
__author__ = "chunribu@mail.sdu.edu.cn"

if __name__ == "__main__":
    run_as_command()