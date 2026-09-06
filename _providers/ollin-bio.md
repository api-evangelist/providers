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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ollin-bio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ollin.bio/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ollin.bio/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ollin.bio/terms-of-use/
created: '2026-07-17'
description: Ollin Bio is a privately held biotechnology company developing novel therapeutics, organizing its work around defined therapeutic areas and a product pipeline of drug candidates in development. Backed by a16z, the company was added to the API Evangelist network as a portfolio-company lead. As a research-stage therapeutics company, Ollin Bio publishes a marketing and corporate website but does not expose a public developer program, API, documentation, or SDKs at this time. This profile records the company's public identity and web properties; it will be re-enriched if a public API surface ever appears.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ollin-bio.png
layout: provider
modified: '2026-07-20'
name: Ollin Bio
nav: Providers
network: true
overview: Ollin Bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Therapeutics, Life Sciences, and Drug Development.
random_paper: 19
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ollin-bio/refs/heads/main/screenshots/ollin-bio-2026-08-07T190132.png
security:
- kind: domain-security
  name: Ollin Bio Domain Security
  slug: ollin-bio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ollin-bio
tags:
- Company
- Biotechnology
- Therapeutics
- Life Sciences
- Drug Development
- Pharmaceuticals
- a16z Portfolio
website: https://ollin.bio/
---
