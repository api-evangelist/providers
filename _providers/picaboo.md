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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Picaboo provides an API for creating photobooks, managing orders, and accessing product catalogs.
  name: Picaboo API
  slug: picaboo-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/picaboo/vendors/picaboo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/picaboo-vendors.yml
- group: other
  href: https://artifacts.apis.io/picaboo/hosts/picaboo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/picaboo-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.picaboo.com/terms/
- group: start
  title: ''
  type: SignUp
  url: https://auth.picaboo.com/signup?client_id=77fhk924ao6nc3ut64g85tfj5d&response_type=code&scope=email+openid+phone+profile&redirect_uri=https%3A%2F%2Fapp.picaboo.com%2FServerYB%2FStore%2FAccountDetail.ashx&state=https%3A%2F%2Fwww.picaboo.com%2F
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.picaboo.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.picaboo.com/pricing/
- group: auth
  href: https://artifacts.apis.io/picaboo/security/picaboo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/picaboo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.picaboo.com/
coverage:
  checked: '2026-10-22'
  detail: Main website is a WordPress site with JavaScript‑rendered content, no machine‑readable API spec discovered.
  evidence:
  - status: 200
    url: https://www.picaboo.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: Picaboo provides an online platform for creating and ordering custom photobooks, prints, and photo gifts. Users can upload photos, design layouts with templates, and purchase high‑quality printed products. The service targets both consumers and professional photographers, offering tools for photo management, sharing, and e‑commerce integration. Picaboo emphasizes ease of use, fast turnaround, and a variety of product options, positioning itself as a leading digital photo‑book and print provider.
image: https://www.picaboo.com/wp-content/uploads/Today.png
layout: provider
modified: '2026-10-22'
name: Picaboo
nav: Providers
network: true
overview: 'Picaboo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Photo, Printing, E-commerce, and SaaS.


  Picaboo''s developer surface includes signup flow, pricing, and 6 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Picaboo Domain Security
  slug: picaboo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: picaboo
tags:
- Company
- Photo
- Printing
- E-commerce
- SaaS
website: https://www.picaboo.com/
---
