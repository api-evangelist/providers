---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: 'The single HTTP endpoint VEIR declares in its own RFC 9727 API catalog. It returns veir.com page content as text/markdown for agent consumption. Probed 2026-08-05: it returns HTTP 200 with content-typ'
  name: VEIR Markdown Content Endpoint
  slug: markdown
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://veir.com/
- group: company
  title: ''
  type: Blog
  url: https://veir.com/news
- group: operate
  title: ''
  type: Support
  url: https://veir.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://veir.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://veir.com/suppliertermsandconditions
- group: agent
  title: ''
  type: WellKnown
  url: well-known/veir-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/veir-api-catalog.json
- group: other
  title: ''
  type: ContentSignal
  url: well-known/veir-robots.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/veir-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/veir-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/veir-openid-configuration.json
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/veir-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/veir-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/veir-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/veir-domain-security.yml
coverage:
  checked: '2026-08-05'
  detail: VEIR sells superconducting cable hardware, not software — veir.com serves an agent content layer (markdown twins, /sitemap.md, an RFC 9727 api-catalog) but the only API it names, https://veir.com/api/markdown, is a content endpoint that ignores its parameters, and the OIDC discovery document it publishes advertises authorization, token and JWKS endpoints that all return 404.
  evidence:
  - status: 200
    url: https://veir.com/.well-known/api-catalog
  - status: 200
    url: https://veir.com/api/markdown
  - status: 200
    url: https://veir.com/.well-known/openid-configuration
  - status: 404
    url: https://veir.com/oauth/token
  - status: 404
    url: https://veir.com/openapi.json
  - status: 404
    url: https://veir.com/.well-known/agent-card.json
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: VEIR is a superconducting power delivery company founded in 2019 and headquartered in Woburn, Massachusetts. It builds low- and medium-voltage high-temperature superconducting (HTS) transmission systems that carry five to ten times more power than conventional conductors at the same voltage level, with roughly 90% less resistive line loss, targeted at AI data center campuses, energy producers, utilities and OEMs. Investors include Microsoft's Climate Innovation Fund, National Grid Partners, Breakthrough Energy Ventures, Congruent Ventures, The Engine Ventures, Galvanize Climate Solutions, Piva Capital, Tyche Partners and VXI Capital. VEIR is a hardware company and publishes no product API or developer program, but it does publish a deliberate agent-facing content layer on veir.com — a markdown twin of every indexed page, a semantic index at /sitemap.md, an RFC 9727 API catalog, OpenID Connect and RFC 9728 OAuth protected-resource discovery documents, and a Content-Signal AI
  usage preference in robots.txt.
image: https://images.prismic.io/veir/ad7Kup1ZCF7ETMhn_veir-og-image.png?auto=format,compress&rect=0,0,1200,630&w=2400&h=1260
layout: provider
modified: '2026-08-05'
name: VEIR
nav: Providers
network: true
overview: 'VEIR publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Electricity, Data Centers, and Infrastructure.


  VEIR''s developer surface includes engineering blog, support, authentication, and 12 more developer resources.'
random_paper: 90
scopes:
- name: Veir Scopes
  scope_count: 3
  slug: veir-scopes
  summary_line: 3 scopes · authorizationCode/clientCredentials
score:
  band: emerging
  composite: 21.8
  delta: -1.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 22.8
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 56.8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Veir Authentication
  slug: veir-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Veir Domain Security
  slug: veir-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: veir
tags:
- Company
- Energy
- Electricity
- Data Centers
- Infrastructure
- Superconductors
- Content
website: https://veir.com/
---
