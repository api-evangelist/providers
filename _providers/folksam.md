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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/folksam/refs/heads/main/hosts/folksam-hosts.yml
  title: ''
  type: Hosts
  url: hosts/folksam-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/folksam
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/folksam/refs/heads/main/security/folksam-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/folksam-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://folksam.se/
coverage:
  checked: '2026-10-15'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found on discovered hosts.
  evidence:
  - status: 404
    url: https://api.folksam.se/openapi.json
  - status: 404
    url: https://api.folksam.se/v1/openapi.json
  - status: 404
    url: https://api.folksam.se/swagger.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: Folksam Försäkringsbolag is a Swedish insurance company offering a wide range of insurance products for homes, cars, and individuals, as well as savings and pension solutions. It serves over 900,000 vehicles and countless households across Sweden, emphasizing customer service and digital accessibility through its website.
image: https://folksamse.azureedge.net/media/imageCardSamla_tcm5-84088.jpg
layout: provider
modified: '2026-10-14'
name: Folksam
nav: Providers
network: true
overview: Folksam is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Sweden, Financial Services, and Consumer.
random_paper: 1
score:
  band: minimal
  composite: 3.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 5.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Folksam Domain Security
  slug: folksam-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: folksam
tags:
- Company
- Insurance
- Sweden
- Financial Services
- Consumer
website: https://folksam.se/
---
