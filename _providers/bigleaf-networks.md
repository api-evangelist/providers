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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bigleaf-networks/refs/heads/main/llms/bigleaf-networks-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bigleaf-networks-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bigleaf-networks/refs/heads/main/well-known/bigleaf-networks-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bigleaf-networks-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bigleaf-networks/refs/heads/main/well-known/bigleaf-networks-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bigleaf-networks-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bigleaf-networks/refs/heads/main/hosts/bigleaf-networks-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bigleaf-networks-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bigleaf-networks/refs/heads/main/vendors/bigleaf-networks-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bigleaf-networks-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.bigleaf.net/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bigleaf.net/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bigleaf.net/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bigleaf.net/blog/price-vs-value-in-network-connectivity/
- group: company
  title: ''
  type: Newsroom
  url: https://www.bigleaf.net/company/news/?1=1
- group: other
  title: ''
  type: Leadership
  url: https://www.bigleaf.net/company/leadership/
- group: company
  title: ''
  type: Blog
  url: https://www.bigleaf.net/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bigleaf-networks/refs/heads/main/security/bigleaf-networks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bigleaf-networks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bigleaf.net/
coverage:
  checked: '2026-09-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found at the API host (api.bigleaf.net) after probing common spec endpoints.
  evidence:
  - status: 404
    url: https://api.bigleaf.net/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Bigleaf Networks provides cloud‑managed WAN optimization and connectivity solutions, delivering real‑time traffic optimization, hybrid WAN, 5G integration, and reliable internet redundancy for enterprises. Their platform improves performance, uptime, and simplifies network management across multiple locations and devices.
image: https://www.bigleaf.net/wp-content/uploads/2026/04/Blog-Featured-Images-2026Circuit-Data-Metering-1.webp
layout: provider
modified: '2026-09-28'
name: Bigleaf Networks
nav: Providers
network: true
overview: 'Bigleaf Networks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud-Managed WAN, Network Optimization, Hybrid WAN, 5G Integration, and Enterprise Connectivity.


  Bigleaf Networks'' developer surface includes support, pricing, engineering blog, and 11 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 58.9
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bigleaf Networks Domain Security
  slug: bigleaf-networks-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bigleaf-networks
tags:
- Cloud-Managed WAN
- Network Optimization
- Hybrid WAN
- 5G Integration
- Enterprise Connectivity
- Company
website: https://www.bigleaf.net/
---
