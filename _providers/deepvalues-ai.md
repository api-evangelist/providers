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
- description: DeepValues AI provides AI-driven analytics platform.
  name: DeepValues AI
  slug: deepvalues-ai
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/deepvalues-ai/llms/deepvalues-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deepvalues-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/deepvalues-ai/well-known/deepvalues-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deepvalues-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/deepvalues-ai/hosts/deepvalues-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deepvalues-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/deepvalues-ai/vendors/deepvalues-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deepvalues-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deepvalues.ai/terms.html
- group: other
  title: ''
  type: Leadership
  url: https://research.deepvalues.ai/company/team/
- group: auth
  href: https://artifacts.apis.io/deepvalues-ai/security/deepvalues-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deepvalues-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deepvalues.ai/
coverage:
  checked: '2026-11-05'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found despite documented API reference pages.
  evidence:
  - status: 200
    url: https://app.deepvalues.ai/api
  - status: 200
    url: https://research.deepvalues.ai/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: DeepValues.AI is an AI-native financial assistant that provides institutional‑grade research, intrinsic‑value tools, and Smart Money tracking for everyday investors. It reads every SEC filing, earnings call, and 13F, delivering structured briefings, valuation models, and AI‑driven Q&A in multiple languages, all without ads or conflicts of interest. The platform offers free weekly margin‑of‑safety briefs, premium reports, and mobile apps for iOS and Android. Built by LuLu Ventures LLC, it aims to democratize deep value investing for individuals.
image: https://deepvalues.ai/images/deepvalues-appicon-1024.jpg
layout: provider
modified: '2026-11-05'
name: DeepValues.AI
nav: Providers
network: true
overview: DeepValues.AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Finance, Investment, and Valuation.
random_paper: 21
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.9
    operational_transparency: 0.0
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
  name: Deepvalues Ai Domain Security
  slug: deepvalues-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: deepvalues-ai
tags:
- Company
- Artificial Intelligence
- Finance
- Investment
- Valuation
- Research
website: https://deepvalues.ai/
---
