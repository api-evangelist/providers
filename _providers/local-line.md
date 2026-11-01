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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/local-line/plans/local-line-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/local-line-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/local-line/llms/local-line-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/local-line-llms.txt
- group: other
  href: https://artifacts.apis.io/local-line/hosts/local-line-hosts.yml
  title: ''
  type: Hosts
  url: hosts/local-line-hosts.yml
- group: other
  href: https://artifacts.apis.io/local-line/vendors/local-line-vendors.yml
  title: ''
  type: Vendors
  url: vendors/local-line-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.localline.co/tag/press
- group: docs
  title: ''
  type: Documentation
  url: https://www.localline.co/guides/how-to-run-a-csa
- group: auth
  href: https://artifacts.apis.io/local-line/security/local-line-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/local-line-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.localline.co/
- group: company
  title: ''
  type: Blog
  url: https://www.localline.co/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.localline.co/buyers/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.localline.co/register
- group: start
  title: ''
  type: Login
  url: https://www.localline.co/login
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found despite probing common spec URLs on api.localline.co.
  evidence:
  - status: 200
    url: https://api.localline.co/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Local Line is a farm‑to‑fork commerce platform that enables producers, distributors, grocers, and restaurants to buy and sell local food directly. Trusted by leading farms and retailers, it offers built‑in reporting, traceability, and integrations with ERP, POS, and e‑commerce tools, helping create a transparent, efficient local food supply chain.
image: https://cdn.prod.website-files.com/65ddf7b99a8b454b93dd2a82/6a1462815602c40208ee7c2b_Local%20Line%20Farm-to-Fork%20Commerce%20Platform%20(1).png
layout: provider
modified: '2026-10-28'
name: Local Line
nav: Providers
network: true
overview: 'Local Line is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, E-commerce, Supply Chain, Food Tech, and SaaS.


  Local Line''s developer surface includes documentation, engineering blog, pricing, signup flow, and 8 more developer resources.'
plans:
- name: Local Line Plans Pricing
  plan_count: 3
  slug: local-line-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Local Line Rate Limits
  slug: local-line-rate-limits
scopes:
- name: Local Line Scopes
  scope_count: 0
  slug: local-line-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Local Line Authentication
  slug: local-line-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Local Line Domain Security
  slug: local-line-domain-security
  summary_line: TLSv1.3 · HSTS
slug: local-line
tags:
- Agriculture
- E-commerce
- Supply Chain
- Food Tech
- SaaS
website: https://www.localline.co/
---
