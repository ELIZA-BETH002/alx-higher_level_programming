#include "Python.h"

void print_python_string(PyObject *p)
{
    PyUnicodeObject *str = (PyUnicodeObject *)p;

    printf("[.] string object info\n");
    printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(str) ? "compact ascii" : "compact unicode object");
    printf("  length: %ld\n", PyUnicode_GET_LENGTH(str));
    printf("  value: %ls\n", PyUnicode_AS_UNICODE(str));
}

