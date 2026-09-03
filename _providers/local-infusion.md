---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: true
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.6
  scored_at: '2026-09-02'
api_count: 5
apis:
- baseURL: https://mylocalinfusion.com/wp-json/
  baseurl_source: declared
  description: WordPress core content API (posts, pages, media, taxonomies, settings) plus the site's `location` custom post type, which carries the company's public infusion-center directory. Read access to publish
  name: Local Infusion WordPress Content API
  slug: local-infusion-wp-v2-api
- baseURL: https://mylocalinfusion.com/wp-json/
  baseurl_source: declared
  description: Two Model Context Protocol servers exposed by the WordPress MCP adapter. Both require authentication — mcp-oauth-server returned HTTP 401 with a correct RFC 9728 Bearer challenge and mcp-adapter-defau
  name: Local Infusion MCP API
  slug: local-infusion-mcp-api
- baseURL: https://mylocalinfusion.com/wp-json/
  baseurl_source: declared
  description: WordPress Abilities API — the named-ability registry the MCP adapter projects tools from. Routes are advertised in the public discovery document but read access is capability-gated (/wp-json/wp-abilit
  name: Local Infusion WordPress Abilities API
  slug: local-infusion-wp-abilities-v1-api
- baseURL: https://mylocalinfusion.com/wp-json/
  baseurl_source: declared
  description: REST API index / namespace discovery, plus the /batch/v1 request batching endpoint.
  name: Local Infusion WordPress Root API
  slug: local-infusion-root-api
- baseURL: https://mylocalinfusion.com/wp-json/
  baseurl_source: declared
  description: oEmbed discovery and proxy endpoints served by the same WordPress install.
  name: Local Infusion oEmbed API
  slug: local-infusion-oembed-1-0-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/local-infusion-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/local-infusion-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/local-infusion-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://mylocalinfusion.com/
- group: company
  title: ''
  type: Blog
  url: https://mylocalinfusion.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://mylocalinfusion.com/feed/
- group: company
  title: ''
  type: Newsroom
  url: https://mylocalinfusion.com/press/
- group: company
  title: ''
  type: Careers
  url: https://mylocalinfusion.com/careers/
- group: operate
  title: ''
  type: FAQ
  url: https://mylocalinfusion.com/faqs/
- group: operate
  title: ''
  type: Contact
  url: https://mylocalinfusion.com/get-started/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mylocalinfusion.com/privacy-policy/
- group: other
  title: ''
  type: Accessibility
  url: https://mylocalinfusion.com/accessibility/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.nasdaqprivatemarket.com/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/local-infusion-wp-rest-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/local-infusion-wp-rest-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/local-infusion-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/local-infusion-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/local-infusion-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/local-infusion-well-known.yml
- group: other
  title: ''
  type: ContentSignal
  url: well-known/local-infusion-robots.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/local-infusion-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/local-infusion-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/local-infusion-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/local-infusion-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/local-infusion-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/local-infusion-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/local-infusion-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/local-infusion-rate-limits.yml
created: '2026-08-25'
description: 'Local Infusion is a tech-enabled outpatient infusion-therapy provider operating ambulatory infusion centers across thirteen US states — Connecticut, Florida, Maine, Maryland, Massachusetts, New Hampshire, New Jersey, New York, North Carolina, Ohio, South Carolina, Texas and Virginia — where patients with autoimmune, neurological, gastrointestinal and other chronic conditions receive specialty biologic infusions in private suites, supported by a dedicated Infusion Guide who handles referrals, prior authorization, benefits investigation and financial assistance. It sells care, not software: there is no developer programme, no product API, no SDK and no published pricing for any machine surface. It is catalogued here because its corporate WordPress site serves a live, self-describing REST API of 282 routes — including a publicly readable `location` custom post type carrying the company''s 75-center directory — because the same install fronts two Model Context Protocol servers
  guarded by an OAuth 2.1 authorization server the host advertises through RFC 8414 and RFC 9728 metadata, and because the site carries an unusually deliberate agent-discovery layer: llms.txt, llms-full.txt, and .well-known ai-manifest, brand-facts and llm-sitemap documents, with a robots.txt that explicitly allows GPTBot, ClaudeBot, PerplexityBot and Google-Extended.'
image: https://mylocalinfusion.com/wp-content/uploads/2024/11/Local-Infusion-window-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Local Infusion MCP Server
  slug: local-infusion-mcp-server
modified: '2026-08-25'
name: Local Infusion
nav: Providers
network: true
overview: 'Local Infusion publishes 5 APIs on the [APIs.io](https://apis.io/) network, including WordPress Content API, MCP API, WordPress Abilities API, and 2 more. Tagged areas include Company, Healthcare, Health Services, Infusion Therapy, and Specialty Pharmacy.


  Local Infusion''s developer surface includes authentication, engineering blog, FAQ, and 26 more developer resources.'
plans:
- name: Local Infusion Plans Pricing
  plan_count: 0
  slug: local-infusion-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Local Infusion Rate Limits
  slug: local-infusion-rate-limits
scopes:
- name: Local Infusion Scopes
  scope_count: 1
  slug: local-infusion-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 19
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.8
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 16.6
    developer_ergonomics: 16.1
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 24.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 65.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/local-infusion/refs/heads/main/screenshots/local-infusion-2026-09-02T150317.png
security:
- kind: authentication
  name: Local Infusion Authentication
  slug: local-infusion-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Local Infusion Domain Security
  slug: local-infusion-domain-security
  summary_line: TLSv1.3 · DMARC
slug: local-infusion
tags:
- Company
- Healthcare
- Health Services
- Infusion Therapy
- Specialty Pharmacy
- Ambulatory Care
- Patient Services
- Autoimmune
- Chronic Care
- MCP
- WordPress
website: https://mylocalinfusion.com/
---
