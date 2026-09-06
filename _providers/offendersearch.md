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
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 35.6
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: REST API for national sex-offender screening; API-key authenticated, JSON responses, synchronous and asynchronous search across all 58 US registries.
  name: Offendersearch API
  slug: offendersearch-api
artifact_total: 7
asyncapis:
- description: ''
  name: Offendersearch Webhooks
  slug: offendersearch-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/offendersearch-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/offendersearch-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/offendersearch-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/offendersearch-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/offendersearch-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://offendersearch.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://offendersearch.app/privacy
- group: operate
  title: ''
  type: Support
  url: https://offendersearch.app/contact
- group: company
  title: ''
  type: Blog
  url: https://offendersearch.app/blog
- group: start
  title: ''
  type: SignUp
  url: https://offendersearch.app/sign-up
- group: start
  title: ''
  type: Login
  url: https://offendersearch.app/sign-in
created: '2026-08-23'
description: A commercial REST API (and private-beta MCP server) for nationwide US sex-offender registry screening, searching 58 US registries through one API with scored matches and per-source provenance.
image: https://offendersearch.app/opengraph-image.png
layout: provider
mcp_servers:
- description: 'Offendersearch operates an official hosted (remote) MCP server. The marketing page (/mcp-server) describes it as private beta — "the hosted endpoint is not yet open to self-serve signups" — and shows '
  name: Offendersearch MCP Server
  slug: offendersearch-mcp-server
modified: '2026-09-03'
name: Offendersearch
nav: Providers
network: true
overview: 'Offendersearch publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Background Screening, Identity & risk, Trust and Safety, Public Records, and Criminal data.


  The Offendersearch catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Offendersearch''s developer surface includes authentication, support, engineering blog, signup flow, and 8 more developer resources.'
plans:
- name: Offendersearch Plans Pricing
  plan_count: 4
  slug: offendersearch-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Offendersearch Rate Limits
  slug: offendersearch-rate-limits
score:
  band: developing
  composite: 48.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 48.1
    developer_ergonomics: 56.5
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 48.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/offendersearch/refs/heads/main/screenshots/offendersearch-2026-09-02T150825.png
security:
- kind: authentication
  name: Offendersearch Authentication
  slug: offendersearch-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Offendersearch Domain Security
  slug: offendersearch-domain-security
  summary_line: TLSv1.3 · DMARC
slug: offendersearch
tags:
- Background Screening
- Identity & risk
- Trust and Safety
- Public Records
- Criminal data
- Compliance
- Sex-offender registry data
- Staffing & recruiting
- Tenant Screening
- Healthcare
- Gig marketplaces
---
