---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API reference for BacklinksWinkel, accessible via the website but requires login.
  name: BacklinksWinkel API
  slug: backlinkswinkel-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/backlinkswinkel-nl/llms/backlinkswinkel-nl-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/backlinkswinkel-nl-llms.txt
- group: agent
  href: https://artifacts.apis.io/backlinkswinkel-nl/well-known/backlinkswinkel-nl-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/backlinkswinkel-nl-well-known.yml
- group: other
  href: https://artifacts.apis.io/backlinkswinkel-nl/hosts/backlinkswinkel-nl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/backlinkswinkel-nl-hosts.yml
- group: other
  href: https://artifacts.apis.io/backlinkswinkel-nl/vendors/backlinkswinkel-nl-vendors.yml
  title: ''
  type: Vendors
  url: vendors/backlinkswinkel-nl-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://backlinkswinkel.nl/privacy/
- group: start
  title: ''
  type: Login
  url: https://backlinkswinkel.nl/accounts/login/?next=/catalogus/
- group: auth
  href: https://artifacts.apis.io/backlinkswinkel-nl/security/backlinkswinkel-nl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/backlinkswinkel-nl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://backlinkswinkel.nl/
- group: company
  title: ''
  type: Blog
  url: https://backlinkswinkel.nl/blog/
coverage:
  checked: '2026-11-02'
  detail: API reference page redirects to a login page requiring authentication.
  evidence:
  - status: 302
    url: https://backlinkswinkel.nl/api
  reason: auth-required
  state: gated
created: '2026-11-02'
description: BacklinksWinkel is a Dutch link‑building service offering a catalog of real Dutch websites for backlink acquisition. Customers can select individual backlinks or fixed packages starting at €249, with transparent domain rating (DR) and pricing displayed upfront. The platform provides white‑label options, detailed reporting, and SEO expertise to improve search rankings. Operated in the Netherlands, the company focuses on quality backlinks from sites with established metrics.
image: https://backlinkswinkel.nl/static/images/og-image.jpg
layout: provider
modified: '2026-11-02'
name: BacklinksWinkel
nav: Providers
network: true
overview: 'BacklinksWinkel is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include SEO, Link Building, Backlinks, Dutch, and Marketing.


  BacklinksWinkel''s developer surface includes engineering blog and 8 more developer resources.'
plans:
- name: Backlinkswinkel Nl Plans Pricing
  plan_count: 0
  slug: backlinkswinkel-nl-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Backlinkswinkel Nl Rate Limits
  slug: backlinkswinkel-nl-rate-limits
scopes:
- name: Backlinkswinkel Nl Scopes
  scope_count: 0
  slug: backlinkswinkel-nl-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 12.5
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Backlinkswinkel Nl Authentication
  slug: backlinkswinkel-nl-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Backlinkswinkel Nl Domain Security
  slug: backlinkswinkel-nl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: backlinkswinkel-nl
tags:
- SEO
- Link Building
- Backlinks
- Dutch
- Marketing
website: https://backlinkswinkel.nl/
---
