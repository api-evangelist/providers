---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://ckm.openehr.org/ckm/rest/v1
  baseurl_source: declared
  description: REST API for the Clinical Knowledge Manager — 48 operations across 39 paths covering archetypes (list, search, ADL/XML/mindmap retrieval, specialisation parent, status by asset version, MD5 hash, impo
  name: CKM REST API
  slug: ckm-rest-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://oceanhealthsystems.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ckm.openehr.org/ckm/rest-doc/
- group: docs
  title: ''
  type: APIReference
  url: https://ckm.openehr.org/ckm/rest-doc/
- group: operate
  title: ''
  type: Support
  url: https://oceanehr.atlassian.net/servicedesk/customer/portal/15
- group: company
  title: ''
  type: Blog
  url: https://oceanhealthsystems.com/media/
- group: company
  title: ''
  type: BlogRSS
  url: https://oceanhealthsystems.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OceanHealthSystems
- group: commercial
  title: ''
  type: TermsOfService
  url: https://oceanhealthsystems.com/fair-use-policy/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://oceanhealthsystems.com/privacy-policy/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/ocean-health-systems-ckm-rest-api-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/ocean-health-systems-ckm-rest-api-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ocean-health-systems-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ocean-health-systems-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ocean-health-systems-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ocean-health-systems-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ocean-health-systems-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ocean-health-systems-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ocean-health-systems-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/ocean-health-systems-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ocean-health-systems-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ocean-health-systems-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ocean-health-systems-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ocean-health-systems-domain-security.yml
created: '2026-09-02'
description: Ocean Health Systems (legally Ocean Informatics Pty Ltd, founded 1998, with offices in Bundall QLD, Chatswood NSW and London) is the Australian clinical-informatics company whose founders commercialised the first openEHR clinical data repository and built Clinical Knowledge Manager (CKM) — the repository and collaborative governance environment in which openEHR archetypes, templates, terminology subsets and release sets are authored, peer reviewed, semantically versioned, approved and published, with terminology binding to SNOMED CT and LOINC and mappings out to FHIR and OMOP. CKM runs the international openEHR community instance as well as national and vendor deployments, and ships a documented Swagger 2.0 REST API (48 operations) for discovering models and pulling their ADL, XML, OET and Operational Template representations. Ocean also builds Multiprac Immunize and Multiprac Surveillance for immunisation and infection prevention, and publishes the free Archetype Editor and
  Template Designer authoring tools.
image: https://oceanhealthsystems.com/wp-content/uploads/2023/09/Asset-33@300x-e1695112566701.png
layout: provider
modified: '2026-09-02'
name: Ocean Health Systems
nav: Providers
network: true
overview: 'Ocean Health Systems publishes 1 API on the [APIs.io](https://apis.io/) network: CKM REST API. Tagged areas include Health, Healthcare, Electronic Health Records, openEHR, and Clinical Data.


  Ocean Health Systems'' developer surface includes documentation, API reference, support, engineering blog, authentication, changelog, and 18 more developer resources.'
plans:
- name: Ocean Health Systems Plans Pricing
  plan_count: 0
  slug: ocean-health-systems-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Ocean Health Systems Rate Limits
  slug: ocean-health-systems-rate-limits
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 33.3
    developer_ergonomics: 37.5
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 32.1
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Ocean Health Systems Authentication
  slug: ocean-health-systems-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Ocean Health Systems Domain Security
  slug: ocean-health-systems-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ocean-health-systems
tags:
- Health
- Healthcare
- Electronic Health Records
- openEHR
- Clinical Data
- Clinical Knowledge Management
- Interoperability
- Health Informatics
- Terminology
- Archetypes
- Infection Prevention
- Immunisation
website: https://oceanhealthsystems.com/
---
