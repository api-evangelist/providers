---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Visio Agentic Access
  operation_count: 13
  slug: visio-agentic-access
  summary_line: 13 operations · 3 acting
api_count: 8
apis:
- description: Access and manipulate Visio files stored in OneDrive and SharePoint through Microsoft Graph. While direct Visio-specific REST endpoints are limited, Microsoft Graph provides file management capabiliti
  name: Microsoft Graph Visio API
  slug: microsoft-graph-visio-api
- description: Operations for controlling the Visio application host settings
  name: Microsoft Visio API Application API
  slug: visio-application-api
- description: Operations for reading and managing shape comments
  name: Microsoft Visio API Comments API
  slug: visio-comments-api
- description: Operations for accessing and managing Visio document properties and views
  name: Microsoft Visio API Documents API
  slug: visio-documents-api
- description: Operations for accessing hyperlinks attached to shapes
  name: Microsoft Visio API Hyperlinks API
  slug: visio-hyperlinks-api
- description: Operations for listing and managing pages within a Visio document
  name: Microsoft Visio API Pages API
  slug: visio-pages-api
- description: Operations for reading structured data associated with shapes
  name: Microsoft Visio API Shape Data API
  slug: visio-shape-data-api
- description: Operations for accessing and managing shapes on a Visio page
  name: Microsoft Visio API Shapes API
  slug: visio-shapes-api
artifact_total: 31
collections:
- collection_type: postman
  name: Visio JavaScript Application API
  slug: postman-visio-application-api
- collection_type: postman
  name: Visio JavaScript Application Comments API
  slug: postman-visio-comments-api
- collection_type: postman
  name: Visio JavaScript Application Documents API
  slug: postman-visio-documents-api
- collection_type: postman
  name: Visio JavaScript Application Hyperlinks API
  slug: postman-visio-hyperlinks-api
- collection_type: postman
  name: Visio JavaScript Application Pages API
  slug: postman-visio-pages-api
- collection_type: postman
  name: Visio JavaScript Application Shape Data API
  slug: postman-visio-shape-data-api
- collection_type: postman
  name: Visio JavaScript Application Shapes API
  slug: postman-visio-shapes-api
- collection_type: open
  name: Visio JavaScript API
  slug: open-visio-javascript
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-visio-api/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/visio-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/visio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/visio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/visio-authentication.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/en-us/microsoft-365
- group: operate
  title: ''
  type: StatusPage
  url: https://status.office.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/microsoft-365/visio/microsoft-visio-plans-and-pricing-compare-visio-options
- group: company
  title: ''
  type: Blog
  url: https://devblogs.microsoft.com/microsoft365dev/
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/javascript/api/overview/visio/release-notes
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/visio-javascript-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/visio-shape-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/visio-page-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/visio-shape-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/visio-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/visio-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/visio-rules.yml
created: '2024'
description: Microsoft Visio provides APIs for creating, editing, and managing Visio diagrams and drawings. The Visio JavaScript API enables developers to build Office Add-ins that interact with Visio diagrams embedded in SharePoint Online pages, accessing document elements such as pages, shapes, hyperlinks, comments, and shape data. Visio APIs support programmatic diagram manipulation, visual overlay creation, mouse event handling, and data visualization workflows.
examples:
- key_count: 2
  name: Visio Javascript Listpages Example
  slug: visio-javascript-listPages-example
- key_count: 2
  name: Visio Javascript Listshapes Example
  slug: visio-javascript-listShapes-example
finops:
- name: Visio Finops
  service_category: API
  slug: visio-finops
image: https://www.microsoft.com/en-us/microsoft-365/visio/visio-logo.png
json_schemas:
- name: Visio Page
  property_count: 6
  slug: visio-page
- name: Visio Shape
  property_count: 9
  slug: visio-shape
json_structures:
- name: Visio Shape Structure
  property_count: 0
  slug: visio-shape-structure
jsonld:
- class_count: 35
  name: Visio Context
  property_count: 8
  slug: visio-context
layout: provider
modified: '2026-05-19'
name: Microsoft Visio API
nav: Providers
network: true
overview: 'Microsoft Visio API publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Application API, Comments API, Documents API, and 4 more. Tagged areas include Business Process, Collaboration, Diagrams, Enterprise, and Flowcharts.


  The Microsoft Visio API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Microsoft Visio API''s developer surface includes authentication, pricing, engineering blog, changelog, and 15 more developer resources.'
plans:
- name: Visio Plans Pricing
  plan_count: 3
  slug: visio-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Visio Rate Limits
  slug: visio-rate-limits
rules:
- name: Microsoft Visio API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: visio-jsonschema-spectral-rules
- name: Microsoft Visio API API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 2
    info: 0
    warn: 6
  slug: visio-rules
score:
  band: strong
  composite: 60.5
  delta: -3.5
  facets:
    commercial_clarity: 71.1
    contract_quality: 68.6
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 63.2
  previous_composite: 64.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/visio/refs/heads/main/screenshots/visio-2026-06-20T201052.png
security:
- kind: authentication
  name: Visio Authentication
  slug: visio-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Visio Domain Security
  slug: visio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Visio Vulnerability Disclosure
  slug: visio-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: visio
tags:
- Business Process
- Collaboration
- Diagrams
- Enterprise
- Flowcharts
- Microsoft 365
- Visualization
website: https://developer.microsoft.com/en-us/microsoft-365
---
