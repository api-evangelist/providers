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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/roadrunner-ai/well-known/roadrunner-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/roadrunner-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/roadrunner-ai/hosts/roadrunner-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/roadrunner-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/roadrunner-ai/vendors/roadrunner-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/roadrunner-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://roadrunner.ai/legal/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.roadrunner.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://roadrunner.ai/legal/privacy-policy
- group: other
  title: ''
  type: Leadership
  url: https://roadrunner.ai/team
- group: docs
  title: ''
  type: Documentation
  url: https://docs.roadrunner.ai/
- group: auth
  href: https://artifacts.apis.io/roadrunner-ai/security/roadrunner-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/roadrunner-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://roadrunner.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://roadrunner.ai/product
- group: company
  title: ''
  type: Blog
  url: https://roadrunner.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://roadrunner.ai/contact
- group: commercial
  title: ''
  type: Legal
  url: https://roadrunner.ai/legal
- group: start
  title: ''
  type: GettingStarted
  url: https://roadrunner.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://roadrunner.ai/product
coverage:
  checked: '2026-10-29'
  detail: Docs require login at https://docs.roadrunner.ai/login, blocking access to API specifications.
  evidence:
  - status: 200
    url: https://docs.roadrunner.ai/login
  reason: partner-login
  state: gated
created: '2026-10-29'
description: Roadrunner provides an AI-native CPQ platform that enables users to create, configure, and approve quotes using natural language prompts. The solution automates pricing rules, licensing models, and approval workflows, integrating with existing tech stacks and CRMs. Backed by Founders Fund and Kleiner Perkins, Roadrunner aims to simplify complex quoting processes for sales, finance, and RevOps teams.
image: https://roadrunner.ai/site/photos/og-image.jpg
layout: provider
modified: '2026-10-29'
name: Roadrunner
nav: Providers
network: true
overview: 'Roadrunner is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, CPQ, SaaS, and Quoting.


  Roadrunner''s developer surface includes documentation, engineering blog, support, legal docs, getting-started guide, pricing, and 10 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 21.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 50.0
    operational_transparency: 15.8
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Roadrunner Ai Domain Security
  slug: roadrunner-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: roadrunner-ai
tags:
- Company
- AI
- CPQ
- SaaS
- Quoting
website: https://roadrunner.ai/
---
