---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'The public WordPress REST API (wp-json) of the Local Infusion website at mylocalinfusion.com: the route index of the site''s content management system, catalogued as one site surface rather than as sep'
  name: Local Infusion Website (WordPress REST)
  slug: mylocalinfusion-com-website-wordpress-rest
- baseURL: https://mylocalinfusion.com/wp-json/
  baseurl_source: declared
  description: Two Model Context Protocol servers exposed by the WordPress MCP adapter. Both require authentication — mcp-oauth-server returned HTTP 401 with a correct RFC 9728 Bearer challenge and mcp-adapter-defau
  name: Local Infusion MCP API
  slug: local-infusion-mcp-api
artifact_total: 11
common:
- group: auth
  href: https://artifacts.apis.io/local-infusion/security/local-infusion-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/local-infusion-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/local-infusion/scopes/local-infusion-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/local-infusion-scopes.yml
- group: auth
  href: https://artifacts.apis.io/local-infusion/authentication/local-infusion-authentication.yml
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
- group: other
  href: https://artifacts.apis.io/local-infusion/overlays/local-infusion-wp-rest-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/local-infusion-wp-rest-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/local-infusion/mcp/local-infusion-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/local-infusion-mcp.yml
- group: build
  href: https://artifacts.apis.io/local-infusion/mcp/local-infusion-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/local-infusion-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/local-infusion/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/local-infusion/llms/local-infusion-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/local-infusion-llms.txt
- group: agent
  href: https://artifacts.apis.io/local-infusion/well-known/local-infusion-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/local-infusion-well-known.yml
- group: other
  href: https://artifacts.apis.io/local-infusion/well-known/local-infusion-robots.txt
  title: ''
  type: ContentSignal
  url: well-known/local-infusion-robots.txt
- group: design
  href: https://artifacts.apis.io/local-infusion/conventions/local-infusion-conventions.yml
  title: ''
  type: Conventions
  url: conventions/local-infusion-conventions.yml
- group: design
  href: https://artifacts.apis.io/local-infusion/errors/local-infusion-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/local-infusion-problem-types.yml
- group: design
  href: https://artifacts.apis.io/local-infusion/data-model/local-infusion-data-model.yml
  title: ''
  type: DataModel
  url: data-model/local-infusion-data-model.yml
- group: design
  href: https://artifacts.apis.io/local-infusion/lifecycle/local-infusion-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/local-infusion-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/local-infusion/conformance/local-infusion-conformance.yml
  title: ''
  type: Conformance
  url: conformance/local-infusion-conformance.yml
- group: build
  href: https://artifacts.apis.io/local-infusion/packages/local-infusion-packages.yml
  title: ''
  type: Packages
  url: packages/local-infusion-packages.yml
- group: commercial
  href: https://artifacts.apis.io/local-infusion/plans/local-infusion-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/local-infusion-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/local-infusion/rate-limits/local-infusion-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/local-infusion-rate-limits.yml
created: '2026-08-25'
description: 'Local Infusion is a tech-enabled outpatient infusion-therapy provider operating ambulatory infusion centers across thirteen US states — Connecticut, Florida, Maine, Maryland, Massachusetts, New Hampshire, New Jersey, New York, North Carolina, Ohio, South Carolina, Texas and Virginia — where patients with autoimmune, neurological, gastrointestinal and other chronic conditions receive specialty biologic infusions in private suites, supported by a dedicated Infusion Guide who handles referrals, prior authorization, benefits investigation and financial assistance. It sells care, not software: there is no developer programme, no product API, no SDK and no published pricing for any machine surface. It is catalogued here because its corporate WordPress site serves a live, self-describing REST API of 282 routes — including a publicly readable `location` custom post type carrying the company''s 75-center directory — because the same install fronts two Model Context Protocol servers
  guarded by an OAuth 2.1 authorization server the host advertises through RFC 8414 and RFC 9728 metadata, and because the site carries an unusually deliberate agent-discovery layer: llms.txt, llms-full.txt, and .well-known ai-manifest, brand-facts and llm-sitemap documents, with a robots.txt that explicitly allows GPTBot, ClaudeBot, PerplexityBot and Google-Extended.'
image: https://mylocalinfusion.com/wp-content/uploads/2024/11/Local-Infusion-window-logo.jpg
layout: provider
mcp_servers:
- description: 'Local Infusion''s corporate WordPress site exposes two live Model Context Protocol servers under the `mcp` REST namespace, guarded by an OAuth 2.1 authorization server the same host advertises via RFC '
  name: Local Infusion MCP Server
  slug: local-infusion-mcp-yml
modified: '2026-08-25'
name: Local Infusion
nav: Providers
network: true
overview: 'Local Infusion is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including MCP API, and 1 more. Tagged areas include Company, Healthcare, Health Services, Infusion Therapy, and Specialty Pharmacy.


  The Local Infusion catalog on APIs.io includes 1 Spectral governance ruleset.


  Local Infusion''s developer surface includes authentication, engineering blog, FAQ, and 25 more developer resources.'
plans:
- name: Local Infusion Plans Pricing
  plan_count: 0
  slug: local-infusion-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Local Infusion Rate Limits
  slug: local-infusion-rate-limits
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: Local Infusion API Rules
  rule_count: 66
  severity_counts:
    error: 59
    hint: 0
    info: 1
    warn: 6
  slug: local-infusion-rules
scopes:
- name: Local Infusion Scopes
  scope_count: 1
  slug: local-infusion-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 17.0
    developer_ergonomics: 20.8
    discoverability: 67.5
    operational_transparency: 0.0
  previous_composite: 24.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: site-plugin
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 40.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/local-infusion/local-infusion-2026-09-02T150317.png
security:
- kind: authentication
  name: Local Infusion Authentication
  slug: local-infusion-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Local Infusion Domain Security
  slug: local-infusion-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: Discover the Local Infusion API and MCP surface
  slug: local-infusion-discover-surface
- name: Read the Local Infusion center directory
  slug: local-infusion-read-center-directory
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
