---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: na
    mcp_server: documented
    mcp_tool_quality: full
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 48.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://account.shieldlabs.ai/api
  baseurl_source: declared
  description: Recommended snapshot reads on account.shieldlabs.ai. Authenticated with a Private API Key. Response envelope `{ data, total }`, limit/offset pagination, newest first. Free — reads do not consume reque
  name: ShieldLabs History API
  slug: shieldlabs-history-api-api
- baseURL: https://api.shieldlabs.ai
  baseurl_source: declared
  description: 'Profile and balance on api.shieldlabs.ai. Authenticated with Secret Key headers (`Authorization: Bearer` plus `X-Shield-Domain`). Its `GET /v1/history` path returns a PascalCase JSON array and is DEPR'
  name: ShieldLabs Management API
  slug: shieldlabs-management-api-api
- baseURL: https://api.shieldlabs.ai
  baseurl_source: declared
  description: The event half of the ShieldLabs contract. This document carries no REST paths — it holds the OpenAPI 3.1 top-level `webhooks` object describing `identification.scored`, the signed at-most-once envelo
  name: ShieldLabs API
  slug: shieldlabs-shieldlabs-api-api
artifact_total: 16
asyncapis:
- description: ''
  name: Shieldlabs Webhooks
  slug: shieldlabs-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://shieldlabs.ai
- group: commercial
  title: ''
  type: License
  url: https://github.com/ShieldLabs-ai/shieldlabs-openapi/blob/main/LICENSE
- group: other
  href: https://artifacts.apis.io/shieldlabs/overlays/shieldlabs-server-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/shieldlabs-server-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.shieldlabs.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.shieldlabs.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.shieldlabs.ai/api/server-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.shieldlabs.ai/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.shieldlabs.ai/support
- group: company
  title: ''
  type: Blog
  url: https://shieldlabs.ai/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://shieldlabs.ai/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ShieldLabs-ai
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ShieldLabs-ai/shieldlabs-openapi
- group: commercial
  title: ''
  type: Pricing
  url: https://shieldlabs.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.shieldlabs.ai/signup
- group: start
  title: ''
  type: Login
  url: https://app.shieldlabs.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.shieldlabs.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.shieldlabs.ai/legal/privacy-policy
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Shieldlabs_ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shieldlabs-ai
- group: auth
  href: https://artifacts.apis.io/shieldlabs/authentication/shieldlabs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/shieldlabs-authentication.yml
- group: design
  href: https://artifacts.apis.io/shieldlabs/conventions/shieldlabs-conventions.yml
  title: ''
  type: Conventions
  url: conventions/shieldlabs-conventions.yml
- group: design
  href: https://artifacts.apis.io/shieldlabs/conventions/shieldlabs-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/shieldlabs-conventions.yml
- group: design
  href: https://artifacts.apis.io/shieldlabs/errors/shieldlabs-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/shieldlabs-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/shieldlabs/rate-limits/shieldlabs-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/shieldlabs-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/shieldlabs/plans/shieldlabs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/shieldlabs-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/shieldlabs/lifecycle/shieldlabs-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/shieldlabs-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/shieldlabs/lifecycle/shieldlabs-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/shieldlabs-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/shieldlabs/changelog/shieldlabs-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/shieldlabs-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.shieldlabs.ai/changelog
- group: design
  href: https://artifacts.apis.io/shieldlabs/asyncapi/shieldlabs-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/shieldlabs-webhooks.yml
- group: start
  href: https://artifacts.apis.io/shieldlabs/sandbox/shieldlabs-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/shieldlabs-sandbox.yml
- group: design
  href: https://artifacts.apis.io/shieldlabs/components/shieldlabs-components.yml
  title: ''
  type: Components
  url: components/shieldlabs-components.yml
- group: build
  href: https://artifacts.apis.io/shieldlabs/packages/shieldlabs-packages.yml
  title: ''
  type: Packages
  url: packages/shieldlabs-packages.yml
- group: build
  href: https://artifacts.apis.io/shieldlabs/packages/shieldlabs-packages.yml
  title: ''
  type: SDKs
  url: packages/shieldlabs-packages.yml
- group: design
  href: https://artifacts.apis.io/shieldlabs/conformance/shieldlabs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/shieldlabs-conformance.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.shieldlabs.ai/security
- group: auth
  href: https://artifacts.apis.io/shieldlabs/security/shieldlabs-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/shieldlabs-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/shieldlabs/security/shieldlabs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shieldlabs-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/shieldlabs/well-known/shieldlabs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/shieldlabs-well-known.yml
- group: agent
  href: https://artifacts.apis.io/shieldlabs/mcp/shieldlabs-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/shieldlabs-mcp.yml
- group: build
  href: https://artifacts.apis.io/shieldlabs/mcp/shieldlabs-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/shieldlabs-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/shieldlabs/a2a/shieldlabs-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/shieldlabs-a2a.yml
- group: agent
  href: https://artifacts.apis.io/shieldlabs/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/shieldlabs/llms/shieldlabs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shieldlabs-llms.txt
- group: agent
  title: ''
  type: LLMsFullTxt
  url: https://shieldlabs.ai/llms-full.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://shieldlabs.ai/llms.txt
- group: build
  title: ''
  type: SDKs
  url: https://github.com/orgs/ShieldLabs-ai/repositories
created: '2026-08-19'
description: 'Anonymous visitor identification and fraud-prevention platform. A browser ES-module snippet loaded from cdn.shieldlabs.ai collects 100+ device and network signals and returns six persistent identifiers (DeviceID, VisitorID, CookieID, SessionID, RequestID and a caller-supplied hashed UserHID) plus an explainable 0-100 Risk Score built from weighted anonymity signals — VPN, proxy, Tor, privacy relay, datacenter, IP reputation, anti-detect browser, geolocation spoofing, OS mismatch, incognito, browser automation and suspicious paid clicks. ShieldLabs deliberately makes no allow/challenge/block decision: it returns the score and the signals behind it, and the customer''s own code owns the verdict. Delivery is a signed at-most-once webhook (identification.scored, HMAC-SHA256 in X-Shield-Signature, no retries), backed by two server-side REST surfaces on account.shieldlabs.ai and api.shieldlabs.ai — both read-only, neither consuming request balance — described by a public OpenAPI
  3.1 specification the company maintains in its own MIT-licensed GitHub repo and serves from its docs host. The Management API''s history path was deprecated on 2026-09-01 with a dated Sunset of 2027-01-01, a named successor, and RFC 8594 Deprecation/Sunset/Link headers. Self-serve and per-identification priced, with a 5,000-identification free tier and no sales gate.'
examples:
- key_count: 4
  name: Shieldlabs Identification Scored Example
  slug: shieldlabs-identification-scored-example
finops:
- has_sources: true
  method: derived
  name: Shieldlabs Finops
  primary_unit: identification
  service_category: ''
  slug: shieldlabs-finops
  template: false
image: https://shieldlabs.ai/og/home.png
json_schemas:
- name: ShieldLabs webhook event
  property_count: 4
  slug: shieldlabs-identification-scored.schema
layout: provider
mcp_servers:
- description: Remote MCP server at docs.shieldlabs.ai over HTTP; 3 tools listed.
  name: ShieldLabs MCP Server
  slug: shieldlabs
modified: '2026-09-16'
name: ShieldLabs
nav: Providers
network: true
overview: 'ShieldLabs publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including History API, Management API, and 1 more. Tagged areas include Fraud Prevention, Abuse Prevention, Visitor Identification, Device Fingerprinting, and Bot Detection.


  The ShieldLabs catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  ShieldLabs'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 40 more developer resources.'
plans:
- name: Shieldlabs Plans Pricing
  plan_count: 7
  slug: shieldlabs-plans-pricing
- name: Shieldlabs Price Estimates
  plan_count: 0
  slug: shieldlabs-price-estimates
random_paper: 19
rate_limits:
- limit_count: 7
  name: Shieldlabs Rate Limits
  slug: shieldlabs-rate-limits
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: ShieldLabs API Rules
  rule_count: 49
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 1
  slug: shieldlabs-rules
score:
  band: exemplar
  composite: 69.8
  coverage:
    artifact_dirs: 32
    catalog_earned: 73.9
    catalog_earned_first_party: 24.0
    catalog_gap: 41.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 77.6
    contract_governance: 18.2
    contract_quality: 66.7
    developer_ergonomics: 78.6
    discoverability: 75.0
    operational_transparency: 76.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 69.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/shieldlabs/shieldlabs-2026-09-02T155148.png
security:
- kind: authentication
  name: Shieldlabs Authentication
  slug: shieldlabs-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Shieldlabs Domain Security
  slug: shieldlabs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Shieldlabs Vulnerability Disclosure
  slug: shieldlabs-vulnerability-disclosure
  summary_line: Hackerone · contact published
skill_count: 1
skills:
- name: Shieldlabs
  slug: shieldlabs-shieldlabs
slug: shieldlabs
tags:
- Fraud Prevention
- Abuse Prevention
- Visitor Identification
- Device Fingerprinting
- Bot Detection
- vpn-proxy-detection
- Risk Scoring
- Identity
- Security
- Webhook
- traffic-quality
- A2A
website: https://shieldlabs.ai
---
