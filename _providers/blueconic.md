---
access_model:
  confidence: high
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 18
  human_in_the_loop: 1
  name: Blueconic Agentic Access
  operation_count: 64
  slug: blueconic-agentic-access
  summary_line: 64 operations · 18 acting · 1 human-in-the-loop
api_count: 28
apis:
- description: 'The Audit Event API allows users to connect BlueConic to a SIEM system. We recommend using this API to periodically receive security-related activities based on a rolling window. The API has a 30-day '
  name: BlueConic Audit Events API
  slug: blueconic-audit-events-api
- description: The Channel API allows you to retrieve information about [channels in BlueConic](https://support.blueconic.com/hc/en-us/articles/200472632-Overview-What-are-channels-in-BlueConic).
  name: BlueConic Channels API
  slug: blueconic-channels-api
- description: BlueConic Connections lets you connect with other systems to synchronize customer data. The following methods allow you to retrieve the connection configuration and run history. [Read more](https://su
  name: BlueConic Connections API
  slug: blueconic-connections-api
- description: A Dialogue is an online (personalized) conversation with a visitor to a channel. [Read more](https://support.blueconic.com/hc/en-us/articles/200456521-What-are-dialogues-)
  name: BlueConic Dialogues API
  slug: blueconic-dialogues-api
- description: Retrieve all types of groups, such as “Househould” or “Account”. Each group type has its own properties that can be used for segmentation. <a href="https://support.blueconic.com/hc/en-us/articles/3600
  name: BlueConic Group Types API
  slug: blueconic-group-types-api
- description: The following methods allow you to create, modify, retrieve, and delete BlueConic groups. To manage group properties, use the [Properties endpoints](https://rest.apidoc.blueconic.com/#tag--Properties)
  name: BlueConic Groups API
  slug: blueconic-groups-api
- description: Used to track an interaction (view, click, or conversion) with a BlueConic Dialogue. See [Tracking metrics for views, clicks, and conversions](https://support.blueconic.com/hc/en-us/articles/360020105
  name: BlueConic Interaction events API
  slug: blueconic-interaction-events-api
- description: Get the interactions (i.e. listeners and/or dialogues) that must be executed for a given profile that visits a certain web page (for web channels), a screen (on mobile or CTV channels) or a campaign I
  name: BlueConic Interactions API
  slug: blueconic-interactions-api
- description: The following methods allow you to retrieve information about lifecycles. See [Lifecycles](https://support.blueconic.com/en/articles/247909-lifecycles-overview).
  name: BlueConic Lifecycles API
  slug: blueconic-lifecycles-api
- description: Listeners add information about visitors to their profile, based on their online behavior or provided input. Use this endpoint to retrieve listener configuration. [Read more](https://support.blueconic
  name: BlueConic Listeners API
  slug: blueconic-listeners-api
- description: The following methods allow you to create, modify, retrieve, and delete machine learning Models in ONNX format. See [Models](https://support.blueconic.com/en/articles/307965-real-time-models).
  name: BlueConic Models API
  slug: blueconic-models-api
- description: The following methods allow you to retrieve AI Workbench notebooks and their run history. See [AI Workbench Overview](https://support.blueconic.com/en/articles/247838-ai-workbench-overview).
  name: BlueConic Notebooks API
  slug: blueconic-notebooks-api
- description: The OAuth 2.0 API allows external applications to be authenticated and authorized to access the public BlueConic API. The OAuth 2.0 specification is implemented according to [RFC 6749](https://www.rfc
  name: BlueConic OAuth 2.0 API
  slug: blueconic-oauth-2-0-api
- description: Objectives are used to group items needed for your marketing objectives. When consent is required, items in the objective only get access to profiles that have given consent to the objective. [Read mo
  name: BlueConic Objectives API
  slug: blueconic-objectives-api
- description: Pageview events are used to track page views by profiles. This is used by BlueConic Listeners. See [Listeners and Trackers](https://support.blueconic.com/hc/en-us/sections/200913331-Listeners-and-Trac
  name: BlueConic Pageview events API
  slug: blueconic-pageview-events-api
- description: Retrieve plugins from the gallery, or limit results to installed plugins only. See [Plugins](https://support.blueconic.com/en/articles/248049-plugins-overview).
  name: BlueConic Plugins API
  slug: blueconic-plugins-api
- description: Consent management events for a profile; consent changed or permission level changed. [Read more about using Objectives for privacy and consent](https://support.blueconic.com/hc/en-us/articles/3600021
  name: BlueConic Profile events API
  slug: blueconic-profile-events-api
- description: 'The following methods allow you to create, modify, retrieve properties from, and delete [BlueConic Profiles](https://support.blueconic.com/hc/en-us/articles/115001671965-Overview-BlueConic-Profiles), '
  name: BlueConic Profiles API
  slug: blueconic-profiles-api
- description: The following methods allow you to retrieve and update [Profile Properties](https://support.blueconic.com/hc/en-us/articles/202608231-Capturing-customer-data-in-Profile-Properties) and [Group Properti
  name: BlueConic Properties API
  slug: blueconic-properties-api
- description: Generate individualized content and product recommendations for a given profile. [Read more](https://support.blueconic.com/hc/en-us/articles/115005971169-Overview-Content-and-Product-Recommendations).
  name: BlueConic Recommendations API
  slug: blueconic-recommendations-api
- description: All reporting related endpoints.
  name: BlueConic Reporting API
  slug: blueconic-reporting-api
- description: A role contains a collection of data privacy and feature access permissions that you can assign to a user. Every BlueConic user is assigned to at least one role. A user can only access the features th
  name: BlueConic Roles API
  slug: blueconic-roles-api
- description: A segment is a group of profiles characterized by a defined set of attributes & properties. The following methods allow you to retrieve information from segments and the profiles within a given segmen
  name: BlueConic Segments API
  slug: blueconic-segments-api
- description: A store is a database for managing metadata about products or articles. You can populate it using a Product collector or Content collector, which scrapes data from your website. This metadata powers f
  name: BlueConic Stores API
  slug: blueconic-stores-api
- description: Roll up BlueConic timeline event data and store the results in a profile property. You can use that profile property for segmentation, reporting, and activation. [Read more](https://support.blueconic.
  name: BlueConic Timeline event rollups API
  slug: blueconic-timeline-event-rollups-api
- description: Timeline events store time-based data on events that occur for a profile, such as product orders or page views. In BlueConic, a Timeline event type defines how events are stored in a profile. For exam
  name: BlueConic Timeline Event Types API
  slug: blueconic-timeline-event-types-api
- description: The following methods allow you to create, modify, and retrieve URL mappings (tracking pixel or shortened URL). These can be created via the External tracker tab, but can also be created as a separate
  name: BlueConic URL mappings API
  slug: blueconic-url-mappings-api
- description: Users are the people who have access to the BlueConic environment. [Read more](https://support.blueconic.com/hc/en-us/articles/360000013785-Users)
  name: BlueConic Users API
  slug: blueconic-users-api
artifact_total: 130
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/blueconic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blueconic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/blueconic-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/blueconic-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.blueconic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.blueconic.com/hc/en-us/categories/200458421-Developers
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/blueconic
- group: docs
  title: ''
  type: OpenAPI
  url: https://github.com/blueconic/openapi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/blueconic
- group: other
  title: ''
  type: X
  url: https://twitter.com/blueconic
- group: company
  title: ''
  type: Blog
  url: https://www.blueconic.com/resources/category/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.blueconic.com/request-demo
- group: operate
  title: ''
  type: StatusPage
  url: https://status.blueconic.com
- group: operate
  title: ''
  type: Support
  url: https://support.blueconic.com/en/
- group: build
  title: ''
  type: iOSSDK
  url: https://github.com/blueconic/blueconic-ios-sdk
- group: build
  title: ''
  type: RokuSDK
  url: https://github.com/blueconic/blueconic-roku-sdk
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/blueconic/blueconic-mcp
- group: commercial
  title: ''
  type: Plans
  url: plans/blueconic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/blueconic-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/blueconic-finops.yml
created: '2026-06-13'
description: BlueConic is a customer data platform (CDP) with a REST API for managing unified customer profiles, lifecycle stages, segments, connections, and permissions-based data activation. The API provides OAuth 2.0-secured access to visitor profiles, segments, interactions, and audit events via an OpenAPI-compliant interface.
examples:
- key_count: 3
  name: Addcontentitemstostore Request
  slug: addContentItemsToStore-request
- key_count: 3
  name: Createcontentstore Request
  slug: createContentStore-request
- key_count: 3
  name: Createcontentstore Response 200
  slug: createContentStore-response-200
- key_count: 3
  name: Createmodel Response 200
  slug: createModel-response-200
- key_count: 3
  name: Createurlmapping Request
  slug: createURLMapping-request
- key_count: 3
  name: Createurlmapping Response 200
  slug: createURLMapping-response-200
- key_count: 3
  name: Createupdatedeletegroups Request
  slug: createUpdateDeleteGroups-request
- key_count: 3
  name: Createupdatedeletegroups Response 200
  slug: createUpdateDeleteGroups-response-200
- key_count: 3
  name: Createupdatedeleteprofiles Request
  slug: createUpdateDeleteProfiles-request
- key_count: 3
  name: Createupdatedeleteprofiles Response 200
  slug: createUpdateDeleteProfiles-response-200
- key_count: 3
  name: Createupdateprofileorgroupproperty Request
  slug: createUpdateProfileOrGroupProperty-request
- key_count: 3
  name: Createupdateprofileorgroupproperty Response 200
  slug: createUpdateProfileOrGroupProperty-response-200
- key_count: 3
  name: Deletecontentitemsfromstore Request
  slug: deleteContentItemsFromStore-request
- key_count: 3
  name: Deletemodel Response 200
  slug: deleteModel-response-200
- key_count: 3
  name: Deleteprofileorgroupproperty Response 200
  slug: deleteProfileOrGroupProperty-response-200
- key_count: 3
  name: Getallchannels Response 200
  slug: getAllChannels-response-200
- key_count: 3
  name: Getallconnections Response 200
  slug: getAllConnections-response-200
- key_count: 3
  name: Getallcontentstores Response 200
  slug: getAllContentStores-response-200
- key_count: 3
  name: Getalldialogues Response 200
  slug: getAllDialogues-response-200
- key_count: 3
  name: Getallgrouptypes Response 200
  slug: getAllGroupTypes-response-200
- key_count: 3
  name: Getallgroupsbygrouptype Response 200
  slug: getAllGroupsByGroupType-response-200
- key_count: 3
  name: Getalllifecycles Response 200
  slug: getAllLifecycles-response-200
- key_count: 3
  name: Getalllisteners Response 200
  slug: getAllListeners-response-200
- key_count: 3
  name: Getallmodels Response 200
  slug: getAllModels-response-200
- key_count: 3
  name: Getallnotebooks Response 200
  slug: getAllNotebooks-response-200
- key_count: 3
  name: Getallobjectives Response 200
  slug: getAllObjectives-response-200
- key_count: 3
  name: Getallplugins Response 200
  slug: getAllPlugins-response-200
- key_count: 3
  name: Getallprofileorgroupproperties Response 200
  slug: getAllProfileOrGroupProperties-response-200
- key_count: 3
  name: Getallroles Response 200
  slug: getAllRoles-response-200
- key_count: 3
  name: Getallrollups Response 200
  slug: getAllRollups-response-200
- key_count: 3
  name: Getallsegments Response 200
  slug: getAllSegments-response-200
- key_count: 3
  name: Getallusers Response 200
  slug: getAllUsers-response-200
- key_count: 3
  name: Getauditevents Response 200
  slug: getAuditEvents-response-200
- key_count: 3
  name: Getconnectionruns Response 200
  slug: getConnectionRuns-response-200
- key_count: 3
  name: Getcontentitemsfromstore Response 200
  slug: getContentItemsFromStore-response-200
- key_count: 3
  name: Getdialoguestatistics Response 200
  slug: getDialogueStatistics-response-200
- key_count: 3
  name: Getinteractions Response 200
  slug: getInteractions-response-200
- key_count: 3
  name: Getnotebookrunhistory Response 200
  slug: getNotebookRunHistory-response-200
- key_count: 3
  name: Getonechannel Response 200
  slug: getOneChannel-response-200
- key_count: 3
  name: Getoneconnection Response 200
  slug: getOneConnection-response-200
- key_count: 3
  name: Getonedialogue Response 200
  slug: getOneDialogue-response-200
- key_count: 3
  name: Getonegroupofgrouptype Response 200
  slug: getOneGroupOfGroupType-response-200
- key_count: 3
  name: Getonelifecycle Response 200
  slug: getOneLifecycle-response-200
- key_count: 3
  name: Getonelistener Response 200
  slug: getOneListener-response-200
- key_count: 3
  name: Getonemodelmetadata Response 200
  slug: getOneModelMetadata-response-200
- key_count: 3
  name: Getonenotebook Response 200
  slug: getOneNotebook-response-200
- key_count: 3
  name: Getoneobjective Response 200
  slug: getOneObjective-response-200
- key_count: 3
  name: Getoneplugin Response 200
  slug: getOnePlugin-response-200
- key_count: 3
  name: Getoneprofile Response 200
  slug: getOneProfile-response-200
- key_count: 3
  name: Getoneprofileorgroupproperty Response 200
  slug: getOneProfileOrGroupProperty-response-200
- key_count: 3
  name: Getonerole Response 200
  slug: getOneRole-response-200
- key_count: 3
  name: Getonerollup Response 200
  slug: getOneRollup-response-200
- key_count: 3
  name: Getonetimelineeventtype Response 200
  slug: getOneTimelineEventType-response-200
- key_count: 3
  name: Getoneurlmapping Response 200
  slug: getOneURLMapping-response-200
- key_count: 3
  name: Getoneuser Response 200
  slug: getOneUser-response-200
- key_count: 3
  name: Getprofileevents Response 200
  slug: getProfileEvents-response-200
- key_count: 3
  name: Getprofilesinsegment Response 200
  slug: getProfilesInSegment-response-200
- key_count: 3
  name: Getrecommendationspostjsonpasync Request
  slug: getRecommendationsPostJsonpAsync-request
- key_count: 3
  name: Getrecommendationspostjsonpasync Response 200
  slug: getRecommendationsPostJsonpAsync-response-200
- key_count: 3
  name: Gettimelineeventtypes Response 200
  slug: getTimelineEventTypes-response-200
- key_count: 3
  name: Gettoken Response 200
  slug: getToken-response-200
- key_count: 3
  name: Searchprofiles Response 200
  slug: searchProfiles-response-200
- key_count: 3
  name: Updatecontentstore Request
  slug: updateContentStore-request
- key_count: 3
  name: Updatecontentstore Response 200
  slug: updateContentStore-response-200
- key_count: 3
  name: Updatemodel Response 200
  slug: updateModel-response-200
- key_count: 3
  name: Updateurlmapping Request
  slug: updateURLMapping-request
- key_count: 3
  name: Updateurlmapping Response 200
  slug: updateURLMapping-response-200
finops:
- name: Blueconic Finops
  service_category: ''
  slug: blueconic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blueconic.png
json_schemas:
- name: AuditEntryBean
  property_count: 7
  slug: auditentrybean
- name: AuditEventsBean
  property_count: 1
  slug: auditeventsbean
- name: BlueConicUserBean
  property_count: 14
  slug: blueconicuserbean
- name: channel
  property_count: 15
  slug: channel
- name: Connection
  property_count: 17
  slug: connection
- name: contentStore
  property_count: 11
  slug: contentstore
- name: dialogue
  property_count: 13
  slug: dialogue
- name: group
  property_count: 5
  slug: group
- name: interactions
  property_count: 1
  slug: interactions
- name: lifecycle
  property_count: 12
  slug: lifecycle
- name: ModelBean
  property_count: 16
  slug: modelbean
- name: notebook
  property_count: 11
  slug: notebook
- name: objective
  property_count: 17
  slug: objective
- name: profile
  property_count: 14
  slug: profile
- name: profileProperties
  property_count: 6
  slug: profileproperties
- name: profileProperty
  property_count: 31
  slug: profileproperty
- name: profiles
  property_count: 5
  slug: profiles
- name: RecommendationRequest
  property_count: 4
  slug: recommendationrequest
- name: RecommendationResponse
  property_count: 3
  slug: recommendationresponse
- name: RoleBean
  property_count: 10
  slug: rolebean
- name: segment
  property_count: 11
  slug: segment
- name: segments
  property_count: 5
  slug: segments
- name: stage
  property_count: 3
  slug: stage
- name: timelineEventType
  property_count: 14
  slug: timelineeventtype
- name: UserBean
  property_count: 2
  slug: userbean
jsonld:
- class_count: 47
  name: Blueconic Context
  property_count: 3
  slug: blueconic-context
layout: provider
mcp_servers:
- description: ''
  name: blueconic-mcp
  slug: blueconic-mcp
modified: '2026-06-13'
name: BlueConic
nav: Providers
network: true
overview: 'BlueConic publishes 28 APIs on the [APIs.io](https://apis.io/) network, including Audit Events API, Channels API, Connections API, and 25 more. Tagged areas include Customer Data Platform, CDP, Customer Profiles, Segments, and Data Activation.


  The BlueConic catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BlueConic''s developer surface includes authentication, documentation, engineering blog, pricing, support, and 15 more developer resources.'
plans:
- name: Blueconic Plans Pricing
  plan_count: 1
  slug: blueconic-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 0
  name: Blueconic Rate Limits
  slug: blueconic-rate-limits
rules:
- name: BlueConic API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: blueconic-jsonschema-spectral-rules
scopes:
- name: Blueconic Scopes
  scope_count: 27
  slug: blueconic-scopes
  summary_line: 27 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 45.6
  delta: -4.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 64.0
    developer_ergonomics: 34.8
    discoverability: 50.0
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 50.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 28
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blueconic/refs/heads/main/screenshots/blueconic-2026-06-20T173532.png
security:
- kind: authentication
  name: Blueconic Authentication
  slug: blueconic-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Blueconic Domain Security
  slug: blueconic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blueconic
tags:
- Customer Data Platform
- CDP
- Customer Profiles
- Segments
- Data Activation
- First-Party Data
- Lifecycle Stages
- Connections
- Privacy
website: https://www.blueconic.com/
---
