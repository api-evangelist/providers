---
aid: presto-foundation
name: Presto Foundation
description: The Presto Foundation is a Linux Foundation project supporting Presto, an open source distributed SQL query engine for big data analytics. Founded by Facebook (Meta), Uber, Twitter, and Alibaba, Presto enables interactive analytics across diverse data sources at massive scale, with a vendor-neutral governance model and an active ecosystem of contributors and integrations.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Big Data
  - Distributed SQL
  - Linux Foundation
  - Open Source
  - Query Engine
  - SQL
created: '2026-03-16'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/presto-foundation/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: presto-foundation:presto-client-rest-api
    name: Presto Client REST API
    description: The Presto Client REST API is the HTTP protocol used by Presto clients to submit SQL queries to a Presto coordinator and stream back results. It centers on POST /v1/statement to submit a query, GET on the returned nextUri to fetch subsequent result batches, and DELETE on nextUri to cancel a running query. Session context such as user, source, catalog, schema, time zone, and language is conveyed through X-Presto-* headers, and supports authentication mechanisms including Kerberos, LDAP, password files, OAuth 2.0, and custom authenticators.
    humanURL: https://prestodb.io/docs/current/develop/client-protocol.html
    tags:
      - Analytics
      - Big Data
      - Client Protocol
      - REST API
      - SQL
    properties:
      - type: Documentation
        url: https://prestodb.io/docs/current/develop/client-protocol.html
      - type: REST API Reference
        url: https://prestodb.io/docs/current/rest.html
      - type: GitHub Repository
        url: https://github.com/prestodb/presto
  - aid: presto-foundation:presto-coordinator-rest-api
    name: Presto Coordinator REST API
    description: The Presto Coordinator REST API exposes resources for inspecting and managing a running Presto cluster, including Node, Query, Stage, Statement, and Task resources. These endpoints are served by the coordinator process and are used by clients, monitoring tools, and the Presto worker protocol to coordinate distributed query execution and observe cluster health.
    humanURL: https://prestodb.io/docs/current/rest.html
    tags:
      - Analytics
      - Big Data
      - Cluster Management
      - REST API
      - SQL
    properties:
      - type: Documentation
        url: https://prestodb.io/docs/current/rest.html
      - type: Node Resource
        url: https://prestodb.io/docs/current/rest/node.html
      - type: Query Resource
        url: https://prestodb.io/docs/current/rest/query.html
      - type: Stage Resource
        url: https://prestodb.io/docs/current/rest/stage.html
      - type: Statement Resource
        url: https://prestodb.io/docs/current/rest/statement.html
      - type: Task Resource
        url: https://prestodb.io/docs/current/rest/task.html
common:
  - type: Portal
    url: https://prestodb.io/
  - type: Documentation
    url: https://prestodb.io/docs/current/
  - type: Foundation
    url: https://prestodb.io/foundation/
  - type: Blog
    url: https://prestodb.io/blog/
  - type: Community
    url: https://prestodb.io/community/
  - type: Events
    url: https://prestodb.io/events/
  - type: Resources
    url: https://prestodb.io/resources/
  - type: GitHub Organization
    url: https://github.com/prestodb
  - type: Slack
    url: https://communityinviter.com/apps/prestodb/prestodb
  - type: Twitter
    url: https://twitter.com/prestodb
  - type: YouTube
    url: https://www.youtube.com/c/PrestoDB
  - type: Linux Foundation
    url: https://www.linuxfoundation.org/projects/case-studies/presto/
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
