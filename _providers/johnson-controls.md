---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Johnson Controls Agentic Access
  operation_count: 70
  slug: johnson-controls-agentic-access
  summary_line: 70 operations · 16 acting
api_count: 1
apis:
- baseURL: https://{hostname}/api/v6
  baseurl_source: declared
  description: 'This section describes the operations you can perform on activities. Activities are a superset of all alarms and audits in a Metasys system. Use activities operations to view audits and alarms. Apply '
  name: Johnson Controls Activities API
  slug: johnson-controls-activities-api
- baseURL: https://{hostname}/api/v6
  baseurl_source: declared
  description: Alarms alert users to potential problems identified by a Metasys system, for example high zone temperatures. Use alarms operations to get object alarms, network device alarms, single alarms, alarm col
  name: Johnson Controls Alarms API
  slug: johnson-controls-alarms-api
- baseURL: https://{hostname}/api/v6
  baseurl_source: declared
  description: 'How to retrieve, discard, and annotate audits. ### Relationships Audits have relationships to other resources in the system. Find information about the most important below. - **objects** When users o'
  name: Johnson Controls Audits API
  slug: johnson-controls-audits-api
- baseURL: https://{hostname}/api/v6
  baseurl_source: declared
  description: Operations to get and refresh an access token.
  name: Johnson Controls Authentication API
  slug: johnson-controls-authentication-api
- baseURL: https://{hostname}/api/v6
  baseurl_source: declared
  description: This section describes the operations you can perform on equipment. Equipment is a broad term for anything that makes a building run, including boilers, chillers, air handling units, lights, meters, a
  name: Johnson Controls Equipment API
  slug: johnson-controls-equipment-api
- baseURL: https://{hostname}/api/v6
  baseurl_source: declared
  description: 'This section describes the operations you can perform on network devices. Network devices are physical devices such as coordinators and routers that are required for communication between hardware on '
  name: Johnson Controls network devices API
  slug: johnson-controls-network-devices-api
- baseURL: https://{hostname}/api/v6
  baseurl_source: declared
  description: 'This section describes the operations you can perform on objects. Objects are self-contained functional items in the Metasys system, for a full definition refer to the [Metasys System Glossary](https:'
  name: Johnson Controls Objects API
  slug: johnson-controls-objects-api
- baseURL: https://{hostname}/api/v6
  baseurl_source: declared
  description: A collection of JSON schemas for describing enumerations and object types.
  name: Johnson Controls Schemas API
  slug: johnson-controls-schemas-api
- baseURL: https://{hostname}/api/v6
  baseurl_source: declared
  description: Operations on space-related resources.
  name: Johnson Controls Spaces API
  slug: johnson-controls-spaces-api
- baseURL: https://{hostname}/api/v6
  baseurl_source: declared
  description: 'Your Metasys system works continuously: sensors report current conditions, algorithms make adjustments, and alarms alert operators to potential issues. Streaming is how the Metasys API provides access'
  name: Johnson Controls Streaming API
  slug: johnson-controls-streaming-api
- baseURL: https://{hostname}/api/v6
  baseurl_source: declared
  description: 'This section describes the operations you can perform on time series sample data. ### Origin of Time Series data The Metasys system has two locations from which time series samples can be retrieved. T'
  name: Johnson Controls time series API
  slug: johnson-controls-time-series-api
artifact_total: 27
common:
- group: other
  href: https://artifacts.apis.io/johnson-controls/capabilities/johnson-controls-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/johnson-controls-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/johnson-controls/agentic-access/johnson-controls-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/johnson-controls-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/johnson-controls/rules/johnson-controls-rules.yml
  title: ''
  type: Spectral
  url: rules/johnson-controls-rules.yml
- group: design
  href: https://artifacts.apis.io/johnson-controls/json-ld/johnson-controls-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/johnson-controls-context.jsonld
- group: design
  href: https://artifacts.apis.io/johnson-controls/vocabulary/johnson-controls-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/johnson-controls-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/johnson-controls/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/johnson-controls/data-model/johnson-controls-data-model.yml
  title: ''
  type: DataModel
  url: data-model/johnson-controls-data-model.yml
- group: build
  href: https://artifacts.apis.io/johnson-controls/cli/johnson-controls-cli.yml
  title: ''
  type: CLI
  url: cli/johnson-controls-cli.yml
- group: operate
  href: https://artifacts.apis.io/johnson-controls/changelog/johnson-controls-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/johnson-controls-changelog.yml
- group: design
  href: https://artifacts.apis.io/johnson-controls/conventions/johnson-controls-conventions.yml
  title: ''
  type: Conventions
  url: conventions/johnson-controls-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.johnsoncontrols.com/
- group: design
  href: https://artifacts.apis.io/johnson-controls/lifecycle/johnson-controls-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/johnson-controls-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/johnson-controls/errors/johnson-controls-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/johnson-controls-problem-types.yml
- group: design
  href: https://artifacts.apis.io/johnson-controls/conformance/johnson-controls-conformance.yml
  title: ''
  type: Conformance
  url: conformance/johnson-controls-conformance.yml
- group: other
  href: https://artifacts.apis.io/johnson-controls/overlays/johnson-controls-metasys-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/johnson-controls-metasys-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/johnson-controls/llms/johnson-controls-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/johnson-controls-llms.txt
- group: other
  href: https://artifacts.apis.io/johnson-controls/hosts/johnson-controls-hosts.yml
  title: ''
  type: Hosts
  url: hosts/johnson-controls-hosts.yml
- group: build
  href: https://artifacts.apis.io/johnson-controls/integrations/johnson-controls-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/johnson-controls-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/johnson-controls/vendors/johnson-controls-vendors.yml
  title: ''
  type: Vendors
  url: vendors/johnson-controls-vendors.yml
- group: build
  href: https://artifacts.apis.io/johnson-controls/packages/johnson-controls-packages.yml
  title: ''
  type: SDKs
  url: packages/johnson-controls-packages.yml
- group: build
  href: https://artifacts.apis.io/johnson-controls/packages/johnson-controls-packages.yml
  title: ''
  type: Packages
  url: packages/johnson-controls-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.johnsoncontrols.com/security
- group: start
  title: ''
  type: GettingStarted
  url: https://www.johnsoncontrols.com/services-and-support/fire-maintenance-and-support/connected-sprinkler-service/onboarding
- group: auth
  href: https://artifacts.apis.io/johnson-controls/authentication/johnson-controls-authentication.yml
  title: ''
  type: Authentication
  url: authentication/johnson-controls-authentication.yml
- group: auth
  href: https://artifacts.apis.io/johnson-controls/security/johnson-controls-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/johnson-controls-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/johnson-controls/security/johnson-controls-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/johnson-controls-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/johnsoncontrols
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/johnson-controls
- group: company
  title: ''
  type: Website
  url: https://www.johnsoncontrols.com/
- group: other
  title: ''
  type: OpenBlue
  url: https://www.johnsoncontrols.com/openblue
- group: docs
  title: ''
  type: Documentation
  url: https://jci-metasys.github.io/api-landing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jci-metasys
- group: operate
  title: ''
  type: Support
  url: https://www.johnsoncontrols.com/services-and-support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.johnsoncontrols.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.johnsoncontrols.com/trust-center/privacy
- group: start
  title: ''
  type: Login
  url: https://www.johnsoncontrols.com/login
- group: company
  title: ''
  type: Newsroom
  url: https://www.johnsoncontrols.com/media-center/news
created: '2026-03-24'
description: Johnson Controls is a global diversified technology and multi-industrial leader serving customers in over 150 countries, providing products, services, and solutions for buildings (HVAC, fire, security, building automation), energy storage, and connected building platforms (Metasys, OpenBlue). Its developer surface is the Metasys REST API, served by each customer's own Metasys site director and documented publicly (with a versioned OpenAPI reference) at jci-metasys.github.io/api-landing.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/johnson-controls.png
json_schemas:
- name: activities
  property_count: 5
  slug: johnson-controls-activities
- name: alarm
  property_count: 24
  slug: johnson-controls-alarm
- name: audit
  property_count: 24
  slug: johnson-controls-audit
- name: Equipment
  property_count: 17
  slug: johnson-controls-equipment-item
- name: equipmentPoints
  property_count: 5
  slug: johnson-controls-equipment-points
- name: networkDevice
  property_count: 26
  slug: johnson-controls-network-device
jsonld:
- class_count: 62
  name: Johnson Controls Context
  property_count: 116
  slug: johnson-controls-context
layout: provider
modified: '2026-10-20'
name: Johnson Controls
nav: Providers
network: true
overview: 'Johnson Controls publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activities API, Alarms API, Audits API, and 8 more. Tagged areas include Building Automation, Energy Storage, Fire & Security, HVAC, and Smart Buildings.


  The Johnson Controls catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Johnson Controls'' developer surface includes CLI, changelog, getting-started guide, authentication, documentation, support, and 31 more developer resources.'
plans:
- name: Johnson Controls Plans Pricing
  plan_count: 0
  slug: johnson-controls-plans-pricing
press:
- date: ''
  title: How AI is Transforming the Built Environment
  url: https://www.johnsoncontrols.co.uk/media-center/2024/april/ai-in-the-built-environment
- date: ''
  title: Johnson Controls completes sale of residential and light ...
  url: https://www.johnsoncontrols.com/media-center/news/press-releases/2025/08/01/johnson-controls-completes-sale-of-residential-and-light-commercial-hvac-business
- date: ''
  title: Johnson Controls launches series of thermal management ...
  url: https://www.prnewswire.com/news-releases/johnson-controls-launches-series-of-thermal-management-reference-design-guides-for-gigawatt-scale-ai-data-centers-302676158.html
- date: ''
  title: Scaling AI means delivering data centers on time ...
  url: https://www.facebook.com/JohnsonControls/posts/scaling-ai-means-delivering-data-centers-on-time-anywhere-johnson-controls-is-gr/1168072228697473/
- date: ''
  title: Johnson Controls expands AI features in OpenBlue digital ...
  url: https://www.johnsoncontrols.com/media-center/news/press-releases/2024/11/12/johnson-controls-expands-ai-features-in-openblue
random_paper: 16
rate_limits:
- limit_count: 0
  name: Johnson Controls Rate Limits
  slug: johnson-controls-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Johnson Controls API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: johnson-controls-rules
score:
  band: developing
  composite: 50.5
  coverage:
    artifact_dirs: 32
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    contract_governance: 22.0
    contract_quality: 57.6
    developer_ergonomics: 54.2
    discoverability: 67.9
    operational_transparency: 31.6
  previous_composite: 50.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 24.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/johnson-controls/johnson-controls-2026-06-20T183753.png
security:
- kind: authentication
  name: Johnson Controls Authentication
  slug: johnson-controls-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Johnson Controls Domain Security
  slug: johnson-controls-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Johnson Controls Trust Center
  slug: johnson-controls-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, FedRAMP, GDPR
skill_count: 2
skills:
- name: command-an-object
  slug: johnson-controls-command-an-object
- name: read-object-attributes
  slug: johnson-controls-read-object-attributes
slug: johnson-controls
tags:
- Building Automation
- Energy Storage
- Fire & Security
- HVAC
- Smart Buildings
- Fortune 100
website: https://www.johnsoncontrols.com/
---
