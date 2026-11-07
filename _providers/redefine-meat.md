---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Two live Model Context Protocol endpoints served from the same WordPress installation and advertised through RFC 9728 OAuth 2.0 Protected Resource Metadata. Both are OAuth-gated - an anonymous tools/l
  name: Redefine Meat MCP Server
  slug: mcp
- description: 'The public WordPress REST API (wp-json) of the Redefine Meat website at www.redefinemeat.com: the route index of the site''s content management system, catalogued as one site surface rather than as sep'
  name: Redefine Meat Website (WordPress REST)
  slug: redefinemeat-com-website-wordpress-rest
artifact_total: 12
asyncapis:
- description: ''
  name: Redefine Meat Webhooks
  slug: redefine-meat-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-redefine-meat-wp-rest-index-original
common:
- group: other
  href: https://artifacts.apis.io/redefine-meat/overlays/redefine-meat-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/redefine-meat-content-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/redefine-meat/security/redefine-meat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/redefine-meat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.redefinemeat.com/
- group: other
  title: ''
  type: Company
  url: https://www.redefinemeat.com/company/
- group: other
  title: ''
  type: Products
  url: https://www.redefinemeat.com/products/
- group: operate
  title: ''
  type: Support
  url: https://www.redefinemeat.com/contact/
- group: operate
  title: ''
  type: FAQ
  url: https://www.redefinemeat.com/faq/
- group: company
  title: ''
  type: Blog
  url: https://www.redefinemeat.com/blogs/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.redefinemeat.com/feed/
- group: company
  title: ''
  type: Press
  url: https://www.redefinemeat.com/news-media/
- group: company
  title: ''
  type: Careers
  url: https://www.redefinemeat.com/careers/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.redefinemeat.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.redefinemeat.com/privacy-policy/
- group: other
  title: ''
  type: Imprint
  url: https://www.redefinemeat.com/imprint/
- group: other
  title: ''
  type: WhereToBuy
  url: https://www.redefinemeat.com/where-to-find/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/redefine-meat-stock
- group: agent
  href: https://artifacts.apis.io/redefine-meat/well-known/redefine-meat-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/redefine-meat-well-known.yml
- group: auth
  href: https://artifacts.apis.io/redefine-meat/authentication/redefine-meat-authentication.yml
  title: ''
  type: Authentication
  url: authentication/redefine-meat-authentication.yml
- group: auth
  href: https://artifacts.apis.io/redefine-meat/scopes/redefine-meat-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/redefine-meat-scopes.yml
- group: design
  href: https://artifacts.apis.io/redefine-meat/conventions/redefine-meat-conventions.yml
  title: ''
  type: Conventions
  url: conventions/redefine-meat-conventions.yml
- group: design
  href: https://artifacts.apis.io/redefine-meat/errors/redefine-meat-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/redefine-meat-problem-types.yml
- group: design
  href: https://artifacts.apis.io/redefine-meat/lifecycle/redefine-meat-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/redefine-meat-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/redefine-meat/conformance/redefine-meat-conformance.yml
  title: ''
  type: Conformance
  url: conformance/redefine-meat-conformance.yml
- group: design
  href: https://artifacts.apis.io/redefine-meat/data-model/redefine-meat-data-model.yml
  title: ''
  type: DataModel
  url: data-model/redefine-meat-data-model.yml
- group: agent
  href: https://artifacts.apis.io/redefine-meat/llms/redefine-meat-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/redefine-meat-llms.txt
- group: agent
  href: https://artifacts.apis.io/redefine-meat/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-05'
description: 'Redefine Meat is an Israeli food-technology company, founded in 2018, that manufactures plant-based whole-cut meat alternatives it markets as New-Meat, using proprietary industrial 3D printing together with plant-protein formulations it calls Alt-Muscle, Alt-Fat and Alt-Blood. Its range spans steaks, burgers, shawarma, beef mince, lamb kofta, pulled beef and bratwurst across consumer (B2C) and foodservice (B2B / PRO) lines, sold through restaurants, hotels, caterers and retail in the United Kingdom, Germany, the Netherlands, France and Israel. Redefine Meat operates no developer program, but its own website at www.redefinemeat.com runs on WordPress and WooCommerce and exposes a genuinely public, machine-readable API surface: a WordPress REST API discovery index advertising 845 routes across 30 namespaces, an anonymously readable WooCommerce Store API for products, categories and cart, and two OAuth-gated Model Context Protocol endpoints advertised through RFC 8414 and RFC 9728
  well-known metadata.'
image: https://www.redefinemeat.com/wp-content/uploads/2023/11/Europe_Retail_Support_1920x800.jpg
layout: provider
mcp_servers:
- description: www.redefinemeat.com serves two live Model Context Protocol endpoints from its WordPress installation, advertised through RFC 9728 OAuth 2.0 Protected Resource Metadata at /.well-known/oauth-protected
  name: Redefine Meat MCP Server
  slug: redefine-meat-mcp-yml
modified: '2026-08-05'
name: Redefine Meat
nav: Providers
network: true
overview: 'Redefine Meat publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Food and Beverage, Alternative Protein, Plant-Based, Food Technology, and Manufacturing.


  The Redefine Meat catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Redefine Meat''s developer surface includes support, FAQ, engineering blog, authentication, and 22 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: Redefine Meat API Rules
  rule_count: 58
  severity_counts:
    error: 53
    hint: 0
    info: 2
    warn: 3
  slug: redefine-meat-rules
scopes:
- name: Redefine Meat Scopes
  scope_count: 1
  slug: redefine-meat-scopes
  summary_line: 1 scope · authorizationCode/refreshToken
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.3
  facets:
    access_clarity: 21.1
    contract_governance: 31.8
    contract_quality: 39.0
    developer_ergonomics: 25.6
    discoverability: 60.8
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - israel
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 28.9
  provenance:
    conformance: first-party
    mcp: site-plugin
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/redefine-meat/redefine-meat-2026-09-02T153205.png
security:
- kind: authentication
  name: Redefine Meat Authentication
  slug: redefine-meat-authentication
  summary_line: apiKey/http/oauth2 · 7 schemes
- kind: domain-security
  name: Redefine Meat Domain Security
  slug: redefine-meat-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: Browse the Redefine Meat product catalog
  slug: redefine-meat-browse-catalog
- name: Build a Redefine Meat cart
  slug: redefine-meat-build-a-cart
- name: Read Redefine Meat editorial content
  slug: redefine-meat-read-content
slug: redefine-meat
tags:
- Food and Beverage
- Alternative Protein
- Plant-Based
- Food Technology
- Manufacturing
- E-Commerce
- WooCommerce
- WordPress
- Retail
- MCP
website: https://www.redefinemeat.com/
---
