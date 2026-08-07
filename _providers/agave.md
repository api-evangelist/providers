---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Agave Agentic Access
  operation_count: 11
  slug: agave-agentic-access
  summary_line: 11 operations · 2 acting
api_count: 11
apis:
- description: 'Agave Link is a front-end component that enables users to select source systems, authenticate with their construction software accounts, and share data with your application, handling OAuth flows for '
  name: Agave Link Component
  slug: agave-link
- description: Agave File Manager is a front-end component that allows users to pick files and folders from linked construction software accounts to share with your application.
  name: Agave File Manager Component
  slug: agave-file-manager
- description: Project budget and cost management resources.
  name: Agave Budgets API
  slug: agave-budgets-api
- description: Prime contracts and commitment management.
  name: Agave Contracts API
  slug: agave-contracts-api
- description: Job cost codes and cost types.
  name: Agave Cost Codes API
  slug: agave-cost-codes-api
- description: Employee records and workforce management.
  name: Agave Employees API
  slug: agave-employees-api
- description: Accounts payable invoices and billing.
  name: Agave Invoices API
  slug: agave-invoices-api
- description: Agave Link session management for user authentication.
  name: Agave Link Sessions API
  slug: agave-link-sessions-api
- description: Construction project management resources.
  name: Agave Projects API
  slug: agave-projects-api
- description: Employee timesheet and labor tracking.
  name: Agave Timesheets API
  slug: agave-timesheets-api
- description: Vendor and subcontractor management.
  name: Agave Vendors API
  slug: agave-vendors-api
artifact_total: 104
collections:
- collection_type: open
  name: Agave Unified Construction API
  slug: open-agave-unified-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/agave-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/agave-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agave-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agave-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agave-api
- group: start
  title: ''
  type: Portal
  url: https://docs.agaveapi.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.agaveapi.com/quickstart
- group: auth
  title: ''
  type: Authentication
  url: https://docs.agaveapi.com/agave-api/identifiers
- group: commercial
  title: ''
  type: Pricing
  url: https://www.agaveapi.com/software-vendors/pricing/
- group: auth
  title: ''
  type: Security
  url: https://security.agaveapi.com/
- group: company
  title: ''
  type: Partners
  url: https://www.agaveapi.com/partners/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agave-api
- group: build
  title: React SDK
  type: SDKs
  url: https://github.com/agave-api/react-agave-link
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/agave-unified-api-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-budget-list-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-budget-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-contract-list-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-contract-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-cost-code-list-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-cost-code-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-employee-list-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-employee-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-invoice-list-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-invoice-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-invoice-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-link-session-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-link-session-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-project-list-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-project-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-timesheet-list-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-timesheet-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-vendor-list-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-vendor-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-budget-list-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-budget-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-contract-list-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-contract-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-cost-code-list-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-cost-code-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-employee-list-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-employee-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-invoice-list-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-invoice-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-invoice-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-link-session-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-link-session-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-project-list-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-project-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-timesheet-list-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-timesheet-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-vendor-list-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-vendor-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/agave-unified-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/unified-api-budget-example.json
- group: build
  title: ''
  type: Examples
  url: examples/unified-api-budget-list-example.json
- group: build
  title: ''
  type: Examples
  url: examples/unified-api-contract-example.json
- group: build
  title: ''
  type: Examples
  url: examples/unified-api-contract-list-example.json
- group: build
  title: ''
  type: Examples
  url: examples/unified-api-cost-code-example.json
- group: build
  title: ''
  type: Examples
  url: examples/unified-api-cost-code-list-example.json
- group: build
  title: ''
  type: Examples
  url: examples/unified-api-employee-example.json
- group: build
  title: ''
  type: Examples
  url: examples/unified-api-employee-list-example.json
- group: build
  title: ''
  type: Examples
  url: examples/unified-api-invoice-example.json
- group: build
  title: ''
  type: Examples
  url: examples/unified-api-invoice-list-example.json
- group: build
  title: ''
  type: Examples
  url: examples/unified-api-invoice-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/unified-api-link-session-example.json
- group: build
  title: ''
  type: Examples
  url: examples/unified-api-link-session-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/unified-api-project-example.json
- group: build
  title: ''
  type: Examples
  url: examples/unified-api-project-list-example.json
- group: build
  title: ''
  type: Examples
  url: examples/unified-api-timesheet-example.json
- group: build
  title: ''
  type: Examples
  url: examples/unified-api-timesheet-list-example.json
- group: build
  title: ''
  type: Examples
  url: examples/unified-api-vendor-example.json
- group: build
  title: ''
  type: Examples
  url: examples/unified-api-vendor-list-example.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/agave-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/agave-vocabulary.yaml
- group: company
  title: ''
  type: Blog
  url: https://useagave.com/blog
created: '2025-03-01'
description: Agave is a unified API platform for the construction industry, enabling software companies and contractors to read and write data across 100+ construction and accounting software systems including Procore, Autodesk Build, QuickBooks, Sage, Viewpoint, and more.
examples:
- key_count: 8
  name: Unified Api Budget Example
  slug: unified-api-budget-example
- key_count: 3
  name: Unified Api Budget List Example
  slug: unified-api-budget-list-example
- key_count: 8
  name: Unified Api Contract Example
  slug: unified-api-contract-example
- key_count: 3
  name: Unified Api Contract List Example
  slug: unified-api-contract-list-example
- key_count: 5
  name: Unified Api Cost Code Example
  slug: unified-api-cost-code-example
- key_count: 3
  name: Unified Api Cost Code List Example
  slug: unified-api-cost-code-list-example
- key_count: 7
  name: Unified Api Employee Example
  slug: unified-api-employee-example
- key_count: 3
  name: Unified Api Employee List Example
  slug: unified-api-employee-list-example
- key_count: 8
  name: Unified Api Invoice Example
  slug: unified-api-invoice-example
- key_count: 3
  name: Unified Api Invoice List Example
  slug: unified-api-invoice-list-example
- key_count: 5
  name: Unified Api Invoice Request Example
  slug: unified-api-invoice-request-example
- key_count: 3
  name: Unified Api Link Session Example
  slug: unified-api-link-session-example
- key_count: 2
  name: Unified Api Link Session Request Example
  slug: unified-api-link-session-request-example
- key_count: 11
  name: Unified Api Project Example
  slug: unified-api-project-example
- key_count: 3
  name: Unified Api Project List Example
  slug: unified-api-project-list-example
- key_count: 8
  name: Unified Api Timesheet Example
  slug: unified-api-timesheet-example
- key_count: 3
  name: Unified Api Timesheet List Example
  slug: unified-api-timesheet-list-example
- key_count: 7
  name: Unified Api Vendor Example
  slug: unified-api-vendor-example
- key_count: 3
  name: Unified Api Vendor List Example
  slug: unified-api-vendor-list-example
features:
- description: Single REST API to read and write data across 100+ construction and accounting software systems with normalized data models.
  name: Unified Construction API
- description: Pre-built front-end component for user authentication that handles OAuth flows for all supported construction software platforms.
  name: Agave Link Authentication
- description: Automatic synchronization of jobs, financials, timesheets, and cost data between field systems and ERP platforms.
  name: ERP Sync
- description: AI-powered invoice capture, job matching, cost code coding, approval routing, and ERP sync for accounts payable workflows.
  name: AP Invoice Automation
- description: Direct passthrough of requests to source system APIs with Agave handling authentication and protocol translation.
  name: Passthrough Requests
- description: Real-time webhook notifications for data changes in connected construction software systems.
  name: Webhooks
- description: Sandbox mode for testing integrations without affecting production data in connected systems.
  name: Sandbox Environments
- description: Pre-built front-end component for browsing and selecting files from connected construction document storage systems.
  name: Agave File Manager
finops:
- name: Agave Finops
  service_category: Construction Tech / Integration
  slug: agave-finops
graphqls:
- description: This conceptual GraphQL schema represents the Agave Unified Construction API domain model. Agave provides a single API layer that normalizes data across 100+ construction and accounting software syste
  name: Agave GraphQL Schema
  slug: agave-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agave.png
integrations:
- description: Full read/write integration with Procore for projects, budgets, contracts, commitments, and documents.
  name: Procore
- description: Integration with Autodesk Build for project management and document storage.
  name: Autodesk Build
- description: Integration with QuickBooks Online for job costing, invoices, and financial data.
  name: QuickBooks Online
- description: Integration with Sage 100 Contractor for construction job costing and accounting.
  name: Sage 100 Contractor
- description: Integration with Sage Intacct cloud ERP for construction financial management.
  name: Sage Intacct
- description: Integration with Viewpoint Vista for construction ERP including SQL-based data access.
  name: Viewpoint Vista
- description: Integration with ServiceTitan for field service management and job costing.
  name: ServiceTitan
- description: Integration with Acumatica cloud ERP for construction financial management.
  name: Acumatica
- description: Integration with Foundation construction accounting software.
  name: Foundation
- description: Integration with CMiC enterprise construction ERP platform.
  name: CMiC
json_schemas:
- name: BudgetList
  property_count: 3
  slug: unified-api-budget-list
- name: Budget
  property_count: 8
  slug: unified-api-budget
- name: ContractList
  property_count: 3
  slug: unified-api-contract-list
- name: Contract
  property_count: 8
  slug: unified-api-contract
- name: CostCodeList
  property_count: 3
  slug: unified-api-cost-code-list
- name: CostCode
  property_count: 5
  slug: unified-api-cost-code
- name: EmployeeList
  property_count: 3
  slug: unified-api-employee-list
- name: Employee
  property_count: 7
  slug: unified-api-employee
- name: InvoiceList
  property_count: 3
  slug: unified-api-invoice-list
- name: InvoiceRequest
  property_count: 5
  slug: unified-api-invoice-request
- name: Invoice
  property_count: 8
  slug: unified-api-invoice
- name: LinkSessionRequest
  property_count: 2
  slug: unified-api-link-session-request
- name: LinkSession
  property_count: 3
  slug: unified-api-link-session
- name: ProjectList
  property_count: 3
  slug: unified-api-project-list
- name: Project
  property_count: 11
  slug: unified-api-project
- name: TimesheetList
  property_count: 3
  slug: unified-api-timesheet-list
- name: Timesheet
  property_count: 8
  slug: unified-api-timesheet
- name: VendorList
  property_count: 3
  slug: unified-api-vendor-list
- name: Vendor
  property_count: 7
  slug: unified-api-vendor
json_structures:
- name: Unified Api Budget List Structure
  property_count: 3
  slug: unified-api-budget-list-structure
- name: Unified Api Budget Structure
  property_count: 8
  slug: unified-api-budget-structure
- name: Unified Api Contract List Structure
  property_count: 3
  slug: unified-api-contract-list-structure
- name: Unified Api Contract Structure
  property_count: 8
  slug: unified-api-contract-structure
- name: Unified Api Cost Code List Structure
  property_count: 3
  slug: unified-api-cost-code-list-structure
- name: Unified Api Cost Code Structure
  property_count: 5
  slug: unified-api-cost-code-structure
- name: Unified Api Employee List Structure
  property_count: 3
  slug: unified-api-employee-list-structure
- name: Unified Api Employee Structure
  property_count: 7
  slug: unified-api-employee-structure
- name: Unified Api Invoice List Structure
  property_count: 3
  slug: unified-api-invoice-list-structure
- name: Unified Api Invoice Request Structure
  property_count: 5
  slug: unified-api-invoice-request-structure
- name: Unified Api Invoice Structure
  property_count: 8
  slug: unified-api-invoice-structure
- name: Unified Api Link Session Request Structure
  property_count: 2
  slug: unified-api-link-session-request-structure
- name: Unified Api Link Session Structure
  property_count: 3
  slug: unified-api-link-session-structure
- name: Unified Api Project List Structure
  property_count: 3
  slug: unified-api-project-list-structure
- name: Unified Api Project Structure
  property_count: 11
  slug: unified-api-project-structure
- name: Unified Api Timesheet List Structure
  property_count: 3
  slug: unified-api-timesheet-list-structure
- name: Unified Api Timesheet Structure
  property_count: 8
  slug: unified-api-timesheet-structure
- name: Unified Api Vendor List Structure
  property_count: 3
  slug: unified-api-vendor-list-structure
- name: Unified Api Vendor Structure
  property_count: 7
  slug: unified-api-vendor-structure
jsonld:
- class_count: 24
  name: Agave Unified Context
  property_count: 42
  slug: agave-unified-context
layout: provider
modified: '2026-04-19'
name: Agave
nav: Providers
network: true
overview: 'Agave publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Budgets API, Contracts API, Cost Codes API, and 6 more. Tagged areas include Accounting, Construction, and Integration.


  The Agave catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Agave''s developer surface includes authentication, developer portal, getting-started guide, pricing, code examples, engineering blog, and 69 more developer resources.'
plans:
- name: Agave Plans Pricing
  plan_count: 1
  slug: agave-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 1
  name: Agave Rate Limits
  slug: agave-rate-limits
rules:
- name: Agave API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: agave-jsonschema-spectral-rules
- name: Agave API Rules
  rule_count: 29
  severity_counts:
    error: 14
    hint: 0
    info: 0
    warn: 15
  slug: agave-spectral-rules
score:
  band: developing
  composite: 44.8
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 32.1
    developer_ergonomics: 39.1
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 44.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/screenshots/agave-2026-06-20T165757.png
security:
- kind: authentication
  name: Agave Authentication
  slug: agave-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Agave Domain Security
  slug: agave-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Agave Trust Center
  slug: agave-trust-center
  summary_line: SOC 2, GDPR
slug: agave
tags:
- Accounting
- Construction
- Integration
use_cases:
- description: Construction software companies integrate with 100+ other platforms via a single API instead of building and maintaining individual integrations.
  name: Construction Software Integration
- description: Automatically sync jobs, cost codes, and financials between project management systems like Procore and ERP systems like QuickBooks or Sage.
  name: ERP and PM Sync
- description: Automate AP invoice capture, job matching, and ERP posting using AI-powered invoice processing workflows.
  name: Invoice Processing Automation
- description: Pull budget, contract, commitment, and cost data from construction software for real-time job cost analysis and reporting.
  name: Job Costing
- description: Sync employee timesheets from field systems to accounting ERPs to eliminate manual payroll data entry.
  name: Timesheet Integration
- description: Enable users to select and share files from connected construction document storage systems using Agave File Manager.
  name: Document Management
website: https://docs.agaveapi.com
---
