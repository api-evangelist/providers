---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Agco Agentic Access
  operation_count: 3
  slug: agco-agentic-access
  summary_line: 3 operations
api_count: 2
apis:
- baseURL: https://api.agcocorp.com
  baseurl_source: declared
  description: Access machine location and tracking data.
  name: agco Locations API
  slug: agco-locations-api
- baseURL: https://api.agcocorp.com
  baseurl_source: declared
  description: Access machine information and status.
  name: agco Machines API
  slug: agco-machines-api
- baseURL: https://api.agcocorp.com
  baseurl_source: declared
  description: Retrieve machine telemetry and sensor data.
  name: agco Telemetry API
  slug: agco-telemetry-api
- baseURL: https://secure.agco-ats.com
  baseurl_source: declared
  description: 'The AGCO Technical Support (ATS) API behind AGCO''s Electronic Diagnostic Tool (EDT) and dealer software distribution platform. Publishes 285 operations across 55 tags covering authorization codes and '
  name: AGCO ATS API
  slug: agco-ats-api
artifact_total: 40
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AGCO AgCommand API
  slug: open-agco-agcommand-api
- collection_type: open
  name: AGCO AgCommand Locations API
  slug: open-agco-locations-api
- collection_type: open
  name: AGCO AgCommand Locations Machines API
  slug: open-agco-machines-api
- collection_type: open
  name: AGCO AgCommand Locations Telemetry API
  slug: open-agco-telemetry-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/agco-capability-edges.yml
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
- group: build
  title: ''
  type: Packages
  url: packages/agco-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/agco-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agco-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/agco-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/agco-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/agco-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/agco-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/agco-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/agco-ats-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/agco-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/agco-rate-limits.yml
- group: docs
  title: ''
  type: APIReference
  url: https://secure.agco-ats.com/swagger
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/agco/agco-json-api-profiles
- group: operate
  title: ''
  type: Support
  url: https://agcocorp.support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agcocorp.com/us/en/home/compliance-center/privacy-statement/privacy-statement-en.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agcocorp.com/us/en/home/compliance-center/legal.html
- group: start
  title: ''
  type: Login
  url: https://access.agcocorp.com/en/
- group: company
  title: ''
  type: Website
  url: https://www.agcocorp.com/
created: '2026-05-04'
description: 'AGCO is a global manufacturer of agricultural machinery and precision-ag technology — Fendt, Massey Ferguson, Valtra, Challenger, GSI and PTx. Its one publicly reachable machine-readable contract is the AGCO Technical Support (ATS) API at secure.agco-ats.com: a Swagger 2.0 document with 285 operations across 55 tags, served with a public Swagger UI, covering dealer records, authorization codes and vouchers, software package distribution to Electronic Diagnostic Tool (EDT) installations, a content submission and release pipeline, translation workflow, and AGCO Power aftermarket services. AGCO also publishes three first-party JSON:API profiles standardising filtering, search and change events. The AgCommand telematics API announced in 2015 for third-party developers has no reachable public documentation: the developer portal at developer.agcocorp.com no longer publishes and api.agcocorp.com is an API Gateway that authenticates every path.'
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
modified: '2026-09-04'
name: Agco
nav: Providers
network: true
overview: 'Agco publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Locations API, Machines API, Telemetry API, and 1 more. Tagged areas include Fortune 500, Agriculture, Farm Equipment, Manufacturing, and Telematics.


  The Agco catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Agco''s developer surface includes authentication, developer portal, getting-started guide, engineering blog, code examples, API reference, documentation, and 33 more developer resources.'
plans:
- name: Agco Plans Pricing
  plan_count: 0
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
random_paper: 11
rate_limits:
- limit_count: 0
  name: Agco Rate Limits
  slug: agco-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Agco API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: agco-jsonschema-spectral-rules
- effective_rule_count: 66
  extends:
  - spectral:oas
  name: Agco API Rules
  rule_count: 25
  severity_counts:
    error: 14
    hint: 0
    info: 0
    warn: 11
  slug: agco-spectral-rules
score:
  band: developing
  composite: 46.5
  coverage:
    artifact_dirs: 30
    catalog_earned: 57.5
    catalog_earned_first_party: 0.0
    catalog_gap: 57.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 47.0
    contract_quality: 63.0
    developer_ergonomics: 54.2
    discoverability: 68.5
    governance: 47.0
    operational_transparency: 2.6
  previous_composite: 45.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agco/refs/heads/main/screenshots/agco-2026-06-20T165808.png
security:
- kind: authentication
  name: Agco Ats Authentication
  slug: agco-ats-authentication
  summary_line: 0 schemes
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
- Agriculture
- Farm Equipment
- Manufacturing
- Telematics
- Precision Agriculture
- Diagnostics
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
website: https://www.agcocorp.com/
---
