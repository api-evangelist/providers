---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Keenethics Labs Com Agentic Access
  operation_count: 10
  slug: keenethics-labs-com-agentic-access
  summary_line: 10 operations · 2 acting
api_count: 1
apis:
- baseURL: http://localhost:3000/api/
  baseurl_source: spec
  description: The activity API from keenethics-labs-com — 2 operation(s) for activity.
  name: keenethics-labs-com Activity API
  slug: keenethics-labs-com-activity-api
- baseURL: http://localhost:3000/api/
  baseurl_source: spec
  description: The districts API from keenethics-labs-com — 1 operation(s) for districts.
  name: keenethics-labs-com Districts API
  slug: keenethics-labs-com-districts-api
- baseURL: http://localhost:3000/api/
  baseurl_source: spec
  description: The events API from keenethics-labs-com — 1 operation(s) for events.
  name: keenethics-labs-com Events API
  slug: keenethics-labs-com-events-api
- baseURL: http://localhost:3000/api/
  baseurl_source: spec
  description: The feedbacks API from keenethics-labs-com — 1 operation(s) for feedbacks.
  name: keenethics-labs-com Feedbacks API
  slug: keenethics-labs-com-feedbacks-api
- baseURL: http://localhost:3000/api/
  baseurl_source: spec
  description: The navigation API from keenethics-labs-com — 1 operation(s) for navigation.
  name: keenethics-labs-com Navigation API
  slug: keenethics-labs-com-navigation-api
- baseURL: http://localhost:3000/api/
  baseurl_source: spec
  description: The search API from keenethics-labs-com — 3 operation(s) for search.
  name: keenethics-labs-com Search API
  slug: keenethics-labs-com-search-api
- baseURL: http://localhost:3000/api/
  baseurl_source: spec
  description: The specialization API from keenethics-labs-com — 1 operation(s) for specialization.
  name: keenethics-labs-com Specialization API
  slug: keenethics-labs-com-specialization-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/keenethics-labs-com/agentic-access/keenethics-labs-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/keenethics-labs-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/keenethics-labs-com/rules/keenethics-labs-com-rules.yml
  title: ''
  type: Spectral
  url: rules/keenethics-labs-com-rules.yml
- group: design
  href: https://artifacts.apis.io/keenethics-labs-com/json-ld/keenethics-labs-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/keenethics-labs-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/keenethics-labs-com/vocabulary/keenethics-labs-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/keenethics-labs-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/keenethics-labs-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/keenethics-labs-com/data-model/keenethics-labs-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/keenethics-labs-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/keenethics-labs-com/conformance/keenethics-labs-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/keenethics-labs-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/keenethics-labs-com/hosts/keenethics-labs-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/keenethics-labs-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/keenethics-labs-com/vendors/keenethics-labs-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/keenethics-labs-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/keenethics-labs-com/security/keenethics-labs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/keenethics-labs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://keenethics-labs.com/
- group: company
  title: ''
  type: Blog
  url: https://keenethics.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/keenethics
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://keenethics.com/privacy-policy
created: '2026-10-30'
description: Keenethics Labs is the R&D division of KeenEthics, focusing on experimental projects and innovations in web and mobile development. The lab showcases AI-powered demos, experimental applications, and cutting‑edge technologies, aiming to push the boundaries of modern software engineering. It operates as a showcase platform for internal prototypes and open‑source tools.
image: https://keenethics-labs.com/logo-labs.svg
json_schemas:
- name: ActivityType
  property_count: 8
  slug: keenethics-labs-com-activity-type
- name: Event
  property_count: 15
  slug: keenethics-labs-com-event
- name: SearchEntry
  property_count: 5
  slug: keenethics-labs-com-search-entry
- name: Specialization
  property_count: 3
  slug: keenethics-labs-com-specialization
jsonld:
- class_count: 11
  name: Keenethics Labs Com Context
  property_count: 56
  slug: keenethics-labs-com-context
layout: provider
modified: '2026-10-30'
name: keenethics-labs-com
nav: Providers
network: true
overview: 'keenethics-labs-com publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activity API, Districts API, Events API, and 4 more. Tagged areas include Company, R&D, Innovation, AI, and Web Development.


  The keenethics-labs-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  keenethics-labs-com''s developer surface includes engineering blog and 13 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: keenethics-labs-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: keenethics-labs-com-rules
scopes:
- name: Keenethics Labs Com Scopes
  scope_count: 0
  slug: keenethics-labs-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 26
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 51.6
    developer_ergonomics: 8.8
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Keenethics Labs Com Authentication
  slug: keenethics-labs-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Keenethics Labs Com Domain Security
  slug: keenethics-labs-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: entertainment-hub
  slug: keenethics-labs-com-entertainment-hub
slug: keenethics-labs-com
tags:
- Company
- R&D
- Innovation
- AI
- Web Development
- Experimental Projects
website: https://keenethics-labs.com/
---
