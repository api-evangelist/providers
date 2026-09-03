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
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 25
  human_in_the_loop: 2
  name: Commvault Agentic Access
  operation_count: 60
  slug: commvault-agentic-access
  summary_line: 60 operations · 25 acting · 2 human-in-the-loop
api_count: 3
apis:
- baseURL: https://webserver.commvault.com/webconsole/api
  baseurl_source: declared
  description: Manage backup agents installed on clients
  name: Commvault Agents API
  slug: commvault-agents-api
- baseURL: https://webserver.commvault.com/webconsole/api
  baseurl_source: declared
  description: Manage alerts and notification configurations
  name: Commvault Alerts API
  slug: commvault-alerts-api
- baseURL: https://webserver.commvault.com/webconsole/api
  baseurl_source: declared
  description: Login and token management operations
  name: Commvault Authentication API
  slug: commvault-authentication-api
- baseURL: https://webserver.commvault.com/webconsole/api
  baseurl_source: declared
  description: Manage clients (servers, workstations, virtual machines)
  name: Commvault Clients API
  slug: commvault-clients-api
- baseURL: https://webserver.commvault.com/webconsole/api
  baseurl_source: declared
  description: Dashboard summary and health monitoring
  name: Commvault Dashboard API
  slug: commvault-dashboard-api
- baseURL: https://webserver.commvault.com/webconsole/api
  baseurl_source: declared
  description: Manage database protection
  name: Commvault Databases API
  slug: commvault-databases-api
- baseURL: https://webserver.commvault.com/webconsole/api
  baseurl_source: declared
  description: Manage file server protection
  name: Commvault File Servers API
  slug: commvault-file-servers-api
- baseURL: https://webserver.commvault.com/webconsole/api
  baseurl_source: declared
  description: View and manage backup, restore, and administrative jobs
  name: Commvault Jobs API
  slug: commvault-jobs-api
- baseURL: https://webserver.commvault.com/webconsole/api
  baseurl_source: declared
  description: Manage laptop backup operations
  name: Commvault Laptops API
  slug: commvault-laptops-api
- baseURL: https://webserver.commvault.com/webconsole/api
  baseurl_source: declared
  description: Trigger and monitor automated operations
  name: Commvault Operations API
  slug: commvault-operations-api
- baseURL: https://webserver.commvault.com/webconsole/api
  baseurl_source: declared
  description: Manage server plans for data protection
  name: Commvault Plans API
  slug: commvault-plans-api
- baseURL: https://webserver.commvault.com/webconsole/api
  baseurl_source: declared
  description: Manage data protection policies
  name: Commvault Policies API
  slug: commvault-policies-api
- baseURL: https://webserver.commvault.com/webconsole/api
  baseurl_source: declared
  description: Reporting and analytics
  name: Commvault Reports API
  slug: commvault-reports-api
- baseURL: https://webserver.commvault.com/webconsole/api
  baseurl_source: declared
  description: Manage schedule policies for automated operations
  name: Commvault Schedule Policies API
  slug: commvault-schedule-policies-api
- baseURL: https://webserver.commvault.com/webconsole/api
  baseurl_source: declared
  description: Manage job schedules and schedule policies
  name: Commvault Schedules API
  slug: commvault-schedules-api
- baseURL: https://webserver.commvault.com/webconsole/api
  baseurl_source: declared
  description: Manage and execute automation scripts
  name: Commvault Scripts API
  slug: commvault-scripts-api
- baseURL: https://webserver.commvault.com/webconsole/api
  baseurl_source: declared
  description: Manage server groups for organizing protected infrastructure
  name: Commvault Server Groups API
  slug: commvault-server-groups-api
- baseURL: https://webserver.commvault.com/webconsole/api
  baseurl_source: declared
  description: Service Level Agreement compliance monitoring
  name: Commvault SLA API
  slug: commvault-sla-api
- baseURL: https://webserver.commvault.com/webconsole/api
  baseurl_source: declared
  description: Storage pool and library management
  name: Commvault Storage API
  slug: commvault-storage-api
- baseURL: https://webserver.commvault.com/webconsole/api
  baseurl_source: declared
  description: Manage storage policies and copies
  name: Commvault Storage Policies API
  slug: commvault-storage-policies-api
- baseURL: https://webserver.commvault.com/webconsole/api
  baseurl_source: declared
  description: Manage subclients that define backup content
  name: Commvault Subclients API
  slug: commvault-subclients-api
- baseURL: https://webserver.commvault.com/webconsole/api
  baseurl_source: declared
  description: Manage Commvault users and user groups
  name: Commvault Users API
  slug: commvault-users-api
- baseURL: https://webserver.commvault.com/webconsole/api
  baseurl_source: declared
  description: Manage virtual machine backup and recovery
  name: Commvault Virtual Machines API
  slug: commvault-virtual-machines-api
- baseURL: https://webserver.commvault.com/webconsole/api
  baseurl_source: declared
  description: Create, manage, and execute automation workflows
  name: Commvault Workflows API
  slug: commvault-workflows-api
artifact_total: 87
collections:
- collection_type: postman
  name: Commvault Automation Agents API
  slug: postman-commvault-agents-api
- collection_type: postman
  name: Commvault Automation Agents Alerts API
  slug: postman-commvault-alerts-api
- collection_type: postman
  name: Commvault Automation Agents Authentication API
  slug: postman-commvault-authentication-api
- collection_type: postman
  name: Commvault Automation Agents Clients API
  slug: postman-commvault-clients-api
- collection_type: postman
  name: Commvault Automation Agents Dashboard API
  slug: postman-commvault-dashboard-api
- collection_type: postman
  name: Commvault Automation Agents Databases API
  slug: postman-commvault-databases-api
- collection_type: postman
  name: Commvault Automation Agents File Servers API
  slug: postman-commvault-file-servers-api
- collection_type: postman
  name: Commvault Automation Agents Jobs API
  slug: postman-commvault-jobs-api
- collection_type: postman
  name: Commvault Automation Agents Laptops API
  slug: postman-commvault-laptops-api
- collection_type: postman
  name: Commvault Automation Agents Operations API
  slug: postman-commvault-operations-api
- collection_type: postman
  name: Commvault Automation Agents Plans API
  slug: postman-commvault-plans-api
- collection_type: postman
  name: Commvault Automation Agents Policies API
  slug: postman-commvault-policies-api
- collection_type: postman
  name: Commvault Automation Agents Reports API
  slug: postman-commvault-reports-api
- collection_type: postman
  name: Commvault Automation Agents Schedule Policies API
  slug: postman-commvault-schedule-policies-api
- collection_type: postman
  name: Commvault Automation Agents Schedules API
  slug: postman-commvault-schedules-api
- collection_type: postman
  name: Commvault Automation Agents Scripts API
  slug: postman-commvault-scripts-api
- collection_type: postman
  name: Commvault Automation Agents Server Groups API
  slug: postman-commvault-server-groups-api
- collection_type: postman
  name: Commvault Automation Agents SLA API
  slug: postman-commvault-sla-api
- collection_type: postman
  name: Commvault Automation Agents Storage API
  slug: postman-commvault-storage-api
- collection_type: postman
  name: Commvault Automation Agents Storage Policies API
  slug: postman-commvault-storage-policies-api
- collection_type: postman
  name: Commvault Automation Agents Subclients API
  slug: postman-commvault-subclients-api
- collection_type: postman
  name: Commvault Automation Agents Users API
  slug: postman-commvault-users-api
- collection_type: postman
  name: Commvault Automation Agents Virtual Machines API
  slug: postman-commvault-virtual-machines-api
- collection_type: postman
  name: Commvault Automation Agents Workflows API
  slug: postman-commvault-workflows-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Commvault Automation Agents API
  slug: open-commvault-agents-api
- collection_type: open
  name: Commvault Automation Agents Alerts API
  slug: open-commvault-alerts-api
- collection_type: open
  name: Commvault Automation Agents Authentication API
  slug: open-commvault-authentication-api
- collection_type: open
  name: Commvault Automation API
  slug: open-commvault-automation
- collection_type: open
  name: Commvault Automation Agents Clients API
  slug: open-commvault-clients-api
- collection_type: open
  name: Commvault Command Center API
  slug: open-commvault-command-center
- collection_type: open
  name: Commvault Automation Agents Dashboard API
  slug: open-commvault-dashboard-api
- collection_type: open
  name: Commvault Automation Agents Databases API
  slug: open-commvault-databases-api
- collection_type: open
  name: Commvault Automation Agents File Servers API
  slug: open-commvault-file-servers-api
- collection_type: open
  name: Commvault Automation Agents Jobs API
  slug: open-commvault-jobs-api
- collection_type: open
  name: Commvault Automation Agents Laptops API
  slug: open-commvault-laptops-api
- collection_type: open
  name: Commvault Automation Agents Operations API
  slug: open-commvault-operations-api
- collection_type: open
  name: Commvault Automation Agents Plans API
  slug: open-commvault-plans-api
- collection_type: open
  name: Commvault Automation Agents Policies API
  slug: open-commvault-policies-api
- collection_type: open
  name: Commvault Automation Agents Reports API
  slug: open-commvault-reports-api
- collection_type: open
  name: Commvault REST API
  slug: open-commvault-rest
- collection_type: open
  name: Commvault Automation Agents Schedule Policies API
  slug: open-commvault-schedule-policies-api
- collection_type: open
  name: Commvault Automation Agents Schedules API
  slug: open-commvault-schedules-api
- collection_type: open
  name: Commvault Automation Agents Scripts API
  slug: open-commvault-scripts-api
- collection_type: open
  name: Commvault Automation Agents Server Groups API
  slug: open-commvault-server-groups-api
- collection_type: open
  name: Commvault Automation Agents SLA API
  slug: open-commvault-sla-api
- collection_type: open
  name: Commvault Automation Agents Storage API
  slug: open-commvault-storage-api
- collection_type: open
  name: Commvault Automation Agents Storage Policies API
  slug: open-commvault-storage-policies-api
- collection_type: open
  name: Commvault Automation Agents Subclients API
  slug: open-commvault-subclients-api
- collection_type: open
  name: Commvault Automation Agents Users API
  slug: open-commvault-users-api
- collection_type: open
  name: Commvault Automation Agents Virtual Machines API
  slug: open-commvault-virtual-machines-api
- collection_type: open
  name: Commvault Automation Agents Workflows API
  slug: open-commvault-workflows-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/commvault/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/commvault-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/commvault-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/commvault-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Commvault
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/commvault
- group: start
  title: ''
  type: Portal
  url: https://cloud.commvault.com/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.commvault.com/
- group: operate
  title: ''
  type: Support
  url: https://www.commvault.com/support
- group: start
  title: ''
  type: Login
  url: https://login.commvault.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.commvault.com/
- group: company
  title: ''
  type: Blog
  url: https://www.commvault.com/blogs
- group: operate
  title: ''
  type: Contact
  url: https://www.commvault.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.commvault.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.commvault.com/terms-of-use
- group: design
  title: ''
  type: JSONLD
  url: json-ld/commvault-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/commvault-backup-job-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/commvault-client-schema.json
created: '2025-01-20'
description: Commvault is a cloud-native cyber resilience platform that delivers unified data security, identity resilience, and cyber recovery. The Commvault REST API, Command Center API, and Automation API provide programmatic access to backup, restore, replication, threat scan, reporting, and orchestration capabilities across enterprise workloads spanning on-premises, virtual machines, and cloud applications.
finops:
- name: Commvault Finops
  service_category: Data Protection
  slug: commvault-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/commvault.png
json_schemas:
- name: Commvault Backup Job
  property_count: 16
  slug: commvault-backup-job
- name: Commvault Client
  property_count: 13
  slug: commvault-client
jsonld:
- class_count: 0
  name: Commvault Context
  property_count: 10
  slug: commvault-context
layout: provider
modified: '2026-05-19'
name: Commvault
nav: Providers
network: true
overview: 'Commvault publishes 24 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Alerts API, Authentication API, and 21 more. Tagged areas include Backup, Cloud Storage, Cyber Recovery, Data Management, and Data Protection.


  The Commvault catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Commvault''s developer surface includes authentication, developer portal, documentation, support, engineering blog, and 13 more developer resources.'
plans:
- name: Commvault Plans Pricing
  plan_count: 12
  slug: commvault-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Commvault Rate Limits
  slug: commvault-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Commvault API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: commvault-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Commvault API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 5
  slug: commvault-rules
score:
  band: developing
  composite: 40.7
  coverage:
    artifact_dirs: 14
    catalog_gap: 54.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 13.6
    contract_quality: 61.8
    developer_ergonomics: 38.1
    discoverability: 74.1
    governance: 13.6
    operational_transparency: 15.8
  previous_composite: 40.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 24
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/commvault/refs/heads/main/screenshots/commvault-2026-06-20T174828.png
security:
- kind: authentication
  name: Commvault Authentication
  slug: commvault-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Commvault Domain Security
  slug: commvault-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: commvault
tags:
- Backup
- Cloud Storage
- Cyber Recovery
- Data Management
- Data Protection
- Disaster Recovery
- Enterprise Software
website: https://cloud.commvault.com/
---
