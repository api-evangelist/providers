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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.8
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/seagate/refs/heads/main/changelog/seagate-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/seagate-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/seagate/refs/heads/main/well-known/seagate-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/seagate-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/seagate/refs/heads/main/hosts/seagate-hosts.yml
  title: ''
  type: Hosts
  url: hosts/seagate-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/seagate/refs/heads/main/vendors/seagate-vendors.yml
  title: ''
  type: Vendors
  url: vendors/seagate-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.seagate.com/trust/
- group: operate
  title: ''
  type: Support
  url: https://www.seagate.com/support/
- group: auth
  title: ''
  type: Security
  url: https://www.seagate.com/manuals/lyve-drive-shuttle/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.seagate.com/legal/privacy/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://alumni.seagate.com/login/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.seagate.com/products/whats-new/
- group: company
  title: ''
  type: Blog
  url: https://www.seagate.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.seagate.com/support/kb/maxtor-central-axis-quickstart-2799en/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/seagate/refs/heads/main/security/seagate-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/seagate-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/seagate/refs/heads/main/security/seagate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/seagate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.seagate.com
coverage:
  detail: No public developer program or API documentation was found on seagate.com or its subdomains.
  evidence:
  - status: 404
    url: https://api.seagate.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Seagate is a global leader in data storage solutions, providing a wide range of hard disk drives, solid-state drives, and enterprise storage systems for consumers, businesses, and data centers. The company focuses on high-capacity, high-performance storage technologies, supporting cloud, AI, and big data workloads worldwide.
image: https://www.seagate.com/content/dam/seagate/assets/esg/images/seagate-office-building.jpg
layout: provider
modified: '2026-10-13'
name: Seagate
nav: Providers
network: true
overview: 'Seagate is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Storage, Data, Enterprise, and Technology.


  Seagate''s developer surface includes changelog, support, engineering blog, getting-started guide, and 11 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 20.1
  coverage:
    artifact_dirs: 5
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
    operational_transparency: 26.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Seagate Domain Security
  slug: seagate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Seagate Vulnerability Disclosure
  slug: seagate-vulnerability-disclosure
  summary_line: no policy recorded
slug: seagate
tags:
- Company
- Storage
- Data
- Enterprise
- Technology
website: https://www.seagate.com
---
