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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/dokladbot-cz/llms/dokladbot-cz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dokladbot-cz-llms.txt
- group: agent
  href: https://artifacts.apis.io/dokladbot-cz/well-known/dokladbot-cz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dokladbot-cz-well-known.yml
- group: other
  href: https://artifacts.apis.io/dokladbot-cz/hosts/dokladbot-cz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dokladbot-cz-hosts.yml
- group: other
  href: https://artifacts.apis.io/dokladbot-cz/vendors/dokladbot-cz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dokladbot-cz-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://dokladbot.cz/blog
- group: auth
  href: https://artifacts.apis.io/dokladbot-cz/security/dokladbot-cz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dokladbot-cz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dokladbot.cz/
coverage:
  checked: '2026-11-05'
  detail: No public API documentation or machine-readable contract was found on the provider's hosts.
  evidence:
  - status: 404
    url: https://dokladbot.cz/api/openapi.json
  reason: tenant-only
  state: none
created: '2026-11-05'
description: DokladBot provides automated accounting via WhatsApp for self‑employed individuals and small businesses in the Czech Republic. It captures receipts, generates invoices with QR codes, handles VAT, manages inventory, payroll, and exports data to popular accounting software such as Pohoda, Money S3, and ABRA Flexi. Pricing starts at 199 CZK per month without VAT.
image: https://dokladbot.cz/opengraph-image.png
layout: provider
modified: '2026-11-05'
name: DokladBot
nav: Providers
network: true
overview: 'DokladBot is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Accounting, Automation, Czech Republic, Small Business, and WhatsApp.


  DokladBot''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 4.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dokladbot Cz Domain Security
  slug: dokladbot-cz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dokladbot-cz
tags:
- Accounting
- Automation
- Czech Republic
- Small Business
- WhatsApp
website: https://dokladbot.cz/
---
