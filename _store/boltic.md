---
aid: boltic
url: https://raw.githubusercontent.com/api-evangelist/boltic/refs/heads/main/apis.yml
apis:
- aid: boltic:gateway-api
  name: Boltic Gateway API
  tags:
  - Gateways
  - Plugins
  - Routing
  - Security
  humanURL: https://docs.boltic.io/gateway/intro/
  properties:
  - url: https://docs.boltic.io/gateway/intro/
    type: Documentation
  - url: openapi/boltic-gateway-api-openapi.yml
    type: OpenAPI
  - url: json-schema/boltic-route.json
    type: JSONSchema
  description: The Boltic Gateway API provides a developer-friendly API gateway designed to simplify and secure how services interact across your platform. It enables seamless request routing, payload transformation, and enforcement of security policies across diverse integration types including serverless functions, workflows, tables, and proxy endpoints. The Gateway supports dynamic URL rewriting, path parameter injection, fine-grained authentication, and real-time observability.
- aid: boltic:workflow-api
  name: Boltic Workflow API
  tags:
  - Automation
  - Integrations
  - Triggers
  - Workflows
  humanURL: https://www.boltic.io/products/workflow
  properties:
  - url: https://docs.boltic.io/
    type: Documentation
  - url: openapi/boltic-workflow-api-openapi.yml
    type: OpenAPI
  - url: json-schema/boltic-workflow.json
    type: JSONSchema
  description: The Boltic Workflow API enables programmatic creation, management, and execution of automation workflows. Workflows are visual, no-code automation sequences that connect triggers with actions across 500+ integrations. The API supports HTTP-triggered workflows with customizable responses, scheduled executions, webhook-based triggers, and integration with AI providers including Perplexity, Hugging Face, Meta, and DeepSeek.
- aid: boltic:tables-api
  name: Boltic Tables API
  tags:
  - CRUD
  - Databases
  - NoCode
  - Tables
  humanURL: https://www.boltic.io/products/boltic-tables
  properties:
  - url: https://docs.boltic.io/docs/workflow-builder/activities/tables/
    type: Documentation
  - url: openapi/boltic-tables-api-openapi.yml
    type: OpenAPI
  - url: json-schema/boltic-table.json
    type: JSONSchema
  description: The Boltic Tables API provides programmatic access to Boltic Tables, a no-code database for teams to organize, manage, and automate structured data workflows. The API supports full CRUD operations on tables and rows, SQL query execution via a built-in SQL editor with AI-powered query generation, and integration with workflows for automated data processing triggered by table changes.
- aid: boltic:pipes-api
  name: Boltic Pipes API
  tags:
  - DataSync
  - ETL
  - Integration
  - Pipelines
  humanURL: https://docs.boltic.io/docs/pipes/pipe-creation/
  properties:
  - url: https://docs.boltic.io/docs/pipes/pipe-creation/
    type: Documentation
  - url: openapi/boltic-pipes-api-openapi.yml
    type: OpenAPI
  - url: json-schema/boltic-pipe.json
    type: JSONSchema
  description: The Boltic Pipes API provides programmatic access to data synchronization pipelines that connect data sources to destinations. Pipes enable real-time data syncing across systems via automated pipelines with zero maintenance. Sources include databases such as MongoDB, MySQL, and PostgreSQL, SaaS applications via API endpoints, and file storage. The API supports configurable sync frequencies including minutely, hourly, and daily schedules.
- aid: boltic:streams-api
  name: Boltic Streams API
  tags:
  - Analytics
  - Events
  - RealTime
  - Streaming
  humanURL: https://www.boltic.io/products/streams
  properties:
  - url: https://docs.boltic.io/docs/streams/intro/
    type: Documentation
  - url: openapi/boltic-streams-api-openapi.yml
    type: OpenAPI
  - url: json-schema/boltic-stream-event.json
    type: JSONSchema
  description: The Boltic Streams API provides real-time event streaming capabilities for tracking custom events and streaming data from websites, mobile apps, and servers. It includes source debugger tools for confirming API call delivery, an event analysis dashboard for monitoring event flows, and real-time data processing for actionable insights.
name: Boltic
tags:
- Automation
- DataSync
- Gateways
- NoCode
- Streaming
- Workflows
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-01-02'
modified: '2026-04-07'
position: Consuming
description: Boltic is an AI workflow automation platform that helps businesses streamline operations across customer support, finance, product, and marketing functions. The platform enables companies to build autonomous AI agents, create no-code workflows with drag-and-drop functionality, and connect with over 500 integrations including major tools like Salesforce, HubSpot, Shopify, and Google BigQuery.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
common:
- name: AI Powered Workflow Automation for Finance, Ecommerce, Healthcare & Support | Boltic.io
  description: 'null'
  url: https://www.boltic.io/
  type: Website
- name: Boltic Templates
  description: 'null'
  url: https://www.boltic.io/templates
  type: Templates
- name: Comprehensive List of Boltic Integrations | Accelerate Your Workflow
  description: 'null'
  url: https://www.boltic.io/integrations
  type: Integrations
- name: Pricing | Boltic
  description: 'null'
  url: https://www.boltic.io/pricing
  type: Pricing
- name: Boltic - Company
  description: 'null'
  url: https://www.boltic.io/about-us
  type: About
- name: Boltic Partner Program | Earn, Build, and Grow with Automation
  description: 'null'
  url: https://www.boltic.io/partners
  type: Partners
- name: Enterprise-Grade Modern Big DataOps Platform- Boltic
  description: 'null'
  url: https://www.boltic.io/blog
  type: Blog
- name: Boltic
  description: 'null'
  url: https://docs.boltic.io/?_gl=1*1jcnaph*_gcl_au*MjkzMjA5Mjk4LjE3Njc1NzI3NTI.*_ga*MTMwNzk5NDc0NS4xNzY3NTcyNzUy*_ga_YX1KJTTWZX*czE3Njc1NzI3NTEkbzEkZzEkdDE3Njc1NzI5NTIkajUwJGwwJGgxNDMzNTc1NTM0*_ga_MNYX5YZNXR*czE3Njc1NzI3NTEkbzEkZzEkdDE3Njc1NzI5NTIkajUwJGwwJGgw
  type: Documentation
- name: Boltic Changelog | Latest Product Updates & Feature Enhancements
  description: 'null'
  url: https://www.boltic.io/changelog
  type: ChangeLog
---

