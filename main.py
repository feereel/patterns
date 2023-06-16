from mainwindow import Window

if __name__ == '__main__':

    handle = Window()
    handlee = Window()

    handle.title('Daw')
    handle.geometry('1280x720')

    assert(handle is handlee)

    handle.mainloop()