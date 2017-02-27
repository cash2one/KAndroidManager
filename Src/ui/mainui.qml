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

        Button {
            id: connect
            text: qsTr("连接")
            onClicked: {
                root.sig_connect()
            }
        }

        GridView {
            id: layouttools
            width: 140
            height: 140
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            Layout.fillHeight: true
            Layout.fillWidth: true
            cellWidth: 70
            model: ListModel {
                ListElement {
                    name: "Grey"
                    colorCode: "grey"
                }

                ListElement {
                    name: "Red"
                    colorCode: "red"
                }

                ListElement {
                    name: "Blue"
                    colorCode: "blue"
                }

                ListElement {
                    name: "Green"
                    colorCode: "green"
                }
            }
            delegate: Item {
                x: 5
                height: 50
                Column {
                    Rectangle {
                        width: 40
                        height: 40
                        color: colorCode
                        anchors.horizontalCenter: parent.horizontalCenter
                    }

                    Text {
                        x: 5
                        text: name
                        anchors.horizontalCenter: parent.horizontalCenter
                        font.bold: true
                    }
                    spacing: 5
                }
            }
            cellHeight: 70

            Button {
                id: files
                text: qsTr("Button")
            }
        }

    }
}

