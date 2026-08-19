---
access_model:
  confidence: high
  label: Freemium, self-service
  onboarding: unknown
  pricing: freemium
  public: true
  source:
  - https://www.zoho.com/crm/zohocrm-pricing.html
  - https://www.zoho.com/crm/signup.html
  - https://api-console.zoho.com/
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 249
  human_in_the_loop: 1
  name: Zoho Crm Agentic Access
  operation_count: 405
  slug: zoho-crm-agentic-access
  summary_line: 405 operations · 249 acting · 1 human-in-the-loop
api_count: 106
apis:
- description: 'Instant Notifications API for Zoho CRM. Subscribers register a channel via POST /crm/v2/actions/watch with a notify_url and a list of module/operation events (for example Leads.create, Contacts.edit, '
  name: Zoho CRM Notifications API v2
  slug: notifications-api-v2
- description: API to list all available REST APIs in Zoho CRM v8 for the current user and org.
  name: Zoho CRM Available Apis
  slug: apis
- description: API for fetching and updating appointment preferences in Zoho CRM. These preferences define how appointments behave, including job sheet visibility, deal creation, and booking constraints.
  name: Zoho CRM Appointment Preference
  slug: appointment-preference
- description: appointments module api. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 7 operation(s).
  name: Zoho CRM Appointments API
  slug: appointments
- description: Assignment rule apis. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 2 operation(s).
  name: Zoho CRM Assignment rules
  slug: assignment-rules
- description: Associates emails to CRM records and checks availability. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 1 operation(s).
  name: Zoho CRM Associate Email API
  slug: associate-email
- description: Attachments. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 4 operation(s).
  name: Zoho CRM Attachments
  slug: attachments
- description: Bulk Read. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 3 operation(s).
  name: Zoho CRM Audit Log Export
  slug: audit-log-export
- description: Retrieve the list of currencies supported in CRM. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 0 operation(s).
  name: Zoho CRM Available Currencies
  slug: available-currencies
- description: Bulk Read. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 3 operation(s).
  name: Zoho CRM Bulk Read
  slug: bulk-read
- description: Bulk Write API allows you to insert, update, or upsert a large set of data. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 2 operation(s).
  name: Zoho CRM Bulk Write
  slug: bulk-write
- description: Manage organization-wide business hours configuration for Zoho CRM. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 3 operation(s).
  name: Zoho CRM Business Hours
  slug: business-hours
- description: Unenroll cadence for record. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 2 operation(s).
  name: Zoho CRM Cadence Execution
  slug: cadences-execution
- description: Cadences v8 OAS. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 1 operation(s).
  name: Zoho CRM Cadences
  slug: cadences
- description: Preference to show From Number / To Number fields in CRM User can enable the respective preference in order to have the field in CRM. i.e. If user needs From Number field, show_fromnumber preference i
  name: Zoho CRM Call Preferences
  slug: call-preferences
- description: To cancel a meeting and to send an email regarding the meeting cancellation to the participants.
  name: Zoho CRM Cancel Meetings
  slug: cancel-meetings
- description: API for changing the owner of records in CRM modules. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 2 operation(s).
  name: Zoho CRM Change Owner
  slug: change-owner
- description: Composite API. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 1 operation(s).
  name: Zoho CRM Composite Requests
  slug: composite-requests
- description: Contact role API. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 7 operation(s).
  name: Zoho CRM Contact Roles
  slug: contact-roles
- description: API endpoint for retrieving lead conversion options including matching contacts, accounts, field mappings, and layout preferences. Helps determine available conversion paths before performing actual l
  name: Zoho CRM Lead Conversion Options API
  slug: conversion-option
- description: API endpoint for converting Leads into Contacts, Accounts, and Deals within Zoho CRM. Supports configurable conversion options including owner assignment, notification preferences, and tag carryover.
  name: Zoho CRM Lead Conversion API
  slug: convert
- description: COQL APIs to fetch records data based on queries. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 1 operation(s).
  name: Zoho CRM Coql
  slug: coql
- description: APIs for currencies management in CRM. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 7 operation(s).
  name: Zoho CRM Currencies
  slug: currencies
- description: To apply CRUD operations of customviews, to pin field and to sort fields of customviews
  name: Zoho CRM Custom Views
  slug: custom-views
- description: Data Sharing. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 2 operation(s).
  name: Zoho CRM Data Sharing
  slug: data-sharing
- description: 'API for managing contact roles in Deal records. Track and manage which contacts are associated with deals and their specific roles (e.g., Decision Maker, Influencer). Supports full CRUD operations to '
  name: Zoho CRM Deal Contact Roles
  slug: deal-contact-roles
- description: Record Actions. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 4 operation(s).
  name: Zoho CRM Deal Link Emails
  slug: deal-link-emails
- description: Download attachments associated with emails in Zoho CRM. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 1 operation(s).
  name: Zoho CRM Download Email Attachments
  slug: download-attachments
- description: Download Inline Images of an Email. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 1 operation(s).
  name: Zoho CRM Download Inline Images
  slug: download-inline-images
- description: duplicate check preference api. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 4 operation(s).
  name: Zoho CRM Duplicate Check Preference
  slug: duplicate-check-preference
- description: Bad Request. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 5 operation(s).
  name: Zoho CRM Email Drafts
  slug: email-drafts
- description: OpenAPI definition for managing Email Templates APIs. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 1 operation(s).
  name: Zoho CRM Email Templates
  slug: email-templates
- description: To get the details of the users and the type with whom you can share the record's emails.
  name: Zoho CRM Get Email Shared Details
  slug: emails-sharing-details
- description: Details about the Features. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 2 operation(s).
  name: Zoho CRM Features
  slug: features
- description: Rich Text Fields allow users to input formatted text of up to 50,000 characters, including HTML elements. These fields are ideal for entries that require styling and organization, such as product desc
  name: Zoho CRM Fetch Full Data
  slug: fetch-full-data
- description: FieldUpdate v8 OAS. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 6 operation(s).
  name: Zoho CRM Field Updates
  slug: field-updates
- description: To get the field metadata for the specified module including standard module, custom module, subform module, and linking module in you Zoho CRM account. The fields displayed are from all layouts for t
  name: Zoho CRM Fields API
  slug: fields
- description: Zoho CRM Files API — endpoints to upload and retrieve files. POST /crm/v8/files accepts multipart/form-data with a required 'file' field (binary) and returns upload metadata (id, name, status). GET /c
  name: Zoho CRM Files
  slug: files
- description: API endpoints for finding and merging duplicate records in Zoho CRM modules. Supports querying merge job status and performing record merge operations with field mapping and validation.
  name: Zoho CRM Find And Merge
  slug: find-and-merge
- description: API specification for Fiscal Year. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 2 operation(s).
  name: Zoho CRM Fiscal Year
  slug: fiscal-year
- description: To get the list of email addresses that you can send emails from. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 1 operation(s).
  name: Zoho CRM From Addresses
  slug: from-addresses
- description: Get related records count. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 1 operation(s).
  name: Zoho CRM Related Records Count
  slug: get-related-records-count
- description: Global sets are collections of picklist values that can be associated with multiple picklists across modules. Example use cases include maintaining a consistent set of status values or priority levels
  name: Zoho CRM Global Picklists
  slug: global-picklists
- description: Manage business and shift holidays in Zoho CRM. This API allows you to create, retrieve, update, and delete holidays that affect business hours and shift schedules. Business holidays apply to all user
  name: Zoho CRM Holidays API
  slug: holidays
- description: Converts a Quote or Sales Order into Sales Orders or Invoices as applicable. Quotes can be converted into Sales Orders or Invoices.Sales Orders can be converted only into Invoices.
  name: Zoho CRM Inventory Convert
  slug: inventory-convert
- description: OpenAPI definition for managing Inventory Templates APIs. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 1 operation(s).
  name: Zoho CRM Inventory Templates
  slug: inventory-templates
- description: 'API for layout activation and deactivation in Zoho CRM. Supports activating inactive layouts with profile association management and deactivating active layouts with configuration transfer to another '
  name: Zoho CRM Layout Activate and Deactivate API
  slug: layouts-activate-deactivate
- description: 'CRUD operations on Layout customization for modules in Zoho CRM. Supports getting the details of all layouts or a specific layout of a module, updating a layout, deactivating/activating a layout, and '
  name: Zoho CRM Layouts API
  slug: layouts
- description: Record Locking Information APIs allows you to lock records, unlock records, view locking information of locked records and edit locking information of locked records.
  name: Zoho CRM Locking Information
  slug: locking-informations
- description: API specification for MailMerge. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 3 operation(s).
  name: Zoho CRM Mail Merge
  slug: mail-merge
- description: The 'map_dependency' API allows users to manage dependencies between picklist fields in a module layout. It supports operations to retrieve, create, update, and delete field dependencies. These depend
  name: Zoho CRM Map Dependency
  slug: map-dependency
- description: API for mass changing the owner of records in a module based on a custom view. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 2 operation(s).
  name: Zoho CRM Mass Change Owner
  slug: mass-change-owner
- description: Mass convert leads into other CRM modules (Deals/Contacts/Accounts) with options for attachments, tags and related modules.
  name: Zoho CRM Mass Convert
  slug: mass-convert
- description: Mass delete records with record ids and custom view id. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 2 operation(s).
  name: Zoho CRM Mass Delete Api
  slug: mass-delete-cvid
- description: API for mass deletion of tags in Zoho CRM. This endpoint allows administrators to delete multiple tags across modules in bulk.
  name: Zoho CRM Mass Delete Tags
  slug: mass-delete-tags
- description: Enables users to update a specific field value across multiple records within a CRM module.
  name: Zoho CRM Mass Update API
  slug: mass-update
- description: To retrieve records that match your search criteria within a single module. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 1 operation(s).
  name: Zoho CRM Search Records
  slug: module-search
- description: Modules. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 5 operation(s).
  name: Zoho CRM Modules
  slug: modules
- description: Notes. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 7 operation(s).
  name: Zoho CRM Notes
  slug: notes
- description: Notifications management API for subscribing, listing and creating CRM notification channels.
  name: Zoho CRM Notifications
  slug: notifications
- description: Organization Details. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 1 operation(s).
  name: Zoho CRM Org
  slug: org
- description: org_photo. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 3 operation(s).
  name: Zoho CRM Org Photo
  slug: org-photo
- description: Retrieves the ownership change history for CRM records, tracking how record ownership transferred from one user to another over time.
  name: Zoho CRM Ownership History API
  slug: ownership-history
- description: Returns the available pick list values for a specified field in a module. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 1 operation(s).
  name: Zoho CRM Pick List Values
  slug: pick-list-values
- description: API for Managing Pipelines. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 8 operation(s).
  name: Zoho CRM Pipeline
  slug: pipeline
- description: Portal User Type API is used to create, read, update and delete user group for a portal in ZOHO CRM. A portal user type defines a set of permissions and access levels for users associated with that po
  name: Zoho CRM Portal User Type
  slug: portal-user-type
- description: API for managing portal users. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 8 operation(s).
  name: Zoho CRM Portal Users
  slug: portal-users
- description: Portals settings API. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 5 operation(s).
  name: Zoho CRM Portals
  slug: portals
- description: crud operations on CRM profiles. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 5 operation(s).
  name: Zoho CRM Profiles API
  slug: profiles
- description: Records Count. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 1 operation(s).
  name: Zoho CRM Module Record Count
  slug: record-count
- description: Record locking configuration allows you to set up the configuration needed to lock the records in modules manually or automatically when certain conditions are met.
  name: Zoho CRM Record Locking Configuration
  slug: record-locking-configurations
- description: The Zoho CRM Records API allows you to perform CRUD (Create, Read, Update, Delete) operations on records across all modules in your CRM. Use this API to retrieve, create, update, delete, upsert, and c
  name: Zoho CRM Records
  slug: record
- description: Record. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 3 operation(s).
  name: Zoho CRM Record Photo
  slug: record-photo
- description: API To share emails at record-level for a specific record or multiple records with other users in your Zoho CRM organization through API.
  name: Zoho CRM Record Level Sharing Of Emails
  slug: record-share-email
- description: To get, restore and delete Recycle Bin records. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 8 operation(s).
  name: Zoho CRM Recycle Bin
  slug: recycle-bin
- description: Manage the Related List Meta operations in Zoho CRM including retrieving, updating, and customizing related lists for different modules and layouts.
  name: Zoho CRM Related Lists
  slug: related-lists
- description: Notes API allows you to manage additional information attached to CRM records. Notes provide context and details about contacts, accounts, deals, tasks, and other modules. Use this API to create, retr
  name: Zoho CRM Related Notes
  slug: related-notes
- description: RESTful API for managing relationships between CRM records across different modules. Provides comprehensive operations for retrieving, updating, and delinking related records with support for bulk ope
  name: Zoho CRM Related Records API
  slug: related-records
- description: Retrieve Roles in the CRM - Manage user roles and permissions within the Zoho CRM system
  name: Zoho CRM Roles
  slug: roles
- description: Scoring Rules configuration APIs. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 10 operation(s).
  name: Zoho CRM Scoring Rules
  slug: scoring-rules
- description: API to send emails to a record's email ID through Zoho CRM. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 1 operation(s).
  name: Zoho CRM Send Mail
  slug: send-mail
- description: Service Preference. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 2 operation(s).
  name: Zoho CRM Service Preference
  slug: service-preference
- description: API specification for Services API. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 7 operation(s).
  name: Zoho CRM Services API
  slug: services
- description: Share Records. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 4 operation(s).
  name: Zoho CRM Share Records
  slug: share-records
- description: Manage shift hours configuration for Zoho CRM business hours, including shift timing, break schedules, user assignments, and holiday definitions.
  name: Zoho CRM Shift Hours
  slug: shift-hours
- description: This file contains tag actions endpoints. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 6 operation(s).
  name: Zoho CRM Tag Actions API
  slug: tags-actions
- description: This file contains tags CRUD apis. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 5 operation(s).
  name: Zoho CRM Tags CRUD API
  slug: tags
- description: Territories. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 15 operation(s).
  name: Zoho CRM Territories
  slug: territories
- description: Manage users assigned to territories. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 6 operation(s).
  name: Zoho CRM Territory Users
  slug: territory-users
- description: timelines. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 1 operation(s).
  name: Zoho CRM Timelines
  slug: timelines
- description: Unblock Email. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 2 operation(s).
  name: Zoho CRM Unblock Email
  slug: unblock-email
- description: API specification for unsubscribe_links_oas_v8. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 7 operation(s).
  name: Zoho CRM unsubscribe_links
  slug: unsubscribe-links
- description: Upload file. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 1 operation(s).
  name: Zoho CRM Upload
  slug: upload
- description: In Zoho CRM, you can create user groups (set of users) to manage a set of common records. Every group can consist of members that are grouped based on the users, roles (with/without subordinates), ter
  name: Zoho CRM User Groups
  slug: user-groups
- description: Users CRUD operations. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 6 operation(s).
  name: Zoho CRM Users API
  slug: users
- description: API for managing user territories in Zoho CRM. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 5 operation(s).
  name: Zoho CRM Users Territories
  slug: users-territories
- description: API for transferring user data and deleting users in Zoho CRM. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 6 operation(s).
  name: Zoho CRM Users Transfer
  slug: users-transfer
- description: API specification for variable_groups. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 4 operation(s).
  name: Zoho CRM Variable Groups
  slug: variable-groups
- description: API specification for Variables_OAS_v8. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 7 operation(s).
  name: Zoho CRM Variables
  slug: variables
- description: OpenAPI specification for Zoho CRM Webhooks (settings/automation) — endpoints to create, list, update, delete webhooks, inspect failures and usage reports. Targets CRM v8 automation workflows and inte
  name: Zoho CRM Webhooks
  slug: webhooks
- description: Wizards API. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 1 operation(s).
  name: Zoho CRM Wizards
  slug: wizards
- description: Workflow Configuration v8 OAS. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 1 operation(s).
  name: Zoho CRM Workflow Configurations
  slug: workflow-configurations
- description: WorkflowRule v8 OAS. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 12 operation(s).
  name: Zoho CRM Workflow Rules
  slug: workflow-rules
- description: Manage Workflow task (Create, edit,delete and view). Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 6 operation(s).
  name: Zoho CRM Automation Task
  slug: workflow-tasks
- description: Zia enrichment configurations in CRM modules. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 1 operation(s).
  name: Zoho CRM Zia Enrichment Configuration API
  slug: zia-enrichment
- description: Triggers the ZIA organization enrichment process for a given CRM record. Published by Zoho in its first-party OpenAPI 3.1.0 repository github.com/zoho/crm-oas; 3 operation(s).
  name: Zoho CRM ZIA Organization Enrichment API
  slug: zia-org-enrichment
artifact_total: 118
asyncapis:
- description: AsyncAPI 2.6 specification for the Zoho CRM Notifications (Instant Notifications) API surface. Subscribers register a notify_url (channel) with Zoho CRM via the REST "actions/watch" endpoint and recei
  name: Zoho CRM Notifications API
  slug: zoho-crm-notifications-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://www.zoho.com/crm/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.zoho.com/crm/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://www.zoho.com/crm/developer/docs/api/v8/
- group: docs
  title: ''
  type: APIReference
  url: https://www.zoho.com/crm/developer/docs/api/v8/list-available-rest-apis.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.zoho.com/crm/developer/docs/api/v8/oauth-overview.html
- group: operate
  title: ''
  type: Support
  url: https://help.zoho.com/portal/en/community/zoho-crm
- group: company
  title: ''
  type: Blog
  url: https://www.zoho.com/crm/blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zoho
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/zoho/crm-oas
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/zohocrm
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zoho.com/crm/zohocrm-pricing.html
- group: start
  title: ''
  type: SignUp
  url: https://www.zoho.com/crm/signup.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zoho.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zoho.com/privacy.html
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/zohocrmdevelopers/zoho-crm-developers/overview
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/zohocrmdevelopers/zoho-crm-developers/overview
- group: start
  title: ''
  type: Console
  url: https://api-console.zoho.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/zoho-crm-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zoho-crm-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zoho-crm-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zoho-crm-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zoho-crm-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/zoho-crm-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zoho-crm-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zoho.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zoho-crm-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zoho-crm-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/zoho-crm-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/zoho-crm-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/zoho-crm-cli.yml
- group: design
  title: ''
  type: Components
  url: components/zoho-crm-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/zoho-crm-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zoho-crm-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/zoho-crm-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zoho-crm-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://bugbounty.zohocorp.com/bb/info
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zoho-crm-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/zoho-crm-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.zoho.com/compliance.html
- group: design
  title: ''
  type: Conformance
  url: conformance/zoho-crm-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zoho-crm-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/zoho-crm-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zoho-crm-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zoho-crm-llms.txt
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/zoho-crm-notifications-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/zoho-crm-notifications-asyncapi.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/zoho-crm-graphql.md
- group: design
  title: ''
  type: Rules
  url: rules/zoho-crm-asyncapi-spectral-rules.yml
created: '2026-05-11'
description: Zoho CRM is Zoho Corporation's AI-powered sales and customer relationship management platform, used to manage leads, contacts, accounts, deals, activities and customer engagement across channels. Its REST API is currently at v8 and is published as first-party OpenAPI 3.1.0 — 105 specification files covering 405 operations, hosted by Zoho at github.com/zoho/crm-oas and linked from the developer documentation. Authentication is OAuth 2.0 authorization-code against accounts.zoho.com with 458 distinct scopes, and every specification templates both the data centre and the API version into the server URL (https://zohoapis.{dc}/crm/{version}, dc one of com, eu, in, cn, au). Usage is metered in API credits on a rolling 24-hour window rather than in requests, alongside an org-level concurrency cap. Zoho additionally ships server-side SDKs for Node.js, TypeScript, Python, PHP, C#, Java, Ruby and Scala, a widget/extension CLI (ZET), a documented webhook surface (Instant Notifications),
  and a hosted MCP product that names Zoho CRM as a supported app.
graphqls:
- description: This is a conceptual GraphQL schema for Zoho CRM, derived from the Zoho CRM REST API v8. Zoho CRM is an AI-powered sales and customer relationship management platform that helps businesses manage lead
  name: Zoho CRM GraphQL Schema
  slug: zoho-crm-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zoho-crm.png
layout: provider
mcp_servers:
- description: ''
  name: zoho-crm-mcp.yml
  slug: zoho-crm-mcpyml
modified: '2026-08-13'
name: Zoho CRM
nav: Providers
network: true
overview: 'Zoho CRM publishes 106 APIs on the [APIs.io](https://apis.io/) network, including Notifications API v2, Available Apis, Appointment Preference, and 103 more. Tagged areas include CRM, Sales, Customer Relationship Management, Marketing Automation, and Lead Management.


  The Zoho CRM catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Zoho CRM''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 42 more developer resources.'
plans:
- name: Zoho Crm Plans Pricing
  plan_count: 5
  slug: zoho-crm-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 12
  name: Zoho Crm Rate Limits
  slug: zoho-crm-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Zoho CRM API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: zoho-crm-asyncapi-spectral-rules
scopes:
- name: Zoho Crm Scopes
  scope_count: 458
  slug: zoho-crm-scopes
  summary_line: 458 scopes · authorizationCode/clientCredentials
score:
  band: exemplar
  composite: 75.2
  delta: -5.7
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 41.7
    contract_quality: 64.2
    developer_ergonomics: 80.4
    discoverability: 87.0
    governance: 41.7
    operational_transparency: 84.2
  previous_composite: 80.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 2.9
      derived: 0
      marker_coverage: 0.0
      total: 105
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/zoho-crm/refs/heads/main/screenshots/zoho-crm-2026-06-20T201938.png
security:
- kind: authentication
  name: Zoho Crm Authentication
  slug: zoho-crm-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Zoho Crm Domain Security
  slug: zoho-crm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zoho Crm Vulnerability Disclosure
  slug: zoho-crm-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Zoho Crm Trust Center
  slug: zoho-crm-trust-center
  summary_line: ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27018, ISO/IEC 27701, ISO 9001, ISO/IEC 20000-1, ISO 22301, SOC 1 Type 2 (SSAE 18 / ISAE 3402), SOC 2 Type 2, SOC 2 + HIPAA Type 2, PCI DSS (SAQ-D), CSA STAR Self-Assessment, Cyber Essentials Plus, TX-RAMP, ENS (Esquema Nacional de Seguridad, Spain), NCA Class B (Saudi Arabia), NHS DSPT (UK) v8, GoBD (Germany), 21 CFR Part 11 / EudraLex Annex 11, WCAG 2.2 AA
slug: zoho-crm
tags:
- CRM
- Sales
- Customer Relationship Management
- Marketing Automation
- Lead Management
- Customer Engagement
- Sales Automation
- Contact Management
- Pipeline Management
- SaaS
- OpenAPI
- OAuth
website: https://www.zoho.com/crm/
---
