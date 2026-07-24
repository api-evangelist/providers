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
    asyncapi_events: false
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
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Stackexchange Agentic Access
  operation_count: 70
  slug: stackexchange-agentic-access
  summary_line: 70 operations
api_count: 17
apis:
- description: Newer REST API powering Stack Overflow for Teams (private/internal instances). Resource-oriented (questions, answers, articles, comments, tags, users, collections, communities) with full CRUD and bear
  name: Stack Overflow for Teams API v3
  slug: stack-overflow-for-teams-api-v3
- description: OAuth access token introspection and invalidation.
  name: Stack Exchange Access Tokens API
  slug: stackexchange-access-tokens-api
- description: Answer objects — list, fetch by id, and per-question answers.
  name: Stack Exchange Answers API
  slug: stackexchange-answers-api
- description: Badges defined on a site — by id, name, type, and recipients.
  name: Stack Exchange Badges API
  slug: stackexchange-badges-api
- description: Comments attached to questions and answers across the network.
  name: Stack Exchange Comments API
  slug: stackexchange-comments-api
- description: Recent network events (1.5 minute live window) for the authenticated user.
  name: Stack Exchange Events API
  slug: stackexchange-events-api
- description: Custom response filter creation and inspection.
  name: Stack Exchange Filters API
  slug: stackexchange-filters-api
- description: Site-wide statistics, totals, and metadata.
  name: Stack Exchange Info API
  slug: stackexchange-info-api
- description: Convenience surfaces that infer the user from the OAuth access token.
  name: Stack Exchange Me API
  slug: stackexchange-me-api
- description: Generic post surfaces covering both questions and answers as `post` objects.
  name: Stack Exchange Posts API
  slug: stackexchange-posts-api
- description: Question objects across the network — list, fetch, related, linked, search-equivalents.
  name: Stack Exchange Questions API
  slug: stackexchange-questions-api
- description: Revision history for posts.
  name: Stack Exchange Revisions API
  slug: stackexchange-revisions-api
- description: Question search — basic title-match, full-text excerpts, and advanced.
  name: Stack Exchange Search API
  slug: stackexchange-search-api
- description: Enumeration and metadata for the 180+ Stack Exchange Q&A sites.
  name: Stack Exchange Sites API
  slug: stackexchange-sites-api
- description: Pending edits proposed by users awaiting review.
  name: Stack Exchange Suggested Edits API
  slug: stackexchange-suggested-edits-api
- description: Tag catalog, synonyms, wikis, top askers/answerers, and related tags.
  name: Stack Exchange Tags API
  slug: stackexchange-tags-api
- description: Site users, their reputation, badges, tags, top posts, timeline, and write surfaces.
  name: Stack Exchange Users API
  slug: stackexchange-users-api
artifact_total: 92
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stackexchange-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stackexchange-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stackexchange-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/stackexchange-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://stackexchange.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.stackexchange.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://stackapps.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/StackExchange
- group: company
  title: ''
  type: Blog
  url: https://stackoverflow.blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://stackoverflow.com/legal/api-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://stackoverflow.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://stackstatus.tumblr.com/
- group: other
  title: ''
  type: ApplicationRegistration
  url: https://stackapps.com/apps/oauth/register
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: build
  title: MCP Server (Stack Overflow)
  type: Tools
  url: https://github.com/StackExchange/Stack-MCP
- group: build
  title: MCP Server Documentation
  type: Tools
  url: https://api.stackexchange.com/docs/mcp-server
- group: build
  title: Stack Exchange Data Explorer
  type: Tools
  url: https://github.com/StackExchange/StackExchange.DataExplorer
- group: build
  title: Stacks Design System
  type: Tools
  url: https://github.com/StackExchange/Stacks
- group: commercial
  title: ''
  type: Plans
  url: plans/stackexchange-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stackexchange-rate-limits.yml
- group: design
  title: ''
  type: Rules
  url: rules/stackexchange-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/stackexchange-vocabulary.yml
created: '2026-05-28'
description: Stack Exchange is the network of Q&A communities founded by Joel Spolsky and Jeff Atwood and headlined by Stack Overflow, the largest community of software developers on the web. The Stack Exchange API v2.3 (api.stackexchange.com) is a single, read-mostly HTTP/JSON interface that spans 180+ Q&A sites — Stack Overflow, Server Fault, Super User, Ask Ubuntu, Stats, Math Overflow, and the long tail of topical communities — and exposes the entire Q&A graph (questions, answers, comments, users, tags, badges, reputation, revisions, notifications, inbox, suggested-edits, network sites) under a uniform method surface. Stack Exchange also operates Stack Overflow for Teams (private knowledge bases with its own v3 REST API) and ships an official Stack Overflow MCP server that grounds AI agents in community-verified content.
examples:
- key_count: 4
  name: Stackexchange Api V2 3 Access Token Example
  slug: stackexchange-api-v2-3-access-token-example
- key_count: 22
  name: Stackexchange Api V2 3 Answer Example
  slug: stackexchange-api-v2-3-answer-example
- key_count: 3
  name: Stackexchange Api V2 3 Badge Count Example
  slug: stackexchange-api-v2-3-badge-count-example
- key_count: 8
  name: Stackexchange Api V2 3 Badge Example
  slug: stackexchange-api-v2-3-badge-example
- key_count: 12
  name: Stackexchange Api V2 3 Comment Example
  slug: stackexchange-api-v2-3-comment-example
- key_count: 5
  name: Stackexchange Api V2 3 Event Example
  slug: stackexchange-api-v2-3-event-example
- key_count: 3
  name: Stackexchange Api V2 3 Filter Example
  slug: stackexchange-api-v2-3-filter-example
- key_count: 10
  name: Stackexchange Api V2 3 Inbox Item Example
  slug: stackexchange-api-v2-3-inbox-item-example
- key_count: 14
  name: Stackexchange Api V2 3 Info Example
  slug: stackexchange-api-v2-3-info-example
- key_count: 6
  name: Stackexchange Api V2 3 Notification Example
  slug: stackexchange-api-v2-3-notification-example
- key_count: 10
  name: Stackexchange Api V2 3 Post Example
  slug: stackexchange-api-v2-3-post-example
- key_count: 3
  name: Stackexchange Api V2 3 Privilege Item Example
  slug: stackexchange-api-v2-3-privilege-item-example
- key_count: 24
  name: Stackexchange Api V2 3 Question Example
  slug: stackexchange-api-v2-3-question-example
- key_count: 6
  name: Stackexchange Api V2 3 Reputation Change Example
  slug: stackexchange-api-v2-3-reputation-change-example
- key_count: 16
  name: Stackexchange Api V2 3 Revision Example
  slug: stackexchange-api-v2-3-revision-example
- key_count: 7
  name: Stackexchange Api V2 3 Shallow User Example
  slug: stackexchange-api-v2-3-shallow-user-example
- key_count: 13
  name: Stackexchange Api V2 3 Site Example
  slug: stackexchange-api-v2-3-site-example
- key_count: 11
  name: Stackexchange Api V2 3 Suggested Edit Example
  slug: stackexchange-api-v2-3-suggested-edit-example
- key_count: 7
  name: Stackexchange Api V2 3 Tag Example
  slug: stackexchange-api-v2-3-tag-example
- key_count: 3
  name: Stackexchange Api V2 3 Tag Score Example
  slug: stackexchange-api-v2-3-tag-score-example
- key_count: 5
  name: Stackexchange Api V2 3 Tag Synonym Example
  slug: stackexchange-api-v2-3-tag-synonym-example
- key_count: 25
  name: Stackexchange Api V2 3 User Example
  slug: stackexchange-api-v2-3-user-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stackexchange.png
json_schemas:
- name: AccessToken
  property_count: 4
  slug: stackexchange-api-v2-3-access-token
- name: Answer
  property_count: 22
  slug: stackexchange-api-v2-3-answer
- name: BadgeCount
  property_count: 3
  slug: stackexchange-api-v2-3-badge-count
- name: Badge
  property_count: 8
  slug: stackexchange-api-v2-3-badge
- name: Comment
  property_count: 12
  slug: stackexchange-api-v2-3-comment
- name: Event
  property_count: 5
  slug: stackexchange-api-v2-3-event
- name: Filter
  property_count: 3
  slug: stackexchange-api-v2-3-filter
- name: InboxItem
  property_count: 10
  slug: stackexchange-api-v2-3-inbox-item
- name: Info
  property_count: 14
  slug: stackexchange-api-v2-3-info
- name: Notification
  property_count: 6
  slug: stackexchange-api-v2-3-notification
- name: Post
  property_count: 10
  slug: stackexchange-api-v2-3-post
- name: PrivilegeItem
  property_count: 3
  slug: stackexchange-api-v2-3-privilege-item
- name: Question
  property_count: 24
  slug: stackexchange-api-v2-3-question
- name: ReputationChange
  property_count: 6
  slug: stackexchange-api-v2-3-reputation-change
- name: Revision
  property_count: 16
  slug: stackexchange-api-v2-3-revision
- name: ShallowUser
  property_count: 7
  slug: stackexchange-api-v2-3-shallow-user
- name: Site
  property_count: 13
  slug: stackexchange-api-v2-3-site
- name: SuggestedEdit
  property_count: 11
  slug: stackexchange-api-v2-3-suggested-edit
- name: Tag
  property_count: 7
  slug: stackexchange-api-v2-3-tag
- name: TagScore
  property_count: 3
  slug: stackexchange-api-v2-3-tag-score
- name: TagSynonym
  property_count: 5
  slug: stackexchange-api-v2-3-tag-synonym
- name: User
  property_count: 25
  slug: stackexchange-api-v2-3-user
json_structures:
- name: Stackexchange Api V2 3 Access Token Structure
  property_count: 4
  slug: stackexchange-api-v2-3-access-token-structure
- name: Stackexchange Api V2 3 Answer Structure
  property_count: 22
  slug: stackexchange-api-v2-3-answer-structure
- name: Stackexchange Api V2 3 Badge Count Structure
  property_count: 3
  slug: stackexchange-api-v2-3-badge-count-structure
- name: Stackexchange Api V2 3 Badge Structure
  property_count: 8
  slug: stackexchange-api-v2-3-badge-structure
- name: Stackexchange Api V2 3 Comment Structure
  property_count: 12
  slug: stackexchange-api-v2-3-comment-structure
- name: Stackexchange Api V2 3 Event Structure
  property_count: 5
  slug: stackexchange-api-v2-3-event-structure
- name: Stackexchange Api V2 3 Filter Structure
  property_count: 3
  slug: stackexchange-api-v2-3-filter-structure
- name: Stackexchange Api V2 3 Inbox Item Structure
  property_count: 10
  slug: stackexchange-api-v2-3-inbox-item-structure
- name: Stackexchange Api V2 3 Info Structure
  property_count: 14
  slug: stackexchange-api-v2-3-info-structure
- name: Stackexchange Api V2 3 Notification Structure
  property_count: 6
  slug: stackexchange-api-v2-3-notification-structure
- name: Stackexchange Api V2 3 Post Structure
  property_count: 10
  slug: stackexchange-api-v2-3-post-structure
- name: Stackexchange Api V2 3 Privilege Item Structure
  property_count: 3
  slug: stackexchange-api-v2-3-privilege-item-structure
- name: Stackexchange Api V2 3 Question Structure
  property_count: 24
  slug: stackexchange-api-v2-3-question-structure
- name: Stackexchange Api V2 3 Reputation Change Structure
  property_count: 6
  slug: stackexchange-api-v2-3-reputation-change-structure
- name: Stackexchange Api V2 3 Revision Structure
  property_count: 16
  slug: stackexchange-api-v2-3-revision-structure
- name: Stackexchange Api V2 3 Shallow User Structure
  property_count: 7
  slug: stackexchange-api-v2-3-shallow-user-structure
- name: Stackexchange Api V2 3 Site Structure
  property_count: 13
  slug: stackexchange-api-v2-3-site-structure
- name: Stackexchange Api V2 3 Suggested Edit Structure
  property_count: 11
  slug: stackexchange-api-v2-3-suggested-edit-structure
- name: Stackexchange Api V2 3 Tag Score Structure
  property_count: 3
  slug: stackexchange-api-v2-3-tag-score-structure
- name: Stackexchange Api V2 3 Tag Structure
  property_count: 7
  slug: stackexchange-api-v2-3-tag-structure
- name: Stackexchange Api V2 3 Tag Synonym Structure
  property_count: 5
  slug: stackexchange-api-v2-3-tag-synonym-structure
- name: Stackexchange Api V2 3 User Structure
  property_count: 25
  slug: stackexchange-api-v2-3-user-structure
jsonld:
- class_count: 22
  name: Stackexchange Api V2 3 Context
  property_count: 134
  slug: stackexchange-api-v2-3-context
layout: provider
modified: '2026-05-29'
name: Stack Exchange
nav: Providers
network: true
overview: 'Stack Exchange publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Access Tokens API, Answers API, Badges API, and 13 more. Tagged areas include Q And A, Developer Community, Knowledge Graph, Stack Overflow, and Stack Exchange.


  The Stack Exchange catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Stack Exchange''s developer surface includes authentication, documentation, engineering blog, tooling, and 18 more developer resources.'
plans:
- name: Stackexchange Plans Pricing
  plan_count: 3
  slug: stackexchange-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 6
  name: Stackexchange Rate Limits
  slug: stackexchange-rate-limits
rules:
- name: Stack Exchange API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: stackexchange-jsonschema-spectral-rules
- name: Stack Exchange API Rules
  rule_count: 48
  severity_counts:
    error: 16
    hint: 0
    info: 8
    warn: 24
  slug: stackexchange-spectral-rules
scopes:
- name: Stackexchange Scopes
  scope_count: 4
  slug: stackexchange-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: strong
  composite: 60.9
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 68.1
    developer_ergonomics: 30.4
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 52.6
  previous_composite: 60.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stackexchange/refs/heads/main/screenshots/stackexchange-2026-06-20T194445.png
security:
- kind: authentication
  name: Stackexchange Authentication
  slug: stackexchange-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Stackexchange Domain Security
  slug: stackexchange-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stackexchange
tags:
- Q And A
- Developer Community
- Knowledge Graph
- Stack Overflow
- Stack Exchange
- Reputation
- Tags
- Community
- MCP
- AI Grounding
website: https://stackexchange.com/
---
