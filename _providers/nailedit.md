---
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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/nailedit/plans/nailedit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nailedit-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/nailedit/llms/nailedit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nailedit-llms.txt
- group: other
  href: https://artifacts.apis.io/nailedit/hosts/nailedit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nailedit-hosts.yml
- group: other
  href: https://artifacts.apis.io/nailedit/vendors/nailedit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nailedit-vendors.yml
- group: auth
  href: https://artifacts.apis.io/nailedit/security/nailedit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nailedit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nailedit.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://nailedit.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://nailedit.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://nailedit.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://nailedit.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://nailedit.ai/pricing
- group: operate
  title: ''
  type: Support
  url: https://nailedit.ai/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nailedit.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nailedit.ai/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nailedit
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 401
    url: https://nailedit.ai/api/mcp
  - status: 200
    url: https://nailedit.ai/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: Nailedit provides a free AI-powered mock interview platform that helps job seekers practice interview questions. Users can paste job postings, answer aloud, and receive scores on five key interview criteria. The service aims to improve confidence and performance in real interviews, offering a free starter tier and AI-driven feedback.
image: https://nailedit.ai/icon-512.png
layout: provider
modified: '2026-10-21'
name: Nailedit
nav: Providers
network: true
overview: 'Nailedit is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Interview, Mock, and Career.


  Nailedit''s developer surface includes documentation, API reference, getting-started guide, pricing, support, and 10 more developer resources.'
plans:
- name: Nailedit Plans Pricing
  plan_count: 5
  slug: nailedit-plans-pricing
random_paper: 2
score:
  band: thin
  composite: 26.4
  coverage:
    artifact_dirs: 8
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
    discoverability: 48.2
    operational_transparency: 5.3
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
  name: Nailedit Domain Security
  slug: nailedit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nailedit
tags:
- Company
- AI
- Interview
- Mock
- Career
website: https://nailedit.ai/
---
