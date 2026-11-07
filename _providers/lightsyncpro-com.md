---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
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
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MCP (Model Context Protocol) API for LightSync Pro, providing AI‑assistant integration and asset synchronization. Documentation at https://lightsyncpro.com/docs/mcp/.
  name: LightSync Pro MCP API
  slug: lightsync-pro-mcp-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/lightsyncpro-com/plans/lightsyncpro-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lightsyncpro-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/lightsyncpro-com/changelog/lightsyncpro-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/lightsyncpro-com-changelog.yml
- group: agent
  href: https://artifacts.apis.io/lightsyncpro-com/llms/lightsyncpro-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lightsyncpro-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/lightsyncpro-com/well-known/lightsyncpro-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lightsyncpro-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/lightsyncpro-com/hosts/lightsyncpro-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lightsyncpro-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/lightsyncpro-com/vendors/lightsyncpro-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lightsyncpro-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/lightsyncpro-com/packages/lightsyncpro-com-packages.yml
  title: ''
  type: SDKs
  url: packages/lightsyncpro-com-packages.yml
- group: build
  href: https://artifacts.apis.io/lightsyncpro-com/packages/lightsyncpro-com-packages.yml
  title: ''
  type: Packages
  url: packages/lightsyncpro-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lightsyncpro.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://lightsyncpro.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lightsyncpro.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://lightsyncpro.com/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://lightsyncpro.com/docs/
- group: operate
  title: ''
  type: ChangeLog
  url: https://lightsyncpro.com/changelog/
- group: start
  title: ''
  type: GettingStarted
  url: https://lightsyncpro.com/docs-category/getting-started/
- group: auth
  href: https://artifacts.apis.io/lightsyncpro-com/security/lightsyncpro-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lightsyncpro-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lightsyncpro.com/
coverage:
  checked: '2026-10-30'
  detail: API requires authentication via OAuth; public well-known document points to a protected MCP endpoint.
  evidence:
  - status: 200
    url: https://lightsyncpro.com/.well-known/oauth-protected-resource
  reason: partner-login
  state: gated
created: '2026-10-30'
description: LightSync Pro enables automatic synchronization of Adobe Lightroom, Figma, Dropbox, Shutterstock, Canva, and other media sources to WordPress and Shopify sites. It adds AI‑generated images via OpenRouter and extends syncing to Google Drive, OneDrive, HubSpot, Contentful, Webflow, and a generic HTTP API, offering a low‑code solution for content creators and e‑commerce merchants.
image: https://lightsyncpro.com/wp-content/uploads/2021/06/lightsyncpro-logo-2.png
layout: provider
modified: '2026-10-30'
name: lightsyncpro-com
nav: Providers
network: true
overview: 'lightsyncpro-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automation, WordPress, Shopify, and Sync.


  lightsyncpro-com''s developer surface includes changelog, support, pricing, documentation, getting-started guide, and 12 more developer resources.'
plans:
- name: Lightsyncpro Com Plans Pricing
  plan_count: 2
  slug: lightsyncpro-com-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Lightsyncpro Com Rate Limits
  slug: lightsyncpro-com-rate-limits
scopes:
- name: Lightsyncpro Com Scopes
  scope_count: 0
  slug: lightsyncpro-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 21.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.4
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 73.2
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 28.7
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/lightsyncpro-com/lightsyncpro-com-2026-11-03T134901.png
security:
- kind: authentication
  name: Lightsyncpro Com Authentication
  slug: lightsyncpro-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Lightsyncpro Com Domain Security
  slug: lightsyncpro-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: lightsyncpro-com
tags:
- Company
- Automation
- WordPress
- Shopify
- Sync
website: https://lightsyncpro.com/
---
