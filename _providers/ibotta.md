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
  - rate-limits
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
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://api.ibops.net/bex-api
  baseurl_source: declared
  description: The Openai API from Ibotta — 1 operation(s) for openai.
  name: Ibotta Openai API
  slug: ibotta-openai-api
artifact_total: 10
collections:
- collection_type: open
  name: Ibotta Product API
  slug: open-ibotta-product-api
common:
- group: operate
  href: https://artifacts.apis.io/ibotta/rate-limits/ibotta-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ibotta-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/ibotta/overlays/ibotta-product-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ibotta-product-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/ibotta/mcp/ibotta-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/ibotta-mcp.yml
- group: agent
  href: https://artifacts.apis.io/ibotta/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://home.ibotta.com/
- group: company
  title: ''
  type: Blog
  url: https://home.ibotta.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://help.ibotta.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Ibotta
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.ibotta.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.ibotta.com/
- group: company
  title: ''
  type: Partners
  url: https://ipn.ibotta.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ipn.ibotta.com/integrating-with-the-ipn
- group: start
  title: ''
  type: GettingStarted
  url: https://ipn.ibotta.com/resource-hub/ipn-integration
- group: start
  title: ''
  type: Login
  url: https://portal.ipn.ibotta.com/
- group: auth
  href: https://artifacts.apis.io/ibotta/security/ibotta-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ibotta-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/ibotta/well-known/ibotta-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ibotta-well-known.yml
- group: auth
  href: https://artifacts.apis.io/ibotta/security/ibotta-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/ibotta-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ibotta/security/ibotta-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ibotta-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/ibotta/conformance/ibotta-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ibotta-conformance.yml
- group: design
  href: https://artifacts.apis.io/ibotta/conventions/ibotta-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ibotta-conventions.yml
- group: design
  href: https://artifacts.apis.io/ibotta/lifecycle/ibotta-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ibotta-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/ibotta/scopes/ibotta-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/ibotta-scopes.yml
- group: build
  href: https://artifacts.apis.io/ibotta/packages/ibotta-packages.yml
  title: ''
  type: Packages
  url: packages/ibotta-packages.yml
- group: commercial
  href: https://artifacts.apis.io/ibotta/plans/ibotta-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ibotta-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/ibotta/llms/ibotta-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ibotta-llms.txt
created: '2026-07-17'
description: 'Ibotta is a Denver-based consumer technology company (NYSE: IBTA) that operates a cash-back rewards platform and the Ibotta Performance Network (IPN), a digital promotions and retail-media network. Consumers earn real cash back on everyday purchases in-store and online through the Ibotta mobile app, browser extension, and connected retailer loyalty accounts. For brands, agencies, and retailers, the Ibotta Performance Network distributes digital rebates and promotions to more than 200 million shoppers across Ibotta''s owned properties and a network of partner retailers and publishers (including Walmart, Dollar General, Family Dollar, and others). Ibotta was surfaced in the API Evangelist network as a portfolio company of GGV Capital. Ibotta publishes exactly one machine-readable API contract: the Ibotta Product API (an OpenAPI 3.0.1 document at ibotta.com/bex-api/api-docs.json), declared by the ChatGPT plugin manifest Ibotta still serves at ibotta.com/.well-known/ai-plugin.json
  — a single product-search operation backing the Ibotta browser extension, gated by a service bearer token that is not self-serve. The Ibotta Performance Network APIs that partners actually integrate against are documented only inside the IPN partner portal (portal.ipn.ibotta.com), which is behind Auth0 and reached through a sales conversation; no public IPN API reference, pricing, or rate-limit documentation exists.'
image: https://images.ctfassets.net/zgieqvh3kubv/59XQvan2WhYzTi2PwaCGQV/454455352f937dde633bac1485ab3fdd/featured-ibotta.webp
layout: provider
modified: '2026-08-12'
name: Ibotta
nav: Providers
network: true
overview: 'Ibotta publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Openai API. Tagged areas include Company, Consumer, Cashback, Rewards, and Retail Media.


  The Ibotta catalog on APIs.io includes 1 Spectral governance ruleset.


  Ibotta''s developer surface includes engineering blog, support, documentation, getting-started guide, and 21 more developer resources.'
plans:
- name: Ibotta Plans Pricing
  plan_count: 0
  slug: ibotta-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Ibotta Rate Limits
  slug: ibotta-rate-limits
rules:
- authorship: generated
  effective_rule_count: 79
  extends:
  - spectral:oas
  name: Ibotta API Rules
  rule_count: 38
  severity_counts:
    error: 36
    hint: 0
    info: 1
    warn: 1
  slug: ibotta-rules
scopes:
- name: Ibotta Scopes
  scope_count: 0
  slug: ibotta-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    contract_governance: 18.2
    contract_quality: 43.5
    developer_ergonomics: 42.3
    discoverability: 66.1
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 33.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/ibotta/ibotta-2026-07-25T221955.png
security:
- kind: authentication
  name: Ibotta Authentication
  slug: ibotta-authentication
  summary_line: http/oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Ibotta Domain Security
  slug: ibotta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ibotta Vulnerability Disclosure
  slug: ibotta-vulnerability-disclosure
  summary_line: Hackerone
skill_count: 1
skills:
- name: ibotta-product-search
  slug: ibotta-product-search
slug: ibotta
tags:
- Company
- Consumer
- Cashback
- Rewards
- Retail Media
- Coupons
- Loyalty
- Shopping
- Advertising
- Promotions
- Product Search
- Retail
- Affiliates
- Consumer Packaged Goods
website: https://home.ibotta.com/
---
