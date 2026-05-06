---
aid: apache-openwhisk
name: Apache OpenWhisk
description: Apache OpenWhisk is an open-source serverless cloud platform that executes functions in response to events at any scale. It supports multiple programming languages and provides a rich programming model for creating serverless APIs and event-driven applications.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Native
  - Event-Driven
  - FaaS
  - Serverless
  - Apache
  - Open Source
  - Functions
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-openwhisk/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-openwhisk:apache-openwhisk-rest-api
    name: Apache OpenWhisk REST API
    description: The OpenWhisk API provides REST endpoints for managing actions, triggers, rules, packages, and activations, supporting serverless function development in JavaScript, Python, Swift, Java, Go, PHP, and custom Docker runtimes.
    humanURL: https://openwhisk.apache.org/documentation.html
    tags:
      - FaaS
      - Functions
      - REST
      - Serverless
      - Apache
      - Open Source
      - Cloud Native
    properties:
      - type: Documentation
        url: https://openwhisk.apache.org/documentation.html
      - type: OpenAPI
        url: openapi/apache-openwhisk-rest-api.yaml
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
common:
  - type: GitHubOrganization
    url: https://github.com/apache/openwhisk
  - type: Documentation
    url: https://openwhisk.apache.org/
  - type: SpectralRules
    url: rules/apache-openwhisk-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-openwhisk-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/serverless-workflow.yaml
  - type: JSON-LD
    url: json-ld/apache-openwhisk-context.jsonld
  - type: Features
    data:
      - name: Serverless Functions
        description: Execute stateless functions in response to events without managing infrastructure
      - name: Multi-Language Support
        description: Supports Node.js, Python, Java, Go, PHP, Ruby, Swift, and custom Docker runtimes
      - name: Event Triggers
        description: Named event channels that fire actions based on external events
      - name: Action Sequences
        description: Compose multiple actions into sequential pipelines
      - name: Package System
        description: Pre-built integrations via /whisk.system namespace
      - name: REST API
        description: Full REST API for managing all platform resources programmatically
      - name: Docker Actions
        description: Custom runtime support via Docker containers for any language
  - type: UseCases
    data:
      - name: Event-Driven Microservices
        description: Build loosely coupled microservices that respond to events
      - name: IoT Data Processing
        description: Process sensor and device events at scale without infrastructure management
      - name: API Backend
        description: Create REST APIs backed by serverless functions
      - name: Scheduled Tasks
        description: Run periodic jobs using alarm triggers
      - name: Chatbots & Webhooks
        description: Handle Slack, GitHub, and other webhook events
  - type: Integrations
    data:
      - name: Slack
        description: Respond to Slack events and slash commands
      - name: GitHub
        description: Automate workflows based on GitHub repository events
      - name: Apache Kafka
        description: Process Kafka message stream events
      - name: Cloudant
        description: React to CouchDB/Cloudant database changes
      - name: IBM Cloud
        description: Available as IBM Cloud Functions on IBM Cloud
      - name: Kubernetes
        description: Deploy OpenWhisk on Kubernetes using Helm charts
---
