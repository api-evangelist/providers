---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Emitwise Agentic Access
  operation_count: 7
  slug: emitwise-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 5
apis:
- description: Physical or virtual locations whose emissions are tracked.
  name: Emitwise Facilities API
  slug: emitwise-facilities-api
- description: Activity-data file uploads used to calculate emissions.
  name: Emitwise Files API
  slug: emitwise-files-api
- description: Sustainability initiatives that group emissions data.
  name: Emitwise Projects API
  slug: emitwise-projects-api
- description: Activity data schema definitions.
  name: Emitwise Schema API
  slug: emitwise-schema-api
- description: Aggregated Scope 3 supplier emissions data.
  name: Emitwise Suppliers API
  slug: emitwise-suppliers-api
artifact_total: 13
collections:
- collection_type: open
  name: Emitwise API
  slug: open-emitwise-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/emitwise-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/emitwise-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/emitwise-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://emitwise.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.emitwise.com/
- group: start
  title: ''
  type: APIPortal
  url: https://docs.emitwise.com/
- group: other
  title: ''
  type: Dashboard
  url: https://dash.emitwise.com/
- group: other
  title: ''
  type: PCFCalculator
  url: https://emitwise.com/pcf-calculator/
- group: commercial
  title: ''
  type: Privacy
  url: https://emitwise.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://emitwise.com/terms/
- group: other
  title: ''
  type: CookiePolicy
  url: https://emitwise.com/cookie-policy/
- group: company
  title: ''
  type: Blog
  url: https://emitwise.com/home/feed/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.greenprojecttech.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.greenprojecttech.com/contact/get-in-touch
- group: build
  title: ''
  type: GitHub
  url: https://github.com/emitwise
created: '2026-05-25'
description: Emitwise is a London-based carbon accounting and Scope 3 reporting platform that uses AI to help large enterprises measure, manage, and reduce their product carbon footprint (PCF) and supply-chain greenhouse-gas emissions. The platform ingests spend data, activity data, and supplier information, auto-classifies suppliers, and produces audit-ready emissions reporting aligned with the GHG Protocol (Scope 1, 2, and 3) and frameworks such as CDP and CSRD. The Emitwise developer API at api.emitwise.com exposes facilities, projects, activity-data files, schema metadata, and aggregated supplier emissions data so customers can integrate carbon accounting into procurement, ERP, and sustainability reporting systems. Access is granted per-customer through Emitwise CSMs; API keys are generated from the Company settings area of the dashboard. In July 2025, Emitwise was acquired by Green Project Technologies; the Emitwise platform and team are now part of Green Project's end-to-end decarbonization
  solutions, while the existing Emitwise developer portal and API endpoints remain live for customers.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/emitwise.png
json_schemas:
- name: Emitwise Facility
  property_count: 5
  slug: emitwise-facility
- name: Emitwise Supplier
  property_count: 6
  slug: emitwise-supplier
jsonld:
- class_count: 17
  name: Emitwise Context
  property_count: 1
  slug: emitwise-context
layout: provider
modified: '2026-05-25'
name: Emitwise
nav: Providers
network: true
overview: 'Emitwise publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Facilities API, Files API, Projects API, and 2 more. Tagged areas include Carbon Accounting, Greenhouse Gas, Scope 3, Supply Chain Emissions, and Product Carbon Footprint.


  The Emitwise catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Emitwise''s developer surface includes authentication, documentation, privacy policy, engineering blog, GitHub presence, and 10 more developer resources.'
random_paper: 51
rules:
- name: Emitwise API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: emitwise-jsonschema-spectral-rules
score:
  band: thin
  composite: 40.7
  delta: -4.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 72.0
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 44.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/emitwise/refs/heads/main/screenshots/emitwise-2026-06-20T180633.png
security:
- kind: authentication
  name: Emitwise Authentication
  slug: emitwise-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Emitwise Domain Security
  slug: emitwise-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: emitwise
tags:
- Carbon Accounting
- Greenhouse Gas
- Scope 3
- Supply Chain Emissions
- Product Carbon Footprint
- Sustainability
- ESG
- CDP
- CSRD
- GHG Protocol
- Climate
- Procurement
- AI
website: https://emitwise.com/
---
