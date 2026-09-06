---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 29.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 41
  human_in_the_loop: 2
  name: Gradetv Agentic Access
  operation_count: 83
  slug: gradetv-agentic-access
  summary_line: 83 operations · 41 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: REST API for the Grade IPTV catalog and personal library, with a public OpenAPI 3.1 contract, hosted MCP server (46 tools), llms.txt agent documentation, and a well-known API catalog.
  name: Grade API
  slug: grade-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://gradetv.net
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/gradetv-tool-crosswalk.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gradetv-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gradetv-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/gradetv-security.txt
- group: auth
  title: ''
  type: Security
  url: security/gradetv-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gradetv-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gradetv-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gradetv-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gradetv-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/gradetv-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gradetv-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gradetv-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/gradetv-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://gradetv.net/api/billing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gradetv.net/termos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gradetv.net/privacidade
- group: start
  title: ''
  type: GettingStarted
  url: https://gradetv.net/como-usar
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gradetv-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gradetv-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gradetv-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gradetv-authentication.yml
created: '2026-09-05'
description: A searchable directory of public/free-to-air TV and radio broadcasts (sourced from iptv-org) plus a personal, URL-addressable media library with exportable feeds (M3U, M3U8, JSON, XSPF), EPG guide, per-channel health scores, and live chat. Exposes a REST API with OpenAPI 3.1, a hosted MCP server, and llms.txt agent docs.
image: https://gradetv.net/icon.svg
layout: provider
mcp_servers:
- description: ''
  name: Grade MCP Server
  slug: grade-mcp-server
- description: ''
  name: Grade
  slug: grade
modified: '2026-09-05'
name: Grade
nav: Providers
network: true
overview: 'Grade publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include IPTV, Streaming, Live TV, Live Radio, and Media Catalog.


  Grade''s developer surface includes pricing, getting-started guide, authentication, and 20 more developer resources.'
plans:
- name: Gradetv Plans Pricing
  plan_count: 4
  slug: gradetv-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 4
  name: Gradetv Rate Limits
  slug: gradetv-rate-limits
score:
  band: developing
  composite: 44.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 34.1
    developer_ergonomics: 42.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: Gradetv Authentication
  slug: gradetv-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gradetv Domain Security
  slug: gradetv-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Gradetv Vulnerability Disclosure
  slug: gradetv-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: gradetv
tags:
- IPTV
- Streaming
- Live TV
- Live Radio
- Media Catalog
- Broadcast Metadata
- EPG
- TV Guide
- Content Aggregation
- Agent-native
- MCP
- x402
- Micropayments
- Brazil
website: https://gradetv.net
---
