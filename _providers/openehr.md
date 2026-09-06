---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 49
  human_in_the_loop: 0
  name: Openehr Agentic Access
  operation_count: 97
  slug: openehr-agentic-access
  summary_line: 97 operations · 49 acting
api_count: 7
apis:
- baseURL_template: https://{baseUrl}/v1
  baseurl_source: spec_template
  description: The core openEHR record API — create and manage EHRs, compositions, directories, contributions and versioned objects. openEHR SPECIFICATION, not a callable service — 33 operation(s) across 23 path(s),
  name: openEHR EHR API
  slug: ehr
- baseURL_template: https://{baseUrl}/v1
  baseurl_source: spec_template
  description: Execute stored and ad-hoc Archetype Query Language (AQL) queries against an openEHR system. openEHR SPECIFICATION, not a callable service — 6 operation(s) across 3 path(s), served from the templated h
  name: openEHR Query API
  slug: query
- baseURL_template: https://{baseUrl}/v1
  baseurl_source: spec_template
  description: Manage the definition layer — ADL 1.4 and ADL 2 templates, operational templates and stored queries. openEHR SPECIFICATION, not a callable service — 13 operation(s) across 9 path(s), served from the t
  name: openEHR Definition API
  slug: definition
- baseURL_template: https://{baseUrl}/v1
  baseurl_source: spec_template
  description: System-level service endpoints for an openEHR server. openEHR SPECIFICATION, not a callable service — 1 operation(s) across 1 path(s), served from the templated host `https://{baseUrl}/v1`.
  name: openEHR System API
  slug: system
- baseURL_template: https://{baseUrl}/v1
  baseurl_source: spec_template
  description: Party, role and demographic data handling. Published but marked DEVELOPMENT by openEHR. openEHR SPECIFICATION, not a callable service — 42 operation(s) across 27 path(s), served from the templated hos
  name: openEHR Demographic API
  slug: demographic
- baseURL_template: https://{baseUrl}/v1
  baseurl_source: spec_template
  description: Administrative operations over EHRs. Published but marked DEVELOPMENT by openEHR. openEHR SPECIFICATION, not a callable service — 2 operation(s) across 2 path(s), served from the templated host `https
  name: openEHR Admin API
  slug: admin
artifact_total: 10
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openehr-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://openehr.org/
- group: docs
  title: ''
  type: Specification
  url: https://specifications.openehr.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openEHR
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/openEHR/specifications-ITS-REST
- group: other
  title: ''
  type: Governance
  url: https://openehr.org/governance/
- group: other
  title: ''
  type: Participants
  url: https://openehr.org/specification-program/
- group: other
  title: ''
  type: Membership
  url: https://openehr.org/professional-members-2/
- group: operate
  title: ''
  type: ReleaseProcess
  url: https://specifications.openehr.org/governance/release_strategy
- group: other
  title: ''
  type: Charter
  url: https://specifications.openehr.org/governance/change_process
- group: start
  title: ''
  type: Registry
  url: https://ckm.openehr.org/ckm/
- group: other
  title: ''
  type: MailingList
  url: https://discourse.openehr.org/
- group: company
  title: ''
  type: News
  url: https://openehr.org/news/
- group: other
  title: ''
  type: Events
  url: https://openehr.org/events/
- group: commercial
  title: ''
  type: License
  url: https://creativecommons.org/licenses/by-nd/3.0/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.openehr.org/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.openehr.org/implementation/
- group: docs
  title: ''
  type: APIReference
  url: https://specifications.openehr.org/releases/ITS-REST/latest/
- group: agent
  title: ''
  type: LLMsTxt
  url: https://specifications.openehr.org/llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: https://specifications.openehr.org/releases
- group: design
  title: ''
  type: Vocabulary
  url: https://specifications.openehr.org/releases/TERM/latest/
- group: docs
  title: ''
  type: JSONSchema
  url: https://specifications.openehr.org/releases/ITS-JSON/latest/
- group: design
  title: ''
  type: Conformance
  url: https://developer.openehr.org/conformance/
- group: other
  title: ''
  type: Participants
  url: https://openehr.org/industry-partners/
- group: other
  title: ''
  type: Adopters
  url: https://openehr.org/organisation-partners/
- group: other
  title: ''
  type: WorkingGroups
  url: https://openehr.org/programs/specification/board_members
created: '2026-09-02'
description: 'openEHR is the open specification family for electronic health records, and the main structural alternative to HL7 FHIR. It is governed by two UK not-for-profit entities: the openEHR Foundation, a company limited by guarantee that holds the intellectual property, and the openEHR Community Interest Company, trading as openEHR International, which has run day-to-day operations since 10 May 2019. Its defining idea is two-level modelling — a small, stable Reference Model that software implements once, plus a large, separately governed body of clinician-authored archetypes and templates expressed in the Archetype Definition Language and queried through the Archetype Query Language. The specification site publishes 68 specifications across 14 components at three maturity levels of openEHR''s own declaring: Stable (AM, BASE, CDS, ITS-REST, ITS-XML, LANG, QUERY, RM, TERM), Development (CNF, ITS-BMM, ITS-JSON, SM) and Paused (PROC). The ITS-REST component ships real OpenAPI 3.0 for
  six API surfaces — EHR, Query, Definition and System are STABLE, Demographic and Admin are DEVELOPMENT — under a Creative Commons Attribution-NoDerivs 3.0 licence, with the tooling repositories under Apache-2.0. The coalition is unusually legible: 59 named people across the CIC Board, Foundation Board and the Specification, Clinical and Education program boards, with employers published beside 37 of them. What this repo holds are SPECIFICATIONS, not services — every contract here has the templated server https://{baseUrl}/v1 and describes what a conformant implementation must offer, so none of it is a callable API and it must never be read as one.'
image: https://openehr.org/wp-content/uploads/2024/11/openehr_logo_9DNsQEt-3.png
json_schemas:
- name: Openehr Rm 1.0.3 All
  property_count: 0
  slug: openehr-rm-1.0.3-all
- name: Openehr Rm 1.0.4 All
  property_count: 0
  slug: openehr-rm-1.0.4-all
- name: Openehr Rm 1.1.0 All
  property_count: 0
  slug: openehr-rm-1.1.0-all
layout: provider
modified: '2026-09-02'
name: openEHR
nav: Providers
network: true
overview: 'openEHR publishes 6 APIs on the [APIs.io](https://apis.io/) network, including EHR API, Query API, Definition API, and 3 more. Tagged areas include openEHR, Healthcare, EHR, Electronic Health Records, and Health Informatics.


  openEHR''s developer surface includes product news, documentation, API reference, changelog, and 22 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 50.0
    catalog_earned_first_party: 0.0
    catalog_gap: 65.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.8
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 15.2
    contract_quality: 58.9
    developer_ergonomics: 26.2
    discoverability: 72.2
    governance: 15.2
    operational_transparency: 18.4
  previous_composite: 29.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 3.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
slug: openehr
tags:
- openEHR
- Healthcare
- EHR
- Electronic Health Records
- Health Informatics
- Standards
- Specification
- Interoperability
- Information Model
- Archetypes
- AQL
- ADL
- Clinical Modelling
- Reference Model
- Not-for-profit
website: https://openehr.org/
---
