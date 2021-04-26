# Application - 📝 Todo list

This commandline program is a basic implementation for a todo list application using Python 3.7+ that allows you to build and maintain a TODO list.

## Usage

### Program options

| Description                                          | Usage                                                                                                 |
|------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| Create a todo                                        | `python to_do_list_app.py create "item1"`                                                             |
| Create multiple todos                                | `python to_do_list_app.py create "item2" "item3" "item4" "item5" "it1" "it2"`                         |
| Read (list) all todos                                | `python to_do_list_app.py list-all`                                                                   |
| Read (list) all todos that contain a given substring | `python to_do_list_app.py list-all --substring "item"`                                                |
| Read (list) all todos that are complete              | `python to_do_list_app.py list-all --complete`                                                        |
| Read (list) all todos that are not complete          | `python to_do_list_app.py list-all --no-complete`                                                     |
| Update a todo description                            | `python to_do_list_app.py toggle "item1" "item1_new"`                                                 |
| Update the state of a todo                           | `python to_do_list_app.py update "item1" "item2"`                                                     |
| Delete a todo                                        | `python to_do_list_app.py delete "item2"`                                                             |
| Delete multiple todos                                | `python to_do_list_app.py delete "item3" "item4"`                                                     |
| Delete all todos                                     | `python to_do_list_app.py delete-all`                                                                 |
| Interactive mode                                     | `python to_do_list_app.py create "item1"`                                                             |

## Pros, cons and next steps

### Pros

- pro 1
- pro 2

### Cons

- con 1
- con 2

### Next steps

- next step 1
- next step 2

## License

This project is licensed under the terms of the MIT license.
