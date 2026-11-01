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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ibisworld Agentic Access
  operation_count: 7
  slug: ibisworld-agentic-access
  summary_line: 7 operations
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
- group: commercial
  href: https://artifacts.apis.io/ibisworld/plans/ibisworld-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ibisworld-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/ibisworld/rate-limits/ibisworld-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ibisworld-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/ibisworld/finops/ibisworld-finops.yml
  title: ''
  type: FinOps
  url: finops/ibisworld-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.ibisworld.com/blog/
- group: other
  href: https://artifacts.apis.io/ibisworld/capabilities/ibisworld-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/ibisworld-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/ibisworld/agentic-access/ibisworld-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ibisworld-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/ibisworld/security/ibisworld-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ibisworld-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/ibisworld/authentication/ibisworld-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ibisworld-authentication.yml
- group: auth
  href: https://artifacts.apis.io/ibisworld/scopes/ibisworld-scopes.yml
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
  href: https://artifacts.apis.io/ibisworld/rules/ibisworld-rules.yml
  title: ''
  type: Rules
  url: rules/ibisworld-rules.yml
created: '2026-03-16'
description: IBISWorld is a leading provider of industry research and market intelligence, offering data on thousands of industries across global markets. IBISWorld provides APIs for accessing industry reports, market size data, and economic forecasts programmatically.
finops:
- has_sources: false
  method: generated
  name: Ibisworld Finops
  primary_unit: request
  service_category: API
  slug: ibisworld-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ibisworld.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.ibisworld.com over HTTP.
  name: IBISWorld MCP Server
  slug: ibisworld
modified: '2026-10-06'
name: IBISWorld
nav: Providers
network: true
overview: 'IBISWorld publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Business Environment API, Classification API, Company API, and 2 more. Tagged areas include Business Intelligence, Economics, Industry Data, and Market Research.


  The IBISWorld catalog on APIs.io includes 1 Spectral governance ruleset.


  IBISWorld''s developer surface includes engineering blog, authentication, developer portal, documentation, and 12 more developer resources.'
plans:
- name: Ibisworld Plans Pricing
  plan_count: 3
  slug: ibisworld-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Ibisworld Rate Limits
  slug: ibisworld-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 0
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
  composite: 32.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 47.9
    developer_ergonomics: 40.5
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 32.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ibisworld/ibisworld-2026-10-11T190552.png
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
