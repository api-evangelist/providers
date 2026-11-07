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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public API reference page (gated) for Deal.ai platform
  name: Deal.ai API
  slug: deal-ai-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/dealai/well-known/dealai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dealai-well-known.yml
- group: other
  href: https://artifacts.apis.io/dealai/hosts/dealai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dealai-hosts.yml
- group: other
  href: https://artifacts.apis.io/dealai/vendors/dealai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dealai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://home.deal.ai/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://home.deal.ai/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/forgeglobal
- group: auth
  href: https://artifacts.apis.io/dealai/security/dealai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dealai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://home.deal.ai/
coverage:
  checked: '2026-10-22'
  detail: API documentation at https://join.deal.ai/api-docs returns HTTP 403, blocking access to the contract.
  evidence:
  - status: 403
    url: https://join.deal.ai/api-docs
  reason: sales-gate
  state: gated
created: '2026-10-22'
description: Deal.ai is an all‑in‑one AI platform that provides over 75 AI tools for marketing, content creation, and business growth. It powers applications such as Famous.ai and SuperCool, offering features like AI‑generated podcasts, video creation, copywriting, and website building. Targeted at entrepreneurs and agencies, Deal.ai aims to streamline workflows with a unified interface and supports integrations across various services. The platform emphasizes ease of use, scalability, and a subscription model for continuous AI enhancements.
image: https://deal.ai/og-image.png
layout: provider
modified: '2026-10-22'
name: Deal.ai
nav: Providers
network: true
overview: Deal.ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Marketing, Content, and Software-as-a-Service.
random_paper: 8
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.1
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 2.6
  previous_composite: 10.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/dealai/dealai-2026-11-03T130343.png
security:
- kind: domain-security
  name: Dealai Domain Security
  slug: dealai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dealai
tags:
- Company
- Artificial Intelligence
- Marketing
- Content
- Software-as-a-Service
- Platform
website: https://home.deal.ai/
---
