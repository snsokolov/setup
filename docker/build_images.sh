# Script to build all images. Run each time when images needs to be rebuilt.

# Building development image.
docker build dev -t dev

# Print out the list of all images.
docker images
