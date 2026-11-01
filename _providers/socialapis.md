---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Socialapis Agentic Access
  operation_count: 53
  slug: socialapis-agentic-access
  summary_line: 53 operations
api_count: 1
apis:
- baseURL: https://api.socialapis.io
  baseurl_source: declared
  description: Your plan, usage and limits. These calls are free.
  name: SocialAPIs Account API
  slug: socialapis-account-api
- baseURL: https://api.socialapis.io
  baseurl_source: declared
  description: 'Public Facebook groups: details, ID, posts and videos.'
  name: SocialAPIs Facebook Groups API
  slug: socialapis-facebook-groups-api
- baseURL: https://api.socialapis.io
  baseurl_source: declared
  description: Marketplace listings, vehicles, rentals, sellers and categories.
  name: SocialAPIs Facebook Marketplace API
  slug: socialapis-facebook-marketplace-api
- baseURL: https://api.socialapis.io
  baseurl_source: declared
  description: Download Facebook images and videos.
  name: SocialAPIs Facebook Media API
  slug: socialapis-facebook-media-api
- baseURL: https://api.socialapis.io
  baseurl_source: declared
  description: 'Public Facebook pages: details, ID, posts, videos and reels.'
  name: SocialAPIs Facebook Pages API
  slug: socialapis-facebook-pages-api
- baseURL: https://api.socialapis.io
  baseurl_source: declared
  description: 'Facebook posts and videos: details, attachments, comments and replies.'
  name: SocialAPIs Facebook Posts API
  slug: socialapis-facebook-posts-api
- baseURL: https://api.socialapis.io
  baseurl_source: declared
  description: Keyword search for Facebook pages, people, posts, videos and locations.
  name: SocialAPIs Facebook Search API
  slug: socialapis-facebook-search-api
- baseURL: https://api.socialapis.io
  baseurl_source: declared
  description: Instagram profiles, posts, reels, highlights, search and locations.
  name: SocialAPIs Instagram API
  slug: socialapis-instagram-api
- baseURL: https://api.socialapis.io
  baseurl_source: declared
  description: Ads, advertisers and ad details from the Meta Ads Library.
  name: SocialAPIs Meta Ads Library API
  slug: socialapis-meta-ads-library-api
- baseURL: https://api.socialapis.io
  baseurl_source: declared
  description: The Other API from SocialAPIs — 1 operation(s) for other.
  name: SocialAPIs Other API
  slug: socialapis-other-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/socialapis/agentic-access/socialapis-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/socialapis-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/socialapis/plans/socialapis-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/socialapis-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/socialapis/rules/socialapis-rules.yml
  title: ''
  type: Spectral
  url: rules/socialapis-rules.yml
- group: design
  href: https://artifacts.apis.io/socialapis/json-ld/socialapis-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/socialapis-context.jsonld
- group: design
  href: https://artifacts.apis.io/socialapis/vocabulary/socialapis-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/socialapis-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/socialapis/data-model/socialapis-data-model.yml
  title: ''
  type: DataModel
  url: data-model/socialapis-data-model.yml
- group: design
  href: https://artifacts.apis.io/socialapis/errors/socialapis-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/socialapis-problem-types.yml
- group: design
  href: https://artifacts.apis.io/socialapis/conformance/socialapis-conformance.yml
  title: ''
  type: Conformance
  url: conformance/socialapis-conformance.yml
- group: agent
  href: https://artifacts.apis.io/socialapis/llms/socialapis-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/socialapis-llms.txt
- group: agent
  href: https://artifacts.apis.io/socialapis/mcp/socialapis-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/socialapis-mcp.yml
- group: agent
  href: https://artifacts.apis.io/socialapis/well-known/socialapis-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/socialapis-well-known.yml
- group: other
  href: https://artifacts.apis.io/socialapis/hosts/socialapis-hosts.yml
  title: ''
  type: Hosts
  url: hosts/socialapis-hosts.yml
- group: other
  href: https://artifacts.apis.io/socialapis/vendors/socialapis-vendors.yml
  title: ''
  type: Vendors
  url: vendors/socialapis-vendors.yml
- group: build
  href: https://artifacts.apis.io/socialapis/packages/socialapis-packages.yml
  title: ''
  type: SDKs
  url: packages/socialapis-packages.yml
- group: build
  href: https://artifacts.apis.io/socialapis/packages/socialapis-packages.yml
  title: ''
  type: Packages
  url: packages/socialapis-packages.yml
- group: auth
  href: https://artifacts.apis.io/socialapis/authentication/socialapis-authentication.yml
  title: ''
  type: Authentication
  url: authentication/socialapis-authentication.yml
- group: auth
  href: https://artifacts.apis.io/socialapis/security/socialapis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/socialapis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://socialapis.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://socialapis.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.socialapis.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.socialapis.io/api-reference/facebook
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.socialapis.io/getting-started/quick-start
- group: operate
  title: ''
  type: Support
  url: https://socialapis.io/contact-us
- group: company
  title: ''
  type: Blog
  url: https://socialapis.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SocialAPIsHub
- group: commercial
  title: ''
  type: Pricing
  url: https://socialapis.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://socialapis.io/auth/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://socialapis.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://socialapis.io/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/socialapis/workspace
created: '2026-10-18'
description: SocialAPIs provides developers with easy access to Facebook and other social media data through a suite of APIs. The platform offers real-time data on pages, groups, posts, and more, enabling developers to build applications for lead generation, analytics, and social listening. Trusted by over 5,000 developers, SocialAPIs delivers high uptime, fast responses, and comprehensive documentation to help integrate social data into products quickly and reliably.
image: https://socialapis.io/og-image.png
jsonld:
- class_count: 1
  name: Socialapis Context
  property_count: 4
  slug: socialapis-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.socialapis.io requiring an API key.
  name: SocialAPIs MCP Server
  slug: socialapis-mcp-yml
modified: '2026-10-18'
name: SocialAPIs
nav: Providers
network: true
overview: 'SocialAPIs publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Facebook Groups API, Facebook Marketplace API, and 7 more. Tagged areas include Company, Social Media, Data, and Developers.


  The SocialAPIs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SocialAPIs'' developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 23 more developer resources.'
plans:
- name: Socialapis Plans Pricing
  plan_count: 5
  slug: socialapis-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: SocialAPIs API Rules
  rule_count: 18
  severity_counts:
    error: 17
    hint: 0
    info: 1
    warn: 0
  slug: socialapis-rules
score:
  band: developing
  composite: 52.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 54.0
    catalog_earned_first_party: 12.0
    catalog_gap: 61.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 19.7
    contract_quality: 54.8
    developer_ergonomics: 69.0
    discoverability: 56.7
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Socialapis Authentication
  slug: socialapis-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Socialapis Domain Security
  slug: socialapis-domain-security
  summary_line: TLSv1.3
slug: socialapis
tags:
- Company
- Social Media
- Data
- Developers
website: https://socialapis.io/
---
