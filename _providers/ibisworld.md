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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Ibisworld Agentic Access
  operation_count: 7
  slug: ibisworld-agentic-access
  summary_line: 7 operations · 7 acting
api_count: 5
apis:
- description: Macroeconomic and business environment profile data.
  name: IBISWorld Business Environment API
  slug: ibisworld-business-environment-api
- description: Industry classification systems and taxonomies.
  name: IBISWorld Classification API
  slug: ibisworld-classification-api
- description: Company-specific information and lookups.
  name: IBISWorld Company API
  slug: ibisworld-company-api
- description: Bulk data export and download operations.
  name: IBISWorld Downloads API
  slug: ibisworld-downloads-api
- description: Industry research reports and market intelligence data.
  name: IBISWorld Industry API
  slug: ibisworld-industry-api
artifact_total: 14
collections:
- collection_type: open
  name: IBISWorld API
  slug: open-ibisworld
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ibisworld-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ibisworld-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ibisworld-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ibisworld-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ibisworld
- group: company
  title: ''
  type: Website
  url: https://www.ibisworld.com/
- group: start
  title: ''
  type: Portal
  url: https://www.ibisworld.com/api/
- group: docs
  title: ''
  type: Documentation
  url: https://api.ibisworld.com/docs/
- group: other
  title: ''
  type: Data Navigator
  url: https://data-navigator.ibisworld.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ibisworld.com/terms-of-use/
- group: design
  title: ''
  type: Rules
  url: rules/ibisworld-rules.yml
created: '2026-03-16'
description: IBISWorld is a leading provider of industry research and market intelligence, offering data on thousands of industries across global markets. IBISWorld provides APIs for accessing industry reports, market size data, and economic forecasts programmatically.
finops:
- name: Ibisworld Finops
  service_category: API
  slug: ibisworld-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ibisworld.png
layout: provider
modified: '2026-05-19'
name: IBISWorld
nav: Providers
network: true
overview: 'IBISWorld publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Business Environment API, Classification API, Company API, and 2 more. Tagged areas include Business Intelligence, Economics, Industry Data, and Market Research.


  The IBISWorld catalog on APIs.io includes 1 Spectral governance ruleset.


  IBISWorld''s developer surface includes authentication, developer portal, documentation, and 8 more developer resources.'
plans:
- name: Ibisworld Plans Pricing
  plan_count: 3
  slug: ibisworld-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 5
  name: Ibisworld Rate Limits
  slug: ibisworld-rate-limits
rules:
- name: IBISWorld API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: ibisworld-rules
scopes:
- name: Ibisworld Scopes
  scope_count: 0
  slug: ibisworld-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 34.3
  delta: -8.4
  facets:
    commercial_clarity: 26.3
    contract_quality: 58.4
    developer_ergonomics: 28.3
    discoverability: 64.8
    governance: 10.4
    operational_transparency: 7.9
  previous_composite: 42.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
security:
- kind: authentication
  name: Ibisworld Authentication
  slug: ibisworld-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Ibisworld Domain Security
  slug: ibisworld-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ibisworld
tags:
- Business Intelligence
- Economics
- Industry Data
- Market Research
website: https://www.ibisworld.com/
---
