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
    dynamic_client_registration: true
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
  score: 15.1
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Syngenta developer portal (requires login)
  name: Syngenta API
  slug: syngenta-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/syngenta/refs/heads/main/well-known/syngenta-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/syngenta-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/syngenta/refs/heads/main/hosts/syngenta-hosts.yml
  title: ''
  type: Hosts
  url: hosts/syngenta-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/syngenta/refs/heads/main/vendors/syngenta-vendors.yml
  title: ''
  type: Vendors
  url: vendors/syngenta-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/syngenta/refs/heads/main/packages/syngenta-packages.yml
  title: ''
  type: SDKs
  url: packages/syngenta-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/syngenta/refs/heads/main/packages/syngenta-packages.yml
  title: ''
  type: Packages
  url: packages/syngenta-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.syngenta.com/terms-and-conditions
- group: start
  title: ''
  type: SignUp
  url: https://www.syngenta.com/syngenta-common/sign-up-popup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.syngenta.com/privacy-statement
- group: company
  title: ''
  type: Newsroom
  url: https://www.syngenta.com/media
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.syngenta.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/syngenta
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/syngenta/refs/heads/main/security/syngenta-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/syngenta-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.syngenta.com
coverage:
  checked: '2026-10-13'
  detail: Developer portal requires login and returns 401 for OpenAPI URLs, no machine-readable spec is publicly available.
  evidence:
  - status: 401
    url: https://portal.syngenta.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Syngenta is a global agribusiness that develops and markets seeds, crop protection products, and digital farming solutions. The company focuses on sustainable agriculture, research and innovation to help farmers increase productivity while reducing environmental impact. It operates worldwide, offering a portfolio that includes crop protection chemicals, seeds, biologicals, and digital tools for farm management.
image: https://www.syngenta.com/sites/default/files/2024-12/syngenta.jpg
layout: provider
modified: '2026-10-13'
name: Syngenta
nav: Providers
network: true
overview: 'Syngenta is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, Seeds, Crop Protection, and Digital Farming.


  Syngenta''s developer surface includes signup flow and 12 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 58.9
    operational_transparency: 5.3
  provenance:
    mcp: derived
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
  name: Syngenta Domain Security
  slug: syngenta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: syngenta
tags:
- Company
- Agriculture
- Seeds
- Crop Protection
- Digital Farming
website: https://www.syngenta.com
---
