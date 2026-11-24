# JSON Fundamentals

This folder contains examples of JSON (JavaScript Object Notation).

## 1. JSON Object

A JSON object stores data in key-value pairs.

### Example

```json
{
    "name": "Jyoshna",
    "age": 19,
    "college": "Atria University",
    "course": "BS Engineering",
    "department": "Digital Transformation"
}
```

### Explanation

- `name` stores the person's name.
- `age` stores the person's age.
- `college` stores the college name.
- `course` stores the course.
- `department` stores the department.

Each key has a corresponding value.

---

## 2. JSON Object with Array

A JSON object can also contain an array as one of its values.

An array stores multiple values inside square brackets `[]`.

### Example

```json
{
    "name": "Jyoshna",
    "age": 19,
    "college": "Atria University",
    "skills": [
        "Python",
        "JavaScript",
        "HTML",
        "CSS",
        "SQL"
    ],
    "hobbies": [
        "Coding",
        "Reading",
        "Learning"
    ]
}
```

### Explanation

- `name` stores the person's name.
- `age` stores the person's age.
- `college` stores the college name.
- `skills` is an array containing multiple skills.
- `hobbies` is an array containing multiple hobbies.

### JSON Syntax

| Symbol | Purpose |
|---|---|
| `{ }` | Defines a JSON object |
| `[ ]` | Defines an array |
| `:` | Separates a key and its value |
| `,` | Separates properties or array elements |
| `" "` | Defines strings |

---

## Conclusion

JSON is a lightweight data format used to store and exchange data between applications and APIs.