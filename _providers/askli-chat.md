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
    dynamic_client_registration: false
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
  score: 14.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Askli provides AI‑powered user research APIs accessible via their platform. Documentation is available at the website but no machine‑readable contract was found.
  name: Askli API
  slug: askli-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/askli-chat/plans/askli-chat-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/askli-chat-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/askli-chat/llms/askli-chat-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/askli-chat-llms.txt
- group: agent
  href: https://artifacts.apis.io/askli-chat/well-known/askli-chat-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/askli-chat-well-known.yml
- group: other
  href: https://artifacts.apis.io/askli-chat/hosts/askli-chat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/askli-chat-hosts.yml
- group: other
  href: https://artifacts.apis.io/askli-chat/vendors/askli-chat-vendors.yml
  title: ''
  type: Vendors
  url: vendors/askli-chat-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.askli.chat/terms
- group: operate
  title: ''
  type: Support
  url: https://www.askli.chat/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.askli.chat/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.askli.chat/pricing
- group: auth
  href: https://artifacts.apis.io/askli-chat/security/askli-chat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/askli-chat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.askli.chat/
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL spec could be located on the provider's domain.
  evidence:
  - status: 404
    url: https://www.askli.chat/openapi.json
  - status: 404
    url: https://www.askli.chat/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Askli provides AI‑powered user research, enabling product teams to validate ideas, features, and customer needs by conducting real‑user interviews moderated by artificial intelligence. The platform offers quick checks, pricing plans, and integrations, delivering evidence‑based insights to guide development decisions and reduce assumptions.
image: https://www.askli.chat/brand/askli-logo.png
layout: provider
modified: '2026-11-01'
name: Askli
nav: Providers
network: true
overview: 'Askli is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, User Research, Market Validation, Product Development, and Software-as-a-Service.


  Askli''s developer surface includes support, pricing, and 9 more developer resources.'
plans:
- name: Askli Chat Plans Pricing
  plan_count: 1
  slug: askli-chat-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 13.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.2
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 17.7
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Askli Chat Domain Security
  slug: askli-chat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: askli-chat
tags:
- Artificial Intelligence
- User Research
- Market Validation
- Product Development
- Software-as-a-Service
website: https://www.askli.chat/
---
