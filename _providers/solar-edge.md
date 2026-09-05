---
access_model:
  confidence: medium
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Solar Edge Agentic Access
  operation_count: 23
  slug: solar-edge-agentic-access
  summary_line: 23 operations
api_count: 3
apis:
- baseURL: https://monitoringapi.solaredge.com
  baseurl_source: declared
  description: Account and sub-account management
  name: SolarEdge Accounts API
  slug: solar-edge-accounts-api
- baseURL: https://monitoringapi.solaredge.com
  baseurl_source: declared
  description: Energy production measurements and time-frame energy
  name: SolarEdge Energy API
  slug: solar-edge-energy-api
- baseURL: https://monitoringapi.solaredge.com
  baseurl_source: declared
  description: Environmental benefit metrics
  name: SolarEdge Environmental API
  slug: solar-edge-environmental-api
- baseURL: https://monitoringapi.solaredge.com
  baseurl_source: declared
  description: Inverters, batteries, meters, sensors, and inventory
  name: SolarEdge Equipment API
  slug: solar-edge-equipment-api
- baseURL: https://monitoringapi.solaredge.com
  baseurl_source: declared
  description: Power measurements and power flow
  name: SolarEdge Power API
  slug: solar-edge-power-api
- baseURL: https://monitoringapi.solaredge.com
  baseurl_source: declared
  description: Site list and site-level data
  name: SolarEdge Sites API
  slug: solar-edge-sites-api
- baseURL: https://monitoringapi.solaredge.com
  baseurl_source: declared
  description: Battery storage data
  name: SolarEdge Storage API
  slug: solar-edge-storage-api
- baseURL: https://monitoringapi.solaredge.com
  baseurl_source: declared
  description: API version information
  name: SolarEdge Version API
  slug: solar-edge-version-api
- baseURL: https://monitoringapi.solaredge.com
  baseurl_source: declared
  description: Account hierarchy.
  name: SolarEdge Account API
  slug: solar-edge-account-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SolarEdge Monitoring Account API
  slug: open-solar-edge-account-api
- collection_type: open
  name: SolarEdge Monitoring Accounts API
  slug: open-solar-edge-accounts-api
- collection_type: open
  name: SolarEdge Monitoring Accounts Energy API
  slug: open-solar-edge-energy-api
- collection_type: open
  name: SolarEdge Monitoring Accounts Environmental API
  slug: open-solar-edge-environmental-api
- collection_type: open
  name: SolarEdge Monitoring Accounts Equipment API
  slug: open-solar-edge-equipment-api
- collection_type: open
  name: SolarEdge Monitoring Accounts Power API
  slug: open-solar-edge-power-api
- collection_type: open
  name: SolarEdge Monitoring Accounts Sites API
  slug: open-solar-edge-sites-api
- collection_type: open
  name: SolarEdge Monitoring Accounts Storage API
  slug: open-solar-edge-storage-api
- collection_type: open
  name: SolarEdge Monitoring Accounts Version API
  slug: open-solar-edge-version-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/solar-edge-monitoring-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/solar-edge-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/solar-edge-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/solar-edge-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.solaredge.com
- group: docs
  title: ''
  type: Documentation
  url: https://knowledge-center.solaredge.com/sites/kc/files/se_monitoring_api.pdf
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/SolarEdgeTech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/solaredge
- group: company
  title: ''
  type: Blog
  url: https://www.solaredge.com/us/solaredge-blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.solaredge.com/us/commercial/developer
- group: other
  title: ''
  type: X
  url: https://x.com/SolarEdgePV
- group: commercial
  title: ''
  type: Plans
  url: plans/solar-edge-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/solar-edge-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/solar-edge-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.solaredge.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.solaredge.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SolarEdge
- group: operate
  title: ''
  type: Support
  url: https://www.solaredge.com/us/service/support
- group: start
  title: ''
  type: SignUp
  url: https://monitoring.solaredge.com/solaredge-web/p/login
- group: start
  title: ''
  type: Login
  url: https://monitoring.solaredge.com/solaredge-web/p/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.solaredge.com/us/legal/eula
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.solaredge.com/us/legal/privacy-policy
- group: design
  title: ''
  type: Conventions
  url: conventions/solar-edge-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/solar-edge-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/solar-edge-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/solar-edge-conformance.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/solar-edge-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/solar-edge-llms.txt
created: '2026-06-13'
description: SolarEdge Technologies provides a cloud-based Monitoring API that enables web services and third-party applications to access real-time and historical solar production data stored on the SolarEdge monitoring server. The REST API delivers site energy measurements, power flow data, inverter technical telemetry, battery storage status, equipment inventory, and environmental benefit metrics for SolarEdge-connected systems. Authentication is handled via an API key generated through the SolarEdge monitoring portal, and all requests are made over HTTPS with responses returned in JSON format. The platform supports both site-level and account-level queries, with bulk call options allowing developers to retrieve data across multiple sites in a single request. SolarEdge serves residential, commercial, and utility-scale solar installations globally, making their API central to energy management integrations, home automation platforms, and fleet monitoring solutions.
examples:
- key_count: 1
  name: Solar Edge Energy Example
  slug: solar-edge-energy-example
- key_count: 1
  name: Solar Edge Env Benefits Example
  slug: solar-edge-env-benefits-example
- key_count: 1
  name: Solar Edge Power Flow Example
  slug: solar-edge-power-flow-example
- key_count: 1
  name: Solar Edge Site List Example
  slug: solar-edge-site-list-example
- key_count: 1
  name: Solar Edge Site Overview Example
  slug: solar-edge-site-overview-example
finops:
- name: Solar Edge Finops
  service_category: ''
  slug: solar-edge-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/solar-edge.png
json_schemas:
- name: SolarEdge Energy Measurement
  property_count: 1
  slug: solar-edge-energy
- name: SolarEdge Inverter Telemetry
  property_count: 12
  slug: solar-edge-inverter
- name: SolarEdge Site
  property_count: 12
  slug: solar-edge-site
jsonld:
- class_count: 67
  name: Solar Edge Context
  property_count: 44
  slug: solar-edge-context
layout: provider
modified: '2026-08-08'
name: SolarEdge
nav: Providers
network: true
overview: 'SolarEdge publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Energy API, Environmental API, and 6 more. Tagged areas include Solar, Energy, Monitoring, PV, and Inverter.


  The SolarEdge catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SolarEdge''s developer surface includes authentication, documentation, engineering blog, pricing, API reference, support, signup flow, and 21 more developer resources.'
plans:
- name: Solar Edge Plans Pricing
  plan_count: 1
  slug: solar-edge-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 3
  name: Solar Edge Rate Limits
  slug: solar-edge-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: SolarEdge API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: solar-edge-jsonschema-spectral-rules
score:
  band: strong
  composite: 56.2
  coverage:
    artifact_dirs: 24
    catalog_earned: 77.3
    catalog_earned_first_party: 0.0
    catalog_gap: 37.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 14.4
    contract_quality: 63.9
    developer_ergonomics: 45.2
    discoverability: 81.5
    governance: 14.4
    operational_transparency: 34.2
  previous_composite: 56.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/solar-edge/refs/heads/main/screenshots/solar-edge-2026-06-20T194200.png
security:
- kind: authentication
  name: Solar Edge Authentication
  slug: solar-edge-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Solar Edge Domain Security
  slug: solar-edge-domain-security
  summary_line: TLSv1.3 · DMARC
slug: solar-edge
tags:
- Solar
- Energy
- Monitoring
- PV
- Inverter
- Renewable Energy
- IoT
website: https://www.solaredge.com
---
