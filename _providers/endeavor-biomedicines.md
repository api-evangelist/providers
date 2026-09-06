---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'An MCP (Model Context Protocol) server exposed by the WordPress MCP adapter at /wp-json/mcp/mcp-oauth-server on endeavorbiomedicines.com. The endpoint is live but authentication-gated: an anonymous in'
  name: Endeavor BioMedicines WordPress MCP Server
  slug: endeavor-biomedicines-wordpress-mcp-server
- baseURL: https://endeavorbiomedicines.com/wp-json
  baseurl_source: declared
  description: The mcp API from Endeavor BioMedicines — 3 operation(s) for mcp.
  name: Endeavor BioMedicines MCP API
  slug: endeavor-biomedicines-mcp-api
- baseURL: https://endeavorbiomedicines.com/wp-json
  baseurl_source: declared
  description: The oembed/1.0 API from Endeavor BioMedicines — 3 operation(s) for oembed/1.0.
  name: Endeavor BioMedicines Oembed/1.0 API
  slug: endeavor-biomedicines-oembed-1-0-api
- baseURL: https://endeavorbiomedicines.com/wp-json
  baseurl_source: declared
  description: The wp-abilities/v1 API from Endeavor BioMedicines — 6 operation(s) for wp-abilities/v1.
  name: Endeavor BioMedicines Wp Abilities/v1 API
  slug: endeavor-biomedicines-wp-abilities-v1-api
- baseURL: https://endeavorbiomedicines.com/wp-json
  baseurl_source: declared
  description: The wp-block-editor/v1 API from Endeavor BioMedicines — 4 operation(s) for wp-block-editor/v1.
  name: Endeavor BioMedicines Wp Block Editor/v1 API
  slug: endeavor-biomedicines-wp-block-editor-v1-api
- baseURL: https://endeavorbiomedicines.com/wp-json
  baseurl_source: declared
  description: The wp-site-health/v1 API from Endeavor BioMedicines — 8 operation(s) for wp-site-health/v1.
  name: Endeavor BioMedicines Wp Site Health/v1 API
  slug: endeavor-biomedicines-wp-site-health-v1-api
- baseURL: https://endeavorbiomedicines.com/wp-json
  baseurl_source: declared
  description: The wp/v2 API from Endeavor BioMedicines — 122 operation(s) for wp/v2.
  name: Endeavor BioMedicines Wp/v2 API
  slug: endeavor-biomedicines-wp-v2-api
artifact_total: 14
collections:
- collection_type: open
  name: Endeavor BioMedicines WordPress REST API
  slug: open-endeavor-biomedicines-wordpress-rest
common:
- group: other
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
  title: ''
  type: WellKnown
  url: well-known/endeavor-biomedicines-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/endeavor-biomedicines-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/endeavor-biomedicines-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/endeavor-biomedicines-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/endeavor-biomedicines-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/endeavor-biomedicines-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/endeavor-biomedicines-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/endeavor-biomedicines-plans-pricing.yml
- group: operate
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
- description: ''
  name: Endeavor BioMedicines MCP Server
  slug: endeavor-biomedicines-mcp-server
modified: '2026-08-12'
name: Endeavor BioMedicines
nav: Providers
network: true
overview: 'Endeavor BioMedicines publishes 6 APIs on the [APIs.io](https://apis.io/) network, including MCP API, Oembed/1.0 API, Wp Abilities/v1 API, and 3 more. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Clinical Trials.


  Endeavor BioMedicines'' developer surface includes engineering blog, support, authentication, and 15 more developer resources.'
plans:
- name: Endeavor Biomedicines Plans Pricing
  plan_count: 0
  slug: endeavor-biomedicines-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Endeavor Biomedicines Rate Limits
  slug: endeavor-biomedicines-rate-limits
scopes:
- name: Endeavor Biomedicines Scopes
  scope_count: 1
  slug: endeavor-biomedicines-scopes
  summary_line: 1 scope · authorizationCode/refreshToken
score:
  band: thin
  composite: 26.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 16.2
    developer_ergonomics: 20.8
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 26.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/endeavor-biomedicines/refs/heads/main/screenshots/endeavor-biomedicines-2026-09-02T145356.png
security:
- kind: authentication
  name: Endeavor Biomedicines Authentication
  slug: endeavor-biomedicines-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Endeavor Biomedicines Domain Security
  slug: endeavor-biomedicines-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
