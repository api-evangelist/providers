---
access_model:
  confidence: low
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
api_count: 0
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/bakeryos-io/well-known/bakeryos-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bakeryos-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/bakeryos-io/hosts/bakeryos-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bakeryos-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/bakeryos-io/vendors/bakeryos-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bakeryos-io-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bakeryos-io/security/bakeryos-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bakeryos-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bakeryos.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bakeryos.io/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bakeryos.io/terms
coverage:
  checked: '2026-11-02'
  detail: MCP endpoint https://app.bakeryos.io/mcp returns 401 Unauthorized, indicating the API is behind authentication.
  evidence:
  - status: 401
    url: https://app.bakeryos.io/mcp
  reason: auth-required
  state: gated
created: '2026-11-02'
description: 'L’app conçue par un boulanger pour tenir ta boulangerie : recettes au gramme, coût matière et marge toujours à jour, planning, heures de l’équipe et assistant IA, même sans réseau. Gratuite pendant le lancement.'
image: https://bakeryos.io/og-image.png
layout: provider
modified: '2026-11-02'
name: BakeryOS
nav: Providers
network: true
overview: BakeryOS is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Bakery, Management, Software-as-a-Service, Mobile, and French.
plans:
- name: Bakeryos Io Plans Pricing
  plan_count: 0
  slug: bakeryos-io-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Bakeryos Io Rate Limits
  slug: bakeryos-io-rate-limits
scopes:
- name: Bakeryos Io Scopes
  scope_count: 0
  slug: bakeryos-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 11.2
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bakeryos Io Authentication
  slug: bakeryos-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Bakeryos Io Domain Security
  slug: bakeryos-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bakeryos-io
tags:
- Bakery
- Management
- Software-as-a-Service
- Mobile
- French
website: https://bakeryos.io/
---
