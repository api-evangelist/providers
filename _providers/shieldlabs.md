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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.7
  scored_at: '2026-09-03'
api_count: 2
apis:
- baseURL: https://api.shieldlabs.ai
  baseurl_source: declared
  description: 'Recommended snapshot reads on account.shieldlabs.ai (service: Shield.Portal.Admin). Authenticated with Private API Key. Response envelope `{ data, total }`.'
  name: ShieldLabs History API
  slug: shieldlabs-history-api-api
- baseURL: https://api.shieldlabs.ai
  baseurl_source: declared
  description: 'Profile, balance, and alternate History on api.shieldlabs.ai (service: Shield.Core). Authenticated with Secret Key headers. History returns a PascalCase JSON array.'
  name: ShieldLabs Management API
  slug: shieldlabs-management-api-api
- baseURL: https://api.shieldlabs.ai
  baseurl_source: declared
  description: The ShieldLabs API API from ShieldLabs — 0 operation(s) for shieldlabs api.
  name: ShieldLabs ShieldLabs API
  slug: shieldlabs-shieldlabs-api-api
artifact_total: 12
asyncapis:
- description: ''
  name: Shieldlabs Webhooks
  slug: shieldlabs-webhooks
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/ShieldLabs-ai/shieldlabs-openapi/blob/main/LICENSE
- group: other
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
  title: ''
  type: Authentication
  url: authentication/shieldlabs-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shieldlabs-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/shieldlabs-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/shieldlabs-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shieldlabs-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/shieldlabs-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shieldlabs-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/shieldlabs-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.shieldlabs.ai/changelog
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/shieldlabs-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/shieldlabs-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/shieldlabs-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/shieldlabs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/shieldlabs-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/shieldlabs-conformance.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.shieldlabs.ai/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/shieldlabs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shieldlabs-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/shieldlabs-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/shieldlabs-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/shieldlabs-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/shieldlabs-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shieldlabs-llms.txt
created: '2026-08-19'
description: 'Anonymous visitor identification and fraud-prevention platform. A browser ES-module snippet loaded from cdn.shieldlabs.ai collects 100+ device and network signals and returns six persistent identifiers (DeviceID, VisitorID, CookieID, SessionID, RequestID and a caller-supplied hashed UserHID) plus an explainable 0-100 Risk Score built from weighted anonymity signals — VPN, proxy, Tor, privacy relay, datacenter, IP reputation, anti-detect browser, geolocation spoofing, OS mismatch, incognito, browser automation and suspicious paid clicks. ShieldLabs deliberately makes no allow/challenge/block decision: it returns the score and the signals behind it, and the customer''s own code owns the verdict. Delivery is a signed at-most-once webhook (identification.scored, HMAC-SHA256 in X-Shield-Signature, no retries), backed by two server-side REST surfaces — a free History API on account.shieldlabs.ai and a billed Management API on api.shieldlabs.ai — described by a public OpenAPI 3.1
  specification the company maintains in its own MIT-licensed GitHub repo. Self-serve and per-identification priced, with a 5,000-identification free tier and no sales gate.'
examples:
- key_count: 4
  name: Shieldlabs Identification Scored Example
  slug: shieldlabs-identification-scored-example
image: https://shieldlabs.ai/og/home.png
json_schemas:
- name: ShieldLabs webhook event
  property_count: 4
  slug: shieldlabs-identification-scored.schema
layout: provider
mcp_servers:
- description: ''
  name: ShieldLabs MCP Server
  slug: shieldlabs-mcp-server
modified: '2026-08-19'
name: ShieldLabs
nav: Providers
network: true
overview: 'ShieldLabs publishes 3 APIs on the [APIs.io](https://apis.io/) network: History API, Management API, and ShieldLabs API. Tagged areas include Fraud Detection, Abuse Prevention, Visitor Identification, Device Fingerprinting, and Bot Detection.


  The ShieldLabs catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ShieldLabs'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 35 more developer resources.'
plans:
- name: Shieldlabs Plans Pricing
  plan_count: 4
  slug: shieldlabs-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Shieldlabs Rate Limits
  slug: shieldlabs-rate-limits
score:
  band: strong
  composite: 63.1
  coverage:
    artifact_dirs: 25
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 4.5
    contract_quality: 65.8
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 68.4
  previous_composite: 63.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shieldlabs/refs/heads/main/screenshots/shieldlabs-2026-09-02T155148.png
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
slug: shieldlabs
tags:
- Fraud Detection
- Abuse Prevention
- Visitor Identification
- Device Fingerprinting
- Bot Detection
- vpn-proxy-detection
- Risk Scoring
- Identity
- Security
- Webhook
- Anti-Fraud
- traffic-quality
website: https://docs.shieldlabs.ai/
---
