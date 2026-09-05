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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.2
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Autodesk Construction Cloud Agentic Access
  operation_count: 13
  slug: autodesk-construction-cloud-agentic-access
  summary_line: 13 operations · 5 acting
api_count: 2
apis:
- description: The ACC Cost Management API provides access to budget codes, contract lifecycle management, and expense tracking in Autodesk Construction Cloud. REST APIs enable ERP integration, change order manageme
  name: Autodesk Construction Cloud Cost Management API
  slug: acc-cost-management-api
- description: The ACC Model Coordination API enables access to model sets, clash detection results, and coordination issues in Autodesk Construction Cloud. REST APIs support automated BIM coordination workflows, cl
  name: Autodesk Construction Cloud Model Coordination API
  slug: acc-model-coordination-api
- description: The ACC RFIs API enables management of Requests for Information (RFIs) in Autodesk Construction Cloud. REST APIs support RFI creation, tracking, response workflows, and reporting for construction proj
  name: Autodesk Construction Cloud RFIs API
  slug: acc-rfis-api
- description: The ACC Submittals API provides programmatic access to submittal workflows in Autodesk Construction Cloud. REST APIs support submittal item creation, review routing, approval tracking, and specificati
  name: Autodesk Construction Cloud Submittals API
  slug: acc-submittals-api
- description: The ACC Data Connector API enables bulk extraction of project data from Autodesk Construction Cloud for analytics and reporting. REST APIs support scheduled and on-demand data exports across issues, R
  name: Autodesk Construction Cloud Data Connector API
  slug: acc-data-connector-api
- baseURL: https://developer.api.autodesk.com
  baseurl_source: declared
  description: Company/business unit management
  name: Autodesk Construction Cloud Companies API
  slug: autodesk-construction-cloud-companies-api
- baseURL: https://developer.api.autodesk.com
  baseurl_source: declared
  description: Construction issue management
  name: Autodesk Construction Cloud Issues API
  slug: autodesk-construction-cloud-issues-api
- baseURL: https://developer.api.autodesk.com
  baseurl_source: declared
  description: Issue type configuration
  name: Autodesk Construction Cloud IssueTypes API
  slug: autodesk-construction-cloud-issuetypes-api
- baseURL: https://developer.api.autodesk.com
  baseurl_source: declared
  description: ACC project management
  name: Autodesk Construction Cloud Projects API
  slug: autodesk-construction-cloud-projects-api
- baseURL: https://developer.api.autodesk.com
  baseurl_source: declared
  description: Project and account user management
  name: Autodesk Construction Cloud Users API
  slug: autodesk-construction-cloud-users-api
artifact_total: 75
asyncapis:
- description: Autodesk Construction Cloud (ACC) and APS Webhooks deliver event notifications for project activities including issue creation, document updates, RFI changes, submittal status changes, and model coord
  name: Autodesk Construction Cloud Webhooks
  slug: acc-webhooks-asyncapi
collections:
- collection_type: postman
  name: Autodesk Construction Cloud Admin Companies API
  slug: postman-autodesk-construction-cloud-companies-api
- collection_type: postman
  name: Autodesk Construction Cloud Admin Companies Issues API
  slug: postman-autodesk-construction-cloud-issues-api
- collection_type: postman
  name: Autodesk Construction Cloud Admin Companies IssueTypes API
  slug: postman-autodesk-construction-cloud-issuetypes-api
- collection_type: postman
  name: Autodesk Construction Cloud Admin Companies Projects API
  slug: postman-autodesk-construction-cloud-projects-api
- collection_type: postman
  name: Autodesk Construction Cloud Admin Companies Users API
  slug: postman-autodesk-construction-cloud-users-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Autodesk Construction Cloud Admin API
  slug: open-acc-admin
- collection_type: open
  name: Autodesk Construction Cloud Issues API
  slug: open-acc-issues
- collection_type: open
  name: Autodesk Construction Cloud Admin Companies API
  slug: open-autodesk-construction-cloud-companies-api
- collection_type: open
  name: Autodesk Construction Cloud Admin Companies Issues API
  slug: open-autodesk-construction-cloud-issues-api
- collection_type: open
  name: Autodesk Construction Cloud Admin Companies IssueTypes API
  slug: open-autodesk-construction-cloud-issuetypes-api
- collection_type: open
  name: Autodesk Construction Cloud Admin Companies Projects API
  slug: open-autodesk-construction-cloud-projects-api
- collection_type: open
  name: Autodesk Construction Cloud Admin Companies Users API
  slug: open-autodesk-construction-cloud-users-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/autodesk-construction-cloud-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/autodesk-construction-cloud/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/autodesk-construction-cloud-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/autodesk-construction-cloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/autodesk-construction-cloud-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/autodesk-construction-cloud-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/autodesk-construction-cloud
- group: company
  title: ''
  type: Website
  url: https://www.autodesk.com
- group: start
  title: ''
  type: Portal
  url: https://aps.autodesk.com/
- group: docs
  title: ''
  type: Documentation
  url: https://aps.autodesk.com/developer/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://aps.autodesk.com/en/docs/acc/v1/tutorials/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://get-started.aps.autodesk.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.autodesk.com/company/legal-notices-trademarks/terms-of-service-autodesk360-web-services/forge-platform-web-services-api-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.autodesk.com/company/legal-notices-trademarks/privacy-statement
- group: operate
  title: ''
  type: StatusPage
  url: https://health.autodesk.com/
- group: operate
  title: ''
  type: Support
  url: https://aps.autodesk.com/contact-support
- group: operate
  title: ''
  type: ChangeLog
  url: https://aps.autodesk.com/topics/platform-updates
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/autodesk-platform-services
- group: docs
  title: ''
  type: AsyncAPI
  url: https://raw.githubusercontent.com/api-evangelist/autodesk-construction-cloud/refs/heads/main/asyncapi/acc-webhooks-asyncapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/autodesk-construction-cloud/refs/heads/main/json-schema/acc-project-schema.json
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/autodesk-construction-cloud/refs/heads/main/json-ld/acc-context.jsonld
created: '2025-01-01'
description: Autodesk Construction Cloud (ACC) is a unified platform connecting workflows, teams, and data across the construction project lifecycle, integrating preconstruction, design collaboration, project management, and field execution tools. ACC provides REST APIs through the Autodesk Platform Services (APS) for programmatic access to project management, issues, RFIs, submittals, cost management, model coordination, and data export capabilities.
examples:
- key_count: 22
  name: Acc Issue Example
  slug: acc-issue-example
- key_count: 23
  name: Acc Project Example
  slug: acc-project-example
features:
- description: Programmatic management of ACC accounts, projects, users, and company settings with automation of project provisioning and user access control.
  name: Project Administration
- description: Creation, tracking, and management of construction issues, observations, punch lists, and quality control items through REST APIs.
  name: Issues and Field Management
- description: Budget tracking, contract lifecycle management, change order processing, and financial reporting for construction project portfolios.
  name: Cost Management
- description: Automated BIM coordination with clash detection, model set management, and coordination issue tracking across design disciplines.
  name: Model Coordination
- description: End-to-end management of Requests for Information and submittal review workflows with approval tracking and compliance reporting.
  name: RFI and Submittal Management
- description: Bulk extraction of project data for analytics and business intelligence, supporting scheduled and on-demand exports across all ACC modules.
  name: Data Connector
- description: Event-driven notifications via webhooks for real-time integration with external systems when project data changes in ACC.
  name: Webhooks
finops:
- name: Autodesk Construction Cloud Finops
  service_category: Construction Software / Project Management
  slug: autodesk-construction-cloud-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Autodesk Construction Cloud (ACC) platform, derived from the Autodesk Platform Services (APS) REST APIs. It is intended to illustrate the do
  name: Autodesk Construction Cloud GraphQL Schema
  slug: autodesk-construction-cloud-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/autodesk-construction-cloud.png
integrations:
- description: Full integration with the Autodesk Platform Services (APS) ecosystem including Data Management, Model Derivative, and Authentication APIs.
  name: Autodesk Platform Services
- description: Integration possibilities with Procore construction management platform for cross-platform project data synchronization.
  name: Procore
- description: Schedule data integration with Oracle Primavera P6 for project schedule management and reporting across enterprise construction portfolios.
  name: Primavera P6
- description: Enterprise ERP integration with SAP for financial data synchronization, purchase order management, and project accounting workflows.
  name: SAP
json_schemas:
- name: Autodesk Construction Cloud Issue
  property_count: 23
  slug: acc-issue
- name: Autodesk Construction Cloud Project
  property_count: 24
  slug: acc-project
- name: AccountUsersResponse
  property_count: 2
  slug: autodesk-construction-cloud-accountusersresponse
- name: CompaniesResponse
  property_count: 2
  slug: autodesk-construction-cloud-companiesresponse
- name: Error
  property_count: 3
  slug: autodesk-construction-cloud-error
- name: Issue
  property_count: 23
  slug: autodesk-construction-cloud-issue
- name: IssueRequest
  property_count: 9
  slug: autodesk-construction-cloud-issuerequest
- name: IssuesResponse
  property_count: 2
  slug: autodesk-construction-cloud-issuesresponse
- name: IssueType
  property_count: 5
  slug: autodesk-construction-cloud-issuetype
- name: IssueUpdateRequest
  property_count: 6
  slug: autodesk-construction-cloud-issueupdaterequest
- name: Pagination
  property_count: 4
  slug: autodesk-construction-cloud-pagination
- name: Project
  property_count: 24
  slug: autodesk-construction-cloud-project
- name: ProjectRequest
  property_count: 11
  slug: autodesk-construction-cloud-projectrequest
- name: ProjectResponse
  property_count: 1
  slug: autodesk-construction-cloud-projectresponse
- name: ProjectsResponse
  property_count: 2
  slug: autodesk-construction-cloud-projectsresponse
- name: ProjectUpdateRequest
  property_count: 4
  slug: autodesk-construction-cloud-projectupdaterequest
- name: ProjectUser
  property_count: 10
  slug: autodesk-construction-cloud-projectuser
- name: ProjectUserRequest
  property_count: 3
  slug: autodesk-construction-cloud-projectuserrequest
- name: ProjectUsersResponse
  property_count: 2
  slug: autodesk-construction-cloud-projectusersresponse
json_structures:
- name: Acc Issue Structure
  property_count: 21
  slug: acc-issue-structure
- name: Acc Project Structure
  property_count: 23
  slug: acc-project-structure
- name: Autodesk Construction Cloud Structure
  property_count: 0
  slug: autodesk-construction-cloud-structure
jsonld:
- class_count: 0
  name: Acc Context
  property_count: 3
  slug: acc-context
layout: provider
modified: '2026-05-19'
name: Autodesk Construction Cloud
nav: Providers
network: true
overview: 'Autodesk Construction Cloud publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Companies API, Issues API, IssueTypes API, and 2 more. Tagged areas include Construction, BIM, Project Management, AEC, and CAD.


  The Autodesk Construction Cloud catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Autodesk Construction Cloud''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, changelog, and 15 more developer resources.'
plans:
- name: Autodesk Construction Cloud Plans Pricing
  plan_count: 3
  slug: autodesk-construction-cloud-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 3
  name: Autodesk Construction Cloud Rate Limits
  slug: autodesk-construction-cloud-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Autodesk Construction Cloud API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: autodesk-construction-cloud-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Autodesk Construction Cloud API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: autodesk-construction-cloud-jsonschema-spectral-rules
scopes:
- name: Autodesk Construction Cloud Scopes
  scope_count: 4
  slug: autodesk-construction-cloud-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 51.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 61.5
    catalog_earned_first_party: 0.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 13.6
    contract_quality: 77.6
    developer_ergonomics: 51.2
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 42.1
  previous_composite: 51.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/autodesk-construction-cloud/refs/heads/main/screenshots/autodesk-construction-cloud-2026-06-20T172629.png
security:
- kind: authentication
  name: Autodesk Construction Cloud Authentication
  slug: autodesk-construction-cloud-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Autodesk Construction Cloud Domain Security
  slug: autodesk-construction-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: autodesk-construction-cloud
tags:
- Construction
- BIM
- Project Management
- AEC
- CAD
- Architecture
- Engineering
- Field Management
use_cases:
- description: Connecting ACC cost management and project data with enterprise ERP systems for unified financial reporting and project accounting.
  name: ERP Integration
- description: Automating BIM coordination workflows including clash detection review, model set updates, and coordination issue resolution across teams.
  name: BIM Workflow Automation
- description: Building custom dashboards and reports using the Data Connector API to aggregate project data across issues, RFIs, submittals, and costs.
  name: Construction Project Reporting
- description: Integrating ACC issues and punch list management with mobile field apps, IoT sensors, and safety management platforms.
  name: Field Management Integration
- description: Automating RFI and submittal routing, review reminders, and approval tracking to reduce administrative burden on project document control teams.
  name: Document Control Automation
website: https://www.autodesk.com
---
