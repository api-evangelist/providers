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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: A permanent festival of art and photography books, limited editions and prints, directly from independent publishers and self‑published artists worldwide.
  name: Artbook Society API
  slug: artbook-society-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/artbooksociety-com/llms/artbooksociety-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/artbooksociety-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/artbooksociety-com/well-known/artbooksociety-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/artbooksociety-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/artbooksociety-com/hosts/artbooksociety-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/artbooksociety-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/artbooksociety-com/security/artbooksociety-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/artbooksociety-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.artbooksociety.com/
- group: company
  title: ''
  type: Blog
  url: https://www.artbooksociety.com/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.artbooksociety.com/en/legal/tariffs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.artbooksociety.com/en/legal/cguv
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.artbooksociety.com/en/legal/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.artbooksociety.com/en/contact
- group: operate
  title: ''
  type: Roadmap
  url: https://www.artbooksociety.com/en/roadmap
coverage:
  checked: '2026-11-02'
  detail: The only API endpoint discovered is a POST-only /mcp, which cannot be accessed via GET, preventing contract retrieval.
  evidence:
  - status: 405
    url: https://www.artbooksociety.com/mcp
  reason: auth-required
  state: gated
created: '2026-11-01'
description: Artbook Society is an international platform for art publishing, offering a permanent festival of art and photography books, limited editions and prints directly from independent publishers and self‑published artists worldwide. It connects artists, publishers, and collectors, fostering a global community of art enthusiasts.
image: https://cdn.artbooksociety.com/images/seo/og-default.jpg
layout: provider
modified: '2026-11-01'
name: Artbook Society
nav: Providers
network: true
overview: 'Artbook Society is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Art, Publishing, Books, Photography, and Marketplace.


  Artbook Society''s developer surface includes engineering blog, pricing, support, and 8 more developer resources.'
random_paper: 14
rate_limits:
- limit_count: 0
  name: Artbooksociety Com Rate Limits
  slug: artbooksociety-com-rate-limits
scopes:
- name: Artbooksociety Com Scopes
  scope_count: 0
  slug: artbooksociety-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 57.1
    operational_transparency: 2.6
  previous_composite: 15.4
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Artbooksociety Com Authentication
  slug: artbooksociety-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Artbooksociety Com Domain Security
  slug: artbooksociety-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: artbooksociety-com
tags:
- Art
- Publishing
- Books
- Photography
- Marketplace
website: https://www.artbooksociety.com/
---
