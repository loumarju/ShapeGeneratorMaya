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