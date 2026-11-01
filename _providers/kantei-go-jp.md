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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/kantei-go-jp/hosts/kantei-go-jp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kantei-go-jp-hosts.yml
- group: auth
  href: https://artifacts.apis.io/kantei-go-jp/security/kantei-go-jp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kantei-go-jp-domain-security.yml
coverage:
  checked: '2026-10-29'
  detail: The Office for Promotion of Regional Revitalization is a governmental body with no public API or developer documentation.
  evidence:
  - status: 200
    url: https://www.cao.go.jp/
  reason: not-a-software-company
  state: none
created: '2026-10-29'
description: The Office for Promotion of Regional Revitalization, part of Japan's Cabinet Office, is a governmental body tasked with formulating and implementing policies to stimulate economic activity, improve infrastructure, and support community development in regional areas across Japan. It coordinates with local authorities, businesses, and stakeholders to design revitalization projects, provide financial assistance, and promote sustainable growth, aiming to address challenges such as population decline and regional disparities.
layout: provider
modified: '2026-10-29'
name: Office for Promotion of Regional Revitalization, Cabinet Office of Japan
nav: Providers
network: true
overview: Office for Promotion of Regional Revitalization, Cabinet Office of Japan is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Government, Japan, RegionalRevitalization, and CabinetOffice.
random_paper: 6
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Kantei Go Jp Domain Security
  slug: kantei-go-jp-domain-security
  summary_line: TLSv1.3 · HSTS
slug: kantei-go-jp
tags:
- Company
- Government
- Japan
- RegionalRevitalization
- CabinetOffice
---
