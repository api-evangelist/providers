---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Google Workspace Agentic Access
  operation_count: 21
  slug: google-workspace-agentic-access
  summary_line: 21 operations · 15 acting
api_count: 1
apis:
- description: Send and read email, manage drafts and labels, and handle mailbox settings.
  name: Gmail API
  slug: gmail
- description: Store and synchronize files across devices, manage file metadata and permissions.
  name: Google Drive API
  slug: drive
- description: Create and manage calendars, events, and attendees.
  name: Google Calendar API
  slug: calendar
- description: Create and manage video conferencing meetings, spaces, recordings, and transcripts.
  name: Google Meet REST API
  slug: meet
- description: Create and edit documents programmatically.
  name: Google Docs API
  slug: docs
- description: Read and write data in Google Sheets.
  name: Google Sheets API
  slug: sheets
- description: Create and modify presentations.
  name: Google Slides API
  slug: slides
- description: Build bots and integrations for Google Chat.
  name: Google Chat API
  slug: chat
- description: View audit and usage reports for a Google Workspace domain including user activity and admin actions.
  name: Admin SDK Reports API
  slug: admin-reports
- description: Create and modify forms and quizzes, retrieve form responses and quiz grades.
  name: Google Forms API
  slug: forms
- description: Search, read, and update Google Tasks content and metadata.
  name: Google Tasks API
  slug: tasks
- description: Manage Google Keep notes including creating, listing, and deleting notes and managing permissions.
  name: Google Keep API
  slug: keep
- description: Manage eDiscovery for your organization including matters, holds, and exports across Google Workspace services.
  name: Google Vault API
  slug: vault
- description: Manage classes, rosters, invitations, and coursework in Google Classroom.
  name: Google Classroom API
  slug: classroom
- description: Read and manage the authenticated user contacts and profiles, and search the directory.
  name: People API
  slug: people
- description: Index non-Google Workspace data and search across all organizational data sources.
  name: Google Cloud Search API
  slug: cloud-search
- description: Retrieve information about changes made to objects within a user Google Drive.
  name: Drive Activity API
  slug: drive-activity
- description: Create and manage labels to organize and classify files in Google Drive.
  name: Drive Labels API
  slug: drive-labels
- description: Manage alerts on issues affecting your Google Workspace domain including security and compliance warnings.
  name: Alert Center API
  slug: alert-center
- description: Update and retrieve settings for existing Google Groups including permissions and access controls.
  name: Groups Settings API
  slug: groups-settings
- description: Migrate shared emails from public folders and distribution lists to Google Groups discussion archives.
  name: Groups Migration API
  slug: groups-migration
- description: Transfer ownership of user data from one user to another within a domain.
  name: Admin SDK Data Transfer API
  slug: data-transfer
- description: Manage Google Workspace and related product licenses for all users of a customer.
  name: Enterprise License Manager API
  slug: license-manager
- description: Perform common reseller functions at scale including placing orders and managing customer subscriptions.
  name: Google Workspace Reseller API
  slug: reseller
- description: Gather statistics on bulk emails sent to Gmail users including spam reports and delivery errors.
  name: Gmail Postmaster Tools API
  slug: postmaster
- description: Manage customer and user license status for Google Workspace Marketplace applications.
  name: Google Workspace Marketplace API
  slug: marketplace
- baseURL: https://gmail.googleapis.com
  baseurl_source: declared
  description: Manage groups in a Google Workspace domain
  name: Google Workspace Groups API
  slug: google-workspace-groups-api
- baseURL: https://gmail.googleapis.com
  baseurl_source: declared
  description: Manage user accounts in a Google Workspace domain
  name: Google Workspace Users API
  slug: google-workspace-users-api
- description: The Google Meet API allows developers to build applications that integrate with Google Meet.
  name: Google Meet API
  slug: google-meet-api
- baseURL: https://gmail.googleapis.com
  baseurl_source: declared
  description: The Calendar API from Google Workspace APIs — 3 operation(s) for calendar.
  name: Google Workspace APIs Calendar API
  slug: google-suites-calendar-api
- baseURL: https://gmail.googleapis.com
  baseurl_source: declared
  description: The Drive API from Google Workspace APIs — 2 operation(s) for drive.
  name: Google Workspace APIs Drive API
  slug: google-suites-drive-api
- baseURL: https://gmail.googleapis.com
  baseurl_source: declared
  description: The Gmail API from Google Workspace APIs — 4 operation(s) for gmail.
  name: Google Workspace APIs Gmail API
  slug: google-suites-gmail-api
- baseURL: https://admin.googleapis.com
  baseurl_source: declared
  description: Manage organizational units in a Google Workspace domain
  name: Google Workspace Org Units API
  slug: google-workspace-org-units-api
arazzos:
- description: Confirm a user exists, then list every group the user belongs to.
  name: Google Workspace Audit a User's Group Memberships
  slug: google-workspace-audit-user-groups-workflow
- description: Create a group with an email and description, then read it back.
  name: Google Workspace Create a Group
  slug: google-workspace-create-group-workflow
- description: Create an organizational unit, then move a user into it and confirm.
  name: Google Workspace Create an Org Unit and Assign a User
  slug: google-workspace-create-org-unit-and-assign-user-workflow
- description: Move a user out of an org unit, then delete the now-empty unit.
  name: Google Workspace Decommission an Org Unit
  slug: google-workspace-decommission-org-unit-workflow
- description: Look up a user, confirm it exists, then delete the account.
  name: Google Workspace Delete a User Safely
  slug: google-workspace-delete-user-safely-workflow
- description: Search groups by query, branch on a match, then delete the group.
  name: Google Workspace Find and Delete a Group
  slug: google-workspace-find-and-delete-group-workflow
- description: Search users by query, branch on whether a match was found, then patch it.
  name: Google Workspace Find and Update a User
  slug: google-workspace-find-and-update-user-workflow
- description: List all child org units under a path, then read the first one in detail.
  name: Google Workspace Inspect the Org Unit Tree
  slug: google-workspace-inspect-org-unit-tree-workflow
- description: Verify the target org unit exists, then move a user into it and confirm.
  name: Google Workspace Move a User to Another Org Unit
  slug: google-workspace-move-user-org-unit-workflow
- description: Suspend a departing user, sign them out of all sessions, and confirm the state.
  name: Google Workspace Offboard a User
  slug: google-workspace-offboard-user-workflow
- description: Confirm a user exists, grant super admin, then verify the admin flag.
  name: Google Workspace Promote a User to Super Administrator
  slug: google-workspace-promote-user-to-admin-workflow
- description: Create a new user account, place it in an organizational unit, and read it back.
  name: Google Workspace Provision a User
  slug: google-workspace-provision-user-workflow
- description: Read a group, patch its name and description, then confirm the change.
  name: Google Workspace Rename a Group
  slug: google-workspace-rename-group-workflow
- description: Read an org unit, patch its name and description, then confirm.
  name: Google Workspace Rename an Org Unit
  slug: google-workspace-rename-org-unit-workflow
- description: Confirm a user, set a new password forcing change at next login, sign them out.
  name: Google Workspace Reset a User Password
  slug: google-workspace-reset-user-password-workflow
- description: Find a recently deleted user, undelete it into an org unit, and confirm.
  name: Google Workspace Restore a Deleted User
  slug: google-workspace-restore-deleted-user-workflow
artifact_total: 127
collections:
- collection_type: postman
  name: Google Workspace Admin SDK Directory API
  slug: postman-admin-sdk-directory-api
- collection_type: open
  name: Google Workspace Admin SDK Directory API
  slug: open-admin-sdk-directory-api
- collection_type: open
  name: Google Workspace Admin SDK Directory Groups API
  slug: open-google-workspace-groups-api
- collection_type: open
  name: Google Workspace Admin SDK Directory Groups OrgUnits API
  slug: open-google-workspace-orgunits-api
- collection_type: open
  name: Google Workspace Admin SDK Directory Groups Users API
  slug: open-google-workspace-users-api
common:
- group: design
  href: https://artifacts.apis.io/google-workspace/rules/google-workspace-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/google-workspace-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/google-workspace/rules/google-workspace-rules.yml
  title: ''
  type: Spectral
  url: rules/google-workspace-rules.yml
- group: design
  href: https://artifacts.apis.io/google-workspace/rules/google-workspace-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/google-workspace-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/google-workspace/json-ld/admin-sdk-directory-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/admin-sdk-directory-context.jsonld
- group: design
  href: https://artifacts.apis.io/google-workspace/vocabulary/google-workspace-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/google-workspace-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/google-workspace/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/google-workspace/data-model/google-workspace-data-model.yml
  title: ''
  type: DataModel
  url: data-model/google-workspace-data-model.yml
- group: build
  href: https://artifacts.apis.io/google-workspace/cli/google-workspace-cli.yml
  title: ''
  type: CLI
  url: cli/google-workspace-cli.yml
- group: design
  href: https://artifacts.apis.io/google-workspace/conventions/google-workspace-conventions.yml
  title: ''
  type: Conventions
  url: conventions/google-workspace-conventions.yml
- group: design
  href: https://artifacts.apis.io/google-workspace/lifecycle/google-workspace-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/google-workspace-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/google-workspace/errors/google-workspace-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/google-workspace-error-codes.yml
- group: design
  href: https://artifacts.apis.io/google-workspace/errors/google-workspace-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/google-workspace-problem-types.yml
- group: design
  href: https://artifacts.apis.io/google-workspace/conformance/google-workspace-conformance.yml
  title: ''
  type: Conformance
  url: conformance/google-workspace-conformance.yml
- group: agent
  href: https://artifacts.apis.io/google-workspace/llms/google-workspace-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/google-workspace-llms.txt
- group: build
  href: https://artifacts.apis.io/google-workspace/mcp/google-workspace-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/google-workspace-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/google-workspace/mcp/google-workspace-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/google-workspace-mcp.yml
- group: agent
  href: https://artifacts.apis.io/google-workspace/well-known/google-workspace-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/google-workspace-well-known.yml
- group: other
  href: https://artifacts.apis.io/google-workspace/hosts/google-workspace-hosts.yml
  title: ''
  type: Hosts
  url: hosts/google-workspace-hosts.yml
- group: build
  href: https://artifacts.apis.io/google-workspace/integrations/google-workspace-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/google-workspace-integration-edges.yml
- group: build
  href: https://artifacts.apis.io/google-workspace/packages/google-workspace-packages.yml
  title: ''
  type: SDKs
  url: packages/google-workspace-packages.yml
- group: build
  href: https://artifacts.apis.io/google-workspace/packages/google-workspace-packages.yml
  title: ''
  type: Packages
  url: packages/google-workspace-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://workspace.google.com/security/
- group: company
  title: ''
  type: Newsroom
  url: https://cloud.google.com/press/
- group: start
  title: ''
  type: Login
  url: https://accounts.google.com/v3/signin/identifier?continue=https://docs.google.com/&emr=1&followup=https://docs.google.com/&osid=1&passive=1209600&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1862456855:1793821621910294
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/
- group: commercial
  href: https://artifacts.apis.io/google-workspace/finops/google-workspace-finops.yml
  title: ''
  type: FinOps
  url: finops/google-workspace-finops.yml
- group: operate
  href: https://artifacts.apis.io/google-workspace/rate-limits/google-workspace-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-workspace-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/google-workspace/plans/google-workspace-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-workspace-plans-pricing.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: company
  title: ''
  type: Website
  url: https://workspace.google.com/
- group: other
  href: https://artifacts.apis.io/google-workspace/capabilities/google-workspace-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/google-workspace-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/google-workspace/agentic-access/google-workspace-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-workspace-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/google-workspace/security/google-workspace-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-workspace-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-workspace/security/google-workspace-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-workspace-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/google-workspace/authentication/google-workspace-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-workspace-authentication.yml
- group: auth
  href: https://artifacts.apis.io/google-workspace/scopes/google-workspace-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/google-workspace-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-workspace/overview
- group: design
  href: https://artifacts.apis.io/google-workspace/arazzo/google-workspace-audit-user-groups-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-audit-user-groups-workflow.yml
- group: design
  href: https://artifacts.apis.io/google-workspace/arazzo/google-workspace-create-group-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-create-group-workflow.yml
- group: design
  href: https://artifacts.apis.io/google-workspace/arazzo/google-workspace-create-org-unit-and-assign-user-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-create-org-unit-and-assign-user-workflow.yml
- group: design
  href: https://artifacts.apis.io/google-workspace/arazzo/google-workspace-decommission-org-unit-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-decommission-org-unit-workflow.yml
- group: design
  href: https://artifacts.apis.io/google-workspace/arazzo/google-workspace-delete-user-safely-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-delete-user-safely-workflow.yml
- group: design
  href: https://artifacts.apis.io/google-workspace/arazzo/google-workspace-find-and-delete-group-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-find-and-delete-group-workflow.yml
- group: design
  href: https://artifacts.apis.io/google-workspace/arazzo/google-workspace-find-and-update-user-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-find-and-update-user-workflow.yml
- group: design
  href: https://artifacts.apis.io/google-workspace/arazzo/google-workspace-inspect-org-unit-tree-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-inspect-org-unit-tree-workflow.yml
- group: design
  href: https://artifacts.apis.io/google-workspace/arazzo/google-workspace-move-user-org-unit-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-move-user-org-unit-workflow.yml
- group: design
  href: https://artifacts.apis.io/google-workspace/arazzo/google-workspace-offboard-user-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-offboard-user-workflow.yml
- group: design
  href: https://artifacts.apis.io/google-workspace/arazzo/google-workspace-promote-user-to-admin-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-promote-user-to-admin-workflow.yml
- group: design
  href: https://artifacts.apis.io/google-workspace/arazzo/google-workspace-provision-user-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-provision-user-workflow.yml
- group: design
  href: https://artifacts.apis.io/google-workspace/arazzo/google-workspace-rename-group-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-rename-group-workflow.yml
- group: design
  href: https://artifacts.apis.io/google-workspace/arazzo/google-workspace-rename-org-unit-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-rename-org-unit-workflow.yml
- group: design
  href: https://artifacts.apis.io/google-workspace/arazzo/google-workspace-reset-user-password-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-reset-user-password-workflow.yml
- group: design
  href: https://artifacts.apis.io/google-workspace/arazzo/google-workspace-restore-deleted-user-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-restore-deleted-user-workflow.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleworkspace
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/googleworkspace
- group: start
  title: ''
  type: Console
  url: https://console.cloud.google.com
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/identity/protocols/oauth2
- group: commercial
  title: ''
  type: TermsOfService
  url: https://workspace.google.com/terms/service-terms/
- group: operate
  title: ''
  type: Support
  url: https://support.google.com/workspace
- group: operate
  title: ''
  type: StatusPage
  url: https://www.google.com/appsstatus/dashboard/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.google.com/workspace
- group: commercial
  title: ''
  type: Pricing
  url: https://workspace.google.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://workspaceupdates.googleblog.com
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developers.google.com/workspace/release-notes
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/workspace/guides/get-started
created: '2024-01-01'
description: A collection of productivity and collaboration tools from Google including Gmail, Drive, Calendar, Meet, and more.
examples:
- key_count: 1
  name: Admin Sdk Directory Error Example
  slug: admin-sdk-directory-error-example
- key_count: 10
  name: Admin Sdk Directory Group Example
  slug: admin-sdk-directory-group-example
- key_count: 4
  name: Admin Sdk Directory Groups Example
  slug: admin-sdk-directory-groups-example
- key_count: 9
  name: Admin Sdk Directory Org Unit Example
  slug: admin-sdk-directory-org-unit-example
- key_count: 3
  name: Admin Sdk Directory Org Units Example
  slug: admin-sdk-directory-org-units-example
- key_count: 41
  name: Admin Sdk Directory User Example
  slug: admin-sdk-directory-user-example
- key_count: 4
  name: Admin Sdk Directory User Name Example
  slug: admin-sdk-directory-user-name-example
- key_count: 5
  name: Admin Sdk Directory Users Example
  slug: admin-sdk-directory-users-example
features:
- description: Send, receive, and manage email with Gmail API, build chat bots with Chat API, and host video meetings with Meet API.
  name: Email and Communication
- description: Create and edit documents, spreadsheets, presentations, and forms programmatically across Google Workspace apps.
  name: Document Collaboration
- description: Store, sync, and manage files with Drive API including permissions, metadata, labels, and activity tracking.
  name: File Storage and Management
- description: Manage users, groups, organizational units, and devices across a Google Workspace domain with Admin SDK.
  name: Directory and User Management
- description: Create and manage calendars, events, and attendees with automatic conflict detection and resource booking.
  name: Calendar and Scheduling
- description: Monitor security alerts, manage eDiscovery holds, and generate audit reports for compliance requirements.
  name: Security and Compliance
- description: Index and search across Google Workspace and external data sources with Cloud Search API.
  name: Enterprise Search
- description: Manage tasks and notes programmatically with Tasks API and Keep API for productivity workflows.
  name: Task and Note Management
finops:
- has_sources: true
  method: derived
  name: Google Workspace Finops
  primary_unit: user
  service_category: ''
  slug: google-workspace-finops
  template: false
image: https://workspace.google.com/static/img/logo.svg
integrations:
- description: Sync contacts, calendar events, and emails between Google Workspace and Salesforce CRM.
  name: Salesforce
- description: Bridge Google Workspace content and notifications with Slack channels for unified collaboration.
  name: Slack
- description: Interoperability support for document sharing and calendar synchronization with Microsoft Office apps.
  name: Microsoft 365
- description: Link Google Drive files, create documents from Jira issues, and sync calendar events with project timelines.
  name: Jira
- description: Connect Google Workspace apps with thousands of services through Zapier automation workflows.
  name: Zapier
- description: Integrate Google Drive attachments, Calendar events, and Gmail notifications with Asana project management.
  name: Asana
json_schemas:
- name: Error
  property_count: 1
  slug: admin-sdk-directory-error
- name: Group
  property_count: 10
  slug: admin-sdk-directory-group
- name: Groups
  property_count: 4
  slug: admin-sdk-directory-groups
- name: OrgUnit
  property_count: 9
  slug: admin-sdk-directory-org-unit
- name: OrgUnits
  property_count: 3
  slug: admin-sdk-directory-org-units
- name: UserName
  property_count: 4
  slug: admin-sdk-directory-user-name
- name: User
  property_count: 41
  slug: admin-sdk-directory-user
- name: Users
  property_count: 5
  slug: admin-sdk-directory-users
- name: Error
  property_count: 1
  slug: google-workspace-error
- name: Event
  property_count: 8
  slug: google-workspace-event
- name: File
  property_count: 6
  slug: google-workspace-file
- name: Group
  property_count: 10
  slug: google-workspace-group
- name: Groups
  property_count: 4
  slug: google-workspace-groups
- name: Message
  property_count: 4
  slug: google-workspace-message
- name: OrgUnit
  property_count: 9
  slug: google-workspace-orgunit
- name: OrgUnits
  property_count: 3
  slug: google-workspace-orgunits
- name: Google Workspace Admin SDK Directory API Models
  property_count: 0
  slug: google-workspace-user
- name: UserName
  property_count: 4
  slug: google-workspace-username
- name: Users
  property_count: 5
  slug: google-workspace-users
json_structures:
- name: Admin Sdk Directory Error Structure
  property_count: 1
  slug: admin-sdk-directory-error-structure
- name: Admin Sdk Directory Group Structure
  property_count: 10
  slug: admin-sdk-directory-group-structure
- name: Admin Sdk Directory Groups Structure
  property_count: 4
  slug: admin-sdk-directory-groups-structure
- name: Admin Sdk Directory Org Unit Structure
  property_count: 9
  slug: admin-sdk-directory-org-unit-structure
- name: Admin Sdk Directory Org Units Structure
  property_count: 3
  slug: admin-sdk-directory-org-units-structure
- name: Admin Sdk Directory User Name Structure
  property_count: 4
  slug: admin-sdk-directory-user-name-structure
- name: Admin Sdk Directory User Structure
  property_count: 41
  slug: admin-sdk-directory-user-structure
- name: Admin Sdk Directory Users Structure
  property_count: 5
  slug: admin-sdk-directory-users-structure
- name: Google Workspace Structure
  property_count: 0
  slug: google-workspace-structure
jsonld:
- class_count: 0
  name: Admin Sdk Directory Context
  property_count: 0
  slug: admin-sdk-directory-context
- class_count: 0
  name: Google Workspace Context
  property_count: 3
  slug: google-workspace-context
layout: provider
mcp_servers:
- description: Google documents one remote MCP server per Workspace product (Developer Preview). tools/list was probed live on each documented endpoint on 2026-11-04 and answered anonymously; tool calls require OAut
  name: Google Workspace MCP servers
  slug: google-workspace-mcp-servers
modified: '2026-05-19'
name: Google Workspace
nav: Providers
network: true
overview: 'Google Workspace publishes 33 API contracts indexed on the [APIs.io](https://apis.io/) network, including Groups API, Users API, APIs Calendar API, and 30 more. Tagged areas include Calendar, Collaboration, Email, Productivity, and Storage.


  The Google Workspace catalog on APIs.io includes 2 JSON-LD contexts and 3 Spectral governance rulesets.


  Google Workspace''s developer surface includes CLI, documentation, authentication, developer console, support, pricing, engineering blog, and 58 more developer resources.'
plans:
- name: Google Workspace Plans Pricing
  plan_count: 4
  slug: google-workspace-plans-pricing
- name: Google Workspace Price Estimates
  plan_count: 0
  slug: google-workspace-price-estimates
random_paper: 1
rate_limits:
- limit_count: 4
  name: Google Workspace Rate Limits
  slug: google-workspace-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Google Workspace — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-workspace-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Google Workspace API Rules
  rule_count: 60
  severity_counts:
    error: 55
    hint: 0
    info: 1
    warn: 4
  slug: google-workspace-rules
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Google Workspace API Rules
  rule_count: 18
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 9
  slug: google-workspace-spectral-rules
scopes:
- name: Google Workspace Scopes
  scope_count: 6
  slug: google-workspace-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: exemplar
  composite: 68.6
  coverage:
    artifact_dirs: 39
    catalog_earned: 78.4
    catalog_earned_first_party: 24.0
    catalog_gap: 36.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.7
  facets:
    access_clarity: 84.2
    contract_governance: 31.8
    contract_quality: 61.0
    developer_ergonomics: 69.6
    discoverability: 58.3
    operational_transparency: 76.3
  previous_composite: 61.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/google-workspace/google-workspace-2026-06-20T182248.png
security:
- kind: authentication
  name: Google Workspace Authentication
  slug: google-workspace-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Workspace Domain Security
  slug: google-workspace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Workspace Vulnerability Disclosure
  slug: google-workspace-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: provision-directory-user
  slug: google-workspace-provision-directory-user
- name: schedule-calendar-event
  slug: google-workspace-schedule-calendar-event
- name: send-gmail-message
  slug: google-workspace-send-gmail-message
slug: google-workspace
tags:
- Calendar
- Collaboration
- Email
- Productivity
- Storage
- Video Conferencing
- Google Workspace
use_cases:
- description: Provision user accounts, assign groups and licenses, and configure organizational units for new employee onboarding.
  name: Automated Onboarding
- description: Automate document creation, approval workflows, and distribution using Docs, Sheets, and Drive APIs.
  name: Document Workflow Automation
- description: Schedule meetings, manage recordings and transcripts, and integrate video conferencing into custom applications.
  name: Meeting Management
- description: Monitor security alerts, audit user activity, and enforce compliance policies across the Google Workspace domain.
  name: Security Monitoring
- description: Automate email campaigns, manage support inboxes, and integrate Gmail with CRM and helpdesk systems.
  name: Customer Communication
website: https://workspace.google.com/
---
