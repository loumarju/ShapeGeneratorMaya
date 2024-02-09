'''
1. objectSel(): Esta función selecciona objetos en Maya. Primero, verifica si hay al menos dos objetos seleccionados en la escena. 
Si no es así, la función retorna False. Si hay al menos dos objetos seleccionados, obtiene la lista de formas (shapes) de los objetos 
seleccionados y la historia de las formas (incluyendo los pesos de los clusters). Luego, busca cualquier 'skinCluster' (un tipo de deformador 
que se utiliza para la animación de personajes) en la historia de las formas. Finalmente, define el último objeto seleccionado como el objetivo 
y llama a la función assignSkc() con el 'skinCluster' y el objetivo como argumentos.

2.assignSkc(skc, target): Esta función asigna un 'skinCluster' a un objetivo. Primero, obtiene la historia de las formas del objetivo y busca 
cualquier 'skinCluster' antiguo. Si encuentra alguno, lo elimina. Luego, obtiene la lista de influencias ponderadas del 'skinCluster' 
(los huesos que afectan a la deformación de la piel) y crea un nuevo 'skinCluster' en el objetivo con estas influencias. Después, copia los 
pesos de la piel del 'skinCluster' original al nuevo 'skinCluster'. Finalmente, renombra el nuevo 'skinCluster' con el nombre del original y 
lo retorna.

La última línea objectSel() simplemente llama a la función objectSel() cuando se ejecuta el script'''

import maya.cmds as cmds


def objectSel():
    if len(cmds.ls(sl=True)) < 2:
        return False
    else:
        # Create a variable that contains the shapes of the geometry selected
        objects = cmds.listRelatives(s=True)
        # We put lv3 for the select also the weights of the clusters
        shapeHistory = cmds.listHistory(objects[0], lv=3)
        skc = cmds.ls(shapeHistory, typ='skinCluster')
        # We define the target mesh selected, and we put [-1] because is the last mesh selected
        target = cmds.ls(sl=True)[-1]
        assignSkc(skc, target)

        return True


def assignSkc(skc, target):
    shapeHistory = cmds.listHistory(target, lv=3)
    oldSkc = cmds.ls(shapeHistory, typ='skinCluster')
    if oldSkc:
        cmds.delete(oldSkc)
    jnt = cmds.skinCluster(skc, weightedInfluence=True, q=True)
    newSkc = cmds.skinCluster(jnt, target)
    cmds.copySkinWeights(ss=skc[0], ds=newSkc[0], nm=True, surfaceAssociation='closestPoint')
    cmds.rename(newSkc, skc[0])
    return newSkc


objectSel()