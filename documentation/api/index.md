# LineS Documentation - API

- [LineS Documentation - Welcome     ]( /documentation/index.md)
- [LineS Documentation - Portal      ]( /documentation/portal/index.md)
- [LineS Documentation - API         ]( /documentation/api/index.md)
  - [Supported GTFS entities         ]( /documentation/api/index.md#supported-gtfs-entities)
  - [Available Endpoints             ]( /documentation/api/index.md#available-endpoints)
- [LineS Documentation - Toolkits    ]( /documentation/toolkits/index.md)

In this section, you will find information on how to use the LineS API, which is the interface for managing your GTFS feeds programmatically.

## Supported GTFS entities

In its current implementation, the API offers **FULL CRUD** support for the following GTFS entities: `agency.txt`, `calendar.txt`, `calendar_dates.txt`, `routes.txt`, `stops.txt`, `stop_times.txt`, and `trips.txt`.

Other GTFS entities cannot be managed through CRUD operations in the API, but they can be uploaded and downloaded as part of GTFS feed ZIP files, using the `/upload` and `/download` endpoints described below.

Here is a table summarizing the supported GTFS entities and their corresponding API labels, that should be used in the API endpoints to reference them:

| GTFS Entity        | API Entity       |
| ------------------ | ---------------- |
| agency.txt         | `agencies`       |
| calendar.txt       | `calendars`      |
| calendar_dates.txt | `calendar-dates` |
| routes.txt         | `routes`         |
| stops.txt          | `stops`          |
| stop_times.txt     | `stop-times`     |
| trips.txt          | `trips`          |

> E.g., to get stop `id:stop-0` from feed `id:feed-0` use `GET /feeds/feed-0/stops/stop-0`.

## Available Endpoints

This section will provide a detail description of the available endpoints in the API.

- API version: `v1`
- Base URL: `http://hostname:port/v1/gtfs`
- Body format: JSON
- Response format: JSON
- Fallback error for all endpoints: `500 Internal Server Error`

Some endpoints may require authentication via API keys. The key should be provided as a query parameter `key` in the request, e.g., `?key=API_KEY`. To generate an API key, please refer to [Managing your account](/documentation/portal/index.md#managing-your-account).

---

### `GET /feeds`

Returns a list of all available GTFS feeds.

**Responses**

- `200 OK`: list of feeds with their IDs and metadata.

---

### `GET /feeds/[feed_id]`

Returns detailed information about a specific GTFS feed by ID.

**Path Parameters**

- `feed_id` (string): the identifier of the feed.

**Responses**

- `200 OK`: feed ID and metadata.
- `400 Bad Request`: `feed_id` is empty.
- `404 Not Found`: feed does not exist.

---

### `POST /feeds/[feed_id]`

Create a new GTFS feed with the specified ID.

**Path Parameters**

- `feed_id` (string): the identifier for the new feed.

**Query Parameters**

- `key` (string): API key of feed creator for authentication.

**Responses**

- `201 Created`: feed successfully created.
- `400 Bad Request`: `feed_id` is empty.
- `403 Forbidden`: API key is invalid or user is not authorized to create feeds.
- `409 Conflict`: feed already exists.
- 

---

### `DELETE /feeds/[feed_id]`

Delete a GTFS feed by ID.

**Path Parameters**

- `feed_id` (string): the identifier of the feed to delete.

**Query Parameters**

- `key` (string): API key of feed creator for authentication.
  
**Responses**

- `204 No Content`: feed successfully deleted.
- `400 Bad Request`: `feed_id` is empty.
- `403 Forbidden`: API key is invalid or user is not authorized to delete the feed.
- `404 Not Found`: feed does not exist.

---

### `GET /feeds/[feed_id]/download`

Download a GTFS feed as a ZIP file.

**Path Parameters**

- `feed_id` (string): the identifier of the feed to download.

**Responses**

- `200 OK`: ZIP file containing the GTFS feed.
- `400 Bad Request`: `feed_id` is empty.
- `404 Not Found`: feed does not exist.

### `PUT /feeds/[feed_id]/upload`

Upload a GTFS feed as a ZIP file.

**Path Parameters**

- `feed_id` (string): the identifier of the feed to upload.

**Query Parameters**

- `key` (string): API key of feed editor for authentication.

**Request Body**

- `data` (file): the GTFS feed ZIP file to upload.

**Responses**

- `204 No Content`: feed successfully uploaded.
- `400 Bad Request`: `feed_id` is empty or invalid ZIP file.
- `403 Forbidden`: API key is invalid or user is not authorized to upload feeds.
- `404 Not Found`: feed does not exist.
- `415 Unsupported Media Type`: uploaded file is not a valid ZIP file.

### `GET /feeds/[feed_id]/report`

Generate a validation report for a GTFS feed.

**Path Parameters**

- `feed_id` (string): the identifier of the feed to validate.

**Query Parameters**

- `format` (string): the format of the report, either `json` or `html`. Default is `json`.

**Responses**

- `200 OK`: validation report in the requested format.
- `400 Bad Request`: `feed_id` is empty.
- `404 Not Found`: feed does not exist.

### `GET /feeds/[feed_id]/log`

Get the Git log of a GTFS feed.

**Path Parameters**

- `feed_id` (string): the identifier of the feed to get the log for.

**Responses**

- `200 OK`: list of commits in the feed's Git repository.
- `400 Bad Request`: `feed_id` is empty.
- `404 Not Found`: feed does not exist.

### `GET /feeds/[feed_id]/diff/[commit_id]`

Get the Git diff for a specific commit in a GTFS feed.

**Path Parameters**

- `feed_id` (string): the identifier of the feed.
- `commit_id` (string): the commit ID to get the diff for.

**Responses**
- `200 OK`: diff of the specified commit.
- `400 Bad Request`: `feed_id` is empty.
- `404 Not Found`: feed does not exist or commit not found.

### `POST /feeds/[feed_id]/revert/[commit_id]`

Revert a specific commit in a GTFS feed.

**Path Parameters**

- `feed_id` (string): the identifier of the feed.
- `commit_id` (string): the commit ID to revert.

**Query Parameters**

- `key` (string): API key of feed editor for authentication.

**Responses**

- `204 No Content`: commit successfully reverted.
- `400 Bad Request`: `feed_id` is empty.
- `403 Forbidden`: API key is invalid or user is not authorized to revert commits.
- `404 Not Found`: feed does not exist or commit not found.
- `409 Conflict`: error reverting commit.

### `GET /feeds/[feed_id]/[api_entity]`

Get all entities of a specific type from a GTFS feed.

**Path Parameters**

- `feed_id` (string): the identifier of the feed.
- `api_entity` (string): the entity type to retrieve.

**Responses**

- `200 OK`: list of entities of the specified type.
- `400 Bad Request`: `feed_id` is empty or `api_entity` is invalid.
- `404 Not Found`: feed does not exist or entity type not found.

### `GET /feeds/[feed_id]/[api_entity]/[entity_id]`

Get a specific entity by ID from a GTFS feed.

**Path Parameters**

- `feed_id` (string): the identifier of the feed.
- `api_entity` (string): the entity type to retrieve.
- `entity_id` (string): the ID of the entity to retrieve.

**Responses**

- `200 OK`: the requested entity.
- `400 Bad Request`: `feed_id` is empty, `api_entity` is invalid, or `entity_id` is empty.
- `404 Not Found`: feed does not exist, entity type not found, or entity ID not found.

### `POST /feeds/[feed_id]/[api_entity]`

Create new entities of a specific type in a GTFS feed.

**Path Parameters**

- `feed_id` (string): the identifier of the feed.
- `api_entity` (string): the entity type to create.

**Query Parameters**

- `key` (string): API key of feed editor for authentication.

**Request Body**

- `data` (entity): the entity data to create. Can be a single entity or a list of entities.

**Responses**

- `201 Created`: entities successfully created.
- `400 Bad Request`: `feed_id` is empty, `api_entity` is invalid, or entity data is invalid.
- `403 Forbidden`: API key is invalid or user is not authorized to create entities.
- `404 Not Found`: feed does not exist or entity type not found.

### `PUT /feeds/[feed_id]/[api_entity]`

Update existing entities of a specific type in a GTFS feed.

**Path Parameters**

- `feed_id` (string): the identifier of the feed.
- `api_entity` (string): the entity type to update.

**Query Parameters**

- `key` (string): API key of feed editor for authentication.

**Request Body**

- `data` (entity): the entity data to update. Can be a single entity or a list of entities.

**Responses**

- `204 No Content`: entities successfully updated.
- `400 Bad Request`: `feed_id` is empty, `api_entity` is invalid, or entity data is invalid.
- `403 Forbidden`: API key is invalid or user is not authorized to update entities.
- `404 Not Found`: feed does not exist or entity type not found.

### `DELETE /feeds/[feed_id]/[api_entity]/[entity_id]`

Delete a specific entity by ID from a GTFS feed.

**Path Parameters**

- `feed_id` (string): the identifier of the feed.
- `api_entity` (string): the entity type to delete.
- `entity_id` (string): the ID of the entity to delete.

**Query Parameters**

- `key` (string): API key of feed editor for authentication.

**Responses**

- `204 No Content`: entity successfully deleted.
- `400 Bad Request`: `feed_id` is empty, `api_entity` is invalid, or `entity_id` is empty.
- `403 Forbidden`: API key is invalid or user is not authorized to delete entities.
- `404 Not Found`: feed does not exist, entity type not found, or entity ID not found.
