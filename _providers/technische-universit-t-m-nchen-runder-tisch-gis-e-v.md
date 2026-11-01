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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API reference for the Technische Universität München - Runder Tisch GIS e.V. association (no public machine‑readable contract found).
  name: GIS Association API
  slug: gis-association-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/technische-universit-t-m-nchen-runder-tisch-gis-e-v/security/technische-universit-t-m-nchen-runder-tisch-gis-e-v-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/technische-universit-t-m-nchen-runder-tisch-gis-e-v-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/technische-universit-t-m-nchen-runder-tisch-gis-e-v/llms/technische-universit-t-m-nchen-runder-tisch-gis-e-v-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/technische-universit-t-m-nchen-runder-tisch-gis-e-v-llms.txt
- group: auth
  href: https://artifacts.apis.io/technische-universit-t-m-nchen-runder-tisch-gis-e-v/well-known/technische-universit-t-m-nchen-runder-tisch-gis-e-v-tum-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/technische-universit-t-m-nchen-runder-tisch-gis-e-v-tum-security.txt
- group: auth
  href: https://artifacts.apis.io/technische-universit-t-m-nchen-runder-tisch-gis-e-v/well-known/technische-universit-t-m-nchen-runder-tisch-gis-e-v-nav-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/technische-universit-t-m-nchen-runder-tisch-gis-e-v-nav-security.txt
- group: agent
  href: https://artifacts.apis.io/technische-universit-t-m-nchen-runder-tisch-gis-e-v/well-known/technische-universit-t-m-nchen-runder-tisch-gis-e-v-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/technische-universit-t-m-nchen-runder-tisch-gis-e-v-well-known.yml
- group: other
  href: https://artifacts.apis.io/technische-universit-t-m-nchen-runder-tisch-gis-e-v/hosts/technische-universit-t-m-nchen-runder-tisch-gis-e-v-hosts.yml
  title: ''
  type: Hosts
  url: hosts/technische-universit-t-m-nchen-runder-tisch-gis-e-v-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://www.tum.de/die-tum/kontakt-und-anfahrt/login/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tum
- group: auth
  href: https://artifacts.apis.io/technische-universit-t-m-nchen-runder-tisch-gis-e-v/security/technische-universit-t-m-nchen-runder-tisch-gis-e-v-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/technische-universit-t-m-nchen-runder-tisch-gis-e-v-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/technische-universit-t-m-nchen-runder-tisch-gis-e-v/security/technische-universit-t-m-nchen-runder-tisch-gis-e-v-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/technische-universit-t-m-nchen-runder-tisch-gis-e-v-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tum.de/
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract was discovered on the provider's hosts.
  evidence:
  - status: 0
    url: https://api.tum.de/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Technische Universität München – Runder Tisch GIS e.V. is a non‑profit association at the Technical University of Munich that brings together researchers, students and industry partners around geographic information systems (GIS). It promotes the exchange of knowledge, organizes events, workshops and projects, and supports open‑source GIS initiatives. The group serves as a hub for GIS education, research collaborations, and community building within the university and the broader German GIS ecosystem.
image: https://www.tum.de/fileadmin/_processed_/a/1/csm_OG2_a211f33903.jpg
layout: provider
modified: '2026-10-28'
name: Technische Universität München - Runder Tisch GIS e.V.
nav: Providers
network: true
overview: Technische Universität München - Runder Tisch GIS e.V. is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GIS, Education, Research, Open-Source, and Community.
random_paper: 2
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 17.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Technische Universit T M Nchen Runder Tisch Gis E V Domain Security
  slug: technische-universit-t-m-nchen-runder-tisch-gis-e-v-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Technische Universit T M Nchen Runder Tisch Gis E V Vulnerability Disclosure
  slug: technische-universit-t-m-nchen-runder-tisch-gis-e-v-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: technische-universit-t-m-nchen-runder-tisch-gis-e-v
tags:
- GIS
- Education
- Research
- Open-Source
- Community
- Company
website: https://www.tum.de/
---
