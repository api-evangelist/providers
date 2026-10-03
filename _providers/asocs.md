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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/asocs/refs/heads/main/hosts/asocs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asocs-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://asocscloud.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://asocscloud.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://asocscloud.com/category/news/
- group: docs
  title: ''
  type: Documentation
  url: https://asocscloud.com/category/guides/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.asocscloud.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/asocscloud
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/asocs/refs/heads/main/security/asocs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asocs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asocscloud.com
coverage:
  checked: 2026-09-26
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on asocscloud.com or its subdomains.
  evidence:
  - status: 404
    url: https://asocscloud.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: ASOCS provides industrial digital transformation solutions, offering 5G‑enabled connectivity, generative AI for physical systems, and robust platforms like CYRUS® and HERMES to synchronize digital twins, autonomous machines, and processes across factories, ports, and logistics hubs.
layout: provider
modified: '2026-09-26'
name: Asocs
nav: Providers
network: true
overview: 'Asocs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Industrial 5G, Private Networks, AI Positioning, AI Kits, and Enterprise Solutions.


  Asocs'' developer surface includes documentation and 8 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 46.4
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Asocs Domain Security
  slug: asocs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: asocs
tags:
- Industrial 5G
- Private Networks
- AI Positioning
- AI Kits
- Enterprise Solutions
- System Integrators
website: https://asocscloud.com
---
