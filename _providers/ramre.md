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
  url: security/ramre-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aoreltd.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aoreltd.com/terms-and-conditions-of-use
created: '2026-07-17'
description: 'Ramre (RamRe) is the brand associated with Ram Reinsurance, now operating as American Overseas Group Limited (AOG) — a Bermuda-based insurance holding company that is tax resident in the United Kingdom. Through its U.S. subsidiaries the group writes non-standard automobile insurance and provides related management services, and it operates as a reinsurer through a subsidiary based in Barbados. The company was surfaced as a portfolio company of Canaan Partners and added to the API Evangelist network as a stub for enrichment. An enrichment pass found no public developer program, API, documentation, or SDK surface: this is a financial-services holding company whose public web presence (ramre.com now redirects to aoreltd.com) is corporate and investor-relations oriented, with no machine-readable API artifacts to catalog.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ramre.png
layout: provider
modified: '2026-07-20'
name: Ramre
nav: Providers
network: true
overview: Ramre is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Reinsurance, Financial-Services, and Auto Insurance.
random_paper: 10
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 15.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ramre/refs/heads/main/screenshots/ramre-2026-09-02T152837.png
security:
- kind: domain-security
  name: Ramre Domain Security
  slug: ramre-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ramre
tags:
- Company
- Insurance
- Reinsurance
- Financial-Services
- Auto Insurance
- Bermuda
website: https://aoreltd.com/
---
