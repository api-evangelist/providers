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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ion Group Agentic Access
  operation_count: 3
  slug: ion-group-agentic-access
  summary_line: 3 operations
api_count: 2
apis:
- description: Detailed profiling of Special Purpose Acquisition Companies (SPACs). Gain access to real-time content and analytics covering the full spectrum of the SPAC market, from IPO Filing/Pricing, additional f
  name: Ion Group Dealogic Analytics SPAC API
  slug: dealogic-analytics-spac-api
- description: Get list of entities
  name: Ion Group Entities API
  slug: ion-group-entities-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ion Group Acuris Entities API
  slug: open-ion-group-entities-api
- collection_type: open
  name: Ion Group Acuris Entities API
  slug: open-ion-group
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ion-group-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ion-group-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ion-group-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/iongroup
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/iongroup
- group: company
  title: ''
  type: Website
  url: https://iongroup.com/
- group: start
  title: ''
  type: Portal
  url: https://iongroup.com/analytics/data-portal/
created: '2024-04-14'
description: ION Group is a visionary innovator delivering mission-critical trading and workflow automation software to financial institutions, corporations, central banks, and governments. ION helps customers improve decision-making, simplify complex processes, and empower people through automation.
finops:
- name: Ion Group Finops
  service_category: API
  slug: ion-group-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ion-group.png
layout: provider
modified: '2026-05-19'
name: Ion Group
nav: Providers
network: true
overview: 'Ion Group publishes 1 API on the [APIs.io](https://apis.io/) network: Entities API. Tagged areas include Analytics, Financial, Financial Services, and Trading.


  Ion Group''s developer surface includes authentication, developer portal, and 5 more developer resources.'
plans:
- name: Ion Group Plans Pricing
  plan_count: 3
  slug: ion-group-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Ion Group Rate Limits
  slug: ion-group-rate-limits
score:
  band: emerging
  composite: 26.1
  delta: -1.5
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 52.4
    developer_ergonomics: 21.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 27.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 30.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ion-group/refs/heads/main/screenshots/ion-group-2026-06-20T183527.png
security:
- kind: authentication
  name: Ion Group Authentication
  slug: ion-group-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ion Group Domain Security
  slug: ion-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ion-group
tags:
- Analytics
- Financial
- Financial Services
- Trading
website: https://iongroup.com/
---
