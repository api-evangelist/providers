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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Acutis Go fleet management
  name: Acutis Go API
  slug: acutis-go-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/acutisgo-com/llms/acutisgo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/acutisgo-com-llms.txt
- group: other
  href: https://artifacts.apis.io/acutisgo-com/hosts/acutisgo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/acutisgo-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://acutisgo.com/terms.html
- group: start
  title: ''
  type: SignUp
  url: https://app.acutisgo.com/signup?product=go
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://acutisgo.com/privacy.html
- group: docs
  title: ''
  type: Documentation
  url: https://help.acutisgo.com/
- group: auth
  href: https://artifacts.apis.io/acutisgo-com/security/acutisgo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/acutisgo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://acutisgo.com/
created: '2026-10-31'
description: Acutis Go provides an endpoint agent that continuously monitors network and machine health on laptops and other devices. It runs as a lightweight 7 MB Go binary, observing network path, Wi‑Fi, drivers, certificates, and system health every 60 seconds, delivering plain‑English verdicts to help desks without requiring admin rights or remote access. The service is free, observe‑only, and integrates with a web dashboard for fleet management.
image: https://acutisgo.com/og-image.png
layout: provider
modified: '2026-10-31'
name: Acutis Go
nav: Providers
network: true
overview: 'Acutis Go is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Networks, Agents, Observability, and Free.


  Acutis Go''s developer surface includes signup flow, documentation, and 6 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 14.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Acutisgo Com Domain Security
  slug: acutisgo-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: acutisgo-com
tags:
- Company
- Networks
- Agents
- Observability
- Free
- Dashboards
website: https://acutisgo.com/
---
