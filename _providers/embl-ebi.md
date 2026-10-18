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
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/embl-ebi/refs/heads/main/well-known/embl-ebi-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/embl-ebi-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/embl-ebi/refs/heads/main/well-known/embl-ebi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/embl-ebi-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/embl-ebi/refs/heads/main/hosts/embl-ebi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/embl-ebi-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ebi.ac.uk/about/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.ebi.ac.uk/support
- group: auth
  title: ''
  type: Security
  url: https://www.ebi.ac.uk/security/
- group: company
  title: ''
  type: Newsroom
  url: https://www.ebi.ac.uk/about/news
- group: other
  title: ''
  type: Leadership
  url: https://www.ebi.ac.uk/about/leadership
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/embl-ebi/refs/heads/main/security/embl-ebi-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/embl-ebi-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/embl-ebi/refs/heads/main/security/embl-ebi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/embl-ebi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ebi.ac.uk
coverage:
  checked: '2026-10-14'
  detail: The EMBL-EBI website provides documentation but no discoverable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://www.ebi.ac.uk
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: The European Bioinformatics Institute (EMBL-EBI) is a world‑leading centre for bioinformatics research and services, providing freely accessible data resources, tools and databases to the global scientific community. It supports a wide range of life‑science research, from genomics and proteomics to structural biology and systems biology, and collaborates internationally to advance open science and data sharing.
image: https://acxngcvroo.cloudimg.io/v7/www.embl.org/files/wp-content/uploads/EMBL-EBI-home-hero-cells_2021-1-scaled.jpeg?width=1600
layout: provider
modified: '2026-10-14'
name: EMBL-EBI
nav: Providers
network: true
overview: 'EMBL-EBI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Bioinformatics, Data, Research, and Open Science.


  EMBL-EBI''s developer surface includes support and 10 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 51.8
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Embl Ebi Domain Security
  slug: embl-ebi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Embl Ebi Vulnerability Disclosure
  slug: embl-ebi-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: embl-ebi
tags:
- Company
- Bioinformatics
- Data
- Research
- Open Science
- Europe
website: https://www.ebi.ac.uk
---
