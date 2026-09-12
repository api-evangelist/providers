---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/federal-mine-safety-and-health-review-commission-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/federal-mine-safety-and-health-review-commission-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.fmshrc.gov/content/vulnerability-disclosure-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/federal-mine-safety-and-health-review-commission-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/federal-mine-safety-and-health-review-commission
- group: company
  title: ''
  type: Website
  url: https://www.fmshrc.gov/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fmshrc.gov/content/fmshrc-privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.fmshrc.gov/content/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.fmshrc.gov/about/news
coverage:
  checked: '2026-09-09'
  detail: FMSHRC runs a Drupal 10 site with JSON:API and REST disabled — /jsonapi, /api, /rest, /graphql, /data.json and /openapi.json all return 404 and a node requested with ?_format=json returns HTTP 406 — and its only transactional surface, the e-CMS at fmshrc-ecms.entellitrak.com, is a vendor-hosted login form, so the agency publishes decisions as HTML and PDF and no programmable interface at all.
  evidence:
  - status: 404
    url: https://www.fmshrc.gov/jsonapi
  - status: 406
    url: https://www.fmshrc.gov/node/5513050?_format=json
  - status: 404
    url: https://www.fmshrc.gov/openapi.json
  - status: 404
    url: https://www.fmshrc.gov/.well-known/api-catalog
  - status: 404
    url: https://fmshrc-ecms.entellitrak.com/openapi.json
  reason: no-developer-program
  state: none
created: '2024-12-03'
description: The Federal Mine Safety and Health Review Commission (FMSHRC) is an independent United States adjudicative agency that provides administrative trial and appellate review of legal disputes arising under the Federal Mine Safety and Health Amendments Act of 1977 (the Mine Act). Its administrative law judges and its five-member Commission hear contests of the citations, orders and civil penalties issued by the Department of Labor's Mine Safety and Health Administration, along with miner discrimination complaints under section 105(c). FMSHRC does not regulate mining or enforce the Mine Act. It publishes decisions, dockets and Blue Book volumes as HTML and PDF on fmshrc.gov and runs a vendor-hosted electronic case management system for filing, but exposes no public API, developer program or machine-readable contract.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/federal-mine-safety-and-health-review-commission.png
layout: provider
modified: '2026-09-09'
name: Federal Mine Safety and Health Review Commission
nav: Providers
network: true
overview: 'Federal Mine Safety and Health Review Commission is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Federal-Government, Mine Safety, Adjudication, Occupational-Safety, and Legal.


  Federal Mine Safety and Health Review Commission''s developer surface includes support, engineering blog, and 7 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    operational_transparency: 10.5
  previous_composite: 11.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 29.6
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/federal-mine-safety-and-health-review-commission/refs/heads/main/screenshots/federal-mine-safety-and-health-review-commission-2026-06-20T181121.png
security:
- kind: domain-security
  name: Federal Mine Safety And Health Review Commission Domain Security
  slug: federal-mine-safety-and-health-review-commission-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Federal Mine Safety And Health Review Commission Vulnerability Disclosure
  slug: federal-mine-safety-and-health-review-commission-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: federal-mine-safety-and-health-review-commission
tags:
- Federal-Government
- Mine Safety
- Adjudication
- Occupational-Safety
- Legal
- Regulatory-Enforcement
website: https://www.fmshrc.gov/
---
