---
access_model:
  confidence: low
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Premier Inc runs an API gateway host at api.premierinc.com that answers 503 to anonymous requests; no public developer portal, documentation or contract is published (developer.premierinc.com does not
  name: Premier Inc API
  slug: premier-inc-api
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/premier-inc/hosts/premier-inc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/premier-inc-hosts.yml
- group: other
  href: https://artifacts.apis.io/premier-inc/vendors/premier-inc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/premier-inc-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://premierinc.com/leadership
- group: commercial
  href: https://artifacts.apis.io/premier-inc/plans/premier-inc-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/premier-inc-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/premier-inc/rate-limits/premier-inc-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/premier-inc-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/premier-inc/finops/premier-inc-finops.yml
  title: ''
  type: FinOps
  url: finops/premier-inc-finops.yml
- group: auth
  href: https://artifacts.apis.io/premier-inc/security/premier-inc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/premier-inc-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PremierInc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/premierinc
- group: company
  title: ''
  type: Website
  url: https://premierinc.com
- group: company
  title: ''
  type: Blog
  url: https://premierinc.com/feed.xml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://premierinc.com/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://premierinc.com/terms-conditions
- group: company
  title: ''
  type: Newsroom
  url: https://premierinc.com/newsroom
coverage:
  checked: '2026-10-20'
  detail: premierinc.com links no developer or API pages, developer.premierinc.com does not resolve, the PremierInc GitHub org has no public repos, and api.premierinc.com answers 503 to every anonymous path.
  evidence:
  - status: 503
    url: https://api.premierinc.com/openapi.json
  - status: 200
    url: https://premierinc.com/
  - status: 200
    url: https://github.com/PremierInc
  reason: no-developer-program
  state: none
created: '2026-04-19'
description: 'Premier Inc (NASDAQ: PINC) is a US healthcare improvement company that operates one of the largest group purchasing organizations and the PINC AI technology and services platform for clinical intelligence, margin improvement and value-based care, built on cost, quality and operational data from US hospital discharges. It publishes no public developer program.'
finops:
- has_sources: true
  method: generated
  name: Premier Inc Finops
  primary_unit: ''
  service_category: Healthcare
  slug: premier-inc-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/premier-inc.png
layout: provider
modified: '2026-10-20'
name: Premier Inc
nav: Providers
network: true
overview: 'Premier Inc is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Group Purchasing, Analytics, Supply Chain, and Value-Based Care.


  Premier Inc''s developer surface includes engineering blog and 13 more developer resources.'
plans:
- name: Premier Inc Plans Pricing
  plan_count: 1
  slug: premier-inc-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Premier Inc Rate Limits
  slug: premier-inc-rate-limits
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 67.9
    operational_transparency: 7.9
  previous_composite: 13.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/premier-inc/premier-inc-2026-06-20T192047.png
security:
- kind: domain-security
  name: Premier Inc Domain Security
  slug: premier-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: premier-inc
tags:
- Healthcare
- Group Purchasing
- Analytics
- Supply Chain
- Value-Based Care
website: https://premierinc.com
---
