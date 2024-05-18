

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 6.5
import QtQuick.Controls 6.5
import UntitledProject1
import QtQuick.Studio.Components 1.0

Rectangle {
    id: rectangle
    width: Constants.width
    height: Constants.height

    color: Constants.backgroundColor

    Button {
        id: run
        x: 423
        y: 54
        width: 241
        height: 40
        text: qsTr("RUN")
    }

    TextArea {
        id: textArea
        x: 8
        y: 8
        width: 355
        height: 1264
        placeholderText: qsTr("Text Area")
    }

    Button {
        id: file
        x: 423
        y: 8
        text: qsTr("File")

        Label {
            id: displayFile
            x: 105
            y: 11
            width: 133
            height: 16
            text: qsTr("Label")
        }
    }

    GroupItem {
        x: 423
        y: 100
        width: 241
        height: 92

        Label {
            id: numberCount
            x: 0
            y: 38
            text: qsTr("Label")
        }

        Label {
            id: label2
            x: 0
            y: 68
            text: qsTr("Label")
        }

        Label {
            id: sum
            x: 0
            y: 8
            width: 241
            height: 16
            text: qsTr("Label")
        }
    }
    states: [
        State {
            name: "clicked"
        }
    ]
}
