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
  - '{''url'': ''https://safetyculture.com'', ''status'': 301, ''note'': ''declared website redirects to https://mitti.com/ — a different registrable domain (safetyculture.com -> mitti.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 219
  human_in_the_loop: 4
  name: Safetyculture Agentic Access
  operation_count: 416
  slug: safetyculture-agentic-access
  summary_line: 416 operations · 219 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.safetyculture.io
  baseurl_source: declared
  description: The Actions API from SafetyCulture — 30 operation(s) for actions.
  name: SafetyCulture Actions API
  slug: safetyculture-actions-api
- baseURL: https://api.safetyculture.io
  baseurl_source: declared
  description: The Apps API from SafetyCulture — 7 operation(s) for apps.
  name: SafetyCulture Apps API
  slug: safetyculture-apps-api
- baseURL: https://api.safetyculture.io
  baseurl_source: declared
  description: The Assets API from SafetyCulture — 34 operation(s) for assets.
  name: SafetyCulture Assets API
  slug: safetyculture-assets-api
- baseURL: https://api.safetyculture.io
  baseurl_source: declared
  description: The Bulk user operations API from SafetyCulture — 4 operation(s) for bulk user operations.
  name: SafetyCulture Bulk user operations API
  slug: safetyculture-bulk-user-operations-api
- baseURL: https://api.safetyculture.io
  baseurl_source: declared
  description: The Companies API from SafetyCulture — 9 operation(s) for companies.
  name: SafetyCulture Companies API
  slug: safetyculture-companies-api
- baseURL: https://api.safetyculture.io
  baseurl_source: declared
  description: The Credentials API from SafetyCulture — 9 operation(s) for credentials.
  name: SafetyCulture Credentials API
  slug: safetyculture-credentials-api
- baseURL: https://api.safetyculture.io
  baseurl_source: declared
  description: The Data Feeds API from SafetyCulture — 39 operation(s) for data feeds.
  name: SafetyCulture Data Feeds API
  slug: safetyculture-data-feeds-api
- baseURL: https://api.safetyculture.io
  baseurl_source: declared
  description: The Directory (Sites) API from SafetyCulture — 13 operation(s) for directory (sites).
  name: SafetyCulture Directory (Sites) API
  slug: safetyculture-directory-sites-api
- baseURL: https://api.safetyculture.io
  baseurl_source: declared
  description: The Documents API from SafetyCulture — 10 operation(s) for documents.
  name: SafetyCulture Documents API
  slug: safetyculture-documents-api
- baseURL: https://api.safetyculture.io
  baseurl_source: declared
  description: The Groups API from SafetyCulture — 7 operation(s) for groups.
  name: SafetyCulture Groups API
  slug: safetyculture-groups-api
- baseURL: https://api.safetyculture.io
  baseurl_source: declared
  description: The Heads Up API from SafetyCulture — 5 operation(s) for heads up.
  name: SafetyCulture Heads Up API
  slug: safetyculture-heads-up-api
- baseURL: https://api.safetyculture.io
  baseurl_source: declared
  description: The Inspections API from SafetyCulture — 26 operation(s) for inspections.
  name: SafetyCulture Inspections API
  slug: safetyculture-inspections-api
- baseURL: https://api.safetyculture.io
  baseurl_source: declared
  description: The Investigations API from SafetyCulture — 27 operation(s) for investigations.
  name: SafetyCulture Investigations API
  slug: safetyculture-investigations-api
- baseURL: https://api.safetyculture.io
  baseurl_source: declared
  description: The Issues API from SafetyCulture — 24 operation(s) for issues.
  name: SafetyCulture Issues API
  slug: safetyculture-issues-api
- baseURL: https://api.safetyculture.io
  baseurl_source: declared
  description: The Lone Worker API from SafetyCulture — 2 operation(s) for lone worker.
  name: SafetyCulture Lone Worker API
  slug: safetyculture-lone-worker-api
- baseURL: https://api.safetyculture.io
  baseurl_source: declared
  description: The Media API from SafetyCulture — 1 operation(s) for media.
  name: SafetyCulture Media API
  slug: safetyculture-media-api
- baseURL: https://api.safetyculture.io
  baseurl_source: declared
  description: The OSHA API from SafetyCulture — 8 operation(s) for osha.
  name: SafetyCulture OSHA API
  slug: safetyculture-osha-api
- baseURL: https://api.safetyculture.io
  baseurl_source: declared
  description: The Response Sets API from SafetyCulture — 5 operation(s) for response sets.
  name: SafetyCulture Response Sets API
  slug: safetyculture-response-sets-api
- baseURL: https://api.safetyculture.io
  baseurl_source: declared
  description: The Roles API from SafetyCulture — 3 operation(s) for roles.
  name: SafetyCulture Roles API
  slug: safetyculture-roles-api
- baseURL: https://api.safetyculture.io
  baseurl_source: declared
  description: The Schedules API from SafetyCulture — 12 operation(s) for schedules.
  name: SafetyCulture Schedules API
  slug: safetyculture-schedules-api
- baseURL: https://api.safetyculture.io
  baseurl_source: declared
  description: The Schedules (legacy) API from SafetyCulture — 2 operation(s) for schedules (legacy).
  name: SafetyCulture Schedules (legacy) API
  slug: safetyculture-schedules-legacy-api
- baseURL: https://api.safetyculture.io
  baseurl_source: declared
  description: The Sensors API from SafetyCulture — 7 operation(s) for sensors.
  name: SafetyCulture Sensors API
  slug: safetyculture-sensors-api
- baseURL: https://api.safetyculture.io
  baseurl_source: declared
  description: The Structures API from SafetyCulture — 11 operation(s) for structures.
  name: SafetyCulture Structures API
  slug: safetyculture-structures-api
- baseURL: https://api.safetyculture.io
  baseurl_source: declared
  description: The Templates API from SafetyCulture — 7 operation(s) for templates.
  name: SafetyCulture Templates API
  slug: safetyculture-templates-api
- baseURL: https://api.safetyculture.io
  baseurl_source: declared
  description: The Training API from SafetyCulture — 24 operation(s) for training.
  name: SafetyCulture Training API
  slug: safetyculture-training-api
- baseURL: https://api.safetyculture.io
  baseurl_source: declared
  description: The Users API from SafetyCulture — 14 operation(s) for users.
  name: SafetyCulture Users API
  slug: safetyculture-users-api
- baseURL: https://api.safetyculture.io
  baseurl_source: declared
  description: The Webhooks API from SafetyCulture — 3 operation(s) for webhooks.
  name: SafetyCulture Webhooks API
  slug: safetyculture-webhooks-api
artifact_total: 48
asyncapis:
- description: ''
  name: Safetyculture Webhooks
  slug: safetyculture-webhooks
common:
- group: other
  href: https://artifacts.apis.io/safetyculture/capabilities/safetyculture-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/safetyculture-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/safetyculture/plans/safetyculture-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/safetyculture-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/safetyculture/agentic-access/safetyculture-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/safetyculture-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/safetyculture/rules/safetyculture-rules.yml
  title: ''
  type: Spectral
  url: rules/safetyculture-rules.yml
- group: design
  href: https://artifacts.apis.io/safetyculture/json-ld/safetyculture-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/safetyculture-context.jsonld
- group: design
  href: https://artifacts.apis.io/safetyculture/vocabulary/safetyculture-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/safetyculture-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/safetyculture/data-model/safetyculture-data-model.yml
  title: ''
  type: DataModel
  url: data-model/safetyculture-data-model.yml
- group: operate
  href: https://artifacts.apis.io/safetyculture/lifecycle/safetyculture-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/safetyculture-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/safetyculture/errors/safetyculture-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/safetyculture-problem-types.yml
- group: other
  href: https://artifacts.apis.io/safetyculture/hosts/safetyculture-hosts.yml
  title: ''
  type: Hosts
  url: hosts/safetyculture-hosts.yml
- group: other
  href: https://artifacts.apis.io/safetyculture/vendors/safetyculture-vendors.yml
  title: ''
  type: Vendors
  url: vendors/safetyculture-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://safetyculture.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.safetyculture.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.safetyculture.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.safetyculture.com/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.safetyculture.com/reference/getting-started
- group: company
  title: ''
  type: Blog
  url: https://safetyculture.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://safetyculture.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.safetyculture.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://safetyculture.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://safetyculture.com/legal/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://safetyculture.com/partner-program/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SafetyCulture
- group: operate
  title: ''
  type: StatusPage
  url: https://status.safetyculture.com
- group: auth
  href: https://artifacts.apis.io/safetyculture/authentication/safetyculture-authentication.yml
  title: ''
  type: Authentication
  url: authentication/safetyculture-authentication.yml
- group: agent
  href: https://artifacts.apis.io/safetyculture/llms/safetyculture-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/safetyculture-llms.txt
- group: agent
  href: https://artifacts.apis.io/safetyculture/well-known/safetyculture-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/safetyculture-well-known.yml
- group: auth
  href: https://artifacts.apis.io/safetyculture/well-known/safetyculture-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/safetyculture-security.txt
- group: operate
  href: https://artifacts.apis.io/safetyculture/rate-limits/safetyculture-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/safetyculture-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/safetyculture/asyncapi/safetyculture-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/safetyculture-webhooks.yml
- group: design
  href: https://artifacts.apis.io/safetyculture/conventions/safetyculture-conventions.yml
  title: ''
  type: Conventions
  url: conventions/safetyculture-conventions.yml
- group: design
  href: https://artifacts.apis.io/safetyculture/lifecycle/safetyculture-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/safetyculture-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/safetyculture/conformance/safetyculture-conformance.yml
  title: ''
  type: Conformance
  url: conformance/safetyculture-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://safetyculture.com/security
- group: build
  href: https://artifacts.apis.io/safetyculture/packages/safetyculture-packages.yml
  title: ''
  type: Packages
  url: packages/safetyculture-packages.yml
- group: build
  href: https://artifacts.apis.io/safetyculture/packages/safetyculture-packages.yml
  title: ''
  type: SDKs
  url: packages/safetyculture-packages.yml
- group: build
  href: https://artifacts.apis.io/safetyculture/cli/safetyculture-cli.yml
  title: ''
  type: CLI
  url: cli/safetyculture-cli.yml
- group: agent
  href: https://artifacts.apis.io/safetyculture/mcp/safetyculture-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/safetyculture-mcp.yml
- group: agent
  href: https://artifacts.apis.io/safetyculture/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/safetyculture/security/safetyculture-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/safetyculture-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/safetyculture/security/safetyculture-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/safetyculture-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://safetyculture.com/security
- group: auth
  href: https://artifacts.apis.io/safetyculture/security/safetyculture-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/safetyculture-trust-center.yml
created: '2026-07-17'
description: SafetyCulture (formerly iAuditor) is a workplace operations and safety platform used by frontline teams to run inspections, capture and track issues, assign corrective actions, manage assets and sites, deliver training, and provision users. Its public REST API at https://api.safetyculture.io exposes more than 380 documented operations across inspections, templates, assets, actions, issues, users, groups, schedules, training, credentials, and webhooks, secured with bearer API tokens (service-user and personal). Near real-time webhooks stream a rich catalog of inspection, action, incident, media, and training events, and SCIM 2.0 supports user provisioning via Microsoft Entra ID and Okta.
finops:
- has_sources: true
  method: derived
  name: Safetyculture Finops
  primary_unit: seat
  service_category: ''
  slug: safetyculture-finops
  template: false
image: https://safetyculture.com/favicon.ico
json_schemas:
- name: s12.incidents.v1.CreateCaseRequest
  property_count: 35
  slug: safetyculture-s12-incidents-v1-create-case-request
- name: s12.incidents.v1.OSHAService.UpdateCaseBody
  property_count: 2
  slug: safetyculture-s12-incidents-v1-oshaservice-update-case-body
- name: UpdateScheduleItem
  property_count: 20
  slug: safetyculture-s12-schedules-v1-update-schedule-item
- name: CreateActionRequest represents the parameters to `CreateAction`
  property_count: 18
  slug: safetyculture-s12-tasks-v1-create-action-request
- name: CreateIncidentRequest represents the parameters to `CreateIncident`
  property_count: 14
  slug: safetyculture-s12-tasks-v1-create-incident-request
- name: SubmitIncidentRequest represents the incident submitted by a contributor
  property_count: 19
  slug: safetyculture-s12-tasks-v1-submit-incident-request
jsonld:
- class_count: 120
  name: Safetyculture Context
  property_count: 157
  slug: safetyculture-context
layout: provider
modified: '2026-07-21'
name: SafetyCulture
nav: Providers
network: true
overview: 'SafetyCulture publishes 27 API contracts indexed on the [APIs.io](https://apis.io/) network, including Actions API, Apps API, Assets API, and 24 more. Tagged areas include Company, Business Applications, Safety, Inspection, and Workplace Operations.


  The SafetyCulture catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  SafetyCulture''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 36 more developer resources.'
plans:
- name: Safetyculture Plans Pricing
  plan_count: 5
  slug: safetyculture-plans-pricing
- name: Safetyculture Price Estimates
  plan_count: 0
  slug: safetyculture-price-estimates
random_paper: 8
rate_limits:
- limit_count: 6
  name: Safetyculture Rate Limits
  slug: safetyculture-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: SafetyCulture API Rules
  rule_count: 13
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 3
  slug: safetyculture-rules
score:
  band: exemplar
  composite: 75.5
  coverage:
    artifact_dirs: 30
    catalog_earned: 89.8
    catalog_earned_first_party: 24.0
    catalog_gap: 25.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 100.0
    contract_governance: 35.6
    contract_quality: 66.8
    developer_ergonomics: 73.2
    discoverability: 66.1
    operational_transparency: 78.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 75.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 27
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/safetyculture/safetyculture-2026-08-17T081708.png
security:
- kind: authentication
  name: Safetyculture Authentication
  slug: safetyculture-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Safetyculture Domain Security
  slug: safetyculture-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Safetyculture Vulnerability Disclosure
  slug: safetyculture-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Safetyculture Trust Center
  slug: safetyculture-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 3
skills:
- name: Capture and track an issue
  slug: safetyculture-capture-and-track-issue
- name: Provision users and groups
  slug: safetyculture-provision-users-and-groups
- name: Subscribe to SafetyCulture events with webhooks
  slug: safetyculture-subscribe-to-events
slug: safetyculture
tags:
- Company
- Business Applications
- Safety
- Inspection
- Workplace Operations
- EHS
- Compliance
- Training
- Field Service Management
- Webhook
- Australia
website: https://safetyculture.com
---
