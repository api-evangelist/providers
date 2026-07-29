---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 35
  human_in_the_loop: 0
  name: Mcafee Agentic Access
  operation_count: 61
  slug: mcafee-agentic-access
  summary_line: 61 operations · 35 acting
api_count: 26
apis:
- description: Real-time threat intelligence sharing and reputation services API.
  name: McAfee Threat Intelligence Exchange (TIE) API
  slug: mcafee-tie-api
- description: Messaging fabric for real-time security data exchange and integration.
  name: McAfee Data Exchange Layer (DXL) API
  slug: mcafee-dxl-api
- description: Manage security alarms
  name: McAfee (Trellix) Alarms API
  slug: mcafee-alarms-api
- description: Session authentication and management
  name: McAfee (Trellix) Authentication API
  slug: mcafee-authentication-api
- description: Manage incident response cases
  name: McAfee (Trellix) Cases API
  slug: mcafee-cases-api
- description: Core server operations and authentication
  name: McAfee (Trellix) Core API
  slug: mcafee-core-api
- description: Manage event data sources
  name: McAfee (Trellix) Data Sources API
  slug: mcafee-data-sources-api
- description: EDR detection events and alerts
  name: McAfee (Trellix) Detections API
  slug: mcafee-detections-api
- description: Manage ESM device hierarchy
  name: McAfee (Trellix) Devices API
  slug: mcafee-devices-api
- description: Query and retrieve security events
  name: McAfee (Trellix) Events API
  slug: mcafee-events-api
- description: Import and export configuration files
  name: McAfee (Trellix) File Operations API
  slug: mcafee-file-operations-api
- description: Threat investigation workflows and actions
  name: McAfee (Trellix) Investigations API
  slug: mcafee-investigations-api
- description: Manage URL and IP lists used in filtering
  name: McAfee (Trellix) Lists API
  slug: mcafee-lists-api
- description: Appliance health and traffic monitoring
  name: McAfee (Trellix) Monitoring API
  slug: mcafee-monitoring-api
- description: Manage and assign security policies
  name: McAfee (Trellix) Policies API
  slug: mcafee-policies-api
- description: Manage proxy and policy settings
  name: McAfee (Trellix) Policy Configuration API
  slug: mcafee-policy-configuration-api
- description: Execute ePO queries and retrieve results
  name: McAfee (Trellix) Queries API
  slug: mcafee-queries-api
- description: Real-time data collection from endpoints
  name: McAfee (Trellix) Real-Time Search API
  slug: mcafee-real-time-search-api
- description: Manage web security rule sets
  name: McAfee (Trellix) Rule Sets API
  slug: mcafee-rule-sets-api
- description: Manage software repositories and packages
  name: McAfee (Trellix) Software API
  slug: mcafee-software-api
- description: Manage the ePO System Tree groups
  name: McAfee (Trellix) System Groups API
  slug: mcafee-system-groups-api
- description: Manage endpoints and systems registered in ePO
  name: McAfee (Trellix) Systems API
  slug: mcafee-systems-api
- description: Manage client tasks and server tasks
  name: McAfee (Trellix) Tasks API
  slug: mcafee-tasks-api
- description: Retrieve threat event data from managed endpoints
  name: McAfee (Trellix) Threat Events API
  slug: mcafee-threat-events-api
- description: Retrieve and manage detected threats
  name: McAfee (Trellix) Threats API
  slug: mcafee-threats-api
- description: Manage security watchlists
  name: McAfee (Trellix) Watchlists API
  slug: mcafee-watchlists-api
artifact_total: 81
collections:
- collection_type: open
  name: McAfee ePO API
  slug: open-mcafee-epo
- collection_type: open
  name: McAfee ESM API
  slug: open-mcafee-esm
- collection_type: open
  name: McAfee MVISION API
  slug: open-mcafee-mvision
- collection_type: open
  name: McAfee Web Gateway API
  slug: open-mcafee-web-gateway
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mcafee-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mcafee-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mcafee-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mcafee
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.mcafee.com
- group: company
  title: ''
  type: Website
  url: https://www.trellix.com/
- group: operate
  title: ''
  type: Support
  url: https://www.trellix.com/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trellix.com/about/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trellix.com/about/legal/privacy/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/mcafee-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/mcafee-threat-event-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/mcafee-endpoint-schema.json
created: '2024-01-20'
description: APIs for McAfee Enterprise security products and services. McAfee Enterprise rebranded as Trellix in 2022, but its on-premises and SaaS platforms (ePO, MVISION, ESM, Web Gateway, TIE, DXL) continue to expose REST APIs documented here for centralized security management, threat intelligence, EDR, messaging, and SIEM integration.
finops:
- name: Mcafee Finops
  service_category: Cybersecurity Software
  slug: mcafee-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mcafee.png
json_schemas:
- name: ApiCommand
  property_count: 3
  slug: mcafee-apicommand
- name: ApplianceStatus
  property_count: 6
  slug: mcafee-appliancestatus
- name: Case
  property_count: 8
  slug: mcafee-case
- name: ClientTask
  property_count: 5
  slug: mcafee-clienttask
- name: CommandResult
  property_count: 1
  slug: mcafee-commandresult
- name: DataSource
  property_count: 7
  slug: mcafee-datasource
- name: Detection
  property_count: 3
  slug: mcafee-detection
- name: DetectionListResponse
  property_count: 2
  slug: mcafee-detectionlistresponse
- name: DetectionResponse
  property_count: 1
  slug: mcafee-detectionresponse
- name: Device
  property_count: 3
  slug: mcafee-device
- name: DeviceListResponse
  property_count: 2
  slug: mcafee-devicelistresponse
- name: DeviceResponse
  property_count: 1
  slug: mcafee-deviceresponse
- name: McAfee Managed Endpoint
  property_count: 21
  slug: mcafee-endpoint
- name: EsmDevice
  property_count: 6
  slug: mcafee-esmdevice
- name: FilterList
  property_count: 4
  slug: mcafee-filterlist
- name: FilterListDetail
  property_count: 4
  slug: mcafee-filterlistdetail
- name: Investigation
  property_count: 3
  slug: mcafee-investigation
- name: InvestigationListResponse
  property_count: 2
  slug: mcafee-investigationlistresponse
- name: InvestigationResponse
  property_count: 1
  slug: mcafee-investigationresponse
- name: ListEntry
  property_count: 2
  slug: mcafee-listentry
- name: LoginResponse
  property_count: 4
  slug: mcafee-loginresponse
- name: PaginationMeta
  property_count: 3
  slug: mcafee-paginationmeta
- name: Policy
  property_count: 5
  slug: mcafee-policy
- name: RealTimeSearchResponse
  property_count: 1
  slug: mcafee-realtimesearchresponse
- name: RemediationActionResponse
  property_count: 1
  slug: mcafee-remediationactionresponse
- name: Rule
  property_count: 5
  slug: mcafee-rule
- name: RuleSet
  property_count: 4
  slug: mcafee-ruleset
- name: RuleSetDetail
  property_count: 4
  slug: mcafee-rulesetdetail
- name: SavedQuery
  property_count: 5
  slug: mcafee-savedquery
- name: ServerTask
  property_count: 5
  slug: mcafee-servertask
- name: SoftwarePackage
  property_count: 4
  slug: mcafee-softwarepackage
- name: System
  property_count: 12
  slug: mcafee-system
- name: SystemGroup
  property_count: 3
  slug: mcafee-systemgroup
- name: McAfee Threat Event
  property_count: 24
  slug: mcafee-threat-event
- name: Threat
  property_count: 3
  slug: mcafee-threat
- name: ThreatEvent
  property_count: 12
  slug: mcafee-threatevent
- name: ThreatListResponse
  property_count: 2
  slug: mcafee-threatlistresponse
- name: ThreatResponse
  property_count: 1
  slug: mcafee-threatresponse
- name: TokenResponse
  property_count: 4
  slug: mcafee-tokenresponse
- name: TrafficStatistics
  property_count: 6
  slug: mcafee-trafficstatistics
- name: TriggeredAlarm
  property_count: 10
  slug: mcafee-triggeredalarm
- name: Watchlist
  property_count: 5
  slug: mcafee-watchlist
json_structures:
- name: Mcafee Structure
  property_count: 0
  slug: mcafee-structure
jsonld:
- class_count: 0
  name: Mcafee Context
  property_count: 10
  slug: mcafee-context
layout: provider
modified: '2026-05-19'
name: McAfee (Trellix)
nav: Providers
network: true
overview: 'McAfee (Trellix) publishes 24 APIs on the [APIs.io](https://apis.io/) network, including Alarms API, Authentication API, Cases API, and 21 more. Tagged areas include Antivirus, Cybersecurity, Endpoint Protection, Security, and Threat Intelligence.


  The McAfee (Trellix) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  McAfee (Trellix)''s developer surface includes authentication, support, and 10 more developer resources.'
plans:
- name: Mcafee Plans Pricing
  plan_count: 1
  slug: mcafee-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 2
  name: Mcafee Rate Limits
  slug: mcafee-rate-limits
rules:
- name: McAfee (Trellix) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: mcafee-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.0
  delta: -5.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 64.3
    developer_ergonomics: 23.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 53.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 24
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/mcafee/refs/heads/main/screenshots/mcafee-2026-06-20T185056.png
security:
- kind: authentication
  name: Mcafee Authentication
  slug: mcafee-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Mcafee Domain Security
  slug: mcafee-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mcafee
tags:
- Antivirus
- Cybersecurity
- Endpoint Protection
- Security
- Threat Intelligence
website: https://www.trellix.com/
---
