---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://ckm.openehr.org/ckm/rest/v1
  baseurl_source: declared
  description: Endpoint for archetype-related services, including listing and getting archetypes.
  name: Ocean Health Systems Archetypes API
  slug: ocean-health-systems-archetypes-api
- baseURL: https://ckm.openehr.org/ckm/rest/v1
  baseurl_source: declared
  description: Endpoint for change request-related services, including listing and getting change requests.
  name: Ocean Health Systems Change Requests API
  slug: ocean-health-systems-change-requests-api
- baseURL: https://ckm.openehr.org/ckm/rest/v1
  baseurl_source: declared
  description: Endpoint for project-related services, including listing and getting projects.
  name: Ocean Health Systems Projects API
  slug: ocean-health-systems-projects-api
- baseURL: https://ckm.openehr.org/ckm/rest/v1
  baseurl_source: declared
  description: Endpoint for resource proposal-related services, including listing and getting resource proposals.
  name: Ocean Health Systems Resource Proposals API
  slug: ocean-health-systems-resource-proposals-api
- baseURL: https://ckm.openehr.org/ckm/rest/v1
  baseurl_source: declared
  description: Endpoint for generic resources, including archetypes and templates. May sometimes be easier to use.
  name: Ocean Health Systems Resources API
  slug: ocean-health-systems-resources-api
- baseURL: https://ckm.openehr.org/ckm/rest/v1
  baseurl_source: declared
  description: Endpoint for creating a new user session or signing out.
  name: Ocean Health Systems Sessions API
  slug: ocean-health-systems-sessions-api
- baseURL: https://ckm.openehr.org/ckm/rest/v1
  baseurl_source: declared
  description: Endpoint for subdomain-related services, including listing and getting subdomains.
  name: Ocean Health Systems Subdomains API
  slug: ocean-health-systems-subdomains-api
- baseURL: https://ckm.openehr.org/ckm/rest/v1
  baseurl_source: declared
  description: Endpoint for template-related services, including listing and getting templates.
  name: Ocean Health Systems Templates API
  slug: ocean-health-systems-templates-api
- baseURL: https://ckm.openehr.org/ckm/rest/v1
  baseurl_source: declared
  description: Endpoint for user-related services, including creating new users as an admin.
  name: Ocean Health Systems Users API
  slug: ocean-health-systems-users-api
artifact_total: 17
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
  href: https://artifacts.apis.io/ocean-health-systems/openapi/ocean-health-systems-ckm-rest-api-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/ocean-health-systems-ckm-rest-api-openapi.json
- group: other
  href: https://artifacts.apis.io/ocean-health-systems/overlays/ocean-health-systems-ckm-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ocean-health-systems-ckm-rest-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/ocean-health-systems/authentication/ocean-health-systems-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ocean-health-systems-authentication.yml
- group: design
  href: https://artifacts.apis.io/ocean-health-systems/conventions/ocean-health-systems-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ocean-health-systems-conventions.yml
- group: design
  href: https://artifacts.apis.io/ocean-health-systems/errors/ocean-health-systems-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ocean-health-systems-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ocean-health-systems/data-model/ocean-health-systems-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ocean-health-systems-data-model.yml
- group: design
  href: https://artifacts.apis.io/ocean-health-systems/conformance/ocean-health-systems-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ocean-health-systems-conformance.yml
- group: design
  href: https://artifacts.apis.io/ocean-health-systems/lifecycle/ocean-health-systems-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ocean-health-systems-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/ocean-health-systems/changelog/ocean-health-systems-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ocean-health-systems-changelog.yml
- group: build
  href: https://artifacts.apis.io/ocean-health-systems/packages/ocean-health-systems-packages.yml
  title: ''
  type: Packages
  url: packages/ocean-health-systems-packages.yml
- group: commercial
  href: https://artifacts.apis.io/ocean-health-systems/plans/ocean-health-systems-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ocean-health-systems-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/ocean-health-systems/rate-limits/ocean-health-systems-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ocean-health-systems-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/ocean-health-systems/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/ocean-health-systems/llms/ocean-health-systems-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ocean-health-systems-llms.txt
- group: auth
  href: https://artifacts.apis.io/ocean-health-systems/security/ocean-health-systems-domain-security.yml
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
overview: 'Ocean Health Systems publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Archetypes API, Change Requests API, Projects API, and 6 more. Tagged areas include Health, Healthcare, Electronic Health Records, openEHR, and Clinical Data.


  The Ocean Health Systems catalog on APIs.io includes 1 Spectral governance ruleset.


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
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Ocean Health Systems API Rules
  rule_count: 62
  severity_counts:
    error: 55
    hint: 0
    info: 1
    warn: 6
  slug: ocean-health-systems-rules
score:
  band: thin
  composite: 35.1
  coverage:
    artifact_dirs: 23
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 47.3
    developer_ergonomics: 37.5
    discoverability: 66.1
    operational_transparency: 18.4
  previous_composite: 34.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/ocean-health-systems/ocean-health-systems-2026-10-11T111734.png
security:
- kind: authentication
  name: Ocean Health Systems Authentication
  slug: ocean-health-systems-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Ocean Health Systems Domain Security
  slug: ocean-health-systems-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: ocean-health-systems-audit-model-governance
  slug: ocean-health-systems-audit-model-governance
- name: ocean-health-systems-discover-clinical-models
  slug: ocean-health-systems-discover-clinical-models
- name: ocean-health-systems-publish-a-template
  slug: ocean-health-systems-publish-a-template
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
- immunisation
website: https://oceanhealthsystems.com/
---
