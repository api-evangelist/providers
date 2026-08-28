---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.0
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 172
  human_in_the_loop: 5
  name: Armor Agentic Access
  operation_count: 427
  slug: armor-agentic-access
  summary_line: 427 operations · 172 acting · 5 human-in-the-loop
api_count: 70
apis:
- description: Operations for managing ACLs (deprecated)
  name: Armor Access Control Lists API
  slug: armor-access-control-lists-api
- description: Account management operations
  name: Armor Account API
  slug: armor-account-api
- description: The Account Management API from Armor — 47 operation(s) for account management.
  name: Armor Account Management API
  slug: armor-account-management-api
- description: The AccountPrimaryBilling API from Armor — 1 operation(s) for accountprimarybilling.
  name: Armor Account Primary Billing API
  slug: armor-accountprimarybilling-api
- description: The ActiveResponse API from Armor — 1 operation(s) for activeresponse.
  name: Armor Active Response API
  slug: armor-activeresponse-api
- description: The Advanced Backup API from Armor — 38 operation(s) for advanced backup.
  name: Armor Advanced Backup API
  slug: armor-advanced-backup-api
- description: Threat intelligence data for security entities
  name: Armor AIP - Entity Intelligence API
  slug: armor-aip-entity-intelligence-api
- description: AI-processed incident data and analytics
  name: Armor AIP - Incident Data API
  slug: armor-aip-incident-data-api
- description: Assessment account management
  name: Armor Assessments API
  slug: armor-assessments-api
- description: 'FH-AUTH authentication flow endpoints. ## Flow Overview 1. POST `/auth/authorize` with credentials → receive authorization code 2. POST `/auth/token` with code → receive access token 3. Use `Authoriza'
  name: Armor Authentication API
  slug: armor-authentication-api
- description: Cloud connection management operations
  name: Armor Cloud Connections API
  slug: armor-cloud-connections-api
- description: Connector management operations
  name: Armor Connector API
  slug: armor-connector-api
- description: Cloud Security Posture Management cloud connectors
  name: Armor CSPM Connector API
  slug: armor-cspm-connector-api
- description: CSPM control remediation information
  name: Armor CSPM Control Remediation API
  slug: armor-cspm-control-remediation-api
- description: CSPM policy management
  name: Armor CSPM Policies API
  slug: armor-cspm-policies-api
- description: CSPM policy controls management
  name: Armor CSPM Policy Controls API
  slug: armor-cspm-policy-controls-api
- description: CSPM report operations
  name: Armor CSPM Report API
  slug: armor-cspm-report-api
- description: CSPM report configuration management
  name: Armor CSPM Report Configuration API
  slug: armor-cspm-report-configuration-api
- description: CSPM resource management
  name: Armor CSPM Resources API
  slug: armor-cspm-resources-api
- description: CSPM cloud connector summary
  name: Armor CSPM Summary API
  slug: armor-cspm-summary-api
- description: CSPM cloud connector usage
  name: Armor CSPM Usage API
  slug: armor-cspm-usage-api
- description: Investigation package and live response operations
  name: Armor Defender - Investigation API
  slug: armor-defender-investigation-api
- description: Execute and manage actions on Microsoft Defender machines
  name: Armor Defender - Machine Actions API
  slug: armor-defender-machine-actions-api
- description: Microsoft Defender machine/device management
  name: Armor Defender - Machines API
  slug: armor-defender-machines-api
- description: Operations for retrieving and managing detection rules
  name: Armor Detection Rules API
  slug: armor-detection-rules-api
- description: The detection resource enables an API customer to build a webhook detection configuration.
  name: Armor Detections API
  slug: armor-detections-api
- description: Endpoint Detection and Response operations
  name: Armor EDR API
  slug: armor-edr-api
- description: The event-type resource enables an API user to maintain the event types.
  name: Armor Events API
  slug: armor-events-api
- description: Operations for managing flow sources
  name: Armor Flow Sources API
  slug: armor-flow-sources-api
- description: Service health and monitoring endpoints
  name: Armor Health API
  slug: armor-health-api
- description: Health monitoring status operations
  name: Armor Health Monitoring Status API
  slug: armor-health-monitoring-status-api
- description: Image management operations
  name: Armor Image API
  slug: armor-image-api
- description: The Infrastructure API from Armor — 35 operation(s) for infrastructure.
  name: Armor Infrastructure API
  slug: armor-infrastructure-api
- description: Security incident management
  name: Armor JSM - Incidents API
  slug: armor-jsm-incidents-api
- description: Metrics aggregation and reporting
  name: Armor JSM - Metrics API
  slug: armor-jsm-metrics-api
- description: JSM organization management
  name: Armor JSM - Organizations API
  slug: armor-jsm-organizations-api
- description: Service request management
  name: Armor JSM - Service Requests API
  slug: armor-jsm-service-requests-api
- description: The Keys API from Armor — 2 operation(s) for keys.
  name: Armor Keys API
  slug: armor-keys-api
- description: Operations for managing log endpoints
  name: Armor Log Endpoints API
  slug: armor-log-endpoints-api
- description: Operations for managing log groups
  name: Armor Log Groups API
  slug: armor-log-groups-api
- description: Operations for managing log sources
  name: Armor Log Sources API
  slug: armor-log-sources-api
- description: Malware configuration APIs. These APIs are only available for specific partners.
  name: Armor Malware Configuration API
  slug: armor-malware-configuration-api
- description: Meta resources and utility operations
  name: Armor Meta API
  slug: armor-meta-api
- description: The Network Services API from Armor — 23 operation(s) for network services.
  name: Armor Network Services API
  slug: armor-network-services-api
- description: The notification resource enables an API customer to build a webhook notification configuration.
  name: Armor Notifications API
  slug: armor-notifications-api
- description: The Preferences resource describes a list of user-level preferences.
  name: Armor Preferences API
  slug: armor-preferences-api
- description: Registry management operations
  name: Armor Registry API
  slug: armor-registry-api
- description: Monthly Security Report file management and retrieval
  name: Armor Reports - MSR API
  slug: armor-reports-msr-api
- description: The tasks resource enables an API customer to schedule, cancel and view agent CLI operations.
  name: Armor Scheduled Tasks API
  slug: armor-scheduled-tasks-api
- description: The secure notes resource allows users to securely store and manage sensitive information such as passwords, credentials, and other confidential data.
  name: Armor Secure Notes API
  slug: armor-secure-notes-api
- description: The Security Analytics API from Armor — 2 operation(s) for security analytics.
  name: Armor Security Analytics API
  slug: armor-security-analytics-api
- description: The Security API from Armor — 29 operation(s) for security.
  name: Armor Security API
  slug: armor-security-api
- description: Security detection event operations
  name: Armor Security Detection Events API
  slug: armor-security-detection-events-api
- description: Security detection operations
  name: Armor Security Detections API
  slug: armor-security-detections-api
- description: Security detections overview operations
  name: Armor Security Detections Overview API
  slug: armor-security-detections-overview-api
- description: The Security Incidents API from Armor — 2 operation(s) for security incidents.
  name: Armor Security Incidents API
  slug: armor-security-incidents-api
- description: Sensor management operations
  name: Armor Sensor API
  slug: armor-sensor-api
- description: The Support API from Armor — 16 operation(s) for support.
  name: Armor Support API
  slug: armor-support-api
- description: Tag management operations
  name: Armor Tags API
  slug: armor-tags-api
- description: Customer-specific threat intelligence
  name: Armor TI - Customer Intelligence API
  slug: armor-ti-customer-intelligence-api
- description: Proxy endpoint for OpenCTI GraphQL queries
  name: Armor TI - GraphQL API
  slug: armor-ti-graphql-api
- description: Retrieve threat actor intelligence data
  name: Armor TI - Threat Actors API
  slug: armor-ti-threat-actors-api
- description: Infrastructure management toolbox operations
  name: Armor Toolbox API
  slug: armor-toolbox-api
- description: The tours resource describes a list of UI tours that help users learn about features in the ARMOR Management Portal. The preferences stored in this resource aid the portal in determining which tours s
  name: Armor Tours API
  slug: armor-tours-api
- description: Trend AV report operations
  name: Armor Trend API
  slug: armor-trend-api
- description: User profile and account information
  name: Armor User API
  slug: armor-user-api
- description: The Utilization API from Armor — 2 operation(s) for utilization.
  name: Armor Utilization API
  slug: armor-utilization-api
- description: Vulnerability scan exclusions management
  name: Armor VS Exclusions API
  slug: armor-vs-exclusions-api
- description: Vulnerability scan reports
  name: Armor VS Reports API
  slug: armor-vs-reports-api
- description: Vulnerability scanning operations
  name: Armor Vulnerability Scanning API
  slug: armor-vulnerability-scanning-api
artifact_total: 147
asyncapis:
- description: ''
  name: Armor Webhooks Events
  slug: armor-webhooks-events
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Armor Log Management Access Control Lists API
  slug: open-armor-access-control-lists-api
- collection_type: open
  name: Container Security Account API
  slug: open-armor-account-api
- collection_type: open
  name: Armor Services Account Management API
  slug: open-armor-account-management-api
- collection_type: open
  name: Armor Services Account Primary Billing API
  slug: open-armor-accountprimarybilling-api
- collection_type: open
  name: Armor Services Active Response API
  slug: open-armor-activeresponse-api
- collection_type: open
  name: Armor Services Advanced Backup API
  slug: open-armor-advanced-backup-api
- collection_type: open
  name: MDR Public AIP - Entity Intelligence API
  slug: open-armor-aip-entity-intelligence-api
- collection_type: open
  name: MDR Public AIP - Incident Data API
  slug: open-armor-aip-incident-data-api
- collection_type: open
  name: Armor Compliance Assessments API
  slug: open-armor-assessments-api
- collection_type: open
  name: Armor FH-AUTH Security Authentication API
  slug: open-armor-authentication-api
- collection_type: open
  name: Accounts Cloud Connections API
  slug: open-armor-cloud-connections-api
- collection_type: open
  name: Container Security Connector API
  slug: open-armor-connector-api
- collection_type: open
  name: Armor Compliance CSPM Connector API
  slug: open-armor-cspm-connector-api
- collection_type: open
  name: Armor Compliance CSPM Control Remediation API
  slug: open-armor-cspm-control-remediation-api
- collection_type: open
  name: Armor Compliance CSPM Policies API
  slug: open-armor-cspm-policies-api
- collection_type: open
  name: Armor Compliance CSPM Policy Controls API
  slug: open-armor-cspm-policy-controls-api
- collection_type: open
  name: Armor Compliance CSPM Report API
  slug: open-armor-cspm-report-api
- collection_type: open
  name: Armor Compliance CSPM Report Configuration API
  slug: open-armor-cspm-report-configuration-api
- collection_type: open
  name: Armor Compliance CSPM Resources API
  slug: open-armor-cspm-resources-api
- collection_type: open
  name: Armor Compliance CSPM Summary API
  slug: open-armor-cspm-summary-api
- collection_type: open
  name: Armor Compliance CSPM Usage API
  slug: open-armor-cspm-usage-api
- collection_type: open
  name: MDR Public Defender - Investigation API
  slug: open-armor-defender-investigation-api
- collection_type: open
  name: MDR Public Defender - Machine Actions API
  slug: open-armor-defender-machine-actions-api
- collection_type: open
  name: MDR Public Defender - Machines API
  slug: open-armor-defender-machines-api
- collection_type: open
  name: MDR Public Detection Rules API
  slug: open-armor-detection-rules-api
- collection_type: open
  name: Armor Webhooks Detections API
  slug: open-armor-detections-api
- collection_type: open
  name: Incident Management EDR API
  slug: open-armor-edr-api
- collection_type: open
  name: Armor Webhooks Events API
  slug: open-armor-events-api
- collection_type: open
  name: Armor Log Management Flow Sources API
  slug: open-armor-flow-sources-api
- collection_type: open
  name: MDR Public Health API
  slug: open-armor-health-api
- collection_type: open
  name: Agent Management Health Monitoring Status API
  slug: open-armor-health-monitoring-status-api
- collection_type: open
  name: Container Security Image API
  slug: open-armor-image-api
- collection_type: open
  name: Armor Services Infrastructure API
  slug: open-armor-infrastructure-api
- collection_type: open
  name: MDR Public JSM - Incidents API
  slug: open-armor-jsm-incidents-api
- collection_type: open
  name: MDR Public JSM - Metrics API
  slug: open-armor-jsm-metrics-api
- collection_type: open
  name: MDR Public JSM - Organizations API
  slug: open-armor-jsm-organizations-api
- collection_type: open
  name: MDR Public JSM - Service Requests API
  slug: open-armor-jsm-service-requests-api
- collection_type: open
  name: Armor Services Keys API
  slug: open-armor-keys-api
- collection_type: open
  name: Armor Log Management Log Endpoints API
  slug: open-armor-log-endpoints-api
- collection_type: open
  name: Armor Log Management Log Groups API
  slug: open-armor-log-groups-api
- collection_type: open
  name: Armor Log Management Log Sources API
  slug: open-armor-log-sources-api
- collection_type: open
  name: Agent Management Malware Configuration API
  slug: open-armor-malware-configuration-api
- collection_type: open
  name: Armor Log Management Meta API
  slug: open-armor-meta-api
- collection_type: open
  name: Armor Services Network Services API
  slug: open-armor-network-services-api
- collection_type: open
  name: Armor Webhooks Notifications API
  slug: open-armor-notifications-api
- collection_type: open
  name: Notifications Preferences API
  slug: open-armor-preferences-api
- collection_type: open
  name: Container Security Registry API
  slug: open-armor-registry-api
- collection_type: open
  name: MDR Public Reports - MSR API
  slug: open-armor-reports-msr-api
- collection_type: open
  name: Agent Management Scheduled Tasks API
  slug: open-armor-scheduled-tasks-api
- collection_type: open
  name: Accounts Secure Notes API
  slug: open-armor-secure-notes-api
- collection_type: open
  name: Armor Services Security Analytics API
  slug: open-armor-security-analytics-api
- collection_type: open
  name: Armor Services Security API
  slug: open-armor-security-api
- collection_type: open
  name: Incident Management Security Detection Events API
  slug: open-armor-security-detection-events-api
- collection_type: open
  name: Incident Management Security Detections API
  slug: open-armor-security-detections-api
- collection_type: open
  name: Incident Management Security Detections Overview API
  slug: open-armor-security-detections-overview-api
- collection_type: open
  name: Armor Services Security Incidents API
  slug: open-armor-security-incidents-api
- collection_type: open
  name: Container Security Sensor API
  slug: open-armor-sensor-api
- collection_type: open
  name: Armor Services Support API
  slug: open-armor-support-api
- collection_type: open
  name: Agent Management Tags API
  slug: open-armor-tags-api
- collection_type: open
  name: MDR Public TI - Customer Intelligence API
  slug: open-armor-ti-customer-intelligence-api
- collection_type: open
  name: MDR Public TI - GraphQL API
  slug: open-armor-ti-graphql-api
- collection_type: open
  name: MDR Public TI - Threat Actors API
  slug: open-armor-ti-threat-actors-api
- collection_type: open
  name: Infrastructure Management Toolbox API
  slug: open-armor-toolbox-api
- collection_type: open
  name: Accounts Tours API
  slug: open-armor-tours-api
- collection_type: open
  name: Incident Management Trend API
  slug: open-armor-trend-api
- collection_type: open
  name: Armor User API
  slug: open-armor-user-api
- collection_type: open
  name: Armor Services Utilization API
  slug: open-armor-utilization-api
- collection_type: open
  name: Armor Compliance VS Exclusions API
  slug: open-armor-vs-exclusions-api
- collection_type: open
  name: Armor Compliance VS Reports API
  slug: open-armor-vs-reports-api
- collection_type: open
  name: Armor Compliance Vulnerability Scanning API
  slug: open-armor-vulnerability-scanning-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/armor-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/armor-accounts-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/armor-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/armor-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/armor-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.armor.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.armor.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.armor.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.armor.com/
- group: company
  title: ''
  type: Blog
  url: https://res.armor.com/resources/?fwp_type=blog&_type=blog
- group: operate
  title: ''
  type: Support
  url: https://www.armor.com/forms/under-attack
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/armor
- group: commercial
  title: ''
  type: Pricing
  url: https://www.armor.com/solutions/pricing
- group: start
  title: ''
  type: SignUp
  url: https://amp.armor.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://armor.pub/docs/Armor-General-Terms-of-Service.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.armor.com/legal/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.armor.com/why-armor/trusted-expertise
- group: operate
  title: ''
  type: StatusPage
  url: https://status.armor.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/armor-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/armor-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/armor-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/armor-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/armor-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/armor-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/armor-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/armor-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/armor-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/armor-webhooks-events.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-06'
description: 'Armor (legal name Armor Defense Inc.) is a cybersecurity company headquartered in Plano, Texas, founded as FireHost in 2009 by Chris Drake and rebranded as Armor as its portfolio expanded from secure cloud hosting into managed security. Armor sells vendor-agnostic, cloud-native managed detection and response (Armor MDR), compliant managed private cloud (Armor Enterprise Cloud), the Armor Agent workload protection agent (formerly Armor Anywhere), and compliance and offensive-security professional services, to more than 1,700 organizations across 40 countries with a 24/7 follow-the-sun SOC operating from Plano, London, Singapore and Pune. Armor publishes a public developer portal at developer.armor.com that serves sixteen machine-readable contracts through ReDoc: four Swagger 2.0 documents for the original v1 Armor Services API on api.armor.com (account management, infrastructure, security and support, 254 operations) and twelve OpenAPI 3.0.3 documents for the v2 platform on
  *.api.secure-prod.services (accounts, agent management, compliance and CSPM, container security, incident management, infrastructure management, log management, notifications, webhooks, the unified MDR public API, and the ARMOR-PSK and FH-AUTH authentication contracts). Armor also publishes a detailed first-party llms.txt at armor.com/llms.txt and holds SOC 2 Type II, HITRUST CSF, PCI DSS Level 1 Service Provider, ISO 27001, TX-RAMP Level 2, HIPAA and Data Privacy Framework attestations.'
image: https://framerusercontent.com/images/iwYUUtUgg7arqxZ6LH5PMsmFouE.png
layout: provider
mcp_servers:
- description: ''
  name: Armor MCP Server
  slug: armor-mcp-server
modified: '2026-08-06'
name: Armor
nav: Providers
network: true
overview: 'Armor publishes 70 APIs on the [APIs.io](https://apis.io/) network, including Access Control Lists API, Account API, Account Management API, and 67 more. Tagged areas include Company, Cybersecurity, Managed Detection and Response, Cloud Security, and Compliance.


  The Armor catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Armor''s developer surface includes documentation, API reference, engineering blog, support, pricing, signup flow, authentication, and 22 more developer resources.'
random_paper: 20
scopes:
- name: Armor Scopes
  scope_count: 4
  slug: armor-scopes
  summary_line: 4 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 47.4
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 30.3
    contract_quality: 64.3
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 30.3
    operational_transparency: 10.5
  previous_composite: 47.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 70
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/armor/refs/heads/main/screenshots/armor-2026-08-07T161726.png
security:
- kind: authentication
  name: Armor Authentication
  slug: armor-authentication
  summary_line: apiKey/http/oauth2 · 6 schemes
- kind: domain-security
  name: Armor Domain Security
  slug: armor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: armor
tags:
- Company
- Cybersecurity
- Managed Detection and Response
- Cloud Security
- Compliance
- SIEM
- Vulnerability Management
- Endpoint Security
- Threat Intelligence
- Managed Private Cloud
- CSPM
- Container Security
website: https://www.armor.com/
---
