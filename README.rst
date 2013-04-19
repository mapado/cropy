cropy : Python content based image crop
=========================================
Command line tool and module to crop an image to a specific resolution removing less important parts first.

First started with the approch of this publication but seems a bit complex and slow (http://research.microsoft.com/en-us/um/people/jiansun/papers/SalientDetection_CVPR07.pdf).

cropy uses entropy information to identify slices of the image with less informations.


Usage
-----

To use with command line::

  cropy -i [input image] -r [width] [height] -o [output name] -s [maxSteps]

- input image : location of the image to crop
- width, eight : dimensions of the resultant cropped image
- output name : name of the output image (default : original_name.width.eight.orginal_extension)
- maxSteps : number of iteration : greater means more precision but slower (default : 10)

More info and examples on http://blog.mapado.com/cropy-how-to-crop-an-image-keeping-the-best-content/

Installation
------------
You can install cropy using pip::

    $ pip install cropy


Note that cropy requires ``scikit-learn``, which itself is based on ``numpy`` and ``scipy`` and requires ``cython`` to compile.

Possible upgrade
----------------
- locate faces inside image to prevent removing
- locate text on images to crop first


Thanks
------
Inspired from slycrop (php entropy based crop) : https://github.com/stojg/slycrop
