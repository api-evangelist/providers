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
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 49
  human_in_the_loop: 0
  name: Openehr Agentic Access
  operation_count: 97
  slug: openehr-agentic-access
  summary_line: 97 operations · 49 acting
api_count: 13
apis:
- baseURL_template: https://{baseUrl}/v1
  baseurl_source: spec_template
  description: Management of [AOM and ADL 1.4](https://specifications.openehr.org/releases/AM/latest) Operational Templates (OPTs). These templates can be created using [modelling tools](https://www.openehr.org/down
  name: openEHR ADL1.4 API
  slug: openehr-adl1-4-api
- baseURL_template: https://{baseUrl}/v1
  baseurl_source: spec_template
  description: Management of [AOM2](https://specifications.openehr.org/releases/AM/latest/AOM2.html#_templates) templates. See also [ADL2 Template specifications](https://specifications.openehr.org/releases/AM/lates
  name: openEHR ADL2 API
  slug: openehr-adl2-api
- baseURL_template: https://{baseUrl}/v1
  baseurl_source: spec_template
  description: Management of the [AGENT](https://specifications.openehr.org/releases/RM/latest/demographic.html#_agent_class) class.
  name: openEHR AGENT API
  slug: openehr-agent-api
- baseURL_template: https://{baseUrl}/v1
  baseurl_source: spec_template
  description: Management of [COMPOSITION](https://specifications.openehr.org/releases/RM/latest/ehr.html#_composition_class) and [VERSIONED_COMPOSITION](https://specifications.openehr.org/releases/RM/latest/ehr.htm
  name: openEHR COMPOSITION API
  slug: openehr-composition-api
- baseURL_template: https://{baseUrl}/v1
  baseurl_source: spec_template
  description: Management of [CONTRIBUTION](https://specifications.openehr.org/releases/RM/latest/common.html#_contribution_class) class.
  name: openEHR CONTRIBUTION API
  slug: openehr-contribution-api
- baseURL_template: https://{baseUrl}/v1
  baseurl_source: spec_template
  description: Management of the [directory](https://specifications.openehr.org/releases/RM/latest/ehr.html#_directory) [FOLDER](https://specifications.openehr.org/releases/RM/latest/common.html#_folder_class) resou
  name: openEHR DIRECTORY API
  slug: openehr-directory-api
- baseURL_template: https://{baseUrl}/v1
  baseurl_source: spec_template
  description: Admin management of [EHRs](https://specifications.openehr.org/releases/RM/latest/ehr.html#_ehr_class).
  name: openEHR EHR API
  slug: openehr-ehr-api
- baseURL_template: https://{baseUrl}/v1
  baseurl_source: spec_template
  description: Management of [EHR_STATUS](https://specifications.openehr.org/releases/RM/latest/ehr.html#_ehr_status_class) and [VERSIONED_EHR_STATUS](https://specifications.openehr.org/releases/RM/latest/ehr.html#_
  name: openEHR EHR STATUS API
  slug: openehr-ehr-status-api
- baseURL_template: https://{baseUrl}/v1
  baseurl_source: spec_template
  description: Management of the [GROUP](https://specifications.openehr.org/releases/RM/latest/demographic.html#_group_class) class.
  name: openEHR GROUP API
  slug: openehr-group-api
- baseURL_template: https://{baseUrl}/v1
  baseurl_source: spec_template
  description: Management of [ITEM_TAG](https://specifications.openehr.org/releases/RM/development/common.html#_item_tag_class) resources.
  name: openEHR ITEM TAG API
  slug: openehr-item-tag-api
- baseURL_template: https://{baseUrl}/v1
  baseurl_source: spec_template
  description: The Options API from openEHR — 1 operation(s) for options.
  name: openEHR Options API
  slug: openehr-options-api
- baseURL_template: https://{baseUrl}/v1
  baseurl_source: spec_template
  description: Management of the [ORGANISATION](https://specifications.openehr.org/releases/RM/latest/demographic.html#_organisation_class) class.
  name: openEHR ORGANISATION API
  slug: openehr-organisation-api
- baseURL_template: https://{baseUrl}/v1
  baseurl_source: spec_template
  description: Management of the [PERSON](https://specifications.openehr.org/releases/RM/latest/demographic.html#_person_class) class.
  name: openEHR PERSON API
  slug: openehr-person-api
- baseURL_template: https://{baseUrl}/v1
  baseurl_source: spec_template
  description: Management of stored (registered) queries in the system, including creation of new versions and retrieval by qualified name and version. These endpoints enable registration and lifecycle management of
  name: openEHR Query API
  slug: openehr-query-api
- baseURL_template: https://{baseUrl}/v1
  baseurl_source: spec_template
  description: Management of the [ROLE](https://specifications.openehr.org/releases/RM/latest/demographic.html#_role_class) class.
  name: openEHR ROLE API
  slug: openehr-role-api
- baseURL_template: https://{baseUrl}/v1
  baseurl_source: spec_template
  description: Management of the [VERSIONED_PARTY](https://specifications.openehr.org/releases/RM/latest/demographic.html#_versioned_party_class) class.
  name: openEHR VERSIONED PARTY API
  slug: openehr-versioned-party-api
artifact_total: 20
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/openehr/refs/heads/main/agentic-access/openehr-agentic-access.yml
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
overview: 'openEHR publishes 16 APIs on the [APIs.io](https://apis.io/) network, including ADL1.4 API, ADL2 API, AGENT API, and 13 more. Tagged areas include openEHR, Healthcare, EHR, Electronic Health Records, and Health Informatics.


  openEHR''s developer surface includes product news, documentation, API reference, changelog, and 22 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.1
  facets:
    access_clarity: 0.0
    contract_governance: 15.2
    contract_quality: 52.8
    developer_ergonomics: 26.2
    discoverability: 57.4
    operational_transparency: 18.4
  previous_composite: 28.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 3.1
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
- Not-for-Profit
website: https://openehr.org/
---
