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
  url: security/minted-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://minted.com
- group: operate
  title: ''
  type: Support
  url: https://help.minted.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/minted
created: '2026-07-17'
description: Minted is a San Francisco-based online design marketplace that crowdsources graphic and fine-art designs from a global community of independent artists and sells the winning work as stationery, wedding invitations, holiday cards, art prints, home decor, and personalized gifts. Its e-commerce storefront at minted.com pairs artist-submitted designs with in-house printing and fulfillment. This profile was surfaced as a portfolio company of Norwest Venture Partners and Slow Ventures and added to the API Evangelist network; the enrichment pass probed for any public developer surface and found no documented public API — Minted operates as a direct-to-consumer commerce brand, not an API provider.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/minted.png
layout: provider
modified: '2026-07-20'
name: Minted
nav: Providers
network: true
overview: 'Minted is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Marketplace, Stationery, and Design.


  Minted''s developer surface includes support and 3 more developer resources.'
random_paper: 11
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
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 5.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/minted/refs/heads/main/screenshots/minted-2026-08-07T173002.png
security:
- kind: domain-security
  name: Minted Domain Security
  slug: minted-domain-security
  summary_line: TLSv1.3 · DMARC
slug: minted
tags:
- Company
- E-Commerce
- Marketplace
- Stationery
- Design
- Consumer
- Retail
website: https://minted.com
---
