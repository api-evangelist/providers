---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
- group: commercial
  href: https://artifacts.apis.io/askmyev-com/plans/askmyev-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/askmyev-com-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://askmyev.com/privacy/
- group: agent
  href: https://artifacts.apis.io/askmyev-com/llms/askmyev-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/askmyev-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/askmyev-com/well-known/askmyev-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/askmyev-com-security.txt
- group: agent
  href: https://artifacts.apis.io/askmyev-com/well-known/askmyev-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/askmyev-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/askmyev-com/hosts/askmyev-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/askmyev-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/askmyev-com/vendors/askmyev-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/askmyev-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://askmyev.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://askmyev.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://askmyev.com/privacy/
- group: start
  title: ''
  type: Login
  url: https://askmyev.com/start/signin
- group: docs
  title: ''
  type: Documentation
  url: https://askmyev.com/guides/
- group: start
  title: ''
  type: GettingStarted
  url: https://askmyev.com/setup/
- group: auth
  href: https://artifacts.apis.io/askmyev-com/security/askmyev-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/askmyev-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/askmyev-com/security/askmyev-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/askmyev-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://askmyev.com/
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found despite public documentation pages.
  evidence:
  - status: 404
    url: https://api.askmyev.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AskMyEV provides an AI-powered assistant for Tesla owners, integrating ChatGPT, Claude, Grok, and Cursor to analyze vehicle data. Users can query battery health, range, charging costs, tire pressure, and alerts through a read‑only interface. The service offers a free trial and aims to simplify Tesla data insights with conversational AI.
image: https://askmyev.com/og/askmyev.jpg
layout: provider
modified: '2026-11-01'
name: AskMyEV
nav: Providers
network: true
overview: 'AskMyEV is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Tesla, Automotive, and Assistant.


  AskMyEV''s developer surface includes support, documentation, getting-started guide, and 13 more developer resources.'
plans:
- name: Askmyev Com Plans Pricing
  plan_count: 2
  slug: askmyev-com-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 16.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.3
  facets:
    access_clarity: 38.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 48.2
    operational_transparency: 5.3
  previous_composite: 23.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Askmyev Com Domain Security
  slug: askmyev-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Askmyev Com Vulnerability Disclosure
  slug: askmyev-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: askmyev-com
tags:
- Company
- Artificial Intelligence
- Tesla
- Automotive
- Assistant
website: https://askmyev.com/
---
