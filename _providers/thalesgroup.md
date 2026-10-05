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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thalesgroup/refs/heads/main/vendors/thalesgroup-vendors.yml
  title: ''
  type: Vendors
  url: vendors/thalesgroup-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.thalesgroup.com/en/global/group/psirt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thalesgroup/refs/heads/main/well-known/thalesgroup-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/thalesgroup-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/thalesgroup/refs/heads/main/well-known/thalesgroup-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/thalesgroup-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thalesgroup/refs/heads/main/hosts/thalesgroup-hosts.yml
  title: ''
  type: Hosts
  url: hosts/thalesgroup-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/thalesgroup/refs/heads/main/packages/thalesgroup-packages.yml
  title: ''
  type: SDKs
  url: packages/thalesgroup-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/thalesgroup/refs/heads/main/packages/thalesgroup-packages.yml
  title: ''
  type: Packages
  url: packages/thalesgroup-packages.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.thalesgroup.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ThalesGroup
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thalesgroup/refs/heads/main/security/thalesgroup-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/thalesgroup-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thalesgroup/refs/heads/main/security/thalesgroup-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thalesgroup-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.thalesgroup.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.thalesgroup.com
  reason: no-developer-program
  state: none
created: '2026-10-03'
description: Thales is a global technology leader providing advanced solutions for aerospace, defense, security, and digital identity. The company designs and integrates cutting‑edge systems ranging from secure communications and cyber‑defense to critical infrastructure protection and digital transformation services. With a presence in over 50 countries, Thales serves governments, enterprises, and individuals, delivering trusted technologies that safeguard data, assets, and people across complex environments.
layout: provider
modified: '2026-10-03'
name: Thales
nav: Providers
network: true
overview: 'Thales is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Aerospace, Defense, and Digital Identity.


  Thales'' developer surface includes documentation and 11 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 44.6
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Thalesgroup Domain Security
  slug: thalesgroup-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Thalesgroup Vulnerability Disclosure
  slug: thalesgroup-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: thalesgroup
tags:
- Company
- Technology
- Aerospace
- Defense
- Digital Identity
website: https://www.thalesgroup.com
---
