---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''http://www.ebureau.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.transunion.com/solution/advanced-analytics — a different registrable domain (ebureau.com -> transunion.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/ebureau-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.ebureau.com/
created: '2026-07-17'
description: eBureau was a predictive analytics and big-data scoring company founded in 2004 and headquartered in St. Cloud, Minnesota, providing real-time predictive scores, identity verification, and fraud-prevention products (eScore, eIDverifier, eIDcompare) to lenders, insurers, and marketers. eBureau was acquired by TransUnion in December 2015 and its capabilities were absorbed into TransUnion's fraud and identity solutions; the ebureau.com domain remains live (behind Cloudflare) but exposes no independent public developer portal, API reference, or machine-readable API specification. This API Evangelist profile was surfaced as a portfolio company of Redpoint Ventures and enriched with a live domain-security probe.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ebureau.png
layout: provider
modified: '2026-07-18'
name: eBureau
nav: Providers
network: true
overview: eBureau is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Predictive Analytics, Identity Verification, Fraud Prevention, and Credit Risk.
random_paper: 10
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ebureau/refs/heads/main/screenshots/ebureau-2026-07-25T212732.png
security:
- kind: domain-security
  name: Ebureau Domain Security
  slug: ebureau-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ebureau
tags:
- Company
- Predictive Analytics
- Identity Verification
- Fraud Prevention
- Credit Risk
- Data
- Acquired
website: http://www.ebureau.com/
---
