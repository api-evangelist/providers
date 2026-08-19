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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 10
  human_in_the_loop: 2
  name: Threads Api Agentic Access
  operation_count: 32
  slug: threads-api-agentic-access
  summary_line: 32 operations · 10 acting · 2 human-in-the-loop
api_count: 9
apis:
- description: Authorization is a required step to get the necessary user permissions to act on behalf of the user. Please take a look at the [walkthrough of the authentication process](https://developers.facebook.c
  name: Threads Authorization API
  slug: threads-api-authorization-api
- description: 'This folder will enable you to: 1. Create a Media Container. The API will return a Media Container ID which will be used in the second step. 2. Publish a single Quote post.'
  name: Threads Post to Threads > Quote Threads Posts API
  slug: threads-api-post-to-threads-quote-threads-posts-api
- description: This folder will enable you to repost an original Threads post.
  name: Threads Post to Threads > Repost Threads Posts API
  slug: threads-api-post-to-threads-repost-threads-posts-api
- description: The Threads Reply Moderation API allows you to read and manage replies to users' own Threads.
  name: Threads Read And Manage Threads > Read and Manage Threads Replies API
  slug: threads-api-read-and-manage-threads-read-and-manage-threads-replies-api
- description: This folder will enable you to use the Threads API to retrieve details about a user's own replies.
  name: Threads Read And Manage Threads > Read Replies Media Objects API
  slug: threads-api-read-and-manage-threads-read-replies-media-objects-api
- description: This folder will enable you to use the Threads API to retrieve details about posts and accounts.
  name: Threads Read And Manage Threads > Read Threads Insights API
  slug: threads-api-read-and-manage-threads-read-threads-insights-api
- description: This folder will enable you to use the Threads API to retrieve details about posts.
  name: Threads Read And Manage Threads > Retrieve Threads Media Objects API
  slug: threads-api-read-and-manage-threads-retrieve-threads-media-objects-api
- description: This folder will enable you to get profile information about a Threads user.
  name: Threads Read And Manage Threads > Retrieve Threads Profiles API
  slug: threads-api-read-and-manage-threads-retrieve-threads-profiles-api
- description: This folder will enbale you to perform basic toubleshooting.
  name: Threads Troubleshooting API
  slug: threads-api-troubleshooting-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Threads Authorization API
  slug: open-threads-api-authorization-api
- collection_type: open
  name: Threads Authorization Post to Threads > Quote Threads Posts API
  slug: open-threads-api-post-to-threads-quote-threads-posts-api
- collection_type: open
  name: Threads Authorization Post to Threads > Repost Threads Posts API
  slug: open-threads-api-post-to-threads-repost-threads-posts-api
- collection_type: open
  name: Threads Authorization Read And Manage Threads > Read and Manage Threads Replies API
  slug: open-threads-api-read-and-manage-threads-read-and-manage-threads-replies-api
- collection_type: open
  name: Threads Authorization Read And Manage Threads > Read Replies Media Objects API
  slug: open-threads-api-read-and-manage-threads-read-replies-media-objects-api
- collection_type: open
  name: Threads Authorization Read And Manage Threads > Read Threads Insights API
  slug: open-threads-api-read-and-manage-threads-read-threads-insights-api
- collection_type: open
  name: Threads Authorization Read And Manage Threads > Retrieve Threads Media Objects API
  slug: open-threads-api-read-and-manage-threads-retrieve-threads-media-objects-api
- collection_type: open
  name: Threads Authorization Read And Manage Threads > Retrieve Threads Profiles API
  slug: open-threads-api-read-and-manage-threads-retrieve-threads-profiles-api
- collection_type: open
  name: Threads Authorization Troubleshooting API
  slug: open-threads-api-troubleshooting-api
- collection_type: open
  name: Threads API
  slug: open-threads-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/threads-api-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/threads-api-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/threads-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/threads-api-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/threads-meta
- group: company
  title: ''
  type: Website
  url: https://www.threads.net/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.facebook.com/docs/threads/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.facebook.com/docs/threads/get-started
- group: auth
  title: ''
  type: Authentication
  url: https://developers.facebook.com/docs/threads/get-started/get-access-tokens-and-permissions
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.facebook.com/docs/threads/changelog
- group: design
  title: ''
  type: Webhooks
  url: https://developers.facebook.com/docs/threads/webhooks
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/meta/threads/overview
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.facebook.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.facebook.com/privacy/policy/
created: '2024-11-16'
description: The Meta Threads API enables developers to build integrations for the Threads social media platform. It supports publishing text, image, video, carousel, and quote posts, reading and managing replies, accessing profile information, retrieving media insights, and managing account settings. Authentication uses OAuth 2.0 with scoped access tokens.
examples:
- key_count: 2
  name: Threads Api Get List Threads Example
  slug: threads-api-get-list-threads-example
- key_count: 2
  name: Threads Api Get Post Insights Example
  slug: threads-api-get-post-insights-example
finops:
- name: Threads Api Finops
  service_category: API
  slug: threads-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/threads-api.png
json_schemas:
- name: Thread
  property_count: 17
  slug: threads-api-thread
json_structures:
- name: Threads Api Thread Structure
  property_count: 0
  slug: threads-api-thread-structure
jsonld:
- class_count: 26
  name: Threads Api Context
  property_count: 0
  slug: threads-api-context
layout: provider
modified: '2026-05-19'
name: Threads
nav: Providers
network: true
overview: 'Threads publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Authorization API, Post to Threads > Quote Threads Posts API, Post to Threads > Repost Threads Posts API, and 6 more. Tagged areas include Social, Social Networks, Meta, Publishing, and Media.


  The Threads catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Threads'' developer surface includes authentication, getting-started guide, changelog, and 11 more developer resources.'
plans:
- name: Threads Api Plans Pricing
  plan_count: 3
  slug: threads-api-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 5
  name: Threads Api Rate Limits
  slug: threads-api-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Threads API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: threads-api-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Threads API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 3
  slug: threads-api-rules
score:
  band: thin
  composite: 39.2
  delta: -8.2
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 54.5
    developer_ergonomics: 38.1
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 31.6
  previous_composite: 47.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/threads-api/refs/heads/main/screenshots/threads-api-2026-08-17T083445.png
security:
- kind: authentication
  name: Threads Api Authentication
  slug: threads-api-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Threads Api Domain Security
  slug: threads-api-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Threads Api Vulnerability Disclosure
  slug: threads-api-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: threads-api
tags:
- Social
- Social Networks
- Meta
- Publishing
- Media
website: https://www.threads.net/
---
