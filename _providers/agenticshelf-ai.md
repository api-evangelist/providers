---
access_model:
  confidence: medium
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/agenticshelf-ai/plans/agenticshelf-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agenticshelf-ai-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/agenticshelf-ai/hosts/agenticshelf-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agenticshelf-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/agenticshelf-ai/vendors/agenticshelf-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agenticshelf-ai-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://www.agenticshelf.ai/console
- group: auth
  href: https://artifacts.apis.io/agenticshelf-ai/security/agenticshelf-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agenticshelf-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agenticshelf.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.agenticshelf.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.agenticshelf.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agenticshelf.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agenticshelf.ai/privacy
coverage:
  checked: '2026-10-29'
  detail: The API documentation is behind a sign‑in page (https://www.agenticshelf.ai/console) requiring authentication.
  evidence:
  - status: 200
    url: https://www.agenticshelf.ai/console
  reason: customer-only-docs
  state: gated
created: '2026-10-29'
description: Agentic Shelf delivers Multi-Channel Presence (MCP) tools, live audits, and AI‑driven visibility for e‑commerce platforms. It offers adapters for Shopify, Amazon, WooCommerce, BigCommerce and custom headless stores, enabling merchants to measure and improve how large language models cite their products. The platform provides a free audit console, methodology documentation, and a roadmap for future AI commerce capabilities.
image: https://www.agenticshelf.ai/agentic-shelf-logo.svg
layout: provider
modified: '2026-10-29'
name: agenticshelf-ai
nav: Providers
network: true
overview: 'agenticshelf-ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Commerce, MCP, and Auditing.


  agenticshelf-ai''s developer surface includes sandbox, pricing, engineering blog, and 7 more developer resources.'
plans:
- name: Agenticshelf Ai Plans Pricing
  plan_count: 1
  slug: agenticshelf-ai-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Agenticshelf Ai Rate Limits
  slug: agenticshelf-ai-rate-limits
scopes:
- name: Agenticshelf Ai Scopes
  scope_count: 0
  slug: agenticshelf-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.6
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 18.2
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/agenticshelf-ai/agenticshelf-ai-2026-11-03T120359.png
security:
- kind: authentication
  name: Agenticshelf Ai Authentication
  slug: agenticshelf-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Agenticshelf Ai Domain Security
  slug: agenticshelf-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: agenticshelf-ai
tags:
- Company
- Artificial Intelligence
- Commerce
- MCP
- Auditing
website: https://agenticshelf.ai/
---
