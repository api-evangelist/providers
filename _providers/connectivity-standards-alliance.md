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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Developer Resources - CSA-IOT
  name: Connectivity Standards Alliance API
  slug: connectivity-standards-alliance-api
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/connectivity-standards-alliance/refs/heads/main/well-known/connectivity-standards-alliance-community-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/connectivity-standards-alliance-community-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/connectivity-standards-alliance/refs/heads/main/well-known/connectivity-standards-alliance-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/connectivity-standards-alliance-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/connectivity-standards-alliance/refs/heads/main/hosts/connectivity-standards-alliance-hosts.yml
  title: ''
  type: Hosts
  url: hosts/connectivity-standards-alliance-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/connectivity-standards-alliance/refs/heads/main/vendors/connectivity-standards-alliance-vendors.yml
  title: ''
  type: Vendors
  url: vendors/connectivity-standards-alliance-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://csa-iot.org/resources/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://csa-iot.org/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://community.csa-iot.org/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/csa-iot
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/connectivity-standards-alliance/refs/heads/main/security/connectivity-standards-alliance-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/connectivity-standards-alliance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://csa-iot.org
- group: docs
  title: ''
  type: Documentation
  url: https://csa-iot.org/resources/developer-resources/
- group: operate
  title: ''
  type: Support
  url: https://csa-iot.org/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://csa-iot.org/newsroom/
coverage:
  checked: '2026-10-13'
  detail: The developer resources page provides HTML documentation but no machine‑readable OpenAPI, GraphQL, or AsyncAPI spec.
  evidence:
  - status: 200
    url: https://csa-iot.org/resources/developer-resources/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: The Connectivity Standards Alliance (CSA) is a global industry consortium that develops and promotes open standards for the Internet of Things (IoT). It oversees the Matter, Zigbee, and Aliro specifications, providing certification programs, testing tools, and resources for manufacturers and developers to ensure interoperable, secure IoT products. CSA engages members worldwide through events, developer resources, and a community portal.
image: https://csa-iot.org/wp-content/uploads/2025/03/home-hero-superconnector-draft-1-1.png
layout: provider
modified: '2026-10-13'
name: Connectivity Standards Alliance
nav: Providers
network: true
overview: 'Connectivity Standards Alliance is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IoT, Standards, Consortium, and Open Source.


  Connectivity Standards Alliance''s developer surface includes documentation, support, engineering blog, and 10 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Connectivity Standards Alliance Domain Security
  slug: connectivity-standards-alliance-domain-security
  summary_line: TLSv1.3 · DMARC
slug: connectivity-standards-alliance
tags:
- Company
- IoT
- Standards
- Consortium
- Open Source
website: https://csa-iot.org
---
