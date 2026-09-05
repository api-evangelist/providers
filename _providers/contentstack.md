---
access_model:
  confidence: medium
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
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
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 68
  human_in_the_loop: 0
  name: Contentstack Agentic Access
  operation_count: 132
  slug: contentstack-agentic-access
  summary_line: 132 operations · 68 acting
api_count: 8
apis:
- description: The Contentstack GraphQL Content Delivery API enables developers to query content from their Contentstack stack using GraphQL syntax, allowing precise retrieval of only the fields and relationships ne
  name: Contentstack GraphQL Content Delivery API
  slug: graphql-content-delivery-api
- description: The Contentstack Image Delivery API allows developers to retrieve and transform images stored as assets in their Contentstack stacks. It supports on-the-fly image manipulation operations including res
  name: Contentstack Image Delivery API
  slug: image-delivery-api
- baseURL: https://api.contentstack.io
  baseurl_source: declared
  description: The Contentstack Analytics API provides access to usage and performance metrics for CMS, Launch, and Automate products within a Contentstack organization. Developers can retrieve analytics data progra
  name: Contentstack Analytics API
  slug: analytics-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: Accounts represent authenticated connections to external services and third-party platforms used by automations as action targets.
  name: contentstack Accounts API
  slug: contentstack-accounts-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: Assets are media files such as images, videos, and documents stored in the Contentstack asset library.
  name: contentstack Assets API
  slug: contentstack-assets-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: Attributes represent individual user data characteristics such as age, location, or browsing history used to define audience segments.
  name: contentstack Attributes API
  slug: contentstack-attributes-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: Audiences are defined segments of users grouped by demographic, behavioral, or other attribute-based criteria for targeted content experiences.
  name: contentstack Audiences API
  slug: contentstack-audiences-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: Audit logs track all administrative actions taken within an automation project, providing a history of configuration changes.
  name: contentstack Audit Logs API
  slug: contentstack-audit-logs-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: Automations are individual workflow definitions that connect triggers (such as Contentstack content events) to actions (such as sending notifications or updating external systems).
  name: contentstack Automations API
  slug: contentstack-automations-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: Brand Kits are centralized repositories for an organization's brand identity assets, guidelines, and AI configuration. They are used to ensure consistent brand voice and style across AI-generated cont
  name: contentstack Brand Kits API
  slug: contentstack-brand-kits-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: Content types define the structure of content entries in a Contentstack stack. They specify the fields and their data types that entries must conform to.
  name: contentstack Content Types API
  slug: contentstack-content-types-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: Deployments represent individual build and publish operations to a Launch environment. Each deployment has associated build logs, server logs, and status tracking.
  name: contentstack Deployments API
  slug: contentstack-deployments-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: Entries are instances of content types that hold the actual content data. They can be filtered, sorted, paginated, and localized.
  name: contentstack Entries API
  slug: contentstack-entries-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: Entry variants are customized versions of an entry created for personalization or A/B testing purposes.
  name: contentstack Entry Variants API
  slug: contentstack-entry-variants-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: Endpoints for managing deployment environments (e.g., production, staging) within a stack.
  name: contentstack Environments API
  slug: contentstack-environments-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: The events endpoint allows applications to track user actions and behavioral events for experience analytics and audience rule evaluation.
  name: contentstack Events API
  slug: contentstack-events-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: Execution logs record each time an automation runs, including the trigger context, steps executed, and success or failure status.
  name: contentstack Execution Logs API
  slug: contentstack-execution-logs-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: Experiences define personalized content variations delivered to specific audience segments, supporting both segmented and A/B test configurations.
  name: contentstack Experiences API
  slug: contentstack-experiences-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: File upload endpoints provide pre-signed URLs for securely uploading build artifacts to Contentstack Launch infrastructure before triggering a deployment.
  name: contentstack File Uploads API
  slug: contentstack-file-uploads-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: Geolocation endpoints provide geographic datasets including regions, countries, and cities for location-based audience targeting.
  name: contentstack Geolocation API
  slug: contentstack-geolocation-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: Global fields are reusable field groups that can be referenced across multiple content types within a Contentstack stack.
  name: contentstack Global Fields API
  slug: contentstack-global-fields-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: LLM Configuration endpoints allow organizations to register custom API credentials for large language model providers, enabling content generation through their own LLM subscriptions.
  name: contentstack LLM Configuration API
  slug: contentstack-llm-configuration-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: The manifest endpoint returns a list of all active experiences and their corresponding variants that are activated for the current user based on their attributes and audience membership.
  name: contentstack Manifest API
  slug: contentstack-manifest-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: Endpoints for managing Contentstack organizations, including user invitations, roles, stacks, and audit logs at the organization level.
  name: contentstack Organizations API
  slug: contentstack-organizations-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: Automation projects are containers for automations within a Contentstack organization. Each project groups related automations and can have its own variables and account connections.
  name: contentstack Projects API
  slug: contentstack-projects-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: SCIM group endpoints allow Identity Providers to manage group memberships in Contentstack, which map to role-based access control within the CMS.
  name: contentstack SCIM Groups API
  slug: contentstack-scim-groups-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: Schema discovery endpoints implement the SCIM 2.0 service provider configuration, returning supported schemas and resource types for IdP compatibility validation.
  name: contentstack SCIM Schema Discovery API
  slug: contentstack-scim-schema-discovery-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: SCIM user endpoints enable Identity Providers to provision, update, and deprovision user accounts within a Contentstack organization following the SCIM 2.0 User schema.
  name: contentstack SCIM Users API
  slug: contentstack-scim-users-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: Endpoints for creating and managing Contentstack stacks, including settings, users, sharing, and ownership transfer.
  name: contentstack Stacks API
  slug: contentstack-stacks-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: The synchronization endpoints allow developers to sync published content incrementally, enabling efficient local caching and offline-first patterns.
  name: contentstack Synchronization API
  slug: contentstack-synchronization-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: Endpoints for setting, updating, and merging user attribute data used to determine audience membership and personalized content targeting.
  name: contentstack User Attributes API
  slug: contentstack-user-attributes-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: Endpoints for authenticating users and managing session tokens within Contentstack.
  name: contentstack User Sessions API
  slug: contentstack-user-sessions-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: Endpoints for managing Contentstack user accounts including profile updates, password resets, and account activation.
  name: contentstack Users API
  slug: contentstack-users-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: Project variables are reusable key-value pairs that can be referenced across multiple automations within a project.
  name: contentstack Variables API
  slug: contentstack-variables-api
- baseURL: https://cdn.contentstack.io
  baseurl_source: declared
  description: Voice Profiles define the writing style, tone, and persona characteristics for AI content generation within a Brand Kit. Multiple voice profiles can be created to support different content contexts or
  name: contentstack Voice Profiles API
  slug: contentstack-voice-profiles-api
artifact_total: 200
asyncapis:
- description: Contentstack Webhooks provide event-driven notifications for content lifecycle events within a stack. When configured, Contentstack sends HTTP POST requests to your specified endpoint URL whenever mat
  name: Contentstack Webhooks
  slug: contentstack-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Contentstack Analytics Accounts API
  slug: open-contentstack-accounts-api
- collection_type: open
  name: Contentstack Accounts Analytics API
  slug: open-contentstack-analytics-api
- collection_type: open
  name: Contentstack Analytics Accounts Assets API
  slug: open-contentstack-assets-api
- collection_type: open
  name: Contentstack Analytics Accounts Attributes API
  slug: open-contentstack-attributes-api
- collection_type: open
  name: Contentstack Analytics Accounts Audiences API
  slug: open-contentstack-audiences-api
- collection_type: open
  name: Contentstack Analytics Accounts Audit Logs API
  slug: open-contentstack-audit-logs-api
- collection_type: open
  name: Contentstack Automate Management API
  slug: open-contentstack-automate-management-api
- collection_type: open
  name: Contentstack Analytics Accounts Automations API
  slug: open-contentstack-automations-api
- collection_type: open
  name: Contentstack Brand Kit Management API
  slug: open-contentstack-brand-kit-management-api
- collection_type: open
  name: Contentstack Analytics Accounts Brand Kits API
  slug: open-contentstack-brand-kits-api
- collection_type: open
  name: Contentstack Analytics Accounts Cache Analytics API
  slug: open-contentstack-cache-analytics-api
- collection_type: open
  name: Contentstack Content Delivery API
  slug: open-contentstack-content-delivery-api
- collection_type: open
  name: Contentstack Content Management API
  slug: open-contentstack-content-management-api
- collection_type: open
  name: Contentstack Analytics Accounts Content Types API
  slug: open-contentstack-content-types-api
- collection_type: open
  name: Contentstack Analytics Accounts Deployments API
  slug: open-contentstack-deployments-api
- collection_type: open
  name: Contentstack Analytics Accounts Device Usage API
  slug: open-contentstack-device-usage-api
- collection_type: open
  name: Contentstack Analytics Accounts Entries API
  slug: open-contentstack-entries-api
- collection_type: open
  name: Contentstack Analytics Accounts Entry Variants API
  slug: open-contentstack-entry-variants-api
- collection_type: open
  name: Contentstack Analytics Accounts Environments API
  slug: open-contentstack-environments-api
- collection_type: open
  name: Contentstack Analytics Accounts Events API
  slug: open-contentstack-events-api
- collection_type: open
  name: Contentstack Analytics Accounts Execution Logs API
  slug: open-contentstack-execution-logs-api
- collection_type: open
  name: Contentstack Analytics Accounts Experiences API
  slug: open-contentstack-experiences-api
- collection_type: open
  name: Contentstack Analytics Accounts File Uploads API
  slug: open-contentstack-file-uploads-api
- collection_type: open
  name: Contentstack Analytics Accounts Generative AI API
  slug: open-contentstack-generative-ai-api
- collection_type: open
  name: Contentstack Analytics Accounts Geolocation API
  slug: open-contentstack-geolocation-api
- collection_type: open
  name: Contentstack Analytics Accounts Global Fields API
  slug: open-contentstack-global-fields-api
- collection_type: open
  name: Contentstack Analytics Accounts Jobs API
  slug: open-contentstack-jobs-api
- collection_type: open
  name: Contentstack Analytics Accounts Knowledge Vault API
  slug: open-contentstack-knowledge-vault-api
- collection_type: open
  name: Contentstack Launch API
  slug: open-contentstack-launch-api
- collection_type: open
  name: Contentstack Analytics Accounts LLM Configuration API
  slug: open-contentstack-llm-configuration-api
- collection_type: open
  name: Contentstack Analytics Accounts Manifest API
  slug: open-contentstack-manifest-api
- collection_type: open
  name: Contentstack Analytics Accounts Organizations API
  slug: open-contentstack-organizations-api
- collection_type: open
  name: Contentstack Personalize Edge API
  slug: open-contentstack-personalize-edge-api
- collection_type: open
  name: Contentstack Personalize Management API
  slug: open-contentstack-personalize-management-api
- collection_type: open
  name: Contentstack Analytics Accounts Projects API
  slug: open-contentstack-projects-api
- collection_type: open
  name: Contentstack SCIM API
  slug: open-contentstack-scim-api
- collection_type: open
  name: Contentstack Analytics Accounts SCIM Groups API
  slug: open-contentstack-scim-groups-api
- collection_type: open
  name: Contentstack Analytics Accounts SCIM Schema Discovery API
  slug: open-contentstack-scim-schema-discovery-api
- collection_type: open
  name: Contentstack Analytics Accounts SCIM Users API
  slug: open-contentstack-scim-users-api
- collection_type: open
  name: Contentstack Analytics Accounts SDK Usage API
  slug: open-contentstack-sdk-usage-api
- collection_type: open
  name: Contentstack Analytics Accounts Stacks API
  slug: open-contentstack-stacks-api
- collection_type: open
  name: Contentstack Analytics Accounts Status Code Analytics API
  slug: open-contentstack-status-code-analytics-api
- collection_type: open
  name: Contentstack Analytics Accounts Subscription Usage API
  slug: open-contentstack-subscription-usage-api
- collection_type: open
  name: Contentstack Analytics Accounts Synchronization API
  slug: open-contentstack-synchronization-api
- collection_type: open
  name: Contentstack Analytics Accounts URL Analytics API
  slug: open-contentstack-url-analytics-api
- collection_type: open
  name: Contentstack Analytics Accounts Usage Analytics API
  slug: open-contentstack-usage-analytics-api
- collection_type: open
  name: Contentstack Analytics Accounts User Attributes API
  slug: open-contentstack-user-attributes-api
- collection_type: open
  name: Contentstack Analytics Accounts User Sessions API
  slug: open-contentstack-user-sessions-api
- collection_type: open
  name: Contentstack Analytics Accounts Users API
  slug: open-contentstack-users-api
- collection_type: open
  name: Contentstack Analytics Accounts Variables API
  slug: open-contentstack-variables-api
- collection_type: open
  name: Contentstack Analytics Accounts Voice Profiles API
  slug: open-contentstack-voice-profiles-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/contentstack-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/contentstack-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/contentstack-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/contentstack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/contentstack-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/contentstack
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/contentstack
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/contentstack-webhooks-asyncapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/contentstack-entry-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/contentstack-stack-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/contentstack-webhook-payload-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/contentstack-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/contentstack-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/contentstack-rules.yml
description: This document is a detailed reference to Contentstack’s Content Delivery API. Retrieve content from your account and deliver it to web and mobile properties.
finops:
- name: Contentstack Finops
  service_category: Headless CMS / Digital Experience Platform
  slug: contentstack-finops
graphqls:
- description: The Contentstack GraphQL Content Delivery API enables developers to query content from their Contentstack stack using GraphQL syntax, allowing precise retrieval of only the fields and relationships ne
  name: contentstack GraphQL API
  slug: contentstack-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/contentstack.png
json_schemas:
- name: Account
  property_count: 4
  slug: contentstack-account
- name: AccountList
  property_count: 1
  slug: contentstack-accountlist
- name: AnalyticsRequest
  property_count: 5
  slug: contentstack-analyticsrequest
- name: Asset
  property_count: 8
  slug: contentstack-asset
- name: AssetList
  property_count: 2
  slug: contentstack-assetlist
- name: Attribute
  property_count: 5
  slug: contentstack-attribute
- name: AttributeList
  property_count: 1
  slug: contentstack-attributelist
- name: Audience
  property_count: 5
  slug: contentstack-audience
- name: AudienceList
  property_count: 1
  slug: contentstack-audiencelist
- name: AuditLog
  property_count: 4
  slug: contentstack-auditlog
- name: AuditLogList
  property_count: 1
  slug: contentstack-auditloglist
- name: Automation
  property_count: 7
  slug: contentstack-automation
- name: AutomationList
  property_count: 1
  slug: contentstack-automationlist
- name: BrandKit
  property_count: 6
  slug: contentstack-brandkit
- name: BrandKitList
  property_count: 2
  slug: contentstack-brandkitlist
- name: CacheUsage
  property_count: 4
  slug: contentstack-cacheusage
- name: ContentType
  property_count: 6
  slug: contentstack-contenttype
- name: ContentTypeList
  property_count: 2
  slug: contentstack-contenttypelist
- name: CreateAttributeRequest
  property_count: 3
  slug: contentstack-createattributerequest
- name: CreateAudienceRequest
  property_count: 3
  slug: contentstack-createaudiencerequest
- name: CreateBrandKitRequest
  property_count: 2
  slug: contentstack-createbrandkitrequest
- name: CreateContentTypeRequest
  property_count: 1
  slug: contentstack-createcontenttyperequest
- name: CreateDeploymentRequest
  property_count: 2
  slug: contentstack-createdeploymentrequest
- name: CreateEntryRequest
  property_count: 1
  slug: contentstack-createentryrequest
- name: CreateEnvironmentRequest
  property_count: 2
  slug: contentstack-createenvironmentrequest
- name: CreateEventRequest
  property_count: 2
  slug: contentstack-createeventrequest
- name: CreateExperienceRequest
  property_count: 3
  slug: contentstack-createexperiencerequest
- name: CreateLlmConfigRequest
  property_count: 4
  slug: contentstack-createllmconfigrequest
- name: CreateProjectRequest
  property_count: 2
  slug: contentstack-createprojectrequest
- name: CreateStackRequest
  property_count: 1
  slug: contentstack-createstackrequest
- name: CreateVariableRequest
  property_count: 4
  slug: contentstack-createvariablerequest
- name: CreateVoiceProfileRequest
  property_count: 4
  slug: contentstack-createvoiceprofilerequest
- name: DeleteResponse
  property_count: 1
  slug: contentstack-deleteresponse
- name: Deployment
  property_count: 4
  slug: contentstack-deployment
- name: DeploymentList
  property_count: 1
  slug: contentstack-deploymentlist
- name: Contentstack Entry
  property_count: 14
  slug: contentstack-entry
- name: EntryList
  property_count: 2
  slug: contentstack-entrylist
- name: EntryVariant
  property_count: 3
  slug: contentstack-entryvariant
- name: EntryVariantList
  property_count: 1
  slug: contentstack-entryvariantlist
- name: Environment
  property_count: 4
  slug: contentstack-environment
- name: EnvironmentList
  property_count: 1
  slug: contentstack-environmentlist
- name: Error
  property_count: 2
  slug: contentstack-error
- name: EventList
  property_count: 1
  slug: contentstack-eventlist
- name: ExecutionLog
  property_count: 6
  slug: contentstack-executionlog
- name: ExecutionLogList
  property_count: 1
  slug: contentstack-executionloglist
- name: Experience
  property_count: 6
  slug: contentstack-experience
- name: ExperienceList
  property_count: 1
  slug: contentstack-experiencelist
- name: ExperiencePriority
  property_count: 1
  slug: contentstack-experiencepriority
- name: ExperienceVariant
  property_count: 4
  slug: contentstack-experiencevariant
- name: Field
  property_count: 5
  slug: contentstack-field
- name: GenAIRequest
  property_count: 3
  slug: contentstack-genairequest
- name: GenAIResponse
  property_count: 2
  slug: contentstack-genairesponse
- name: GeoItem
  property_count: 3
  slug: contentstack-geoitem
- name: GeoList
  property_count: 1
  slug: contentstack-geolist
- name: GlobalField
  property_count: 5
  slug: contentstack-globalfield
- name: GlobalFieldList
  property_count: 1
  slug: contentstack-globalfieldlist
- name: IngestContentRequest
  property_count: 3
  slug: contentstack-ingestcontentrequest
- name: JobData
  property_count: 4
  slug: contentstack-jobdata
- name: JobResponse
  property_count: 2
  slug: contentstack-jobresponse
- name: KnowledgeVaultResponse
  property_count: 3
  slug: contentstack-knowledgevaultresponse
- name: LlmConfig
  property_count: 4
  slug: contentstack-llmconfig
- name: LogEntry
  property_count: 3
  slug: contentstack-logentry
- name: LoginRequest
  property_count: 1
  slug: contentstack-loginrequest
- name: LoginResponse
  property_count: 1
  slug: contentstack-loginresponse
- name: LogResponse
  property_count: 1
  slug: contentstack-logresponse
- name: Manifest
  property_count: 1
  slug: contentstack-manifest
- name: ManifestExperience
  property_count: 4
  slug: contentstack-manifestexperience
- name: MergeUserAttributesRequest
  property_count: 2
  slug: contentstack-mergeuserattributesrequest
- name: Organization
  property_count: 4
  slug: contentstack-organization
- name: OrganizationList
  property_count: 1
  slug: contentstack-organizationlist
- name: PersonalizeEvent
  property_count: 4
  slug: contentstack-personalizeevent
- name: Project
  property_count: 6
  slug: contentstack-project
- name: ProjectList
  property_count: 1
  slug: contentstack-projectlist
- name: PublishRequest
  property_count: 1
  slug: contentstack-publishrequest
- name: ScimError
  property_count: 3
  slug: contentstack-scimerror
- name: ScimGroup
  property_count: 4
  slug: contentstack-scimgroup
- name: ScimListResponse
  property_count: 5
  slug: contentstack-scimlistresponse
- name: ScimPatchOperation
  property_count: 3
  slug: contentstack-scimpatchoperation
- name: ScimPatchRequest
  property_count: 2
  slug: contentstack-scimpatchrequest
- name: ScimUser
  property_count: 6
  slug: contentstack-scimuser
- name: Contentstack Stack
  property_count: 12
  slug: contentstack-stack
- name: StackList
  property_count: 1
  slug: contentstack-stacklist
- name: SyncItem
  property_count: 4
  slug: contentstack-syncitem
- name: SyncResponse
  property_count: 6
  slug: contentstack-syncresponse
- name: TokenUsage
  property_count: 3
  slug: contentstack-tokenusage
- name: TrackEvent
  property_count: 3
  slug: contentstack-trackevent
- name: TrackEventsRequest
  property_count: 0
  slug: contentstack-trackeventsrequest
- name: UpdateEntryRequest
  property_count: 1
  slug: contentstack-updateentryrequest
- name: UpdateStackRequest
  property_count: 1
  slug: contentstack-updatestackrequest
- name: UpdateUserRequest
  property_count: 1
  slug: contentstack-updateuserrequest
- name: UploadUrlResponse
  property_count: 3
  slug: contentstack-uploadurlresponse
- name: UsageAnalyticsRequest
  property_count: 0
  slug: contentstack-usageanalyticsrequest
- name: User
  property_count: 6
  slug: contentstack-user
- name: UserAttributesRequest
  property_count: 0
  slug: contentstack-userattributesrequest
- name: Variable
  property_count: 5
  slug: contentstack-variable
- name: VariableList
  property_count: 1
  slug: contentstack-variablelist
- name: VoiceProfile
  property_count: 7
  slug: contentstack-voiceprofile
- name: VoiceProfileList
  property_count: 1
  slug: contentstack-voiceprofilelist
- name: Contentstack Webhook Payload
  property_count: 6
  slug: contentstack-webhook-payload
json_structures:
- name: Contentstack Structure
  property_count: 0
  slug: contentstack-structure
jsonld:
- class_count: 0
  name: Contentstack Context
  property_count: 13
  slug: contentstack-context
layout: provider
modified: '2026-05-19'
name: Contentstack
nav: Providers
network: true
overview: 'Contentstack publishes 33 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Accounts API, Assets API, and 30 more.


  The Contentstack catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Contentstack''s developer surface includes authentication and 13 more developer resources.'
plans:
- name: Contentstack Plans Pricing
  plan_count: 3
  slug: contentstack-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Contentstack Rate Limits
  slug: contentstack-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Contentstack API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: contentstack-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Contentstack API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: contentstack-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Contentstack API Rules
  rule_count: 8
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 3
  slug: contentstack-rules
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 53.5
    catalog_earned_first_party: 0.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 28.8
    contract_quality: 76.0
    developer_ergonomics: 21.4
    discoverability: 50.0
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 43
  regulatory:
    note: provider declares no identity tags; regime could not be determined
    undetermined: true
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/contentstack/refs/heads/main/screenshots/contentstack-2026-06-20T174935.png
security:
- kind: authentication
  name: Contentstack Authentication
  slug: contentstack-authentication
  summary_line: apiKey/http · 5 schemes
- kind: domain-security
  name: Contentstack Domain Security
  slug: contentstack-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Contentstack Trust Center
  slug: contentstack-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: contentstack
---
