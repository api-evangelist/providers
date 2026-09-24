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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-09-24'
api_count: 1
apis:
- description: Membrain provides a sales enablement platform with APIs for prospecting, pipeline management, and analytics.
  name: Membrain Platform API
  slug: platform
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/membrain/refs/heads/main/plans/membrain-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/membrain-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/membrain/refs/heads/main/well-known/membrain-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/membrain-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/membrain/refs/heads/main/hosts/membrain-hosts.yml
  title: ''
  type: Hosts
  url: hosts/membrain-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/membrain/refs/heads/main/vendors/membrain-vendors.yml
  title: ''
  type: Vendors
  url: vendors/membrain-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.membrain.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/membrain/refs/heads/main/security/membrain-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/membrain-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://membrain.com/
- group: company
  title: ''
  type: Blog
  url: https://www.membrain.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.membrain.com/sales-coaching-assessment?hsLang=en
- group: start
  title: ''
  type: Login
  url: https://go.membrain.com/WebsiteLogin/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.membrain.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.membrain.com/legal/privacy-policy?hsLang=en
- group: operate
  title: ''
  type: Support
  url: https://www.membrain.com/help-center/?hsLang=en
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.membrain.com/website-terms-of-use?hsLang=en
coverage:
  checked: 2026-09-22
  detail: API documentation requires login via developer portal
  evidence:
  - status: 200
    url: https://developer.membrain.com/Login.aspx
  reason: customer-only-docs
  state: gated
created: '2026-09-22'
description: Membrain is a B2B growth platform that helps sales teams improve prospecting, pipeline management, account growth, and overall sales performance. It offers built-in tools, analytics, automation, and integrations to streamline the sales process, providing resources such as blogs, webinars, whitepapers, and a partner ecosystem. The platform targets sales managers, reps, marketing, HR, manufacturing, and MSPs, delivering a comprehensive solution for modern selling.
image: https://www.membrain.com/hubfs/Featured%20image-Membrain.png
layout: provider
modified: '2026-09-22'
name: Membrain
nav: Providers
network: true
overview: 'Membrain publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales, B2B, Platform, and CRM.


  Membrain''s developer surface includes documentation, engineering blog, getting-started guide, pricing, support, and 9 more developer resources.'
plans:
- name: Membrain Plans Pricing
  plan_count: 2
  slug: membrain-plans-pricing
random_paper: 7
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 59.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Membrain Domain Security
  slug: membrain-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: membrain
tags:
- Company
- Sales
- B2B
- Platform
- CRM
website: https://membrain.com/
---
