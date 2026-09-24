---
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
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.4
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Sociallisteningapi Agentic Access
  operation_count: 43
  slug: sociallisteningapi-agentic-access
  summary_line: 43 operations
api_count: 1
apis:
- baseURL: https://api.sociallisteningapi.com
  baseurl_source: declared
  description: REST API that searches and retrieves public social data (LinkedIn, X, Reddit, Facebook, Hacker News, TikTok, YouTube, Pinterest, Instagram, Google and Discourse) with a normalized response, cursor pag
  name: SocialListeningAPI
  slug: sociallisteningapi
- description: Hosted remote MCP server for Claude and ChatGPT that exposes the SocialListeningAPI search tools (all sources except Discourse). Clients connect through OAuth 2.0 (authorization code + PKCE, scopes mc
  name: SocialListeningAPI MCP Server
  slug: sociallisteningapi-mcp
artifact_total: 17
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sociallisteningapi/refs/heads/main/mcp/sociallisteningapi-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/sociallisteningapi-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sociallisteningapi/refs/heads/main/agentic-access/sociallisteningapi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sociallisteningapi-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/sociallisteningapi/refs/heads/main/rate-limits/sociallisteningapi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sociallisteningapi-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/sociallisteningapi/refs/heads/main/plans/sociallisteningapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sociallisteningapi-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sociallisteningapi/refs/heads/main/rules/sociallisteningapi-rules.yml
  title: ''
  type: Spectral
  url: rules/sociallisteningapi-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sociallisteningapi/refs/heads/main/json-ld/sociallisteningapi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sociallisteningapi-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sociallisteningapi/refs/heads/main/vocabulary/sociallisteningapi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sociallisteningapi-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sociallisteningapi/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sociallisteningapi/refs/heads/main/data-model/sociallisteningapi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sociallisteningapi-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sociallisteningapi/refs/heads/main/conventions/sociallisteningapi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sociallisteningapi-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sociallisteningapi/refs/heads/main/scopes/sociallisteningapi-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/sociallisteningapi-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sociallisteningapi/refs/heads/main/lifecycle/sociallisteningapi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sociallisteningapi-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sociallisteningapi/refs/heads/main/errors/sociallisteningapi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sociallisteningapi-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sociallisteningapi/refs/heads/main/conformance/sociallisteningapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sociallisteningapi-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sociallisteningapi/refs/heads/main/overlays/sociallisteningapi-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sociallisteningapi-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sociallisteningapi/refs/heads/main/llms/sociallisteningapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sociallisteningapi-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sociallisteningapi/refs/heads/main/well-known/sociallisteningapi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sociallisteningapi-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sociallisteningapi/refs/heads/main/hosts/sociallisteningapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sociallisteningapi-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sociallisteningapi/refs/heads/main/vendors/sociallisteningapi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sociallisteningapi-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sociallisteningapi/refs/heads/main/security/sociallisteningapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sociallisteningapi-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sociallisteningapi/refs/heads/main/authentication/sociallisteningapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sociallisteningapi-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://sociallisteningapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://sociallisteningapi.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://sociallisteningapi.com/docs/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://sociallisteningapi.com/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://sociallisteningapi.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://sociallisteningapi.com/support
- group: company
  title: ''
  type: Blog
  url: https://sociallisteningapi.com/articles
- group: start
  title: ''
  type: SignUp
  url: https://app.sociallisteningapi.com?type=signup
- group: start
  title: ''
  type: Login
  url: https://app.sociallisteningapi.com?type=login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sociallisteningapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sociallisteningapi.com/privacy
created: '2026-09-23'
description: SocialListeningAPI is a social listening API for developers and AI agents that searches public posts, videos, profiles, forum discussions and Google results across LinkedIn, X, Reddit, Facebook, Hacker News, TikTok, YouTube, Pinterest, Instagram, Google and Discourse through one x-api-key and a normalized response shape. It is priced with one-time credit packs that do not expire, publishes an OpenAPI 3.1 document at api.sociallisteningapi.com/openapi.json, and runs an OAuth-protected remote MCP server for Claude and ChatGPT. It began as the API behind the Mentionkit social listening app and is operated by Nazare Studios Pty Ltd (Victoria, Australia).
image: https://sociallisteningapi.com/banner.jpg
json_schemas:
- name: CommentSearchResponse
  property_count: 9
  slug: sociallisteningapi-comment-search-response
- name: DiscourseSearchResponse
  property_count: 9
  slug: sociallisteningapi-discourse-search-response
- name: DiscoverySearchResponse
  property_count: 9
  slug: sociallisteningapi-discovery-search-response
- name: GoogleSearchResponse
  property_count: 9
  slug: sociallisteningapi-google-search-response
- name: ProfileResponse
  property_count: 9
  slug: sociallisteningapi-profile-response
- name: SocialSearchResponse
  property_count: 9
  slug: sociallisteningapi-social-search-response
jsonld:
- class_count: 24
  name: Sociallisteningapi Context
  property_count: 58
  slug: sociallisteningapi-context
layout: provider
mcp_servers:
- description: SocialListeningAPI's MCP connects public social search to Claude and ChatGPT. It is listed in Claude's connector directory and connects through OAuth; searches use credits from the approved workspace.
  name: SocialListeningAPI MCP
  slug: sociallisteningapi-mcp
modified: '2026-09-23'
name: SocialListeningAPI
nav: Providers
network: true
overview: 'SocialListeningAPI publishes 1 API on the [APIs.io](https://apis.io/) network: SocialListeningAPI. Tagged areas include Social Listening, Social Media, Search, Brand Monitoring, and Market Research.


  The SocialListeningAPI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SocialListeningAPI''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, support, engineering blog, and 25 more developer resources.'
plans:
- name: Sociallisteningapi Plans Pricing
  plan_count: 3
  slug: sociallisteningapi-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Sociallisteningapi Rate Limits
  slug: sociallisteningapi-rate-limits
rules:
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: SocialListeningAPI API Rules
  rule_count: 17
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 3
  slug: sociallisteningapi-rules
scopes:
- name: Sociallisteningapi Scopes
  scope_count: 0
  slug: sociallisteningapi-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 55.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 83.8
    catalog_earned_first_party: 20.0
    catalog_gap: 31.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 73.5
    developer_ergonomics: 49.4
    discoverability: 75.9
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Sociallisteningapi Authentication
  slug: sociallisteningapi-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Sociallisteningapi Domain Security
  slug: sociallisteningapi-domain-security
  summary_line: TLSv1.3
slug: sociallisteningapi
tags:
- Social Listening
- Social Media
- Search
- Brand Monitoring
- Market Research
- MCP
- Reddit
- LinkedIn
website: https://sociallisteningapi.com/
---
