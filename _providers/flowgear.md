---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/flowgear/plans/flowgear-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/flowgear-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/flowgear/llms/flowgear-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flowgear-llms.txt
- group: other
  href: https://artifacts.apis.io/flowgear/hosts/flowgear-hosts.yml
  title: ''
  type: Hosts
  url: hosts/flowgear-hosts.yml
- group: build
  href: https://artifacts.apis.io/flowgear/packages/flowgear-packages.yml
  title: ''
  type: SDKs
  url: packages/flowgear-packages.yml
- group: build
  href: https://artifacts.apis.io/flowgear/packages/flowgear-packages.yml
  title: ''
  type: Packages
  url: packages/flowgear-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.flowgear.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flowgear.net/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.flowgear.net/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.flowgear.net/common/releases
- group: docs
  title: ''
  type: APIReference
  url: https://help.flowgear.net/reference
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Flowgear
- group: auth
  href: https://artifacts.apis.io/flowgear/security/flowgear-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flowgear-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.flowgear.net/
- group: docs
  title: ''
  type: Documentation
  url: https://help.flowgear.net/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.flowgear.net/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.flowgear.net/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.flowgear.net/v2/getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.flowgear.net/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.flowgear.net
created: '2026-10-20'
description: Flowgear provides an integration development platform that enables businesses to build, run, and govern automated workflows and data integrations at the speed of AI. The platform offers a single‑tenant, governed infrastructure with custom connectors, AI‑driven agents, and a visual builder, supporting use cases across finance, HR, sales, marketing, and more. Flowgear aims to accelerate digital transformation by simplifying complex system integrations and providing enterprise‑grade security and scalability.
image: https://www.flowgear.net/og/default.png
layout: provider
modified: '2026-10-20'
name: Flowgear
nav: Providers
network: true
overview: 'Flowgear is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Integration, Automation, AI, Platform, and Enterprise.


  Flowgear''s developer surface includes changelog, API reference, documentation, pricing, engineering blog, getting-started guide, support, and 12 more developer resources.'
plans:
- name: Flowgear Plans Pricing
  plan_count: 5
  slug: flowgear-plans-pricing
random_paper: 15
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 50.0
    operational_transparency: 36.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Flowgear Domain Security
  slug: flowgear-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flowgear
tags:
- Integration
- Automation
- AI
- Platform
- Enterprise
website: https://www.flowgear.net/
---
