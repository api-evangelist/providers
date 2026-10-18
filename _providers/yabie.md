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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Yabie's API documentation is hosted on their support site covering product integration.
  name: Yabie API
  slug: yabie-api
artifact_total: 3
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/yabie/refs/heads/main/vendors/yabie-vendors.yml
  title: ''
  type: Vendors
  url: vendors/yabie-vendors.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/yabie/refs/heads/main/changelog/yabie-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/yabie-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/yabie/refs/heads/main/llms/yabie-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/yabie-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/yabie/refs/heads/main/well-known/yabie-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/yabie-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/yabie/refs/heads/main/well-known/yabie-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/yabie-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/yabie/refs/heads/main/hosts/yabie-hosts.yml
  title: ''
  type: Hosts
  url: hosts/yabie-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://support.yabie.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.yabie.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://yabie.com/legal/privacy/
- group: docs
  title: ''
  type: Documentation
  url: https://support.yabie.com/docs/lager
- group: company
  title: ''
  type: Blog
  url: https://blog.yabie.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/yabie/refs/heads/main/security/yabie-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/yabie-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/yabie/refs/heads/main/security/yabie-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yabie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://yabie.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://api.yabie.com/mcp
  - status: 403
    url: https://yabie.com/mcp
  - status: 403
    url: https://blog.yabie.com/mcp
  - status: 403
    url: https://shop.yabie.com/mcp
  - status: 200
    url: https://yabie.com/
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: Yabie is a technology company focused on providing innovative solutions in the digital marketplace. It aims to connect businesses with advanced API-driven services, enhancing integration capabilities and streamlining workflows across various industries. The company emphasizes scalability, security, and developer-friendly tools to foster ecosystem growth and enable seamless data exchange.
image: https://yabie.com/wp-content/uploads/2023/08/Utvald-3.jpg
layout: provider
modified: '2026-10-15'
name: Yabie
nav: Providers
network: true
overview: 'Yabie is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Yabie''s developer surface includes changelog, support, documentation, engineering blog, and 10 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 55.4
    operational_transparency: 31.6
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Yabie Domain Security
  slug: yabie-domain-security
  summary_line: DMARC
- kind: trust-center
  name: Yabie Trust Center
  slug: yabie-trust-center
  summary_line: trust center published
slug: yabie
tags:
- Company
website: https://yabie.com/
---
