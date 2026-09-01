---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.1
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The docs API from Soda Health — 10 operation(s) for docs.
  name: Soda Health docs API
  slug: soda-health-docs-api
- description: The docs-auth API from Soda Health — 2 operation(s) for docs-auth.
  name: Soda Health docs-auth API
  slug: soda-health-docs-auth-api
- description: The Evermore Docs Portal API from Soda Health — 1 operation(s) for evermore docs portal.
  name: Soda Health Evermore Docs Portal API
  slug: soda-health-evermore-docs-portal-api
- description: The health API from Soda Health — 3 operation(s) for health.
  name: Soda Health health API
  slug: soda-health-health-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Evermore Portal docs API
  slug: open-soda-health-docs-api
- collection_type: open
  name: Evermore Portal docs docs-auth API
  slug: open-soda-health-docs-auth-api
- collection_type: open
  name: Evermore Portal docs Evermore Docs Portal API
  slug: open-soda-health-evermore-docs-portal-api
- collection_type: open
  name: Evermore Portal docs health API
  slug: open-soda-health-health-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.evermoreoutcomes.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.evermoreoutcomes.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.evermoreoutcomes.com/api/openapi.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/soda-health-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/soda-health-domain-security.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/soda-health-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/soda-health-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/soda-health-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/soda-health-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/soda-health-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/soda-health-lifecycle.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/soda-health-docs-portal-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/soda-health-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/soda-health-browse-docs.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/soda-health-issue-magic-link.md
created: '2026-07-17'
description: 'Soda Health is a healthcare benefits technology company that builds a benefits administration and "health wallet" platform for health plans, powering supplemental benefits for Medicare Advantage and Medicaid members such as over-the-counter (OTC), healthy food and grocery, and other flex/spending-card benefits. The company now operates as Evermore Outcomes — sodahealth.com redirects to evermoreoutcomes.com and the product documentation is branded "Evermore Product Documentation," while account and program references still carry the Soda Health name. The public developer surface found is the Evermore Docs Portal API (docs.evermoreoutcomes.com): a Confluence-backed, customer-facing documentation portal secured with magic-link tokens and OIDC single sign-on, scoped per customer program. The core benefits/wallet product APIs are gated behind that portal and are not publicly published. Soda Health was surfaced as a portfolio company of Lightspeed Venture Partners.'
image: https://docs.evermoreoutcomes.com/favicon-192.png
layout: provider
mcp_servers:
- description: ''
  name: Soda Health MCP Server
  slug: soda-health-mcp-server
modified: '2026-07-21'
name: Soda Health
nav: Providers
network: true
overview: 'Soda Health publishes 4 APIs on the [APIs.io](https://apis.io/) network, including docs API, docs-auth API, Evermore Docs Portal API, and 1 more. Tagged areas include Company, Healthcare, Health Benefits, Medicare Advantage, and Medicaid.


  Soda Health''s developer surface includes documentation, API reference, authentication, and 12 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 52.0
    developer_ergonomics: 20.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 25.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Soda Health Authentication
  slug: soda-health-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Soda Health Domain Security
  slug: soda-health-domain-security
  summary_line: TLSv1.3 · DMARC
slug: soda-health
tags:
- Company
- Healthcare
- Health Benefits
- Medicare Advantage
- Medicaid
- Supplemental Benefits
- Benefits Administration
- Documentation Portal
website: https://docs.evermoreoutcomes.com/
---
