---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/boring-company/refs/heads/main/llms/boring-company-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boring-company-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/boring-company/refs/heads/main/well-known/boring-company-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/boring-company-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boring-company/refs/heads/main/hosts/boring-company-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boring-company-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boring-company/refs/heads/main/vendors/boring-company-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boring-company-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boring-company/refs/heads/main/security/boring-company-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boring-company-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.boringcompany.com
coverage:
  checked: '2026-10-02'
  detail: GraphQL endpoint returned a schema but could not verify it belongs to Boring Company
  evidence:
  - status: 200
    url: https://shop.boringcompany.com/api/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-02'
description: The Boring Company, founded by Elon Musk, focuses on developing tunneling and infrastructure technologies to reduce traffic congestion and enable rapid point‑to‑point transportation. It designs and manufactures advanced tunnel boring machines, such as Prufrock, and builds large‑scale transportation systems like the Vegas Loop. The company aims to create safe, fast, and low‑cost tunnels for transportation, utilities, and freight, transforming urban mobility and infrastructure.
image: https://boringcompany.com/assets/og-image.jpg
layout: provider
modified: '2026-10-02'
name: Boring Company
nav: Providers
network: true
overview: Boring Company is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Tunneling, Infrastructure, Transportation, and ElonMusk.
random_paper: 15
score:
  band: minimal
  composite: 4.1
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
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boring Company Domain Security
  slug: boring-company-domain-security
  summary_line: TLSv1.3 · DMARC
slug: boring-company
tags:
- Company
- Tunneling
- Infrastructure
- Transportation
- ElonMusk
website: https://www.boringcompany.com
---
