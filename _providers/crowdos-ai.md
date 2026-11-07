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
    mcp_server: documented
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
  score: 21.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: docs
  title: ''
  type: Documentation
  url: https://crowdos.ai/guides
- group: start
  title: ''
  type: DeveloperPortal
  url: https://crowdos.ai/developers
- group: commercial
  href: https://artifacts.apis.io/crowdos-ai/plans/crowdos-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/crowdos-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/crowdos-ai/llms/crowdos-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crowdos-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/crowdos-ai/well-known/crowdos-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/crowdos-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/crowdos-ai/hosts/crowdos-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crowdos-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/crowdos-ai/vendors/crowdos-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crowdos-ai-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://crowdos.ai/signup
- group: auth
  href: https://artifacts.apis.io/crowdos-ai/security/crowdos-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crowdos-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crowdos.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://crowdos.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crowdos.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crowdos.ai/privacy
coverage:
  checked: '2026-11-04'
  detail: Documentation pages exist but no machine‑readable OpenAPI, AsyncAPI, GraphQL or other contract is published.
  evidence:
  - status: 200
    url: https://crowdos.ai/guides
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: CrowdOS provides a population‑intelligence platform that runs synthetic focus groups of 20–1,000 census‑grounded respondents in minutes. It offers free plans, paid tiers, and enterprise options, delivering AI‑driven market research validated against Pew Research benchmarks. The service includes a developer MCP API for integration, detailed documentation, and a privacy‑focused data handling policy.
image: https://crowdos.ai/opengraph-image
layout: provider
modified: '2026-11-04'
name: CrowdOS
nav: Providers
network: true
overview: 'CrowdOS is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Market Research, Synthetic Data, Focus Groups, and Platform.


  CrowdOS''s developer surface includes documentation, signup flow, pricing, and 10 more developer resources.'
plans:
- name: Crowdos Ai Plans Pricing
  plan_count: 3
  slug: crowdos-ai-plans-pricing
random_paper: 8
score:
  band: emerging
  composite: 24.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crowdos Ai Domain Security
  slug: crowdos-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crowdos-ai
tags:
- Artificial Intelligence
- Market Research
- Synthetic Data
- Focus Groups
- Platform
website: https://crowdos.ai/
---
