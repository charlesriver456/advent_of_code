### Solutions to Advent of Code

Link to the site: https://adventofcode.com

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Docker
To run using Docker, first navigate to the directory and build the image:

```
docker build -t your_image_name .
```

Then run the image and mount files in the container

```
docker run -it -v path/to/directory:/app your_image_name
```

You can then use your text editor of choice to modify the code and you should see it changing in the container!
