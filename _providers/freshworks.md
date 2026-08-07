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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 70
  human_in_the_loop: 0
  name: Freshworks Agentic Access
  operation_count: 158
  slug: freshworks-agentic-access
  summary_line: 158 operations · 70 acting
api_count: 44
apis:
- description: 'The Freshmarketer API provides developer access to marketing automation capabilities within the Freshmarketer platform. It enables programmatic management of marketing campaigns, contact lists, email '
  name: Freshworks Freshmarketer API
  slug: freshmarketer-api
- description: The Freshworks App SDK enables developers to build custom applications and extensions that run within the Freshworks product ecosystem. It provides tools for creating apps for Freshdesk, Freshservice,
  name: Freshworks App SDK
  slug: freshworks-app-sdk
- description: Manage company accounts with which you have business relationships.
  name: freshworks Accounts API
  slug: freshworks-accounts-api
- description: Manage chat agents and their availability.
  name: freshworks Agents API
  slug: freshworks-agents-api
- description: Manage job applicants and their application details.
  name: freshworks Applicants API
  slug: freshworks-applicants-api
- description: Manage scheduled appointments and meetings.
  name: freshworks Appointments API
  slug: freshworks-appointments-api
- description: Manage IT assets including hardware, software, and configurations.
  name: freshworks Assets API
  slug: freshworks-assets-api
- description: Manage organizational branch or office locations.
  name: freshworks Branches API
  slug: freshworks-branches-api
- description: Manage business hours configurations.
  name: freshworks Business Hours API
  slug: freshworks-business-hours-api
- description: Access call center metrics and analytics data.
  name: freshworks Call Metrics API
  slug: freshworks-call-metrics-api
- description: Access call records, call details, and call metrics from the Freshcaller system.
  name: freshworks Calls API
  slug: freshworks-calls-api
- description: Manage change requests for controlled modifications to IT infrastructure.
  name: freshworks Changes API
  slug: freshworks-changes-api
- description: Manage messaging channels and their configurations.
  name: freshworks Channels API
  slug: freshworks-channels-api
- description: Manage company records associated with contacts.
  name: freshworks Companies API
  slug: freshworks-companies-api
- description: Manage customer contacts including creation, updates, merging, and deactivation.
  name: freshworks Contacts API
  slug: freshworks-contacts-api
- description: Manage customer conversations and their lifecycle.
  name: freshworks Conversations API
  slug: freshworks-conversations-api
- description: Manage sales deals and their pipeline progression.
  name: freshworks Deals API
  slug: freshworks-deals-api
- description: Manage organizational department records.
  name: freshworks Departments API
  slug: freshworks-departments-api
- description: Manage email configuration settings for the helpdesk.
  name: freshworks Email Configs API
  slug: freshworks-email-configs-api
- description: Manage employee records including personal information, job details, and employment history.
  name: freshworks Employees API
  slug: freshworks-employees-api
- description: Manage agent groups for conversation routing.
  name: freshworks Groups API
  slug: freshworks-groups-api
- description: Manage job postings and their associated applicant fields.
  name: freshworks Job Postings API
  slug: freshworks-job-postings-api
- description: Manage sales leads before they are converted to contacts or accounts.
  name: freshworks Leads API
  slug: freshworks-leads-api
- description: Manage employee levels and designations.
  name: freshworks Levels API
  slug: freshworks-levels-api
- description: Manage office and facility locations.
  name: freshworks Locations API
  slug: freshworks-locations-api
- description: Send and retrieve messages within conversations.
  name: freshworks Messages API
  slug: freshworks-messages-api
- description: Manage notes attached to CRM records.
  name: freshworks Notes API
  slug: freshworks-notes-api
- description: Manage problem records for root cause analysis of recurring incidents.
  name: freshworks Problems API
  slug: freshworks-problems-api
- description: Manage products associated with the helpdesk.
  name: freshworks Products API
  slug: freshworks-products-api
- description: Manage release records for deploying changes to production.
  name: freshworks Releases API
  slug: freshworks-releases-api
- description: Manage requesters who submit tickets to the service desk.
  name: freshworks Requesters API
  slug: freshworks-requesters-api
- description: Manage agent roles and permissions.
  name: freshworks Roles API
  slug: freshworks-roles-api
- description: Track and manage sales activity records.
  name: freshworks Sales Activities API
  slug: freshworks-sales-activities-api
- description: Manage service catalog items available for request.
  name: freshworks Service Catalog API
  slug: freshworks-service-catalog-api
- description: Manage SLA policies for ticket response and resolution targets.
  name: freshworks SLA Policies API
  slug: freshworks-sla-policies-api
- description: Manage sub-departments within departments.
  name: freshworks Sub-Departments API
  slug: freshworks-sub-departments-api
- description: Manage customer satisfaction surveys.
  name: freshworks Surveys API
  slug: freshworks-surveys-api
- description: Manage tasks associated with sales activities.
  name: freshworks Tasks API
  slug: freshworks-tasks-api
- description: Manage agent teams for call routing and organization.
  name: freshworks Teams API
  slug: freshworks-teams-api
- description: Manage helpdesk tickets including creation, updates, assignment, and resolution workflows.
  name: freshworks Tickets API
  slug: freshworks-tickets-api
- description: Track time spent on tickets.
  name: freshworks Time Entries API
  slug: freshworks-time-entries-api
- description: Manage time-off types and employee leave requests.
  name: freshworks Time Off API
  slug: freshworks-time-off-api
- description: Manage agent users in the Freshcaller system including creation, updates, and status management.
  name: freshworks Users API
  slug: freshworks-users-api
- description: Manage vendor records for IT procurement and contracts.
  name: freshworks Vendors API
  slug: freshworks-vendors-api
artifact_total: 154
asyncapis:
- description: Freshworks products support webhook callbacks that notify external applications when specific events occur within the helpdesk, service desk, CRM, and messaging platforms. Webhooks are configured thro
  name: Freshworks Webhook Events
  slug: freshworks-webhooks-asyncapi
collections:
- collection_type: open
  name: Freshworks Freshcaller API
  slug: open-freshworks-freshcaller-api
- collection_type: open
  name: Freshworks Freshchat API
  slug: open-freshworks-freshchat-api
- collection_type: open
  name: Freshworks Freshdesk API
  slug: open-freshworks-freshdesk-api
- collection_type: open
  name: Freshworks Freshsales API
  slug: open-freshworks-freshsales-api
- collection_type: open
  name: Freshworks Freshservice API
  slug: open-freshworks-freshservice-api
- collection_type: open
  name: Freshworks Freshteam API
  slug: open-freshworks-freshteam-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/freshworks-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/freshworks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/freshworks-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/freshworks
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/freshworks-inc
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/freshworks-webhooks-asyncapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/freshworks-ticket-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/freshworks-contact-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/freshworks-context.jsonld
description: Freshworks is a software company that develops cloud-based business software including customer support, IT service management, sales force automation, marketing automation, and HR applications.
features:
- Freshdesk Growth at $19/agent/mo with shared inbox + reports
- Freshdesk Pro at $55/agent/mo with custom objects + Freddy AI
- Freshdesk Enterprise at $89/agent/mo with audit logs + approval workflows
- Freshchat, Freshsales (CRM), Freshservice (ITSM) parallel tiers
- 'Freddy AI Agent: 500 sessions/mo on Pro+'
- Freddy AI Copilot and Insights
- REST API per product (Freshdesk, Freshchat, Freshsales)
- 'Tier-based rate limits: 100 (Growth), 400 (Pro), 700 (Enterprise) req/min'
- OAuth 2.0 + API keys
- Webhooks for ticket, contact, conversation events
- Marketplace for Freshworks apps
- Custom Apps SDK
- Multilingual help desk (40+ languages)
- 5,000 collaborators included on Growth+
- Unified CRM across Sales, Marketing, Support
- Audit logs and skills-based routing on Enterprise
finops:
- name: Freshworks Finops
  service_category: Customer Support / CRM
  slug: freshworks-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/freshworks.png
json_schemas:
- name: Account
  property_count: 17
  slug: freshworks-account
- name: AccountCreate
  property_count: 14
  slug: freshworks-accountcreate
- name: Agent
  property_count: 10
  slug: freshworks-agent
- name: AgentUpdate
  property_count: 4
  slug: freshworks-agentupdate
- name: Applicant
  property_count: 12
  slug: freshworks-applicant
- name: ApplicantCreate
  property_count: 6
  slug: freshworks-applicantcreate
- name: Appointment
  property_count: 11
  slug: freshworks-appointment
- name: AppointmentCreate
  property_count: 7
  slug: freshworks-appointmentcreate
- name: Asset
  property_count: 15
  slug: freshworks-asset
- name: AssetCreate
  property_count: 10
  slug: freshworks-assetcreate
- name: Branch
  property_count: 12
  slug: freshworks-branch
- name: BusinessHours
  property_count: 7
  slug: freshworks-businesshours
- name: Call
  property_count: 18
  slug: freshworks-call
- name: CallMetric
  property_count: 8
  slug: freshworks-callmetric
- name: Change
  property_count: 15
  slug: freshworks-change
- name: ChangeCreate
  property_count: 12
  slug: freshworks-changecreate
- name: Channel
  property_count: 7
  slug: freshworks-channel
- name: Company
  property_count: 12
  slug: freshworks-company
- name: CompanyCreate
  property_count: 9
  slug: freshworks-companycreate
- name: Freshworks Contact
  property_count: 25
  slug: freshworks-contact
- name: ContactCreate
  property_count: 12
  slug: freshworks-contactcreate
- name: Conversation
  property_count: 8
  slug: freshworks-conversation
- name: ConversationCreate
  property_count: 4
  slug: freshworks-conversationcreate
- name: ConversationUpdate
  property_count: 3
  slug: freshworks-conversationupdate
- name: Deal
  property_count: 13
  slug: freshworks-deal
- name: DealCreate
  property_count: 9
  slug: freshworks-dealcreate
- name: Department
  property_count: 9
  slug: freshworks-department
- name: EmailConfig
  property_count: 8
  slug: freshworks-emailconfig
- name: Employee
  property_count: 22
  slug: freshworks-employee
- name: EmployeeUpdate
  property_count: 11
  slug: freshworks-employeeupdate
- name: Error
  property_count: 2
  slug: freshworks-error
- name: Field
  property_count: 7
  slug: freshworks-field
- name: Group
  property_count: 6
  slug: freshworks-group
- name: GroupCreate
  property_count: 6
  slug: freshworks-groupcreate
- name: JobPosting
  property_count: 13
  slug: freshworks-jobposting
- name: Lead
  property_count: 15
  slug: freshworks-lead
- name: LeadCreate
  property_count: 9
  slug: freshworks-leadcreate
- name: Level
  property_count: 4
  slug: freshworks-level
- name: Location
  property_count: 6
  slug: freshworks-location
- name: Message
  property_count: 7
  slug: freshworks-message
- name: MessageCreate
  property_count: 4
  slug: freshworks-messagecreate
- name: Meta
  property_count: 3
  slug: freshworks-meta
- name: Note
  property_count: 6
  slug: freshworks-note
- name: NoteCreate
  property_count: 3
  slug: freshworks-notecreate
- name: PaginationLinks
  property_count: 2
  slug: freshworks-paginationlinks
- name: Problem
  property_count: 13
  slug: freshworks-problem
- name: ProblemCreate
  property_count: 10
  slug: freshworks-problemcreate
- name: Product
  property_count: 5
  slug: freshworks-product
- name: Release
  property_count: 10
  slug: freshworks-release
- name: ReleaseCreate
  property_count: 7
  slug: freshworks-releasecreate
- name: ReplyCreate
  property_count: 3
  slug: freshworks-replycreate
- name: Requester
  property_count: 14
  slug: freshworks-requester
- name: RequesterCreate
  property_count: 9
  slug: freshworks-requestercreate
- name: Role
  property_count: 6
  slug: freshworks-role
- name: SalesActivity
  property_count: 12
  slug: freshworks-salesactivity
- name: SalesActivityCreate
  property_count: 8
  slug: freshworks-salesactivitycreate
- name: SatisfactionRating
  property_count: 9
  slug: freshworks-satisfactionrating
- name: ServiceItem
  property_count: 10
  slug: freshworks-serviceitem
- name: SLAPolicy
  property_count: 7
  slug: freshworks-slapolicy
- name: SubDepartment
  property_count: 5
  slug: freshworks-subdepartment
- name: Task
  property_count: 12
  slug: freshworks-task
- name: TaskCreate
  property_count: 7
  slug: freshworks-taskcreate
- name: Team
  property_count: 6
  slug: freshworks-team
- name: TeamCreate
  property_count: 3
  slug: freshworks-teamcreate
- name: Freshworks Ticket
  property_count: 22
  slug: freshworks-ticket
- name: TicketCreate
  property_count: 17
  slug: freshworks-ticketcreate
- name: TicketUpdate
  property_count: 9
  slug: freshworks-ticketupdate
- name: TimeEntry
  property_count: 10
  slug: freshworks-timeentry
- name: TimeEntryCreate
  property_count: 5
  slug: freshworks-timeentrycreate
- name: TimeOffRequest
  property_count: 9
  slug: freshworks-timeoffrequest
- name: TimeOffRequestCreate
  property_count: 5
  slug: freshworks-timeoffrequestcreate
- name: TimeOffType
  property_count: 4
  slug: freshworks-timeofftype
- name: User
  property_count: 9
  slug: freshworks-user
- name: UserCreate
  property_count: 5
  slug: freshworks-usercreate
- name: UserStatus
  property_count: 5
  slug: freshworks-userstatus
- name: Vendor
  property_count: 9
  slug: freshworks-vendor
- name: VendorCreate
  property_count: 6
  slug: freshworks-vendorcreate
json_structures:
- name: Freshworks Structure
  property_count: 0
  slug: freshworks-structure
jsonld:
- class_count: 0
  name: Freshworks Context
  property_count: 9
  slug: freshworks-context
layout: provider
modified: '2026-05-19'
name: freshworks
nav: Providers
network: true
overview: 'freshworks publishes 42 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Agents API, Applicants API, and 39 more.


  The freshworks catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  freshworks'' developer surface includes authentication and 8 more developer resources.'
plans:
- name: Freshworks Plans Pricing
  plan_count: 3
  slug: freshworks-plans-pricing
random_paper: 85
rate_limits:
- limit_count: 4
  name: Freshworks Rate Limits
  slug: freshworks-rate-limits
rules:
- name: freshworks API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: freshworks-asyncapi-spectral-rules
- name: freshworks API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: freshworks-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 78.3
    developer_ergonomics: 10.9
    discoverability: 50.0
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 42
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/freshworks/refs/heads/main/screenshots/freshworks-2026-06-20T181551.png
security:
- kind: authentication
  name: Freshworks Authentication
  slug: freshworks-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Freshworks Domain Security
  slug: freshworks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: freshworks
---
