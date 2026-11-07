---
access_model:
  confidence: low
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: docs
  title: ''
  type: Documentation
  url: https://help.zenchef.com/
- group: other
  href: https://artifacts.apis.io/zenchef/hosts/zenchef-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zenchef-hosts.yml
- group: other
  href: https://artifacts.apis.io/zenchef/vendors/zenchef-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zenchef-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zenchef.com/legal-notice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zenchef.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.zenchef.com/release-notes
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zenchef
- group: auth
  href: https://artifacts.apis.io/zenchef/security/zenchef-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zenchef-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zenchef.com/
- group: operate
  title: ''
  type: Support
  url: https://www.zenchef.com/contact
- group: company
  title: ''
  type: Blog
  url: https://blog.zenchef.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zenchef.com/plans
coverage:
  checked: '2026-10-28'
  detail: The documentation pages are rendered via JavaScript and no machine‑readable OpenAPI, AsyncAPI, GraphQL or other contract was found.
  evidence:
  - status: 200
    url: https://www.zenchef.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Zenchef provides an all‑in‑one restaurant management platform that handles reservations, table management, payments, guest communication, and analytics. Their SaaS solution helps restaurants reduce no‑shows, fill last‑minute tables, and improve revenue through integrated booking, AI‑driven tools, and a guest‑facing app. The platform serves individual venues and groups, offering customizable branding, multi‑location oversight, and a marketplace of integrations for POS, marketing, and loyalty systems.
image: https://cdn.prod.website-files.com/6572fc8832fc5d79f0c6feda/65a15d27dd94e60c14066e42_2311_OBOP_Mainvisual.png
layout: provider
modified: '2026-10-28'
name: Zenchef
nav: Providers
network: true
overview: 'Zenchef is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Restaurant, Software-as-a-Service, Reservations, Payments, and Analytics.


  Zenchef''s developer surface includes documentation, changelog, support, engineering blog, pricing, and 7 more developer resources.'
plans:
- name: Zenchef Plans
  plan_count: 3
  slug: zenchef-plans
random_paper: 19
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.8
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 48.2
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 22.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 8.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/zenchef/zenchef-2026-11-03T150447.png
security:
- kind: domain-security
  name: Zenchef Domain Security
  slug: zenchef-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zenchef
tags:
- Restaurant
- Software-as-a-Service
- Reservations
- Payments
- Analytics
- Company
website: https://zenchef.com/
---
