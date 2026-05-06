---
aid: kvdb
name: KVdb
description: Stop wasting time setting up NoSQL databases. KVdb is a hosted serverless key-value database with a simple HTTPS REST API. Buckets act as namespaces for keys, with built-in access control via secret, read, and write keys, custom Lua scripts, and per-bucket TTLs.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Databases
  - Key-Value
  - NoSQL
  - Serverless
url: https://raw.githubusercontent.com/api-evangelist/kvdb/refs/heads/main/apis.yml
created: '2025-02-08'
modified: '2026-04-28'
specificationVersion: '0.19'
access: 3rd-Party
position: Consumer
apis:
  - aid: kvdb:kvdb
    name: KVdb
    description: KVdb provides a hosted, serverless key-value database accessible over a simple REST API. Operations include creating and managing buckets, setting and retrieving values, atomic numeric increments, prefix-based key listing, and uploading and executing custom Lua scripts.
    humanURL: https://kvdb.io/
    tags:
      - Databases
      - Key-Value
      - REST API
      - Serverless
    properties:
      - type: Documentation
        url: https://kvdb.io/
      - type: Getting Started
        url: https://kvdb.io/
      - type: OpenAPI
        url: openapi/kvdb-openapi.yml
common:
  - type: Website
    url: https://kvdb.io/
  - type: Documentation
    url: https://kvdb.io/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
