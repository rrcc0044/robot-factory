# Robots
Supports registering, viewing, and updating robots.

## Dump list of robots to mimic inventory system
```sh
$ docker exec <container> python3 manage.py dump_robots --count=<int|10>
```

## View list of robot

**Request**:

`GET` `/api/v1/robots`

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

## Process Robots

**Request**:

`POST` `/api/v1/robots/process`

**Parameters:**

Name       | Type   | Description
-----------|--------|---
processRobots | list | The list of id of robots to be qa


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

`POST` `/api/v1/robots/:id/extinguish`


**Response**:

```json
Content-Type application/json
200 OK

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
    "status": [],
    "qa_status": null
}
```


## Recycle Robots

**Request**:

`POST` `/api/v1/robots/recycle`

**Parameters:**

Name       | Type   | Description
-----------|--------|---
recycleRobots | list | The list of id of robots to be recycled


**Response**:

```json
Content-Type application/json
200 OK
```
