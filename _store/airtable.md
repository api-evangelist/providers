---
aid: airtable
url: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/apis.yml
apis:
  - aid: airtable:airtable-api
    name: Airtable API
    tags:
      - Bases
      - Collaborators
      - Comments
      - Fields
      - Records
      - Tables
      - Views
      - Webhooks
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.airtable.com
    humanURL: https://airtable.com/developers/web/api/introduction
    properties:
      - url: https://airtable.com/developers/web/api/introduction
        type: Documentation
      - url: https://support.airtable.com/docs/getting-started-with-airtables-web-api
        type: GettingStarted
      - url: https://airtable.com/developers/web/api/authentication
        type: Authentication
      - url: https://airtable.com/developers/web/guides/personal-access-tokens
        type: Authentication
      - url: https://airtable.com/developers/web/guides/oauth-integrations
        type: Authentication
      - url: https://airtable.com/developers/web/api/webhooks-overview
        type: AsyncAPI
      - url: https://github.com/Airtable/airtable.js
        type: SDK
      - url: https://www.npmjs.com/package/airtable
        type: SDK
      - url: https://airtable.com/developers/web/api/list-records
        type: APIReference
      - url: https://airtable.com/developers/web/api/update-record
        type: APIReference
      - url: https://airtable.com/developers/web/api/rate-limits
        type: RateLimits
      - url: https://airtable.com/developers/web/api/errors
        type: Errors
      - url: https://airtable.com/developers/web/api/cursor-pagination
        type: Documentation
      - url: https://airtable.com/developers/web/api/field-model
        type: Documentation
      - url: openapi/airtable-airtable-api-openapi.yml
        type: OpenAPI
      - url: json-schema/airtable-record-schema.json
        type: JSONSchema
      - url: json-schema/airtable-comment-schema.json
        type: JSONSchema
      - url: json-schema/airtable-webhook-schema.json
        type: JSONSchema
      - url: json-ld/airtable-context.jsonld
        type: JSON-LD
    description: The Airtable API can be used to integrate your data in Airtable with any external system. The API closely follows REST semantics, uses JSON to encode objects, and relies on standard HTTP codes to signal operation outcomes.
  - aid: airtable:airtable-metadata-api
    name: Airtable Metadata API
    tags:
      - Bases
      - Fields
      - Metadata
      - Schema
      - Tables
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.airtable.com/v0/meta
    humanURL: https://airtable.com/developers/web/api/list-bases
    properties:
      - url: https://airtable.com/developers/web/api/list-bases
        type: Documentation
      - url: https://airtable.com/developers/web/api/get-base-schema
        type: Documentation
      - url: https://airtable.com/developers/web/api/create-base
        type: Documentation
      - url: https://airtable.com/developers/web/api/create-table
        type: Documentation
      - url: https://airtable.com/developers/web/api/create-field
        type: Documentation
      - url: https://airtable.com/developers/web/api/update-table
        type: APIReference
      - url: https://airtable.com/developers/web/api/update-field
        type: APIReference
      - url: openapi/airtable-metadata-api-openapi.yml
        type: OpenAPI
      - url: json-schema/airtable-base-schema.json
        type: JSONSchema
      - url: json-schema/airtable-table-schema.json
        type: JSONSchema
      - url: json-schema/airtable-field-schema.json
        type: JSONSchema
      - url: json-schema/airtable-view-schema.json
        type: JSONSchema
      - url: json-ld/airtable-context.jsonld
        type: JSON-LD
    description: The Airtable Metadata API provides access to base and schema management operations. You can list bases, retrieve base schemas with table and field definitions, create new bases, tables, and fields, and update table and field configurations programmatically.
  - aid: airtable:airtable-enterprise-api
    name: Airtable Enterprise API
    tags:
      - Admin
      - Audit
      - Enterprise
      - Groups
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.airtable.com/v0
    humanURL: https://support.airtable.com/docs/airtable-enterprise-api
    properties:
      - url: https://support.airtable.com/docs/airtable-enterprise-api
        type: Documentation
      - url: https://airtable.com/developers/web/api/get-enterprise
        type: APIReference
      - url: https://airtable.com/developers/web/api/manage-user
        type: APIReference
      - url: https://airtable.com/developers/web/api/manage-user-membership
        type: APIReference
      - url: https://airtable.com/developers/web/api/delete-user-by-id
        type: APIReference
      - url: https://airtable.com/developers/web/api/remove-user-from-enterprise
        type: APIReference
      - url: https://airtable.com/developers/web/api/get-user-group
        type: APIReference
      - url: openapi/airtable-enterprise-api-openapi.yml
        type: OpenAPI
      - url: json-schema/airtable-user-schema.json
        type: JSONSchema
      - url: json-schema/airtable-workspace-schema.json
        type: JSONSchema
      - url: json-ld/airtable-context.jsonld
        type: JSON-LD
    description: The Airtable Enterprise API allows enterprise teams to manage their account programmatically outside of the Admin panel. It supports managing users, updating access permissions, and managing bases, tables, and views at scale for enterprise deployments.
  - aid: airtable:airtable-scim-api
    name: Airtable SCIM API
    tags:
      - Groups
      - Identity
      - Provisioning
      - SCIM
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://airtable.com/scim/v2
    humanURL: https://airtable.com/developers/web/api/scim-overview
    properties:
      - url: https://airtable.com/developers/web/api/scim-overview
        type: Documentation
      - url: https://airtable.com/developers/web/api/model/scim-user-schema
        type: APIReference
      - url: https://airtable.com/developers/web/api/create-scim-user
        type: APIReference
      - url: https://airtable.com/developers/web/api/get-scim-user
        type: APIReference
      - url: https://airtable.com/developers/web/api/put-scim-user
        type: APIReference
      - url: https://airtable.com/developers/web/api/delete-scim-user
        type: APIReference
      - url: https://airtable.com/developers/web/api/get-scim-group
        type: APIReference
      - url: https://airtable.com/developers/web/api/delete-scim-group
        type: APIReference
      - url: https://support.airtable.com/docs/managing-users-via-idp-sync
        type: GettingStarted
      - url: openapi/airtable-scim-api-openapi.yml
        type: OpenAPI
      - url: json-ld/airtable-context.jsonld
        type: JSON-LD
    description: The Airtable SCIM API supports the System for Cross-domain Identity Management specification for automated user and group provisioning. It enables identity providers like Okta and Microsoft Entra ID to manage user accounts and group memberships programmatically.
  - aid: airtable:airtable-audit-logs-api
    name: Airtable Audit Logs API
    tags:
      - Audit
      - Compliance
      - Enterprise
      - Logs
      - Security
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.airtable.com/v0
    humanURL: https://airtable.com/developers/web/api/audit-logs-overview
    properties:
      - url: https://airtable.com/developers/web/api/audit-logs-overview
        type: Documentation
      - url: https://airtable.com/developers/web/api/audit-logs-integration-guide
        type: GettingStarted
      - url: https://airtable.com/developers/web/api/create-audit-log-request
        type: APIReference
      - url: https://airtable.com/developers/web/api/get-audit-log-request
        type: APIReference
      - url: https://airtable.com/developers/web/api/list-audit-log-requests
        type: APIReference
      - url: https://airtable.com/developers/web/api/audit-log-events
        type: APIReference
      - url: https://airtable.com/developers/web/api/audit-log-event-types
        type: APIReference
      - url: https://support.airtable.com/docs/accessing-enterprise-audit-logs-in-airtable
        type: Support
      - url: openapi/airtable-audit-logs-api-openapi.yml
        type: OpenAPI
      - url: json-schema/airtable-audit-log-event-schema.json
        type: JSONSchema
      - url: json-ld/airtable-context.jsonld
        type: JSON-LD
    description: The Airtable Audit Logs API provides programmatic access to enterprise audit logs for compliance monitoring and security tracking. It supports creating and retrieving audit log requests with event filtering by user, event type, and date range.
  - aid: airtable:airtable-shares-api
    name: Airtable Shares API
    tags:
      - Access
      - Collaboration
      - Enterprise
      - Shares
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.airtable.com/v0
    humanURL: https://airtable.com/developers/web/api/list-shares
    properties:
      - url: https://airtable.com/developers/web/api/list-shares
        type: APIReference
      - url: https://airtable.com/developers/web/api/manage-share
        type: APIReference
      - url: https://airtable.com/developers/web/api/delete-share
        type: APIReference
      - url: openapi/airtable-shares-api-openapi.yml
        type: OpenAPI
      - url: json-schema/airtable-share-schema.json
        type: JSONSchema
      - url: json-ld/airtable-context.jsonld
        type: JSON-LD
    description: The Airtable Shares API allows enterprise administrators to list, manage, and delete share links across an organization. It provides programmatic control over base sharing and access management.
name: Airtable
tags:
  - Applications
  - Collaboration
  - Data
  - Databases
  - Low-Code
  - Productivity
  - Spreadsheets
image: https://www.airtable.com/images/logo.png
common:
  - url: https://airtable.com/developers
    type: Portal
  - url: https://airtable.com/developers/web/api/introduction
    type: Documentation
  - url: https://www.airtable.com/guides/scale/using-airtable-api
    type: GettingStarted
  - url: https://airtable.com/developers/web/api/oauth-reference
    type: Authentication
  - url: https://airtable.com/developers/web/api/scopes
    type: Authentication
  - url: https://support.airtable.com/docs/creating-personal-access-tokens
    type: Authentication
  - url: https://airtable.com/developers/web/api/errors
    type: Errors
  - url: https://airtable.com/developers/web/api/rate-limits
    type: RateLimits
  - url: https://support.airtable.com/docs/managing-api-call-limits-in-airtable
    type: RateLimits
  - url: https://airtable.com/developers/web/api/changelog
    type: ChangeLog
  - url: https://support.airtable.com/docs/airtable-api-deprecation-guidelines
    type: Policies
  - url: https://airtable.com/developers/web/api/cursor-pagination
    type: Documentation
  - url: https://airtable.com/developers/web/api/field-model
    type: Documentation
  - url: https://airtable.com/developers/web/api/change-events
    type: Documentation
  - url: https://blog.airtable.com
    type: Blog
  - url: https://status.airtable.com
    type: StatusPage
  - url: https://support.airtable.com
    type: Support
  - url: https://airtable.com/tos
    type: TermsOfService
  - url: https://airtable.com/privacy
    type: PrivacyPolicy
  - url: https://airtable.com/pricing
    type: Pricing
  - url: https://github.com/airtable
    type: GitHubOrganization
  - url: https://community.airtable.com
    type: Community
  - url: https://community.airtable.com/c/developers/55
    type: Forum
  - url: https://www.airtable.com
    type: Portal
  - url: https://airtable.com/login
    type: Portal
  - url: https://airtable.com/signup
    type: SignUp
  - url: http://eepurl.com/gVD-df
    type: Newsletter
  - url: https://airtable.com/developers/extensions
    type: Documentation
  - url: https://airtable.com/developers/scripting/api
    type: Documentation
  - url: https://support.airtable.com/docs/airtable-enterprise-api
    type: Documentation
  - url: https://support.airtable.com/docs/airtable-webhooks-api-overview
    type: AsyncAPI
  - url: https://airtable.com/developers/web/guides/webhooks-api
    type: Documentation
  - url: https://support.airtable.com/docs/airtable-resources-for-developers
    type: Documentation
  - url: https://www.airtable.com/whatsnew
    type: ChangeLog
  - url: https://x.com/airtable
    type: Twitter
  - url: https://www.linkedin.com/company/airtable
    type: LinkedIn
  - url: https://www.youtube.com/@AirtableApp
    type: YouTube
  - url: https://stackoverflow.com/questions/tagged/airtable
    type: StackOverflow
  - url: https://github.com/Airtable/airtable.js
    type: SDK
  - url: https://www.npmjs.com/package/airtable
    type: SDK
  - type: Features
    data:
      - 'Free plan: small-team building blocks'
      - Team at $20/user/mo annual with enhanced capacity
      - Business at $45/user/mo with advanced customization
      - Enterprise Scale with up to 100M records and unlimited workspaces
      - REST API with 5 req/sec per base hard cap
      - 10 records per write, 100 per read
      - Webhooks for record/cell changes
      - Airtable Sync for cross-base data flow
      - Interface Designer for custom apps
      - Automations with multi-step workflows
      - Extensions marketplace for embedded apps
      - OAuth 2.0 and personal access tokens
      - Metadata API for schema discovery
      - Attachments via S3-backed file uploads
      - Linked records and lookups across bases
      - AI features (Cobuilder, Field AI) on paid plans
    sources:
      - https://www.airtable.com/pricing
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: Project Management
        description: Track tasks, milestones, and team assignments in structured databases.
      - name: CRM
        description: Build custom CRM systems for tracking contacts, deals, and pipelines.
      - name: Content Management
        description: Manage editorial calendars, content assets, and publishing workflows.
      - name: Inventory Management
        description: Track inventory, orders, and supply chain data.
      - name: Event Planning
        description: Coordinate event logistics, attendees, and schedules.
      - name: HR & Recruiting
        description: Manage job applicants, employee records, and onboarding processes.
  - type: Integrations
    data:
      - name: Zapier
        description: Connect Airtable to 5000+ apps via Zapier automations.
      - name: Make (Integromat)
        description: Visual automation builder for complex Airtable workflows.
      - name: Slack
        description: Send Airtable notifications and updates to Slack channels.
      - name: Salesforce
        description: Sync Airtable data with Salesforce CRM.
      - name: GitHub
        description: Link Airtable records to GitHub issues and pull requests.
      - name: Okta
        description: Enterprise SSO and SCIM provisioning via Okta.
      - name: Google Workspace
        description: Import from Google Sheets and sync with Google Drive.
  - url: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/rules/airtable-spectral-rules.yml
    type: SpectralRules
    title: Airtable Spectral Rules
  - url: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/capabilities/database-management.yaml
    type: NaftikoCapability
    title: Database Management
  - url: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/vocabulary/airtable-vocabulary.yaml
    type: Vocabulary
    title: Airtable Vocabulary
created: '2023-11-21T00:00:00.000Z'
modified: '2026-05-04'
description: Airtable is a cloud-based collaboration service that combines the simplicity of a spreadsheet with the complexity of a database. It provides APIs for managing bases, tables, records, and more.
maintainers:
  - FN: Kin Lane
    url: http://apievangelist.com
    email: kin@apievangelist.com
  - FN: Airtable
    email: support@airtable.com
    url: https://airtable.com
specificationVersion: '0.19'
type: Index
position: Consumer
access: 3rd-Party
---
