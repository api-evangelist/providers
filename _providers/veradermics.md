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
    error_semantics: false
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
  score: 20.4
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.veradermics.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.veradermics.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.veradermics.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.veradermics.com/contact-us/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/veradermics-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/veradermics-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/veradermics-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/veradermics-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/veradermics-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/veradermics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/veradermics-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/veradermics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/veradermics-rate-limits.yml
created: '2026-09-02'
description: Veradermics is a dermatologist-founded, late clinical-stage biopharmaceutical company headquartered in New Haven, Connecticut, developing first-in-class therapeutics for common dermatologic and aesthetic conditions. Its lead program, VDPHL01, is an oral, non-hormonal candidate for pattern hair loss in men and women, in Phase II/III trials — the first oral pattern-hair-loss trials in nearly thirty years and the first US trials in female pattern hair loss. A broader pipeline targets alopecia, warts, molluscum contagiosum and atopic dermatitis. The company closed an oversubscribed $150M Series C in October 2025 and completed a US IPO in February 2026 under the ticker MANE. Veradermics operates no public developer program, developer portal, SDK or documented API; the only machine-readable surfaces on its corporate host are WordPress platform plumbing — an RFC 8414 / RFC 9728 OAuth discovery chain and an auth-gated MCP server registered by the WordPress MCP Adapter.
image: https://veradermics.b-cdn.net/wp-content/uploads/2026/04/VERADERMICS-Website-OG-Option-1-2026APR23-V01-D.jpg
layout: provider
mcp_servers:
- description: ''
  name: Veradermics MCP (WordPress MCP Adapter)
  slug: veradermics-mcp-wordpress-mcp-adapter
modified: '2026-09-02'
name: Veradermics
nav: Providers
network: true
overview: 'Veradermics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Healthcare.


  Veradermics'' developer surface includes support, authentication, and 11 more developer resources.'
plans:
- name: Veradermics Plans Pricing
  plan_count: 0
  slug: veradermics-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Veradermics Rate Limits
  slug: veradermics-rate-limits
scopes:
- name: Veradermics Scopes
  scope_count: 0
  slug: veradermics-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 9
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 19.8
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: authentication
  name: Veradermics Authentication
  slug: veradermics-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Veradermics Domain Security
  slug: veradermics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: veradermics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Healthcare
- Dermatology
- Clinical Trials
- Drug Development
website: https://www.veradermics.com/
---
