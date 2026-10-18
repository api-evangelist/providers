---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.3
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: The Patrons API from Koha — 2 operation(s) for patrons.
  name: Koha Patrons API
  slug: koha-patrons-api
artifact_total: 6
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/koha/refs/heads/main/rules/koha-rules.yml
  title: ''
  type: Spectral
  url: rules/koha-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/koha/refs/heads/main/json-ld/koha-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/koha-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/koha/refs/heads/main/vocabulary/koha-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/koha-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/koha/refs/heads/main/data-model/koha-data-model.yml
  title: ''
  type: DataModel
  url: data-model/koha-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/koha/refs/heads/main/conformance/koha-conformance.yml
  title: ''
  type: Conformance
  url: conformance/koha-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/koha/refs/heads/main/well-known/koha-git-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/koha-git-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/koha/refs/heads/main/well-known/koha-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/koha-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/koha/refs/heads/main/hosts/koha-hosts.yml
  title: ''
  type: Hosts
  url: hosts/koha-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/koha/refs/heads/main/packages/koha-packages.yml
  title: ''
  type: SDKs
  url: packages/koha-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/koha/refs/heads/main/packages/koha-packages.yml
  title: ''
  type: Packages
  url: packages/koha-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Koha-Community
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/koha/refs/heads/main/security/koha-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/koha-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://koha-community.org
- group: docs
  title: ''
  type: Documentation
  url: https://koha-community.org/documentation/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://koha-community.org/get-involved/for-developers/
- group: operate
  title: ''
  type: Support
  url: https://koha-community.org/get-involved/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://koha-community.org
  reason: no-developer-program
  state: none
created: '2026-10-14'
description: Koha is an open-source integrated library system (ILS) used worldwide by libraries to manage cataloging, circulation, acquisitions, and public access. The Koha community provides extensive documentation, support, and development resources, making it a robust platform for library automation and digital services.
json_schemas:
- name: GetApiV1PatronsResponse
  property_count: 11
  slug: koha-get-api-v1-patrons-response
- name: GetApiV1PatronsResponse2
  property_count: 45
  slug: koha-get-api-v1-patrons-response2
jsonld:
- class_count: 2
  name: Koha Context
  property_count: 53
  slug: koha-context
layout: provider
modified: '2026-10-14'
name: Koha
nav: Providers
network: true
overview: 'Koha is listed with 1 API on the [APIs.io](https://apis.io/) network: Patrons API. Tagged areas include Library, Open Source, ILS, Community, and Software.


  The Koha catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Koha''s developer surface includes documentation, support, and 14 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Koha API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: koha-rules
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 47.3
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 21.3
    developer_ergonomics: 31.0
    discoverability: 53.6
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 16.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Koha Domain Security
  slug: koha-domain-security
  summary_line: TLSv1.3 · DMARC
slug: koha
tags:
- Library
- Open Source
- ILS
- Community
- Software
website: https://koha-community.org
---
