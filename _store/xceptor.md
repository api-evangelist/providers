---
aid: xceptor
name: Xceptor
description: Xceptor is a data automation platform that helps organizations extract, transform, and integrate data from various sources, particularly focused on document processing and financial data automation.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/xceptor/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-03-16'
specificationVersion: '0.19'
tags:
  - API Integration
  - Data Automation
  - Data Extraction
  - Document Processing
  - ETL
  - Financial Data
  - Financial Services
  - Intelligent Document Processing
  - Reconciliations
  - Trade Operations
apis:
  - name: Xceptor REST API
    description: RESTful API for managing data processing workflows, document ingestion, and data extraction in Xceptor. Provides programmatic access to the Xceptor data automation platform for integrating with existing systems and orchestrating automated data processing pipelines.
    image: https://www.xceptor.com/images/xceptor-logo.png
    baseURL: https://api.xceptor.com/v1
    humanURL: https://www.xceptor.com/api
    documentation: https://docs.xceptor.com/api/rest
    properties:
      - type: Documentation
        url: https://docs.xceptor.com/api/rest
      - type: OpenAPI
        url: https://api.xceptor.com/v1/openapi.json
      - type: Authentication
        url: https://docs.xceptor.com/api/authentication
    contact:
      - type: Support
        url: https://www.xceptor.com/support
      - type: Email
        url: mailto:api-support@xceptor.com
    tags:
      - Data Processing
      - Documents
      - REST
      - Workflows
  - name: Xceptor Workflow API
    description: API for creating, managing, and executing data processing workflows within the Xceptor platform. Enables programmatic orchestration of automated data processing pipelines including event-driven triggers and business rules execution.
    image: https://www.xceptor.com/images/xceptor-logo.png
    baseURL: https://api.xceptor.com/v1/workflows
    humanURL: https://www.xceptor.com/workflows
    documentation: https://docs.xceptor.com/api/workflows
    properties:
      - type: Documentation
        url: https://docs.xceptor.com/api/workflows
      - type: Postman Collection
        url: https://www.postman.com/xceptor/workspace/workflows
    tags:
      - Automation
      - Orchestration
      - Workflows
  - name: Xceptor Document Upload API
    description: API for uploading and processing documents through Xceptor's data extraction engine. Supports intelligent document processing using NLP, OCR, and generative AI to transform unstructured documents including PDFs, emails, and spreadsheets into structured, trusted data.
    image: https://www.xceptor.com/images/xceptor-logo.png
    baseURL: https://api.xceptor.com/v1/documents
    humanURL: https://www.xceptor.com/documents
    documentation: https://docs.xceptor.com/api/documents
    properties:
      - type: Documentation
        url: https://docs.xceptor.com/api/documents
      - type: Examples
        url: https://docs.xceptor.com/api/examples/documents
    tags:
      - Documents
      - Extraction
      - OCR
      - Upload
  - name: Xceptor Data Export API
    description: API for exporting processed data in various formats. Supports output to multiple downstream systems and data formats including XML, JSON, CSV, and Excel for integration with trading platforms, data warehouses, and regulatory reporting systems.
    image: https://www.xceptor.com/images/xceptor-logo.png
    baseURL: https://api.xceptor.com/v1/export
    humanURL: https://www.xceptor.com/export
    documentation: https://docs.xceptor.com/api/export
    properties:
      - type: Documentation
        url: https://docs.xceptor.com/api/export
      - type: Formats
        url: https://docs.xceptor.com/api/export-formats
    tags:
      - Data
      - Export
      - Integration
  - name: Xceptor Connector API
    description: API and connector framework for integrating Xceptor with external systems and data sources. Provides pre-built connectors for cloud storage (AWS S3, Azure Blob, Google Cloud Storage), messaging systems (Kafka, RabbitMQ), databases (SQL Server, Snowflake), and financial industry protocols (SWIFT 15022 and 20022). Enables bidirectional data exchange with the Xceptor platform.
    image: https://www.xceptor.com/images/xceptor-logo.png
    baseURL: https://api.xceptor.com/v1
    humanURL: https://www.xceptor.com/platform/connectors
    properties:
      - type: Documentation
        url: https://www.xceptor.com/platform/connectors
    tags:
      - Cloud
      - Connectors
      - Financial Data
      - Integration
      - SWIFT
common:
  - type: Portal
    url: https://portal.xceptor.com
  - type: Getting Started
    url: https://docs.xceptor.com/getting-started
  - type: Authentication
    url: https://docs.xceptor.com/authentication
  - type: Rate Limits
    url: https://docs.xceptor.com/rate-limits
  - type: Status Page
    url: https://status.xceptor.com
  - type: Terms of Service
    url: https://www.xceptor.com/legal-tcs
  - type: Privacy Policy
    url: https://www.xceptor.com/privacy-policy
  - type: Contact
    url: https://www.xceptor.com/contact-us
  - type: Website
    url: https://www.xceptor.com
  - type: Platform
    url: https://www.xceptor.com/platform
  - type: Solutions
    url: https://www.xceptor.com/solutions
  - type: Blog
    url: https://www.xceptor.com/blogs
  - type: Newsroom
    url: https://www.xceptor.com/company/newsroom
  - type: Support
    url: https://xceptor.zendesk.com/hc/en-gb
  - type: Training
    url: https://www.xceptor.com/support/training
  - type: Community
    url: https://connect.xceptor.com
  - type: Academy
    url: https://academy.xceptor.com/learn
  - type: Resources
    url: https://www.xceptor.com/resources
  - type: Glossary
    url: https://www.xceptor.com/resources/glossary
  - type: Webinars
    url: https://www.xceptor.com/resources/webinars
  - type: Videos
    url: https://www.xceptor.com/resources/videos
  - type: About
    url: https://www.xceptor.com/about
  - type: Partners
    url: https://www.xceptor.com/find-a-partner
  - type: LinkedIn
    url: https://www.linkedin.com/company/xceptor
  - type: X
    url: https://x.com/xceptor
  - type: Connector Marketplace
    url: https://app.xceptor.cloud/xsllibrary/mx/home/
  - type: Azure Marketplace
    url: https://azuremarketplace.microsoft.com/en-us/marketplace/apps/xceptor.xceptor
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
include: []
---
