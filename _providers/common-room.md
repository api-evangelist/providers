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
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 53.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Common Room Agentic Access
  operation_count: 54
  slug: common-room-agentic-access
  summary_line: 54 operations · 11 acting
api_count: 23
apis:
- description: SCIM REST API for accessing community-scoped resources and managing user provisioning and deprovisioning.
  name: Common Room SCIM API
  slug: common-room-scim-api
- description: The Activities API from Common Room — 7 operation(s) for activities.
  name: Common Room Activities API
  slug: common-room-activities-api
- description: The Contacts API from Common Room — 6 operation(s) for contacts.
  name: Common Room Contacts API
  slug: common-room-contacts-api
- description: Operations related to custom field definitions
  name: Common Room Custom Fields API
  slug: common-room-custom-fields-api
- description: Notify Common Room that data is available for import
  name: Common Room Data Available API
  slug: common-room-data-available-api
- description: Operations related to NAICS industry codes
  name: Common Room Industries API
  slug: common-room-industries-api
- description: Operations related to lead score definitions
  name: Common Room Lead Scores API
  slug: common-room-lead-scores-api
- description: Operations related to location data
  name: Common Room Locations API
  slug: common-room-locations-api
- description: Information about the authenticated user
  name: Common Room Me API
  slug: common-room-me-api
- description: Operations related to custom object type definitions
  name: Common Room Object Types API
  slug: common-room-object-types-api
- description: Operations related to custom objects
  name: Common Room Objects API
  slug: common-room-objects-api
- description: Operations related to organization management
  name: Common Room Organizations API
  slug: common-room-organizations-api
- description: Operations related to prospector company discovery
  name: Common Room Prospector Companies API
  slug: common-room-prospector-companies-api
- description: Operations related to prospector contact discovery
  name: Common Room Prospector Contacts API
  slug: common-room-prospector-contacts-api
- description: Operations related to signal sources (integrations)
  name: Common Room Providers API
  slug: common-room-providers-api
- description: The Right to be Forgotten API from Common Room — 1 operation(s) for right to be forgotten.
  name: Common Room Right to be Forgotten API
  slug: common-room-right-to-be-forgotten-api
- description: The SCIM API from Common Room — 2 operation(s) for scim.
  name: Common Room SCIM API
  slug: common-room-scim-api
- description: The Segments API from Common Room — 3 operation(s) for segments.
  name: Common Room Segments API
  slug: common-room-segments-api
- description: The Tags API from Common Room — 2 operation(s) for tags.
  name: Common Room Tags API
  slug: common-room-tags-api
- description: Operations related to technographics and tech stack products
  name: Common Room Tech Stack Products API
  slug: common-room-tech-stack-products-api
- description: The Token Status API from Common Room — 1 operation(s) for token status.
  name: Common Room Token Status API
  slug: common-room-token-status-api
- description: Operations related to topics
  name: Common Room Topics API
  slug: common-room-topics-api
- description: Operations related to website visit tracking
  name: Common Room Website Visits API
  slug: common-room-website-visits-api
artifact_total: 111
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
created: '2026-06-13'
description: Common Room is a community intelligence platform with a REST API for tracking member signals across GitHub, Slack, Discord, LinkedIn, and social platforms, managing segments, and automating outreach for go-to-market teams.
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
modified: '2026-06-13'
name: Common Room
nav: Providers
network: true
overview: 'Common Room publishes 23 APIs on the [APIs.io](https://apis.io/) network, including SCIM API, Activities API, Contacts API, and 20 more. Tagged areas include Community Intelligence, Go-to-Market, Member Signals, GitHub, and Slack.


  The Common Room catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Common Room''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Common Room Plans Pricing
  plan_count: 3
  slug: common-room-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 0
  name: Common Room Rate Limits
  slug: common-room-rate-limits
rules:
- name: Common Room API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: common-room-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 61.5
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 13.2
  previous_composite: 50.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/common-room/refs/heads/main/screenshots/common-room-2026-06-20T174819.png
security:
- kind: authentication
  name: Common Room Authentication
  slug: common-room-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Common Room Domain Security
  slug: common-room-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Common Room Vulnerability Disclosure
  slug: common-room-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: common-room
tags:
- Community Intelligence
- Go-to-Market
- Member Signals
- GitHub
- Slack
- Discord
- LinkedIn
- Sales Intelligence
- Contact Management
- Webhooks
website: https://www.commonroom.io/
---
