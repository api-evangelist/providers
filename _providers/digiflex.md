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
artifact_total: 0
common:
- group: company
  title: ''
  type: InvestorPortfolio
  url: https://www.battery.com/list-of-all-companies/
coverage:
  checked: '2026-08-10'
  detail: Digiflex, Ltd. was an Israeli inkjet computer-to-plate printer manufacturer that PV Nano Cell acquired on 2017-12-03 and absorbed; digiflex.com is still registered but has no working nameservers (SERVFAIL, no A record) and the acquirer's own site no longer mentions the brand.
  evidence:
  - status: 0
    url: https://www.digiflex.com/
  - status: 200
    url: https://pvnanocell.com/
  - status: 200
    url: https://digiflex.io/
  - status: 403
    url: https://digiflex.ai/
  reason: defunct
  state: none
created: '2026-07-17'
description: 'Digiflex (listed by Battery Ventures as "Digiflex, Ltd.") was an Israeli manufacturer of inkjet-based computer-to-plate and digital printing systems, best known for the Flexojet line of flexographic plate-making printers. It was a hardware company: the product was a physical printing press, not software, so it never had a developer program, a public API, or any machine-readable contract to publish. PV Nano Cell signed a $10M all-stock letter of intent in March 2017 and closed the acquisition on 3 December 2017, folding Digiflex in as a wholly-owned subsidiary to carry the Flexojet systems into printed electronics; Battery Ventures now carries the name on its list-of-all-companies page as an exited investment. The brand has since been fully absorbed — the acquirer''s current site (pvnanocell.com, HTTP 200) makes no mention of DigiFlex, and digiflex.com, while still registered through Dynadot to an April 2027 expiry, has no working nameservers and returns SERVFAIL with no A record.
  The live domains sharing the name are unrelated third parties: digiflex.io is a West Midlands web-design agency, digiflex.co.uk is a separate UK business, and digiflex.ai sits behind a Cloudflare bot challenge with no verifiable link to the Battery investment. No developer portal, documentation, OpenAPI, SDK, package-registry presence, or any other API artifact exists for this company. This profile is retained as an honest record of an acquired and absorbed portfolio lead with no API surface rather than being enriched with speculative attribution.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/digiflex.png
layout: provider
modified: '2026-08-10'
name: Digiflex
nav: Providers
network: true
overview: Digiflex is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Venture Backed, Battery Ventures, Portfolio Lead, and Exited.
random_paper: 4
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 1
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
    - middle-east
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
    - owner: catalog
      reason: never_enriched
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/digiflex/refs/heads/main/screenshots/digiflex-2026-07-25T212005.png
slug: digiflex
tags:
- Company
- Venture Backed
- Battery Ventures
- Portfolio Lead
- Exited
- Acquired
- Digital Printing
- Manufacturing
- Israel
---
