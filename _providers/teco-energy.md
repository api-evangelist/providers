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
  name: Teco Energy Agentic Access
  operation_count: 11
  slug: teco-energy-agentic-access
  summary_line: 11 operations · 3 acting
api_count: 6
apis:
- description: Tampa Electric provides a developer portal powered by Azure API Management at developer.tecoenergy.com. The portal enables developers to discover APIs, review documentation, try APIs interactively, an
  name: Tampa Electric API Management
  slug: developer-api
- description: The Accounts API from TECO Energy — 1 operation(s) for accounts.
  name: TECO Energy Accounts API
  slug: teco-energy-accounts-api
- description: The Billing API from TECO Energy — 3 operation(s) for billing.
  name: TECO Energy Billing API
  slug: teco-energy-billing-api
- description: The Energy Usage API from TECO Energy — 1 operation(s) for energy usage.
  name: TECO Energy Energy Usage API
  slug: teco-energy-energy-usage-api
- description: The Outages API from TECO Energy — 4 operation(s) for outages.
  name: TECO Energy Outages API
  slug: teco-energy-outages-api
- description: The Service Requests API from TECO Energy — 1 operation(s) for service requests.
  name: TECO Energy Service Requests API
  slug: teco-energy-service-requests-api
artifact_total: 22
collections:
- collection_type: open
  name: Tampa Electric Account API
  slug: open-teco-energy-account
- collection_type: open
  name: Tampa Electric Outage API
  slug: open-teco-energy-outage
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/teco-energy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/teco-energy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/teco-energy-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.tecoenergy.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.tecoenergy.com/
- group: company
  title: ''
  type: Website
  url: https://www.tampaelectric.com/
- group: start
  title: ''
  type: Portal
  url: https://account.tecoenergy.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://account.tecoenergy.com/Outage/Outagemap
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/teco-energy
created: '2026-03-24'
description: TECO Energy is an energy holding company and subsidiary of Emera Inc., operating Tampa Electric (electric utility serving west central Florida) and Peoples Gas (natural gas utility serving Florida). TECO Energy provides a developer portal powered by Azure API Management at developer.tecoenergy.com, exposing APIs for outage management, account services, energy usage, billing, and grid operations. Tampa Electric serves approximately 800,000 customers across the Tampa Bay area and parts of central Florida.
examples:
- key_count: 2
  name: Teco Energy Get Usage Example
  slug: teco-energy-get-usage-example
- key_count: 2
  name: Teco Energy List Outages Example
  slug: teco-energy-list-outages-example
finops:
- name: Teco Energy Finops
  service_category: Energy / Utilities
  slug: teco-energy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/teco-energy.png
json_schemas:
- name: Tampa Electric Customer Account
  property_count: 9
  slug: teco-energy-account
- name: Tampa Electric Outage
  property_count: 9
  slug: teco-energy-outage
json_structures:
- name: Teco Energy Outage Structure
  property_count: 0
  slug: teco-energy-outage-structure
jsonld:
- class_count: 36
  name: Teco Energy Context
  property_count: 0
  slug: teco-energy-context
layout: provider
modified: '2026-05-19'
name: TECO Energy
nav: Providers
network: true
overview: 'TECO Energy publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Billing API, Energy Usage API, and 2 more. Tagged areas include Energy, Utilities, Electric, Natural Gas, and Smart Grid.


  The TECO Energy catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  TECO Energy''s developer surface includes authentication, developer portal, and 7 more developer resources.'
plans:
- name: Teco Energy Plans Pricing
  plan_count: 1
  slug: teco-energy-plans-pricing
press:
- date: '2026-05-25'
  title: TECO
  url: https://www.fox13news.com/tag/organization/teco
- date: '2026-05-25'
  title: Carlos Alfonso - TECO Energy
  url: https://www.linkedin.com/in/carlos-alfonso-07333937
- date: '2026-05-25'
  title: Social Media
  url: https://www.tampaelectric.com/socialmedia/
- date: '2026-05-25'
  title: Foxconn eyes $1 trillion AI data centre market with TECO ...
  url: https://invezz.com/news/2025/07/30/foxconn-eyes-1-trillion-ai-data-centre-market-with-teco-stake/
- date: '2026-05-25'
  title: Tampa Electric is warning customers about a growing ...
  url: https://www.facebook.com/FOX13TampaBay/posts/tampa-electric-is-warning-customers-about-a-growing-wave-of-utility-scams-using-/1458260039680854/
random_paper: 69
rate_limits:
- limit_count: 1
  name: Teco Energy Rate Limits
  slug: teco-energy-rate-limits
rules:
- name: TECO Energy API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: teco-energy-jsonschema-spectral-rules
- name: TECO Energy API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 1
    info: 0
    warn: 5
  slug: teco-energy-rules
score:
  band: developing
  composite: 44.0
  delta: -7.9
  facets:
    commercial_clarity: 28.9
    contract_quality: 75.4
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 51.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 23.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/teco-energy/refs/heads/main/screenshots/teco-energy-2026-06-20T195017.png
security:
- kind: authentication
  name: Teco Energy Authentication
  slug: teco-energy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Teco Energy Domain Security
  slug: teco-energy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: teco-energy
tags:
- Energy
- Utilities
- Electric
- Natural Gas
- Smart Grid
- Tampa Bay
- Fortune 1000
website: https://www.tecoenergy.com
---
