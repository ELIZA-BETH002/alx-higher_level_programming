#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p)
{
PyBytesObject *bytes;
Py_ssize_t i, size;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

bytes = (PyBytesObject *)p;
size = PyBytes_Size(p);

printf("  size: %ld\n", size);
printf("  trying string: %s\n", PyBytes_AS_STRING(p));

printf("  first %ld bytes: ", (size < 10) ? size + 1 : 10);
for (i = 0; i < size && i < 10; i++)
printf("%02x%c", bytes->ob_sval[i] & 0xff, (i + 1 < 10 && i + 1 < size) ?   : n);
}

void print_python_list(PyObject *p)
{
Py_ssize_t i, size;
PyObject *item;

printf("[*] Python list info\n");

if (!PyList_Check(p))
{
printf("  [ERROR] Invalid List Object\n");
return;
}

size = PyList_Size(p);
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
if (PyBytes_Check(item))
print_python_bytes(item);
}
}

