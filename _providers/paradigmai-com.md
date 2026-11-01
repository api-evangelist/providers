---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
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
  score: 30.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for Paradigm AI platform, documented at the developer docs.
  name: Paradigm API
  slug: paradigm-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/paradigmai-com/plans/paradigmai-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/paradigmai-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/paradigmai-com/authentication/paradigmai-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/paradigmai-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/paradigmai-com/llms/paradigmai-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/paradigmai-com-llms.txt
- group: other
  href: https://artifacts.apis.io/paradigmai-com/a2a/paradigmai-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/paradigmai-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/paradigmai-com/well-known/paradigmai-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/paradigmai-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/paradigmai-com/hosts/paradigmai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/paradigmai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/paradigmai-com/vendors/paradigmai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/paradigmai-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.paradigmai.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.paradigmai.com/getting-started/intro
- group: auth
  href: https://artifacts.apis.io/paradigmai-com/security/paradigmai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/paradigmai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.paradigmai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.paradigmai.com
- group: commercial
  title: ''
  type: Pricing
  url: https://paradigmai.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://paradigmai.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://paradigmai.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://trust.paradigmai.com
coverage:
  checked: '2026-10-29'
  detail: Docs are public but no OpenAPI/AsyncAPI/GraphQL spec found at known locations.
  evidence:
  - status: 404
    url: https://docs.paradigmai.com/openapi.json
  - status: 404
    url: https://api.paradigmai.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Paradigm is an AI-driven platform that empowers businesses to harness advanced machine learning models for data analysis, automation, and decision support. Founded in 2022, Paradigm offers a suite of APIs that enable developers to integrate predictive analytics, natural language processing, and custom model deployment into their applications. Backed by General Catalyst, the company focuses on delivering scalable, secure, and easy-to-use AI services across industries such as finance, healthcare, and retail. The platform emphasizes transparency, compliance, and robust documentation to facilitate rapid adoption and integration.
image: https://a.storyblok.com/f/294639322874097/0c04ccae0e/share.png
layout: provider
modified: '2026-10-29'
name: Paradigm
nav: Providers
network: true
overview: 'Paradigm is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, GTM, Automation, and Analytics.


  Paradigm''s developer surface includes authentication, getting-started guide, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Paradigmai Com Plans Pricing
  plan_count: 5
  slug: paradigmai-com-plans-pricing
random_paper: 11
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    mcp: unknown
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
- kind: authentication
  name: Paradigmai Com Authentication
  slug: paradigmai-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Paradigmai Com Domain Security
  slug: paradigmai-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: paradigmai-com
tags:
- Company
- AI
- GTM
- Automation
- Analytics
website: https://www.paradigmai.com/
---
