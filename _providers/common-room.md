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
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 58.7
  scored_at: '2026-09-05'
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
  slug: common-room-scim-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: The Activities API from Common Room — 7 operation(s) for activities.
  name: Common Room Activities API
  slug: common-room-activities-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: The Contacts API from Common Room — 6 operation(s) for contacts.
  name: Common Room Contacts API
  slug: common-room-contacts-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: Operations related to custom field definitions
  name: Common Room Custom Fields API
  slug: common-room-custom-fields-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: Notify Common Room that data is available for import
  name: Common Room Data Available API
  slug: common-room-data-available-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: Operations related to NAICS industry codes
  name: Common Room Industries API
  slug: common-room-industries-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: Operations related to lead score definitions
  name: Common Room Lead Scores API
  slug: common-room-lead-scores-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: Operations related to location data
  name: Common Room Locations API
  slug: common-room-locations-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: Information about the authenticated user
  name: Common Room Me API
  slug: common-room-me-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: Operations related to custom object type definitions
  name: Common Room Object Types API
  slug: common-room-object-types-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: Operations related to custom objects
  name: Common Room Objects API
  slug: common-room-objects-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: Operations related to organization management
  name: Common Room Organizations API
  slug: common-room-organizations-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: Operations related to prospector company discovery
  name: Common Room Prospector Companies API
  slug: common-room-prospector-companies-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: Operations related to prospector contact discovery
  name: Common Room Prospector Contacts API
  slug: common-room-prospector-contacts-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: Operations related to signal sources (integrations)
  name: Common Room Providers API
  slug: common-room-providers-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: The Right to be Forgotten API from Common Room — 1 operation(s) for right to be forgotten.
  name: Common Room Right to be Forgotten API
  slug: common-room-right-to-be-forgotten-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: The SCIM API from Common Room — 2 operation(s) for scim.
  name: Common Room SCIM API
  slug: common-room-scim-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: The Segments API from Common Room — 3 operation(s) for segments.
  name: Common Room Segments API
  slug: common-room-segments-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: The Tags API from Common Room — 2 operation(s) for tags.
  name: Common Room Tags API
  slug: common-room-tags-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: Operations related to technographics and tech stack products
  name: Common Room Tech Stack Products API
  slug: common-room-tech-stack-products-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: The Token Status API from Common Room — 1 operation(s) for token status.
  name: Common Room Token Status API
  slug: common-room-token-status-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: Operations related to topics
  name: Common Room Topics API
  slug: common-room-topics-api
- baseURL: https://api.commonroom.io
  baseurl_source: declared
  description: Operations related to website visit tracking
  name: Common Room Website Visits API
  slug: common-room-website-visits-api
artifact_total: 138
asyncapis:
- description: ''
  name: Common Room Webhooks
  slug: common-room-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/common-room-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/common-room-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/common-room-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/common-room-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/common-room-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/common-room-finops.yml
- group: build
  title: ''
  type: Packages
  url: packages/common-room-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/common-room-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/common-room-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/common-room-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/common-room-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/common-room-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/common-room-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/common-room-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.commonroom.io/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/common-room-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.commonroom.io/security/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/common-room-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/common-room-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/common-room-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/common-room-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/common-room-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/common-room-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/common-room-components.yml
- group: design
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
- name: Common Room Finops
  service_category: ''
  slug: common-room-finops
graphqls:
- description: Common Room is a community intelligence and go-to-market (GTM) platform that aggregates member signals across GitHub, Slack, Discord, LinkedIn, Twitter, and other channels. This conceptual GraphQL sch
  name: Common Room GraphQL Schema
  slug: common-room-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/common-room.png
json_schemas:
- name: ApiActivity
  property_count: 10
  slug: common-room-core-apiactivity
- name: ApiCustomFields
  property_count: 2
  slug: common-room-core-apicustomfields
- name: ApiTag
  property_count: 0
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
  property_count: 0
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
- description: ''
  name: Common Room MCP Server
  slug: common-room-mcp-server
modified: '2026-08-13'
name: Common Room
nav: Providers
network: true
overview: 'Common Room publishes 23 APIs on the [APIs.io](https://apis.io/) network, including SCIM API, Activities API, Contacts API, and 20 more. Tagged areas include Community Intelligence, Go-To-Market, Member Signals, GitHub, and Slack.


  The Common Room catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Common Room''s developer surface includes authentication, documentation, engineering blog, pricing, CLI, API reference, getting-started guide, and 36 more developer resources.'
plans:
- name: Common Room Plans Pricing
  plan_count: 3
  slug: common-room-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Common Room Rate Limits
  slug: common-room-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Common Room API Rules
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
  band: strong
  composite: 64.9
  coverage:
    artifact_dirs: 31
    catalog_earned: 69.3
    catalog_earned_first_party: 12.0
    catalog_gap: 45.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 93.4
    commercial_clarity: 93.4
    contract_governance: 28.0
    contract_quality: 73.5
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 28.0
    operational_transparency: 23.7
  previous_composite: 64.9
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
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/common-room/refs/heads/main/screenshots/common-room-2026-06-20T174819.png
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
website: https://www.commonroom.io/
---
