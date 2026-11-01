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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/wirescreen/hosts/wirescreen-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wirescreen-hosts.yml
- group: other
  href: https://artifacts.apis.io/wirescreen/vendors/wirescreen-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wirescreen-vendors.yml
- group: auth
  href: https://artifacts.apis.io/wirescreen/security/wirescreen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wirescreen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wirescreen.ai
- group: docs
  title: ''
  type: Documentation
  url: https://wirescreen.ai/about-us
- group: docs
  title: ''
  type: APIReference
  url: https://platform.wirescreen.ai/platform
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wirescreen.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wirescreen.ai/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://wirescreen.ai/press
- group: commercial
  title: ''
  type: Pricing
  url: https://wirescreen.ai/bis-50-rule
coverage:
  checked: '2026-10-29'
  detail: Docs require login via a password page at https://docs.wirescreen.ai/password?redirect=%2F
  evidence:
  - status: 200
    url: https://docs.wirescreen.ai/password?redirect=%2F
  reason: customer-only-docs
  state: gated
created: '2026-10-29'
description: WireScreen provides intelligence and insight on China’s business landscape, offering risk intelligence, compliance analysis, and detailed corporate network mapping. Their platform aggregates public and proprietary data to uncover hidden ownership, supply chains, and corporate connections, serving national security, defense, export controls, and commercial clients seeking deep China market understanding.
image: https://cdn.prod.website-files.com/64931623777f43bb5c1e709f/6a885ed255f0cb34a3aca3ec_open%20graph%20logo.png
layout: provider
modified: '2026-10-29'
name: WireScreen
nav: Providers
network: true
overview: 'WireScreen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Business, Intelligence, China, and Risk.


  WireScreen''s developer surface includes documentation, API reference, engineering blog, pricing, and 6 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Wirescreen Domain Security
  slug: wirescreen-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: wirescreen
tags:
- Company
- Business
- Intelligence
- China
- Risk
- Compliance
website: https://www.wirescreen.ai
---
