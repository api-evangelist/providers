---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: operate
  href: https://artifacts.apis.io/deltek/changelog/deltek-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/deltek-changelog.yml
- group: agent
  href: https://artifacts.apis.io/deltek/well-known/deltek-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deltek-well-known.yml
- group: other
  href: https://artifacts.apis.io/deltek/hosts/deltek-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deltek-hosts.yml
- group: other
  href: https://artifacts.apis.io/deltek/vendors/deltek-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deltek-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.deltek.com/
- group: auth
  title: ''
  type: Security
  url: https://www.deltek.com/company/security-and-trust/security/
- group: company
  title: ''
  type: Newsroom
  url: https://www.deltek.com/company/news/
- group: start
  title: ''
  type: Login
  url: https://www.deltek.com/login/
- group: other
  title: ''
  type: Leadership
  url: https://www.deltek.com/company/leadership/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.deltek.com/company/news/deltek-takes-home-silver-brandon-hall-group-award-for-its-new-hire-onboarding-program/
- group: auth
  href: https://artifacts.apis.io/deltek/security/deltek-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deltek-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.deltek.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.deltek.com/resources/
- group: company
  title: ''
  type: Blog
  url: https://www.deltek.com/resources/articles/
- group: operate
  title: ''
  type: Support
  url: https://deltek.custhelp.com/
- group: start
  title: ''
  type: PartnerPortal
  url: https://deltek.my.site.com/prm/s/login/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.deltek.com/products/propricer/
coverage:
  checked: '2026-10-27'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications were found on Deltek's documented sites.
  evidence:
  - status: 200
    url: https://www.deltek.com/resources/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Deltek provides enterprise software solutions for project-driven work, offering platforms such as Deltek Vantagepoint, Costpoint, and GovWin. Their tools help organizations manage projects, resources, finances, and compliance, delivering speed, clarity, and control throughout the project lifecycle. The company serves government contractors, professional services firms, and other high‑stakes industries with integrated, purpose‑built applications.
image: https://www.deltek.com/globalassets/homepage/deltek-social-share.png
layout: provider
modified: '2026-10-26'
name: Deltek
nav: Providers
network: true
overview: 'Deltek is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software, Enterprise, Project Management, and Government.


  Deltek''s developer surface includes changelog, getting-started guide, documentation, engineering blog, support, pricing, and 11 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 15.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 19.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    operational_transparency: 21.1
  previous_composite: 21.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/deltek/deltek-2026-11-03T130515.png
security:
- kind: domain-security
  name: Deltek Domain Security
  slug: deltek-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: deltek
tags:
- Company
- Software
- Enterprise
- Project Management
- Government
website: https://www.deltek.com/
---
