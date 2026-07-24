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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Navis Agentic Access
  operation_count: 8
  slug: navis-agentic-access
  summary_line: 8 operations
api_count: 5
apis:
- description: Truck gate transactions
  name: Navis (Kaleris) Gate API
  slug: navis-gate-api
- description: Container hold management
  name: Navis (Kaleris) Holds API
  slug: navis-holds-api
- description: Work queues and crane operations
  name: Navis (Kaleris) Operations API
  slug: navis-operations-api
- description: Container and cargo unit tracking
  name: Navis (Kaleris) Units API
  slug: navis-units-api
- description: Vessel port call management and planning
  name: Navis (Kaleris) Vessel Visits API
  slug: navis-vessel-visits-api
artifact_total: 16
collections:
- collection_type: open
  name: Navis N4 Terminal Operating System REST API
  slug: open-navis-n4
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/navis-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/navis-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/navis-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/navis-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/navis
- group: start
  title: ''
  type: Portal
  url: https://kaleris.com/
- group: company
  title: ''
  type: Website
  url: https://kaleris.com/
- group: operate
  title: ''
  type: Support
  url: https://kaleris.com/support/
- group: operate
  title: ''
  type: Support
  url: https://kaleriscommunity.force.com/
- group: company
  title: ''
  type: Blog
  url: https://kaleris.com/resources/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kaleris.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kaleris.com/terms-and-conditions/
- group: operate
  title: ''
  type: StatusPage
  url: https://trust.kaleris.com/
created: '2026-03-18'
description: Navis (now operated by Kaleris) provides terminal operating systems and supply chain software for the maritime and intermodal industries. The flagship N4 product offers APIs for container tracking, vessel planning, berth scheduling, yard management, and gate operations, serving 650+ organizations across 95+ countries.
finops:
- name: Navis Finops
  service_category: API
  slug: navis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/navis.png
json_schemas:
- name: Navis N4 Container Unit
  property_count: 18
  slug: navis-unit
jsonld:
- class_count: 9
  name: Navis Context
  property_count: 13
  slug: navis-context
layout: provider
modified: '2026-05-19'
name: Navis (Kaleris)
nav: Providers
network: true
overview: 'Navis (Kaleris) publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Gate API, Holds API, Operations API, and 2 more. Tagged areas include Maritime, Port, Terminal, Container, and Logistics.


  The Navis (Kaleris) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Navis (Kaleris)''s developer surface includes authentication, developer portal, support, engineering blog, and 9 more developer resources.'
plans:
- name: Navis Plans Pricing
  plan_count: 3
  slug: navis-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 5
  name: Navis Rate Limits
  slug: navis-rate-limits
rules:
- name: Navis (Kaleris) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: navis-jsonschema-spectral-rules
score:
  band: developing
  composite: 57.4
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 67.1
    developer_ergonomics: 26.1
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 47.4
  previous_composite: 57.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/navis/refs/heads/main/screenshots/navis-2026-06-20T190102.png
security:
- kind: authentication
  name: Navis Authentication
  slug: navis-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Navis Domain Security
  slug: navis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Navis Trust Center
  slug: navis-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: navis
tags:
- Maritime
- Port
- Terminal
- Container
- Logistics
website: https://kaleris.com/
---
