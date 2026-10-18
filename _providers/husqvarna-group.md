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
api_count: 1
apis:
- description: Developer portal for Husqvarna Group offering APIs and integration information.
  name: Husqvarna Developer Portal
  slug: husqvarna-developer-portal
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/husqvarna-group/refs/heads/main/hosts/husqvarna-group-hosts.yml
  title: ''
  type: Hosts
  url: hosts/husqvarna-group-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/husqvarna-group/refs/heads/main/vendors/husqvarna-group-vendors.yml
  title: ''
  type: Vendors
  url: vendors/husqvarna-group-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/husqvarna-group/refs/heads/main/packages/husqvarna-group-packages.yml
  title: ''
  type: SDKs
  url: packages/husqvarna-group-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/husqvarna-group/refs/heads/main/packages/husqvarna-group-packages.yml
  title: ''
  type: Packages
  url: packages/husqvarna-group-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.husqvarnagroup.com/en/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacyportal.husqvarnagroup.com/en/privacy-notice
- group: company
  title: ''
  type: Newsroom
  url: https://www.husqvarnagroup.com/en/news
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.husqvarnagroup.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/husqvarnagroup
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/husqvarna-group/refs/heads/main/security/husqvarna-group-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/husqvarna-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://husqvarnagroup.com/
coverage:
  checked: '2026-10-15'
  detail: Developer portal pages are JavaScript-rendered and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://portal.husqvarnagroup.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-14'
description: Husqvarna Group is a global leader in outdoor power products, including chainsaws, lawn mowers, and garden tools, as well as professional forestry equipment. The company operates through several divisions such as Husqvarna Forest & Garden, Gardena, and Husqvarna Construction, serving both consumer and professional markets worldwide. It focuses on innovation, sustainability, and digital services, offering connected devices and platforms for efficient outdoor work.
image: https://www.husqvarnagroup.com/sites/husqvarna/files/styles/open_graph/public/media/JH-648487-1920x720.jpg?itok=WjPxVg9-
layout: provider
modified: '2026-10-14'
name: Husqvarna Group
nav: Providers
network: true
overview: Husqvarna Group is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Outdoor, PowerTools, Forestry, and Sustainability.
random_paper: 3
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 58.9
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Husqvarna Group Domain Security
  slug: husqvarna-group-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: husqvarna-group
tags:
- Company
- Outdoor
- PowerTools
- Forestry
- Sustainability
website: https://husqvarnagroup.com/
---
