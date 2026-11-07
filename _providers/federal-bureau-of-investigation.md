---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Federal Bureau Of Investigation Agentic Access
  operation_count: 1
  slug: federal-bureau-of-investigation-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: The FBI Crime Data Explorer (CDE) provides public access to Uniform Crime Reporting (UCR) data through a JSON API. The API exposes summary statistics, agency-level participation, offense and arrest co
  name: FBI Crime Data Explorer
  slug: crime-data-explorer
- baseURL: https://api.usa.gov/crime/fbi/cde
  baseurl_source: declared
  description: Art Crime API
  name: Federal Bureau of Investigation Artcrimes API
  slug: federal-bureau-of-investigation-artcrimes-api
- baseURL: https://api.usa.gov/crime/fbi/cde
  baseurl_source: declared
  description: Wanted API
  name: Federal Bureau of Investigation Wanted API
  slug: federal-bureau-of-investigation-wanted-api
artifact_total: 11
collections:
- collection_type: open
  name: FBI Most Wanted List API
  slug: open-federal-bureau-of-investigation-list-api
- collection_type: open
  name: FBI Most Wanted
  slug: open-most-wanted-api
common:
- group: commercial
  href: https://artifacts.apis.io/federal-bureau-of-investigation/plans/federal-bureau-of-investigation-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/federal-bureau-of-investigation-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/federal-bureau-of-investigation/rate-limits/federal-bureau-of-investigation-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/federal-bureau-of-investigation-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/federal-bureau-of-investigation/finops/federal-bureau-of-investigation-finops.yml
  title: ''
  type: FinOps
  url: finops/federal-bureau-of-investigation-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.fbi.gov/news/stories
- group: company
  title: ''
  type: BlogRSS
  url: https://www.fbi.gov/news/stories/RSS
- group: agent
  href: https://artifacts.apis.io/federal-bureau-of-investigation/agentic-access/federal-bureau-of-investigation-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/federal-bureau-of-investigation-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/federal-bureau-of-investigation/security/federal-bureau-of-investigation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/federal-bureau-of-investigation-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fbi-cde
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fbi
- group: company
  title: ''
  type: Website
  url: https://www.fbi.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.fbi.gov/services
created: '2024-10-18'
description: The Federal Bureau of Investigation (FBI) is the domestic intelligence and security service of the United States and its principal federal law enforcement agency. The FBI publishes public APIs covering its Most Wanted program and Uniform Crime Reporting (UCR) data through the Crime Data Explorer.
finops:
- has_sources: false
  method: generated
  name: Federal Bureau Of Investigation Finops
  primary_unit: request
  service_category: API
  slug: federal-bureau-of-investigation-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/federal-bureau-of-investigation.png
layout: provider
modified: '2026-10-06'
name: Federal Bureau of Investigation
nav: Providers
network: true
overview: 'Federal Bureau of Investigation publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Artcrimes API, Wanted API, and 1 more. Tagged areas include FBI and Federal Government.


  The Federal Bureau of Investigation catalog on APIs.io includes 1 Spectral governance ruleset.


  Federal Bureau of Investigation''s developer surface includes engineering blog, documentation, and 9 more developer resources.'
plans:
- name: Federal Bureau Of Investigation Plans Pricing
  plan_count: 3
  slug: federal-bureau-of-investigation-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Federal Bureau Of Investigation Rate Limits
  slug: federal-bureau-of-investigation-rate-limits
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: Federal Bureau of Investigation API Rules
  rule_count: 39
  severity_counts:
    error: 36
    hint: 0
    info: 2
    warn: 1
  slug: federal-bureau-of-investigation-rules
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 42.5
    catalog_earned_first_party: 0.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 45.6
    developer_ergonomics: 21.4
    discoverability: 57.1
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 24.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 50.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/federal-bureau-of-investigation/federal-bureau-of-investigation-2026-06-20T181110.png
security:
- kind: domain-security
  name: Federal Bureau Of Investigation Domain Security
  slug: federal-bureau-of-investigation-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: federal-bureau-of-investigation
tags:
- FBI
- Federal Government
website: https://www.fbi.gov/
---
