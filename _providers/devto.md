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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 42
  human_in_the_loop: 0
  name: Devto Agentic Access
  operation_count: 108
  slug: devto-agentic-access
  summary_line: 108 operations · 42 acting
api_count: 19
apis:
- description: The agent_sessions API from DEV Community — 2 operation(s) for agent_sessions.
  name: DEV Community agent_sessions API
  slug: devto-agent-sessions-api
- description: The articles API from DEV Community — 22 operation(s) for articles.
  name: DEV Community articles API
  slug: devto-articles-api
- description: The billboards API from DEV Community — 3 operation(s) for billboards.
  name: DEV Community billboards API
  slug: devto-billboards-api
- description: The comments API from DEV Community — 4 operation(s) for comments.
  name: DEV Community comments API
  slug: devto-comments-api
- description: The display ads API from DEV Community — 3 operation(s) for display ads.
  name: DEV Community display ads API
  slug: devto-display-ads-api
- description: The followed_tags API from DEV Community — 2 operation(s) for followed_tags.
  name: DEV Community followed_tags API
  slug: devto-followed-tags-api
- description: The followers API from DEV Community — 2 operation(s) for followers.
  name: DEV Community followers API
  slug: devto-followers-api
- description: The organizations API from DEV Community — 8 operation(s) for organizations.
  name: DEV Community organizations API
  slug: devto-organizations-api
- description: The pages API from DEV Community — 4 operation(s) for pages.
  name: DEV Community pages API
  slug: devto-pages-api
- description: The podcast_episodes API from DEV Community — 2 operation(s) for podcast_episodes.
  name: DEV Community podcast_episodes API
  slug: devto-podcast-episodes-api
- description: The profile images API from DEV Community — 2 operation(s) for profile images.
  name: DEV Community profile images API
  slug: devto-profile-images-api
- description: The reactions API from DEV Community — 4 operation(s) for reactions.
  name: DEV Community reactions API
  slug: devto-reactions-api
- description: The readinglist API from DEV Community — 2 operation(s) for readinglist.
  name: DEV Community readinglist API
  slug: devto-readinglist-api
- description: The segments API from DEV Community — 5 operation(s) for segments.
  name: DEV Community segments API
  slug: devto-segments-api
- description: The surveys API from DEV Community — 4 operation(s) for surveys.
  name: DEV Community surveys API
  slug: devto-surveys-api
- description: The tags API from DEV Community — 4 operation(s) for tags.
  name: DEV Community tags API
  slug: devto-tags-api
- description: The trends API from DEV Community — 3 operation(s) for trends.
  name: DEV Community trends API
  slug: devto-trends-api
- description: The users API from DEV Community — 23 operation(s) for users.
  name: DEV Community users API
  slug: devto-users-api
- description: The videos API from DEV Community — 2 operation(s) for videos.
  name: DEV Community videos API
  slug: devto-videos-api
artifact_total: 201
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/devto-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/devto-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/devto-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/devto-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://dev.to
- group: docs
  title: ''
  type: Documentation
  url: https://developers.forem.com/api/v1
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/forem
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/dev-a-forem-community/
- group: company
  title: ''
  type: Blog
  url: https://dev.to/devteam
- group: commercial
  title: ''
  type: Pricing
  url: https://dev.to/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dev.to/
- group: other
  title: ''
  type: X
  url: https://x.com/thepracticaldev
- group: commercial
  title: ''
  type: Plans
  url: plans/devto-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/devto-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/devto-finops.yml
created: '2026-06-13'
description: DEV Community (DEV.to) is a developer community platform built on the open-source Forem software. It provides a REST API for managing articles, comments, user profiles, organizations, podcast episodes, and accessing published developer content. The API supports creating and updating posts, retrieving community content by tag or author, managing reactions and reading lists, and administering organizations. Authentication uses an API key passed via the api-key header, with public read access available without authentication.
examples:
- key_count: 5
  name: Adduserstosegment Response 200
  slug: addUsersToSegment-response-200
- key_count: 5
  name: Adduserstosegment Response 401
  slug: addUsersToSegment-response-401
- key_count: 5
  name: Adduserstosegment Response 404
  slug: addUsersToSegment-response-404
- key_count: 5
  name: Adduserstosegment Response 422
  slug: addUsersToSegment-response-422
- key_count: 5
  name: Createagentsession Response 201
  slug: createAgentSession-response-201
- key_count: 5
  name: Createagentsession Response 401
  slug: createAgentSession-response-401
- key_count: 5
  name: Createagentsession Response 422
  slug: createAgentSession-response-422
- key_count: 5
  name: Createarticle Response 201
  slug: createArticle-response-201
- key_count: 5
  name: Createarticle Response 401
  slug: createArticle-response-401
- key_count: 5
  name: Createarticle Response 422
  slug: createArticle-response-422
- key_count: 5
  name: Createorganization Response 201
  slug: createOrganization-response-201
- key_count: 5
  name: Createorganization Response 422
  slug: createOrganization-response-422
- key_count: 5
  name: Createsegment Response 201
  slug: createSegment-response-201
- key_count: 5
  name: Createsegment Response 401
  slug: createSegment-response-401
- key_count: 5
  name: Deletesegment Response 200
  slug: deleteSegment-response-200
- key_count: 5
  name: Deletesegment Response 401
  slug: deleteSegment-response-401
- key_count: 5
  name: Deletesegment Response 404
  slug: deleteSegment-response-404
- key_count: 5
  name: Deletesegment Response 409
  slug: deleteSegment-response-409
- key_count: 5
  name: Delete_Api_Organizations_{Id} Response 200
  slug: delete_api_organizations_{id}-response-200
- key_count: 5
  name: Delete_Api_Organizations_{Id} Response 401
  slug: delete_api_organizations_{id}-response-401
- key_count: 5
  name: Delete_Api_Pages_{Id} Response 200
  slug: delete_api_pages_{id}-response-200
- key_count: 5
  name: Delete_Api_Pages_{Id} Response 401
  slug: delete_api_pages_{id}-response-401
- key_count: 5
  name: Delete_Api_Pages_{Id} Response 422
  slug: delete_api_pages_{id}-response-422
- key_count: 5
  name: Getagentsessionbyid Response 200
  slug: getAgentSessionById-response-200
- key_count: 5
  name: Getagentsessionbyid Response 401
  slug: getAgentSessionById-response-401
- key_count: 5
  name: Getagentsessionbyid Response 404
  slug: getAgentSessionById-response-404
- key_count: 5
  name: Getagentsessions Response 200
  slug: getAgentSessions-response-200
- key_count: 5
  name: Getagentsessions Response 401
  slug: getAgentSessions-response-401
- key_count: 5
  name: Getarticlebyid Response 200
  slug: getArticleById-response-200
- key_count: 5
  name: Getarticlebyid Response 404
  slug: getArticleById-response-404
- key_count: 5
  name: Getarticlebypath Response 200
  slug: getArticleByPath-response-200
- key_count: 5
  name: Getarticlebypath Response 404
  slug: getArticleByPath-response-404
- key_count: 5
  name: Getarticles Response 200
  slug: getArticles-response-200
- key_count: 5
  name: Getcommentbyid Response 200
  slug: getCommentById-response-200
- key_count: 5
  name: Getcommentbyid Response 404
  slug: getCommentById-response-404
- key_count: 5
  name: Getcommentsbyarticleid Response 200
  slug: getCommentsByArticleId-response-200
- key_count: 5
  name: Getcommentsbyarticleid Response 404
  slug: getCommentsByArticleId-response-404
- key_count: 5
  name: Getfollowedtags Response 200
  slug: getFollowedTags-response-200
- key_count: 5
  name: Getfollowedtags Response 401
  slug: getFollowedTags-response-401
- key_count: 5
  name: Getfollowers Response 200
  slug: getFollowers-response-200
- key_count: 5
  name: Getfollowers Response 401
  slug: getFollowers-response-401
- key_count: 5
  name: Getlatestarticles Response 200
  slug: getLatestArticles-response-200
- key_count: 5
  name: Getorgarticles Response 200
  slug: getOrgArticles-response-200
- key_count: 5
  name: Getorgarticles Response 404
  slug: getOrgArticles-response-404
- key_count: 5
  name: Getorgusers Response 200
  slug: getOrgUsers-response-200
- key_count: 5
  name: Getorgusers Response 404
  slug: getOrgUsers-response-404
- key_count: 5
  name: Getorganization Response 200
  slug: getOrganization-response-200
- key_count: 5
  name: Getorganization Response 404
  slug: getOrganization-response-404
- key_count: 5
  name: Getorganizationbyid Response 200
  slug: getOrganizationById-response-200
- key_count: 5
  name: Getorganizationbyid Response 404
  slug: getOrganizationById-response-404
- key_count: 5
  name: Getorganizations Response 200
  slug: getOrganizations-response-200
- key_count: 5
  name: Getpodcastepisodes Response 200
  slug: getPodcastEpisodes-response-200
- key_count: 5
  name: Getpodcastepisodes Response 404
  slug: getPodcastEpisodes-response-404
- key_count: 5
  name: Getprofileimage Response 200
  slug: getProfileImage-response-200
- key_count: 5
  name: Getprofileimage Response 404
  slug: getProfileImage-response-404
- key_count: 5
  name: Getreadinglist Response 401
  slug: getReadinglist-response-401
- key_count: 5
  name: Getsegment Response 200
  slug: getSegment-response-200
- key_count: 5
  name: Getsegment Response 401
  slug: getSegment-response-401
- key_count: 5
  name: Getsegment Response 404
  slug: getSegment-response-404
- key_count: 5
  name: Getsegments Response 200
  slug: getSegments-response-200
- key_count: 5
  name: Getsegments Response 401
  slug: getSegments-response-401
- key_count: 5
  name: Getsurveybyidorslug Response 200
  slug: getSurveyByIdOrSlug-response-200
- key_count: 5
  name: Getsurveybyidorslug Response 401
  slug: getSurveyByIdOrSlug-response-401
- key_count: 5
  name: Getsurveybyidorslug Response 404
  slug: getSurveyByIdOrSlug-response-404
- key_count: 5
  name: Getsurveypolltextresponses Response 200
  slug: getSurveyPollTextResponses-response-200
- key_count: 5
  name: Getsurveypolltextresponses Response 401
  slug: getSurveyPollTextResponses-response-401
- key_count: 5
  name: Getsurveypolltextresponses Response 404
  slug: getSurveyPollTextResponses-response-404
- key_count: 5
  name: Getsurveypollvotes Response 200
  slug: getSurveyPollVotes-response-200
- key_count: 5
  name: Getsurveypollvotes Response 401
  slug: getSurveyPollVotes-response-401
- key_count: 5
  name: Getsurveypollvotes Response 404
  slug: getSurveyPollVotes-response-404
- key_count: 5
  name: Getsurveys Response 200
  slug: getSurveys-response-200
- key_count: 5
  name: Getsurveys Response 401
  slug: getSurveys-response-401
- key_count: 5
  name: Gettags Response 200
  slug: getTags-response-200
- key_count: 5
  name: Gettrend Response 200
  slug: getTrend-response-200
- key_count: 5
  name: Gettrend Response 404
  slug: getTrend-response-404
- key_count: 5
  name: Gettrendarticles Response 200
  slug: getTrendArticles-response-200
- key_count: 5
  name: Gettrendarticles Response 404
  slug: getTrendArticles-response-404
- key_count: 5
  name: Gettrends Response 200
  slug: getTrends-response-200
- key_count: 5
  name: Getuserallarticles Response 401
  slug: getUserAllArticles-response-401
- key_count: 5
  name: Getuserarticles Response 401
  slug: getUserArticles-response-401
- key_count: 5
  name: Getuserme Response 200
  slug: getUserMe-response-200
- key_count: 5
  name: Getuserme Response 401
  slug: getUserMe-response-401
- key_count: 5
  name: Getuserpublishedarticles Response 401
  slug: getUserPublishedArticles-response-401
- key_count: 5
  name: Getuserunpublishedarticles Response 401
  slug: getUserUnpublishedArticles-response-401
- key_count: 5
  name: Getusersinsegment Response 200
  slug: getUsersInSegment-response-200
- key_count: 5
  name: Getusersinsegment Response 401
  slug: getUsersInSegment-response-401
- key_count: 5
  name: Getusersinsegment Response 404
  slug: getUsersInSegment-response-404
- key_count: 5
  name: Get_Api_Billboards Response 401
  slug: get_api_billboards-response-401
- key_count: 5
  name: Get_Api_Billboards_{Id} Response 200
  slug: get_api_billboards_{id}-response-200
- key_count: 5
  name: Get_Api_Billboards_{Id} Response 401
  slug: get_api_billboards_{id}-response-401
- key_count: 5
  name: Get_Api_Billboards_{Id} Response 404
  slug: get_api_billboards_{id}-response-404
- key_count: 5
  name: Get_Api_Pages Response 200
  slug: get_api_pages-response-200
- key_count: 5
  name: Get_Api_Pages_{Id} Response 200
  slug: get_api_pages_{id}-response-200
- key_count: 5
  name: Limituser Response 401
  slug: limitUser-response-401
- key_count: 5
  name: Limituser Response 404
  slug: limitUser-response-404
- key_count: 5
  name: Postadminuserscreate Response 401
  slug: postAdminUsersCreate-response-401
- key_count: 5
  name: Postadminuserscreate Response 422
  slug: postAdminUsersCreate-response-422
- key_count: 5
  name: Post_Api_Billboards Response 201
  slug: post_api_billboards-response-201
- key_count: 5
  name: Post_Api_Billboards Response 401
  slug: post_api_billboards-response-401
- key_count: 5
  name: Post_Api_Billboards Response 422
  slug: post_api_billboards-response-422
- key_count: 5
  name: Post_Api_Pages Response 200
  slug: post_api_pages-response-200
- key_count: 5
  name: Post_Api_Pages Response 401
  slug: post_api_pages-response-401
- key_count: 5
  name: Post_Api_Pages Response 422
  slug: post_api_pages-response-422
- key_count: 5
  name: Post_Api_Reactions Response 200
  slug: post_api_reactions-response-200
- key_count: 5
  name: Post_Api_Reactions Response 401
  slug: post_api_reactions-response-401
- key_count: 5
  name: Post_Api_Reactions_Toggle Response 200
  slug: post_api_reactions_toggle-response-200
- key_count: 5
  name: Post_Api_Reactions_Toggle Response 401
  slug: post_api_reactions_toggle-response-401
- key_count: 5
  name: Put_Api_Billboards_{Id} Response 200
  slug: put_api_billboards_{id}-response-200
- key_count: 5
  name: Put_Api_Billboards_{Id} Response 401
  slug: put_api_billboards_{id}-response-401
- key_count: 5
  name: Put_Api_Billboards_{Id} Response 404
  slug: put_api_billboards_{id}-response-404
- key_count: 5
  name: Put_Api_Billboards_{Id}_Unpublish Response 401
  slug: put_api_billboards_{id}_unpublish-response-401
- key_count: 5
  name: Put_Api_Billboards_{Id}_Unpublish Response 404
  slug: put_api_billboards_{id}_unpublish-response-404
- key_count: 5
  name: Put_Api_Organizations_{Id} Response 200
  slug: put_api_organizations_{id}-response-200
- key_count: 5
  name: Put_Api_Organizations_{Id} Response 401
  slug: put_api_organizations_{id}-response-401
- key_count: 5
  name: Put_Api_Organizations_{Id} Response 404
  slug: put_api_organizations_{id}-response-404
- key_count: 5
  name: Put_Api_Organizations_{Id} Response 422
  slug: put_api_organizations_{id}-response-422
- key_count: 5
  name: Put_Api_Pages_{Id} Response 200
  slug: put_api_pages_{id}-response-200
- key_count: 5
  name: Put_Api_Pages_{Id} Response 401
  slug: put_api_pages_{id}-response-401
- key_count: 5
  name: Put_Api_Pages_{Id} Response 422
  slug: put_api_pages_{id}-response-422
- key_count: 5
  name: Removeusersfromsegment Response 200
  slug: removeUsersFromSegment-response-200
- key_count: 5
  name: Removeusersfromsegment Response 401
  slug: removeUsersFromSegment-response-401
- key_count: 5
  name: Removeusersfromsegment Response 404
  slug: removeUsersFromSegment-response-404
- key_count: 5
  name: Removeusersfromsegment Response 422
  slug: removeUsersFromSegment-response-422
- key_count: 5
  name: Spamuser Response 401
  slug: spamUser-response-401
- key_count: 5
  name: Spamuser Response 404
  slug: spamUser-response-404
- key_count: 5
  name: Suspenduser Response 401
  slug: suspendUser-response-401
- key_count: 5
  name: Suspenduser Response 404
  slug: suspendUser-response-404
- key_count: 5
  name: Trustuser Response 401
  slug: trustUser-response-401
- key_count: 5
  name: Trustuser Response 404
  slug: trustUser-response-404
- key_count: 5
  name: Unlimituser Response 401
  slug: unLimitUser-response-401
- key_count: 5
  name: Unlimituser Response 404
  slug: unLimitUser-response-404
- key_count: 5
  name: Unspamuser Response 401
  slug: unSpamUser-response-401
- key_count: 5
  name: Unspamuser Response 404
  slug: unSpamUser-response-404
- key_count: 5
  name: Untrustuser Response 401
  slug: unTrustUser-response-401
- key_count: 5
  name: Untrustuser Response 404
  slug: unTrustUser-response-404
- key_count: 5
  name: Unpublisharticle Response 401
  slug: unpublishArticle-response-401
- key_count: 5
  name: Unpublisharticle Response 404
  slug: unpublishArticle-response-404
- key_count: 5
  name: Unpublishuser Response 401
  slug: unpublishUser-response-401
- key_count: 5
  name: Unpublishuser Response 404
  slug: unpublishUser-response-404
- key_count: 5
  name: Updatearticle Response 200
  slug: updateArticle-response-200
- key_count: 5
  name: Updatearticle Response 401
  slug: updateArticle-response-401
- key_count: 5
  name: Updatearticle Response 404
  slug: updateArticle-response-404
- key_count: 5
  name: Updatearticle Response 422
  slug: updateArticle-response-422
- key_count: 5
  name: Videos Response 200
  slug: videos-response-200
finops:
- name: Devto Finops
  service_category: ''
  slug: devto-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/devto.png
json_schemas:
- name: AgentSessionIndex
  property_count: 9
  slug: agentsessionindex
- name: AgentSessionShow
  property_count: 13
  slug: agentsessionshow
- name: Article
  property_count: 1
  slug: article
- name: ArticleFlareTag
  property_count: 3
  slug: articleflaretag
- name: ArticleIndex
  property_count: 25
  slug: articleindex
- name: Billboard
  property_count: 16
  slug: billboard
- name: Comment
  property_count: 4
  slug: comment
- name: ExtendedUser
  property_count: 13
  slug: extendeduser
- name: FollowedTag
  property_count: 3
  slug: followedtag
- name: MyUser
  property_count: 14
  slug: myuser
- name: Organization
  property_count: 12
  slug: organization
- name: Page
  property_count: 8
  slug: page
- name: PodcastEpisodeIndex
  property_count: 7
  slug: podcastepisodeindex
- name: Poll
  property_count: 14
  slug: poll
- name: PollOption
  property_count: 7
  slug: polloption
- name: PollTextResponse
  property_count: 8
  slug: polltextresponse
- name: PollVote
  property_count: 8
  slug: pollvote
- name: ProfileImage
  property_count: 4
  slug: profileimage
- name: Segment
  property_count: 3
  slug: segment
- name: SegmentUserIds
  property_count: 1
  slug: segmentuserids
- name: SharedOrganization
  property_count: 5
  slug: sharedorganization
- name: SharedPodcast
  property_count: 3
  slug: sharedpodcast
- name: SharedUser
  property_count: 7
  slug: shareduser
- name: Survey
  property_count: 10
  slug: survey
- name: SurveyWithPolls
  property_count: 0
  slug: surveywithpolls
- name: Tag
  property_count: 4
  slug: tag
- name: Trend
  property_count: 13
  slug: trend
- name: User
  property_count: 11
  slug: user
- name: UserInviteParam
  property_count: 2
  slug: userinviteparam
- name: VideoArticle
  property_count: 9
  slug: videoarticle
layout: provider
modified: '2026-06-13'
name: DEV Community
nav: Providers
network: true
overview: 'DEV Community publishes 19 APIs on the [APIs.io](https://apis.io/) network, including agent_sessions API, articles API, billboards API, and 16 more. Tagged areas include Developer Community, Articles, Blogging, Social, and Content.


  The DEV Community catalog on APIs.io includes 1 Spectral governance ruleset.


  DEV Community''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Devto Plans Pricing
  plan_count: 2
  slug: devto-plans-pricing
random_paper: 71
rate_limits:
- limit_count: 0
  name: Devto Rate Limits
  slug: devto-rate-limits
rules:
- name: DEV Community API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: devto-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.9
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 44.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/devto/refs/heads/main/screenshots/devto-2026-06-20T175951.png
security:
- kind: authentication
  name: Devto Authentication
  slug: devto-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Devto Domain Security
  slug: devto-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Devto Vulnerability Disclosure
  slug: devto-vulnerability-disclosure
  summary_line: disclosure policy published
slug: devto
tags:
- Developer Community
- Articles
- Blogging
- Social
- Content
- Open Source
website: https://dev.to
---
