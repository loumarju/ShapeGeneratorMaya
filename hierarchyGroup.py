import shapeGenerator
reload(shapeGenerator)

from shapeGenerator import ShapeGenerator

shapeGenerator = ShapeGenerator('sphere', 'cube')
print(shapeGenerator.shape)