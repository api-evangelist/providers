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
    agent_card: conformant
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
  score: 8.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Dre1mery is real-estate deal software for US property investors and their AI agents that finds properties, underwrites deals and runs offers, contracts and outreach, in one web app and one MCP server.
  name: Dre1mery API
  slug: dre1mery-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/dre1mery-com/llms/dre1mery-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dre1mery-com-llms.txt
- group: other
  href: https://artifacts.apis.io/dre1mery-com/a2a/dre1mery-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/dre1mery-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/dre1mery-com/well-known/dre1mery-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dre1mery-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dre1mery-com/hosts/dre1mery-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dre1mery-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dre1mery-com/vendors/dre1mery-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dre1mery-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.dre1mery.com/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dre1mery.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dre1mery.com/privacy
- group: start
  title: ''
  type: Login
  url: https://www.dre1mery.com/auth/signin
- group: company
  title: ''
  type: Blog
  url: https://www.dre1mery.com/blog
- group: auth
  href: https://artifacts.apis.io/dre1mery-com/security/dre1mery-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dre1mery-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dre1mery.com/
coverage:
  checked: '2026-11-06'
  detail: Provider docs are rendered via JavaScript and no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://www.dre1mery.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: Dre1mery is an AI-powered real‑estate investment platform offering off‑market deal sourcing, automated underwriting, creative financing, and acquisition tools for US property investors. The web app provides a single MCP server for analysis, modeling, and outreach, with integrated AI agents to streamline the investment workflow.
image: https://www.dre1mery.com/og-image.png
layout: provider
modified: '2026-11-05'
name: Dre1mery
nav: Providers
network: true
overview: 'Dre1mery is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Artificial Intelligence, Investment, Property, and Platform.


  Dre1mery''s developer surface includes engineering blog and 11 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dre1Mery Com Domain Security
  slug: dre1mery-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dre1mery-com
tags:
- Real Estate
- Artificial Intelligence
- Investment
- Property
- Platform
website: https://www.dre1mery.com/
---
