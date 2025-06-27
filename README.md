# The Scriture Encoder!

## Project info

This program utilizes the function _'encodeScripture'_ that receives _'script_line'_ and _'target_base'_ as its parameters. The function encodes a line from a church play script into a different number base representation, converting each character in the parameter _'script_line'_ to its _ASCII code_ with the help of the _'remainders_dict' (dictionary of chars)_ variable and store it in th variable _'script_ascii'_, then converts the ASCII code into the _specified 'target_base'_. Concatenate the encoded values into a single string, separated by spaces.

## Steps to converting a **decimal number** to a **diffent base**:

1. Initialize an empty string for the result;
2. Repeatedly divide the decimal number by the **'taget_base'** number and track the remainders;
3. Append the remainders to the result string in reverse order;
4. For bases **greater than 10**, avail oneself of the letters from **'A' to 'Z' for digits 10 to 35**.

## Example of logical conversion:

- **Convert 42 to base 16 (hexagonal)**;
- 42 / 16 = 2 remainder 10 **(10 represents 'A')**;
- 2 / 16 = 0 remainder 2, which will ilustrate '2' as the **last quotient**;
- So the final result will be **'2A'**.

## **PARAMETERS:**

- **script_line:** (str) A line from a church play script;
- **target_base:** (int) The base for conversion **(from 2 to 36 / binary to base-36)**.

---

## Result:

The function returns a string where each character of **'script_line'** is converted to its ASCII code and then to **'target_base'**, separated by spaces.
