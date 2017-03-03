import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Window 2.2
import QtQuick.Layouts 1.3

ApplicationWindow{
    id:root
    visible:true
    width:800
    height:600

    signal sig_connect()

    ColumnLayout {
        id: columnLayout
        anchors.fill: parent

        RowLayout {
            id: rowLayout
            width: 100
            height: 100
            Layout.fillHeight: true
            Layout.fillWidth: true

            Button {
                id: connect
                text: qsTr("连接")
                onClicked: {
                    root.sig_connect()
                }
            }
        }

        GridLayout {
            id: gridLayout
            width: 100
            height: 100
            rows: 4
            columns: 4
            Layout.fillHeight: true
            Layout.fillWidth: true
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter

            Button {
                id: files
                text: qsTr("文件管理")
                Layout.row:0
                Layout.column: 0
                Layout.columnSpan: 1
                Layout.rowSpan: 1
                Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                Layout.fillHeight: true
                Layout.fillWidth: true
                onClicked: {
                    thismodel.open_filesmanager()
                }
            }
            Button {
                id: unknonw2
                text: qsTr("")
                Layout.columnSpan: 1
                Layout.rowSpan: 1
                Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                Layout.fillHeight: true
                Layout.fillWidth: true
            }
            Button {
                id: unknonw3
                text: qsTr("")
                Layout.columnSpan: 1
                Layout.rowSpan: 1
                Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                Layout.fillHeight: true
                Layout.fillWidth: true
            }
            Button {
                id: unknonw4
                text: qsTr("")
                Layout.columnSpan: 1
                Layout.rowSpan: 1
                Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                Layout.fillHeight: true
                Layout.fillWidth: true
            }
            Button {
                id: unknonw5
                text: qsTr("")
                Layout.columnSpan: 1
                Layout.rowSpan: 1
                Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                Layout.fillHeight: true
                Layout.fillWidth: true
            }
        }



    }
}

