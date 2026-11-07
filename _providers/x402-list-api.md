---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://x402-list.com/api/v1
  baseurl_source: declared
  description: On-demand paid AI assessment of a service shortlist (x402)
  name: x402 List API Assess API
  slug: x402-list-api-assess-api
- baseURL: https://x402-list.com/api/v1
  baseurl_source: declared
  description: 'Change events detected on the live x402 wire: payTo rotations, price moves, and schema changes'
  name: x402 List API Changes API
  slug: x402-list-api-changes-api
- baseURL: https://x402-list.com/api/v1
  baseurl_source: declared
  description: Access monitoring check logs - the raw heartbeat of the x402 ecosystem
  name: x402 List API Checks API
  slug: x402-list-api-checks-api
- baseURL: https://x402-list.com/api/v1
  baseurl_source: declared
  description: Independently on-chain-verified USDC settlement volume per x402 facilitator (multi-chain)
  name: x402 List API Facilitators API
  slug: x402-list-api-facilitators-api
- baseURL: https://x402-list.com/api/v1
  baseurl_source: declared
  description: Rank the best x402 service(s) for a need (the public HTTP recommender)
  name: x402 List API Recommender API
  slug: x402-list-api-recommender-api
- baseURL: https://x402-list.com/api/v1
  baseurl_source: declared
  description: 'Reference data: supported networks, categories, and service tags'
  name: x402 List API Reference API
  slug: x402-list-api-reference-api
- baseURL: https://x402-list.com/api/v1
  baseurl_source: declared
  description: Browse and query x402 services, their endpoints, uptime, and pricing
  name: x402 List API Services API
  slug: x402-list-api-services-api
- baseURL: https://x402-list.com/api/v1
  baseurl_source: declared
  description: Aggregate statistics about the x402 ecosystem
  name: x402 List API Stats API
  slug: x402-list-api-stats-api
- baseURL: https://x402-list.com/api/v1
  baseurl_source: declared
  description: Get a quick health overview of all monitored services
  name: x402 List API Status API
  slug: x402-list-api-status-api
- baseURL: https://x402-list.com/api/v1
  baseurl_source: declared
  description: Submit new x402 services or facilitators for review and listing
  name: x402 List API Submissions API
  slug: x402-list-api-submissions-api
- baseURL: https://x402-list.com/api/v1
  baseurl_source: declared
  description: Post paid suggestions for the directory (feedback in x402)
  name: x402 List API Suggestions API
  slug: x402-list-api-suggestions-api
artifact_total: 22
common:
- group: commercial
  href: https://artifacts.apis.io/x402-list-api/plans/x402-list-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/x402-list-api-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/x402-list-api/rate-limits/x402-list-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/x402-list-api-rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://www.x402-list.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.x402-list.com/feed.xml
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.x402-list.com/mcp
- group: agent
  href: https://artifacts.apis.io/x402-list-api/mcp/x402-list-api-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/x402-list-api-mcp.yml
- group: other
  href: https://artifacts.apis.io/x402-list-api/overlays/x402-list-api-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/x402-list-api-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/x402-list-api/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.x402-list.com/
- group: auth
  href: https://artifacts.apis.io/x402-list-api/security/x402-list-api-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/x402-list-api-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/x402-list-api/security/x402-list-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/x402-list-api-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/x402-list-api/well-known/x402-list-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/x402-list-api-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://x402-list.com/.well-known/api-catalog
- group: auth
  href: https://artifacts.apis.io/x402-list-api/well-known/x402-list-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/x402-list-api-security.txt
- group: auth
  href: https://artifacts.apis.io/x402-list-api/security/x402-list-api-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/x402-list-api-vulnerability-disclosure.yml
- group: other
  title: ''
  type: ContentSignal
  url: https://x402-list.com/robots.txt
- group: other
  title: ''
  type: APIsJSON
  url: https://x402-list.com/.well-known/apis.json
- group: build
  href: https://artifacts.apis.io/x402-list-api/packages/x402-list-api-packages.yml
  title: ''
  type: Packages
  url: packages/x402-list-api-packages.yml
- group: company
  title: ''
  type: Blog
  url: https://x402-list.com/blog
- group: operate
  title: ''
  type: Support
  url: https://x402-list.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://x402-list.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://x402-list.com/privacy
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/mcccsm/x402-list-mcp
created: '2026-09-02'
description: An open, machine-readable, live-monitored directory of services that accept x402 protocol payments (HTTP 402 Payment Required). Self-described as agent-first, it exposes service listings, uptime metrics, pricing, facilitator settlement data, and rankings as JSON for autonomous agents, aggregators, and integrations.
finops:
- has_sources: true
  method: derived
  name: X402 List Api Finops
  primary_unit: submission
  service_category: ''
  slug: x402-list-api-finops
  template: false
image: https://x402-list.com/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: x402 List API MCP Server
  slug: mcp
modified: '2026-10-06'
name: x402 List API
nav: Providers
network: true
overview: 'x402 List API publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Assess API, Changes API, Checks API, and 8 more. Tagged areas include x402, Cryptocurrency, 402, Agentic Payments, and API Directory.


  The x402 List API catalog on APIs.io includes 1 Spectral governance ruleset.


  x402 List API''s developer surface includes engineering blog, support, and 21 more developer resources.'
plans:
- name: X402 List Api Plans Pricing
  plan_count: 6
  slug: x402-list-api-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: X402 List Api Rate Limits
  slug: x402-list-api-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 46
  extends:
  - spectral:oas
  name: x402 List API — spectral rules
  rule_count: 5
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 2
  slug: x402-list-api-spectral
score:
  band: strong
  composite: 59.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 63.8
    catalog_earned_first_party: 20.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 71.1
    contract_governance: 15.9
    contract_quality: 56.5
    developer_ergonomics: 58.9
    discoverability: 85.0
    operational_transparency: 68.4
  previous_composite: 58.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 11
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 27.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/x402-list-api/x402-list-api-2026-10-11T194809.png
security:
- kind: authentication
  name: X402 List Api Authentication
  slug: x402-list-api-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: X402 List Api Domain Security
  slug: x402-list-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: X402 List Api Vulnerability Disclosure
  slug: x402-list-api-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: compare-x402-settlement-rails
  slug: compare-x402-settlement-rails
- name: list-a-service-in-the-x402-directory
  slug: list-a-service-in-the-x402-directory
- name: pick-and-verify-an-x402-service
  slug: pick-and-verify-an-x402-service
slug: x402-list-api
tags:
- x402
- Cryptocurrency
- '402'
- Agentic Payments
- API Directory
- Registry
- AI Agents
- Blockchain
- Developer Tools
- Uptime Monitoring
website: https://www.x402-list.com/
---
