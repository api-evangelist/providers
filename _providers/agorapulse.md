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
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.0
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Agorapulse Agentic Access
  operation_count: 22
  slug: agorapulse-agentic-access
  summary_line: 22 operations · 7 acting
api_count: 15
apis:
- description: Publishing calendar notes management
  name: Agorapulse Calendar Notes API
  slug: agorapulse-calendar-notes-api
- description: The webhook surface of the Agorapulse API — the OpenAPI 3.1 top-level webhooks object carrying the PUBLISHING_POST and INBOX_ITEM events, their payload schemas and the X-Hook-Signature HMAC scheme. Ca
  name: Agorapulse Webhooks API
  slug: agorapulse-agorapulse-api-api
- description: The Competitor API from Agorapulse — 2 operation(s) for competitor.
  name: Agorapulse Competitor API
  slug: agorapulse-competitor-api
- description: Read conversation threads from your social inbox.
  name: Agorapulse Conversations API
  slug: agorapulse-conversations-api
- description: Create draft posts for review and approval.
  name: Agorapulse Drafts API
  slug: agorapulse-drafts-api
- description: Folders that organize a workspace's social profiles, with the profiles each contains.
  name: Agorapulse Groups API
  slug: agorapulse-groups-api
- description: Service health and status checks.
  name: Agorapulse Health API
  slug: agorapulse-health-api
- description: List inbox items (comments, messages, reviews).
  name: Agorapulse Items API
  slug: agorapulse-items-api
- description: Upload media assets to your content library.
  name: Agorapulse Media API
  slug: agorapulse-media-api
- description: List and access the organizations you belong to.
  name: Agorapulse Organizations API
  slug: agorapulse-organizations-api
- description: List a Pinterest profile's boards to obtain the board id a pin requires.
  name: Agorapulse Pinterest boards API
  slug: agorapulse-pinterest-boards-api
- description: The connected social profiles within a workspace.
  name: Agorapulse Profiles API
  slug: agorapulse-profiles-api
- description: Reply to inbox items.
  name: Agorapulse Replies API
  slug: agorapulse-replies-api
- description: Pull audience, content and community-management insights.
  name: Agorapulse Reports API
  slug: agorapulse-reports-api
- description: Workspaces group the social profiles you manage inside an organization.
  name: Agorapulse Workspaces API
  slug: agorapulse-workspaces-api
artifact_total: 149
asyncapis:
- description: ''
  name: Agorapulse Webhooks
  slug: agorapulse-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Agorapulse Agorapulse API API
  slug: open-agorapulse-agorapulse-api-api
- collection_type: open
  name: Agorapulse Calendar notes API
  slug: open-agorapulse-calendar-notes-api
- collection_type: open
  name: Agorapulse Competitor API
  slug: open-agorapulse-competitor-api
- collection_type: open
  name: Agorapulse Conversations API
  slug: open-agorapulse-conversations-api
- collection_type: open
  name: Agorapulse Drafts API
  slug: open-agorapulse-drafts-api
- collection_type: open
  name: Agorapulse Groups API
  slug: open-agorapulse-groups-api
- collection_type: open
  name: Agorapulse Health API
  slug: open-agorapulse-health-api
- collection_type: open
  name: Agorapulse Items API
  slug: open-agorapulse-items-api
- collection_type: open
  name: Agorapulse Media API
  slug: open-agorapulse-media-api
- collection_type: open
  name: Agorapulse Organizations API
  slug: open-agorapulse-organizations-api
- collection_type: open
  name: Agorapulse Pinterest boards API
  slug: open-agorapulse-pinterest-boards-api
- collection_type: open
  name: Agorapulse Profiles API
  slug: open-agorapulse-profiles-api
- collection_type: open
  name: Agorapulse Replies API
  slug: open-agorapulse-replies-api
- collection_type: open
  name: Agorapulse Reports API
  slug: open-agorapulse-reports-api
- collection_type: open
  name: Agorapulse Workspaces API
  slug: open-agorapulse-workspaces-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/agorapulse-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/agorapulse-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/agorapulse-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agorapulse-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agorapulse-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.agorapulse.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.agorapulse.com/en/collections/10906108-product-updates-and-api
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/agorapulse
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agorapulse/
- group: company
  title: ''
  type: Blog
  url: https://www.agorapulse.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.agorapulse.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.agorapulse.com/
- group: other
  title: ''
  type: X
  url: https://x.com/agorapulse
- group: commercial
  title: ''
  type: Plans
  url: plans/agorapulse-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/agorapulse-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/agorapulse-finops.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/agorapulse-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/agorapulse-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/agorapulse-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/agorapulse-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/agorapulse-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agorapulse-llms.txt
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/agorapulse-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/agorapulse-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/agorapulse-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/agorapulse-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/agorapulse-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/agorapulse-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/agorapulse-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/agorapulse-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.agorapulse.com/
- group: auth
  title: ''
  type: Security
  url: https://www.agorapulse.com/security/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/agorapulse-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: APIReference
  url: https://api.agorapulse.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://support.agorapulse.com/en/articles/12417183-how-to-connect-to-agorapulse-s-open-api
- group: operate
  title: ''
  type: Support
  url: https://support.agorapulse.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.agorapulse.com/signup/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agorapulse.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agorapulse.com/privacy-policy/
created: '2026-06-13'
description: Agorapulse is a social media management and CRM platform offering a REST API for publishing content, managing inboxes, monitoring social listening, and accessing performance analytics across Facebook, Instagram, LinkedIn, YouTube, TikTok, and Threads.
examples:
- key_count: 3
  name: Health 200 Example
  slug: health-200-example
finops:
- name: Agorapulse Finops
  service_category: ''
  slug: agorapulse-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agorapulse.png
json_schemas:
- name: AbstractFacebookType
  property_count: 0
  slug: abstractfacebooktype
- name: AbstractItem
  property_count: 12
  slug: abstractitem
- name: AccountManagerSummary
  property_count: 3
  slug: accountmanagersummary
- name: AccountRole
  property_count: 0
  slug: accountrole
- name: AccountSummary
  property_count: 20
  slug: accountsummary
- name: AccountType
  property_count: 0
  slug: accounttype
- name: AudienceReportByDate
  property_count: 2
  slug: audiencereportbydate
- name: CommunityManagementAction
  property_count: 4
  slug: communitymanagementaction
- name: CommunityManagementByDate
  property_count: 3
  slug: communitymanagementbydate
- name: CommunityManagementInsight
  property_count: 1
  slug: communitymanagementinsight
- name: ContentReportData
  property_count: 7
  slug: contentreportdata
- name: ContentReportInsight_1
  property_count: 1
  slug: contentreportinsight_1
- name: CreateCalendarNoteOpenRequest
  property_count: 6
  slug: createcalendarnoteopenrequest
- name: CreateCalendarNoteOpenResponse
  property_count: 7
  slug: createcalendarnoteopenresponse
- name: CreateReplyRequest
  property_count: 4
  slug: createreplyrequest
- name: CreateSimpleDraftOpenRequest.ProfileScheduling
  property_count: 2
  slug: createsimpledraftopenrequest-profilescheduling
- name: CreateSimpleDraftOpenRequest
  property_count: 6
  slug: createsimpledraftopenrequest
- name: CreateSimpleDraftOpenResponse
  property_count: 1
  slug: createsimpledraftopenresponse
- name: CreateSimpleScheduleOpenRequest.ProfileScheduling
  property_count: 2
  slug: createsimplescheduleopenrequest-profilescheduling
- name: CreateSimpleScheduleOpenRequest
  property_count: 6
  slug: createsimplescheduleopenrequest
- name: CreateSimpleScheduleOpenResponse
  property_count: 1
  slug: createsimplescheduleopenresponse
- name: FacebookAudienceInsight
  property_count: 41
  slug: facebookaudienceinsight
- name: FacebookCommunityManagementAction
  property_count: 0
  slug: facebookcommunitymanagementaction
- name: FacebookContentReportInsight
  property_count: 40
  slug: facebookcontentreportinsight
- name: FacebookType.Metadata.Connections
  property_count: 0
  slug: facebooktype-metadata-connections
- name: FacebookType.Metadata
  property_count: 0
  slug: facebooktype-metadata
- name: FacebookType
  property_count: 0
  slug: facebooktype
- name: GroupOfPosts
  property_count: 5
  slug: groupofposts
- name: GroupOfPostsAction
  property_count: 0
  slug: groupofpostsaction
- name: GroupOfPostsEvent
  property_count: 6
  slug: groupofpostsevent
- name: GroupOfPostsEventType
  property_count: 0
  slug: groupofpostseventtype
- name: GroupOfPostsSummary.ProfileSchedulingSummary
  property_count: 2
  slug: groupofpostssummary-profileschedulingsummary
- name: GroupOfPostsSummary.SchedulingSummary
  property_count: 3
  slug: groupofpostssummary-schedulingsummary
- name: GroupOfPostsSummary
  property_count: 5
  slug: groupofpostssummary
- name: InboxItem
  property_count: 13
  slug: inboxitem
- name: InboxItemAction
  property_count: 0
  slug: inboxitemaction
- name: InboxItemCreator
  property_count: 2
  slug: inboxitemcreator
- name: InboxItemEvent
  property_count: 6
  slug: inboxitemevent
- name: InboxItemEventType
  property_count: 0
  slug: inboxitemeventtype
- name: InboxItemSentiment
  property_count: 0
  slug: inboxitemsentiment
- name: InboxItemType
  property_count: 0
  slug: inboxitemtype
- name: InstagramAudienceInsight
  property_count: 38
  slug: instagramaudienceinsight
- name: InstagramCommunityManagementAction
  property_count: 0
  slug: instagramcommunitymanagementaction
- name: InstagramContentReportInsight
  property_count: 31
  slug: instagramcontentreportinsight
- name: InstagramStoryContentReportInsight
  property_count: 9
  slug: instagramstorycontentreportinsight
- name: ItemCreator
  property_count: 2
  slug: itemcreator
- name: ItemDTO
  property_count: 0
  slug: itemdto
- name: ItemFilterType
  property_count: 0
  slug: itemfiltertype
- name: ItemSentiment
  property_count: 0
  slug: itemsentiment
- name: ItemsSearchResponse
  property_count: 2
  slug: itemssearchresponse
- name: ItemType
  property_count: 0
  slug: itemtype
- name: LinkedinAudienceInsight
  property_count: 39
  slug: linkedinaudienceinsight
- name: LinkedinCommunityManagementAction
  property_count: 0
  slug: linkedincommunitymanagementaction
- name: LinkedinContentReportInsight
  property_count: 32
  slug: linkedincontentreportinsight
- name: ListeningItemAction
  property_count: 0
  slug: listeningitemaction
- name: ListeningItemEvent
  property_count: 6
  slug: listeningitemevent
- name: ListeningItemEventType
  property_count: 0
  slug: listeningitemeventtype
- name: MessagesSearchResponse
  property_count: 2
  slug: messagessearchresponse
- name: NamedFacebookType
  property_count: 0
  slug: namedfacebooktype
- name: Network
  property_count: 0
  slug: network
- name: OpenAudienceInsight
  property_count: 1
  slug: openaudienceinsight
- name: Order
  property_count: 0
  slug: order
- name: OrganizationListResponse
  property_count: 1
  slug: organizationlistresponse
- name: OrganizationResponse
  property_count: 3
  slug: organizationresponse
- name: Post
  property_count: 7
  slug: post
- name: PostAction
  property_count: 0
  slug: postaction
- name: PostStatus
  property_count: 0
  slug: poststatus
- name: PostStatus1
  property_count: 0
  slug: poststatus1
- name: PostType
  property_count: 0
  slug: posttype
- name: Profile
  property_count: 3
  slug: profile
- name: Profile1
  property_count: 3
  slug: profile1
- name: ProfileListResponse
  property_count: 1
  slug: profilelistresponse
- name: ProfileResponse_1
  property_count: 5
  slug: profileresponse_1
- name: PublishingCalendarNoteColor
  property_count: 0
  slug: publishingcalendarnotecolor
- name: PublishingPost
  property_count: 2
  slug: publishingpost
- name: PublishingPostEvent
  property_count: 6
  slug: publishingpostevent
- name: PublishingPostEventType
  property_count: 0
  slug: publishingposteventtype
- name: SearchCalendarNoteOpenRequest
  property_count: 3
  slug: searchcalendarnoteopenrequest
- name: SearchCalendarNoteOpenResponse.CalendarNoteOpenItem
  property_count: 7
  slug: searchcalendarnoteopenresponse-calendarnoteopenitem
- name: SearchCalendarNoteOpenResponse
  property_count: 2
  slug: searchcalendarnoteopenresponse
- name: Service
  property_count: 0
  slug: service
- name: SharedCalendarAccountManagerSummary
  property_count: 5
  slug: sharedcalendaraccountmanagersummary
- name: SharedCalendarAccountManagerSummaryResponse
  property_count: 5
  slug: sharedcalendaraccountmanagersummaryresponse
- name: SharedCalendarAccountSummary
  property_count: 10
  slug: sharedcalendaraccountsummary
- name: SharedCalendarAccountSummaryResponse
  property_count: 9
  slug: sharedcalendaraccountsummaryresponse
- name: SharedCalendarManagerSummary
  property_count: 4
  slug: sharedcalendarmanagersummary
- name: SharedCalendarManagerSummaryResponse
  property_count: 4
  slug: sharedcalendarmanagersummaryresponse
- name: SimplePublishOpenRequest
  property_count: 6
  slug: simplepublishopenrequest
- name: SocialNetworkChannel
  property_count: 0
  slug: socialnetworkchannel
- name: SpecificServiceAccountData
  property_count: 1
  slug: specificserviceaccountdata
- name: StudioMediaUploadOpenRequest
  property_count: 5
  slug: studiomediauploadopenrequest
- name: StudioMediaUploadOpenResponse
  property_count: 6
  slug: studiomediauploadopenresponse
- name: ThreadsAudienceInsight
  property_count: 17
  slug: threadsaudienceinsight
- name: TiktokAudienceInsight
  property_count: 10
  slug: tiktokaudienceinsight
- name: TiktokCommunityManagementAction
  property_count: 0
  slug: tiktokcommunitymanagementaction
- name: TikTokContentReportInsight
  property_count: 14
  slug: tiktokcontentreportinsight
- name: TwitterAudienceInsight
  property_count: 19
  slug: twitteraudienceinsight
- name: TwitterContentReportInsight
  property_count: 7
  slug: twittercontentreportinsight
- name: User
  property_count: 3
  slug: user
- name: WorkspaceListResponse
  property_count: 1
  slug: workspacelistresponse
- name: WorkspaceResponse_1
  property_count: 3
  slug: workspaceresponse_1
- name: YoutubeAudienceInsight
  property_count: 17
  slug: youtubeaudienceinsight
- name: YoutubeCommunityManagementAction
  property_count: 0
  slug: youtubecommunitymanagementaction
- name: YoutubeContentReportInsight
  property_count: 10
  slug: youtubecontentreportinsight
jsonld:
- class_count: 233
  name: Agorapulse Context
  property_count: 104
  slug: agorapulse-context
layout: provider
mcp_servers:
- description: ''
  name: Agorapulse MCP Server
  slug: agorapulse-mcp-server
modified: '2026-08-13'
name: Agorapulse
nav: Providers
network: true
overview: 'Agorapulse publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Calendar Notes API, Webhooks API, Competitor API, and 12 more. Tagged areas include Social Media Management, Social-Media, CRM, Analytics, and Publishing.


  The Agorapulse catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Agorapulse''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, API reference, getting-started guide, and 33 more developer resources.'
plans:
- name: Agorapulse Plans Pricing
  plan_count: 4
  slug: agorapulse-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Agorapulse Rate Limits
  slug: agorapulse-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Agorapulse API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: agorapulse-jsonschema-spectral-rules
scopes:
- name: Agorapulse Scopes
  scope_count: 1
  slug: agorapulse-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: exemplar
  composite: 71.4
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 26.5
    contract_quality: 70.9
    developer_ergonomics: 56.5
    discoverability: 92.6
    governance: 26.5
    operational_transparency: 76.3
  previous_composite: 71.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agorapulse/refs/heads/main/screenshots/agorapulse-2026-06-20T170402.png
security:
- kind: authentication
  name: Agorapulse Authentication
  slug: agorapulse-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Agorapulse Domain Security
  slug: agorapulse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Agorapulse Vulnerability Disclosure
  slug: agorapulse-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Agorapulse Trust Center
  slug: agorapulse-trust-center
  summary_line: ISO 27001:2022, SOC 2 Type 2, GDPR
slug: agorapulse
tags:
- Social Media Management
- Social-Media
- CRM
- Analytics
- Publishing
- Inbox Management
- Social Listening
website: https://www.agorapulse.com/
---
