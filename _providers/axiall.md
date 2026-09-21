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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-20'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axiall/refs/heads/main/security/axiall-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/axiall-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/axiall-corporation
- group: other
  title: ''
  type: Successor
  url: https://www.westlake.com
coverage:
  checked: '2026-09-18'
  detail: Axiall was absorbed into Westlake Chemical on 2016-08-31; www.axiall.com and axiall.com resolve to 34.199.101.188 but nothing listens on 80 or 443 (every probe timed out, TCP connect refused), so there is no site, no docs and no contract to read.
  evidence:
  - status: 0
    url: https://www.axiall.com
  - status: 0
    url: https://axiall.com
  - status: 0
    url: https://www.axiall.com/.well-known/agent-card.json
  - status: 200
    url: https://www.westlake.com/westlake-chemical-completes-acquisition-axiall-corporation
  - status: 200
    url: https://www.linkedin.com/company/axiall-corporation
  reason: defunct
  state: none
created: '2026-03-23'
description: Axiall Corporation was a manufacturer and international marketer of chemicals and building products, including chlorovinyls (chlor-alkali, PVC resin and vinyl compounds) and aromatics, for use in industrial and consumer applications. Westlake Chemical completed its acquisition of Axiall on 2016-08-31 and the Axiall brand and website have been absorbed into Westlake; the company published no developer program or API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/axiall.png
layout: provider
modified: '2026-09-18'
name: Axiall
nav: Providers
network: true
overview: Axiall is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Chemicals, Manufacturing, Building Products, Chlor-Alkali, and PVC.
press:
- date: ''
  title: PPG and Georgia Gulf merger complete - Lake Charles
  url: https://www.kplctv.com/story/20718704/ppg-georgia-gulf-merger-nearly-complete/
- date: ''
  title: Axiall, Lotte Announce $3 Billion In Louisiana Chemical ...
  url: https://www.opportunitylouisiana.gov/news/axiall-lotte-announce-3-billion-in-louisiana-chemical-projects
- date: ''
  title: Axiall Corporation Adds Three Directors to Board | MarketScreener
  url: https://www.marketscreener.com/news/latest/Axiall-Corporation-Adds-Three-Directors-to-Board-15977336/
- date: ''
  title: 'Update: Chlorine leak at Proctor chemical plant investigated'
  url: https://www.wtap.com/content/news/Axiall-releases-statement-Chlorine-leak-sends-two-people-to-hospital--391494151.html
- date: ''
  title: Westlake Acquires Epoxy Business | News
  url: https://www.clearygottlieb.com/news-and-insights/news-listing/westlakes-acquisition-of-hexions-global-epoxy-business
random_paper: 19
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 5.0
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Axiall Domain Security
  slug: axiall-domain-security
  summary_line: DMARC
slug: axiall
tags:
- Chemicals
- Manufacturing
- Building Products
- Chlor-Alkali
- PVC
- Vinyls
- Defunct
- Acquired
---
