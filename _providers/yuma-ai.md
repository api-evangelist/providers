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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Public API for Yuma AI agents to integrate with eCommerce platforms. Documentation is available on the website but no machine‑readable contract was found.
  name: Yuma AI API
  slug: yuma-ai-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/yuma-ai/plans/yuma-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/yuma-ai-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://yuma.ai/security
- group: agent
  href: https://artifacts.apis.io/yuma-ai/llms/yuma-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/yuma-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/yuma-ai/well-known/yuma-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/yuma-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/yuma-ai/hosts/yuma-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/yuma-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/yuma-ai/vendors/yuma-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/yuma-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://yuma.ai/terms-of-service
- group: auth
  title: ''
  type: Security
  url: https://yuma.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://yuma.ai/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://yuma.ai/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://yuma.ai/blogs/topic/news
- group: start
  title: ''
  type: Login
  url: https://app.yuma.ai/signin
- group: auth
  href: https://artifacts.apis.io/yuma-ai/security/yuma-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/yuma-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/yuma-ai/security/yuma-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yuma-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://yuma.ai/
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL files were discoverable on yuma.ai or its subdomains.
  evidence:
  - status: 404
    url: https://yuma.ai/openapi.json
  - status: 404
    url: https://api.yuma.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Yuma AI provides AI-powered solutions for businesses, offering tools for data analysis, automation, and decision support. The company focuses on integrating advanced machine learning models into enterprise workflows, enabling scalable insights and operational efficiency. Backed by Gradient Ventures, Yuma AI aims to democratize AI technology across various industries.
image: https://yuma.ai/og/home.jpg
layout: provider
modified: '2026-10-29'
name: Yuma AI
nav: Providers
network: true
overview: 'Yuma AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Machine-Learning, Automation, and Data-Analysis.


  Yuma AI''s developer surface includes pricing and 14 more developer resources.'
plans:
- name: Yuma Ai Plans Pricing
  plan_count: 3
  slug: yuma-ai-plans-pricing
random_paper: 19
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.9
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Yuma Ai Domain Security
  slug: yuma-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Yuma Ai Trust Center
  slug: yuma-ai-trust-center
  summary_line: SOC 2, GDPR
slug: yuma-ai
tags:
- Company
- AI
- Machine-Learning
- Automation
- Data-Analysis
website: https://yuma.ai/
---
