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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.1
  scored_at: '2026-09-20'
api_count: 0
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.aervivo.com/
- group: company
  title: ''
  type: About
  url: https://www.aervivo.com/company
- group: company
  title: ''
  type: Blog
  url: https://www.aervivo.com/newsroom
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aervivo.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://portal.aervivo.com/
- group: company
  title: ''
  type: Careers
  url: https://www.aervivo.com/careers
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aervivo/refs/heads/main/llms/aervivo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aervivo-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aervivo/refs/heads/main/mcp/aervivo-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aervivo-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aervivo/refs/heads/main/well-known/aervivo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aervivo-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aervivo/refs/heads/main/authentication/aervivo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aervivo-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aervivo/refs/heads/main/scopes/aervivo-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aervivo-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aervivo/refs/heads/main/conformance/aervivo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aervivo-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aervivo/refs/heads/main/security/aervivo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aervivo-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aervivo/refs/heads/main/plans/aervivo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aervivo-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aervivo/refs/heads/main/rate-limits/aervivo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aervivo-rate-limits.yml
coverage:
  checked: '2026-09-12'
  detail: Aervivo markets a "modularized, API architecture" for its Aervivo Cloud OSS/BSS but runs no developer site at all; its only application surface, portal.aervivo.com, is a Salesforce Experience Cloud community that redirects every anonymous request to a bare username/password SiteLogin, and api/docs/developer.aervivo.com do not resolve.
  evidence:
  - status: 200
    url: https://portal.aervivo.com/
  - status: 200
    url: https://portal.aervivo.com/SiteLogin
  - status: 400
    url: https://www.aervivo.com/openapi.json
  - status: 404
    url: https://www.aervivo.com/api-docs
  reason: partner-login
  state: gated
created: '2026-09-12'
description: Aervivo, Inc. is a San Diego, California company founded in 2020 that sells the Aervivo Connectivity Platform, a cloud operating system paired with the Aervivo Hybrid Edge ecosystem of fiber and fixed-wireless networking equipment (AerHub, AerSwitch). It lets multifamily property owners, fiber overbuilders, WISPs and incumbent ISPs deploy and operate community-wide gigabit managed WiFi without a full fiber build, bundling a virtualized core network with cloud-based OSS and BSS. Aervivo publishes no developer portal, API reference or machine-readable contract; its partner surface is a Salesforce Experience Cloud portal behind a login at portal.aervivo.com, and the only anonymous machine surface on its own hosts is the Wix Site MCP endpoint its marketing site serves.
image: https://static.wixstatic.com/media/91fe64_ffda9adaafb74ce3b07da6de65ed20cd~mv2.png/v1/fill/w_2039,h_1102,al_c/91fe64_ffda9adaafb74ce3b07da6de65ed20cd~mv2.png
layout: provider
mcp_servers:
- description: Aervivo's marketing site (www.aervivo.com) is built on Wix, and Wix serves a Model Context Protocol endpoint at /_api/mcp on the site's own host. A tools/list call returned HTTP 200 with nine tools, s
  name: Aervivo Site MCP (Wix Site MCP runtime)
  slug: aervivo-site-mcp-wix-site-mcp-runtime
modified: '2026-09-12'
name: Aervivo
nav: Providers
network: true
overview: 'Aervivo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Telecommunications, Internet Service Provider, Fixed Wireless, and Networking.


  Aervivo''s developer surface includes engineering blog, authentication, and 13 more developer resources.'
plans:
- name: Aervivo Plans Pricing
  plan_count: 0
  slug: aervivo-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Aervivo Rate Limits
  slug: aervivo-rate-limits
scopes:
- name: Aervivo Scopes
  scope_count: 36
  slug: aervivo-scopes
  summary_line: 36 scopes
score:
  band: emerging
  composite: 18.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.4
    operational_transparency: 0.0
  previous_composite: 18.9
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 61.1
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aervivo Authentication
  slug: aervivo-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aervivo Domain Security
  slug: aervivo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: aervivo
tags:
- Company
- Telecommunications
- Internet Service Provider
- Fixed Wireless
- Networking
- Wi-Fi
- OSS BSS
- Connectivity
- Real-Estate
- Cloud
website: https://www.aervivo.com/
---
