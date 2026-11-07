---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.bfocus.com.br
  baseurl_source: declared
  description: API pública do bFocus providing lead management and customer support.
  name: bFocus API
  slug: bfocus-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/bfocus-com-br/plans/bfocus-com-br-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bfocus-com-br-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bfocus-com-br/conventions/bfocus-com-br-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/bfocus-com-br-conventions.yml
- group: design
  href: https://artifacts.apis.io/bfocus-com-br/conventions/bfocus-com-br-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bfocus-com-br-conventions.yml
- group: auth
  href: https://artifacts.apis.io/bfocus-com-br/authentication/bfocus-com-br-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bfocus-com-br-authentication.yml
- group: design
  href: https://artifacts.apis.io/bfocus-com-br/conformance/bfocus-com-br-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bfocus-com-br-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bfocus-com-br/llms/bfocus-com-br-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bfocus-com-br-llms.txt
- group: agent
  href: https://artifacts.apis.io/bfocus-com-br/well-known/bfocus-com-br-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bfocus-com-br-well-known.yml
- group: other
  href: https://artifacts.apis.io/bfocus-com-br/hosts/bfocus-com-br-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bfocus-com-br-hosts.yml
- group: other
  href: https://artifacts.apis.io/bfocus-com-br/vendors/bfocus-com-br-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bfocus-com-br-vendors.yml
- group: build
  href: https://artifacts.apis.io/bfocus-com-br/packages/bfocus-com-br-packages.yml
  title: ''
  type: SDKs
  url: packages/bfocus-com-br-packages.yml
- group: build
  href: https://artifacts.apis.io/bfocus-com-br/packages/bfocus-com-br-packages.yml
  title: ''
  type: Packages
  url: packages/bfocus-com-br-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bfocus.com.br/en/desenvolvedores
- group: auth
  href: https://artifacts.apis.io/bfocus-com-br/security/bfocus-com-br-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bfocus-com-br-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bfocus.com.br/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bfocus.com.br/desenvolvedores
- group: docs
  title: ''
  type: APIReference
  url: https://api.bfocus.com.br/api/v1/integration/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bfocus.com.br/precos
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bfocus.com.br/termos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bfocus.com.br/privacidade
- group: operate
  title: ''
  type: Support
  url: https://www.bfocus.com.br/atendimento
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 401
    url: https://api.bfocus.com.br/mcp
  - status: 200
    url: https://bfocus.com.br/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: bFocus provides AI‑enhanced lead management and customer support platform for businesses. It offers chat, ticketing, SLA management, project tracking, error monitoring, and integrates with WhatsApp, email, GitHub, and other services. The solution includes SDKs in multiple languages, widgets for native apps, and compliance with LGPD. The platform targets small to medium enterprises seeking automated customer interaction and workflow automation.
image: https://www.bfocus.com.br/social/og-image.png
layout: provider
modified: '2026-11-02'
name: bFocus
nav: Providers
network: true
overview: 'bFocus is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Lead Management, Customer Service, Software-as-a-Service, and Brazil.


  bFocus'' developer surface includes authentication, getting-started guide, documentation, API reference, pricing, support, and 14 more developer resources.'
plans:
- name: Bfocus Com Br Plans Pricing
  plan_count: 20
  slug: bfocus-com-br-plans-pricing
random_paper: 15
score:
  band: thin
  composite: 33.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 4.5
    contract_quality: 37.6
    developer_ergonomics: 35.7
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bfocus Com Br Authentication
  slug: bfocus-com-br-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bfocus Com Br Domain Security
  slug: bfocus-com-br-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bfocus-com-br
tags:
- Artificial Intelligence
- Lead Management
- Customer Service
- Software-as-a-Service
- Brazil
website: https://bfocus.com.br/
---
