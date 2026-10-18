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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Kundo provides a customer service platform with AI features; API details are not publicly documented.
  name: Kundo API
  slug: kundo-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kundo/refs/heads/main/security/kundo-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/kundo-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kundo/refs/heads/main/llms/kundo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kundo-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kundo/refs/heads/main/well-known/kundo-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kundo-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kundo/refs/heads/main/well-known/kundo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kundo-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kundo/refs/heads/main/hosts/kundo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kundo-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kundo/refs/heads/main/vendors/kundo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kundo-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kundo/refs/heads/main/packages/kundo-packages.yml
  title: ''
  type: SDKs
  url: packages/kundo-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kundo/refs/heads/main/packages/kundo-packages.yml
  title: ''
  type: Packages
  url: packages/kundo-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kundo.se/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kundo
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kundo/refs/heads/main/security/kundo-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/kundo-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kundo/refs/heads/main/security/kundo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kundo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kundo.se/
- group: company
  title: ''
  type: Blog
  url: https://www.kundo.se/blogg
- group: operate
  title: ''
  type: Support
  url: https://www.kundo.se/kontakt
- group: docs
  title: ''
  type: Documentation
  url: https://www.kundo.se/om-oss
coverage:
  checked: '2026-10-15'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract is publicly available on the discovered hosts.
  evidence:
  - status: 404
    url: https://api.kundo.se/openapi.json
  - status: 404
    url: https://api.kundo.se/swagger.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Kundo provides a comprehensive AI‑enhanced customer service platform that combines ticketing, knowledge management, and self‑service tools into a single SaaS solution. Built for enterprises, Kundo leverages artificial intelligence to keep knowledge bases up‑to‑date, automatically suggest answers, and streamline multi‑channel support. The platform offers AI Forms, AI Chat, and a knowledge agent that learns from existing content, helping support teams respond faster and improve customer satisfaction across various industries.
image: https://www.kundo.se/hubfs/OpenGraph.png
layout: provider
modified: '2026-10-15'
name: Kundo
nav: Providers
network: true
overview: 'Kundo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Customer Service, Artificial Intelligence, Software-as-a-Service, Ticketing, and Knowledge Management.


  Kundo''s developer surface includes engineering blog, support, documentation, and 13 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 64.3
    operational_transparency: 31.6
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Kundo Domain Security
  slug: kundo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Kundo Vulnerability Disclosure
  slug: kundo-vulnerability-disclosure
  summary_line: no policy recorded
slug: kundo
tags:
- Customer Service
- Artificial Intelligence
- Software-as-a-Service
- Ticketing
- Knowledge Management
- Sweden
website: https://www.kundo.se/
---
