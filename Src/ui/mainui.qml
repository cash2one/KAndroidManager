import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Window 2.2
import QtQuick.Layouts 1.3

ApplicationWindow{
    visible:true
    width:800
    height:600

    Button {
        id: button
        x: 257
        y: 86
        text: qsTr("Button")
    }
}

