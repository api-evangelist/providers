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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Connects Fortnox accounting software with AI assistants via MCP; documentation is gated behind authentication.
  name: Novus MCP API
  slug: novus-mcp-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/novusmcp-se/llms/novusmcp-se-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/novusmcp-se-llms.txt
- group: agent
  href: https://artifacts.apis.io/novusmcp-se/well-known/novusmcp-se-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/novusmcp-se-well-known.yml
- group: other
  href: https://artifacts.apis.io/novusmcp-se/hosts/novusmcp-se-hosts.yml
  title: ''
  type: Hosts
  url: hosts/novusmcp-se-hosts.yml
- group: auth
  href: https://artifacts.apis.io/novusmcp-se/security/novusmcp-se-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/novusmcp-se-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://novusmcp.se/
- group: docs
  title: ''
  type: Documentation
  url: https://novusmcp.se/guider
- group: start
  title: ''
  type: DeveloperPortal
  url: https://byra.novusmcp.se
- group: start
  title: ''
  type: GettingStarted
  url: https://novusmcp.se/fortnox-mcp
- group: operate
  title: ''
  type: Support
  url: https://novusmcp.se/kontakt
- group: commercial
  title: ''
  type: Pricing
  url: https://novusmcp.se/konto
- group: commercial
  title: ''
  type: TermsOfService
  url: https://novusmcp.se/villkor
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://novusmcp.se/integritetspolicy
coverage:
  checked: '2026-10-30'
  detail: MCP documentation is gated behind authentication requiring login.
  evidence:
  - status: 401
    url: https://novusmcp.se/mcp
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Novus MCP connects Fortnox accounting software with AI assistants like ChatGPT and Claude, enabling businesses to query their bookkeeping data via conversational interfaces. Operated by AMR Intelligence Sweden AB, the service emphasizes secure data handling, GDPR compliance, and flexible AI integration, offering a 30‑day open‑return policy and agency‑level support for agencies and enterprises.
image: https://novusmcp.se/assets/novus-card.png
layout: provider
modified: '2026-10-30'
name: novusmcp-se
nav: Providers
network: true
overview: 'novusmcp-se is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Accounting, Artificial Intelligence, Integration, and Fortnox.


  novusmcp-se''s developer surface includes documentation, getting-started guide, support, pricing, and 8 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.3
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 64.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 20.4
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/novusmcp-se/novusmcp-se-2026-11-03T140326.png
security:
- kind: domain-security
  name: Novusmcp Se Domain Security
  slug: novusmcp-se-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: novusmcp-se
tags:
- Company
- Accounting
- Artificial Intelligence
- Integration
- Fortnox
- Sweden
website: https://novusmcp.se/
---
