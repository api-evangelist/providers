---
aid: agave
url: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/apis.yml
name: Agave
tags:
  - Accounting
  - Construction
  - Integration
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-03-01'
modified: '2026-04-19'
position: Consuming
description: Agave is a unified API platform for the construction industry, enabling software companies and contractors to read and write data across 100+ construction and accounting software systems including Procore, Autodesk Build, QuickBooks, Sage, Viewpoint, and more.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
apis:
  - aid: agave:unified-api
    name: Agave Unified Construction API
    tags:
      - Accounting
      - Budgets
      - Construction
      - Contracts
      - Integration
      - Projects
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.agaveapi.com
    humanURL: https://docs.agaveapi.com/
    properties:
      - url: https://docs.agaveapi.com/
        type: Documentation
      - url: https://docs.agaveapi.com/reference
        type: APIReference
      - url: https://docs.agaveapi.com/quickstart
        type: Quickstart
      - type: OpenAPI
        url: openapi/agave-unified-api-openapi.yml
    description: The Agave Unified Construction API provides a single REST API to read and write data from 100+ construction and accounting software systems. It normalizes data across platforms covering projects, budgets, contracts, commitments, purchase orders, invoices, cost codes, vendors, timesheets, and employees.
  - aid: agave:agave-link
    name: Agave Link Component
    tags:
      - Authentication
      - Construction
      - Front-End
      - OAuth
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.agaveapi.com
    humanURL: https://docs.agaveapi.com/
    properties:
      - url: https://docs.agaveapi.com/
        type: Documentation
      - url: https://github.com/agave-api/react-agave-link
        type: SDK
    description: Agave Link is a front-end component that enables users to select source systems, authenticate with their construction software accounts, and share data with your application, handling OAuth flows for all supported platforms.
  - aid: agave:agave-file-manager
    name: Agave File Manager Component
    tags:
      - Construction
      - Documents
      - Files
      - Front-End
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.agaveapi.com
    humanURL: https://docs.agaveapi.com/agave-file-manager/component
    properties:
      - url: https://docs.agaveapi.com/agave-file-manager/component
        type: Documentation
    description: Agave File Manager is a front-end component that allows users to pick files and folders from linked construction software accounts to share with your application.
common:
  - type: Portal
    url: https://docs.agaveapi.com
  - type: GettingStarted
    url: https://docs.agaveapi.com/quickstart
  - type: Authentication
    url: https://docs.agaveapi.com/agave-api/identifiers
  - type: Pricing
    url: https://www.agaveapi.com/software-vendors/pricing/
  - type: Security
    url: https://security.agaveapi.com/
  - type: Partners
    url: https://www.agaveapi.com/partners/
  - type: GitHubOrganization
    url: https://github.com/agave-api
  - type: SDK
    url: https://github.com/agave-api/react-agave-link
    title: React SDK
  - type: Features
    data:
      - name: Unified Construction API
        description: Single REST API to read and write data across 100+ construction and accounting software systems with normalized data models.
      - name: Agave Link Authentication
        description: Pre-built front-end component for user authentication that handles OAuth flows for all supported construction software platforms.
      - name: ERP Sync
        description: Automatic synchronization of jobs, financials, timesheets, and cost data between field systems and ERP platforms.
      - name: AP Invoice Automation
        description: AI-powered invoice capture, job matching, cost code coding, approval routing, and ERP sync for accounts payable workflows.
      - name: Passthrough Requests
        description: Direct passthrough of requests to source system APIs with Agave handling authentication and protocol translation.
      - name: Webhooks
        description: Real-time webhook notifications for data changes in connected construction software systems.
      - name: Sandbox Environments
        description: Sandbox mode for testing integrations without affecting production data in connected systems.
      - name: Agave File Manager
        description: Pre-built front-end component for browsing and selecting files from connected construction document storage systems.
  - type: UseCases
    data:
      - name: Construction Software Integration
        description: Construction software companies integrate with 100+ other platforms via a single API instead of building and maintaining individual integrations.
      - name: ERP and PM Sync
        description: Automatically sync jobs, cost codes, and financials between project management systems like Procore and ERP systems like QuickBooks or Sage.
      - name: Invoice Processing Automation
        description: Automate AP invoice capture, job matching, and ERP posting using AI-powered invoice processing workflows.
      - name: Job Costing
        description: Pull budget, contract, commitment, and cost data from construction software for real-time job cost analysis and reporting.
      - name: Timesheet Integration
        description: Sync employee timesheets from field systems to accounting ERPs to eliminate manual payroll data entry.
      - name: Document Management
        description: Enable users to select and share files from connected construction document storage systems using Agave File Manager.
  - type: Integrations
    data:
      - name: Procore
        description: Full read/write integration with Procore for projects, budgets, contracts, commitments, and documents.
      - name: Autodesk Build
        description: Integration with Autodesk Build for project management and document storage.
      - name: QuickBooks Online
        description: Integration with QuickBooks Online for job costing, invoices, and financial data.
      - name: Sage 100 Contractor
        description: Integration with Sage 100 Contractor for construction job costing and accounting.
      - name: Sage Intacct
        description: Integration with Sage Intacct cloud ERP for construction financial management.
      - name: Viewpoint Vista
        description: Integration with Viewpoint Vista for construction ERP including SQL-based data access.
      - name: ServiceTitan
        description: Integration with ServiceTitan for field service management and job costing.
      - name: Acumatica
        description: Integration with Acumatica cloud ERP for construction financial management.
      - name: Foundation
        description: Integration with Foundation construction accounting software.
      - name: CMiC
        description: Integration with CMiC enterprise construction ERP platform.
  - type: OpenAPI
    url: openapi/agave-unified-api-openapi.yml
  - type: JSONSchema
    url: json-schema/unified-api-budget-list-schema.json
  - type: JSONSchema
    url: json-schema/unified-api-budget-schema.json
  - type: JSONSchema
    url: json-schema/unified-api-contract-list-schema.json
  - type: JSONSchema
    url: json-schema/unified-api-contract-schema.json
  - type: JSONSchema
    url: json-schema/unified-api-cost-code-list-schema.json
  - type: JSONSchema
    url: json-schema/unified-api-cost-code-schema.json
  - type: JSONSchema
    url: json-schema/unified-api-employee-list-schema.json
  - type: JSONSchema
    url: json-schema/unified-api-employee-schema.json
  - type: JSONSchema
    url: json-schema/unified-api-invoice-list-schema.json
  - type: JSONSchema
    url: json-schema/unified-api-invoice-request-schema.json
  - type: JSONSchema
    url: json-schema/unified-api-invoice-schema.json
  - type: JSONSchema
    url: json-schema/unified-api-link-session-request-schema.json
  - type: JSONSchema
    url: json-schema/unified-api-link-session-schema.json
  - type: JSONSchema
    url: json-schema/unified-api-project-list-schema.json
  - type: JSONSchema
    url: json-schema/unified-api-project-schema.json
  - type: JSONSchema
    url: json-schema/unified-api-timesheet-list-schema.json
  - type: JSONSchema
    url: json-schema/unified-api-timesheet-schema.json
  - type: JSONSchema
    url: json-schema/unified-api-vendor-list-schema.json
  - type: JSONSchema
    url: json-schema/unified-api-vendor-schema.json
  - type: JSONStructure
    url: json-structure/unified-api-budget-list-structure.json
  - type: JSONStructure
    url: json-structure/unified-api-budget-structure.json
  - type: JSONStructure
    url: json-structure/unified-api-contract-list-structure.json
  - type: JSONStructure
    url: json-structure/unified-api-contract-structure.json
  - type: JSONStructure
    url: json-structure/unified-api-cost-code-list-structure.json
  - type: JSONStructure
    url: json-structure/unified-api-cost-code-structure.json
  - type: JSONStructure
    url: json-structure/unified-api-employee-list-structure.json
  - type: JSONStructure
    url: json-structure/unified-api-employee-structure.json
  - type: JSONStructure
    url: json-structure/unified-api-invoice-list-structure.json
  - type: JSONStructure
    url: json-structure/unified-api-invoice-request-structure.json
  - type: JSONStructure
    url: json-structure/unified-api-invoice-structure.json
  - type: JSONStructure
    url: json-structure/unified-api-link-session-request-structure.json
  - type: JSONStructure
    url: json-structure/unified-api-link-session-structure.json
  - type: JSONStructure
    url: json-structure/unified-api-project-list-structure.json
  - type: JSONStructure
    url: json-structure/unified-api-project-structure.json
  - type: JSONStructure
    url: json-structure/unified-api-timesheet-list-structure.json
  - type: JSONStructure
    url: json-structure/unified-api-timesheet-structure.json
  - type: JSONStructure
    url: json-structure/unified-api-vendor-list-structure.json
  - type: JSONStructure
    url: json-structure/unified-api-vendor-structure.json
  - type: JSON-LD
    url: json-ld/agave-unified-context.jsonld
  - type: Example
    url: examples/unified-api-budget-example.json
  - type: Example
    url: examples/unified-api-budget-list-example.json
  - type: Example
    url: examples/unified-api-contract-example.json
  - type: Example
    url: examples/unified-api-contract-list-example.json
  - type: Example
    url: examples/unified-api-cost-code-example.json
  - type: Example
    url: examples/unified-api-cost-code-list-example.json
  - type: Example
    url: examples/unified-api-employee-example.json
  - type: Example
    url: examples/unified-api-employee-list-example.json
  - type: Example
    url: examples/unified-api-invoice-example.json
  - type: Example
    url: examples/unified-api-invoice-list-example.json
  - type: Example
    url: examples/unified-api-invoice-request-example.json
  - type: Example
    url: examples/unified-api-link-session-example.json
  - type: Example
    url: examples/unified-api-link-session-request-example.json
  - type: Example
    url: examples/unified-api-project-example.json
  - type: Example
    url: examples/unified-api-project-list-example.json
  - type: Example
    url: examples/unified-api-timesheet-example.json
  - type: Example
    url: examples/unified-api-timesheet-list-example.json
  - type: Example
    url: examples/unified-api-vendor-example.json
  - type: Example
    url: examples/unified-api-vendor-list-example.json
  - type: SpectralRules
    url: rules/agave-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/agave-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/construction-data-sync.yaml
---
