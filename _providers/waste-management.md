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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Waste Management Agentic Access
  operation_count: 17
  slug: waste-management-agentic-access
  summary_line: 17 operations · 2 acting
api_count: 7
apis:
- description: Retrieve and manage customer service cases.
  name: Waste Management Cases API
  slug: waste-management-cases-api
- description: Manage billing and service contacts.
  name: Waste Management Contacts API
  slug: waste-management-contacts-api
- description: Retrieve and manage customer account information.
  name: Waste Management Customers API
  slug: waste-management-customers-api
- description: Retrieve invoice summaries and details.
  name: Waste Management Invoices API
  slug: waste-management-invoices-api
- description: Retrieve and update customer preference settings.
  name: Waste Management Preferences API
  slug: waste-management-preferences-api
- description: Retrieve service details, schedules, materials, and ETAs.
  name: Waste Management Services API
  slug: waste-management-services-api
- description: Retrieve disposal tickets and summaries.
  name: Waste Management Tickets API
  slug: waste-management-tickets-api
artifact_total: 24
collections:
- collection_type: open
  name: Waste Management Customer API
  slug: open-waste-management-customer-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/waste-management-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/waste-management-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/waste-management-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/waste-management
- group: company
  title: ''
  type: Website
  url: https://www.wm.com
- group: start
  title: ''
  type: Portal
  url: https://api.wm.com/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/waste-management-customer-api-openapi.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/waste-management-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/waste-management-service-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/waste-management-invoice-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/waste-management-service-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/waste-management-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/waste-management-vocabulary.yml
created: '2026-05-03'
description: Waste Management (WM) is the largest environmental services company in North America, providing waste collection, transfer, disposal, and recycling services to over 20 million residential, commercial, industrial, and municipal customers across the United States. WM provides RESTful APIs for customers and third-party integrators to access account data including balance, services, invoices, pickup schedules, and ETAs via JWT authentication.
examples:
- key_count: 3
  name: Waste Management Getcustomeroverview Example
  slug: waste-management-getCustomerOverview-example
- key_count: 3
  name: Waste Management Getserviceeta Example
  slug: waste-management-getServiceEta-example
- key_count: 3
  name: Waste Management Listinvoices Example
  slug: waste-management-listInvoices-example
- key_count: 3
  name: Waste Management Listservices Example
  slug: waste-management-listServices-example
finops:
- name: Waste Management Finops
  service_category: Environmental / Waste Services
  slug: waste-management-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/waste-management.png
json_schemas:
- name: Waste Management Invoice
  property_count: 7
  slug: waste-management-invoice
- name: Waste Management Service
  property_count: 8
  slug: waste-management-service
json_structures:
- name: Waste Management Service Structure
  property_count: 0
  slug: waste-management-service-structure
jsonld:
- class_count: 10
  name: Waste Management Context
  property_count: 21
  slug: waste-management-context
layout: provider
modified: '2026-05-19'
name: Waste Management
nav: Providers
network: true
overview: 'Waste Management publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Cases API, Contacts API, Customers API, and 4 more. Tagged areas include Environmental Services, Fortune 500, Recycling, Solid Waste, and Sustainability.


  The Waste Management catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Waste Management''s developer surface includes authentication, developer portal, and 11 more developer resources.'
plans:
- name: Waste Management Plans Pricing
  plan_count: 1
  slug: waste-management-plans-pricing
press:
- date: '2026-05-25'
  title: Veolia and Mistral AI_ join forces to revolutionize resource ...
  url: https://www.veolia.com/en/our-media/press-releases/veolia-and-mistral-ai-join-forces-revolutionize-resource-efficiency
- date: '2026-05-25'
  title: What is AI in Waste Management Market Size?
  url: https://www.insightaceanalytic.com/report/ai-in-waste-management-market/2354
- date: '2026-05-25'
  title: 'Smart waste management: A paradigm shift enabled by ...'
  url: https://www.sciencedirect.com/science/article/pii/S2949750724000385
- date: '2026-05-25'
  title: AI and Machine Learning for Optimizing Waste ...
  url: https://ascelibrary.org/doi/10.1061/JHTRBP.HZENG-1483
- date: '2026-05-25'
  title: WM Announces New, Modernized High-Tech Recycling and ...
  url: https://investors.wm.com/news-releases/news-release-details/wm-announces-new-modernized-high-tech-recycling-and-renewable
random_paper: 22
rate_limits:
- limit_count: 1
  name: Waste Management Rate Limits
  slug: waste-management-rate-limits
rules:
- name: Waste Management API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: waste-management-jsonschema-spectral-rules
- name: Waste Management API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 0
    warning: 3
  slug: waste-management-rules
score:
  band: thin
  composite: 40.5
  delta: -5.8
  facets:
    commercial_clarity: 13.2
    contract_quality: 70.9
    developer_ergonomics: 19.6
    discoverability: 72.2
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 46.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/waste-management/refs/heads/main/screenshots/waste-management-2026-06-20T201242.png
security:
- kind: authentication
  name: Waste Management Authentication
  slug: waste-management-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Waste Management Domain Security
  slug: waste-management-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: waste-management
tags:
- Environmental Services
- Fortune 500
- Recycling
- Solid Waste
- Sustainability
- Waste Management
website: https://www.wm.com
---
