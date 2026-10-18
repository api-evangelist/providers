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
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: phoenixNAP provides cloud infrastructure and data center services.
  name: phoenixNAP API
  slug: phoenixnap-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/phoenixnap/refs/heads/main/well-known/phoenixnap-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/phoenixnap-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/phoenixnap/refs/heads/main/hosts/phoenixnap-hosts.yml
  title: ''
  type: Hosts
  url: hosts/phoenixnap-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/phoenixnap/refs/heads/main/vendors/phoenixnap-vendors.yml
  title: ''
  type: Vendors
  url: vendors/phoenixnap-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/phoenixnap/refs/heads/main/packages/phoenixnap-packages.yml
  title: ''
  type: SDKs
  url: packages/phoenixnap-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/phoenixnap/refs/heads/main/packages/phoenixnap-packages.yml
  title: ''
  type: Packages
  url: packages/phoenixnap-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://phoenixnap.com/security/data-security-cloud
- group: company
  title: ''
  type: Newsroom
  url: https://phoenixnap.com/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/phoenixnap
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.phoenixnap.com/quick-start
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/phoenixnap/refs/heads/main/security/phoenixnap-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/phoenixnap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://phoenixnap.com
- group: docs
  title: ''
  type: Documentation
  url: https://phoenixnap.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://phoenixnap.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://phoenixnap.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://phoenixnap.com/signup
coverage:
  checked: '2026-10-14'
  detail: Documentation pages return 403 HTML preventing machine-readable spec discovery.
  evidence:
  - status: 403
    url: https://phoenixnap.com/docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-14'
description: phoenixNAP is a global IT services provider offering a diverse portfolio of data center and cloud infrastructure solutions. Founded in 2009, it operates multiple data centers worldwide, delivering IaaS, dedicated servers, colocation, and managed services to enterprises and developers. The company emphasizes high performance, security, and scalability, supporting a range of workloads from web hosting to complex enterprise applications.
image: https://phoenixnap.com/wp-content/uploads/2019/10/pnap-favicon.png
layout: provider
modified: '2026-10-14'
name: phoenixNAP
nav: Providers
network: true
overview: 'phoenixNAP is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud, Infrastructure-as-a-Service, DataCenter, and ManagedServices.


  phoenixNAP''s developer surface includes getting-started guide, documentation, pricing, engineering blog, signup flow, and 10 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 58.9
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Phoenixnap Domain Security
  slug: phoenixnap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: phoenixnap
tags:
- Company
- Cloud
- Infrastructure-as-a-Service
- DataCenter
- ManagedServices
website: https://phoenixnap.com
---
