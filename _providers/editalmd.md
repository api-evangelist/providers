---
agent_readiness:
  band: agent-ready
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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 32.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Public REST API over Brazil's PNCP procurement portal with full-text tender search, tender sheets and deadlines, edital markdown, eligibility extraction, alerts and watchers. Also exposes a hosted MCP
  name: EditalMD API
  slug: editalmd-api
artifact_total: 9
asyncapis:
- description: ''
  name: Editalmd Webhooks
  slug: editalmd-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://editalmd.com
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/editalmd-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/editalmd-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: security/editalmd-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/editalmd-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/editalmd-security.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://editalmd.com/termos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://editalmd.com/privacidade
- group: commercial
  title: ''
  type: Pricing
  url: https://editalmd.com/#precos
created: '2026-09-05'
description: Agent-native data API over Brazil's public-procurement portal PNCP (Portal Nacional de Contratações Públicas). Provides full-text tender search, proposal and challenge deadlines, editais rendered as markdown with provenance and SHA-256 hashes, new-tender alerts by keyword or CNPJ, tender change-watchers, and extracted eligibility (habilitação) checklists. Search is free; other routes are paid per request (x402) or via prepaid credit with no signup.
image: https://editalmd.com/icon.svg
layout: provider
mcp_servers:
- description: ''
  name: EditalMD MCP Server
  slug: editalmd-mcp-server
- description: 'Hosted first-party MCP server (Streamable HTTP, JSON-RPC 2.0) dispatched by the same Cloudflare Worker as the REST API. Exposes 19 tools covering the whole product: free PNCP tender search, tender she'
  name: EditalMD MCP Server
  slug: editalmd-mcp-server-2
modified: '2026-09-05'
name: EditalMD
nav: Providers
network: true
overview: 'EditalMD publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GovTech, Public Procurement, Brazil, PNCP, and Legal & Compliance.


  The EditalMD catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  EditalMD''s developer surface includes pricing and 8 more developer resources.'
plans:
- name: Editalmd Plans Pricing
  plan_count: 0
  slug: editalmd-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Editalmd Rate Limits
  slug: editalmd-rate-limits
score:
  band: developing
  composite: 45.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 50.5
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 39.5
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
  name: Editalmd Authentication
  slug: editalmd-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Editalmd Domain Security
  slug: editalmd-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Editalmd Vulnerability Disclosure
  slug: editalmd-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: editalmd
tags:
- GovTech
- Public Procurement
- Brazil
- PNCP
- Legal & Compliance
- Business Intelligence
- Company Data
- CNPJ
- CNAE
- SICAF
- Document Extraction
- Agent-Native
- MCP
- x402
- Machine-Payable
website: https://editalmd.com
---
