---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.0
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 9
  human_in_the_loop: 2
  name: Open Mobility Foundation Agentic Access
  operation_count: 38
  slug: open-mobility-foundation-agentic-access
  summary_line: 38 operations · 9 acting · 2 human-in-the-loop
api_count: 6
apis:
- description: The Events API from Open Mobility Foundation — 3 operation(s) for events.
  name: Open Mobility Foundation Events API
  slug: open-mobility-foundation-events-api
- description: The Geographies API from Open Mobility Foundation — 2 operation(s) for geographies.
  name: Open Mobility Foundation Geographies API
  slug: open-mobility-foundation-geographies-api
- description: The Geographies.json API from Open Mobility Foundation — 1 operation(s) for geographies.json.
  name: Open Mobility Foundation Geographies.json API
  slug: open-mobility-foundation-geographies-json-api
- description: The Jurisdictions API from Open Mobility Foundation — 2 operation(s) for jurisdictions.
  name: Open Mobility Foundation Jurisdictions API
  slug: open-mobility-foundation-jurisdictions-api
- description: The Jurisdictions.json API from Open Mobility Foundation — 1 operation(s) for jurisdictions.json.
  name: Open Mobility Foundation Jurisdictions.json API
  slug: open-mobility-foundation-jurisdictions-json-api
- description: The Metrics API from Open Mobility Foundation — 1 operation(s) for metrics.
  name: Open Mobility Foundation Metrics API
  slug: open-mobility-foundation-metrics-api
- description: The Policies API from Open Mobility Foundation — 2 operation(s) for policies.
  name: Open Mobility Foundation Policies API
  slug: open-mobility-foundation-policies-api
- description: The Policies.json API from Open Mobility Foundation — 1 operation(s) for policies.json.
  name: Open Mobility Foundation Policies.json API
  slug: open-mobility-foundation-policies-json-api
- description: The Reports API from Open Mobility Foundation — 2 operation(s) for reports.
  name: Open Mobility Foundation Reports API
  slug: open-mobility-foundation-reports-api
- description: The Requirements API from Open Mobility Foundation — 1 operation(s) for requirements.
  name: Open Mobility Foundation Requirements API
  slug: open-mobility-foundation-requirements-api
- description: The Stops API from Open Mobility Foundation — 2 operation(s) for stops.
  name: Open Mobility Foundation Stops API
  slug: open-mobility-foundation-stops-api
- description: The Telemetry API from Open Mobility Foundation — 1 operation(s) for telemetry.
  name: Open Mobility Foundation Telemetry API
  slug: open-mobility-foundation-telemetry-api
- description: The Trips API from Open Mobility Foundation — 1 operation(s) for trips.
  name: Open Mobility Foundation Trips API
  slug: open-mobility-foundation-trips-api
- description: The Value API from Open Mobility Foundation — 1 operation(s) for value.
  name: Open Mobility Foundation Value API
  slug: open-mobility-foundation-value-api
- description: The Vehicles API from Open Mobility Foundation — 4 operation(s) for vehicles.
  name: Open Mobility Foundation Vehicles API
  slug: open-mobility-foundation-vehicles-api
artifact_total: 44
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/open-mobility-foundation/refs/heads/main/agentic-access/open-mobility-foundation-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/open-mobility-foundation-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/open-mobility-foundation/refs/heads/main/rules/open-mobility-foundation-rules.yml
  title: ''
  type: Spectral
  url: rules/open-mobility-foundation-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/open-mobility-foundation/refs/heads/main/rules/open-mobility-foundation-mds-openapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/open-mobility-foundation-mds-openapi-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/open-mobility-foundation/refs/heads/main/json-ld/open-mobility-foundation-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/open-mobility-foundation-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/open-mobility-foundation/refs/heads/main/vocabulary/open-mobility-foundation-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/open-mobility-foundation-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/open-mobility-foundation/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/open-mobility-foundation/refs/heads/main/data-model/open-mobility-foundation-data-model.yml
  title: ''
  type: DataModel
  url: data-model/open-mobility-foundation-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/open-mobility-foundation/refs/heads/main/changelog/open-mobility-foundation-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/open-mobility-foundation-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/open-mobility-foundation/refs/heads/main/conventions/open-mobility-foundation-conventions.yml
  title: ''
  type: Conventions
  url: conventions/open-mobility-foundation-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/open-mobility-foundation/refs/heads/main/scopes/open-mobility-foundation-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/open-mobility-foundation-scopes.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://github.com/openmobilityfoundation/governance/blob/main/technical/ReleaseGuidelines.md#ongoing-version-support
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/open-mobility-foundation/refs/heads/main/lifecycle/open-mobility-foundation-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/open-mobility-foundation-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/open-mobility-foundation/refs/heads/main/errors/open-mobility-foundation-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/open-mobility-foundation-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/open-mobility-foundation/refs/heads/main/conformance/open-mobility-foundation-conformance.yml
  title: ''
  type: Conformance
  url: conformance/open-mobility-foundation-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/open-mobility-foundation/refs/heads/main/overlays/open-mobility-foundation-mds-agency-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/open-mobility-foundation-mds-agency-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/open-mobility-foundation/refs/heads/main/hosts/open-mobility-foundation-hosts.yml
  title: ''
  type: Hosts
  url: hosts/open-mobility-foundation-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/open-mobility-foundation/refs/heads/main/vendors/open-mobility-foundation-vendors.yml
  title: ''
  type: Vendors
  url: vendors/open-mobility-foundation-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/open-mobility-foundation/refs/heads/main/authentication/open-mobility-foundation-authentication.yml
  title: ''
  type: Authentication
  url: authentication/open-mobility-foundation-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/open-mobility-foundation/refs/heads/main/security/open-mobility-foundation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/open-mobility-foundation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.openmobilityfoundation.org/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/openmobilityfoundation/mobility-data-specification
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openmobilityfoundation
- group: company
  title: ''
  type: Blog
  url: https://www.openmobilityfoundation.org/blog/
- group: company
  title: ''
  type: Newsroom
  url: https://www.openmobilityfoundation.org/press
- group: operate
  title: ''
  type: Support
  url: https://www.openmobilityfoundation.org/get-in-touch/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.openmobilityfoundation.org/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.openmobilityfoundation.org/privacy-policy/
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/openmobilityfoundation/mds-openapi/blob/0c07bc3d294237dd41c6273f059efb11b8149c66/.spectral.yaml
created: '2026-10-09'
description: The Open Mobility Foundation (OMF) is a city-governed, open source foundation that stewards open data standards such as the Mobility Data Specification (MDS) and the Curb Data Specification (CDS), used by cities and their technology partners to manage shared mobility (scooters, bike share, car share, taxis, TNCs, AVs, delivery robots) and digitize public space and curbs. It brings together public and private sector stakeholders to develop the standards, OpenAPI definitions and tools for the public right-of-way.
image: https://www.openmobilityfoundation.org/wp-content/uploads/2022/03/OMF-Logo-Final-R.png
json_schemas:
- name: column
  property_count: 3
  slug: open-mobility-foundation-column
- name: data-types/iso-dayhourminute
  property_count: 0
  slug: open-mobility-foundation-data-types-iso-dayhourminute
- name: data-types/iso-duration
  property_count: 0
  slug: open-mobility-foundation-data-types-iso-duration
- name: data-types/timestamp
  property_count: 0
  slug: open-mobility-foundation-data-types-timestamp
- name: data-types/uuid
  property_count: 0
  slug: open-mobility-foundation-data-types-uuid
- name: models/event
  property_count: 0
  slug: open-mobility-foundation-event
- name: models/geography
  property_count: 9
  slug: open-mobility-foundation-geography
- name: models/jurisdiction
  property_count: 7
  slug: open-mobility-foundation-jurisdiction
- name: measures
  property_count: 0
  slug: open-mobility-foundation-measures
- name: models/mutable-stop
  property_count: 9
  slug: open-mobility-foundation-mutable-stop
- name: models/policy
  property_count: 11
  slug: open-mobility-foundation-policy
- name: query
  property_count: 7
  slug: open-mobility-foundation-query
- name: models/report
  property_count: 0
  slug: open-mobility-foundation-report
- name: models/requirements
  property_count: 2
  slug: open-mobility-foundation-requirements
- name: response/last_updated
  property_count: 1
  slug: open-mobility-foundation-response-last-updated
- name: response/version
  property_count: 1
  slug: open-mobility-foundation-response-version
- name: models/stop
  property_count: 0
  slug: open-mobility-foundation-stop
- name: models/telemetry
  property_count: 13
  slug: open-mobility-foundation-telemetry
- name: models/trip
  property_count: 0
  slug: open-mobility-foundation-trip
- name: models/vehicle
  property_count: 0
  slug: open-mobility-foundation-vehicle
jsonld:
- class_count: 37
  name: Open Mobility Foundation Context
  property_count: 101
  slug: open-mobility-foundation-context
layout: provider
modified: '2026-10-09'
name: Open Mobility Foundation
nav: Providers
network: true
overview: 'Open Mobility Foundation publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Events API, Geographies API, Geographies.json API, and 12 more. Tagged areas include Company, Mobility, Open Source, Open Standard, and Transportation.


  The Open Mobility Foundation catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Open Mobility Foundation''s developer surface includes changelog, authentication, documentation, engineering blog, support, and 23 more developer resources.'
plans:
- name: Open Mobility Foundation Plans Pricing
  plan_count: 0
  slug: open-mobility-foundation-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Open Mobility Foundation Rate Limits
  slug: open-mobility-foundation-rate-limits
rules:
- authorship: provider
  effective_rule_count: 42
  extends:
  - spectral:oas
  name: Open Mobility Foundation — mds openapi rules
  rule_count: 1
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 1
  slug: open-mobility-foundation-mds-openapi-spectral-rules
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Open Mobility Foundation API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: open-mobility-foundation-rules
scopes:
- name: Open Mobility Foundation Scopes
  scope_count: 2
  slug: open-mobility-foundation-scopes
  summary_line: 2 scopes
score:
  band: developing
  composite: 41.6
  coverage:
    artifact_dirs: 27
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 21.1
    contract_governance: 35.6
    contract_quality: 58.7
    developer_ergonomics: 30.4
    discoverability: 64.3
    operational_transparency: 28.9
  previous_composite: 47.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/open-mobility-foundation/refs/heads/main/screenshots/open-mobility-foundation-2026-10-11T112037.png
security:
- kind: authentication
  name: Open Mobility Foundation Authentication
  slug: open-mobility-foundation-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Open Mobility Foundation Domain Security
  slug: open-mobility-foundation-domain-security
  summary_line: TLSv1.3 · DMARC
slug: open-mobility-foundation
tags:
- Company
- Mobility
- Open Source
- Open Standard
- Transportation
- Cities
- Micromobility
- Data Specifications
website: https://www.openmobilityfoundation.org/
---
