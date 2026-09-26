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
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/globalstar/refs/heads/main/well-known/globalstar-globalstar-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/globalstar-globalstar-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/globalstar/refs/heads/main/well-known/globalstar-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/globalstar-status-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/globalstar/refs/heads/main/well-known/globalstar-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/globalstar-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/globalstar/refs/heads/main/well-known/globalstar-partner-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/globalstar-partner-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/globalstar/refs/heads/main/well-known/globalstar-myaccount-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/globalstar-myaccount-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/globalstar/refs/heads/main/well-known/globalstar-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/globalstar-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/globalstar/refs/heads/main/hosts/globalstar-hosts.yml
  title: ''
  type: Hosts
  url: hosts/globalstar-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/globalstar/refs/heads/main/vendors/globalstar-vendors.yml
  title: ''
  type: Vendors
  url: vendors/globalstar-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.globalstar.com/
- group: operate
  title: ''
  type: Support
  url: https://www.globalstar.com/support/patents
- group: operate
  title: ''
  type: StatusPage
  url: https://status.globalstar.com/access/login
- group: auth
  title: ''
  type: Security
  url: https://www.globalstar.com/support/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.globalstar.com/support/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.globalstar.com/en-us/about/news
- group: company
  title: ''
  type: Blog
  url: https://blog.globalstar.com/globalstar-blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/globalstar
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/globalstar/refs/heads/main/security/globalstar-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/globalstar-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/globalstar/refs/heads/main/security/globalstar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/globalstar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://globalstar.com/
coverage:
  checked: 2026-09-23
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found at the API host.
  evidence:
  - status: 0
    url: https://api.globalstar.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-23'
description: Globalstar provides satellite communications solutions, offering voice and data services for a range of industries including IoT, emergency response, and enterprise mobility. Their platform delivers always‑on connectivity through a global network of low‑earth‑orbit satellites, enabling tracking, monitoring, and two‑way communication for devices and personnel in remote locations.
image: https://www.globalstar.com/getmedia/e349d929-0e2e-4d24-9481-4567e02ce472/globalstar-share.png
layout: provider
modified: '2026-09-23'
name: Globalstar
nav: Providers
network: true
overview: 'Globalstar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Satellite, Communications, IoT, and Enterprise.


  Globalstar''s developer surface includes support, engineering blog, and 17 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 31.6
  previous_composite: 14.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Globalstar Domain Security
  slug: globalstar-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Globalstar Vulnerability Disclosure
  slug: globalstar-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: globalstar
tags:
- Company
- Satellite
- Communications
- IoT
- Enterprise
website: https://globalstar.com/
---
