---
aid: trino
url: >-
  https://raw.githubusercontent.com/api-evangelist/trino/refs/heads/main/apis.yml
apis:
  - aid: trino:trino
    name: Trino
    tags:
      - API
    humanURL: ' https://trino.io/'
    properties:
      - url: ' https://trino.io/'
        type: Documentation
    description: >-
      Fast distributed SQL query engine for big data analytics that helps you
      explore your data universe. 
name: Trino
tags:
  - SQL
  - MySQL
  - NoSQL
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-06-05'
modified: '2025-07-15'
position: Consuming
description: >-
  Trino is an open-source, distributed SQL query engine built for lightning-fast
  analytics over large, heterogeneous data sets. Originally forked from Presto
  (which emerged at Facebook), it supports ANSI-compliant SQL across a wide
  range of storage systemsfrom data lakes (S3, HDFS, Iceberg) to relational and
  NoSQL databases (MySQL, PostgreSQL, Cassandra, MongoDB, Elasticsearch, Kafka,
  and more) . Architecturally, Trino employs a massively parallel processing
  (MPP) model with a dedicated coordinator that plans queries and multiple
  worker nodes that execute them in parallel, allowing it to scale from
  gigabytes to petabytes of data .
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'
common:
  - name: GitHub Organization
    url: https://github.com/trinodb
    type: GitHubOrganization
  - name: "Trino |\_Distributed SQL query engine for big data"
    description: 'null'
    url: https://trino.io/
    type: Website
  - name: Trino documentation  Trino 476 Documentation
    description: 'null'
    url: https://trino.io/docs/current/
    type: Documentation
  - name: Security  Trino 476 Documentation
    description: 'null'
    url: https://trino.io/docs/current/security.html
    type: Security
  - name: Connectors  Trino 476 Documentation
    description: 'null'
    url: https://trino.io/docs/current/connector.html
    type: Integrations
  - name: Glossary  Trino 476 Documentation
    description: 'null'
    url: https://trino.io/docs/current/glossary.html
    type: Glossary
  - name: Release notes  Trino 476 Documentation
    description: 'null'
    url: https://trino.io/docs/current/release.html
    type: ChangeLog
  - name: "Trino |\_Get started with Trino"
    description: 'null'
    url: https://trino.io/download
    type: GettingStarted
  - name: "Trino |\_Trino Community"
    description: 'null'
    url: https://trino.io/community#events
    type: Events
  - name: Trino | Trino blog
    description: 'null'
    url: https://trino.io/blog/
    type: Blog
  - name: "Trino |\_Trino Community"
    description: 'null'
    url: https://trino.io/community
    type: Discussions
---