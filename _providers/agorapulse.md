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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Agorapulse Agentic Access
  operation_count: 18
  slug: agorapulse-agentic-access
  summary_line: 18 operations · 8 acting
api_count: 12
apis:
- description: Publishing calendar notes management
  name: Agorapulse Calendar Notes API
  slug: agorapulse-calendar-notes-api
- description: The Inbox conversations API from Agorapulse — 1 operation(s) for inbox conversations.
  name: Agorapulse Inbox conversations API
  slug: agorapulse-inbox-conversations-api
- description: The Inbox items API from Agorapulse — 1 operation(s) for inbox items.
  name: Agorapulse Inbox items API
  slug: agorapulse-inbox-items-api
- description: The Inbox reply API from Agorapulse — 1 operation(s) for inbox reply.
  name: Agorapulse Inbox reply API
  slug: agorapulse-inbox-reply-api
- description: The OpenAPI API from Agorapulse — 1 operation(s) for openapi.
  name: Agorapulse OpenAPI API
  slug: agorapulse-openapi-api
- description: The Organization API from Agorapulse — 1 operation(s) for organization.
  name: Agorapulse Organization API
  slug: agorapulse-organization-api
- description: The Profile API from Agorapulse — 1 operation(s) for profile.
  name: Agorapulse Profile API
  slug: agorapulse-profile-api
- description: The Report API from Agorapulse — 3 operation(s) for report.
  name: Agorapulse Report API
  slug: agorapulse-report-api
- description: Publishing simple drafts management
  name: Agorapulse Simple Drafts API
  slug: agorapulse-simple-drafts-api
- description: Publishing simple scheduled and immediate posts management
  name: Agorapulse Simple Scheduling API
  slug: agorapulse-simple-scheduling-api
- description: Studio media upload management
  name: Agorapulse Studio Media API
  slug: agorapulse-studio-media-api
- description: The Workspace API from Agorapulse — 1 operation(s) for workspace.
  name: Agorapulse Workspace API
  slug: agorapulse-workspace-api
artifact_total: 127
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
modified: '2026-06-13'
name: Agorapulse
nav: Providers
network: true
overview: 'Agorapulse publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Calendar Notes API, Inbox conversations API, Inbox items API, and 9 more. Tagged areas include Social Media Management, Social Media, CRM, Analytics, and Publishing.


  The Agorapulse catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Agorapulse''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Agorapulse Plans Pricing
  plan_count: 4
  slug: agorapulse-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 1
  name: Agorapulse Rate Limits
  slug: agorapulse-rate-limits
rules:
- name: Agorapulse API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: agorapulse-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.4
  delta: -5.4
  facets:
    commercial_clarity: 57.9
    contract_quality: 58.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 55.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/agorapulse/refs/heads/main/screenshots/agorapulse-2026-06-20T170402.png
security:
- kind: authentication
  name: Agorapulse Authentication
  slug: agorapulse-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Agorapulse Domain Security
  slug: agorapulse-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Agorapulse Vulnerability Disclosure
  slug: agorapulse-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Agorapulse Trust Center
  slug: agorapulse-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: agorapulse
tags:
- Social Media Management
- Social Media
- CRM
- Analytics
- Publishing
- Inbox Management
- Social Listening
website: https://www.agorapulse.com/
---
