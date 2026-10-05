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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bookkeeping-express/refs/heads/main/plans/bookkeeping-express-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bookkeeping-express-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bookkeeping-express/refs/heads/main/hosts/bookkeeping-express-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bookkeeping-express-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bookkeeping-express/refs/heads/main/vendors/bookkeeping-express-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bookkeeping-express-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bookkeepingexpress.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://bookkeepingexpress.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://bookkeepingexpress.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bookkeeping-express/refs/heads/main/security/bookkeeping-express-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bookkeeping-express-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bookkeepingexpress.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://bookkeepingexpress.com/mcp
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-02'
description: Bookkeeping Express (BKE) provides monthly bookkeeping and financial coaching services for franchise owners and small‑medium businesses. Their platform reconciles books, delivers actionable insights via FinalyzeIQ, and offers fixed‑price plans with senior accountant access. BKE emphasizes security, confidentiality, and U.S.-based accountants, aiming to help clients grow profitably through data‑driven recommendations.
image: https://bookkeepingexpress.com/wp-content/uploads/2026/07/Screenshot-2026-07-03-164620.png
layout: provider
modified: '2026-10-02'
name: BookKeeping Express
nav: Providers
network: true
overview: 'BookKeeping Express is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Bookkeeping, Financial Coaching, Small Business, and Software-as-a-Service.


  BookKeeping Express'' developer surface includes pricing, engineering blog, and 6 more developer resources.'
plans:
- name: Bookkeeping Express Plans Pricing
  plan_count: 1
  slug: bookkeeping-express-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bookkeeping Express Domain Security
  slug: bookkeeping-express-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bookkeeping-express
tags:
- Company
- Bookkeeping
- Financial Coaching
- Small Business
- Software-as-a-Service
website: https://bookkeepingexpress.com
---
