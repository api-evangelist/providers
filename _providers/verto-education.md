---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: A remote Model Context Protocol endpoint served from Verto Education's own WordPress installation and advertised through RFC 9728 protected-resource metadata. Access requires an OAuth 2.0 access token
  name: Verto Education MCP Server
  slug: verto-education-mcp
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/verto-education-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vertoeducation.org/
- group: company
  title: ''
  type: Blog
  url: https://vertoeducation.org/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://vertoeducation.org/blog/feed/
- group: operate
  title: ''
  type: Support
  url: https://vertoeducation.org/getinfo/
- group: start
  title: ''
  type: SignUp
  url: https://vertoeducation.org/apply/
- group: commercial
  title: ''
  type: Pricing
  url: https://vertoeducation.org/abroad-locations/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vertoeducation.org/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vertoeducation.org/privacy-policy/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/verto-education-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/verto-education-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/verto-education-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/verto-education-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/verto-education-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/verto-education-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/verto-education-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/verto-education-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/verto-education-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/verto-education-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/verto-education-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/verto-education-packages.yml
created: '2026-09-02'
description: 'Verto Education is a US study-abroad provider, founded in 2017, that sells a first year of college taken overseas. Students spend one, two or three semesters in Buenos Aires, Prague, London, Florence or Seville, earn up to 16 US-transferable credits per semester through academic provider the University of New Haven, and transfer into one of 60+ partner colleges, in some cases with guaranteed admission. Verto runs no developer programme and publishes no OpenAPI, documentation portal or SDK. It does, however, serve a real agent surface from its own domain: a remote Model Context Protocol endpoint at /wp-json/mcp/mcp-oauth-server, discoverable through RFC 9728 protected-resource metadata and fronted by an OAuth 2.0 authorization server with PKCE, plus a Yoast-generated llms.txt. The MCP endpoint is live but OAuth-gated - tools/list returns 401 anonymously - so its tool schemas cannot be enumerated without credentials.'
image: https://vertoeducation.org/wp-content/uploads/VE-website-social-share-photos-HOMEPAGE.png
layout: provider
mcp_servers:
- description: Verto Education serves a remote Model Context Protocol endpoint from its own WordPress installation at https://vertoeducation.org/wp-json/mcp/mcp-oauth-server. It was discovered from the RFC 9728 prot
  name: Verto Education MCP Server
  slug: verto-education-mcp-server
modified: '2026-09-02'
name: Verto Education
nav: Providers
network: true
overview: 'Verto Education publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Higher Education, Study Abroad, and College Admissions.


  Verto Education''s developer surface includes engineering blog, support, signup flow, pricing, authentication, and 16 more developer resources.'
plans:
- name: Verto Education Plans Pricing
  plan_count: 0
  slug: verto-education-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Verto Education Rate Limits
  slug: verto-education-rate-limits
scopes:
- name: Verto Education Scopes
  scope_count: 0
  slug: verto-education-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.4
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
security:
- kind: authentication
  name: Verto Education Authentication
  slug: verto-education-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Verto Education Domain Security
  slug: verto-education-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: verto-education
tags:
- Company
- Education
- Higher Education
- Study Abroad
- College Admissions
- Students
- Travel
- Model Context Protocol
- OAuth
- Agents
website: https://vertoeducation.org/
---
