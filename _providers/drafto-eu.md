---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/drafto-eu/hosts/drafto-eu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/drafto-eu-hosts.yml
- group: other
  href: https://artifacts.apis.io/drafto-eu/vendors/drafto-eu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/drafto-eu-vendors.yml
- group: auth
  href: https://artifacts.apis.io/drafto-eu/security/drafto-eu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/drafto-eu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://drafto.eu/
- group: operate
  title: ''
  type: Support
  url: https://drafto.eu/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://drafto.eu/privacy
coverage:
  checked: '2026-11-06'
  detail: OpenAPI spec endpoint redirects to login, no machine‑readable contract found.
  evidence:
  - status: 307
    url: https://drafto.eu/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Drafto is a note‑taking app for the web, iPhone, iPad, Android and Mac. It offers notebooks, a rich‑text editor, powerful search, offline sync, Evernote import/export, and integrates with Claude. New accounts are reviewed and approved by hand, emphasizing privacy and quality.
layout: provider
modified: '2026-11-05'
name: Drafto
nav: Providers
network: true
overview: 'Drafto is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Notes, Productivity, Sync, and Privacy.


  Drafto''s developer surface includes support and 5 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Drafto Eu Domain Security
  slug: drafto-eu-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: drafto-eu
tags:
- Company
- Notes
- Productivity
- Sync
- Privacy
website: https://drafto.eu/
---
