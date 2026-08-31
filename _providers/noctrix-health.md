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
    well_known_catalog: true
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: A live Model Context Protocol server operated by Noctrix Health on the Nidra product site. Discovered anonymously from RFC 9728 OAuth 2.0 Protected Resource Metadata at https://nidrarls.com/.well-know
  name: Nidra MCP Server
  slug: nidra-mcp-server
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/noctrix-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://noctrixhealth.com/
- group: other
  title: ''
  type: ProductSite
  url: https://nidrarls.com/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.resmed.com/
- group: operate
  title: ''
  type: Support
  url: https://nidrarls.com/patient-support/
- group: commercial
  title: ''
  type: Pricing
  url: https://nidrarls.com/cost/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nidrarls.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nidrarls.com/terms-of-use/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/noctrix-health-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/noctrix-health-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/noctrix-health-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/noctrix-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/noctrix-health-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/noctrix-health-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/noctrix-health-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/noctrix-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/noctrix-health-rate-limits.yml
created: '2026-08-26'
description: 'Noctrix Health, Inc. is a Pleasanton, California medical device company that develops drug-free wearable neurostimulation therapies for chronic neurological conditions. Its product is the Nidra Tonic Motor Activation (TOMAC) System, a prescription pair of lower-leg devices that stimulate the peroneal nerves to suppress the symptoms of medication-refractory moderate-to-severe Restless Legs Syndrome and improve sleep quality; the NTX100 received FDA De Novo marketing authorization in April 2023 after a 2020 Breakthrough Device Designation. Noctrix was acquired by Resmed and became a wholly owned subsidiary on 1 June 2026. The company runs no developer program and publishes no OpenAPI, SDK or API reference, but the Nidra product site is deliberately agent-ready: it serves a hand-authored llms.txt with markdown twins of every key page, opts AI crawlers in via robots.txt, and runs a live OAuth-protected Model Context Protocol server discoverable through RFC 8414 and RFC 9728 well-known
  metadata.'
image: https://nidrarls.com/themes/nidra/assets/img/nidra-logo.png
layout: provider
mcp_servers:
- description: Noctrix Health runs a live Model Context Protocol server on the Nidra product site (nidrarls.com). It was discovered from RFC 9728 OAuth 2.0 Protected Resource Metadata served anonymously at /.well-kn
  name: Nidra MCP Server
  slug: nidra-mcp-server
modified: '2026-08-26'
name: Noctrix Health
nav: Providers
network: true
overview: 'Noctrix Health publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Medical Devices, Digital Health, and Sleep.


  Noctrix Health''s developer surface includes support, pricing, authentication, and 14 more developer resources.'
plans:
- name: Noctrix Health Plans Pricing
  plan_count: 0
  slug: noctrix-health-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Noctrix Health Rate Limits
  slug: noctrix-health-rate-limits
scopes:
- name: Noctrix Health Scopes
  scope_count: 0
  slug: noctrix-health-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 24.5
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Noctrix Health Authentication
  slug: noctrix-health-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Noctrix Health Domain Security
  slug: noctrix-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: noctrix-health
tags:
- Company
- Health
- Medical Devices
- Digital Health
- Sleep
- Neurology
- Neurostimulation
- Wearables
- MCP
- Agent Readiness
website: https://noctrixhealth.com/
---
