---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: CytoReason Agents Service - A conversational AI platform with sandbox execution
  name: Agents Builder API
  slug: agents-builder-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/cytoreason/conformance/cytoreason-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cytoreason-conformance.yml
- group: other
  href: https://artifacts.apis.io/cytoreason/hosts/cytoreason-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cytoreason-hosts.yml
- group: other
  href: https://artifacts.apis.io/cytoreason/vendors/cytoreason-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cytoreason-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cytoreason/security/cytoreason-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cytoreason-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cytoreason.com
- group: company
  title: ''
  type: Blog
  url: https://info.cytoreason.com/blog
- group: operate
  title: ''
  type: Contact
  url: https://www.cytoreason.com/CytoReason%20Contact.dc.html
created: '2026-10-21'
description: CytoReason is a biotech AI company that builds computational disease biology models to help pharmaceutical and biotech firms make better R&D decisions. Founded in 2016 in Haifa, Israel, it leverages molecular and clinical data to generate predictive insights for drug discovery and portfolio management, serving major pharma partners and raising significant venture funding.
layout: provider
modified: '2026-10-21'
name: Cytoreason
nav: Providers
network: true
overview: 'Cytoreason is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Artificial Intelligence, Drug Discovery, Computational Biology, and Haifa.


  Cytoreason''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cytoreason Domain Security
  slug: cytoreason-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cytoreason
tags:
- Biotechnology
- Artificial Intelligence
- Drug Discovery
- Computational Biology
- Haifa
website: https://www.cytoreason.com
---
