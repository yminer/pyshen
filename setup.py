from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("pyshen.primitives", ["pyshen/primitives.py"],  extra_compile_args=[]),
               Extension("pyshen.core", ["pyshen/core.py"],  extra_compile_args=[]),
               Extension("pyshen.shen", ["pyshen/shen.py"],  extra_compile_args=["-O0"])]

setup(
  name = 'shen app',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)
