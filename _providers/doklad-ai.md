---
access_model:
  confidence: low
  label: Free
  onboarding: unknown
  pricing: free
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
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/doklad-ai/plans/doklad-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/doklad-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/doklad-ai/llms/doklad-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/doklad-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/doklad-ai/well-known/doklad-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/doklad-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/doklad-ai/hosts/doklad-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/doklad-ai-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://doklad.ai/terms
- group: start
  title: ''
  type: SignUp
  url: https://doklad.ai/register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://doklad.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://doklad.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://doklad.ai/blog
- group: auth
  href: https://artifacts.apis.io/doklad-ai/security/doklad-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/doklad-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://doklad.ai/
coverage:
  checked: '2026-11-05'
  detail: The provider's site lists an API reference at https://doklad.ai/api but no machine‑readable OpenAPI, GraphQL, AsyncAPI or other contract is available.
  evidence:
  - status: 404
    url: https://doklad.ai/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: 'doklad-ai is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://doklad.ai/api/og-image?title=Kompletn%C3%AD+fakturace+zdarma&subtitle=Doklad.ai
layout: provider
modified: '2026-11-05'
name: Doklad.ai
nav: Providers
network: true
overview: 'Doklad.ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Doklad.ai''s developer surface includes signup flow, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Doklad Ai Plans Pricing
  plan_count: 1
  slug: doklad-ai-plans-pricing
random_paper: 6
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 8.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 30.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Doklad Ai Domain Security
  slug: doklad-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: doklad-ai
tags:
- Company
website: https://doklad.ai/
---
