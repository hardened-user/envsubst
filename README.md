# Yet another alternative to envsubst

Substitutes the values of environment variables.

Input file is copied to standard output, with references to environment variables of the form `$VARIABLE` or `${VARIABLE}` being replaced with the corresponding values.

By default, undefined variables are not substitute.
