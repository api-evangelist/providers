---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'REST/JSON API surface for the JAGGAER (formerly SciQuest) Advanced Sourcing Optimizer, secured with OAuth 2.0 client-credentials. Grouped into the Customer Host Entity Service (query ASO events for a '
  name: JAGGAER Advanced Sourcing Optimizer (ASO) API
  slug: jaggaer-advanced-sourcing-optimizer-aso-api
artifact_total: 5
asyncapis:
- description: ''
  name: Sciquest Webhooks
  slug: sciquest-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sciquest-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.jaggaer.com/
- group: start
  title: ''
  type: Portal
  url: https://www.jaggaer.com/solutions/integrations
- group: docs
  title: ''
  type: Documentation
  url: https://asodocs.jaggaer.com/
- group: docs
  title: ''
  type: APIReference
  url: https://asodocs.jaggaer.com/
- group: company
  title: ''
  type: Blog
  url: https://www.jaggaer.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jaggaer.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: security/sciquest-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/sciquest-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sciquest-lifecycle.yml
created: '2026-07-17'
description: SciQuest was a spend-management and e-procurement software company founded in 1995 that grew into a source-to-settle suite spanning e-procurement, sourcing, contract lifecycle management, spend analytics, accounts payable and supplier management. In 2017 SciQuest rebranded as JAGGAER and consolidated its products into the JAGGAER One source-to-pay platform. JAGGAER exposes REST/JSON public APIs (request/response and event-driven push), cXML transactional messaging, an OAuth 2.0-secured Advanced Sourcing Optimizer (ASO) API, and 40+ prebuilt ERP connectors (SAP, Oracle, Workday, Microsoft Dynamics, NetSuite, Ellucian). This profile enriches the SciQuest lead against its live successor developer surface.
image: https://www.jaggaer.com/app/themes/jaggaer/assets/images/logo.svg
layout: provider
modified: '2026-07-21'
name: SciQuest
nav: Providers
network: true
overview: 'SciQuest publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise Software, Procurement, eProcurement, and Spend Management.


  The SciQuest catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SciQuest''s developer surface includes developer portal, documentation, API reference, engineering blog, and 6 more developer resources.'
random_paper: 20
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 40.5
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 34.1
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Sciquest Authentication
  slug: sciquest-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Sciquest Domain Security
  slug: sciquest-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Sciquest Trust Center
  slug: sciquest-trust-center
  summary_line: ISO/IEC 27001:2022, ISO/IEC 27017:2015, ISO/IEC 27018:2019, ISO 22301:2019, ISO/IEC 42001:2023, ISO 9001:2015, SOC 1, SOC 2 Type II, PCI DSS v4.0, Cyber Essentials, Cyber Essentials Plus
slug: sciquest
tags:
- Company
- Enterprise Software
- Procurement
- eProcurement
- Spend Management
- Source-to-Pay
- Supplier Management
- Sourcing
website: https://www.jaggaer.com/
---
