---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: GraphQL API for Better Health Supplies
  name: Better Health API
  slug: better-health-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/better-health-supplies-inc/refs/heads/main/llms/better-health-supplies-inc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/better-health-supplies-inc-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/better-health-supplies-inc/refs/heads/main/well-known/better-health-supplies-inc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/better-health-supplies-inc-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/better-health-supplies-inc/refs/heads/main/hosts/better-health-supplies-inc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/better-health-supplies-inc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/better-health-supplies-inc/refs/heads/main/vendors/better-health-supplies-inc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/better-health-supplies-inc-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://joinbetter.com/pages/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://joinbetter.com/pages/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://joinbetter.com/pages/press
- group: company
  title: ''
  type: Blog
  url: https://blog.joinbetter.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/better-health-supplies-inc/refs/heads/main/security/better-health-supplies-inc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/better-health-supplies-inc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://joinbetter.com/
created: '2026-09-28'
description: Better Health Supplies, Inc. (Better Health) is a modern medical supply e‑commerce company that provides a wide range of products for diabetes, incontinence, urology, ostomy, and wound care. It operates an online storefront offering continuous glucose monitors, catheters, ostomy bags, and related accessories, serving both consumers and healthcare professionals across the United States.
image: http://joinbetter.com/cdn/shop/files/better-health-bg_1200x1200.png?v=1747645316
layout: provider
modified: '2026-09-28'
name: Better Health Supplies, Inc.
nav: Providers
network: true
overview: 'Better Health Supplies, Inc. publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Medical Supplies, E-Commerce, and Diabetes.


  Better Health Supplies, Inc.''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 75.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Better Health Supplies Inc Domain Security
  slug: better-health-supplies-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: better-health-supplies-inc
tags:
- Company
- Healthcare
- Medical Supplies
- E-Commerce
- Diabetes
- Urology
website: https://joinbetter.com/
---
