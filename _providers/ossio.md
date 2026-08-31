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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: 'An OAuth-protected Model Context Protocol server mounted on OSSIO''s WordPress corporate site at /wp-json/mcp/mcp-oauth-server, discoverable through the site''s RFC 9728 protected-resource document. It '
  name: OSSIO Site MCP Server
  slug: ossio-site-mcp-server
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://ossio.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ossio.io/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ossio.io/ossio-sms-terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://ossio.io/contact/
- group: company
  title: ''
  type: Blog
  url: https://ossio.io/press/
- group: company
  title: ''
  type: BlogRSS
  url: https://ossio.io/feed/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ossio-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ossio-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/ossio-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ossio-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ossio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ossio-rate-limits.yml
created: '2026-08-26'
description: 'OSSIO is an orthopedic fixation medical device company headquartered in Woburn, Massachusetts and founded in Israel in 2014. It develops and sells OSSIOfiber, a bio-integrative, metal-free implant material used for screws, suture anchors, staples, bone pins and trimmable fixation nails in foot and ankle, hand and wrist, sports medicine and pediatric procedures. OSSIO ships physical implants, not software, and publishes no developer program, no product API and no OpenAPI. Its one machine-readable surface is the corporate website itself: ossio.io runs WordPress with the MCP Adapter installed, exposing an OAuth-protected Model Context Protocol server plus RFC 8414 and RFC 9728 metadata documents at /.well-known/ — a site-content agent surface, not a product API.'
image: https://ossio.io/wp-content/uploads/2023/04/social.png
layout: provider
mcp_servers:
- description: ossio.io mounts a live Model Context Protocol server under the WordPress REST API at /wp-json/mcp/. Two servers are registered — mcp-oauth-server (OAuth-protected, the one named by the RFC 9728 protec
  name: OSSIO Site MCP Server
  slug: ossio-site-mcp-server
modified: '2026-08-26'
name: OSSIO
nav: Providers
network: true
overview: 'OSSIO publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Health, Orthopedics, and Life Sciences.


  OSSIO''s developer surface includes support, engineering blog, and 10 more developer resources.'
plans:
- name: Ossio Plans Pricing
  plan_count: 0
  slug: ossio-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Ossio Rate Limits
  slug: ossio-rate-limits
scopes:
- name: Ossio Scopes
  scope_count: 0
  slug: ossio-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.1
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 22.1
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
  name: Ossio Authentication
  slug: ossio-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Ossio Domain Security
  slug: ossio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ossio
tags:
- Company
- Medical Devices
- Health
- Orthopedics
- Life Sciences
- Manufacturing
- MCP
- Agents
website: https://ossio.io/
---
