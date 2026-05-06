---
aid: pandadoc
name: PandaDoc
description: PandaDoc is a document automation platform that enables businesses to create, send, track, and e-sign documents programmatically. Their developer platform provides REST APIs and embedded tools for integrating document generation, e-signature collection, and workflow automation directly into third-party applications.
type: Contract
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Document Automation
  - E-Signature
  - Document Management
  - Document Generation
  - Webhooks
created: '2026-03-21'
modified: '2026-05-04'
url: https://raw.githubusercontent.com/api-evangelist/pandadoc/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: pandadoc:rest-api
    name: PandaDoc REST API
    description: The PandaDoc REST API provides programmatic access to PandaDoc's document automation platform, enabling developers to create, send, track, and manage documents within their own applications. The API supports the full document lifecycle including generating documents from templates with dynamic data, collecting e-signatures, managing recipients, and tracking document status through webhooks. Authentication is handled via API keys, and a free sandbox environment is available for testing integrations before moving to production. An active Enterprise plan is required to access the production API.
    humanURL: https://developers.pandadoc.com/reference/about
    baseURL: https://api.pandadoc.com/public/v1
    tags:
      - Document Automation
      - E-Signature
      - Document Management
      - REST
    properties:
      - type: Documentation
        url: https://developers.pandadoc.com/reference/about
      - type: OpenAPI
        url: openapi/pandadoc-rest-api-openapi.yml
  - aid: pandadoc:document-generation-api
    name: PandaDoc Document Generation API
    description: The PandaDoc Document Generation API allows developers to programmatically create documents from templates by injecting dynamic data pulled from CRM systems, databases, or other external sources. It supports branded document creation with content placeholders, conditional sections, pricing tables, and custom fields that are populated at runtime. Documents can be generated from existing PandaDoc templates or uploaded PDFs, enabling consistent and automated document production at scale. The API is commonly used in sales, legal, and HR workflows to eliminate manual document preparation.
    humanURL: https://developers.pandadoc.com/docs/getting-started
    baseURL: https://api.pandadoc.com/public/v1
    tags:
      - Document Generation
      - Templates
      - Document Automation
      - CRM Integration
    properties:
      - type: Documentation
        url: https://developers.pandadoc.com/docs/getting-started
      - type: OpenAPI
        url: openapi/pandadoc-rest-api-openapi.yml
  - aid: pandadoc:e-signature-api
    name: PandaDoc E-Signature API
    description: The PandaDoc E-Signature API enables developers to embed legally binding e-signature workflows directly within their applications using a white-label signing experience. It supports sending signature requests via email or SMS, configuring multiple recipients with defined roles and signing order, and collecting signatures without signers needing a PandaDoc account. The API provides real-time status tracking and generates audit trails and signed PDF copies upon completion. It is designed for use cases in contract management, sales, finance, and any workflow requiring legally compliant electronic signatures.
    humanURL: https://www.pandadoc.com/api/
    baseURL: https://api.pandadoc.com/public/v1
    tags:
      - E-Signature
      - Electronic Signatures
      - Document Signing
      - Compliance
    properties:
      - type: Documentation
        url: https://www.pandadoc.com/api/
      - type: OpenAPI
        url: openapi/pandadoc-rest-api-openapi.yml
  - aid: pandadoc:embedded-editing-api
    name: PandaDoc Embedded Editing API
    description: The PandaDoc Embedded Editing API allows developers to embed PandaDoc's document editor directly within their own platform, enabling end users to prepare, customize, and finalize documents without leaving the host application. Users can upload PDFs or select templates, place signature and form fields, adjust content, and assign recipients through a drag-and-drop interface embedded via token-based sessions. Once editing is complete, documents can be sent for e-signature collection and the resulting signed PDFs and audit trails can be retrieved via API. This enables a seamless, branded document experience without requiring users to have separate PandaDoc accounts.
    humanURL: https://www.pandadoc.com/api/embedded-editing/
    baseURL: https://api.pandadoc.com/public/v1
    tags:
      - Embedded Editing
      - Document Editor
      - White Label
      - Embedded
    properties:
      - type: Documentation
        url: https://www.pandadoc.com/api/embedded-editing/
      - type: OpenAPI
        url: openapi/pandadoc-rest-api-openapi.yml
  - aid: pandadoc:webhooks-api
    name: PandaDoc Webhooks API
    description: The PandaDoc Webhooks API enables developers to subscribe to real-time event notifications for document lifecycle events such as document sent, viewed, signed, approved, declined, and completed. Webhooks can be configured to trigger events both within PandaDoc and in connected external systems, enabling automated workflows across a technology stack. Each event payload includes document metadata and status information for processing downstream actions like CRM updates, storage routing, or approval notifications. Webhooks are configured through the PandaDoc dashboard and are available to accounts with API access.
    humanURL: https://developers.pandadoc.com/docs/webhooks-concepts
    baseURL: https://api.pandadoc.com/public/v1
    tags:
      - Webhooks
      - Events
      - Notifications
      - Integration
    properties:
      - type: Documentation
        url: https://developers.pandadoc.com/docs/webhooks-concepts
      - type: OpenAPI
        url: openapi/pandadoc-rest-api-openapi.yml
      - type: AsyncAPI
        url: asyncapi/pandadoc-webhooks-asyncapi.yml
common:
  - type: Portal
    url: https://developers.pandadoc.com/
  - type: Documentation
    url: https://developers.pandadoc.com/docs/getting-started
  - type: Website
    url: https://www.pandadoc.com/
  - type: Blog
    url: https://www.pandadoc.com/blog/
  - type: Login
    url: https://app.pandadoc.com/login/
  - type: PrivacyPolicy
    url: https://www.pandadoc.com/privacy-notice/
  - type: TermsOfService
    url: https://www.pandadoc.com/terms-of-use/
  - type: Support
    url: https://support.pandadoc.com/
  - type: JSONLD
    url: json-ld/pandadoc-context.jsonld
  - type: JSONSchema
    url: json-schema/pandadoc-document-schema.json
  - type: JSONSchema
    url: json-schema/pandadoc-webhook-event-schema.json
  - type: Features
    data:
      - 'Free: 60 documents/year, unlimited seats'
      - 'Starter at $19/mo: 110 documents/year, audit trail'
      - 'Business at $49/seat/mo: unlimited documents, CRM integrations'
      - 'Enterprise: CPQ, workflow automation, SSO, API access'
      - REST API at api.pandadoc.com
      - Default 100 req/min/workspace
      - Documents API + Templates API + Contacts API
      - OAuth 2.0 + API keys (Bearer)
      - Webhooks for document state changes
      - Drag-and-drop editor with rich media
      - E-signature legally binding (eIDAS, ESIGN)
      - Audit trail for all document interactions
      - CRM integrations (Salesforce, HubSpot, etc.)
      - Approval workflows
      - Deal rooms for buyer collaboration
      - Smart content for dynamic documents (Enterprise)
    sources:
      - https://www.pandadoc.com/pricing/
    updated: '2026-05-04'
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
