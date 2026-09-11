---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-10'
api_count: 1
apis:
- description: The Federal Labor Relations Authority administers federal labor-management relations law.
  name: Federal Labor Relations Authority
  slug: federal-labor-relations-authority
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/federal-labor-relations-authority-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/federal-labor-relations-authority
- group: company
  title: ''
  type: Website
  url: https://www.flra.gov/
- group: company
  title: ''
  type: Blog
  url: https://www.flra.gov/rss.xml
- group: operate
  title: ''
  type: Support
  url: https://www.flra.gov/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flra.gov/privacy
- group: commercial
  title: ''
  type: Plans
  url: plans/federal-labor-relations-authority-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/federal-labor-relations-authority-llms.txt
coverage:
  checked: '2026-09-09'
  detail: The FLRA runs a Drupal website with an eFiling flow and an eLibrary case-document search for end users, but no developer program of any kind — /api, /api-docs, /developers, /developer, /jsonapi, /graphql, /openapi.json, /swagger.json and every named /.well-known/ path all return the Drupal 404 page, api.flra.gov / data.flra.gov / developer.flra.gov do not resolve in DNS, and the agency's own Open Government page says its data is still "in the process" of being submitted to data.gov, so the only machine-readable output it publishes is seven RSS feeds.
  evidence:
  - status: 404
    url: https://www.flra.gov/openapi.json
  - status: 404
    url: https://www.flra.gov/api-docs
  - status: 404
    url: https://www.flra.gov/developers
  - status: 404
    url: https://www.flra.gov/jsonapi
  - status: 404
    url: https://www.flra.gov/.well-known/api-catalog
  - status: 200
    url: https://www.flra.gov/open-government
  - status: 200
    url: https://www.flra.gov/rss.xml
  reason: no-developer-program
  state: none
created: '2024-12-03'
description: The Federal Labor Relations Authority oversees the Federal service labor-management relations program. It administers the law that protects the right of employees of the Federal Government to organize, bargain collectively, and participate through labor organizations of their own choosing in decisions affecting them.
finops:
- name: Federal Labor Relations Authority Finops
  service_category: API
  slug: federal-labor-relations-authority-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/federal-labor-relations-authority.png
layout: provider
modified: '2026-09-09'
name: Federal Labor Relations Authority
nav: Providers
network: true
overview: 'Federal Labor Relations Authority publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Federal-Government, Labor, Labor-Relations, Collective-Bargaining, and Public-Sector.


  Federal Labor Relations Authority''s developer surface includes engineering blog, support, and 6 more developer resources.'
plans:
- name: Federal Labor Relations Authority Plans Pricing
  plan_count: 0
  slug: federal-labor-relations-authority-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Federal Labor Relations Authority Rate Limits
  slug: federal-labor-relations-authority-rate-limits
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.4
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 18.5
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/federal-labor-relations-authority/refs/heads/main/screenshots/federal-labor-relations-authority-2026-07-25T214321.png
security:
- kind: domain-security
  name: Federal Labor Relations Authority Domain Security
  slug: federal-labor-relations-authority-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: federal-labor-relations-authority
tags:
- Federal-Government
- Labor
- Labor-Relations
- Collective-Bargaining
- Public-Sector
- Government
- Legal
website: https://www.flra.gov/
---
