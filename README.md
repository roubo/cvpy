cvpy 使用python实现的opencv实用api
============================
JunJian from 2014.8.1

尽量最小化的运行环境（base on ubuntu)
-------------------------------------

* python = 2.7.6
* opencv = 2.4.9 (how to install opencv) 

How to install the opencv
-------------------------

** We can be not care it **

* cmake to build 
    sudo apt-get install cmake

* gcc 
    anyway

* libgtk for highgui 
    sudo apt-get install libgtk2.0-dev
    sudo apt-get install pkg-config

* install
    cd opencv-2.4.9; mkdir build; cd build; 
    cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/home/roubo/lib/opencv/
     ..
    make -j3
    make install
    echo "export LD_LIBRARY_PATH=/home/roubo/lib/opencv/lib" >> ~/.bashrc
    or
    use the ldconfig in systen
    echo "/home/roubo/lib/opencv/lib" > /etc/ld.so.conf.d/opencv.conf
    sudo ldconfig /etc/ld.so.conf
    write to the /etc/bashrc
    "
    PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig
    export PKG_CONFIG_PATH
    "
    Take the ~/lib/ as the special public libs' path, if others are needed, remake it

