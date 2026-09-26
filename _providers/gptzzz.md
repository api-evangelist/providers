---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-09-25'
api_count: 2
apis:
- description: OpenAI-compatible relay interface. The docs give the Base URL https://gptzzz.ai/v1 for OpenAI-compatible clients (which append /chat/completions or /responses); requests are authenticated with a KaiGP
  name: KaiGPT OpenAI-Compatible API
  slug: kaigpt-openai-compatible-api
- description: Claude Messages relay route. The docs give https://gptzzz.ai/v1/messages for Claude Messages requests and say Claude clients must use that protocol configuration rather than the OpenAI request body; t
  name: KaiGPT Claude Messages API
  slug: kaigpt-claude-messages-api
artifact_total: 6
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gptzzz/refs/heads/main/conventions/gptzzz-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gptzzz-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gptzzz/refs/heads/main/authentication/gptzzz-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gptzzz-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gptzzz/refs/heads/main/lifecycle/gptzzz-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gptzzz-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gptzzz/refs/heads/main/errors/gptzzz-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gptzzz-problem-types.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gptzzz/refs/heads/main/llms/gptzzz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gptzzz-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gptzzz/refs/heads/main/hosts/gptzzz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gptzzz-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gptzzz/refs/heads/main/vendors/gptzzz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gptzzz-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://gptzzz.ai/status/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gptzzz/refs/heads/main/security/gptzzz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gptzzz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gptzzz.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://gptzzz.ai/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://gptzzz.ai/blog/api-zhongzhuan-how-to-use/
- group: operate
  title: ''
  type: Support
  url: https://gptzzz.ai/support/
- group: company
  title: ''
  type: Blog
  url: https://gptzzz.ai/blog/
- group: start
  title: ''
  type: SignUp
  url: https://gptzzz.ai/register
- group: start
  title: ''
  type: Login
  url: https://gptzzz.ai/login
- group: docs
  title: ''
  type: Documentation
  url: https://gptzzz.ai/docs/glossary/
- group: design
  title: ''
  type: ErrorCodes
  url: https://gptzzz.ai/docs/api-error-codes/
created: '2026-09-23'
description: KaiGPT (gptzzz.ai, site name "gptzzz.ai", subtitle "AI API 中转服务 中转站") is an independent third-party AI API relay (中转站) and multi-model gateway for Chinese-speaking developers. It exposes an OpenAI-compatible interface at https://gptzzz.ai/v1 (chat completions, Responses, embeddings, images), a Claude Messages route at https://gptzzz.ai/v1/messages and a Gemini-style v1beta surface, authenticated with a KaiGPT API key via Authorization Bearer, x-api-key or x-goog-api-key. Model IDs, group multipliers and limits are shown only in the logged-in console; the public model plaza lists no models or prices yet. It also ships a desktop client that configures Claude Code, Codex, Gemini CLI and OpenCode, and a Chinese knowledge base on relay selection, security and compliance. KaiGPT states it is not affiliated with the model vendors it routes to; it resells access to other providers' model APIs rather than training models itself.
image: https://gptzzz.ai/blog/assets/og-cover.png
layout: provider
modified: '2026-09-23'
name: KaiGPT
nav: Providers
network: true
overview: 'KaiGPT publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, LLM Gateway, API Relay, OpenAI-Compatible, and Claude.


  KaiGPT''s developer surface includes authentication, documentation, getting-started guide, support, engineering blog, signup flow, and 12 more developer resources.'
plans:
- name: Gptzzz Plans Pricing
  plan_count: 0
  slug: gptzzz-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Gptzzz Rate Limits
  slug: gptzzz-rate-limits
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.9
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 64.3
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 20.4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Gptzzz Authentication
  slug: gptzzz-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Gptzzz Domain Security
  slug: gptzzz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gptzzz
tags:
- Artificial Intelligence
- LLM Gateway
- API Relay
- OpenAI-Compatible
- Claude
- Gemini
- LLM
- China
website: https://gptzzz.ai/
---
