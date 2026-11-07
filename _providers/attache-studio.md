---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - plans
  - authentication
  - rate-limits
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
- description: MCP connector for agencies providing GA4, Google Ads, Search Console and Meta Ads via Claude.
  name: Attaché API
  slug: attach-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/attache-studio/plans/attache-studio-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/attache-studio-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/attache-studio/llms/attache-studio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/attache-studio-llms.txt
- group: agent
  href: https://artifacts.apis.io/attache-studio/well-known/attache-studio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/attache-studio-well-known.yml
- group: other
  href: https://artifacts.apis.io/attache-studio/hosts/attache-studio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/attache-studio-hosts.yml
- group: other
  href: https://artifacts.apis.io/attache-studio/vendors/attache-studio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/attache-studio-vendors.yml
- group: auth
  href: https://artifacts.apis.io/attache-studio/security/attache-studio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/attache-studio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://attache.studio/
- group: company
  title: ''
  type: Blog
  url: https://attache.studio/blog
coverage:
  checked: '2026-11-02'
  detail: Public marketing pages describe the MCP connector but no machine‑readable API spec is published.
  evidence:
  - status: 404
    url: https://attache.studio/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Connecteur Claude pour GA4, Google Ads & Search Console — multi-clients | Attaché Attaché Early access Comment ça marche Tarifs Sécurité Blog Se connecter Créer mon espace — gratuit Comment ça marche Tarifs Sécurité Blog Se connecter Vos données marketing dans Claude — en 3 minutes GA4, Google Ads e
layout: provider
modified: '2026-11-02'
name: Attaché
nav: Providers
network: true
overview: 'Attaché is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Marketing, Analytics, Google, Claude, and Software-as-a-Service.


  Attaché''s developer surface includes engineering blog and 7 more developer resources.'
plans:
- name: Attache Studio Plans Pricing
  plan_count: 1
  slug: attache-studio-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Attache Studio Rate Limits
  slug: attache-studio-rate-limits
scopes:
- name: Attache Studio Scopes
  scope_count: 0
  slug: attache-studio-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 38.0
    catalog_earned_first_party: 8.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 11.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Attache Studio Authentication
  slug: attache-studio-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Attache Studio Domain Security
  slug: attache-studio-domain-security
  summary_line: TLSv1.3
slug: attache-studio
tags:
- Marketing
- Analytics
- Google
- Claude
- Software-as-a-Service
- Multi-Client
website: https://attache.studio/
---
