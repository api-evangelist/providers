---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/skusafe/llms/skusafe-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/skusafe-llms.txt
- group: other
  href: https://artifacts.apis.io/skusafe/hosts/skusafe-hosts.yml
  title: ''
  type: Hosts
  url: hosts/skusafe-hosts.yml
- group: other
  href: https://artifacts.apis.io/skusafe/vendors/skusafe-vendors.yml
  title: ''
  type: Vendors
  url: vendors/skusafe-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.skusafe.com
- group: auth
  title: ''
  type: Security
  url: https://skusafe.com/legal/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SKUsafe
- group: auth
  href: https://artifacts.apis.io/skusafe/security/skusafe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/skusafe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.skusafe.com/
- group: company
  title: ''
  type: Blog
  url: https://skusafe.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://skusafe.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://skusafe.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://skusafe.com/legal/privacy-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.skusafe.com/
coverage:
  checked: '2026-10-29'
  detail: The developer portal at https://app.skusafe.com/ requires login, preventing access to API documentation or contracts.
  evidence:
  - status: 200
    url: https://app.skusafe.com/
  reason: customer-only-docs
  state: gated
created: '2026-10-29'
description: SKUSafe provides AI‑native product lifecycle management (PLM) software tailored for the food, beverage, and supplement industries. The platform unifies specifications, formulations, labeling, approvals, and audit trails in a single system, enabling R&D, quality, and supply‑chain teams to collaborate efficiently. Features include digital sign‑off, multi‑geo label generation, lot traceability, purchase‑order management, and automated compliance reporting. SKUSafe helps companies accelerate product development while maintaining regulatory compliance and improving supply‑chain visibility.
image: https://skusafe.com/assets/skusafe-logo.svg
layout: provider
modified: '2026-10-29'
name: SKUSafe
nav: Providers
network: true
overview: 'SKUSafe is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food, Beverages, Consumer Packaged Goods, and PLM.


  SKUSafe''s developer surface includes engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Skusafe Plans Pricing
  plan_count: 0
  slug: skusafe-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Skusafe Rate Limits
  slug: skusafe-rate-limits
scopes:
- name: Skusafe Scopes
  scope_count: 0
  slug: skusafe-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.1
  facets:
    access_clarity: 19.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 55.4
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 19.9
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/skusafe/skusafe-2026-11-03T143314.png
security:
- kind: authentication
  name: Skusafe Authentication
  slug: skusafe-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Skusafe Domain Security
  slug: skusafe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: skusafe
tags:
- Company
- Food
- Beverages
- Consumer Packaged Goods
- PLM
- Supply Chain
- Quality Management
website: https://www.skusafe.com/
---
