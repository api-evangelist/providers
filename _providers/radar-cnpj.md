---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'Public REST API over the Brazilian CNPJ registry: business-idea evaluation, CNPJ lookup, advanced search/export, free-text-to-filters IA translation, geolocation, and anonymous monitoring. Mostly no-a'
  name: Radar CNPJ API
  slug: radar-cnpj-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://radar-cnpj.com
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/radar-cnpj-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/radar-cnpj-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/radar-cnpj-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/radar-cnpj-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/radar-cnpj-security.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://radar-cnpj.com/termos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://radar-cnpj.com/privacidade
- group: other
  title: ''
  type: X-OKF
  url: okf/radar-cnpj-okf-index.md
created: '2026-09-05'
description: Brazilian company-data service built on the Receita Federal CNPJ registry. Paste a business idea in plain text to see how many companies already operate in that space, plus CNPJ lookup, advanced search, geolocation, and change-monitoring. Explicitly agent-first, shipping a full stack of machine-readable discovery artifacts including OpenAPI, a hosted MCP server, and llms.txt.
image: https://radar-cnpj.com/icon.svg
layout: provider
mcp_servers:
- description: ''
  name: Radar CNPJ MCP Server
  slug: radar-cnpj-mcp-server
- description: Official hosted MCP server for Radar CNPJ (Streamable HTTP, JSON-RPC 2.0). GET /mcp returns a server card; POST /mcp answers initialize, tools/list and tools/call with no authentication. Every tool is
  name: Radar CNPJ MCP Server
  slug: radar-cnpj-mcp-server-2
modified: '2026-09-05'
name: Radar CNPJ
nav: Providers
network: true
overview: Radar CNPJ publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Business & Company Data, Government/Open Data, Receita Federal, CNPJ, and Brazil.
plans:
- name: Radar Cnpj Plans Pricing
  plan_count: 2
  slug: radar-cnpj-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Radar Cnpj Rate Limits
  slug: radar-cnpj-rate-limits
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 33.3
    developer_ergonomics: 23.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
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
    regime: Government & Public Sector
    regime_id: government
    score: 57.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: Radar Cnpj Authentication
  slug: radar-cnpj-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Radar Cnpj Domain Security
  slug: radar-cnpj-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Radar Cnpj Vulnerability Disclosure
  slug: radar-cnpj-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: radar-cnpj
tags:
- Business & Company Data
- Government/Open Data
- Receita Federal
- CNPJ
- Brazil
- Regulatory & Compliance
- KYB
- Search
- Data Enrichment
- Geolocation
- Monitoring & Alerts
- Agent-native
- MCP
- Micropayments
- x402
website: https://radar-cnpj.com
---
