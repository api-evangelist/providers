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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MCP tools list for AdAdvisor API
  name: AdAdvisor MCP Tools
  slug: adadvisor-mcp-tools
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/adadvisor-ai/plans/adadvisor-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adadvisor-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/adadvisor-ai/llms/adadvisor-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adadvisor-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/adadvisor-ai/well-known/adadvisor-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adadvisor-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/adadvisor-ai/hosts/adadvisor-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adadvisor-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/adadvisor-ai/vendors/adadvisor-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adadvisor-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adadvisor.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adadvisor.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://adadvisor.ai/pricing
- group: other
  title: ''
  type: Leadership
  url: https://adadvisor.ai/team
- group: docs
  title: ''
  type: Documentation
  url: https://adadvisor.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://adadvisor.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://adadvisor.ai/docs/user-guide/onboarding-walkthrough
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AdAdvisor
- group: auth
  href: https://artifacts.apis.io/adadvisor-ai/security/adadvisor-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adadvisor-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adadvisor.ai/
created: '2026-10-31'
description: AdAdvisor is an AI‑powered command center for paid media that automates media buying, campaign management, and creative generation across Meta, Google, TikTok, Snap and other major ad platforms. The platform combines data engineering, machine learning models, and a unified dashboard to help advertisers scale spend, improve ROAS, and reduce manual workload. Founded by a digital‑marketing agency team, AdAdvisor offers a 7‑day free trial and tools such as calculators, generators, and a Nova AI buyer that runs ad accounts autonomously.
layout: provider
modified: '2026-10-31'
name: AdAdvisor
nav: Providers
network: true
overview: 'AdAdvisor is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Advertising, Media Buying, and Marketing Automation.


  AdAdvisor''s developer surface includes pricing, documentation, engineering blog, getting-started guide, and 11 more developer resources.'
plans:
- name: Adadvisor Ai Plans Pricing
  plan_count: 3
  slug: adadvisor-ai-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 17.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 63.4
    operational_transparency: 2.6
  previous_composite: 24.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Adadvisor Ai Domain Security
  slug: adadvisor-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adadvisor-ai
tags:
- Company
- Artificial Intelligence
- Advertising
- Media Buying
- Marketing Automation
- Software-as-a-Service
website: https://adadvisor.ai/
---
