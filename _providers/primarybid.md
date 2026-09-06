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
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/sofi-technologies/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/primarybid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://primarybid.com
created: '2026-07-17'
description: PrimaryBid was a UK-based fintech that gave retail investors access to public capital markets — IPOs, follow-on equity raises, and public offerings that were historically restricted to institutional investors. It partnered with exchanges, banks, and issuers to broadcast live capital-raising events to individual investors, powering retail participation in listings such as Deliveroo, PensionBee, and Soho House. PrimaryBid's technology was acquired by SoFi Technologies, Inc. in May 2026; the standalone consumer platform has been wound down and its public website now redirects former shareholders to third-party share registrars. This profile is retained in the API Evangelist network as a historical company record. No public developer portal, API documentation, or machine-readable API surface was found during enrichment.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/primarybid.png
layout: provider
modified: '2026-07-20'
name: PrimaryBid
nav: Providers
network: true
overview: PrimaryBid is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Capital Markets, IPO, and Retail Investing.
random_paper: 4
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
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/primarybid/refs/heads/main/screenshots/primarybid-2026-09-02T152008.png
security:
- kind: domain-security
  name: Primarybid Domain Security
  slug: primarybid-domain-security
  summary_line: TLSv1.2 · DMARC
slug: primarybid
tags:
- Company
- Fintech
- Capital Markets
- IPO
- Retail Investing
- Investing
- United Kingdom
website: https://primarybid.com
---
