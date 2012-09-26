CmdDirectoryCompletion
======================

Using Python cmd.Cmd to auto complete the directory.

You can use the different file systems. Just create a
new FS, using the AbstractFileSystem as its Base class.

The AbstractFileSystem is just an interface, so that
the different file systems can using the same operations.

The DirectoryCompletion accepts one argument. 
This argument is the instance of the class derived from
AbstractFileSystem. Of cource, you can just implement
methods such as *list_dir*.
