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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Ibisworld Agentic Access
  operation_count: 7
  slug: ibisworld-agentic-access
  summary_line: 7 operations · 7 acting
api_count: 1
apis:
- baseURL: https://api.ibisworld.com/v3
  baseurl_source: declared
  description: Macroeconomic and business environment profile data.
  name: IBISWorld Business Environment API
  slug: ibisworld-business-environment-api
- baseURL: https://api.ibisworld.com/v3
  baseurl_source: declared
  description: Industry classification systems and taxonomies.
  name: IBISWorld Classification API
  slug: ibisworld-classification-api
- baseURL: https://api.ibisworld.com/v3
  baseurl_source: declared
  description: Company-specific information and lookups.
  name: IBISWorld Company API
  slug: ibisworld-company-api
- baseURL: https://api.ibisworld.com/v3
  baseurl_source: declared
  description: Bulk data export and download operations.
  name: IBISWorld Downloads API
  slug: ibisworld-downloads-api
- baseURL: https://api.ibisworld.com/v3
  baseurl_source: declared
  description: Industry research reports and market intelligence data.
  name: IBISWorld Industry API
  slug: ibisworld-industry-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: IBISWorld Business Environment API
  slug: open-ibisworld-business-environment-api
- collection_type: open
  name: IBISWorld Business Environment Classification API
  slug: open-ibisworld-classification-api
- collection_type: open
  name: IBISWorld Business Environment Company API
  slug: open-ibisworld-company-api
- collection_type: open
  name: IBISWorld Business Environment Downloads API
  slug: open-ibisworld-downloads-api
- collection_type: open
  name: IBISWorld Business Environment Industry API
  slug: open-ibisworld-industry-api
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
random_paper: 9
rate_limits:
- limit_count: 5
  name: Ibisworld Rate Limits
  slug: ibisworld-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: IBISWorld API Rules
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
  composite: 31.0
  coverage:
    artifact_dirs: 12
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 53.2
    developer_ergonomics: 38.1
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 31.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
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
