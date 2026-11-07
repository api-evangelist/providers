---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - security
  trial: false
  try_now: true
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public API for creating shareable AI‑generated content links.
  name: Bauta API
  slug: bauta-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/bauta-app/plans/bauta-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bauta-app-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/bauta-app/llms/bauta-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bauta-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/bauta-app/well-known/bauta-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bauta-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/bauta-app/hosts/bauta-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bauta-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/bauta-app/vendors/bauta-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bauta-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bauta.app/terms
- group: start
  title: ''
  type: SignUp
  url: https://bauta.app/signup
- group: auth
  title: ''
  type: Security
  url: https://bauta.app/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bauta.app/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://bauta.app/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://bauta.app/docs
- group: company
  title: ''
  type: Blog
  url: https://bauta.app/blog/
- group: auth
  href: https://artifacts.apis.io/bauta-app/security/bauta-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bauta-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bauta.app/
coverage:
  checked: '2026-11-02'
  detail: Documentation is public but provides no machine‑readable OpenAPI, GraphQL, or other contract.
  evidence:
  - status: 200
    url: https://bauta.app/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Bauta enables users to instantly share AI‑generated content—presentations, reports, dashboards, or mini‑apps—from tools like Claude, ChatGPT, Cursor, Windsurf, Cowork, or Codex as real, permanent web links. No account, no setup, and no login required. The service creates a shareable page in seconds, turning AI output into a link that can be embedded anywhere.
image: https://bauta.app/og.png
layout: provider
modified: '2026-11-02'
name: Bauta
nav: Providers
network: true
overview: 'Bauta is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Sharing, NoLogin, Web Links, and Productivity.


  Bauta''s developer surface includes signup flow, pricing, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Bauta App Plans Pricing
  plan_count: 5
  slug: bauta-app-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 18.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bauta App Domain Security
  slug: bauta-app-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bauta-app
tags:
- Artificial Intelligence
- Sharing
- NoLogin
- Web Links
- Productivity
website: https://bauta.app/
---
