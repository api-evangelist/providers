---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 64.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Common Room Agentic Access
  operation_count: 54
  slug: common-room-agentic-access
  summary_line: 54 operations · 11 acting
api_count: 3
apis:
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: SCIM REST API for accessing community-scoped resources and managing user provisioning and deprovisioning.
  name: Common Room SCIM API
  phrasing_intents:
  - id: getUsers
    intent: List active owner accounts via SCIM
    question: Which active owners are provisioned in our community through SCIM?
  - id: postUsers
    intent: Provision a new owner account via SCIM
    question: How do I provision a new owner in our community from our identity provider?
  - id: getUsersByEmail
    intent: Get a SCIM user account by email
    question: Can I retrieve one provisioned SCIM account by its email?
  - id: patchUsersByEmail
    intent: Update a SCIM user account
    question: How do I deactivate or change a provisioned user through SCIM?
  phrasing_ops: 4
  slug: common-room-scim-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: The Activities API from Common Room — 7 operation(s) for activities.
  name: Common Room Activities API
  phrasing_intents:
  - id: addUpdateActivityToSource
    intent: Add or update an activity in an API signal source
    question: How do I push activity from my own system into Common Room?
  - id: getActivityTypes
    intent: List the accepted activity types
    question: What activity types are accepted when sending activity?
  - id: getActivitiesById
    intent: Get one activity by its ID
    question: Can I pull up a single activity if I know its a_ ID?
  - id: getActivities
    intent: List activities with filters and paging
    question: How do I page through all the activity recorded in our community?
  - id: getActivityTypes
    intent: List activity type IDs with display names
    question: What human-readable name goes with each activity type ID returned on activities?
  - id: getActivityCategories
    intent: List the community's activity categories
    question: What category labels are used to group activities in our community?
  - id: getActivitySentiment
    intent: List activity sentiment labels
    question: What sentiment classifications does Common Room apply to activity?
  phrasing_ops: 7
  slug: common-room-activities-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: The Contacts API from Common Room — 6 operation(s) for contacts.
  name: Common Room Contacts API
  phrasing_intents:
  - id: addUpdateUserToSource
    intent: Add or update a user in an API signal source
    question: How do I add a person from my own system into Common Room as a contact?
  - id: getMembersCustomFields
    intent: List contact custom fields for a room
    question: What custom fields are defined on contacts in our room?
  - id: getUserByEmail
    intent: Look up a contact's profile by email
    question: How do I find a contact's full profile when all I have is their email address?
  - id: deleteUserByEmail
    intent: Request anonymization of a contact by email
    question: How do I remove a contact's personal data when they ask to be forgotten?
  - id: getMembers
    intent: Find a contact by email or social handle
    question: Can I find a contact by their GitHub, Twitter or LinkedIn handle?
  - id: getContactsById
    intent: Get a contact by its ID
    question: How do I fetch one contact when I have its c_ ID?
  - id: getContacts
    intent: List contacts with filters and paging
    question: What's the way to page through every contact in our community?
  phrasing_ops: 7
  slug: common-room-contacts-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: Operations related to custom field definitions
  name: Common Room Custom Fields API
  phrasing_intents:
  - id: getCustomFieldsById
    intent: Get a custom field definition by ID
    question: Can I look up what a specific cf_ custom field is and how it's defined?
  - id: getCustomFields
    intent: List custom field definitions
    question: What custom fields have we defined across the community?
  phrasing_ops: 2
  slug: common-room-custom-fields-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: Notify Common Room that data is available for import
  name: Common Room Data Available API
  phrasing_intents:
  - id: postDataAvailable
    intent: Signal that new source data is ready to import
    question: How do I tell Common Room that a connected source has new data to import?
  phrasing_ops: 1
  slug: common-room-data-available-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: Operations related to NAICS industry codes
  name: Common Room Industries API
  phrasing_intents:
  - id: getIndustries
    intent: Search NAICS industry codes
    question: Which NAICS industry codes does Common Room recognize?
  phrasing_ops: 1
  slug: common-room-industries-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: Operations related to lead score definitions
  name: Common Room Lead Scores API
  phrasing_intents:
  - id: getLeadScoresById
    intent: Get a lead score definition by ID
    question: Can I see how one specific ls_ lead score is defined?
  - id: getLeadScores
    intent: List all lead score definitions
    question: What lead scores have we defined in our community?
  phrasing_ops: 2
  slug: common-room-lead-scores-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: Operations related to location data
  name: Common Room Locations API
  phrasing_intents:
  - id: getLocationsById
    intent: Get a location by ID
    question: Can I fetch the details of one location from its ID?
  - id: getLocations
    intent: List locations ranked by member count
    question: Where are most of our community members located?
  phrasing_ops: 2
  slug: common-room-locations-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: Information about the authenticated user
  name: Common Room Me API
  phrasing_intents:
  - id: getMe
    intent: Get the authenticated user's profile
    question: Which Common Room user am I authenticated as?
  phrasing_ops: 1
  slug: common-room-me-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: Operations related to custom object type definitions
  name: Common Room Object Types API
  phrasing_intents:
  - id: getObjectTypes
    intent: List custom object type definitions
    question: What custom object types have we defined in our community?
  phrasing_ops: 1
  slug: common-room-object-types-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: Operations related to custom objects
  name: Common Room Objects API
  phrasing_intents:
  - id: getObjectsById
    intent: Get a custom object by ID
    question: Can I fetch one custom object record from its co_ ID?
  - id: getObjects
    intent: List custom objects of a given type
    question: What records exist for one of our custom object types?
  phrasing_ops: 2
  slug: common-room-objects-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: Operations related to organization management
  name: Common Room Organizations API
  phrasing_intents:
  - id: getOrganizationsById
    intent: Get an organization by ID
    question: Can I pull up one organization's record from its o_ ID?
  - id: getOrganizations
    intent: List or filter organizations
    question: What organizations are in our community, sorted by member count?
  phrasing_ops: 2
  slug: common-room-organizations-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: Operations related to prospector company discovery
  name: Common Room Prospector Companies API
  phrasing_intents:
  - id: getProspectorCompanies
    intent: List companies discovered by Prospector
    question: Which companies has Prospector discovered for us?
  phrasing_ops: 1
  slug: common-room-prospector-companies-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: Operations related to prospector contact discovery
  name: Common Room Prospector Contacts API
  phrasing_intents:
  - id: getProspectorContacts
    intent: List contacts discovered by Prospector
    question: Which people has Prospector surfaced as potential leads?
  phrasing_ops: 1
  slug: common-room-prospector-contacts-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: Operations related to signal sources (integrations)
  name: Common Room Providers API
  phrasing_intents:
  - id: getProviders
    intent: List the community's signal sources
    question: Which integrations and signal sources are connected to our community?
  phrasing_ops: 1
  slug: common-room-providers-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: The Right to be Forgotten API from Common Room — 1 operation(s) for right to be forgotten.
  name: Common Room Right to be Forgotten API
  phrasing_intents:
  - id: deleteUserByEmail
    intent: Request anonymization of a contact by email
    question: How do I honor a right-to-be-forgotten request for a contact?
  phrasing_ops: 1
  slug: common-room-right-to-be-forgotten-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: The SCIM API from Common Room — 2 operation(s) for scim.
  name: Common Room SCIM API
  phrasing_intents:
  - id: getUsers
    intent: List active owner accounts via SCIM
    question: Which active owners are provisioned in our community through SCIM?
  - id: postUsers
    intent: Provision a new owner account via SCIM
    question: How do I provision a new owner in our community from our identity provider?
  - id: getUsersByEmail
    intent: Get a SCIM user account by email
    question: Can I retrieve one provisioned SCIM account by its email?
  - id: patchUsersByEmail
    intent: Update a SCIM user account
    question: How do I deactivate or change a provisioned user through SCIM?
  phrasing_ops: 4
  slug: common-room-scim-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: The Segments API from Common Room — 3 operation(s) for segments.
  name: Common Room Segments API
  phrasing_intents:
  - id: getSegments
    intent: List all segments in a room
    question: What segments exist in our Common Room room?
  - id: postSegments
    intent: Create a new segment
    question: How do I create a new segment in our community?
  - id: getSegmentStatuses
    intent: List the statuses available in a segment
    question: Which statuses can contacts have inside a particular segment?
  - id: addContactsToSegment
    intent: Add existing contacts to a segment
    question: How do I add contacts to a segment using their email addresses?
  - id: getSegmentsById
    intent: Get one segment by its ID
    question: Can I look up a single segment's details from its s_ ID?
  phrasing_ops: 5
  slug: common-room-segments-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: The Tags API from Common Room — 2 operation(s) for tags.
  name: Common Room Tags API
  phrasing_intents:
  - id: listTags
    intent: List all user-defined tags
    question: What tags have we defined in our Common Room workspace?
  - id: createTag
    intent: Create a new tag
    question: How do I create a new tag for labeling contacts?
  - id: getTag
    intent: Look up a single tag by ID
    question: Which name and description belong to a specific tag ID?
  - id: updateTag
    intent: Rename or redescribe an existing tag
    question: How do I rename a tag that already exists?
  - id: deleteTag
    intent: Delete a tag everywhere it is used
    question: Will deleting a tag remove it from every contact and activity it was added to?
  phrasing_ops: 5
  slug: common-room-tags-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: Operations related to technographics and tech stack products
  name: Common Room Tech Stack Products API
  phrasing_intents:
  - id: getTechStackProducts
    intent: Search technographic products
    question: Which tech stack products does Common Room track for technographics?
  phrasing_ops: 1
  slug: common-room-tech-stack-products-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: The Token Status API from Common Room — 1 operation(s) for token status.
  name: Common Room Token Status API
  phrasing_intents:
  - id: getApiTokenStatus
    intent: Check the status of the current API token
    question: Is the API token I'm using still valid?
  phrasing_ops: 1
  slug: common-room-token-status-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: Operations related to topics
  name: Common Room Topics API
  phrasing_intents:
  - id: getTopicsById
    intent: Get a topic by ID
    question: Can I look up one topic from its tp_ ID?
  - id: getTopics
    intent: List topics alphabetically
    question: What topics are being tracked in our community?
  phrasing_ops: 2
  slug: common-room-topics-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: Operations related to website visit tracking
  name: Common Room Website Visits API
  phrasing_intents:
  - id: getWebsiteVisits
    intent: List website visits
    question: Which pages on our website have people been visiting?
  phrasing_ops: 1
  slug: common-room-website-visits-api
artifact_total: 141
asyncapis:
- description: ''
  name: Common Room Webhooks
  slug: common-room-webhooks
collections:
- collection_type: open
  name: Common Room Core Activities API
  slug: open-common-room-activities-api
- collection_type: open
  name: Common Room Core Activities Contacts API
  slug: open-common-room-contacts-api
- collection_type: open
  name: Common Room Core Activities Custom Fields API
  slug: open-common-room-custom-fields-api
- collection_type: open
  name: Common Room Core Activities Data Available API
  slug: open-common-room-data-available-api
- collection_type: open
  name: Common Room Core Activities Industries API
  slug: open-common-room-industries-api
- collection_type: open
  name: Common Room Core Activities Lead Scores API
  slug: open-common-room-lead-scores-api
- collection_type: open
  name: Common Room Core Activities Locations API
  slug: open-common-room-locations-api
- collection_type: open
  name: Common Room Core Activities Me API
  slug: open-common-room-me-api
- collection_type: open
  name: Common Room Core Activities Object Types API
  slug: open-common-room-object-types-api
- collection_type: open
  name: Common Room Core Activities Objects API
  slug: open-common-room-objects-api
- collection_type: open
  name: Common Room Core Activities Organizations API
  slug: open-common-room-organizations-api
- collection_type: open
  name: Common Room Core Activities Prospector Companies API
  slug: open-common-room-prospector-companies-api
- collection_type: open
  name: Common Room Core Activities Prospector Contacts API
  slug: open-common-room-prospector-contacts-api
- collection_type: open
  name: Common Room Core Activities Providers API
  slug: open-common-room-providers-api
- collection_type: open
  name: Common Room Core Activities Right to be Forgotten API
  slug: open-common-room-right-to-be-forgotten-api
- collection_type: open
  name: Common Room Core Activities SCIM API
  slug: open-common-room-scim-api
- collection_type: open
  name: Common Room Core Activities Segments API
  slug: open-common-room-segments-api
- collection_type: open
  name: Common Room Core Activities Tags API
  slug: open-common-room-tags-api
- collection_type: open
  name: Common Room Core Activities Tech Stack Products API
  slug: open-common-room-tech-stack-products-api
- collection_type: open
  name: Common Room Core Activities Token Status API
  slug: open-common-room-token-status-api
- collection_type: open
  name: Common Room Core Activities Topics API
  slug: open-common-room-topics-api
- collection_type: open
  name: Common Room Core Activities Website Visits API
  slug: open-common-room-website-visits-api
common:
- group: other
  href: https://artifacts.apis.io/common-room/capabilities/common-room-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/common-room-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/common-room/agentic-access/common-room-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/common-room-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/common-room/security/common-room-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/common-room-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/common-room/security/common-room-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/common-room-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/common-room/authentication/common-room-authentication.yml
  title: ''
  type: Authentication
  url: authentication/common-room-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.commonroom.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.commonroom.io/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/common-room
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/common-room-hq
- group: company
  title: ''
  type: Blog
  url: https://www.commonroom.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.commonroom.io/pricing/
- group: other
  title: ''
  type: X
  url: https://twitter.com/commonroomhq
- group: design
  title: ''
  type: Webhooks
  url: https://www.commonroom.io/docs/set-preferences/webhooks/
- group: auth
  title: ''
  type: Authentication
  url: https://www.commonroom.io/docs/set-preferences/api-tokens/
- group: commercial
  href: https://artifacts.apis.io/common-room/plans/common-room-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/common-room-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/common-room/rate-limits/common-room-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/common-room-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/common-room/finops/common-room-finops.yml
  title: ''
  type: FinOps
  url: finops/common-room-finops.yml
- group: build
  href: https://artifacts.apis.io/common-room/packages/common-room-packages.yml
  title: ''
  type: Packages
  url: packages/common-room-packages.yml
- group: build
  href: https://artifacts.apis.io/common-room/cli/common-room-cli.yml
  title: ''
  type: CLI
  url: cli/common-room-cli.yml
- group: agent
  href: https://artifacts.apis.io/common-room/well-known/common-room-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/common-room-well-known.yml
- group: auth
  href: https://artifacts.apis.io/common-room/well-known/common-room-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/common-room-security.txt
- group: agent
  href: https://artifacts.apis.io/common-room/mcp/common-room-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/common-room-mcp.yml
- group: build
  href: https://artifacts.apis.io/common-room/mcp/common-room-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/common-room-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/common-room/llms/common-room-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/common-room-llms.txt
- group: agent
  href: https://artifacts.apis.io/common-room/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/common-room/conformance/common-room-conformance.yml
  title: ''
  type: Conformance
  url: conformance/common-room-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.commonroom.io/security/
- group: auth
  href: https://artifacts.apis.io/common-room/security/common-room-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/common-room-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.commonroom.io/security/
- group: design
  href: https://artifacts.apis.io/common-room/errors/common-room-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/common-room-problem-types.yml
- group: design
  href: https://artifacts.apis.io/common-room/lifecycle/common-room-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/common-room-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/common-room/scopes/common-room-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/common-room-scopes.yml
- group: design
  href: https://artifacts.apis.io/common-room/conventions/common-room-conventions.yml
  title: ''
  type: Conventions
  url: conventions/common-room-conventions.yml
- group: design
  href: https://artifacts.apis.io/common-room/conventions/common-room-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/common-room-conventions.yml
- group: design
  href: https://artifacts.apis.io/common-room/data-model/common-room-data-model.yml
  title: ''
  type: DataModel
  url: data-model/common-room-data-model.yml
- group: design
  href: https://artifacts.apis.io/common-room/components/common-room-components.yml
  title: ''
  type: Components
  url: components/common-room-components.yml
- group: design
  href: https://artifacts.apis.io/common-room/asyncapi/common-room-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/common-room-webhooks.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.commonroom.io/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://api.commonroom.io/docs/api-v2.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.commonroom.io/docs/get-started/
- group: operate
  title: ''
  type: Support
  url: https://www.commonroom.io/docs/get-started/contacting-common-room-support/
- group: start
  title: ''
  type: Login
  url: https://app.commonroom.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.commonroom.io/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.commonroom.io/privacy-policy/
created: '2026-06-13'
description: Common Room is an AI-native go-to-market and buyer-intelligence platform that unifies first-party product, community, social, web and CRM signals into a single identity-resolved view of contacts and organizations. It exposes a v1 Core REST API for ingesting contacts and activity from your own sources, a v2 REST API for reading contacts, organizations, activities, segments, lead scores, custom objects, website visits and Prospector data, a SCIM 2.0 API for provisioning, a webhook surface driven by workflow rules, a hosted OAuth 2.1 MCP server at mcp.commonroom.io for AI clients, and a first-party `cr` CLI for scripted and agent-driven access.
examples:
- key_count: 6
  name: Common Room Examples
  slug: common-room-examples
finops:
- has_sources: true
  method: derived
  name: Common Room Finops
  primary_unit: subscription
  service_category: ''
  slug: common-room-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/common-room.png
json_schemas:
- name: ApiActivity
  property_count: 10
  slug: common-room-core-apiactivity
- name: ApiCustomFields
  property_count: 2
  slug: common-room-core-apicustomfields
- name: ApiTag
  property_count: 3
  slug: common-room-core-apitag
- name: ApiTagAssignment
  property_count: 0
  slug: common-room-core-apitagassignment
- name: ApiTagAssignmentById
  property_count: 2
  slug: common-room-core-apitagassignmentbyid
- name: ApiTagAssignmentByName
  property_count: 2
  slug: common-room-core-apitagassignmentbyname
- name: ApiTagCreationProperties
  property_count: 1
  slug: common-room-core-apitagcreationproperties
- name: ApiTagUpdateProperties
  property_count: 2
  slug: common-room-core-apitagupdateproperties
- name: ApiToken
  property_count: 3
  slug: common-room-core-apitoken
- name: ApiUser
  property_count: 23
  slug: common-room-core-apiuser
- name: CommunityMember
  property_count: 0
  slug: common-room-core-communitymember
- name: MarkdownContent
  property_count: 2
  slug: common-room-core-markdowncontent
- name: Status
  property_count: 3
  slug: common-room-core-status
- name: TextContent
  property_count: 2
  slug: common-room-core-textcontent
- name: User
  property_count: 6
  slug: common-room-scim-user
- name: ActivityCategoryList
  property_count: 2
  slug: common-room-v2-activitycategorylist
- name: ActivityList
  property_count: 3
  slug: common-room-v2-activitylist
- name: ActivityResponse
  property_count: 2
  slug: common-room-v2-activityresponse
- name: ActivitySentimentList
  property_count: 2
  slug: common-room-v2-activitysentimentlist
- name: ActivityTypeList
  property_count: 2
  slug: common-room-v2-activitytypelist
- name: ApiActivity
  property_count: 13
  slug: common-room-v2-apiactivity
- name: ApiActivityCategory
  property_count: 3
  slug: common-room-v2-apiactivitycategory
- name: ApiActivitySentiment
  property_count: 2
  slug: common-room-v2-apiactivitysentiment
- name: ApiActivityType
  property_count: 2
  slug: common-room-v2-apiactivitytype
- name: ApiCustomField
  property_count: 10
  slug: common-room-v2-apicustomfield
- name: ApiCustomObject
  property_count: 4
  slug: common-room-v2-apicustomobject
- name: ApiFieldValue
  property_count: 0
  slug: common-room-v2-apifieldvalue
- name: ApiLeadScore
  property_count: 3
  slug: common-room-v2-apileadscore
- name: ApiLeadScoreDefinition
  property_count: 5
  slug: common-room-v2-apileadscoredefinition
- name: ApiLocation
  property_count: 3
  slug: common-room-v2-apilocation
- name: ApiLocationItem
  property_count: 6
  slug: common-room-v2-apilocationitem
- name: ApiNaicsCode
  property_count: 3
  slug: common-room-v2-apinaicscode
- name: ApiObjectType
  property_count: 3
  slug: common-room-v2-apiobjecttype
- name: ApiObjectTypeAssoc
  property_count: 3
  slug: common-room-v2-apiobjecttypeassoc
- name: ApiProspectorCompany
  property_count: 12
  slug: common-room-v2-apiprospectorcompany
- name: ApiProspectorCompanyLocation
  property_count: 5
  slug: common-room-v2-apiprospectorcompanylocation
- name: ApiProspectorContact
  property_count: 13
  slug: common-room-v2-apiprospectorcontact
- name: ApiProvider
  property_count: 3
  slug: common-room-v2-apiprovider
- name: ApiSegment
  property_count: 5
  slug: common-room-v2-apisegment
- name: ApiTag
  property_count: 4
  slug: common-room-v2-apitag
- name: ApiTechStackProduct
  property_count: 3
  slug: common-room-v2-apitechstackproduct
- name: ApiToken
  property_count: 3
  slug: common-room-v2-apitoken
- name: ApiTopic
  property_count: 2
  slug: common-room-v2-apitopic
- name: ApiV2Error
  property_count: 2
  slug: common-room-v2-apiv2error
- name: ApiV2ErrorResponse
  property_count: 2
  slug: common-room-v2-apiv2errorresponse
- name: ApiWebsiteVisit
  property_count: 5
  slug: common-room-v2-apiwebsitevisit
- name: Contact
  property_count: 24
  slug: common-room-v2-contact
- name: ContactList
  property_count: 3
  slug: common-room-v2-contactlist
- name: ContactResponse
  property_count: 2
  slug: common-room-v2-contactresponse
- name: CreateSegmentRequest
  property_count: 4
  slug: common-room-v2-createsegmentrequest
- name: CreateSegmentResponse
  property_count: 2
  slug: common-room-v2-createsegmentresponse
- name: CustomFieldList
  property_count: 2
  slug: common-room-v2-customfieldlist
- name: CustomFieldResponse
  property_count: 2
  slug: common-room-v2-customfieldresponse
- name: CustomObjectList
  property_count: 3
  slug: common-room-v2-customobjectlist
- name: CustomObjectResponse
  property_count: 2
  slug: common-room-v2-customobjectresponse
- name: LeadScoreDefinitionList
  property_count: 2
  slug: common-room-v2-leadscoredefinitionlist
- name: LeadScoreDefinitionResponse
  property_count: 2
  slug: common-room-v2-leadscoredefinitionresponse
- name: LocationItemList
  property_count: 3
  slug: common-room-v2-locationitemlist
- name: LocationItemResponse
  property_count: 2
  slug: common-room-v2-locationitemresponse
- name: MeResponse
  property_count: 2
  slug: common-room-v2-meresponse
- name: NaicsCodeList
  property_count: 3
  slug: common-room-v2-naicscodelist
- name: ObjectTypeList
  property_count: 2
  slug: common-room-v2-objecttypelist
- name: Organization
  property_count: 21
  slug: common-room-v2-organization
- name: OrganizationList
  property_count: 3
  slug: common-room-v2-organizationlist
- name: OrganizationResponse
  property_count: 2
  slug: common-room-v2-organizationresponse
- name: ProspectorCompanyList
  property_count: 3
  slug: common-room-v2-prospectorcompanylist
- name: ProspectorContactList
  property_count: 3
  slug: common-room-v2-prospectorcontactlist
- name: ProviderList
  property_count: 3
  slug: common-room-v2-providerlist
- name: SegmentList
  property_count: 3
  slug: common-room-v2-segmentlist
- name: SegmentResponse
  property_count: 2
  slug: common-room-v2-segmentresponse
- name: Status
  property_count: 3
  slug: common-room-v2-status
- name: TagList
  property_count: 3
  slug: common-room-v2-taglist
- name: TagResponse
  property_count: 2
  slug: common-room-v2-tagresponse
- name: TechStackProductList
  property_count: 3
  slug: common-room-v2-techstackproductlist
- name: TopicList
  property_count: 3
  slug: common-room-v2-topiclist
- name: TopicResponse
  property_count: 2
  slug: common-room-v2-topicresponse
- name: WebsiteVisitList
  property_count: 3
  slug: common-room-v2-websitevisitlist
jsonld:
- class_count: 18
  name: Common Room Context
  property_count: 32
  slug: common-room-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.commonroom.io over HTTP requiring OAuth; 5 tools listed.
  name: Common Room MCP Server
  slug: common-room
modified: '2026-08-13'
name: Common Room
nav: Providers
network: true
overview: 'Common Room publishes 23 API contracts indexed on the [APIs.io](https://apis.io/) network, including SCIM API, Activities API, Contacts API, and 20 more. Tagged areas include Community Intelligence, Go-To-Market, Member Signals, GitHub, and Slack.


  The Common Room catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Common Room''s developer surface includes authentication, documentation, engineering blog, pricing, CLI, API reference, getting-started guide, and 37 more developer resources.'
plans:
- name: Common Room Plans Pricing
  plan_count: 3
  slug: common-room-plans-pricing
- name: Common Room Price Estimates
  plan_count: 0
  slug: common-room-price-estimates
random_paper: 11
rate_limits:
- limit_count: 0
  name: Common Room Rate Limits
  slug: common-room-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Common Room — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: common-room-jsonschema-spectral-rules
scopes:
- name: Common Room Scopes
  scope_count: 4
  slug: common-room-scopes
  summary_line: 4 scopes · authorizationCode/deviceCode/refreshToken
score:
  band: exemplar
  composite: 67.3
  coverage:
    artifact_dirs: 35
    catalog_earned: 69.3
    catalog_earned_first_party: 12.0
    catalog_gap: 45.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 93.4
    contract_governance: 28.0
    contract_quality: 68.7
    developer_ergonomics: 66.1
    discoverability: 80.0
    operational_transparency: 23.7
  previous_composite: 67.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/common-room/common-room-2026-06-20T174819.png
security:
- kind: authentication
  name: Common Room Authentication
  slug: common-room-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Common Room Domain Security
  slug: common-room-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Common Room Vulnerability Disclosure
  slug: common-room-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Common Room Trust Center
  slug: common-room-trust-center
  summary_line: SOC 2 Type 2
skill_count: 4
skills:
- name: Common Room account research brief
  slug: common-room-account-research-brief
- name: Common Room build and populate a segment
  slug: common-room-build-a-segment
- name: Common Room ingest contacts and activity from your own source
  slug: common-room-ingest-contacts-and-activity
- name: Common Room right to be forgotten
  slug: common-room-right-to-be-forgotten
slug: common-room
tags:
- Community Intelligence
- Go-To-Market
- Member Signals
- GitHub
- Slack
- Discord
- LinkedIn
- Sales Intelligence
- Contact Management
- Webhook
- Buyer Intelligence
- MCP
- Agent Tooling
- CLI
- SCIM
- Signal Intelligence
- Community
website: https://www.commonroom.io/
---
