# inplus

better python inputs. ( input + )

## **installation**

```bash
pip install inplus
```

## **setting up**

```py
from inplus import Input


# override default input ( optional )
input = Input()
```

## **for standard data types**

datatypes: `str` `int` `float` `bool`

**code:**

```py
def datatype(cls, prompt: str | NoneType = None, error: str | NoneType = None) -> str:
    """datatype

    ask a input from user and return a datatype.
    (same as datatype(input()))

    Args:
        prompt (str, optional): prompt message. Defaults to None.
        error (str, optional): error message. Defaults to None.

    Returns:
        datatype: input.
    """
    ...
```

**example (boolean):**

```py
from inplus import Input


input = Input()  # override default.

print(input.boolean())
print(input.boolean(prompt="prompt", error="error"))
```

output:

```tex
$ python foo.py
enter a boolean (true/false): abcd
! invalid input for boolean
enter a boolean (true/false): true
True
prompt: abcd
! error
prompt: FALSE
False
```
