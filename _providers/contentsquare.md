---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Contentsquare Agentic Access
  operation_count: 10
  slug: contentsquare-agentic-access
  summary_line: 10 operations · 2 acting
api_count: 1
apis:
- description: REST API for exporting Contentsquare metrics and raw analytics data. Authentication uses OAuth 2.0 client_credentials flow against https://api.contentsquare.com/v1/oauth/token, which returns a JWT acc
  name: Contentsquare Data Export API
  slug: data-export-api
- description: REST API for sending enrichment data batches into Contentsquare, enabling teams to merge first-party data with captured session data. Uses the same OAuth 2.0 client credentials authentication and dyna
  name: Contentsquare Enrichment API
  slug: enrichment-api
- baseURL: https://api.eu-west-1.production.contentsquare.com
  baseurl_source: declared
  description: The Authentication API from Contentsquare — 1 operation(s) for authentication.
  name: Contentsquare Authentication API
  slug: contentsquare-authentication-api
- baseURL: https://api.eu-west-1.production.contentsquare.com
  baseurl_source: declared
  description: The Exports API from Contentsquare — 2 operation(s) for exports.
  name: Contentsquare Exports API
  slug: contentsquare-exports-api
- baseURL: https://api.eu-west-1.production.contentsquare.com
  baseurl_source: declared
  description: The Fields API from Contentsquare — 3 operation(s) for fields.
  name: Contentsquare Fields API
  slug: contentsquare-fields-api
- baseURL: https://api.eu-west-1.production.contentsquare.com
  baseurl_source: declared
  description: The Runs API from Contentsquare — 3 operation(s) for runs.
  name: Contentsquare Runs API
  slug: contentsquare-runs-api
artifact_total: 18
collections:
- collection_type: open
  name: Contentsquare Data Export Authentication API
  slug: open-contentsquare-authentication-api
- collection_type: open
  name: Contentsquare Data Export Authentication Exports API
  slug: open-contentsquare-exports-api
- collection_type: open
  name: Contentsquare Data Export Authentication Fields API
  slug: open-contentsquare-fields-api
- collection_type: open
  name: Contentsquare Data Export Authentication Runs API
  slug: open-contentsquare-runs-api
- collection_type: open
  name: Contentsquare Data Export API
  slug: open-contentsquare
common:
- group: company
  title: ''
  type: Blog
  url: https://contentsquare.com/blog/
- group: agent
  href: https://artifacts.apis.io/contentsquare/agentic-access/contentsquare-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/contentsquare-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/contentsquare/security/contentsquare-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/contentsquare-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/contentsquare/security/contentsquare-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/contentsquare-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/contentsquare/security/contentsquare-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contentsquare-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/contentsquare/authentication/contentsquare-authentication.yml
  title: ''
  type: Authentication
  url: authentication/contentsquare-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/contentsquare
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/contentsquare
- group: company
  title: ''
  type: Website
  url: https://contentsquare.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.contentsquare.com/en/
- group: commercial
  title: ''
  type: Pricing
  url: https://contentsquare.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://contentsquare.com/request-demo/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.contentsquare.com/llms.txt
created: '2026-05-11'
description: Contentsquare is a digital experience analytics platform that captures every user interaction on web and mobile properties to surface friction points, conversion blockers, and behavioral insights via session replay, heatmaps, journey analysis, and zone-based analytics. The platform helps product, marketing, and UX teams optimize digital experiences with AI-driven recommendations. Contentsquare offers Data Export and Enrichment REST APIs authenticated via OAuth 2.0 client credentials with dynamic regional base URLs returned at authentication time.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/contentsquare.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.contentsquare.com over HTTP.
  name: Contentsquare MCP Server
  slug: contentsquare
modified: '2026-10-06'
name: Contentsquare
nav: Providers
network: true
overview: 'Contentsquare publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Exports API, Fields API, and 3 more. Tagged areas include Digital Experience Analytics, Product Analytics, Session Replay, Heatmaps, and Customer Experience.


  The Contentsquare catalog on APIs.io includes 1 Spectral governance ruleset.


  Contentsquare''s developer surface includes engineering blog, authentication, documentation, pricing, signup flow, and 8 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Contentsquare API Rules
  rule_count: 53
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 1
  slug: contentsquare-rules
score:
  band: thin
  composite: 34.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 13.6
    contract_quality: 46.8
    developer_ergonomics: 23.8
    discoverability: 75.0
    operational_transparency: 13.2
  previous_composite: 34.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/contentsquare/contentsquare-2026-06-20T175028.png
security:
- kind: authentication
  name: Contentsquare Authentication
  slug: contentsquare-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Contentsquare Domain Security
  slug: contentsquare-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Contentsquare Vulnerability Disclosure
  slug: contentsquare-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Contentsquare Trust Center
  slug: contentsquare-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018
slug: contentsquare
tags:
- Digital Experience Analytics
- Product Analytics
- Session Replay
- Heatmaps
- Customer Experience
- Conversion Optimization
- User Behavior
website: https://contentsquare.com
---
