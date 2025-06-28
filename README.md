# The Scriture Encoder!

## 📝 Project info

This program utilizes the function `encodeScripture` that receives `script_line` and `target_base` as its parameters. The function encodes a line from a church play script into a different number base representation, converting each character in the parameter `script_line` to its **ASCII code** to store it in the local list `ASCII_LIST`, then converts the ASCII code into the **specified `target_base`** with the help of the **module 'string' (contains strings with the corresponding base conversions)** and their useful methods. Concatenate the encoded values into a single string, separated by spaces.

## 🛠️ Steps to converting a **decimal number** to a **diffent base**:

1. Initialize an empty string for the result called `conversion`;
2. Repeatedly divide the decimal number by the `taget_base` number and track the remainders, while concatenating more strings into the `conversion` local variable;
3. Append the remainders to the result string in reverse order;
4. For bases **greater than 10**, avail oneself of the letters from **'A' to 'Z' for remainders from 10 to 35**.

## 🧮 Example of logical conversion:

- **Convert 42 to base 16 (hexagonal)**;
- 42 / 16 = 2 remainder 10 **(10 represents 'A')**;
- 2 / 16 = 0 remainder 2, which will ilustrate '2' as the **last quotient**;
- So the final result will be **'2A'**.

## 💎 **PARAMETERS:**

- **`script_line`** (str):  A line from a church play script;
- **`target_base`** (int):  The base for conversion **(from 2 to 36 / binary to base-36)**.

## 🏠 **LOCAL VARIABLES:**

|       Variable        | Usage                                                                                                            |
| :-------------------: | ---------------------------------------------------------------------------------------------------------------- |
|       `result`        | Will concatenate with the `reversed_conversion` variable to increment the result untill the end of the for loop. |
|     `ASCII_LIST`      | Contains a list of ASCII codes separated by each char respectively (and it never changes during execution).      |
|        `code`         | Represents each ASCII code inside the `ASCII_LIST`.                                                              |
|     `conversion`      | Concatenates with the current base conversion type, specified by the `target_base` variable.                     |
|      `remainder`      | Stored the current remainder from the module operator of `target_base`.                                          |
| `reversed_conversion` | Contains the `conversion` variable and reverses it.                                                              |

---

## 📊 Result:

The function returns a string where each character of `script_line` is converted to its ASCII code and then to the `target_base`, separated by spaces for each seperate ASCII code.
