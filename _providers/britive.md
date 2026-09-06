---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.9
  scored_at: '2026-09-05'
api_count: 3
apis:
- baseURL: https://demo.britive-app.com/api/v1
  baseurl_source: declared
  description: The Britive Secret Manager API covers the Britive vault and secrets lifecycle — vault initialization, static and file secrets, secret versions, secret metadata, password policies, secret templates and
  name: Britive Secrets Manager API
  slug: britive-secrets-manager-api
- description: Britive's first-party Model Context Protocol server, available both as a remote server on the tenant (https://{tenant}.britive-app.com/mcp, OAuth-protected) and as an open-source local server (github.
  name: Britive MCP Server
  slug: britive-mcp-server
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage tag memberships granted via access requests
  name: Britive Access Request Tag Membership API
  slug: britive-access-request-tag-membership-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage API Tokens
  name: Britive API Tokens API
  slug: britive-api-tokens-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Application Environments Accounts
  name: Britive Application Environments - Accounts API
  slug: britive-application-environments-accounts-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Application Environments
  name: Britive Application Environments API
  slug: britive-application-environments-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Application Profiles Advanced Settings
  name: Britive Application Profiles - Advanced Settings API
  slug: britive-application-profiles-advanced-settings-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Application Profiles
  name: Britive Application Profiles API
  slug: britive-application-profiles-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Profile Permission Constraints for the permissions that support to define constraints.
  name: Britive Application Profiles - Permission Constraint Manager API
  slug: britive-application-profiles-permission-constraint-manager-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Application Profiles Permissions
  name: Britive Application Profiles - Permissions API
  slug: britive-application-profiles-permissions-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Application Profiles Policies
  name: Britive Application Profiles - Policies API
  slug: britive-application-profiles-policies-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Application Profiles Scopes
  name: Britive Application Profiles - Scopes API
  slug: britive-application-profiles-scopes-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Application Profiles Session Attributes
  name: Britive Application Profiles - Session Attributes API
  slug: britive-application-profiles-session-attributes-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Application Profiles Sessions
  name: Britive Application Profiles - Sessions API
  slug: britive-application-profiles-sessions-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Application Profiles
  name: Britive Application Profiles - Users and Tags API
  slug: britive-application-profiles-users-and-tags-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage access builder settings for an application
  name: Britive Applications - Access Builder Settings API
  slug: britive-applications-access-builder-settings-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Applications Advanced Settings
  name: Britive Applications - Advanced Settings API
  slug: britive-applications-advanced-settings-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Applications
  name: Britive Applications API
  slug: britive-applications-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage approvers groups for association approvers
  name: Britive Applications - Approvers Groups API
  slug: britive-applications-approvers-groups-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage association approvers for an application
  name: Britive Applications - Association Approvers API
  slug: britive-applications-association-approvers-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Britive Permissions
  name: Britive Applications - Managed Permissions API
  slug: britive-applications-managed-permissions-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Application Permissions
  name: Britive Applications - Permissions API
  slug: britive-applications-permissions-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Application Root Environment Groups
  name: Britive Applications - Root Environment Groups API
  slug: britive-applications-root-environment-groups-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Application Scans
  name: Britive Applications - Scans API
  slug: britive-applications-scans-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: The Approvals API from Britive — 3 operation(s) for approvals.
  name: Britive Approvals API
  slug: britive-approvals-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Audit Log Webhooks
  name: Britive Audit Log Webhooks API
  slug: britive-audit-log-webhooks-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Audit Logs
  name: Britive Audit Logs API
  slug: britive-audit-logs-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Creates an app using custom template and other operations for managing the template.
  name: Britive Custom App Manager API
  slug: britive-custom-app-manager-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Uploads custom app template.
  name: Britive Custom App Template Uploader API
  slug: britive-custom-app-template-uploader-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage global landing page
  name: Britive Global Landing Page API
  slug: britive-global-landing-page-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage identity providers and settings
  name: Britive Identity Providers API
  slug: britive-identity-providers-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage IM Connection Metadata
  name: Britive IM Connection Metadata API
  slug: britive-im-connection-metadata-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage IM Connections
  name: Britive IM Connections API
  slug: britive-im-connections-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage IM Connections
  name: Britive IM Integration API
  slug: britive-im-integration-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage firewall rules/settings
  name: Britive IP Restrictions API
  slug: britive-ip-restrictions-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage ITSM Connection Metadata
  name: Britive ITSM Connection Metadata API
  slug: britive-itsm-connection-metadata-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage ITSM Connections
  name: Britive ITSM Connections API
  slug: britive-itsm-connections-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage ITSM Connections
  name: Britive ITSM Integration API
  slug: britive-itsm-integration-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage MFA authentication settings
  name: Britive Multi Factor Authentication API
  slug: britive-multi-factor-authentication-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage My Access
  name: Britive My Access API
  slug: britive-my-access-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage My Devices
  name: Britive My Devices API
  slug: britive-my-devices-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage My Resources
  name: Britive My Resources API
  slug: britive-my-resources-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage My Resource Integration
  name: Britive My Resources - Integration API
  slug: britive-my-resources-integration-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage My Resource Profiles
  name: Britive My Resources - Profiles API
  slug: britive-my-resources-profiles-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: The Notification Service API from Britive — 9 operation(s) for notification service.
  name: Britive Notification Service API
  slug: britive-notification-service-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage notifications
  name: Britive Notifications API
  slug: britive-notifications-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: The Policy Administration API from Britive — 11 operation(s) for policy administration.
  name: Britive Policy Administration API
  slug: britive-policy-administration-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Profile Requests Britive Permissions
  name: Britive Profile Requests - Managed Permissions API
  slug: britive-profile-requests-managed-permissions-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Reports
  name: Britive Reports API
  slug: britive-reports-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Resources
  name: Britive Resource Manager API
  slug: britive-resource-manager-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Resource Labels
  name: Britive Resource Manager - Labels API
  slug: britive-resource-manager-labels-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Resource Permissions
  name: Britive Resource Manager - Permissions API
  slug: britive-resource-manager-permissions-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Resource Policies
  name: Britive Resource Manager - Policies API
  slug: britive-resource-manager-policies-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Resource Response Templates
  name: Britive Resource Manager - Response Templates API
  slug: britive-resource-manager-response-templates-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Resource Types
  name: Britive Resource Manager - Types API
  slug: britive-resource-manager-types-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Resource Profiles Advanced Settings
  name: Britive Resource Profiles - Advanced Settings API
  slug: britive-resource-profiles-advanced-settings-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Resource Profiles
  name: Britive Resource Profiles API
  slug: britive-resource-profiles-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Resource Profiles Associations
  name: Britive Resource Profiles - Associations API
  slug: britive-resource-profiles-associations-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Resource Profiles Permissions
  name: Britive Resource Profiles - Permissions API
  slug: britive-resource-profiles-permissions-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Resource Profiles Policies
  name: Britive Resource Profiles - Policies API
  slug: britive-resource-profiles-policies-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage SAML Configuration
  name: Britive SAML Configuration API
  slug: britive-saml-configuration-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: The Secret Rotation API from Britive — 2 operation(s) for secret rotation.
  name: Britive Secret Rotation API
  slug: britive-secret-rotation-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage shared signals catalog data
  name: Britive Shared Signals - Catalog API
  slug: britive-shared-signals-catalog-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage shared signals issuers
  name: Britive Shared Signals - Issuers API
  slug: britive-shared-signals-issuers-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage shared signals receivers
  name: Britive Shared Signals - Receivers API
  slug: britive-shared-signals-receivers-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Query shared signals processing results
  name: Britive Shared Signals - Results API
  slug: britive-shared-signals-results-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage service identity association to identity provider
  name: Britive Step Up Authentication API
  slug: britive-step-up-authentication-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage the system announcements
  name: Britive System Announcements API
  slug: britive-system-announcements-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage access request settings for a user tag
  name: Britive Tag Access Request Settings API
  slug: britive-tag-access-request-settings-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Browse tags available for access request
  name: Britive Tag Access Requests API
  slug: britive-tag-access-requests-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Tasks
  name: Britive Task Scheduler API
  slug: britive-task-scheduler-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage User Identity Attributes
  name: Britive User Identity Attributes API
  slug: britive-user-identity-attributes-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage User Built Resources
  name: Britive User Resources API
  slug: britive-user-resources-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Tag Owners manage the tag memberships of their owned tags
  name: Britive User Tag Owner API
  slug: britive-user-tag-owner-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage User Tags
  name: Britive User Tags API
  slug: britive-user-tags-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage Users, Service Identities and AI Identities
  name: Britive Users, Service Identities and AI Identities API
  slug: britive-users-service-identities-and-ai-identities-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage workload identity providers
  name: Britive Workload Identity Providers API
  slug: britive-workload-identity-providers-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage service identity association to SCIM provisioning for identity provider
  name: Britive Workload SCIM Identity Providers API
  slug: britive-workload-scim-identity-providers-api
- baseURL: https://demo.britive-app.com/api
  baseurl_source: declared
  description: Manage service identity association to identity provider
  name: Britive Workload Service Identity Providers API
  slug: britive-workload-service-identity-providers-api
artifact_total: 163
asyncapis:
- description: ''
  name: Britive Events Webhooks
  slug: britive-events-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Britive Services API Documentation Access Request Tag Membership API
  slug: open-britive-access-request-tag-membership-api
- collection_type: open
  name: Britive Services API Documentation API Tokens API
  slug: open-britive-api-tokens-api
- collection_type: open
  name: Britive Services API Documentation Application Environments - Accounts API
  slug: open-britive-application-environments-accounts-api
- collection_type: open
  name: Britive Services API Documentation Application Environments API
  slug: open-britive-application-environments-api
- collection_type: open
  name: Britive Services API Documentation Application Profiles - Advanced Settings API
  slug: open-britive-application-profiles-advanced-settings-api
- collection_type: open
  name: Britive Services API Documentation Application Profiles API
  slug: open-britive-application-profiles-api
- collection_type: open
  name: Britive Services API Documentation Application Profiles - Permission Constraint Manager API
  slug: open-britive-application-profiles-permission-constraint-manager-api
- collection_type: open
  name: Britive Services API Documentation Application Profiles - Permissions API
  slug: open-britive-application-profiles-permissions-api
- collection_type: open
  name: Britive Services API Documentation Application Profiles - Policies API
  slug: open-britive-application-profiles-policies-api
- collection_type: open
  name: Britive Services API Documentation Application Profiles - Scopes API
  slug: open-britive-application-profiles-scopes-api
- collection_type: open
  name: Britive Services API Documentation Application Profiles - Session Attributes API
  slug: open-britive-application-profiles-session-attributes-api
- collection_type: open
  name: Britive Services API Documentation Application Profiles - Sessions API
  slug: open-britive-application-profiles-sessions-api
- collection_type: open
  name: Britive Services API Documentation Application Profiles - Users and Tags API
  slug: open-britive-application-profiles-users-and-tags-api
- collection_type: open
  name: Britive Services API Documentation Applications - Access Builder Settings API
  slug: open-britive-applications-access-builder-settings-api
- collection_type: open
  name: Britive Services API Documentation Applications - Advanced Settings API
  slug: open-britive-applications-advanced-settings-api
- collection_type: open
  name: Britive Services API Documentation Applications API
  slug: open-britive-applications-api
- collection_type: open
  name: Britive Services API Documentation Applications - Approvers Groups API
  slug: open-britive-applications-approvers-groups-api
- collection_type: open
  name: Britive Services API Documentation Applications - Association Approvers API
  slug: open-britive-applications-association-approvers-api
- collection_type: open
  name: Britive Services API Documentation Applications - Managed Permissions API
  slug: open-britive-applications-managed-permissions-api
- collection_type: open
  name: Britive Services API Documentation Applications - Permissions API
  slug: open-britive-applications-permissions-api
- collection_type: open
  name: Britive Services API Documentation Applications - Root Environment Groups API
  slug: open-britive-applications-root-environment-groups-api
- collection_type: open
  name: Britive Services API Documentation Applications - Scans API
  slug: open-britive-applications-scans-api
- collection_type: open
  name: Secret Manager Approvals API
  slug: open-britive-approvals-api
- collection_type: open
  name: Britive Services API Documentation Audit Log Webhooks API
  slug: open-britive-audit-log-webhooks-api
- collection_type: open
  name: Britive Services API Documentation Audit Logs API
  slug: open-britive-audit-logs-api
- collection_type: open
  name: Britive Services API Documentation Custom App Manager API
  slug: open-britive-custom-app-manager-api
- collection_type: open
  name: Britive Services API Documentation Custom App Template Uploader API
  slug: open-britive-custom-app-template-uploader-api
- collection_type: open
  name: Britive Services API Documentation Global Landing Page API
  slug: open-britive-global-landing-page-api
- collection_type: open
  name: Britive Services API Documentation Identity Providers API
  slug: open-britive-identity-providers-api
- collection_type: open
  name: Britive Services API Documentation IM Connection Metadata API
  slug: open-britive-im-connection-metadata-api
- collection_type: open
  name: Britive Services API Documentation IM Connections API
  slug: open-britive-im-connections-api
- collection_type: open
  name: Britive Services API Documentation IM Integration API
  slug: open-britive-im-integration-api
- collection_type: open
  name: Britive Services API Documentation IP Restrictions API
  slug: open-britive-ip-restrictions-api
- collection_type: open
  name: Britive Services API Documentation ITSM Connection Metadata API
  slug: open-britive-itsm-connection-metadata-api
- collection_type: open
  name: Britive Services API Documentation ITSM Connections API
  slug: open-britive-itsm-connections-api
- collection_type: open
  name: Britive Services API Documentation ITSM Integration API
  slug: open-britive-itsm-integration-api
- collection_type: open
  name: Britive Services API Documentation Multi Factor Authentication API
  slug: open-britive-multi-factor-authentication-api
- collection_type: open
  name: Britive Services API Documentation My Access API
  slug: open-britive-my-access-api
- collection_type: open
  name: Britive Services API Documentation My Devices API
  slug: open-britive-my-devices-api
- collection_type: open
  name: Britive Services API Documentation My Resources API
  slug: open-britive-my-resources-api
- collection_type: open
  name: Britive Services API Documentation My Resources - Integration API
  slug: open-britive-my-resources-integration-api
- collection_type: open
  name: Britive Services API Documentation My Resources - Profiles API
  slug: open-britive-my-resources-profiles-api
- collection_type: open
  name: Secret Manager Notification Service API
  slug: open-britive-notification-service-api
- collection_type: open
  name: Britive Services API Documentation Notifications API
  slug: open-britive-notifications-api
- collection_type: open
  name: Secret Manager Policy Administration API
  slug: open-britive-policy-administration-api
- collection_type: open
  name: Britive Services API Documentation Profile Requests - Managed Permissions API
  slug: open-britive-profile-requests-managed-permissions-api
- collection_type: open
  name: Britive Services API Documentation Reports API
  slug: open-britive-reports-api
- collection_type: open
  name: Britive Services API Documentation Resource Manager API
  slug: open-britive-resource-manager-api
- collection_type: open
  name: Britive Services API Documentation Resource Manager - Labels API
  slug: open-britive-resource-manager-labels-api
- collection_type: open
  name: Britive Services API Documentation Resource Manager - Permissions API
  slug: open-britive-resource-manager-permissions-api
- collection_type: open
  name: Britive Services API Documentation Resource Manager - Policies API
  slug: open-britive-resource-manager-policies-api
- collection_type: open
  name: Britive Services API Documentation Resource Manager - Response Templates API
  slug: open-britive-resource-manager-response-templates-api
- collection_type: open
  name: Britive Services API Documentation Resource Manager - Types API
  slug: open-britive-resource-manager-types-api
- collection_type: open
  name: Britive Services API Documentation Resource Profiles - Advanced Settings API
  slug: open-britive-resource-profiles-advanced-settings-api
- collection_type: open
  name: Britive Services API Documentation Resource Profiles API
  slug: open-britive-resource-profiles-api
- collection_type: open
  name: Britive Services API Documentation Resource Profiles - Associations API
  slug: open-britive-resource-profiles-associations-api
- collection_type: open
  name: Britive Services API Documentation Resource Profiles - Permissions API
  slug: open-britive-resource-profiles-permissions-api
- collection_type: open
  name: Britive Services API Documentation Resource Profiles - Policies API
  slug: open-britive-resource-profiles-policies-api
- collection_type: open
  name: Britive Services API Documentation SAML Configuration API
  slug: open-britive-saml-configuration-api
- collection_type: open
  name: Secret Manager Secret Rotation API
  slug: open-britive-secret-rotation-api
- collection_type: open
  name: Secret Manager Secrets Manager API
  slug: open-britive-secrets-manager-api
- collection_type: open
  name: Britive Services API Documentation Shared Signals - Catalog API
  slug: open-britive-shared-signals-catalog-api
- collection_type: open
  name: Britive Services API Documentation Shared Signals - Issuers API
  slug: open-britive-shared-signals-issuers-api
- collection_type: open
  name: Britive Services API Documentation Shared Signals - Receivers API
  slug: open-britive-shared-signals-receivers-api
- collection_type: open
  name: Britive Services API Documentation Shared Signals - Results API
  slug: open-britive-shared-signals-results-api
- collection_type: open
  name: Britive Services API Documentation Step Up Authentication API
  slug: open-britive-step-up-authentication-api
- collection_type: open
  name: Britive Services API Documentation System Announcements API
  slug: open-britive-system-announcements-api
- collection_type: open
  name: Britive Services API Documentation Tag Access Request Settings API
  slug: open-britive-tag-access-request-settings-api
- collection_type: open
  name: Britive Services API Documentation Tag Access Requests API
  slug: open-britive-tag-access-requests-api
- collection_type: open
  name: Britive Services API Documentation Task Scheduler API
  slug: open-britive-task-scheduler-api
- collection_type: open
  name: Britive Services API Documentation User Identity Attributes API
  slug: open-britive-user-identity-attributes-api
- collection_type: open
  name: Britive Services API Documentation User Resources API
  slug: open-britive-user-resources-api
- collection_type: open
  name: Britive Services API Documentation User Tag Owner API
  slug: open-britive-user-tag-owner-api
- collection_type: open
  name: Britive Services API Documentation User Tags API
  slug: open-britive-user-tags-api
- collection_type: open
  name: Britive Services API Documentation Users, Service Identities and AI Identities API
  slug: open-britive-users-service-identities-and-ai-identities-api
- collection_type: open
  name: Britive Services API Documentation Workload Identity Providers API
  slug: open-britive-workload-identity-providers-api
- collection_type: open
  name: Britive Services API Documentation Workload SCIM Identity Providers API
  slug: open-britive-workload-scim-identity-providers-api
- collection_type: open
  name: Britive Services API Documentation Workload Service Identity Providers API
  slug: open-britive-workload-service-identity-providers-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/britive-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/britive/mcp-server/issues
- group: company
  title: ''
  type: Website
  url: https://www.britive.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.britive.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.britive.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.britive.com/apidocs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.britive.com/apidocs/api-prerequisites
- group: company
  title: ''
  type: Blog
  url: https://www.britive.com/resources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/britive
- group: operate
  title: ''
  type: Support
  url: https://www.britive.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://www.britive.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.britive.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.britive.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/britive-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/britive-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/britive-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/britive-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/britive-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/britive-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/britive-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/britive-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/britive-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/britive-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/britive-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/britive-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/britive-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/britive-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/britive-events-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/britive-services-api-overlay.yaml
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/britive
- group: other
  title: ''
  type: TerraformProvider
  url: https://registry.terraform.io/providers/britive/britive/latest
created: '2026-08-08'
description: 'Britive is a runtime privileged access management (PAM) platform that issues just-in-time, ephemeral privileges to human users, non-human identities and AI agents across AWS, Azure, GCP, Oracle Cloud, Kubernetes, Snowflake, Okta, Salesforce, ServiceNow and on-premises systems, so organizations can operate with zero standing privileges. The platform is API-first and agentless: a tenant-scoped REST API at https://{tenant}.britive-app.com/api covers applications, environments, profiles (PAPs), policies, identities, tags, secrets, approvals, audit logs and reporting, and is complemented by an open-source Python SDK, the PyBritive CLI, a Terraform provider, SCIM provisioning, Shared Signals Framework (CAEP/RISC/SET) issuers and receivers, audit-log webhooks, and a first-party MCP server for AI agents.'
image: https://images.prismic.io/britive/ajXRGI1P9HI4UwTa_BritiveRuntimePrivilegedAccessManagementforforAgenticAI%2CNHI%26Humans.png
layout: provider
mcp_servers:
- description: 'Britive ships a first-party Model Context Protocol server that lets AI agents and MCP clients (Claude Desktop, VS Code Copilot) drive the Britive platform: request just-in-time privileged access, chec'
  name: Britive MCP Server
  slug: britive-mcp-server
modified: '2026-08-08'
name: Britive
nav: Providers
network: true
overview: 'Britive publishes 78 APIs on the [APIs.io](https://apis.io/) network, including Secrets Manager API, Access Request Tag Membership API, API Tokens API, and 75 more. Tagged areas include Company, Privileged Access Management, Identity and Access Management, Cloud Security, and Zero Standing Privileges.


  The Britive catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Britive''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, CLI, and 25 more developer resources.'
random_paper: 1
scopes:
- name: Britive Scopes
  scope_count: 0
  slug: britive-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 48.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 60.4
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 42.1
  previous_composite: 48.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 78
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/britive/refs/heads/main/screenshots/britive-2026-08-17T080708.png
security:
- kind: authentication
  name: Britive Authentication
  slug: britive-authentication
  summary_line: http/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Britive Domain Security
  slug: britive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: britive
tags:
- Company
- Privileged Access Management
- Identity and Access Management
- Cloud Security
- Zero Standing Privileges
- Just-In-Time Access
- Non-Human Identity
- Secrets Management
- Agentic AI
- Cybersecurity
website: https://www.britive.com/
---
