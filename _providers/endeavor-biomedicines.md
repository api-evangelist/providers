---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.1
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: The public WordPress REST API served by endeavorbiomedicines.com. Content read operations — posts, pages, media, taxonomies and types — answer anonymously, which makes the company's press releases, pi
  name: Endeavor BioMedicines WordPress REST API
  slug: endeavor-biomedicines-wordpress-rest-api
- description: 'An MCP (Model Context Protocol) server exposed by the WordPress MCP adapter at /wp-json/mcp/mcp-oauth-server on endeavorbiomedicines.com. The endpoint is live but authentication-gated: an anonymous in'
  name: Endeavor BioMedicines WordPress MCP Server
  slug: endeavor-biomedicines-wordpress-mcp-server
artifact_total: 9
collections:
- collection_type: open
  name: Endeavor BioMedicines WordPress REST API
  slug: open-endeavor-biomedicines-wordpress-rest
common:
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
  name: endeavor-biomedicines-mcp.yml
  slug: endeavor-biomedicines-mcpyml
modified: '2026-08-12'
name: Endeavor BioMedicines
nav: Providers
network: true
overview: 'Endeavor BioMedicines publishes 1 API on the [APIs.io](https://apis.io/) network: WordPress REST API. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Clinical Trials.


  Endeavor BioMedicines'' developer surface includes engineering blog, support, authentication, and 14 more developer resources.'
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
  composite: 38.7
  delta: 3.5
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 30.3
    contract_quality: 56.0
    developer_ergonomics: 20.8
    discoverability: 75.9
    governance: 30.3
    operational_transparency: 0.0
  previous_composite: 35.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
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
