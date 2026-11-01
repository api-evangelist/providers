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
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.pigment.com/security
- group: agent
  href: https://artifacts.apis.io/gopigment-com/llms/gopigment-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gopigment-com-llms.txt
- group: other
  href: https://artifacts.apis.io/gopigment-com/hosts/gopigment-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gopigment-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/gopigment-com/vendors/gopigment-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gopigment-com-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.pigment.com/trial/sign-up
- group: auth
  title: ''
  type: Security
  url: https://www.pigment.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pigment.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.pigment.com/newsroom
- group: auth
  href: https://artifacts.apis.io/gopigment-com/security/gopigment-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/gopigment-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/gopigment-com/security/gopigment-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gopigment-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pigment.com/
- group: company
  title: ''
  type: Blog
  url: https://www.pigment.com/blog
- group: operate
  title: ''
  type: Roadmap
  url: https://www.pigment.com/roadmap
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://community.gopigment.com/mcp
  - status: 200
    url: https://www.gopigment.com/
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Pigment provides a modern data platform that enables businesses to integrate, model, and visualize data from multiple sources in a collaborative environment. The platform offers powerful data transformation, analytics, and visualization tools, allowing teams to build data-driven applications and dashboards without extensive coding. Pigment serves enterprises across finance, retail, and technology sectors, focusing on data governance, security, and scalability to support complex data workflows and decision-making processes.
image: https://cdn.prod.website-files.com/6605b12132f6a8b5d23896bd/66d863e42d71cb716b67d825_Pigment%20-%20Prepare%20for%20anything.jpg
layout: provider
modified: '2026-10-22'
name: Pigment
nav: Providers
network: true
overview: 'Pigment is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Platform, Analytics, Visualization, and Collaboration.


  Pigment''s developer surface includes signup flow, engineering blog, and 11 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 15.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Gopigment Com Domain Security
  slug: gopigment-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Gopigment Com Trust Center
  slug: gopigment-com-trust-center
  summary_line: SOC 2, GDPR
slug: gopigment-com
tags:
- Company
- Data Platform
- Analytics
- Visualization
- Collaboration
website: https://www.pigment.com/
---
