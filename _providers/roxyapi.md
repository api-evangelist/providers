---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Production REST API covering 14 spiritual intelligence domains with 210+ endpoints under a single API key, authenticated via X-API-Key header. Documented by a live OpenAPI 3.1 spec and interactive ref
  name: RoxyAPI REST API v2
  slug: roxyapi-rest-api-v2
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://roxyapi.com
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/roxyapi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/roxyapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/roxyapi-authentication.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/roxyapi-a2a.yml
- group: build
  title: ''
  type: Packages
  url: packages/roxyapi-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/roxyapi-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/roxyapi-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/roxyapi-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/roxyapi-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/roxyapi-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/roxyapi-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/roxyapi-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/roxyapi-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://roxyapi.com/policy/dpa
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/roxyapi-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/roxyapi-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://stats.uptimerobot.com/T0kPZKlAjf
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/roxyapi-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/roxyapi-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/roxyapi-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/roxyapi-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/roxyapi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/roxyapi-rate-limits.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/RoxyAPI/.github/blob/main/SECURITY.md
- group: start
  title: ''
  type: DeveloperPortal
  url: https://roxyapi.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://roxyapi.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://roxyapi.com/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://roxyapi.com/contact
- group: company
  title: ''
  type: Blog
  url: https://roxyapi.com/blogs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RoxyAPI
- group: commercial
  title: ''
  type: Pricing
  url: https://roxyapi.com/pricing
- group: start
  title: ''
  type: Login
  url: https://roxyapi.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://roxyapi.com/policy/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://roxyapi.com/policy/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/roxylabs-7113570/roxyapi
created: '2026-07-09'
description: Multi-domain spiritual intelligence API exposing 210+ endpoints across 14 domains (Western Astrology, Vedic Astrology, Forecast, Human Design, Chinese Astrology, Feng Shui, Numerology, Tarot, Biorhythm, I-Ching, Crystals, Dreams, Angel Numbers, Location/Timezone) under a single API key. Powered by the proprietary Roxy Ephemeris engine verified against NASA JPL Horizons DE441. Offers a live OpenAPI 3.1 contract, 15 remote MCP servers (14 per-domain plus a keyless docs server), llms.txt, an AGENTS.md agent playbook, an APIs.json index, an RFC 9727 api-catalog, typed SDKs in five languages, and drop-in UI components.
image: https://roxyapi.com/logo.png
layout: provider
mcp_servers:
- description: 'RoxyAPI ships 15 first-party remote MCP servers over Streamable HTTP: one per intelligence domain at https://roxyapi.com/mcp/{domain} (207 tools total, one per REST endpoint, X-API-Key secret-key auth'
  name: RoxyAPI remote MCP servers (14 per-domain + keyless docs server)
  slug: roxyapi-remote-mcp-servers-14-per-domain-keyless-docs-server
modified: '2026-09-03'
name: RoxyAPI
nav: Providers
network: true
overview: 'RoxyAPI publishes 1 API on the [APIs.io](https://apis.io/) network: REST API v2. Tagged areas include Astrology, Vedic Astrology, numerology, tarot, and human-design.


  RoxyAPI''s developer surface includes authentication, changelog, sandbox, API reference, getting-started guide, support, engineering blog, and 30 more developer resources.'
plans:
- name: Roxyapi Plans Pricing
  plan_count: 4
  slug: roxyapi-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 4
  name: Roxyapi Rate Limits
  slug: roxyapi-rate-limits
score:
  band: strong
  composite: 59.7
  coverage:
    artifact_dirs: 20
    catalog_gap: 57.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 42.8
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 26.7
    developer_ergonomics: 83.3
    discoverability: 70.4
    governance: 18.2
    operational_transparency: 78.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 16.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/roxyapi/refs/heads/main/screenshots/roxyapi-2026-09-02T154145.png
security:
- kind: authentication
  name: Roxyapi Authentication
  slug: roxyapi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Roxyapi Domain Security
  slug: roxyapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Roxyapi Vulnerability Disclosure
  slug: roxyapi-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: roxyapi
tags:
- Astrology
- Vedic Astrology
- numerology
- tarot
- human-design
- Forecast
- biorhythm
- iching
- crystals
- Dreams
- angel-numbers
- Location
- spiritual
- Wellness
- MCP Server
- OpenAPI
- llms-txt
- agent-native
website: https://roxyapi.com
---
