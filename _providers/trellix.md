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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Trellix Agentic Access
  operation_count: 21
  slug: trellix-agentic-access
  summary_line: 21 operations · 6 acting
api_count: 2
apis:
- description: McAfee ePolicy Orchestrator (ePO) REST API for centralized security management, policy enforcement, and reporting across the enterprise.
  name: Trellix ePO API
  slug: trellix-epo-api
- description: The Trellix ePO SaaS API provides cloud-based access to ePolicy Orchestrator management capabilities. It enables programmatic control of devices, events, tags, queries, and response actions through th
  name: Trellix ePO SaaS API
  slug: trellix-epo-saas-api
- description: API for accessing threat intelligence, security analytics, and insights from the Trellix threat research platform. Provides investigation of indicators of compromise, campaign tracking, and prioritize
  name: Trellix Insights API
  slug: trellix-insights-api
- description: Endpoint Detection and Response API for advanced threat hunting, investigation, and automated response capabilities. The EDR API supports querying threat data, searching devices, retrieving action his
  name: Trellix EDR API
  slug: trellix-edr-api
- description: Messaging fabric API that enables real-time communication between security tools and data sharing across the security ecosystem. OpenDXL provides client libraries in Python, JavaScript, and Java for i
  name: Trellix Data Exchange Layer (DXL) API
  slug: trellix-data-exchange-layer-dxl-api
- description: REST API for the Trellix Endpoint Security (HX) platform, formerly FireEye HX. Provides programmatic access to endpoint information, acquisitions, alerts, indicators, conditions, and containment opera
  name: Trellix Endpoint Security (HX) API
  slug: trellix-endpoint-security-hx-api
- description: REST API for Trellix Data Loss Prevention Endpoint that enables programmatic management of DLP policies, retrieval and analysis of data loss incidents, and integration with cloud gateways. Supports ap
  name: Trellix Data Loss Prevention (DLP) API
  slug: trellix-data-loss-prevention-dlp-api
- description: RESTful API for Trellix Email Security Cloud (formerly FireEye ETP) providing custom integration capabilities for advanced threat detection in email. Supports APIs for querying advanced threats, email
  name: Trellix Email Security Cloud API
  slug: trellix-email-security-cloud-api
- description: API for the Trellix Helix security operations platform that integrates security controls from Trellix and over 500 third-party sources to create multi-vector threat detections and AI-guided responses.
  name: Trellix Helix API
  slug: trellix-helix-api
- description: REST API for Trellix Intelligent Sandbox (formerly Advanced Threat Defense) that enables automated submission and analysis of files and URLs in a sandboxed environment. Supports file submission, analy
  name: Trellix Intelligent Sandbox API
  slug: trellix-intelligent-sandbox-api
- description: API for Trellix Threat Intelligence Exchange which acts as a reputation broker enabling real-time sharing of threat intelligence from global and local sources across the security ecosystem via the Dat
  name: Trellix Threat Intelligence Exchange (TIE) API
  slug: trellix-threat-intelligence-exchange-tie-api
- description: REST API interface for managing indicators of compromise within the Trellix security platform. Enables uploading, querying, and managing IOCs including file hashes, IP addresses, domains, and email ad
  name: Trellix IOC (Indicators of Compromise) API
  slug: trellix-ioc-indicators-of-compromise-api
- description: API-driven malware detection service that leverages the Trellix Multi-Vector Virtual Execution (MVX) engine and multiple dynamic machine learning, AI, and correlation engines to analyze submitted file
  name: Trellix Detection as a Service API
  slug: trellix-detection-as-a-service-api
- description: Interactive API documentation and testing tool for Trellix security products formerly under the FireEye brand. Provides a web-based interface for exploring and testing API endpoints across multiple Tr
  name: Trellix API Explorer
  slug: trellix-api-explorer
- description: Retrieve the history of response actions executed on managed endpoints through the EDR platform.
  name: Trellix Action History API
  slug: trellix-action-history-api
- description: Query detection counts, severity rankings, and first detection timestamps for systems affected by threats.
  name: Trellix Affected Hosts API
  slug: trellix-affected-hosts-api
- description: Access discrete detection alerts containing process, user, and host context with trace identifiers and severity scores.
  name: Trellix Alerts API
  slug: trellix-alerts-api
- description: Retrieve individual detection events with process names, command lines, hash identifiers, and domain information.
  name: Trellix Detections API
  slug: trellix-detections-api
- description: Manage and query endpoint devices registered in ePO SaaS, including device attributes, agent status, and system information.
  name: Trellix Devices API
  slug: trellix-devices-api
- description: The Epo API from Trellix — 2 operation(s) for epo.
  name: Trellix Epo API
  slug: trellix-epo-api
- description: Retrieve threat events and security incidents detected across managed endpoints. Events have a 3-day retention period.
  name: Trellix Events API
  slug: trellix-events-api
- description: Manage device groups and organizational hierarchy within the ePO SaaS console.
  name: Trellix Groups API
  slug: trellix-groups-api
- description: Execute and manage saved queries against the ePO SaaS data store for reporting and analysis.
  name: Trellix Queries API
  slug: trellix-queries-api
- description: Execute response actions on endpoints such as killing processes, quarantining files, or isolating hosts.
  name: Trellix Reactions API
  slug: trellix-reactions-api
- description: Trigger automated response actions on managed endpoints, including policy enforcement and remediation tasks.
  name: Trellix Response Actions API
  slug: trellix-response-actions-api
- description: Execute real-time searches across managed endpoints to hunt for indicators of compromise and suspicious activity.
  name: Trellix Searches API
  slug: trellix-searches-api
- description: Query aggregated threat intelligence including threat names, severity rankings, SHA256 hashes, and MITRE ATT&CK mappings.
  name: Trellix Threats API
  slug: trellix-threats-api
artifact_total: 86
collections:
- collection_type: postman
  name: Trellix EDR Action History API
  slug: postman-trellix-action-history-api
- collection_type: postman
  name: Trellix EDR Action History Affected Hosts API
  slug: postman-trellix-affected-hosts-api
- collection_type: postman
  name: Trellix EDR Action History Alerts API
  slug: postman-trellix-alerts-api
- collection_type: postman
  name: Trellix EDR Action History Detections API
  slug: postman-trellix-detections-api
- collection_type: postman
  name: Trellix EDR Action History Devices API
  slug: postman-trellix-devices-api
- collection_type: postman
  name: Trellix EDR Action History Epo API
  slug: postman-trellix-epo-api
- collection_type: postman
  name: Trellix EDR Action History Events API
  slug: postman-trellix-events-api
- collection_type: postman
  name: Trellix EDR Action History Groups API
  slug: postman-trellix-groups-api
- collection_type: postman
  name: Trellix EDR Action History Queries API
  slug: postman-trellix-queries-api
- collection_type: postman
  name: Trellix EDR Action History Reactions API
  slug: postman-trellix-reactions-api
- collection_type: postman
  name: Trellix EDR Action History Response Actions API
  slug: postman-trellix-response-actions-api
- collection_type: postman
  name: Trellix EDR Action History Searches API
  slug: postman-trellix-searches-api
- collection_type: postman
  name: Trellix EDR Action History Threats API
  slug: postman-trellix-threats-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Trellix EDR Action History API
  slug: open-trellix-action-history-api
- collection_type: open
  name: Trellix EDR Action History Affected Hosts API
  slug: open-trellix-affected-hosts-api
- collection_type: open
  name: Trellix EDR Action History Alerts API
  slug: open-trellix-alerts-api
- collection_type: open
  name: Trellix EDR Action History Detections API
  slug: open-trellix-detections-api
- collection_type: open
  name: Trellix EDR Action History Devices API
  slug: open-trellix-devices-api
- collection_type: open
  name: Trellix EDR API
  slug: open-trellix-edr
- collection_type: open
  name: Trellix EDR Action History Epo API
  slug: open-trellix-epo-api
- collection_type: open
  name: Trellix ePO SaaS API
  slug: open-trellix-epo-saas
- collection_type: open
  name: Trellix EDR Action History Events API
  slug: open-trellix-events-api
- collection_type: open
  name: Trellix EDR Action History Groups API
  slug: open-trellix-groups-api
- collection_type: open
  name: Trellix EDR Action History Queries API
  slug: open-trellix-queries-api
- collection_type: open
  name: Trellix EDR Action History Reactions API
  slug: open-trellix-reactions-api
- collection_type: open
  name: Trellix EDR Action History Response Actions API
  slug: open-trellix-response-actions-api
- collection_type: open
  name: Trellix EDR Action History Searches API
  slug: open-trellix-searches-api
- collection_type: open
  name: Trellix EDR Action History Threats API
  slug: open-trellix-threats-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/trellix-enterprise/EDR-Integration-Scripts/issues
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/trellix/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trellix-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trellix-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trellix-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trellixsecurity
- group: start
  title: ''
  type: Portal
  url: https://www.trellix.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.manage.trellix.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trellix.com/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.manage.trellix.com/mvision/docs/umam
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.manage.trellix.com/mvision/docs/uma
- group: operate
  title: ''
  type: Support
  url: https://www.trellix.com/support/
- group: start
  title: ''
  type: Login
  url: https://sso.trellix.com/
- group: start
  title: ''
  type: Signup
  url: https://developer.manage.trellix.com/
- group: operate
  title: ''
  type: Community
  url: https://communitym.trellix.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.trellix.com/
- group: company
  title: ''
  type: Blog
  url: https://www.trellix.com/blogs/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trellix.com/en-us/about/legal/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trellix.com/en-us/about/legal/terms-of-use.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trellix-enterprise
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opendxl
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trellix-opensource
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/advanced-threat-research
- group: company
  title: ''
  type: Website
  url: https://www.trellix.com/
- group: other
  title: ''
  type: Knowledge Base
  url: https://kcm.trellix.com/
- group: build
  title: ''
  type: PostmanCollection
  url: https://www.postman.com/bmarandel/trellix-api-gateway/documentation/d3e3gan/trellix-api-gateway
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.trellix.com/bundle/trellix-developer-portal-and-marketplace-release-notes
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/trellix-edr-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/trellix-epo-saas-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/trellix-threat-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/trellix-device-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/trellix-threat-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/trellix-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/trellix-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/trellix-vocabulary.yml
created: '2024'
description: Trellix is a cybersecurity company that delivers comprehensive, open, and native extended detection and response (XDR) platform. The company provides threat detection, investigation, and response capabilities across endpoints, networks, data, and cloud environments.
examples:
- key_count: 2
  name: Trellix List Threats Example
  slug: trellix-list-threats-example
finops:
- name: Trellix Finops
  service_category: Cybersecurity
  slug: trellix-finops
image: https://www.trellix.com/favicon.ico
json_schemas:
- name: ActionHistoryEntry
  property_count: 7
  slug: trellix-actionhistoryentry
- name: AffectedHost
  property_count: 8
  slug: trellix-affectedhost
- name: Alert
  property_count: 12
  slug: trellix-alert
- name: Detection
  property_count: 10
  slug: trellix-detection
- name: Trellix Device
  property_count: 11
  slug: trellix-device
- name: Event
  property_count: 3
  slug: trellix-event
- name: Group
  property_count: 5
  slug: trellix-group
- name: PaginationMeta
  property_count: 3
  slug: trellix-paginationmeta
- name: Query
  property_count: 5
  slug: trellix-query
- name: Reaction
  property_count: 5
  slug: trellix-reaction
- name: ReactionCreate
  property_count: 3
  slug: trellix-reactioncreate
- name: ResponseAction
  property_count: 5
  slug: trellix-responseaction
- name: ResponseActionCreate
  property_count: 3
  slug: trellix-responseactioncreate
- name: Search
  property_count: 7
  slug: trellix-search
- name: SearchCreate
  property_count: 2
  slug: trellix-searchcreate
- name: Tag
  property_count: 4
  slug: trellix-tag
- name: TagCreate
  property_count: 3
  slug: trellix-tagcreate
- name: Trellix Threat
  property_count: 11
  slug: trellix-threat
json_structures:
- name: Trellix Structure
  property_count: 0
  slug: trellix-structure
- name: Trellix Threat Structure
  property_count: 0
  slug: trellix-threat-structure
jsonld:
- class_count: 22
  name: Trellix Context
  property_count: 8
  slug: trellix-context
layout: provider
modified: '2026-05-19'
name: Trellix
nav: Providers
network: true
overview: 'Trellix publishes 14 APIs on the [APIs.io](https://apis.io/) network, including ePO API, Action History API, Affected Hosts API, and 11 more. Tagged areas include Cloud Security, Cybersecurity, Endpoint Security, Threat Detection, and Threat Intelligence.


  The Trellix catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Trellix''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, signup flow, engineering blog, and 28 more developer resources.'
plans:
- name: Trellix Plans Pricing
  plan_count: 1
  slug: trellix-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Trellix Rate Limits
  slug: trellix-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Trellix API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: trellix-jsonschema-spectral-rules
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: Trellix API Rules
  rule_count: 17
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 12
  slug: trellix-spectral-rules
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 17
    catalog_gap: 57.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 40.8
    commercial_clarity: 40.8
    contract_governance: 17.4
    contract_quality: 62.6
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 17.4
    operational_transparency: 39.5
  open_source:
    applies: true
    score: 0.0
  previous_composite: 39.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trellix/refs/heads/main/screenshots/trellix-2026-06-20T195650.png
security:
- kind: authentication
  name: Trellix Authentication
  slug: trellix-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Trellix Domain Security
  slug: trellix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trellix
tags:
- Cloud Security
- Cybersecurity
- Endpoint Security
- Threat Detection
- Threat Intelligence
- XDR
website: https://www.trellix.com/
---
