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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Tufin Agentic Access
  operation_count: 23
  slug: tufin-agentic-access
  summary_line: 23 operations · 5 acting
api_count: 14
apis:
- description: API for application-centric security policy management and micro-segmentation. SecureApp enables teams to manage security policies at the application level, define connectivity requirements, and autom
  name: Tufin SecureApp API
  slug: tufin-secureapp-api
- description: GraphQL API for the Tufin Orchestration Suite providing flexible querying capabilities for security policy data, network topology, and compliance information. Uses OAuth2 authentication and supports c
  name: Tufin SecureTrack GraphQL API
  slug: tufin-securetrack-graphql-api
- description: REST API for Tufin SecureCloud, the cloud-native security policy management platform. Provides endpoints for managing cloud accounts, applications, assets, Kubernetes clusters, and security policies a
  name: Tufin SecureCloud API
  slug: tufin-securecloud-api
- description: Policy compliance and risk analysis
  name: Tufin Compliance API
  slug: tufin-compliance-api
- description: Manage network devices and firewalls
  name: Tufin Devices API
  slug: tufin-devices-api
- description: Network objects, services, and address groups
  name: Tufin Objects API
  slug: tufin-objects-api
- description: Device policy revisions and change history
  name: Tufin Revisions API
  slug: tufin-revisions-api
- description: Query and manage firewall rules and policies
  name: Tufin Rules API
  slug: tufin-rules-api
- description: Workflow tasks and approvals
  name: Tufin Tasks API
  slug: tufin-tasks-api
- description: Create and manage security change tickets
  name: Tufin Tickets API
  slug: tufin-tickets-api
- description: Network topology analysis and path queries
  name: Tufin Topology API
  slug: tufin-topology-api
- description: User and group management
  name: Tufin Users API
  slug: tufin-users-api
- description: Workflow template definitions
  name: Tufin Workflow Definitions API
  slug: tufin-workflow-definitions-api
- description: Security zones and zone-to-zone matrix
  name: Tufin Zones API
  slug: tufin-zones-api
artifact_total: 60
collections:
- collection_type: postman
  name: Tufin SecureChange REST Compliance API
  slug: postman-tufin-compliance-api
- collection_type: postman
  name: Tufin SecureChange REST Compliance Devices API
  slug: postman-tufin-devices-api
- collection_type: postman
  name: Tufin SecureChange REST Compliance Objects API
  slug: postman-tufin-objects-api
- collection_type: postman
  name: Tufin SecureChange REST Compliance Revisions API
  slug: postman-tufin-revisions-api
- collection_type: postman
  name: Tufin SecureChange REST Compliance Rules API
  slug: postman-tufin-rules-api
- collection_type: postman
  name: Tufin SecureChange REST Compliance Tasks API
  slug: postman-tufin-tasks-api
- collection_type: postman
  name: Tufin SecureChange REST Compliance Tickets API
  slug: postman-tufin-tickets-api
- collection_type: postman
  name: Tufin SecureChange REST Compliance Topology API
  slug: postman-tufin-topology-api
- collection_type: postman
  name: Tufin SecureChange REST Compliance Users API
  slug: postman-tufin-users-api
- collection_type: postman
  name: Tufin SecureChange REST Compliance Workflow Definitions API
  slug: postman-tufin-workflow-definitions-api
- collection_type: postman
  name: Tufin SecureChange REST Compliance Zones API
  slug: postman-tufin-zones-api
- collection_type: open
  name: Tufin SecureChange REST API
  slug: open-tufin-securechange
- collection_type: open
  name: Tufin SecureTrack REST API
  slug: open-tufin-securetrack
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/tufin/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tufin-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tufin-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tufin-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tufin-technologies
- group: start
  title: ''
  type: Portal
  url: https://forum.tufin.com/
- group: operate
  title: ''
  type: Support
  url: https://www.tufin.com/support
- group: docs
  title: ''
  type: Documentation
  url: https://forum.tufin.com/support/kc
- group: company
  title: ''
  type: Blog
  url: https://www.tufin.com/blog
- group: start
  title: ''
  type: Login
  url: https://portal.tufin.io/
- group: operate
  title: ''
  type: Contact
  url: https://www.tufin.com/company/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tufin.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tufin.com/terms-of-use
- group: company
  title: ''
  type: Website
  url: https://www.tufin.com
- group: start
  title: ''
  type: GettingStarted
  url: https://forum.tufin.com/support/kc/latest/Content/Suite/RESTAPI/4423.htm
- group: operate
  title: ''
  type: Community
  url: https://community.tufin.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Tufin
- group: build
  title: ''
  type: SDKs
  url: https://gitlab.com/tufinps/pytos2-ce
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Tufin/pytos
- group: build
  title: ''
  type: PostmanCollection
  url: https://github.com/Tufin/postman
- group: start
  title: ''
  type: Signup
  url: https://www.tufin.com/demo
- group: learn
  title: ''
  type: Videos
  url: https://www.tufin.com/resources/type/videos
- group: other
  title: ''
  type: Developers
  url: https://www.tufin.com/developers
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/tufin-securetrack-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/tufin-securechange-openapi.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tufin-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tufin-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tufin-device-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tufin-ticket-schema.json
created: '2025'
description: Tufin provides security policy orchestration solutions for managing network security policies across hybrid cloud environments, including firewalls, SDN, and cloud security controls. The Tufin Orchestration Suite (TOS) includes SecureTrack for network topology and policy analysis, SecureChange for automated policy change workflows, SecureApp for application-centric policy management, and SecureCloud for cloud-native security posture management. Tufin offers comprehensive REST APIs and GraphQL APIs for integrating with ITSM, SIEM, and other security tools.
examples:
- key_count: 2
  name: Tufin Createticket Example
  slug: tufin-createTicket-example
- key_count: 2
  name: Tufin Getdevices Example
  slug: tufin-getDevices-example
- key_count: 2
  name: Tufin Getrulesbydevice Example
  slug: tufin-getRulesByDevice-example
- key_count: 2
  name: Tufin Gettopologypath Example
  slug: tufin-getTopologyPath-example
finops:
- name: Tufin Finops
  service_category: Network Security Policy Management
  slug: tufin-finops
graphqls:
- description: GraphQL API for the Tufin Orchestration Suite providing flexible querying capabilities for security policy data, network topology, and compliance information. Uses OAuth2 authentication and supports c
  name: Tufin GraphQL API
  slug: tufin-graphql
image: https://www.tufin.com/themes/custom/tufin/logo.svg
json_schemas:
- name: Tufin SecureTrack Device
  property_count: 9
  slug: tufin-device
- name: DeviceInput
  property_count: 4
  slug: tufin-deviceinput
- name: NetworkObject
  property_count: 5
  slug: tufin-networkobject
- name: Revision
  property_count: 4
  slug: tufin-revision
- name: RiskFinding
  property_count: 5
  slug: tufin-riskfinding
- name: Rule
  property_count: 9
  slug: tufin-rule
- name: Service
  property_count: 4
  slug: tufin-service
- name: Task
  property_count: 7
  slug: tufin-task
- name: TaskUpdate
  property_count: 3
  slug: tufin-taskupdate
- name: Tufin SecureChange Ticket
  property_count: 10
  slug: tufin-ticket
- name: TicketInput
  property_count: 6
  slug: tufin-ticketinput
- name: TopologyMap
  property_count: 2
  slug: tufin-topologymap
- name: TopologyPath
  property_count: 3
  slug: tufin-topologypath
- name: User
  property_count: 6
  slug: tufin-user
- name: WorkflowDefinition
  property_count: 5
  slug: tufin-workflowdefinition
- name: Zone
  property_count: 4
  slug: tufin-zone
json_structures:
- name: Tufin Device Structure
  property_count: 0
  slug: tufin-device-structure
- name: Tufin Structure
  property_count: 0
  slug: tufin-structure
- name: Tufin Ticket Structure
  property_count: 0
  slug: tufin-ticket-structure
jsonld:
- class_count: 0
  name: Tufin Context
  property_count: 6
  slug: tufin-context
layout: provider
modified: '2026-05-19'
name: Tufin
nav: Providers
network: true
overview: 'Tufin publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Compliance API, Devices API, Objects API, and 8 more. Tagged areas include Cloud Security, Compliance, Firewall Management, Network Security, and Network Topology.


  The Tufin catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tufin''s developer surface includes authentication, developer portal, support, documentation, engineering blog, getting-started guide, signup flow, and 22 more developer resources.'
plans:
- name: Tufin Plans Pricing
  plan_count: 1
  slug: tufin-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 1
  name: Tufin Rate Limits
  slug: tufin-rate-limits
rules:
- name: Tufin API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tufin-jsonschema-spectral-rules
- name: Tufin API Rules
  rule_count: 11
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 8
  slug: tufin-securetrack-rules
score:
  band: developing
  composite: 51.2
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 60.2
    developer_ergonomics: 56.5
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 10.5
  previous_composite: 51.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tufin/refs/heads/main/screenshots/tufin-2026-06-20T195822.png
security:
- kind: authentication
  name: Tufin Authentication
  slug: tufin-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tufin Domain Security
  slug: tufin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tufin
tags:
- Cloud Security
- Compliance
- Firewall Management
- Network Security
- Network Topology
- Policy Orchestration
- Risk Management
- Security Policy Management
- Zero Trust
website: https://www.tufin.com
---
