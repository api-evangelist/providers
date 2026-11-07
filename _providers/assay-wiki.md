---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
  score: 17.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Assay Wiki platform, providing access to integrations and data.
  name: Assay Wiki API
  slug: assay-wiki-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/assay-wiki/plans/assay-wiki-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/assay-wiki-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/assay-wiki/changelog/assay-wiki-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/assay-wiki-changelog.yml
- group: agent
  href: https://artifacts.apis.io/assay-wiki/llms/assay-wiki-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/assay-wiki-llms.txt
- group: agent
  href: https://artifacts.apis.io/assay-wiki/well-known/assay-wiki-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/assay-wiki-well-known.yml
- group: other
  href: https://artifacts.apis.io/assay-wiki/hosts/assay-wiki-hosts.yml
  title: ''
  type: Hosts
  url: hosts/assay-wiki-hosts.yml
- group: other
  href: https://artifacts.apis.io/assay-wiki/vendors/assay-wiki-vendors.yml
  title: ''
  type: Vendors
  url: vendors/assay-wiki-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://assay.wiki/legal/terms/
- group: auth
  title: ''
  type: Security
  url: https://assay.wiki/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://assay.wiki/legal/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://assay.wiki/press/
- group: start
  title: ''
  type: Login
  url: https://app.assay.wiki/sign-in
- group: operate
  title: ''
  type: ChangeLog
  url: https://assay.wiki/changelog/
- group: auth
  href: https://artifacts.apis.io/assay-wiki/security/assay-wiki-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/assay-wiki-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://assay.wiki/
- group: company
  title: ''
  type: Blog
  url: https://assay.wiki/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://assay.wiki/pricing/
coverage:
  checked: '2026-11-02'
  detail: OpenAPI spec URLs redirect to sign‑in page, requiring authentication.
  evidence:
  - status: 307
    url: https://app.assay.wiki/openapi.json
  reason: auth-required
  state: gated
created: '2026-11-01'
description: Assay finds what''s gone out of date across your site, blog, and decks, and has the fix ready for your approval. Nothing publishes, sends, or spends on its own. The platform offers AI SEO & GEO, AI Product Marketer, pricing, resources, changelog, security, integrations, and a free truth graph.
image: https://assay.wiki/assay-v4-social-preview.png
layout: provider
modified: '2026-11-01'
name: Assay
nav: Providers
network: true
overview: 'Assay is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Content Management, Marketing, Automation, and SEO.


  Assay''s developer surface includes changelog, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Assay Wiki Plans Pricing
  plan_count: 1
  slug: assay-wiki-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Assay Wiki Rate Limits
  slug: assay-wiki-rate-limits
scopes:
- name: Assay Wiki Scopes
  scope_count: 0
  slug: assay-wiki-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.1
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 58.0
    operational_transparency: 13.2
  previous_composite: 24.8
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Assay Wiki Authentication
  slug: assay-wiki-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Assay Wiki Domain Security
  slug: assay-wiki-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: assay-wiki
tags:
- Artificial Intelligence
- Content Management
- Marketing
- Automation
- SEO
website: https://assay.wiki/
---
