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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Rivio provides an AI‑powered execution layer for procurement, exposing endpoints for sourcing, supplier management, and spend analytics.
  name: Rivio API
  slug: rivio-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/rivio/llms/rivio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rivio-llms.txt
- group: other
  href: https://artifacts.apis.io/rivio/hosts/rivio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rivio-hosts.yml
- group: other
  href: https://artifacts.apis.io/rivio/vendors/rivio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rivio-vendors.yml
- group: auth
  href: https://artifacts.apis.io/rivio/security/rivio-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/rivio-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/rivio/security/rivio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rivio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rivio.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.rivio.ai/resources/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.rivio.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rivio.ai/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.rivio.ai/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rivio.ai/terms
coverage:
  checked: '2026-10-29'
  detail: API documentation endpoints return 403 Missing Authentication Token, indicating the reference is behind a customer login.
  evidence:
  - status: 403
    url: https://api.rivio.ai/docs
  reason: customer-only-docs
  state: gated
created: '2026-10-29'
description: Rivio provides an AI‑powered execution layer for procurement, helping enterprises automate sourcing, supplier management, and spend analytics. The platform combines machine‑learning insights with workflow automation to streamline purchasing decisions, reduce costs, and improve compliance across the supply chain. Backed by Gradient Ventures, Rivio targets B2B SaaS markets and integrates with ERP and finance systems.
image: https://www.rivio.ai/rivio-logo.png
layout: provider
modified: '2026-10-29'
name: Rivio
nav: Providers
network: true
overview: 'Rivio is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Procurement, SaaS, and B2B.


  Rivio''s developer surface includes engineering blog, signup flow, and 9 more developer resources.'
plans:
- name: Rivio Plans Pricing
  plan_count: 0
  slug: rivio-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Rivio Rate Limits
  slug: rivio-rate-limits
scopes:
- name: Rivio Scopes
  scope_count: 0
  slug: rivio-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Rivio Authentication
  slug: rivio-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Rivio Domain Security
  slug: rivio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rivio Vulnerability Disclosure
  slug: rivio-vulnerability-disclosure
  summary_line: no policy recorded
slug: rivio
tags:
- Company
- AI
- Procurement
- SaaS
- B2B
- Automation
website: https://www.rivio.ai/
---
