---
aid: scout-rfp
name: Scout RFP
description: Scout RFP is a cloud-based strategic sourcing and procurement platform that streamlines the RFP (Request for Proposal) process for procurement teams. Founded in 2014 and acquired by Workday, Scout RFP is now known as Workday Strategic Sourcing. The platform provides REST APIs for managing sourcing events, suppliers, contracts, awards, attachments, and spend categories, enabling integrations with ERP, CRM, and procurement systems.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Procurement
  - Sourcing
  - RFP
  - Supply Chain
  - Workday
created: '2026-05-02'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/scout-rfp/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: scout-rfp:workday-strategic-sourcing
    name: Workday Strategic Sourcing API
    description: The Workday Strategic Sourcing API (formerly Scout RFP API) provides programmatic access to sourcing and procurement workflows. API services cover events (RFPs, RFIs, auctions), suppliers, contracts, awards, attachments, payments, projects, reports, spend categories, and user management via SCIM. Authentication uses API key and user token headers.
    humanURL: https://apidocs.workdayspend.com/
    tags:
      - Procurement
      - Sourcing
      - RFP
      - Workday
      - Events
    properties:
      - type: Documentation
        url: https://apidocs.workdayspend.com/
      - type: GettingStarted
        url: https://apidocs.workdayspend.com/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/scout-rfp/refs/heads/main/openapi/scout-rfp-events-openapi.yml
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/scout-rfp/refs/heads/main/rules/scout-rfp-rules.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/scout-rfp/refs/heads/main/json-schema/scout-rfp-event-schema.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/scout-rfp/refs/heads/main/json-ld/scout-rfp-context.jsonld
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/scout-rfp/refs/heads/main/json-structure/scout-rfp-event-structure.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/scout-rfp/refs/heads/main/examples/scout-rfp-list-events-example.json
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/scout-rfp/refs/heads/main/vocabulary/scout-rfp-vocabulary.yml
      - type: NaftikoCapabilities
        url: https://raw.githubusercontent.com/api-evangelist/scout-rfp/refs/heads/main/capabilities/strategic-sourcing.yaml
  - aid: scout-rfp:events-api
    name: Events API
    description: Manage sourcing events including RFPs, RFIs, and reverse auctions. Supports creating events from templates, updating event details, managing supplier invitations, worksheets, line items, and bid collection. Version 1.3 is the latest stable release.
    humanURL: https://apidocs.workdayspend.com/services/events/v1.html
    tags:
      - Events
      - RFP
      - Procurement
      - Sourcing
    properties:
      - type: Documentation
        url: https://apidocs.workdayspend.com/services/events/v1.html
  - aid: scout-rfp:suppliers-api
    name: Suppliers API
    description: Manage supplier companies and contacts in the Workday Strategic Sourcing platform. Supports creating, updating, and querying supplier records with version 1.1 of the API.
    humanURL: https://apidocs.workdayspend.com/services/suppliers/v1.html
    tags:
      - Suppliers
      - Procurement
      - Vendor Management
    properties:
      - type: Documentation
        url: https://apidocs.workdayspend.com/services/suppliers/v1.html
  - aid: scout-rfp:contracts-api
    name: Contracts API
    description: Manage contracts within the strategic sourcing platform, including creation, retrieval, and updates. Version 1.1 of the API.
    humanURL: https://apidocs.workdayspend.com/services/contracts/v1.html
    tags:
      - Contracts
      - Procurement
      - Legal
    properties:
      - type: Documentation
        url: https://apidocs.workdayspend.com/services/contracts/v1.html
  - aid: scout-rfp:awards-api
    name: Awards API
    description: Manage sourcing award decisions for completed events, tracking supplier selection outcomes and award values. Version 1.1.
    humanURL: https://apidocs.workdayspend.com/services/awards/v1.html
    tags:
      - Awards
      - Procurement
      - Sourcing
    properties:
      - type: Documentation
        url: https://apidocs.workdayspend.com/services/awards/v1.html
  - aid: scout-rfp:attachments-api
    name: Attachments API
    description: Upload and manage file attachments associated with sourcing events, contracts, and other procurement objects. Version 1.0.
    humanURL: https://apidocs.workdayspend.com/services/attachments/v1.html
    tags:
      - Attachments
      - Files
      - Procurement
    properties:
      - type: Documentation
        url: https://apidocs.workdayspend.com/services/attachments/v1.html
  - aid: scout-rfp:payments-api
    name: Payments API
    description: Manage payment records associated with procurement transactions and contract fulfillment. Version 1.0.
    humanURL: https://apidocs.workdayspend.com/services/payments/v1.html
    tags:
      - Payments
      - Procurement
      - Finance
    properties:
      - type: Documentation
        url: https://apidocs.workdayspend.com/services/payments/v1.html
  - aid: scout-rfp:projects-api
    name: Projects API
    description: Manage procurement projects that organize and group related sourcing events and activities. Version 1.0.
    humanURL: https://apidocs.workdayspend.com/services/projects/v1.html
    tags:
      - Projects
      - Procurement
      - Organization
    properties:
      - type: Documentation
        url: https://apidocs.workdayspend.com/services/projects/v1.html
  - aid: scout-rfp:reports-api
    name: Reports API
    description: Access procurement analytics and reporting data from the Workday Strategic Sourcing platform. Version 1.0.
    humanURL: https://apidocs.workdayspend.com/services/reports/v1.html
    tags:
      - Reports
      - Analytics
      - Procurement
    properties:
      - type: Documentation
        url: https://apidocs.workdayspend.com/services/reports/v1.html
  - aid: scout-rfp:scim-api
    name: SCIM Users API
    description: Manage users in the Workday Strategic Sourcing platform using the SCIM 2.0 standard, enabling integration with identity providers for automated user provisioning and deprovisioning.
    humanURL: https://apidocs.workdayspend.com/services/scim/v2.html
    tags:
      - SCIM
      - User Management
      - Identity
      - SSO
    properties:
      - type: Documentation
        url: https://apidocs.workdayspend.com/services/scim/v2.html
  - aid: scout-rfp:spend-categories-api
    name: Spend Categories API
    description: Manage spend category taxonomies used to classify procurement spending within the Workday Strategic Sourcing platform. Version 1.0.
    humanURL: https://apidocs.workdayspend.com/services/spend_categories/v1.html
    tags:
      - Spend Categories
      - Procurement
      - Classification
    properties:
      - type: Documentation
        url: https://apidocs.workdayspend.com/services/spend_categories/v1.html
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
