# Robots
Supports registering, viewing, and updating robots.

## Dump list of robots to mimic inventory system
```sh
$ docker exec <container> python3 manage.py dump_robots --count=<int|10>
```

## View list of robot

**Request**:

`GET` `/robots`

**Parameters:**

Name       | Type   | Description
-----------|--------|---
qa_status | string | Optional: possible values `qa_passed`, `factory_seconds`, `all`

**Response**:

```json
Content-Type application/json
200 OK

[
    {
        "id": 1,
        "name": "Cindy Garcia",
        "configuration": {
            "color": "blue",
            "hasTracks": false,
            "hasWheels": true,
            "hasSentience": true,
            "numberOfRotors": 11
        },
        "status": [
            "on fire"
        ],
        "qa_status": null
    }
]
```


## Extinguish fire from Robot
Removes the `on fire` status if the robot is `on fire` and `has Sentience`

**Request**:

`PUT` `/robots/:id/extinguish`


**Response**:

```json
Content-Type application/json
200 OK
```


## Recycle Robots

**Request**:

`DELETE` `/robots/recycle`

**Parameters:**

Name       | Type   | Description
-----------|--------|---
recycleRobots | list | The list of id of robots to be recycled


**Response**:

```json
Content-Type application/json
200 OK
```
