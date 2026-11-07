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
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'An MCP (Model Context Protocol) server exposed by the WordPress MCP adapter at /wp-json/mcp/mcp-oauth-server on endeavorbiomedicines.com. The endpoint is live but authentication-gated: an anonymous in'
  name: Endeavor BioMedicines WordPress MCP Server
  slug: endeavor-biomedicines-wordpress-mcp-server
- description: 'The public WordPress REST API (wp-json) of the Endeavor BioMedicines website at endeavorbiomedicines.com: the route index of the site''s content management system, catalogued as one site surface rather'
  name: Endeavor BioMedicines Website (WordPress REST)
  slug: endeavorbiomedicines-com-website-wordpress-rest
artifact_total: 13
collections:
- collection_type: open
  name: Endeavor BioMedicines WordPress REST API
  slug: open-endeavor-biomedicines-wordpress-rest
common:
- group: other
  href: https://artifacts.apis.io/endeavor-biomedicines/overlays/endeavor-biomedicines-wordpress-rest-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/endeavor-biomedicines-wordpress-rest-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://endeavorbiomedicines.com/
- group: company
  title: ''
  type: Blog
  url: https://endeavorbiomedicines.com/media/
- group: company
  title: ''
  type: BlogRSS
  url: https://endeavorbiomedicines.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://endeavorbiomedicines.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://endeavorbiomedicines.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://endeavorbiomedicines.com/legal-notices/
- group: agent
  href: https://artifacts.apis.io/endeavor-biomedicines/well-known/endeavor-biomedicines-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/endeavor-biomedicines-well-known.yml
- group: auth
  href: https://artifacts.apis.io/endeavor-biomedicines/authentication/endeavor-biomedicines-authentication.yml
  title: ''
  type: Authentication
  url: authentication/endeavor-biomedicines-authentication.yml
- group: auth
  href: https://artifacts.apis.io/endeavor-biomedicines/scopes/endeavor-biomedicines-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/endeavor-biomedicines-scopes.yml
- group: design
  href: https://artifacts.apis.io/endeavor-biomedicines/conformance/endeavor-biomedicines-conformance.yml
  title: ''
  type: Conformance
  url: conformance/endeavor-biomedicines-conformance.yml
- group: design
  href: https://artifacts.apis.io/endeavor-biomedicines/lifecycle/endeavor-biomedicines-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/endeavor-biomedicines-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/endeavor-biomedicines/security/endeavor-biomedicines-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/endeavor-biomedicines-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/endeavor-biomedicines/llms/endeavor-biomedicines-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/endeavor-biomedicines-llms.txt
- group: agent
  href: https://artifacts.apis.io/endeavor-biomedicines/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/endeavor-biomedicines/plans/endeavor-biomedicines-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/endeavor-biomedicines-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/endeavor-biomedicines/rate-limits/endeavor-biomedicines-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/endeavor-biomedicines-rate-limits.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/endeavor-biomedicines_stock/
created: '2026-08-12'
description: Endeavor BioMedicines is a clinical-stage biotechnology company headquartered in San Diego, California, developing medicines aimed at reversing — not merely slowing — the course of life-threatening fibrotic and oncologic disease. Its lead investigational candidate, taladegib (ENV-101), is an inhibitor of the Hedgehog signaling pathway in clinical development for idiopathic pulmonary fibrosis, and it has in-licensed HMBD-501, a next-generation HER3-targeted antibody-drug conjugate. Endeavor publishes no developer program or product API; the machine-readable surface profiled here is the public WordPress REST API served from its corporate website, together with an authenticated WordPress MCP server and the RFC 8414 / RFC 9728 OAuth 2.1 discovery documents that host advertises.
image: https://endeavorbiomedicines.com/wp-content/uploads/2024/04/OG_Lungs.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at endeavorbiomedicines.com over HTTP.
  name: Endeavor BioMedicines MCP Server
  slug: endeavor-biomedicines-wordpress-mcp
modified: '2026-08-12'
name: Endeavor BioMedicines
nav: Providers
network: true
overview: 'Endeavor BioMedicines publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Clinical Trials.


  The Endeavor BioMedicines catalog on APIs.io includes 1 Spectral governance ruleset.


  Endeavor BioMedicines'' developer surface includes engineering blog, support, authentication, and 15 more developer resources.'
plans:
- name: Endeavor Biomedicines Plans Pricing
  plan_count: 0
  slug: endeavor-biomedicines-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Endeavor Biomedicines Rate Limits
  slug: endeavor-biomedicines-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Endeavor BioMedicines API Rules
  rule_count: 55
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 5
  slug: endeavor-biomedicines-rules
scopes:
- name: Endeavor Biomedicines Scopes
  scope_count: 1
  slug: endeavor-biomedicines-scopes
  summary_line: 1 scope · authorizationCode/refreshToken
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 21.1
    contract_governance: 31.8
    contract_quality: 1.7
    developer_ergonomics: 25.6
    discoverability: 60.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 22.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: site-plugin
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 32.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/endeavor-biomedicines/endeavor-biomedicines-2026-09-02T145356.png
security:
- kind: authentication
  name: Endeavor Biomedicines Authentication
  slug: endeavor-biomedicines-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Endeavor Biomedicines Domain Security
  slug: endeavor-biomedicines-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Inspect the Endeavor BioMedicines MCP surface
  slug: endeavor-biomedicines-inspect-mcp-surface
- name: Read the Endeavor BioMedicines company profile
  slug: endeavor-biomedicines-read-company-profile
- name: Read Endeavor BioMedicines press releases
  slug: endeavor-biomedicines-read-press-releases
slug: endeavor-biomedicines
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Clinical Trials
- Healthcare
- Drug Development
- Content
- WordPress
website: https://endeavorbiomedicines.com/
---
