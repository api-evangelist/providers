---
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Sherpa provides AI‑powered website platform APIs as described on their documentation site.
  name: Sherpa API
  slug: sherpa-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/withsherpa-ai/plans/withsherpa-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/withsherpa-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/withsherpa-ai/llms/withsherpa-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/withsherpa-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/withsherpa-ai/well-known/withsherpa-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/withsherpa-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/withsherpa-ai/hosts/withsherpa-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/withsherpa-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/withsherpa-ai/vendors/withsherpa-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/withsherpa-ai-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.withsherpa.ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.withsherpa.ai/privacy
- group: start
  title: ''
  type: Login
  url: https://www.withsherpa.ai/signin
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/withsherpa
- group: auth
  href: https://artifacts.apis.io/withsherpa-ai/security/withsherpa-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/withsherpa-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.withsherpa.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.withsherpa.ai/pricing
- group: company
  title: ''
  type: About
  url: https://www.withsherpa.ai/about
coverage:
  checked: '2026-10-29'
  detail: Documentation pages are JavaScript‑rendered and no OpenAPI spec is accessible via GET.
  evidence:
  - status: 404
    url: https://www.withsherpa.ai/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Sherpa provides an AI‑powered website platform that enables teams and agents to manage, build, and personalize web pages through natural language commands. Backed by Y‑Combinator, Sherpa integrates with tools like Claude, ChatGPT, and Slack, offering features such as experiments, page building, adaptation, and pricing plans. The service aims to turn design briefs into production‑ready sites, supporting collaboration and rapid iteration for modern digital teams.
image: https://www.withsherpa.ai/_sherpa/assets/static/marketing/website/social-card-sticker-desk.png
layout: provider
modified: '2026-10-29'
name: Sherpa
nav: Providers
network: true
overview: 'Sherpa is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, WebsitePlatform, LowCode, and Collaboration.


  Sherpa''s developer surface includes pricing and 12 more developer resources.'
plans:
- name: Withsherpa Ai Plans Pricing
  plan_count: 2
  slug: withsherpa-ai-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 21.1
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Withsherpa Ai Domain Security
  slug: withsherpa-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: withsherpa-ai
tags:
- Company
- AI
- WebsitePlatform
- LowCode
- Collaboration
website: https://www.withsherpa.ai/
---
