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
  href: https://artifacts.apis.io/desec/security/desec-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/desec-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/desec/well-known/desec-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/desec-security.txt
- group: agent
  href: https://artifacts.apis.io/desec/well-known/desec-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/desec-well-known.yml
- group: other
  href: https://artifacts.apis.io/desec/hosts/desec-hosts.yml
  title: ''
  type: Hosts
  url: hosts/desec-hosts.yml
- group: other
  href: https://artifacts.apis.io/desec/vendors/desec-vendors.yml
  title: ''
  type: Vendors
  url: vendors/desec-vendors.yml
- group: build
  href: https://artifacts.apis.io/desec/packages/desec-packages.yml
  title: ''
  type: SDKs
  url: packages/desec-packages.yml
- group: build
  href: https://artifacts.apis.io/desec/packages/desec-packages.yml
  title: ''
  type: Packages
  url: packages/desec-packages.yml
- group: auth
  href: https://artifacts.apis.io/desec/security/desec-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/desec-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/desec/security/desec-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/desec-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://desec.io/
- group: docs
  title: ''
  type: Documentation
  url: https://desec.readthedocs.io/en/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://desec.readthedocs.io/en/latest/endpoint-reference.html
- group: start
  title: ''
  type: GettingStarted
  url: https://desec.readthedocs.io/en/latest/quickstart.html
created: '2026-10-27'
description: deSEC provides free, secure DNS hosting with a focus on privacy and security. It offers a modern DNS service that includes DNSSEC, API access for automation, and a user-friendly control panel. The service is open-source, supported by System Security Engineering, and aims to give everyone reliable DNS without cost.
layout: provider
modified: '2026-10-27'
name: deSEC
nav: Providers
network: true
overview: 'deSEC is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include DNS, Security, OpenSource, FreeService, and Company.


  deSEC''s developer surface includes documentation, API reference, getting-started guide, and 10 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 12.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 44.6
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Desec Domain Security
  slug: desec-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Desec Vulnerability Disclosure
  slug: desec-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: desec
tags:
- DNS
- Security
- OpenSource
- FreeService
- Company
website: https://desec.io/
---
