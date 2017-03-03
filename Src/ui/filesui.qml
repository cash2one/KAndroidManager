import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Window 2.2
import QtQuick.Layouts 1.3

Window {
    id:root
    width: 800
    height: 900
    x: (Screen.desktopAvailableWidth - width)/2
    modality: Qt.WindowModal

    ColumnLayout {
        id: columnLayout
        anchors.fill: parent

        RowLayout{
            Layout.fillHeight: true
            Layout.fillWidth: true

            Button {
                id: button
                text: qsTr("Button")
            }

        }

        ListView {
            id: listView
            x: 0
            y: 0
            width: 110
            height: 160
            Layout.fillWidth: true
            model: pathmodel
            delegate: ItemDelegate {
                text: path
                width: parent.width
                background: Rectangle {
                    color: "#F0FFFF"
                }
                highlighted: ListView.isCurrentItem
                onClicked: {
                    listView.currentIndex = index
                }
            }
        }
    }

}
