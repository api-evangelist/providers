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
- description: Domuso developer resources and API documentation
  name: Domuso API
  slug: domuso-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/domusoinc/conformance/domusoinc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/domusoinc-conformance.yml
- group: agent
  href: https://artifacts.apis.io/domusoinc/llms/domusoinc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/domusoinc-llms.txt
- group: other
  href: https://artifacts.apis.io/domusoinc/hosts/domusoinc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/domusoinc-hosts.yml
- group: other
  href: https://artifacts.apis.io/domusoinc/vendors/domusoinc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/domusoinc-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.domuso.com/categories/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.domuso.com/newsroom
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Domuso
- group: auth
  href: https://artifacts.apis.io/domusoinc/security/domusoinc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/domusoinc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.domuso.com
- group: company
  title: ''
  type: Blog
  url: https://www.domuso.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://www.domuso.com/resources-library
- group: operate
  title: ''
  type: Support
  url: https://www.domuso.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.domuso.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.domuso.com/privacy
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 403
    url: https://api.domuso.com/mcp
  - status: 403
    url: https://auth.domuso.com/mcp
  - status: 200
    url: https://www.domuso.com
  - status: 403
    url: https://equityzen.com/company/domusoinc
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-23'
description: Domusoinc, operating as Domuso, provides a multifamily rent payment platform that modernizes how property managers collect rent, manage resident payments, and boost cash flow through digital payments, rewards, and portfolio insights. The service offers paperless payments, centralized resident reporting, and analytics to improve collection efficiency and resident loyalty.
image: https://cdn.prod.website-files.com/67b5e9c129a2ef6f15816967/685d5263414ff3aff5a820a1_Domuso%20logo%20for%20OG.jpg
layout: provider
modified: '2026-10-23'
name: Domusoinc
nav: Providers
network: true
overview: 'Domusoinc is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Property Management, Payments, Software-as-a-Service, and Real Estate.


  Domusoinc''s developer surface includes engineering blog, documentation, support, and 11 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 58.9
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Domusoinc Domain Security
  slug: domusoinc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: domusoinc
tags:
- Company
- Property Management
- Payments
- Software-as-a-Service
- Real Estate
website: https://www.domuso.com
---
