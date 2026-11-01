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
api_count: 1
apis:
- description: API reference for Colaunched AI (access gated behind login).
  name: Colaunched API
  slug: colaunched-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/colaunched-ai/plans/colaunched-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/colaunched-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/colaunched-ai/llms/colaunched-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/colaunched-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/colaunched-ai/hosts/colaunched-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/colaunched-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/colaunched-ai/vendors/colaunched-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/colaunched-ai-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.colaunched.ai/login
- group: auth
  href: https://artifacts.apis.io/colaunched-ai/security/colaunched-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/colaunched-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://colaunched.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.colaunched.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://colaunched.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://colaunched.ai/docs
- group: operate
  title: ''
  type: Support
  url: https://colaunched.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://colaunched.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://colaunched.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://colaunched.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://colaunched.ai/privacy/
coverage:
  checked: '2026-10-30'
  detail: API reference at https://app.colaunched.ai/api redirects to a login page, preventing access to documentation.
  evidence:
  - status: 307
    url: https://app.colaunched.ai/api
  reason: customer-only-docs
  state: gated
created: '2026-10-29'
description: Colaunched is a platform that surfaces business ideas derived from real public demand, scores them for feasibility, timing, market gap, and personal fit, and provides a ninety‑day launch plan with verified first‑revenue milestones. Users can explore ideas, receive detailed scoring, and access AI‑assisted tools such as Claude and ChatGPT to evaluate and execute concepts.
image: https://colaunched.ai/og.png
layout: provider
modified: '2026-10-29'
name: colaunched-ai
nav: Providers
network: true
overview: 'colaunched-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Business, Startup, Idea-Generation, and Market-Research.


  colaunched-ai''s developer surface includes documentation, API reference, support, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Colaunched Ai Plans Pricing
  plan_count: 3
  slug: colaunched-ai-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Colaunched Ai Rate Limits
  slug: colaunched-ai-rate-limits
scopes:
- name: Colaunched Ai Scopes
  scope_count: 0
  slug: colaunched-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Colaunched Ai Authentication
  slug: colaunched-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Colaunched Ai Domain Security
  slug: colaunched-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: colaunched-ai
tags:
- Company
- Business
- Startup
- Idea-Generation
- Market-Research
website: https://colaunched.ai/
---
