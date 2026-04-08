---
aid: xceptor
url: https://raw.githubusercontent.com/api-evangelist/xceptor/refs/heads/main/apis.yml
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
name: Xceptor
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
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Xceptor is a data automation platform that helps organizations extract, transform, and integrate data from various sources, particularly focused on document processing and financial data automation.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

