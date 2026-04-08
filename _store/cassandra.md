---
aid: cassandra
url: https://raw.githubusercontent.com/api-evangelist/cassandra/refs/heads/main/apis.yml
apis:
- aid: cassandra:cassandra-cql-api
  name: Apache Cassandra CQL API
  tags:
  - CQL
  - Database
  humanURL: https://cassandra.apache.org/doc/latest/cassandra/cql/
  properties:
  - url: https://cassandra.apache.org/doc/latest/cassandra/cql/
    type: Documentation
  description: Cassandra Query Language (CQL) API for interacting with Cassandra databases. CQL is a SQL-like language for querying and managing data.
- aid: cassandra:cassandra-rest-api-stargate
  name: Cassandra REST API (Stargate)
  tags:
  - Database
  - REST
  humanURL: https://stargate.io/docs/latest/develop/api-rest/
  properties:
  - url: https://stargate.io/docs/latest/develop/api-rest/
    type: Documentation
  - url: https://stargate.io/docs/latest/develop/api-rest/swagger.html
    type: Reference
  description: RESTful API for Cassandra provided by Stargate, offering HTTP-based access to Cassandra data with JSON payloads.
name: Apache Cassandra
tags:
- Apache
- Big Data
- Database
- Distributed
- NoSQL
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Apache Cassandra is a highly scalable, distributed NoSQL database designed to handle large amounts of data across many commodity servers, providing high availability with no single point of failure.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

