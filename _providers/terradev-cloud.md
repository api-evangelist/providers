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
  band: human-only
  dimensions:
    agent_card: flavored
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
  score: 1.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/terradev-cloud/plans/terradev-cloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/terradev-cloud-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/terradev-cloud/llms/terradev-cloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/terradev-cloud-llms.txt
- group: other
  href: https://artifacts.apis.io/terradev-cloud/a2a/terradev-cloud-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/terradev-cloud-a2a.yml
- group: other
  href: https://artifacts.apis.io/terradev-cloud/hosts/terradev-cloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/terradev-cloud-hosts.yml
- group: auth
  href: https://artifacts.apis.io/terradev-cloud/security/terradev-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/terradev-cloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://terradev.cloud/
- group: docs
  title: ''
  type: Documentation
  url: https://terradev.cloud/docs
- group: docs
  title: ''
  type: APIReference
  url: https://terradev.cloud/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://terradev.cloud/docs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://terradev.cloud/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://terradev.cloud/privacy
created: '2026-10-29'
description: Terradev.cloud provides infrastructure primitives for the agentic economy, offering hosted ledgers, live observability, and GPU provisioning tools. Their platform includes services like Templum for tamper‑evident ledgers, Telinea for trace visualization, and a suite of MCP servers for randomness, consensus, and dead‑drop networking. Pricing starts at $9.99/month with free trials, and they emphasize open‑source components under Apache 2.0. The company targets developers building autonomous agent systems needing verifiable proof of actions.
image: https://terradev.cloud/logo-black.png
layout: provider
modified: '2026-10-29'
name: terradev-cloud
nav: Providers
network: true
overview: 'terradev-cloud is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Infrastructure, AgenticEconomy, Observability, and GPU.


  terradev-cloud''s developer surface includes documentation, API reference, getting-started guide, and 8 more developer resources.'
plans:
- name: Terradev Cloud Plans Pricing
  plan_count: 2
  slug: terradev-cloud-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 55.4
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 19.5
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
screenshot: https://apis.io/screenshots/terradev-cloud/terradev-cloud-2026-11-03T144445.png
security:
- kind: domain-security
  name: Terradev Cloud Domain Security
  slug: terradev-cloud-domain-security
  summary_line: TLSv1.3 · DMARC
slug: terradev-cloud
tags:
- Company
- Infrastructure
- AgenticEconomy
- Observability
- GPU
website: https://terradev.cloud/
---
