---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Agco Agentic Access
  operation_count: 3
  slug: agco-agentic-access
  summary_line: 3 operations
api_count: 3
apis:
- description: Access machine location and tracking data.
  name: agco Locations API
  slug: agco-locations-api
- description: Access machine information and status.
  name: agco Machines API
  slug: agco-machines-api
- description: Retrieve machine telemetry and sensor data.
  name: agco Telemetry API
  slug: agco-telemetry-api
artifact_total: 34
collections:
- collection_type: open
  name: AGCO AgCommand API
  slug: open-agco-agcommand-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/agco-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agco-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agco-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agco-corporation
- group: start
  title: ''
  type: Portal
  url: https://get.agcoconnect.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/agco/agco-json-api-profiles
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agco
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agcocorp.com/legal/privacy-policy.html
- group: company
  title: ''
  type: Blog
  url: https://news.agcocorp.com/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/agco-location-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/agco-machine-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/agco-telemetry-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/agco-location-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/agco-machine-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/agco-telemetry-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/agco-telematics-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/agco-location-example.json
- group: build
  title: ''
  type: Examples
  url: examples/agco-machine-example.json
- group: build
  title: ''
  type: Examples
  url: examples/agco-telemetry-example.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/agco-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/agco-vocabulary.yaml
description: AGCO is a global leader in the design, manufacture, and distribution of agricultural machinery and precision ag technology. The AGCO AgCommand API enables approved third-party developers and service providers to access machine telemetry data, location tracking, and performance metrics from AGCO Connect-ready equipment including Fendt, Massey Ferguson, Challenger, and Valtra brands.
examples:
- key_count: 7
  name: Agco Location Example
  slug: agco-location-example
- key_count: 11
  name: Agco Machine Example
  slug: agco-machine-example
- key_count: 11
  name: Agco Telemetry Example
  slug: agco-telemetry-example
features:
- description: Real-time access to machine performance data including engine speed, load, fuel consumption, and fault codes from AGCO Connect-ready equipment.
  name: Machine Telematics
- description: GPS-based machine location history enabling field work tracking and fleet management dashboards.
  name: Fleet Location Tracking
- description: Remote access to machine diagnostic codes enabling proactive maintenance and reducing downtime.
  name: Diagnostic Fault Codes
- description: Standardized filtering, search, and change event profiles for consistent API behavior across all resources.
  name: JSON API Profiles
- description: Single API access to data from Fendt, Massey Ferguson, Challenger, and Valtra agricultural equipment.
  name: Multi-Brand Coverage
finops:
- name: Agco Finops
  service_category: Agriculture / Telematics
  slug: agco-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agco.png
integrations:
- description: Integration of AGCO telematics data with Procore construction and project management workflows.
  name: Procore
- description: Integration with precision agriculture software platforms for combined field and machine data analysis.
  name: Precision Ag Software
json_schemas:
- name: MachineLocation
  property_count: 7
  slug: agco-location
- name: Machine
  property_count: 11
  slug: agco-machine
- name: Telemetry
  property_count: 11
  slug: agco-telemetry
json_structures:
- name: Agco Location Structure
  property_count: 7
  slug: agco-location-structure
- name: Agco Machine Structure
  property_count: 11
  slug: agco-machine-structure
- name: Agco Telemetry Structure
  property_count: 11
  slug: agco-telemetry-structure
jsonld:
- class_count: 3
  name: Agco Telematics Context
  property_count: 24
  slug: agco-telematics-context
layout: provider
modified: '2026-04-19'
name: agco
nav: Providers
network: true
overview: 'agco publishes 3 APIs on the [APIs.io](https://apis.io/) network: Locations API, Machines API, and Telemetry API. Tagged areas include Fortune 500.


  The agco catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  agco''s developer surface includes authentication, developer portal, getting-started guide, engineering blog, code examples, and 16 more developer resources.'
plans:
- name: Agco Plans Pricing
  plan_count: 1
  slug: agco-plans-pricing
press:
- date: '2026-05-25'
  title: AGCO Tech Day 2025 is coming next week! We're ...
  url: https://www.facebook.com/AGCOcorp/posts/agco-tech-day-2025-is-coming-next-weekwere-showcasing-the-latest-in-ai-autonomy-/1252586473563773/
- date: '2026-05-25'
  title: 'Press release: AI- and sensor solution awarded silver ...'
  url: https://www.linkedin.com/pulse/press-release-ai-sensor-solution-awarded-silver-medal-agritechnica-z9tdf
- date: '2026-05-25'
  title: AGCO Tech Day 2025 Spotlights AI, Autonomy and Mixed ...
  url: https://investors.agcocorp.com/news-releases/news-release-details/agco-tech-day-2025-spotlights-ai-autonomy-and-mixed-fleet
- date: '2026-05-25'
  title: AGCO Invests in AI-Weeding Company
  url: https://www.no-tillfarmer.com/articles/11047-agco-invests-in-ai-weeding-company
- date: '2026-05-25'
  title: AGCO to Showcase Full-Line Innovation and Smart ...
  url: https://www.prnewswire.com/news-releases/agco-to-showcase-full-line-innovation-and-smart-farming-technologies-at-agritechnica-2025-302604586.html
random_paper: 2
rate_limits:
- limit_count: 1
  name: Agco Rate Limits
  slug: agco-rate-limits
rules:
- name: agco API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: agco-jsonschema-spectral-rules
- name: agco API Rules
  rule_count: 25
  severity_counts:
    error: 14
    hint: 0
    info: 0
    warn: 11
  slug: agco-spectral-rules
score:
  band: developing
  composite: 51.2
  delta: 2.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 59.9
    developer_ergonomics: 32.6
    discoverability: 80.0
    governance: 86.8
    operational_transparency: 26.3
  previous_composite: 48.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agco/refs/heads/main/screenshots/agco-2026-06-20T165808.png
security:
- kind: authentication
  name: Agco Authentication
  slug: agco-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Agco Domain Security
  slug: agco-domain-security
  summary_line: TLSv1.2 · DMARC
slug: agco
tags:
- Fortune 500
use_cases:
- description: Build web and mobile dashboards that display real-time machine location, performance, and fuel status for farm operators.
  name: Farm Management Dashboard
- description: Monitor machine fault codes and engine hours remotely to schedule preventive maintenance before failures occur.
  name: Predictive Maintenance
- description: Track machine location and activity data to document field operations, coverage areas, and productivity metrics.
  name: Field Work Tracking
- description: Monitor fuel levels and consumption rates across a fleet to optimize refueling logistics and reduce costs.
  name: Fuel Management
- description: Integrate AGCO machine data into existing farm management or precision agriculture software platforms.
  name: Telematics Integration
website: https://get.agcoconnect.com/
---
