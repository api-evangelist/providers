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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 44
  human_in_the_loop: 1
  name: Ampersand Agentic Access
  operation_count: 81
  slug: ampersand-agentic-access
  summary_line: 81 operations · 44 acting · 1 human-in-the-loop
api_count: 18
apis:
- description: The API Key API from Ampersand — 2 operation(s) for api key.
  name: Ampersand API Key API
  slug: ampersand-api-key-api
- description: The Billing Account API from Ampersand — 2 operation(s) for billing account.
  name: Ampersand Billing Account API
  slug: ampersand-billing-account-api
- description: The Connection API from Ampersand — 3 operation(s) for connection.
  name: Ampersand Connection API
  slug: ampersand-connection-api
- description: The Destination API from Ampersand — 6 operation(s) for destination.
  name: Ampersand Destination API
  slug: ampersand-destination-api
- description: The Installation API from Ampersand — 4 operation(s) for installation.
  name: Ampersand Installation API
  slug: ampersand-installation-api
- description: The Integration API from Ampersand — 4 operation(s) for integration.
  name: Ampersand Integration API
  slug: ampersand-integration-api
- description: The JWT Key API from Ampersand — 2 operation(s) for jwt key.
  name: Ampersand JWT Key API
  slug: ampersand-jwt-key-api
- description: The Notification API from Ampersand — 2 operation(s) for notification.
  name: Ampersand Notification API
  slug: ampersand-notification-api
- description: The OAuth API from Ampersand — 2 operation(s) for oauth.
  name: Ampersand OAuth API
  slug: ampersand-oauth-api
- description: The Objects & Fields API from Ampersand — 4 operation(s) for objects & fields.
  name: Ampersand Objects & Fields API
  slug: ampersand-objects-fields-api
- description: The Operation API from Ampersand — 4 operation(s) for operation.
  name: Ampersand Operation API
  slug: ampersand-operation-api
- description: The Org API from Ampersand — 8 operation(s) for org.
  name: Ampersand Org API
  slug: ampersand-org-api
- description: The Project API from Ampersand — 2 operation(s) for project.
  name: Ampersand Project API
  slug: ampersand-project-api
- description: The Provider API from Ampersand — 2 operation(s) for provider.
  name: Ampersand Provider API
  slug: ampersand-provider-api
- description: The Provider App API from Ampersand — 2 operation(s) for provider app.
  name: Ampersand Provider App API
  slug: ampersand-provider-app-api
- description: The Revision API from Ampersand — 2 operation(s) for revision.
  name: Ampersand Revision API
  slug: ampersand-revision-api
- description: The Upload URL API from Ampersand — 1 operation(s) for upload url.
  name: Ampersand Upload URL API
  slug: ampersand-upload-url-api
- description: The User API from Ampersand — 2 operation(s) for user.
  name: Ampersand User API
  slug: ampersand-user-api
artifact_total: 189
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ampersand-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ampersand-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ampersand-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/meetampersand
- group: company
  title: ''
  type: Website
  url: https://www.withampersand.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.withampersand.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/amp-labs
- group: company
  title: ''
  type: Blog
  url: https://www.withampersand.com/blog
- group: start
  title: ''
  type: Signup
  url: https://dashboard.withampersand.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://dashboard.withampersand.com/sign-in
- group: build
  title: React UI SDK
  type: SDKs
  url: https://www.npmjs.com/package/@amp-labs/react
- group: build
  title: ''
  type: CLI
  url: https://github.com/amp-labs/cli
- group: design
  title: ''
  type: SpectralRules
  url: rules/ampersand-spectral-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/ampersand-api-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ampersand-vocabulary.yaml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.withampersand.com/llms.txt
created: '2026-03-16'
description: Ampersand is a developer-first platform for building native SaaS integrations. It provides an embeddable UI component and managed infrastructure that lets developers add product integrations quickly, handling OAuth, data sync, webhooks, and field mapping out of the box. The platform supports hundreds of SaaS connectors including Salesforce, HubSpot, Marketo, Microsoft Dynamics 365, Zendesk, and Gong with bi-directional sync and declarative configuration.
examples:
- key_count: 4
  name: Ampersand Api Api Key Example
  slug: ampersand-api-api-key-example
- key_count: 1
  name: Ampersand Api Api Key Request Example
  slug: ampersand-api-api-key-request-example
- key_count: 7
  name: Ampersand Api Association Definition Example
  slug: ampersand-api-association-definition-example
- key_count: 2
  name: Ampersand Api Association Labels Example
  slug: ampersand-api-association-labels-example
- key_count: 7
  name: Ampersand Api Backfill Progress Example
  slug: ampersand-api-backfill-progress-example
- key_count: 6
  name: Ampersand Api Billing Account Example
  slug: ampersand-api-billing-account-example
- key_count: 8
  name: Ampersand Api Builder Example
  slug: ampersand-api-builder-example
- key_count: 2
  name: Ampersand Api Builder Info Example
  slug: ampersand-api-builder-info-example
- key_count: 4
  name: Ampersand Api Claimed Domain Response Example
  slug: ampersand-api-claimed-domain-response-example
- key_count: 4
  name: Ampersand Api Config Example
  slug: ampersand-api-config-example
- key_count: 11
  name: Ampersand Api Connection Request Example
  slug: ampersand-api-connection-request-example
- key_count: 3
  name: Ampersand Api Create Jwt Key Request Example
  slug: ampersand-api-create-jwt-key-request-example
- key_count: 6
  name: Ampersand Api Destination Example
  slug: ampersand-api-destination-example
- key_count: 7
  name: Ampersand Api Destination With Secrets Example
  slug: ampersand-api-destination-with-secrets-example
- key_count: 7
  name: Ampersand Api Field Definition Example
  slug: ampersand-api-field-definition-example
- key_count: 4
  name: Ampersand Api Field Upsert Result Example
  slug: ampersand-api-field-upsert-result-example
- key_count: 0
  name: Ampersand Api Generate Connection Request Example
  slug: ampersand-api-generate-connection-request-example
- key_count: 3
  name: Ampersand Api Hydrated Revision Example
  slug: ampersand-api-hydrated-revision-example
- key_count: 8
  name: Ampersand Api Installation Example
  slug: ampersand-api-installation-example
- key_count: 6
  name: Ampersand Api Integration Example
  slug: ampersand-api-integration-example
- key_count: 7
  name: Ampersand Api Invite Example
  slug: ampersand-api-invite-example
- key_count: 3
  name: Ampersand Api Json Patch Operation Example
  slug: ampersand-api-json-patch-operation-example
- key_count: 8
  name: Ampersand Api Jwt Key Example
  slug: ampersand-api-jwt-key-example
- key_count: 1
  name: Ampersand Api Jwt Key Response Example
  slug: ampersand-api-jwt-key-response-example
- key_count: 5
  name: Ampersand Api Notification Event Topic Route Example
  slug: ampersand-api-notification-event-topic-route-example
- key_count: 5
  name: Ampersand Api Numeric Field Options Example
  slug: ampersand-api-numeric-field-options-example
- key_count: 3
  name: Ampersand Api Oauth2 Authorization Code Example
  slug: ampersand-api-oauth2-authorization-code-example
- key_count: 3
  name: Ampersand Api Oauth2 Authorization Code Tokens Only Example
  slug: ampersand-api-oauth2-authorization-code-tokens-only-example
- key_count: 4
  name: Ampersand Api Object Metadata Example
  slug: ampersand-api-object-metadata-example
- key_count: 5
  name: Ampersand Api Org Example
  slug: ampersand-api-org-example
- key_count: 2
  name: Ampersand Api Pagination Info Example
  slug: ampersand-api-pagination-info-example
- key_count: 2
  name: Ampersand Api Patch Api Key Request Example
  slug: ampersand-api-patch-api-key-request-example
- key_count: 2
  name: Ampersand Api Patch Jwt Key Request Example
  slug: ampersand-api-patch-jwt-key-request-example
- key_count: 7
  name: Ampersand Api Project Example
  slug: ampersand-api-project-example
- key_count: 8
  name: Ampersand Api Provider App Example
  slug: ampersand-api-provider-app-example
- key_count: 2
  name: Ampersand Api Provider App Metadata Example
  slug: ampersand-api-provider-app-metadata-example
- key_count: 0
  name: Ampersand Api Provider Metadata Example
  slug: ampersand-api-provider-metadata-example
- key_count: 3
  name: Ampersand Api Provider Metadata Info Example
  slug: ampersand-api-provider-metadata-info-example
- key_count: 3
  name: Ampersand Api Revision Example
  slug: ampersand-api-revision-example
- key_count: 3
  name: Ampersand Api Signed Url Example
  slug: ampersand-api-signed-url-example
- key_count: 5
  name: Ampersand Api String Field Options Example
  slug: ampersand-api-string-field-options-example
- key_count: 5
  name: Ampersand Api Topic Destination Route Example
  slug: ampersand-api-topic-destination-route-example
- key_count: 5
  name: Ampersand Api Topic Example
  slug: ampersand-api-topic-example
- key_count: 1
  name: Ampersand Api Update Connection Request Example
  slug: ampersand-api-update-connection-request-example
- key_count: 2
  name: Ampersand Api Upsert Metadata Request Example
  slug: ampersand-api-upsert-metadata-request-example
- key_count: 2
  name: Ampersand Api Upsert Metadata Response Example
  slug: ampersand-api-upsert-metadata-response-example
- key_count: 0
  name: Ampersand Api Webhook Headers Example
  slug: ampersand-api-webhook-headers-example
features:
- description: Code-based, composable integration building that is version-controllable and CI/CD compatible for professional engineering workflows.
  name: Declarative Integration Framework
- description: Free auth token management with auto-refresh for all supported SaaS providers, eliminating OAuth complexity from product teams.
  name: Managed OAuth Authentication
- description: On-demand read/write operations, scheduled reads, and bulk write capabilities for synchronizing data between SaaS applications.
  name: Bi-directional Data Sync
- description: Authenticated passthrough requests to customer systems enabling direct API calls without managing OAuth tokens.
  name: Proxy API
- description: Historical data retrieval during customer onboarding to populate integrations with existing customer data.
  name: Backfill Support
- description: Automated retries, error handling, quota management, detailed logging, and alerting for production-grade integration reliability.
  name: DevOps Infrastructure
- description: Support for custom objects and fields allowing customers to configure integrations without being constrained by inflexible unified APIs.
  name: Custom Objects and Fields
- description: React UI library with pre-built integration setup flows enabling customers to configure their own SaaS connections within your product.
  name: Embeddable UI Components
- description: Official AI SDK enabling AI agents to read from and write to SaaS applications through natural language via Ampersand integrations.
  name: AI SDK
finops:
- name: Ampersand Finops
  service_category: API
  slug: ampersand-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ampersand.png
json_schemas:
- name: ApiKeyRequest
  property_count: 2
  slug: ampersand-api-api-key-request
- name: ApiKey
  property_count: 5
  slug: ampersand-api-api-key
- name: ApiKeyScopes
  property_count: 0
  slug: ampersand-api-api-key-scopes
- name: AssociationDefinition
  property_count: 8
  slug: ampersand-api-association-definition
- name: AssociationLabels
  property_count: 2
  slug: ampersand-api-association-labels
- name: BackfillProgress
  property_count: 7
  slug: ampersand-api-backfill-progress
- name: BillingAccount
  property_count: 6
  slug: ampersand-api-billing-account
- name: BuilderInfo
  property_count: 3
  slug: ampersand-api-builder-info
- name: Builder
  property_count: 8
  slug: ampersand-api-builder
- name: ClaimedDomainResponse
  property_count: 4
  slug: ampersand-api-claimed-domain-response
- name: Config
  property_count: 5
  slug: ampersand-api-config
- name: ConnectionRequest
  property_count: 13
  slug: ampersand-api-connection-request
- name: CreateJWTKeyRequest
  property_count: 3
  slug: ampersand-api-create-jwt-key-request
- name: Destination
  property_count: 6
  slug: ampersand-api-destination
- name: DestinationWithSecrets
  property_count: 7
  slug: ampersand-api-destination-with-secrets
- name: FieldDefinition
  property_count: 10
  slug: ampersand-api-field-definition
- name: FieldUpsertResult
  property_count: 4
  slug: ampersand-api-field-upsert-result
- name: GenerateConnectionRequest
  property_count: 0
  slug: ampersand-api-generate-connection-request
- name: HydratedRevision
  property_count: 4
  slug: ampersand-api-hydrated-revision
- name: Installation
  property_count: 11
  slug: ampersand-api-installation
- name: Integration
  property_count: 7
  slug: ampersand-api-integration
- name: Invite
  property_count: 7
  slug: ampersand-api-invite
- name: JSONPatchOperation
  property_count: 3
  slug: ampersand-api-json-patch-operation
- name: JWTKeyResponse
  property_count: 1
  slug: ampersand-api-jwt-key-response
- name: JWTKey
  property_count: 8
  slug: ampersand-api-jwt-key
- name: NotificationEventTopicRoute
  property_count: 6
  slug: ampersand-api-notification-event-topic-route
- name: NotificationEventType
  property_count: 0
  slug: ampersand-api-notification-event-type
- name: NumericFieldOptions
  property_count: 5
  slug: ampersand-api-numeric-field-options
- name: Oauth2AuthorizationCode
  property_count: 3
  slug: ampersand-api-oauth2-authorization-code
- name: Oauth2AuthorizationCodeTokensOnly
  property_count: 3
  slug: ampersand-api-oauth2-authorization-code-tokens-only
- name: ObjectMetadata
  property_count: 4
  slug: ampersand-api-object-metadata
- name: Org
  property_count: 5
  slug: ampersand-api-org
- name: PaginationInfo
  property_count: 2
  slug: ampersand-api-pagination-info
- name: PatchApiKeyRequest
  property_count: 2
  slug: ampersand-api-patch-api-key-request
- name: PatchJWTKeyRequest
  property_count: 2
  slug: ampersand-api-patch-jwt-key-request
- name: Project
  property_count: 7
  slug: ampersand-api-project
- name: ProviderAppMetadata
  property_count: 2
  slug: ampersand-api-provider-app-metadata
- name: ProviderApp
  property_count: 9
  slug: ampersand-api-provider-app
- name: ProviderMetadataInfo
  property_count: 3
  slug: ampersand-api-provider-metadata-info
- name: ProviderMetadata
  property_count: 0
  slug: ampersand-api-provider-metadata
- name: Revision
  property_count: 4
  slug: ampersand-api-revision
- name: SignedUrl
  property_count: 3
  slug: ampersand-api-signed-url
- name: StringFieldOptions
  property_count: 5
  slug: ampersand-api-string-field-options
- name: TopicDestinationRoute
  property_count: 5
  slug: ampersand-api-topic-destination-route
- name: Topic
  property_count: 5
  slug: ampersand-api-topic
- name: UpdateConnectionRequest
  property_count: 2
  slug: ampersand-api-update-connection-request
- name: UpdateMask
  property_count: 0
  slug: ampersand-api-update-mask
- name: UpsertMetadataRequest
  property_count: 2
  slug: ampersand-api-upsert-metadata-request
- name: UpsertMetadataResponse
  property_count: 2
  slug: ampersand-api-upsert-metadata-response
- name: WebhookHeaders
  property_count: 0
  slug: ampersand-api-webhook-headers
json_structures:
- name: Ampersand Api Api Key Request Structure
  property_count: 2
  slug: ampersand-api-api-key-request-structure
- name: Ampersand Api Api Key Scopes Structure
  property_count: 0
  slug: ampersand-api-api-key-scopes-structure
- name: Ampersand Api Api Key Structure
  property_count: 5
  slug: ampersand-api-api-key-structure
- name: Ampersand Api Association Definition Structure
  property_count: 8
  slug: ampersand-api-association-definition-structure
- name: Ampersand Api Association Labels Structure
  property_count: 2
  slug: ampersand-api-association-labels-structure
- name: Ampersand Api Backfill Progress Structure
  property_count: 7
  slug: ampersand-api-backfill-progress-structure
- name: Ampersand Api Billing Account Structure
  property_count: 6
  slug: ampersand-api-billing-account-structure
- name: Ampersand Api Builder Info Structure
  property_count: 3
  slug: ampersand-api-builder-info-structure
- name: Ampersand Api Builder Structure
  property_count: 8
  slug: ampersand-api-builder-structure
- name: Ampersand Api Claimed Domain Response Structure
  property_count: 4
  slug: ampersand-api-claimed-domain-response-structure
- name: Ampersand Api Config Structure
  property_count: 5
  slug: ampersand-api-config-structure
- name: Ampersand Api Connection Request Structure
  property_count: 13
  slug: ampersand-api-connection-request-structure
- name: Ampersand Api Create Jwt Key Request Structure
  property_count: 3
  slug: ampersand-api-create-jwt-key-request-structure
- name: Ampersand Api Destination Structure
  property_count: 6
  slug: ampersand-api-destination-structure
- name: Ampersand Api Destination With Secrets Structure
  property_count: 7
  slug: ampersand-api-destination-with-secrets-structure
- name: Ampersand Api Field Definition Structure
  property_count: 10
  slug: ampersand-api-field-definition-structure
- name: Ampersand Api Field Upsert Result Structure
  property_count: 4
  slug: ampersand-api-field-upsert-result-structure
- name: Ampersand Api Generate Connection Request Structure
  property_count: 0
  slug: ampersand-api-generate-connection-request-structure
- name: Ampersand Api Hydrated Revision Structure
  property_count: 4
  slug: ampersand-api-hydrated-revision-structure
- name: Ampersand Api Installation Structure
  property_count: 11
  slug: ampersand-api-installation-structure
- name: Ampersand Api Integration Structure
  property_count: 7
  slug: ampersand-api-integration-structure
- name: Ampersand Api Invite Structure
  property_count: 7
  slug: ampersand-api-invite-structure
- name: Ampersand Api Json Patch Operation Structure
  property_count: 3
  slug: ampersand-api-json-patch-operation-structure
- name: Ampersand Api Jwt Key Response Structure
  property_count: 1
  slug: ampersand-api-jwt-key-response-structure
- name: Ampersand Api Jwt Key Structure
  property_count: 8
  slug: ampersand-api-jwt-key-structure
- name: Ampersand Api Notification Event Topic Route Structure
  property_count: 6
  slug: ampersand-api-notification-event-topic-route-structure
- name: Ampersand Api Notification Event Type Structure
  property_count: 0
  slug: ampersand-api-notification-event-type-structure
- name: Ampersand Api Numeric Field Options Structure
  property_count: 5
  slug: ampersand-api-numeric-field-options-structure
- name: Ampersand Api Oauth2 Authorization Code Structure
  property_count: 3
  slug: ampersand-api-oauth2-authorization-code-structure
- name: Ampersand Api Oauth2 Authorization Code Tokens Only Structure
  property_count: 3
  slug: ampersand-api-oauth2-authorization-code-tokens-only-structure
- name: Ampersand Api Object Metadata Structure
  property_count: 4
  slug: ampersand-api-object-metadata-structure
- name: Ampersand Api Org Structure
  property_count: 5
  slug: ampersand-api-org-structure
- name: Ampersand Api Pagination Info Structure
  property_count: 2
  slug: ampersand-api-pagination-info-structure
- name: Ampersand Api Patch Api Key Request Structure
  property_count: 2
  slug: ampersand-api-patch-api-key-request-structure
- name: Ampersand Api Patch Jwt Key Request Structure
  property_count: 2
  slug: ampersand-api-patch-jwt-key-request-structure
- name: Ampersand Api Project Structure
  property_count: 7
  slug: ampersand-api-project-structure
- name: Ampersand Api Provider App Metadata Structure
  property_count: 2
  slug: ampersand-api-provider-app-metadata-structure
- name: Ampersand Api Provider App Structure
  property_count: 9
  slug: ampersand-api-provider-app-structure
- name: Ampersand Api Provider Metadata Info Structure
  property_count: 3
  slug: ampersand-api-provider-metadata-info-structure
- name: Ampersand Api Provider Metadata Structure
  property_count: 0
  slug: ampersand-api-provider-metadata-structure
- name: Ampersand Api Revision Structure
  property_count: 4
  slug: ampersand-api-revision-structure
- name: Ampersand Api Signed Url Structure
  property_count: 3
  slug: ampersand-api-signed-url-structure
- name: Ampersand Api String Field Options Structure
  property_count: 5
  slug: ampersand-api-string-field-options-structure
- name: Ampersand Api Topic Destination Route Structure
  property_count: 5
  slug: ampersand-api-topic-destination-route-structure
- name: Ampersand Api Topic Structure
  property_count: 5
  slug: ampersand-api-topic-structure
- name: Ampersand Api Update Connection Request Structure
  property_count: 2
  slug: ampersand-api-update-connection-request-structure
- name: Ampersand Api Update Mask Structure
  property_count: 0
  slug: ampersand-api-update-mask-structure
- name: Ampersand Api Upsert Metadata Request Structure
  property_count: 2
  slug: ampersand-api-upsert-metadata-request-structure
- name: Ampersand Api Upsert Metadata Response Structure
  property_count: 2
  slug: ampersand-api-upsert-metadata-response-structure
- name: Ampersand Api Webhook Headers Structure
  property_count: 0
  slug: ampersand-api-webhook-headers-structure
jsonld:
- class_count: 49
  name: Ampersand Api Context
  property_count: 113
  slug: ampersand-api-context
layout: provider
modified: '2026-05-19'
name: Ampersand
nav: Providers
network: true
overview: 'Ampersand publishes 18 APIs on the [APIs.io](https://apis.io/) network, including API Key API, Billing Account API, Connection API, and 15 more. Tagged areas include Developer Tools, Integrations, Platform, SaaS, and OAuth.


  The Ampersand catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Ampersand''s developer surface includes authentication, documentation, engineering blog, signup flow, CLI, and 11 more developer resources.'
plans:
- name: Ampersand Plans Pricing
  plan_count: 3
  slug: ampersand-plans-pricing
random_paper: 115
rate_limits:
- limit_count: 5
  name: Ampersand Rate Limits
  slug: ampersand-rate-limits
rules:
- name: Ampersand API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ampersand-jsonschema-spectral-rules
- name: Ampersand API Rules
  rule_count: 31
  severity_counts:
    error: 15
    hint: 0
    info: 3
    warn: 13
  slug: ampersand-spectral-rules
score:
  band: developing
  composite: 47.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 65.7
    developer_ergonomics: 34.8
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 13.2
  previous_composite: 47.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ampersand/refs/heads/main/screenshots/ampersand-2026-06-20T171937.png
security:
- kind: authentication
  name: Ampersand Authentication
  slug: ampersand-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Ampersand Domain Security
  slug: ampersand-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ampersand
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
use_cases:
- description: Build native Salesforce, HubSpot, and Dynamics 365 integrations to sync customer data bidirectionally with your SaaS product.
  name: CRM Integration
- description: Connect Marketo, HubSpot, and other marketing platforms to enable customer data flows for campaign automation and lead management.
  name: Marketing Automation Integration
- description: Integrate Zendesk and other support platforms to sync tickets, contacts, and customer data with your application.
  name: Customer Support Integration
- description: Connect Gong and other conversation platforms to access call recordings, transcripts, and insights within your application.
  name: Conversation Intelligence Integration
- description: Enable AI agents to read from and write to customer SaaS systems through the Ampersand AI SDK for autonomous workflow automation.
  name: AI Agent Integration
- description: Embed Ampersand's React UI components into your product so customers can self-service configure their own SaaS integrations.
  name: Developer Portal Embedding
website: https://www.withampersand.com/
---
