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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/atalay-ai/llms/atalay-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atalay-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/atalay-ai/well-known/atalay-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/atalay-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/atalay-ai/hosts/atalay-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atalay-ai-hosts.yml
- group: auth
  href: https://artifacts.apis.io/atalay-ai/security/atalay-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atalay-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atalay.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://atalay.ai/gelistiriciler
- group: company
  title: ''
  type: Blog
  url: https://atalay.ai/blog
- group: operate
  title: ''
  type: Support
  url: mailto:destek@atalay.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.atalay.ai/kullanim-kosullari
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.atalay.ai/gizlilik-politikasi
- group: start
  title: ''
  type: SignUp
  url: https://app.atalay.ai/giris
coverage:
  checked: '2026-11-02'
  detail: Developer portal pages are JavaScript-rendered SPA, providing no machine-readable spec.
  evidence:
  - status: 200
    url: https://atalay.ai/gelistiriciler
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: Müşteri mesajını, teklifi, paylaşımı ve muhasebeyi yapay zekâ çalışanların hazırlar, onay sende kalır. Web sitesi, e-ticaret, e-Fatura aynı yerde. İşletmenizin Yapay Zekası. Mesajı, paylaşımı, teklifi ve muhasebeyi yapay zekâ çalışanları hazırlar; son söz senin.
image: https://atalay.ai/logo.png
layout: provider
modified: '2026-11-01'
name: Atalay AI
nav: Providers
network: true
overview: 'Atalay AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Automation, Business, Software-as-a-Service, and Turkish.


  Atalay AI''s developer surface includes engineering blog, support, signup flow, and 8 more developer resources.'
random_paper: 19
scopes:
- name: Atalay Ai Scopes
  scope_count: 0
  slug: atalay-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 16.8
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Atalay Ai Authentication
  slug: atalay-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Atalay Ai Domain Security
  slug: atalay-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: atalay-ai
tags:
- Artificial Intelligence
- Automation
- Business
- Software-as-a-Service
- Turkish
website: https://atalay.ai/
---
