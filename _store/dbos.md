---
aid: dbos
name: DBOS
description: DBOS is a durable execution platform built on Postgres for running resilient workflows, scheduled jobs, durable queues, and Kafka consumers. The core library (DBOS Transact) is available for Python, TypeScript, Go, and Java, with a managed serverless runtime offered as DBOS Cloud.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Composition
  - Durable Execution
  - Postgres
  - Queues
  - Scheduled Jobs
  - Workflow
url: https://raw.githubusercontent.com/api-evangelist/dbos/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-28'
specificationVersion: '0.19'
xType: company
position: Consumer
access: 3rd-Party
apis:
  - aid: dbos:dbos
    name: DBOS Transact
    description: DBOS Transact is a durable execution library that decorates application functions with workflow, step, transaction, scheduled, and Kafka consumer semantics, persisting all state to Postgres so workflows can survive crashes and resume from checkpoints. SDKs are published for Python, TypeScript, Go, and Java.
    humanURL: https://docs.dbos.dev/
    tags:
      - API Composition
      - Durable Execution
      - Library
      - Workflow
    properties:
      - type: Documentation
        url: https://docs.dbos.dev/
      - type: Getting Started
        url: https://docs.dbos.dev/quickstart
      - type: Python Reference
        url: https://docs.dbos.dev/python/reference/decorators
      - type: TypeScript Reference
        url: https://docs.dbos.dev/typescript/reference/decorators
      - type: GitHub Repository
        url: https://github.com/dbos-inc/dbos-transact-py
      - type: JSONSchema
        url: json-schema/workflow.json
  - aid: dbos:dbos-cloud
    name: DBOS Cloud
    description: DBOS Cloud is the managed, serverless hosting platform for DBOS workflows, queues, and scheduled jobs. The CLI deploys and manages DBOS applications and provides a graphical observability UI.
    humanURL: https://docs.dbos.dev/cloud-tutorials/cloud-cli
    tags:
      - Cloud
      - Hosting
      - Observability
      - Serverless
    properties:
      - type: Documentation
        url: https://docs.dbos.dev/cloud-tutorials/cloud-cli
      - type: Console
        url: https://console.dbos.dev/
common:
  - type: Website
    url: https://www.dbos.dev/
  - type: Documentation
    url: https://docs.dbos.dev/
  - type: GitHub Organization
    url: https://github.com/dbos-inc
  - type: Console
    url: https://console.dbos.dev/
  - type: Pricing
    url: https://www.dbos.dev/pricing
  - type: Blog
    url: https://www.dbos.dev/blog
  - type: Discord
    url: https://discord.gg/dbos
  - type: JSON-LD
    url: json-ld/dbos-context.jsonld
  - type: Vocabulary
    url: vocabulary/dbos-vocabulary.yml
  - type: Capabilities
    url: capabilities/dbos-capabilities.yml
  - type: Rules
    url: rules/dbos-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
