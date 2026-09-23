---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
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
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 39.8
  scored_at: '2026-09-23'
api_count: 1
apis:
- baseURL: https://quote-api.smklog.com
  baseurl_source: declared
  description: 'Live parcel shipping rates and agent-prepared checkout for one parcel sent from a US origin. Four operations: POST /quote prices an item described in plain words (or by product URL) across USPS, UPS, '
  name: SMKlog Quote API
  slug: smklog-quote-api
artifact_total: 8
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/smklog-com/refs/heads/main/security/smklog-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/smklog-com-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://smklog.com/
- group: docs
  title: ''
  type: Documentation
  url: https://smklog.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://quote-api.smklog.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://smklog.com/repack-line
- group: operate
  title: ''
  type: Support
  url: https://smklog.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://smklog.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://smklog.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://smklog.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/smklog
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/smklog-com/refs/heads/main/llms/smklog-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/smklog-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://smklog.com/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/smklog-com/refs/heads/main/a2a/smklog-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/smklog-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/smklog-com/refs/heads/main/mcp/smklog-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/smklog-com-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/smklog-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/smklog-com/refs/heads/main/well-known/smklog-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/smklog-com-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/smklog-com/refs/heads/main/well-known/smklog-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/smklog-com-security.txt
- group: auth
  title: ''
  type: Security
  url: https://smklog.com/.well-known/security.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/smklog-com/refs/heads/main/packages/smklog-com-packages.yml
  title: ''
  type: Packages
  url: packages/smklog-com-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/smklog-com/refs/heads/main/authentication/smklog-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/smklog-com-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/smklog-com/refs/heads/main/scopes/smklog-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/smklog-com-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/smklog-com/refs/heads/main/security/smklog-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/smklog-com-domain-security.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://smklog.com/privacy
created: '2026-09-19'
description: 'SMKlog (SMKLOG-2022 LLC, Berkeley Heights, New Jersey) is an independent US parcel shipping calculator and label seller: describe an item in plain words, get live USPS, UPS, FedEx and DHL Express rates from a US origin to the US, Canada, the UK, Germany or Australia, and buy the label online. The same pricing engine is published for machines as the SMKlog Quote API on quote-api.smklog.com: an OpenAPI 3.1 contract with no key required, a remote MCP server with five tools (plus an open-source stdio bridge), an A2A agent card, an RFC 9727 api-catalog, RFC 8414/9728 OAuth metadata for an optional client_credentials rate-limit tier, two provider-published Agent Skills and an llms.txt. Agents price and prepare checkout; a human always completes payment on smklog.com.'
image: https://smklog.com/assets/icon-512.png
layout: provider
mcp_servers:
- description: ''
  name: SMKlog MCP Server
  slug: smklog-mcp-server
modified: '2026-09-19'
name: SMKlog
nav: Providers
network: true
overview: 'SMKlog publishes 1 API on the [APIs.io](https://apis.io/) network: Quote API. Tagged areas include Company, Shipping, Logistics, Parcel Shipping, and shipping-rates.


  SMKlog''s developer surface includes documentation, API reference, getting-started guide, support, pricing, authentication, and 17 more developer resources.'
plans:
- name: Smklog Com Plans Pricing
  plan_count: 3
  slug: smklog-com-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 2
  name: Smklog Com Rate Limits
  slug: smklog-com-rate-limits
scopes:
- name: Smklog Com Scopes
  scope_count: 1
  slug: smklog-com-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 50.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 45.6
    developer_ergonomics: 52.4
    discoverability: 75.9
    operational_transparency: 52.6
  previous_composite: 50.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Smklog Com Authentication
  slug: smklog-com-authentication
  summary_line: none/oauth2 · 2 schemes
- kind: domain-security
  name: Smklog Com Domain Security
  slug: smklog-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Smklog Com Vulnerability Disclosure
  slug: smklog-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: smklog-com
tags:
- Company
- Shipping
- Logistics
- Parcel Shipping
- shipping-rates
- Shipping Labels
- E-Commerce
- Agents
- MCP
- A2A
website: https://smklog.com/
---
