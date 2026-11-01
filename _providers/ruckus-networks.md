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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API documentation is not machine readable; the docs site renders via JavaScript and returns HTML shells for spec URLs.
  name: Ruckus Networks API
  slug: ruckus-networks-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/ruckus-networks/llms/ruckus-networks-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ruckus-networks-llms.txt
- group: other
  href: https://artifacts.apis.io/ruckus-networks/hosts/ruckus-networks-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ruckus-networks-hosts.yml
- group: other
  href: https://artifacts.apis.io/ruckus-networks/vendors/ruckus-networks-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ruckus-networks-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ruckusnetworks.com/about-us/terms/
- group: auth
  title: ''
  type: Security
  url: https://community.ruckuswireless.com/discussions/tagged/security
- group: start
  title: ''
  type: Sandbox
  url: https://community.ruckuswireless.com/discussions/tagged/console
- group: start
  title: ''
  type: Login
  url: https://community.ruckuswireless.com/entry/signin
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ruckusnetworks.com:443/prod/search?filter=%2BContent%5C+Type_md%3A%22Quick+Start+Guide%22+%2B%28ditaMap_md%3Atrue+OR+extension_md%3Apdf%29&maxFacetValues=12&term=*
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RuckusWireless
- group: auth
  href: https://artifacts.apis.io/ruckus-networks/security/ruckus-networks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ruckus-networks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ruckuswireless.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ruckusnetworks.com
- group: operate
  title: ''
  type: Support
  url: https://support.ruckuswireless.com
- group: company
  title: ''
  type: Blog
  url: https://www.ruckusnetworks.com/insights
coverage:
  checked: '2026-10-29'
  detail: Documentation site renders via JavaScript and returns HTML shells for spec URLs, preventing machine-readable contract discovery.
  evidence:
  - status: 200
    url: https://docs.ruckusnetworks.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Ruckus Networks provides AI-driven enterprise Wi‑Fi and networking solutions, offering cloud‑managed access points, switches, and AI‑enhanced radio resource management. Their portfolio includes RUCKUS One, AI, Unleashed, and services for education, hospitality, public venues, and enterprises, emphasizing zero‑trust security and network‑as‑a‑service.
image: https://webresources.vistancenetworks.com/images/assets/RUCKUS-Networks-Logos-artwork_black-orange+%281%29.png/Zz1mM2Q2YTZmOGY3MmUxMWYwOGU2M2I2ZWM5OGJlMmFkNQ==
layout: provider
modified: '2026-10-29'
name: Ruckus Networks
nav: Providers
network: true
overview: 'Ruckus Networks is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Networking, WiFi, AI, and Enterprise.


  Ruckus Networks'' developer surface includes sandbox, getting-started guide, documentation, support, engineering blog, and 9 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 18.7
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
    developer_ergonomics: 35.7
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ruckus Networks Domain Security
  slug: ruckus-networks-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ruckus-networks
tags:
- Company
- Networking
- WiFi
- AI
- Enterprise
website: https://www.ruckuswireless.com
---
