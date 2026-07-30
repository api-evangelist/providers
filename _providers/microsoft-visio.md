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
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Microsoft Visio Agentic Access
  operation_count: 8
  slug: microsoft-visio-agentic-access
  summary_line: 8 operations
api_count: 7
apis:
- description: JavaScript API for building add-ins and extending Visio functionality in the browser with access to documents, pages, shapes, and comments.
  name: Visio JavaScript API
  slug: visio-javascript-api
- description: Operations for reading and managing shape comments.
  name: Microsoft Visio Comments API
  slug: microsoft-visio-comments-api
- description: Operations for Visio document metadata.
  name: Microsoft Visio Documents API
  slug: microsoft-visio-documents-api
- description: Operations for reading shape hyperlinks.
  name: Microsoft Visio Hyperlinks API
  slug: microsoft-visio-hyperlinks-api
- description: Operations for managing pages in Visio documents.
  name: Microsoft Visio Pages API
  slug: microsoft-visio-pages-api
- description: Operations for reading shape data items.
  name: Microsoft Visio Shape Data API
  slug: microsoft-visio-shape-data-api
- description: Operations for managing shapes on pages.
  name: Microsoft Visio Shapes API
  slug: microsoft-visio-shapes-api
artifact_total: 47
collections:
- collection_type: postman
  name: Microsoft Graph Visio Comments API
  slug: postman-microsoft-visio-comments-api
- collection_type: postman
  name: Microsoft Graph Visio Comments Documents API
  slug: postman-microsoft-visio-documents-api
- collection_type: postman
  name: Microsoft Graph Visio Comments Hyperlinks API
  slug: postman-microsoft-visio-hyperlinks-api
- collection_type: postman
  name: Microsoft Graph Visio Comments Pages API
  slug: postman-microsoft-visio-pages-api
- collection_type: postman
  name: Microsoft Graph Visio Comments Shape Data API
  slug: postman-microsoft-visio-shape-data-api
- collection_type: postman
  name: Microsoft Graph Visio Comments Shapes API
  slug: postman-microsoft-visio-shapes-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-visio/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-visio-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-visio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-visio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-visio-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-visio-scopes.yml
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/visio
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/visio-blog/bg-p/VisioBlog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/servicesagreement
- group: operate
  title: ''
  type: StatusPage
  url: https://status.microsoft365.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/microsoft-365/visio/microsoft-visio-plans-and-pricing-compare-visio-options
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OfficeDev
- group: design
  title: ''
  type: SpectralRules
  url: rules/microsoft-visio-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-visio-vocabulary.yaml
created: '2024'
description: APIs and resources for Microsoft Visio, a diagramming and vector graphics application that helps visualize data-connected business process flows. Provides programmatic access to diagrams, pages, shapes, data items, comments, and hyperlinks through Microsoft Graph and JavaScript APIs.
examples:
- key_count: 3
  name: Visio Graph Api Shape Data Item Example
  slug: visio-graph-api-shape-data-item-example
- key_count: 4
  name: Visio Graph Api Visio Comment Example
  slug: visio-graph-api-visio-comment-example
- key_count: 4
  name: Visio Graph Api Visio Hyperlink Example
  slug: visio-graph-api-visio-hyperlink-example
- key_count: 5
  name: Visio Graph Api Visio Page Example
  slug: visio-graph-api-visio-page-example
- key_count: 4
  name: Visio Graph Api Visio Shape Example
  slug: visio-graph-api-visio-shape-example
features:
- description: Render Visio diagrams in the browser via JavaScript API.
  name: Diagram Rendering
- description: Read data items attached to diagram shapes.
  name: Shape Data Access
- description: Navigate and list pages within Visio documents.
  name: Page Navigation
- description: Read and manage comments on shapes.
  name: Comment Support
- description: Access hyperlinks associated with diagram shapes.
  name: Hyperlink Management
finops:
- name: Microsoft Visio Finops
  service_category: API
  slug: microsoft-visio-finops
image: https://learn.microsoft.com/en-us/graph/images/visio-logo.png
json_schemas:
- name: ShapeDataItem
  property_count: 3
  slug: visio-graph-api-shape-data-item
- name: VisioComment
  property_count: 4
  slug: visio-graph-api-visio-comment
- name: VisioHyperlink
  property_count: 4
  slug: visio-graph-api-visio-hyperlink
- name: VisioPage
  property_count: 5
  slug: visio-graph-api-visio-page
- name: VisioShape
  property_count: 4
  slug: visio-graph-api-visio-shape
json_structures:
- name: Visio Graph Api Shape Data Item Structure
  property_count: 3
  slug: visio-graph-api-shape-data-item-structure
- name: Visio Graph Api Visio Comment Structure
  property_count: 4
  slug: visio-graph-api-visio-comment-structure
- name: Visio Graph Api Visio Hyperlink Structure
  property_count: 4
  slug: visio-graph-api-visio-hyperlink-structure
- name: Visio Graph Api Visio Page Structure
  property_count: 5
  slug: visio-graph-api-visio-page-structure
- name: Visio Graph Api Visio Shape Structure
  property_count: 4
  slug: visio-graph-api-visio-shape-structure
jsonld:
- class_count: 7
  name: Microsoft Visio Graph Api Context
  property_count: 13
  slug: microsoft-visio-graph-api-context
layout: provider
modified: '2026-05-19'
name: Microsoft Visio
nav: Providers
network: true
overview: 'Microsoft Visio publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Comments API, Documents API, Hyperlinks API, and 3 more. Tagged areas include Business Process, Diagramming, Flowcharts, Microsoft 365, and Visualization.


  The Microsoft Visio catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Microsoft Visio''s developer surface includes authentication, support, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Microsoft Visio Plans Pricing
  plan_count: 3
  slug: microsoft-visio-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 5
  name: Microsoft Visio Rate Limits
  slug: microsoft-visio-rate-limits
rules:
- name: Microsoft Visio API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: microsoft-visio-jsonschema-spectral-rules
- name: Microsoft Visio API Rules
  rule_count: 24
  severity_counts:
    error: 12
    hint: 0
    info: 0
    warn: 12
  slug: microsoft-visio-spectral-rules
scopes:
- name: Microsoft Visio Scopes
  scope_count: 2
  slug: microsoft-visio-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 58.2
  delta: -6.9
  facets:
    commercial_clarity: 71.1
    contract_quality: 68.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 65.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-visio/refs/heads/main/screenshots/microsoft-visio-2026-06-20T185541.png
security:
- kind: authentication
  name: Microsoft Visio Authentication
  slug: microsoft-visio-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Visio Domain Security
  slug: microsoft-visio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Visio Vulnerability Disclosure
  slug: microsoft-visio-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-visio
tags:
- Business Process
- Diagramming
- Flowcharts
- Microsoft 365
- Visualization
use_cases:
- description: Programmatically analyze network diagrams for infrastructure review.
  name: Network Topology Analysis
- description: Extract and analyze business process flow data from diagrams.
  name: Business Process Review
- description: Inspect diagram shapes and data for compliance validation.
  name: Compliance Auditing
---
