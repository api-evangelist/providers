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
api_count: 1
apis:
- description: Azafaros does not appear to expose a public API; no documentation or OpenAPI spec was found.
  name: Azafaros API
  slug: azafaros-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/azafaros/refs/heads/main/security/azafaros-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/azafaros-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/azafaros/refs/heads/main/well-known/azafaros-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/azafaros-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/azafaros/refs/heads/main/well-known/azafaros-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/azafaros-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/azafaros/refs/heads/main/hosts/azafaros-hosts.yml
  title: ''
  type: Hosts
  url: hosts/azafaros-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.azafaros.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.azafaros.com/news-media/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/azafaros/refs/heads/main/security/azafaros-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/azafaros-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/azafaros/refs/heads/main/security/azafaros-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/azafaros-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.azafaros.com
coverage:
  checked: '2026-09-27'
  detail: No API documentation or OpenAPI spec was found on the provider's domain.
  evidence:
  - status: 404
    url: https://api.azafaros.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: Azafaros B.V. develops therapeutic candidates for severe rare metabolic disorders. Its lead program is the orally available azasugar nizubaglustat, designed to treat central nervous system involvement and modulate glycosphingolipid metabolism in lysosomal storage diseases. The company focuses on patients with conditions such as GM1/GM2 gangliosidoses.
image: https://www.azafaros.com/userdata/instellingen/logo_azafaros-1x38.png
layout: provider
modified: '2026-09-27'
name: Azafaros
nav: Providers
network: true
overview: Azafaros publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Lysosomal Storage Disorders and Rare Metabolic Disorders.
random_paper: 19
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Azafaros Domain Security
  slug: azafaros-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Azafaros Vulnerability Disclosure
  slug: azafaros-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: azafaros
tags:
- Lysosomal Storage Disorders
- Rare Metabolic Disorders
website: https://www.azafaros.com
---
