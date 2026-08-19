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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Google Workspace Agentic Access
  operation_count: 21
  slug: google-workspace-agentic-access
  summary_line: 21 operations · 15 acting
api_count: 29
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
- description: Manage groups in a Google Workspace domain
  name: Google Workspace Groups API
  slug: google-workspace-groups-api
- description: Manage organizational units in a Google Workspace domain
  name: Google Workspace OrgUnits API
  slug: google-workspace-orgunits-api
- description: Manage user accounts in a Google Workspace domain
  name: Google Workspace Users API
  slug: google-workspace-users-api
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
artifact_total: 115
collections:
- collection_type: postman
  name: Google Workspace Admin SDK Directory API
  slug: postman-admin-sdk-directory-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-workspace-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-workspace-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-workspace-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-workspace-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-workspace-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-workspace/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-audit-user-groups-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-create-group-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-create-org-unit-and-assign-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-decommission-org-unit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-delete-user-safely-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-find-and-delete-group-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-find-and-update-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-inspect-org-unit-tree-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-move-user-org-unit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-offboard-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-promote-user-to-admin-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-provision-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-rename-group-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-rename-org-unit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-workspace-reset-user-password-workflow.yml
- group: design
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
- group: build
  title: ''
  type: SDKs
  url: https://developers.google.com/workspace/guides/libraries
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
- name: Google Workspace Finops
  service_category: Productivity / Collaboration SaaS
  slug: google-workspace-finops
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
- name: Group
  property_count: 10
  slug: google-workspace-group
- name: Groups
  property_count: 4
  slug: google-workspace-groups
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
modified: '2026-05-19'
name: Google Workspace
nav: Providers
network: true
overview: 'Google Workspace publishes 3 APIs on the [APIs.io](https://apis.io/) network: Groups API, OrgUnits API, and Users API. Tagged areas include Calendar, Collaboration, Email, Productivity, and Storage.


  The Google Workspace catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Google Workspace''s developer surface includes authentication, developer console, support, pricing, engineering blog, release notes, getting-started guide, and 28 more developer resources.'
plans:
- name: Google Workspace Plans Pricing
  plan_count: 4
  slug: google-workspace-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 7
  name: Google Workspace Rate Limits
  slug: google-workspace-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Google Workspace API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-workspace-jsonschema-spectral-rules
- effective_rule_count: 59
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
  band: developing
  composite: 47.5
  delta: -7.7
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 9.8
    contract_quality: 69.9
    developer_ergonomics: 47.6
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 42.1
  previous_composite: 55.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/google-workspace/refs/heads/main/screenshots/google-workspace-2026-06-20T182248.png
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
slug: google-workspace
tags:
- Calendar
- Collaboration
- Email
- Productivity
- Storage
- Video Conferencing
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
website: https://developers.google.com/workspace
---
