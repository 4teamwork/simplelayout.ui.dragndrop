from Products.CMFCore.utils import getToolByName
from simplelayout.ui.dragndrop.config import PROJECTNAME


def uninstall(self):
    setup_tool = getToolByName(self, 'portal_setup')
    setup_tool.runAllImportStepsFromProfile(
        'profile-{0}:uninstall'.format(PROJECTNAME),
        ignore_dependencies=True)
