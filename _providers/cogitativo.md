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
- description: API surface referenced by host api.cogitativo.com but no machine-readable contract found.
  name: Cogitativo API
  slug: cogitativo-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cogitativo/refs/heads/main/well-known/cogitativo-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cogitativo-clarity-security.txt
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cogitativo/refs/heads/main/llms/cogitativo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cogitativo-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cogitativo/refs/heads/main/well-known/cogitativo-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cogitativo-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cogitativo/refs/heads/main/well-known/cogitativo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cogitativo-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cogitativo/refs/heads/main/hosts/cogitativo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cogitativo-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cogitativo/refs/heads/main/security/cogitativo-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cogitativo-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cogitativo/refs/heads/main/security/cogitativo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cogitativo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cogitativo.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://cogitativo.com
  - status: 200
    url: https://www.hiive.com/securities/cogitativo-stock
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: Cogitativo delivers precision health solutions for health plans and public programs, using AI to connect decisions with outcomes. Their platform offers products like Vision, Conciencia, and Cognitive CxO to manage clinical costs, provider access, payment integrity, and care fragmentation, helping organizations improve care quality and reduce expenses.
image: https://cogitativo.com/assets/og-image.jpg
layout: provider
modified: '2026-10-09'
name: Cogitativo
nav: Providers
network: true
overview: Cogitativo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Tech, Artificial Intelligence, Healthcare, and Analytics.
random_paper: 3
score:
  band: minimal
  composite: 7.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 64.3
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 8.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cogitativo Domain Security
  slug: cogitativo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cogitativo Vulnerability Disclosure
  slug: cogitativo-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cogitativo
tags:
- Company
- Health Tech
- Artificial Intelligence
- Healthcare
- Analytics
website: https://cogitativo.com
---
