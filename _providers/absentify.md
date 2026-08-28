---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.5
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Absentify Agentic Access
  operation_count: 40
  slug: absentify-agentic-access
  summary_line: 40 operations · 23 acting
api_count: 7
apis:
- description: The Absences API from Absentify — 1 operation(s) for absences.
  name: Absentify Absences API
  slug: absentify-absences-api
- description: The Departments API from Absentify — 2 operation(s) for departments.
  name: Absentify Departments API
  slug: absentify-departments-api
- description: The Leave types API from Absentify — 3 operation(s) for leave types.
  name: Absentify Leave types API
  slug: absentify-leave-types-api
- description: The Members API from Absentify — 10 operation(s) for members.
  name: Absentify Members API
  slug: absentify-members-api
- description: The Public holidays API from Absentify — 2 operation(s) for public holidays.
  name: Absentify Public holidays API
  slug: absentify-public-holidays-api
- description: The Requests API from Absentify — 9 operation(s) for requests.
  name: Absentify Requests API
  slug: absentify-requests-api
- description: The Workspace API from Absentify — 1 operation(s) for workspace.
  name: Absentify Workspace API
  slug: absentify-workspace-api
artifact_total: 76
collections:
- collection_type: postman
  name: Absentify Absences API
  slug: postman-absentify-absences-api
- collection_type: postman
  name: Absentify Absences Departments API
  slug: postman-absentify-departments-api
- collection_type: postman
  name: Absentify Absences Leave types API
  slug: postman-absentify-leave-types-api
- collection_type: postman
  name: Absentify Absences Members API
  slug: postman-absentify-members-api
- collection_type: postman
  name: Absentify Absences Public holidays API
  slug: postman-absentify-public-holidays-api
- collection_type: postman
  name: Absentify Absences Requests API
  slug: postman-absentify-requests-api
- collection_type: postman
  name: Absentify Absences Workspace API
  slug: postman-absentify-workspace-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Absentify Absences API
  slug: open-absentify-absences-api
- collection_type: open
  name: Absentify Absences Departments API
  slug: open-absentify-departments-api
- collection_type: open
  name: Absentify Absences Leave types API
  slug: open-absentify-leave-types-api
- collection_type: open
  name: Absentify Absences Members API
  slug: open-absentify-members-api
- collection_type: open
  name: Absentify Absences Public holidays API
  slug: open-absentify-public-holidays-api
- collection_type: open
  name: Absentify Absences Requests API
  slug: open-absentify-requests-api
- collection_type: open
  name: Absentify Absences Workspace API
  slug: open-absentify-workspace-api
- collection_type: open
  name: Absentify API
  slug: open-absentify
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/absentify/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/absentify-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/absentify-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/absentify-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/absentify-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/absentify-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/absentify
- group: start
  title: ''
  type: Portal
  url: https://absentify.com/
- group: docs
  title: ''
  type: Documentation
  url: https://absentify.com/docs/en/
- group: commercial
  title: ''
  type: Pricing
  url: https://absentify.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://absentify.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://absentify.com/terms-and-conditions
- group: company
  title: ''
  type: Blog
  url: https://absentify.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.absentify.com
- group: auth
  title: ''
  type: Security
  url: https://absentify.com/security
- group: build
  title: MCP Server
  type: Tools
  url: https://absentify.com/docs/en/mcp-server
- group: design
  title: ''
  type: SpectralRules
  url: rules/absentify-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/absentify-vocabulary.yaml
created: '2025-02-17'
description: Absentify is an absence management platform integrated with Microsoft 365 and Microsoft Teams that helps businesses track and manage employee absences, leave requests, approvals, and team schedules. Built by BrainCore Solutions GmbH, it provides a REST API for integrating absence management into custom workflows, HR systems, and business automation tools.
examples:
- key_count: 7
  name: Absentify Absence Example
  slug: absentify-absence-example
- key_count: 6
  name: Absentify Department Example
  slug: absentify-department-example
- key_count: 12
  name: Absentify Leave Type Example
  slug: absentify-leave-type-example
- key_count: 13
  name: Absentify Member Example
  slug: absentify-member-example
- key_count: 6
  name: Absentify Public Holiday Calendar Example
  slug: absentify-public-holiday-calendar-example
- key_count: 14
  name: Absentify Request Example
  slug: absentify-request-example
- key_count: 8
  name: Absentify Workspace Example
  slug: absentify-workspace-example
features:
- description: Track and manage employee absences, time off, and leave requests across the organization.
  name: Absence Tracking
- description: Submit, approve, decline, and cancel leave requests with multi-level approval workflows.
  name: Leave Request Management
- description: Native integration with Microsoft 365 and Microsoft Teams for seamless absence management in existing workflows.
  name: Microsoft 365 Integration
- description: Organize employees into departments with custom leave type entitlements and approval chains.
  name: Department Management
- description: Define custom leave types with color coding, limits, approval requirements, and accrual policies.
  name: Leave Type Configuration
- description: Manage public holiday calendars per region and apply them to members and departments.
  name: Public Holiday Calendars
- description: Receive real-time webhook notifications for request creation and status changes.
  name: Webhook Support
- description: Configure workspace-wide settings, fiscal year, and default approval workflows.
  name: Workspace Management
- description: Query absences broken down by individual day for reporting and payroll integration.
  name: Absence Per Day Reporting
finops:
- name: Absentify Finops
  service_category: API
  slug: absentify-finops
image: /assets/icons/absentify.png
integrations:
- description: Native Microsoft Teams app for submitting and approving absence requests without leaving Teams.
  name: Microsoft Teams
- description: Deep integration with Microsoft 365 calendar, Active Directory, and identity management.
  name: Microsoft 365
- description: Connect absentify to thousands of apps via Zapier automation workflows.
  name: Zapier
- description: Automate absence management workflows using Make's visual automation platform.
  name: Make (Integromat)
- description: Send real-time absence event notifications to any system via configurable webhooks.
  name: Custom Webhooks
json_schemas:
- name: Absence
  property_count: 4
  slug: absentify-absence
- name: Department
  property_count: 4
  slug: absentify-department
- name: LeaveType
  property_count: 7
  slug: absentify-leave-type
- name: Member
  property_count: 12
  slug: absentify-member
- name: PublicHolidayCalendar
  property_count: 5
  slug: absentify-public-holiday-calendar
- name: Request
  property_count: 10
  slug: absentify-request
- name: Workspace
  property_count: 4
  slug: absentify-workspace
json_structures:
- name: Absentify Absence Structure
  property_count: 0
  slug: absentify-absence-structure
- name: Absentify Department Structure
  property_count: 0
  slug: absentify-department-structure
- name: Absentify Leave Type Structure
  property_count: 0
  slug: absentify-leave-type-structure
- name: Absentify Member Structure
  property_count: 0
  slug: absentify-member-structure
- name: Absentify Public Holiday Calendar Structure
  property_count: 0
  slug: absentify-public-holiday-calendar-structure
- name: Absentify Request Structure
  property_count: 0
  slug: absentify-request-structure
- name: Absentify Workspace Structure
  property_count: 0
  slug: absentify-workspace-structure
jsonld:
- class_count: 9
  name: Absentify Context
  property_count: 36
  slug: absentify-context
layout: provider
modified: '2026-05-19'
name: Absentify
nav: Providers
network: true
overview: 'Absentify publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Absences API, Departments API, Leave types API, and 4 more. Tagged areas include Absence Management, HR, Leave Management, Microsoft Teams, and Human Resources.


  The Absentify catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Absentify''s developer surface includes authentication, developer portal, documentation, pricing, engineering blog, tooling, and 12 more developer resources.'
plans:
- name: Absentify Plans Pricing
  plan_count: 3
  slug: absentify-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Absentify Rate Limits
  slug: absentify-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Absentify API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: absentify-jsonschema-spectral-rules
- effective_rule_count: 69
  extends:
  - spectral:oas
  name: Absentify API Rules
  rule_count: 28
  severity_counts:
    error: 5
    hint: 0
    info: 4
    warn: 19
  slug: absentify-spectral-rules
score:
  band: developing
  composite: 52.0
  delta: 0.8
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 28.8
    contract_quality: 80.3
    developer_ergonomics: 38.1
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 18.4
  previous_composite: 51.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/absentify/refs/heads/main/screenshots/absentify-2026-06-20T163354.png
security:
- kind: authentication
  name: Absentify Authentication
  slug: absentify-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Absentify Domain Security
  slug: absentify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Absentify Vulnerability Disclosure
  slug: absentify-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Absentify Trust Center
  slug: absentify-trust-center
  summary_line: ISO 27001, GDPR
slug: absentify
tags:
- Absence Management
- HR
- Leave Management
- Microsoft Teams
- Human Resources
use_cases:
- description: Integrate absence data into HRIS platforms like SAP, Workday, or BambooHR for unified people management.
  name: HR System Integration
- description: Export absence data to payroll systems to automatically calculate pay adjustments for time off.
  name: Payroll Processing
- description: Sync absence data into scheduling tools to prevent understaffing and manage coverage.
  name: Team Scheduling
- description: Generate absence reports for regulatory compliance, labor law adherence, and audit purposes.
  name: Compliance Reporting
- description: Build custom absence request approval workflows integrated with business process automation tools.
  name: Custom Approval Workflows
- description: Analyze absence trends, patterns, and costs to improve workforce planning and reduce absenteeism.
  name: Absence Analytics
- description: Automate absence-related notifications and approvals directly within Microsoft Teams channels.
  name: Microsoft Teams Automation
website: https://absentify.com/
---
