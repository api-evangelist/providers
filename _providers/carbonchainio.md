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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.carbonchain.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.carbonchain.com/security
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carbonchainio/refs/heads/main/conformance/carbonchainio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/carbonchainio-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carbonchainio/refs/heads/main/hosts/carbonchainio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carbonchainio-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carbonchainio/refs/heads/main/vendors/carbonchainio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carbonchainio-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.carbonchain.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.carbonchain.com/news
- group: start
  title: ''
  type: GettingStarted
  url: https://www.carbonchain.com/faq-onboarding
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/carbonchain
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carbonchainio/refs/heads/main/security/carbonchainio-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/carbonchainio-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carbonchainio/refs/heads/main/security/carbonchainio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carbonchainio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.carbonchain.com
- group: operate
  title: ''
  type: Support
  url: https://www.carbonchain.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.carbonchain.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.carbonchain.com/cbam/signup
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/carbonchain/workspace
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.carbonchain.com
  - status: 403
    url: https://equityzen.com/company/carbonchainio
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: CarbonChain provides a carbon accounting platform for supply chain emissions, offering tools for tracking, reporting, and reducing carbon footprints across industries. The service integrates with ERP and trading systems, supports CBAM compliance, and delivers detailed emissions data to help companies meet sustainability goals and financing requirements.
image: https://cdn.prod.website-files.com/64e7434965d4aee07569d277/650defc3fd884acf66f96186_OG%20Option%202.png
layout: provider
modified: '2026-10-07'
name: Carbonchainio
nav: Providers
network: true
overview: 'Carbonchainio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Carbon Accounting, Supply Chain, Sustainability, Emissions, and CBAM.


  Carbonchainio''s developer surface includes getting-started guide, support, engineering blog, signup flow, and 12 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 22.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 50.0
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carbonchainio Domain Security
  slug: carbonchainio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Carbonchainio Trust Center
  slug: carbonchainio-trust-center
  summary_line: SOC 2, ISO 27001
slug: carbonchainio
tags:
- Carbon Accounting
- Supply Chain
- Sustainability
- Emissions
- CBAM
website: https://www.carbonchain.com
---
