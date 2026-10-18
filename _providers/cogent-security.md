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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cogent-security/refs/heads/main/llms/cogent-security-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cogent-security-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cogent-security/refs/heads/main/hosts/cogent-security-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cogent-security-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cogent-security/refs/heads/main/vendors/cogent-security-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cogent-security-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.cogentsecurity.com/leadership
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cogent-security/refs/heads/main/security/cogent-security-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cogent-security-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cogentsecurity.com/
coverage:
  checked: '2026-10-09'
  detail: The provider's website contains no machine‑readable API specification or documentation.
  evidence:
  - status: 200
    url: https://www.cogentsecurity.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-09'
description: Cogent Security LLC, founded in 2010, provides security services for U.S. government and defense sectors. Offering risk management, intelligence, counterintelligence, security engineering, and technical surveillance, the company supports the National Nuclear Security Administration and other federal agencies. In 2022 Cogent expanded by acquiring Innovative Technology Partnerships, broadening its capabilities across program management, cloud services, and advanced security programs. The firm emphasizes independent, interdisciplinary expertise to deliver comprehensive security solutions.
image: https://static.wixstatic.com/media/261e3e_a9e8c4668f5249db95468ca358d46204%7Emv2.png/v1/fit/w_2500,h_1330,al_c/261e3e_a9e8c4668f5249db95468ca358d46204%7Emv2.png
layout: provider
modified: '2026-10-09'
name: Cogent Security
nav: Providers
network: true
overview: Cogent Security is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Government, Defense, Intelligence, and Risk Management.
random_paper: 11
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 7
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
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cogent Security Domain Security
  slug: cogent-security-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cogent-security
tags:
- Security
- Government
- Defense
- Intelligence
- Risk Management
- Company
website: https://www.cogentsecurity.com/
---
