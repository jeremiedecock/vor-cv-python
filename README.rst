=========
PyVoR-CV_
=========

Copyright (c) 2015 Jeremie DECOCK (http://www.jdhp.org)


* Web site: http://www.jdhp.org/projects_en.html#pyvorcv
* Online documentation: http://pyvorcv.readthedocs.org
* Source code: https://github.com/jeremiedecock/vor-cv-python
* Issue tracker: https://github.com/jeremiedecock/vor-cv-python/issues
* PyVoR-CV on PyPI: https://pypi.python.org/pypi/pyvorcv

In collaboration with http://www.vorobotics.com


Description
===========

The PyVoR-CV project (Python based VoRobotics Computer Vision), is a computer
vision library made for some VoRobotics projects (VoR11_, VoR12_, ...).
PyVoR-CV is mostly based on the OpenCV_ computer vision library.

|Photo 1|_

Note:

    This project is still in beta stage, so the API is not finalized yet.


Demos
=====

|Video 1|_


Dependencies
============

-  Python 3.4
-  `OpenCV`_ versions 3.0.0 or above
-  `NumPy`_

.. PyVoR-CV is tested to work with Python 3.4 under Gnu/Linux Debian 8 and Windows
.. 7.
.. It should also work with Python 3.X under recent Gnu/Linux and Windows systems.
.. It hasn't been tested (yet) on MacOSX and BSD systems.
.. 
.. `Python-serial`_ is required to install PyVoR-CV.

Note:

..    If you use ``pip`` to install PyVoR-CV, PyAX-12 and Numpy will be
..    automatically downloaded and installed (see the following install_
..    section).

    OpenCV cannot be installed with ``pip``, thus you have to install it
    manually.


.. _install:

Installation
============

Gnu/Linux
---------

You can install, upgrade, uninstall PyVoR-CV with these commands (in a
terminal)::

    pip install --pre pyvorcv
    pip install --upgrade pyvorcv
    pip uninstall pyvorcv

Or, if you have downloaded the PyVoR-CV source code::

    python3 setup.py install

.. There's also a package for Debian/Ubuntu::
.. 
..     sudo apt-get install pyvorcv

Windows
-------

.. Note:
.. 
..     The following installation procedure has been tested to work with Python
..     3.4 under Windows 7.
..     It should also work with recent Windows systems.

You can install, upgrade, uninstall PyVoR-CV with these commands (in a
`command prompt`_)::

    py -m pip install --pre pyvorcv
    py -m pip install --upgrade pyvorcv
    py -m pip uninstall pyvorcv

Or, if you have downloaded the PyVoR-CV source code::

    py setup.py install

MacOSX
-------

.. Note:
.. 
..     The following installation procedure has been tested to work with Python
..     3.4 under MacOSX 10.6 (*Snow Leopard*).
..     It should also work with recent MacOSX systems.

You can install, upgrade, uninstall PyVoR-CV with these commands (in a
terminal)::

    pip install --pre pyvorcv
    pip install --upgrade pyvorcv
    pip uninstall pyvorcv

Or, if you have downloaded the PyVoR-CV source code::

    python3 setup.py install




Bug reports
===========

To search for bugs or report them, please use the PyVoR-CV Bug Tracker at:

    https://github.com/jeremiedecock/vor-cv-python/issues


License
=======

The `PyVoR-CV` library is provided under the terms and conditions of the
`MIT License <http://opensource.org/licenses/MIT>`__.


.. _PyVoR-CV: http://www.jdhp.org/projects_en.html
.. _VoR11: https://pypi.python.org/pypi/vor11
.. _VoR12: https://pypi.python.org/pypi/vor12
.. _OpenCV: http://opencv.org/
.. _NumPy: http://www.numpy.org/
.. _command prompt: https://en.wikipedia.org/wiki/Cmd.exe

.. |Photo 1| image:: http://download.tuxfamily.org/jdhp/image/small_vor12-2.jpeg
.. _Photo 1: http://download.tuxfamily.org/jdhp/image/vor12-2.jpeg

.. |Video 1| image:: http://download.tuxfamily.org/jdhp/image/vor12_demo_youtube.jpeg
.. _Video 1: https://youtu.be/0HlRtU8clt4
