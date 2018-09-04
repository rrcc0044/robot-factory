# Shipments
Supports creation of shipments.

## Create Shipment

**Request**:

`POST` `/api/v1/shipments`

**Parameters:**

Name       | Type   | Description
-----------|--------|---
shipRobots | list | The list of id of robots to be shipped

**Response**:

```json
Content-Type application/json
201 CREATED
```
