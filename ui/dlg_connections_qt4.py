# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlg_connections.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DlgConnections(object):
    def setupUi(self, DlgConnections):
        DlgConnections.setObjectName(_fromUtf8("DlgConnections"))
        DlgConnections.resize(880, 748)
        DlgConnections.setSizeGripEnabled(True)
        self.gridLayout = QtGui.QGridLayout(DlgConnections)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.chkKeepOpen = QtGui.QCheckBox(DlgConnections)
        self.chkKeepOpen.setObjectName(_fromUtf8("chkKeepOpen"))
        self.horizontalLayout.addWidget(self.chkKeepOpen, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.btnAdd = QtGui.QPushButton(DlgConnections)
        self.btnAdd.setEnabled(False)
        self.btnAdd.setMinimumSize(QtCore.QSize(80, 0))
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.horizontalLayout.addWidget(self.btnAdd)
        self.btnClose = QtGui.QPushButton(DlgConnections)
        self.btnClose.setMinimumSize(QtCore.QSize(80, 0))
        self.btnClose.setObjectName(_fromUtf8("btnClose"))
        self.horizontalLayout.addWidget(self.btnClose)
        self.btnHelp = QtGui.QPushButton(DlgConnections)
        self.btnHelp.setMinimumSize(QtCore.QSize(80, 0))
        self.btnHelp.setObjectName(_fromUtf8("btnHelp"))
        self.horizontalLayout.addWidget(self.btnHelp)
        self.horizontalLayout.setStretch(0, 1)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        self.tabConnections = QtGui.QTabWidget(DlgConnections)
        self.tabConnections.setMinimumSize(QtCore.QSize(0, 0))
        self.tabConnections.setAutoFillBackground(False)
        self.tabConnections.setMovable(False)
        self.tabConnections.setObjectName(_fromUtf8("tabConnections"))
        self.tabServer = QtGui.QWidget()
        self.tabServer.setObjectName(_fromUtf8("tabServer"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tabServer)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.grpTilejsonConnections = QtGui.QGroupBox(self.tabServer)
        self.grpTilejsonConnections.setObjectName(_fromUtf8("grpTilejsonConnections"))
        self.gridLayout_4.addWidget(self.grpTilejsonConnections, 0, 0, 1, 1)
        self.tabConnections.addTab(self.tabServer, _fromUtf8(""))
        self.tabFile = QtGui.QWidget()
        self.tabFile.setObjectName(_fromUtf8("tabFile"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tabFile)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.lblMbtilesStyleJsonUrl = QtGui.QLabel(self.tabFile)
        self.lblMbtilesStyleJsonUrl.setObjectName(_fromUtf8("lblMbtilesStyleJsonUrl"))
        self.gridLayout_6.addWidget(self.lblMbtilesStyleJsonUrl, 1, 0, 1, 1)
        self.txtMbtilesStyleJsonUrl = QtGui.QLineEdit(self.tabFile)
        self.txtMbtilesStyleJsonUrl.setObjectName(_fromUtf8("txtMbtilesStyleJsonUrl"))
        self.gridLayout_6.addWidget(self.txtMbtilesStyleJsonUrl, 1, 1, 1, 1)
        self.txtPath = QtGui.QLineEdit(self.tabFile)
        self.txtPath.setText(_fromUtf8(""))
        self.txtPath.setPlaceholderText(_fromUtf8(""))
        self.txtPath.setObjectName(_fromUtf8("txtPath"))
        self.gridLayout_6.addWidget(self.txtPath, 0, 1, 1, 1)
        self.btnBrowse = QtGui.QPushButton(self.tabFile)
        self.btnBrowse.setObjectName(_fromUtf8("btnBrowse"))
        self.gridLayout_6.addWidget(self.btnBrowse, 0, 2, 1, 1)
        self.lblSource = QtGui.QLabel(self.tabFile)
        self.lblSource.setObjectName(_fromUtf8("lblSource"))
        self.gridLayout_6.addWidget(self.lblSource, 0, 0, 1, 1)
        self.btnConnectFile = QtGui.QPushButton(self.tabFile)
        self.btnConnectFile.setObjectName(_fromUtf8("btnConnectFile"))
        self.gridLayout_6.addWidget(self.btnConnectFile, 2, 0, 1, 1)
        self.tabConnections.addTab(self.tabFile, _fromUtf8(""))
        self.tabDirectory = QtGui.QWidget()
        self.tabDirectory.setObjectName(_fromUtf8("tabDirectory"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tabDirectory)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.btnSelectDirectory = QtGui.QPushButton(self.tabDirectory)
        self.btnSelectDirectory.setObjectName(_fromUtf8("btnSelectDirectory"))
        self.gridLayout_2.addWidget(self.btnSelectDirectory, 0, 2, 1, 1)
        self.txtDirectoryStyleJsonUrl = QtGui.QLineEdit(self.tabDirectory)
        self.txtDirectoryStyleJsonUrl.setObjectName(_fromUtf8("txtDirectoryStyleJsonUrl"))
        self.gridLayout_2.addWidget(self.txtDirectoryStyleJsonUrl, 1, 1, 1, 1)
        self.lblDirectoryStyleJsonUrl = QtGui.QLabel(self.tabDirectory)
        self.lblDirectoryStyleJsonUrl.setObjectName(_fromUtf8("lblDirectoryStyleJsonUrl"))
        self.gridLayout_2.addWidget(self.lblDirectoryStyleJsonUrl, 1, 0, 1, 1)
        self.lblSource_2 = QtGui.QLabel(self.tabDirectory)
        self.lblSource_2.setObjectName(_fromUtf8("lblSource_2"))
        self.gridLayout_2.addWidget(self.lblSource_2, 0, 0, 1, 1)
        self.txtDirectoryPath = QtGui.QLineEdit(self.tabDirectory)
        self.txtDirectoryPath.setText(_fromUtf8(""))
        self.txtDirectoryPath.setPlaceholderText(_fromUtf8(""))
        self.txtDirectoryPath.setObjectName(_fromUtf8("txtDirectoryPath"))
        self.gridLayout_2.addWidget(self.txtDirectoryPath, 0, 1, 1, 1)
        self.btnConnectDirectory = QtGui.QPushButton(self.tabDirectory)
        self.btnConnectDirectory.setObjectName(_fromUtf8("btnConnectDirectory"))
        self.gridLayout_2.addWidget(self.btnConnectDirectory, 2, 0, 1, 1)
        self.tabConnections.addTab(self.tabDirectory, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabConnections, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.grpOptions = QtGui.QGroupBox(DlgConnections)
        self.grpOptions.setMinimumSize(QtCore.QSize(0, 190))
        self.grpOptions.setObjectName(_fromUtf8("grpOptions"))
        self.gridLayout.addWidget(self.grpOptions, 4, 0, 1, 1)
        self.grpLayers = QtGui.QGroupBox(DlgConnections)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grpLayers.sizePolicy().hasHeightForWidth())
        self.grpLayers.setSizePolicy(sizePolicy)
        self.grpLayers.setObjectName(_fromUtf8("grpLayers"))
        self.gridLayout_3 = QtGui.QGridLayout(self.grpLayers)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tblLayers = QtGui.QTableView(self.grpLayers)
        self.tblLayers.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tblLayers.setProperty("showDropIndicator", False)
        self.tblLayers.setAlternatingRowColors(True)
        self.tblLayers.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.tblLayers.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tblLayers.setSortingEnabled(True)
        self.tblLayers.setCornerButtonEnabled(True)
        self.tblLayers.setObjectName(_fromUtf8("tblLayers"))
        self.tblLayers.horizontalHeader().setMinimumSectionSize(140)
        self.tblLayers.horizontalHeader().setStretchLastSection(True)
        self.tblLayers.verticalHeader().setVisible(False)
        self.gridLayout_3.addWidget(self.tblLayers, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.grpLayers, 1, 0, 3, 1)

        self.retranslateUi(DlgConnections)
        self.tabConnections.setCurrentIndex(2)
        QtCore.QObject.connect(self.btnClose, QtCore.SIGNAL(_fromUtf8("clicked()")), DlgConnections.reject)
        QtCore.QMetaObject.connectSlotsByName(DlgConnections)
        DlgConnections.setTabOrder(self.tabConnections, self.chkKeepOpen)
        DlgConnections.setTabOrder(self.chkKeepOpen, self.btnAdd)
        DlgConnections.setTabOrder(self.btnAdd, self.btnClose)
        DlgConnections.setTabOrder(self.btnClose, self.btnHelp)
        DlgConnections.setTabOrder(self.btnHelp, self.txtPath)
        DlgConnections.setTabOrder(self.txtPath, self.btnBrowse)

    def retranslateUi(self, DlgConnections):
        DlgConnections.setWindowTitle(_translate("DlgConnections", "Add Layer(s) from a Vector Tile Source", None))
        self.chkKeepOpen.setText(_translate("DlgConnections", "Keep dialog open", None))
        self.btnAdd.setText(_translate("DlgConnections", "Add", None))
        self.btnClose.setText(_translate("DlgConnections", "Close", None))
        self.btnHelp.setText(_translate("DlgConnections", "Help", None))
        self.grpTilejsonConnections.setTitle(_translate("DlgConnections", "Connections", None))
        self.tabConnections.setTabText(self.tabConnections.indexOf(self.tabServer), _translate("DlgConnections", "Online", None))
        self.lblMbtilesStyleJsonUrl.setText(_translate("DlgConnections", "GL Style JSON URL", None))
        self.txtPath.setToolTip(_translate("DlgConnections", "The URL to the TileJSON of the tile service (e.g. http://yourtilehoster.com/index.json)", None))
        self.btnBrowse.setText(_translate("DlgConnections", "Browse", None))
        self.lblSource.setText(_translate("DlgConnections", "Path", None))
        self.btnConnectFile.setText(_translate("DlgConnections", "Refresh", None))
        self.tabConnections.setTabText(self.tabConnections.indexOf(self.tabFile), _translate("DlgConnections", "MBTile", None))
        self.btnSelectDirectory.setText(_translate("DlgConnections", "Browse", None))
        self.lblDirectoryStyleJsonUrl.setText(_translate("DlgConnections", "GL Style JSON URL", None))
        self.lblSource_2.setText(_translate("DlgConnections", "Path", None))
        self.txtDirectoryPath.setToolTip(_translate("DlgConnections", "The URL to the TileJSON of the tile service (e.g. http://yourtilehoster.com/index.json)", None))
        self.btnConnectDirectory.setText(_translate("DlgConnections", "Refresh", None))
        self.tabConnections.setTabText(self.tabConnections.indexOf(self.tabDirectory), _translate("DlgConnections", "Directory", None))
        self.grpOptions.setTitle(_translate("DlgConnections", "Options", None))
        self.grpLayers.setTitle(_translate("DlgConnections", "Layers", None))

