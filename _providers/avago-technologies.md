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
  scored_at: '2026-09-15'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avago-technologies/refs/heads/main/security/avago-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avago-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.avagotech.com/
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/broadcom/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avago-technologies/refs/heads/main/llms/avago-technologies-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avago-technologies-llms.txt
coverage:
  checked: '2026-09-13'
  detail: 'Avago Technologies Limited renamed itself Broadcom Limited on 1 February 2016 after acquiring Broadcom Corporation, so the brand has no surface of its own: every path on avagotech.com returns an HTTP 301 to broadcom.com, avago.com is a third-party domain-brokerage landing page, and no Avago GitHub organization, developer portal, package or machine-readable contract exists.'
  evidence:
  - status: 301
    url: https://www.avagotech.com/
  - status: 301
    url: https://www.avagotech.com/openapi.json
  - status: 301
    url: https://www.avagotech.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/avagotech
  - status: 200
    url: https://avago.com/
  reason: defunct
  state: none
created: '2026-09-13'
description: 'Avago Technologies Limited was the Singapore-headquartered semiconductor company spun out of Agilent Technologies'' semiconductor products group in 2005 that acquired Broadcom Corporation for $37 billion on February 1, 2016 and renamed itself Broadcom Limited, today Broadcom Inc. (NASDAQ: AVGO). Avago is therefore not a subsidiary of Broadcom but its legal predecessor and former corporate name. The brand is retired: every path on avagotech.com returns an HTTP 301 to broadcom.com, avago.com is a third-party domain-brokerage landing page rather than a company site, and no Avago-branded developer portal, documentation, OpenAPI, SDK, package or GitHub organization exists. API surfaces once associated with Avago product lines (LSI and Emulex storage controllers, fiber optics, RF) are published today by Broadcom and are profiled under the broadcom record.'
layout: provider
modified: '2026-09-13'
name: Avago Technologies
nav: Providers
network: true
overview: Avago Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Hardware, Electronic Components, and Acquired.
random_paper: 7
score:
  band: minimal
  composite: 5.4
  coverage:
    artifact_dirs: 3
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.7
    operational_transparency: 0.0
  previous_composite: 5.4
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Avago Technologies Domain Security
  slug: avago-technologies-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: avago-technologies
tags:
- Company
- Semiconductors
- Hardware
- Electronic Components
- Acquired
- Legacy Brand
- Broadcom
website: https://www.avagotech.com/
---
