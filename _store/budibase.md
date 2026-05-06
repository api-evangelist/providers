---
aid: budibase
name: Budibase
description: Budibase is an open source low-code platform for building AI agents, internal tools, and workflow automations. It enables teams to connect databases, spreadsheets, and business systems, then build applications and automations on top without extensive coding. Used by over 300,000 teams ranging from SMEs to government organizations, Budibase accelerates the delivery of internal business applications and process automation.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/budibase/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - AI Agents
  - Automation
  - Internal Tools
  - Low-Code
  - Open Source
  - Workflow Automation
apis:
  - aid: budibase:budibase-rest-api
    name: Budibase REST API
    description: The Budibase Public API provides programmatic access to Budibase resources including applications, tables, rows, users, queries, and automations. It enables external systems to read and write Budibase data, trigger automations, and manage platform resources. Authentication is via an API key generated in account settings.
    humanURL: https://docs.budibase.com/docs/public-api
    tags:
      - Applications
      - Automation
      - Low-Code
      - Tables
      - Users
    properties:
      - type: Documentation
        url: https://docs.budibase.com/docs/public-api
      - type: Authentication
        url: https://docs.budibase.com/docs/public-api#authentication
      - type: OpenAPI
        url: https://budibase.com/api/public/v1/openapi.json
common:
  - type: Website
    url: https://budibase.com
  - type: Documentation
    url: https://docs.budibase.com
  - type: GitHubRepository
    url: https://github.com/budibase/budibase
  - type: Blog
    url: https://budibase.com/blog
  - type: Pricing
    url: https://budibase.com/pricing
  - type: Changelog
    url: https://budibase.com/changelog
  - type: Community
    url: https://discord.com/invite/budibase-733030666647765003
  - type: SignUp
    url: https://account.budibase.app/register
  - type: Login
    url: https://account.budibase.app/auth/login
  - type: Support
    url: https://budibase.com/support
  - type: TermsOfService
    url: https://budibase.com/terms
  - type: PrivacyPolicy
    url: https://budibase.com/privacy
  - type: Integrations
    url: https://budibase.com/product/connections
  - name: Use Cases
    type: UseCases
    data:
      - name: Internal App Building
        url: https://budibase.com/product/apps
        features:
          - Database-Connected Apps
          - CRUD Interfaces
          - Role-Based Access Control
          - Multi-Step Forms
          - Admin Panels
          - Approval Workflows
      - name: AI Agents
        url: https://budibase.com/product/agents
        features:
          - Employee Request Handling
          - Question Answering Across Channels
          - Support Ticket Triage
          - Automated Routing
          - Process Automation
      - name: Workflow Automation
        url: https://budibase.com/product/automations
        features:
          - Approval Workflows
          - Notification Routing
          - Scheduled Automations
          - Trigger-Based Actions
          - Webhook Integrations
          - Multi-Step Pipelines
      - name: Data Management
        url: https://budibase.com/product/data
        features:
          - Database Connections
          - Spreadsheet Import
          - REST API Integration
          - Data Tables
          - Schema Management
          - Data Transformations
  - name: Features
    type: Features
    data:
      - name: Data Sources
        url: https://budibase.com/product/connections
        features:
          - PostgreSQL
          - MySQL
          - MongoDB
          - REST APIs
          - Google Sheets
          - Airtable
          - S3
          - Redis
          - CouchDB
          - Oracle
          - Microsoft SQL Server
      - name: App Building
        url: https://budibase.com/product/apps
        features:
          - Drag-and-Drop UI Builder
          - Pre-Built Components
          - Custom JavaScript
          - Responsive Layouts
          - Multi-Page Apps
          - Screen Templates
          - Role-Based Permissions
      - name: API Builder
        url: https://budibase.com/product/apis
        features:
          - Visual API Explorer
          - REST Endpoint Creation
          - Query Builder
          - Response Mapping
          - Authentication Configuration
      - name: Self-Hosting
        url: https://docs.budibase.com/docs/self-hosting
        features:
          - Docker Deployment
          - Kubernetes Support
          - DigitalOcean App Platform
          - AWS Deployment
          - On-Premises Support
          - Air-Gapped Deployments
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
