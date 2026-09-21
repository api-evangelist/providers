---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.5
  scored_at: '2026-09-20'
api_count: 1
apis:
- baseURL: https://wagerx.io
  baseurl_source: declared
  description: Public read-only REST feeds for dated crypto-casino audit evidence (all audits, one audit by slug), the regulatory intelligence alert feed, the Trump Crypto and Slot Hype indexes, latest news, and the
  name: WagerX iGaming & Regulatory Intelligence API
  slug: wagerx-igaming-regulatory-intelligence-api
- description: Remote, anonymous, stateless streamable-HTTP MCP server (protocol 2025-06-18) exposing 12 read-only tools over casino audit evidence, regulatory intelligence and the Agentic Gambling Index; tools/call
  name: Wagie MCP Server
  slug: wagie-mcp-server
- description: 'A2A JSON-RPC endpoint accepting A2A 1.0 SendMessage and 0.3.0 message/send for bounded iGaming and regulatory questions; discovered through a signed Agent Card at /.well-known/agent-card.json (graded '
  name: Wagie A2A Agent
  slug: wagie-a2a-agent
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://wagerx.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://wagerx.io/api
- group: docs
  title: ''
  type: Documentation
  url: https://wagerx.io/agent-gateway
- group: docs
  title: ''
  type: APIReference
  url: https://wagerx.io/agent-gateway
- group: operate
  title: ''
  type: Support
  url: https://wagerx.io/contact-us
- group: company
  title: ''
  type: About
  url: https://wagerx.io/about-us
- group: company
  title: ''
  type: Blog
  url: https://wagerx.io/news
- group: company
  title: ''
  type: BlogRSS
  url: https://wagerx.io/rss.xml
- group: company
  title: ''
  type: Press
  url: https://wagerx.io/press
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wagerx.io/privacy-policy
- group: other
  title: ''
  type: Methodology
  url: https://wagerx.io/methodology
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/wagerx-io/refs/heads/main/llms/wagerx-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wagerx-io-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://wagerx.io/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/wagerx-io/refs/heads/main/well-known/wagerx-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/wagerx-io-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/wagerx-io/refs/heads/main/well-known/wagerx-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/wagerx-io-security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: https://wagerx.io/.well-known/security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/wagerx-io/refs/heads/main/security/wagerx-io-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/wagerx-io-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/wagerx-io/refs/heads/main/security/wagerx-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wagerx-io-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/wagerx-io/refs/heads/main/security/wagerx-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/wagerx-io-vulnerability-disclosure.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/wagerx-io/refs/heads/main/a2a/wagerx-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/wagerx-io-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/wagerx-io/refs/heads/main/mcp/wagerx-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/wagerx-io-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/wagerx-io/refs/heads/main/mcp/wagerx-io-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/wagerx-io-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/wagerx-io/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wagerx-io/refs/heads/main/conformance/wagerx-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wagerx-io-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/wagerx-io/refs/heads/main/authentication/wagerx-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wagerx-io-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wagerx-io/refs/heads/main/conventions/wagerx-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/wagerx-io-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wagerx-io/refs/heads/main/lifecycle/wagerx-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/wagerx-io-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://wagerx.io/tech/status
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/wagerx-io/refs/heads/main/plans/wagerx-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/wagerx-io-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/wagerx-io/refs/heads/main/rate-limits/wagerx-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/wagerx-io-rate-limits.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/wagerx-io/refs/heads/main/packages/wagerx-io-packages.yml
  title: ''
  type: Packages
  url: packages/wagerx-io-packages.yml
- group: other
  title: ''
  type: AITransparency
  url: https://wagerx.io/wagerx-ai-policy
- group: other
  title: ''
  type: NoticeAndAction
  url: https://wagerx.io/report-content
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/wagerx-io/refs/heads/main/regulatory/wagerx-io-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/wagerx-io-regulatory-posture.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/wagerx-io/refs/heads/main/overlays/wagerx-io-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/wagerx-io-openapi-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wagerx-io/refs/heads/main/errors/wagerx-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wagerx-io-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wagerx-io/refs/heads/main/data-model/wagerx-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wagerx-io-data-model.yml
created: '2026-09-19'
description: 'WagerX is an independent crypto-casino audit lab and gambling regulatory intelligence publisher founded in 2018 by Andreas Ericsson. It runs real-money deposit and withdrawal tests on 40+ crypto casinos, tracks enforcement actions from ~40 gambling regulators, and publishes the results as a free, anonymous, read-only API surface: a REST feed set described by an OpenAPI 3.1 document, the "Wagie" agent exposed over both A2A JSON-RPC and MCP streamable-HTTP with every answer wrapped in an Ed25519-signed evidence envelope, a separate "Tech Concierge" MCP/A2A agent, and an Agentic Gambling Index cataloguing other providers'' MCP servers and A2A agents.'
image: https://wagerx.io/static/images/wagerx-og-default.png
layout: provider
mcp_servers:
- description: ''
  name: WagerX MCP Server
  slug: wagerx-mcp-server
- description: ''
  name: WagerX MCP Server
  slug: wagerx-mcp-server-2
- description: ''
  name: WagerX MCP Server
  slug: wagerx-mcp-server-3
modified: '2026-09-19'
name: WagerX
nav: Providers
network: true
overview: 'WagerX publishes 1 API on the [APIs.io](https://apis.io/) network: iGaming & Regulatory Intelligence API. Tagged areas include Company, Gambling, iGaming, Casinos, and Regulatory Intelligence.


  WagerX''s developer surface includes documentation, API reference, support, engineering blog, authentication, and 32 more developer resources.'
plans:
- name: Wagerx Io Plans Pricing
  plan_count: 1
  slug: wagerx-io-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Wagerx Io Rate Limits
  slug: wagerx-io-rate-limits
score:
  band: developing
  composite: 44.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 53.0
    catalog_earned_first_party: 16.0
    catalog_gap: 62.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 41.6
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 49.4
    developer_ergonomics: 47.0
    discoverability: 87.0
    operational_transparency: 47.4
  previous_composite: 2.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: rising
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Wagerx Io Authentication
  slug: wagerx-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Wagerx Io Domain Security
  slug: wagerx-io-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Wagerx Io Vulnerability Disclosure
  slug: wagerx-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: wagerx-io
tags:
- Company
- Gambling
- iGaming
- Casinos
- Regulatory Intelligence
- Compliance
- Cryptocurrency
- Agents
- MCP
- A2A
- Research
website: https://wagerx.io/
---
