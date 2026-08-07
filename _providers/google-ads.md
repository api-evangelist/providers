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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.0
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Google Ads Agentic Access
  operation_count: 10
  slug: google-ads-agentic-access
  summary_line: 10 operations · 8 acting
api_count: 8
apis:
- description: JavaScript-based scripting interface for programmatically managing and querying Google Ads data directly in a browser-based IDE. Scripts enable automated changes to campaigns, ad groups, and reporting
  name: Google Ads Scripts
  slug: google-ads-scripts
- description: Manage ad groups within campaigns
  name: Google Ads Ad Groups API
  slug: google-ads-ad-groups-api
- description: Create and manage individual ads within ad groups
  name: Google Ads Ads API
  slug: google-ads-ads-api
- description: Manage bidding strategies for campaigns
  name: Google Ads Bidding Strategies API
  slug: google-ads-bidding-strategies-api
- description: Create, read, update, and remove advertising campaigns
  name: Google Ads Campaigns API
  slug: google-ads-campaigns-api
- description: Access and manage Google Ads customer account information
  name: Google Ads Customers API
  slug: google-ads-customers-api
- description: Manage keyword targeting criteria for ad groups
  name: Google Ads Keywords API
  slug: google-ads-keywords-api
- description: Query performance data using Google Ads Query Language (GAQL)
  name: Google Ads Reporting API
  slug: google-ads-reporting-api
artifact_total: 29
collections:
- collection_type: postman
  name: Google Ads Ad Groups API
  slug: postman-google-ads-ad-groups-api
- collection_type: postman
  name: Google Ad Groups Ads API
  slug: postman-google-ads-ads-api
- collection_type: postman
  name: Google Ads Ad Groups Bidding Strategies API
  slug: postman-google-ads-bidding-strategies-api
- collection_type: postman
  name: Google Ads Ad Groups Campaigns API
  slug: postman-google-ads-campaigns-api
- collection_type: postman
  name: Google Ads Ad Groups Customers API
  slug: postman-google-ads-customers-api
- collection_type: postman
  name: Google Ads Ad Groups Keywords API
  slug: postman-google-ads-keywords-api
- collection_type: postman
  name: Google Ads Ad Groups Reporting API
  slug: postman-google-ads-reporting-api
- collection_type: open
  name: Google Ads API
  slug: open-google-ads-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-ads/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-ads-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-ads-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-ads-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-ads-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-ads-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/google-ads-
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com/google-ads/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/google-ads/api/docs/first-call/overview
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/google-ads/api/docs/oauth/overview
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: company
  title: ''
  type: Blog
  url: https://ads-developers.googleblog.com/
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/google-ads/api/support
- group: build
  title: ''
  type: SDKs
  url: https://developers.google.com/google-ads/api/docs/client-libs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleads
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/google-ads-api
- group: operate
  title: ''
  type: Community
  url: https://groups.google.com/g/adwords-api
- group: start
  title: ''
  type: Console
  url: https://ads.google.com/
- group: start
  title: ''
  type: Signup
  url: https://ads.google.com/signup
- group: build
  title: ''
  type: Developer Tools
  url: https://developers.google.com/google-ads/api/docs/developer-toolkit/ai-assistant
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/google-ads-campaign-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-ads-context.jsonld
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/googleads/google-ads-mcp
created: '2024-01-01'
description: The Google Ads API is the modern programmatic interface to Google Ads and the next generation of the AdWords API. It enables developers to interact directly with the Google Ads platform, vastly increasing the efficiency of managing large or complex Google Ads accounts and campaigns.
finops:
- name: Google Ads Finops
  service_category: API
  slug: google-ads-finops
graphqls:
- description: This is a conceptual GraphQL schema for the Google Ads API. It is derived from the [Google Ads API v19 REST and Proto/gRPC services](https://developers.google.com/google-ads/api/reference/rpc) and rep
  name: Google Ads GraphQL Schema
  slug: google-ads-graphql
image: https://www.gstatic.com/images/branding/product/1x/google_ads_64dp.png
json_schemas:
- name: Google Ads Campaign
  property_count: 29
  slug: google-ads-campaign
jsonld:
- class_count: 70
  name: Google Ads Context
  property_count: 36
  slug: google-ads-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Google Ads
nav: Providers
network: true
overview: 'Google Ads publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Ad Groups API, Ads API, Bidding Strategies API, and 4 more. Tagged areas include Advertising, Campaign Management, Digital Advertising, Google, and Marketing.


  The Google Ads catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Ads'' developer surface includes authentication, developer portal, getting-started guide, engineering blog, support, Stack Overflow tag, developer console, and 18 more developer resources.'
plans:
- name: Google Ads Plans Pricing
  plan_count: 3
  slug: google-ads-plans-pricing
random_paper: 90
rate_limits:
- limit_count: 5
  name: Google Ads Rate Limits
  slug: google-ads-rate-limits
rules:
- name: Google Ads API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-ads-jsonschema-spectral-rules
scopes:
- name: Google Ads Scopes
  scope_count: 1
  slug: google-ads-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 64.9
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 75.9
    developer_ergonomics: 63.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 64.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-ads/refs/heads/main/screenshots/google-ads-2026-06-20T182011.png
security:
- kind: authentication
  name: Google Ads Authentication
  slug: google-ads-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Ads Domain Security
  slug: google-ads-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Ads Vulnerability Disclosure
  slug: google-ads-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-ads
tags:
- Advertising
- Campaign Management
- Digital Advertising
- Google
- Marketing
- PPC
website: https://developers.google.com/google-ads/api
---
