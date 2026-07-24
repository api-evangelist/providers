---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 13
  human_in_the_loop: 1
  name: Acronis Agentic Access
  operation_count: 30
  slug: acronis-agentic-access
  summary_line: 30 operations · 13 acting · 1 human-in-the-loop
api_count: 17
apis:
- description: Acronis Resource and Policy Management API enables organizations to efficiently manage resources and policies within their IT infrastructure.
  name: Acronis Resource and Policy Management API
  slug: resource-and-policy-management-api
- description: The Acronis Advanced Automation API allows users to automate and streamline their backup and recovery processes with custom scripts and workflows.
  name: Acronis Advanced Automation API
  slug: advanced-automation-api
- description: The Acronis Event Manager API allows users to monitor and manage events across their entire Acronis ecosystem with real-time access to event data.
  name: Acronis Event Manager API
  slug: event-manager-api
- description: The Acronis Disaster Recovery Service API allows organizations to automate and streamline their disaster recovery processes.
  name: Acronis Disaster Recovery Service API
  slug: disaster-recovery-service-api
- description: The Acronis Endpoint Detection and Response API is a comprehensive security solution that helps organizations detect and respond to cybersecurity threats in real-time.
  name: Acronis Endpoint Detection and Response API
  slug: endpoint-detection-and-response-api
- description: The Acronis Vault Manager REST API allows users to manage and interact with their Acronis Vault storage solutions programmatically.
  name: Acronis Vault Manager REST API
  slug: vault-manager-rest-api
- description: Task activity and sub-operation tracking
  name: Acronis Activities API
  slug: acronis-activities-api
- description: Agent update configuration and execution
  name: Acronis Agent Updates API
  slug: acronis-agent-updates-api
- description: Acronis protection agent management
  name: Acronis Agents API
  slug: acronis-agents-api
- description: Token issuance, revocation, and introspection
  name: Acronis Authentication API
  slug: acronis-authentication-api
- description: OAuth2 client credential management
  name: Acronis Clients API
  slug: acronis-clients-api
- description: Hardware node management
  name: Acronis Hardware Nodes API
  slug: acronis-hardware-nodes-api
- description: Offering items, quotas, and edition management
  name: Acronis Licensing API
  slug: acronis-licensing-api
- description: Backup and protection task monitoring
  name: Acronis Tasks API
  slug: acronis-tasks-api
- description: Tenant hierarchy management and configuration
  name: Acronis Tenants API
  slug: acronis-tenants-api
- description: Usage metrics and reporting
  name: Acronis Usage API
  slug: acronis-usage-api
- description: User account management within tenants
  name: Acronis Users API
  slug: acronis-users-api
artifact_total: 130
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/acronis-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/acronis-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acronis-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/acronis-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/acronis
- group: start
  title: ''
  type: Portal
  url: https://developer.acronis.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.acronis.com/doc/outbound/apis/getting-started/index.html
- group: auth
  title: ''
  type: Authentication
  url: https://developer.acronis.com/doc/outbound/apis/authentication/index.html
- group: company
  title: ''
  type: Blog
  url: https://www.acronis.com/en-us/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.acronis.com/en-us/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.acronis.com/en-us/products/cloud/cyber-protect/pricing/
- group: company
  title: ''
  type: Partners
  url: https://www.acronis.com/en-us/partners/
- group: other
  title: ''
  type: CaseStudies
  url: https://www.acronis.com/en-us/resource-center/category/case-studies/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/acronis
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/rules/acronis-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/vocabulary/acronis-vocabulary.yaml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.acronis.com/en-us/legal/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.acronis.com/doc/outbound/apis/index.html
created: '2025-02-17'
description: Acronis is a leading provider of cyber protection solutions that deliver innovative technology to protect data, applications, and systems from the ever-evolving threats of today's digital world. They offer a comprehensive suite of products, including backup and disaster recovery solutions, file sync and share services, and anti-malware protection.
examples:
- key_count: 6
  name: Account Management Client Example
  slug: account-management-client-example
- key_count: 7
  name: Account Management Contact Example
  slug: account-management-contact-example
- key_count: 5
  name: Account Management Offering Item Example
  slug: account-management-offering-item-example
- key_count: 3
  name: Account Management Quota Example
  slug: account-management-quota-example
- key_count: 3
  name: Account Management Report Example
  slug: account-management-report-example
- key_count: 2
  name: Account Management Search Results Example
  slug: account-management-search-results-example
- key_count: 10
  name: Account Management Tenant Example
  slug: account-management-tenant-example
- key_count: 5
  name: Account Management Token Response Example
  slug: account-management-token-response-example
- key_count: 4
  name: Account Management Usage Item Example
  slug: account-management-usage-item-example
- key_count: 8
  name: Account Management User Example
  slug: account-management-user-example
- key_count: 6
  name: Acronis Createtenant Example
  slug: acronis-createtenant-example
- key_count: 6
  name: Acronis Getagent Example
  slug: acronis-getagent-example
- key_count: 6
  name: Acronis Gettask Example
  slug: acronis-gettask-example
- key_count: 6
  name: Acronis Listagents Example
  slug: acronis-listagents-example
- key_count: 6
  name: Acronis Listtasks Example
  slug: acronis-listtasks-example
- key_count: 6
  name: Acronis Listtenants Example
  slug: acronis-listtenants-example
- key_count: 8
  name: Agent Management Agent Example
  slug: agent-management-agent-example
- key_count: 4
  name: Agent Management Agent O S Example
  slug: agent-management-agent-o-s-example
- key_count: 3
  name: Agent Management Agent Update Settings Example
  slug: agent-management-agent-update-settings-example
- key_count: 5
  name: Agent Management Hardware Node Example
  slug: agent-management-hardware-node-example
- key_count: 10
  name: Task Manager Activity Example
  slug: task-manager-activity-example
- key_count: 14
  name: Task Manager Task Example
  slug: task-manager-task-example
features:
- description: Multi-tier tenant management for MSPs, partners, and customers with offering item quotas.
  name: Tenant Hierarchy Management
- description: Remote management of Acronis backup agents across Windows, Linux, macOS, and cloud workloads.
  name: Agent Management
- description: Real-time monitoring of backup and protection tasks with state, result, and activity tracking.
  name: Backup Task Monitoring
- description: Automated usage metrics collection and report generation for billing and capacity planning.
  name: Usage Reporting
- description: Programmatic creation and application of protection policies to resources.
  name: Policy Management
- description: Automated failover and recovery orchestration for business continuity.
  name: Disaster Recovery API
- description: EDR capabilities for threat detection, investigation, and response via API.
  name: Endpoint Detection and Response
finops:
- name: Acronis Finops
  service_category: Cyber Protection / Backup / Endpoint Security
  slug: acronis-finops
image: /assets/icons/acronis.png
integrations:
- description: Integration with ConnectWise, Autotask, and other PSA platforms for MSP billing and ticketing.
  name: PSA Platforms
- description: Event streaming to SIEM platforms via Event Manager API for security monitoring.
  name: SIEM Systems
- description: Integration with RMM platforms for agent deployment and backup policy management.
  name: RMM Tools
- description: Usage data export for automated billing via usage and offering item APIs.
  name: Billing Systems
json_schemas:
- name: Client
  property_count: 6
  slug: account-management-client
- name: Contact
  property_count: 7
  slug: account-management-contact
- name: OfferingItem
  property_count: 5
  slug: account-management-offering-item
- name: Quota
  property_count: 3
  slug: account-management-quota
- name: Report
  property_count: 3
  slug: account-management-report
- name: SearchResults
  property_count: 2
  slug: account-management-search-results
- name: Tenant
  property_count: 10
  slug: account-management-tenant
- name: TokenResponse
  property_count: 5
  slug: account-management-token-response
- name: UsageItem
  property_count: 4
  slug: account-management-usage-item
- name: User
  property_count: 8
  slug: account-management-user
- name: Activity
  property_count: 10
  slug: acronis-activity
- name: ActivityList
  property_count: 2
  slug: acronis-activitylist
- name: Agent
  property_count: 8
  slug: acronis-agent
- name: AgentList
  property_count: 2
  slug: acronis-agentlist
- name: AgentOS
  property_count: 4
  slug: acronis-agentos
- name: AgentUpdateSettings
  property_count: 3
  slug: acronis-agentupdatesettings
- name: Client
  property_count: 6
  slug: acronis-client
- name: ClientList
  property_count: 1
  slug: acronis-clientlist
- name: ClientRequest
  property_count: 3
  slug: acronis-clientrequest
- name: Contact
  property_count: 7
  slug: acronis-contact
- name: Error
  property_count: 3
  slug: acronis-error
- name: HardwareNode
  property_count: 5
  slug: acronis-hardwarenode
- name: HardwareNodeList
  property_count: 1
  slug: acronis-hardwarenodelist
- name: MaintenanceWindow
  property_count: 3
  slug: acronis-maintenancewindow
- name: OfferingItem
  property_count: 5
  slug: acronis-offeringitem
- name: OfferingItemList
  property_count: 1
  slug: acronis-offeringitemlist
- name: OfferingItemUpdateRequest
  property_count: 1
  slug: acronis-offeringitemupdaterequest
- name: Paging
  property_count: 1
  slug: acronis-paging
- name: Quota
  property_count: 3
  slug: acronis-quota
- name: Report
  property_count: 3
  slug: acronis-report
- name: ReportRequest
  property_count: 2
  slug: acronis-reportrequest
- name: SearchResults
  property_count: 2
  slug: acronis-searchresults
- name: Task
  property_count: 14
  slug: acronis-task
- name: TaskList
  property_count: 2
  slug: acronis-tasklist
- name: Tenant
  property_count: 10
  slug: acronis-tenant
- name: TenantList
  property_count: 2
  slug: acronis-tenantlist
- name: TenantRequest
  property_count: 5
  slug: acronis-tenantrequest
- name: TokenResponse
  property_count: 5
  slug: acronis-tokenresponse
- name: UsageItem
  property_count: 4
  slug: acronis-usageitem
- name: UsageList
  property_count: 1
  slug: acronis-usagelist
- name: User
  property_count: 8
  slug: acronis-user
- name: UserList
  property_count: 2
  slug: acronis-userlist
- name: AgentOS
  property_count: 4
  slug: agent-management-agent-o-s
- name: Agent
  property_count: 8
  slug: agent-management-agent
- name: AgentUpdateSettings
  property_count: 3
  slug: agent-management-agent-update-settings
- name: HardwareNode
  property_count: 5
  slug: agent-management-hardware-node
- name: Activity
  property_count: 10
  slug: task-manager-activity
- name: Task
  property_count: 14
  slug: task-manager-task
json_structures:
- name: Account Management Client Structure
  property_count: 6
  slug: account-management-client-structure
- name: Account Management Contact Structure
  property_count: 7
  slug: account-management-contact-structure
- name: Account Management Offering Item Structure
  property_count: 5
  slug: account-management-offering-item-structure
- name: Account Management Quota Structure
  property_count: 3
  slug: account-management-quota-structure
- name: Account Management Report Structure
  property_count: 3
  slug: account-management-report-structure
- name: Account Management Search Results Structure
  property_count: 2
  slug: account-management-search-results-structure
- name: Account Management Tenant Structure
  property_count: 10
  slug: account-management-tenant-structure
- name: Account Management Token Response Structure
  property_count: 5
  slug: account-management-token-response-structure
- name: Account Management Usage Item Structure
  property_count: 4
  slug: account-management-usage-item-structure
- name: Account Management User Structure
  property_count: 8
  slug: account-management-user-structure
- name: Acronis Structure
  property_count: 0
  slug: acronis-structure
- name: Agent Management Agent O S Structure
  property_count: 4
  slug: agent-management-agent-o-s-structure
- name: Agent Management Agent Structure
  property_count: 8
  slug: agent-management-agent-structure
- name: Agent Management Agent Update Settings Structure
  property_count: 3
  slug: agent-management-agent-update-settings-structure
- name: Agent Management Hardware Node Structure
  property_count: 5
  slug: agent-management-hardware-node-structure
- name: Task Manager Activity Structure
  property_count: 10
  slug: task-manager-activity-structure
- name: Task Manager Task Structure
  property_count: 14
  slug: task-manager-task-structure
jsonld:
- class_count: 18
  name: Acronis Context
  property_count: 61
  slug: acronis-context
layout: provider
modified: '2026-04-19'
name: Acronis
nav: Providers
network: true
overview: 'Acronis publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Agent Updates API, Agents API, and 8 more. Tagged areas include Cybersecurity, Data Protection, and Endpoint Management.


  The Acronis catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Acronis'' developer surface includes authentication, developer portal, getting-started guide, engineering blog, support, pricing, changelog, and 11 more developer resources.'
plans:
- name: Acronis Plans Pricing
  plan_count: 4
  slug: acronis-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 1
  name: Acronis Rate Limits
  slug: acronis-rate-limits
rules:
- name: Acronis API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: acronis-jsonschema-spectral-rules
- name: Acronis API Rules
  rule_count: 38
  severity_counts:
    error: 15
    hint: 0
    info: 7
    warn: 16
  slug: acronis-spectral-rules
score:
  band: strong
  composite: 60.6
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 70.7
    developer_ergonomics: 37.0
    discoverability: 75.0
    governance: 86.8
    operational_transparency: 42.1
  previous_composite: 60.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/screenshots/acronis-2026-06-20T164007.png
security:
- kind: authentication
  name: Acronis Authentication
  slug: acronis-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Acronis Domain Security
  slug: acronis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Acronis Vulnerability Disclosure
  slug: acronis-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: acronis
tags:
- Cybersecurity
- Data Protection
- Endpoint Management
use_cases:
- description: Automate tenant provisioning, licensing management, and usage reporting for managed service providers.
  name: MSP Platform Automation
- description: Build custom dashboards tracking backup task status, failures, and completion rates.
  name: Backup Monitoring Dashboard
- description: Monitor agent online status, version compliance, and update management across endpoints.
  name: Agent Health Monitoring
- description: Generate automated reports on data protection status for compliance and audit requirements.
  name: Compliance Reporting
- description: Trigger and monitor DR failover workflows programmatically for RTO/RPO compliance.
  name: Disaster Recovery Automation
website: https://developer.acronis.com/
---
