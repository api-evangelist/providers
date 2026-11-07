---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
- description: API documented at https://ask10ais.com/en/guides/questions-to-ask providing rankings, methodology, pricing etc.
  name: Ask10AI API
  slug: ask10ai-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/ask10ais-com/plans/ask10ais-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ask10ais-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/ask10ais-com/llms/ask10ais-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ask10ais-com-llms.txt
- group: other
  href: https://artifacts.apis.io/ask10ais-com/hosts/ask10ais-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ask10ais-com-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://ask10ais.com/en/login
- group: start
  title: ''
  type: GettingStarted
  url: https://ask10ais.com/en/agents
- group: auth
  href: https://artifacts.apis.io/ask10ais-com/security/ask10ais-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ask10ais-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ask10ais.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ask10ais.com/en/
- group: commercial
  title: ''
  type: Pricing
  url: https://ask10ais.com/en/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ask10ais.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ask10ais.com/en/privacy
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI or other machine‑readable contract is published; only human docs exist.
  evidence:
  - status: 200
    url: https://ask10ais.com/en/guides/questions-to-ask
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Ask10AI provides a cross‑model AI brand mindshare ranking platform that publicly verifies raw model responses. The service offers methodology insights, pricing details, and refusal logs, allowing brands to diagnose and improve their AI visibility across multiple large language models. Users can access rankings, methodology, insights, and pricing in both English and Chinese, with tools to share results via QR codes and social media.
image: https://ask10ais.com/api/share-card/page/home?lang=en&v=2
layout: provider
modified: '2026-11-01'
name: Ask10AI
nav: Providers
network: true
overview: 'Ask10AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Rankings, Brand Monitoring, LLM Evaluation, and AI Visibility.


  Ask10AI''s developer surface includes getting-started guide, documentation, pricing, and 8 more developer resources.'
plans:
- name: Ask10Ais Com Plans Pricing
  plan_count: 11
  slug: ask10ais-com-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.3
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 24.2
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ask10Ais Com Domain Security
  slug: ask10ais-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ask10ais-com
tags:
- AI Rankings
- Brand Monitoring
- LLM Evaluation
- AI Visibility
website: https://ask10ais.com/
---
