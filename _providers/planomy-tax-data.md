---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 59.5
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Planomy Tax Data Agentic Access
  operation_count: 2
  slug: planomy-tax-data-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- description: Dated, source-attributed US tax and retirement figures.
  name: Planomy Tax Data Tax Data API
  slug: planomy-tax-data-tax-data-api
artifact_total: 10
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/planomy-tax-data-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/planomy-tax-data-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://planomy.net/
- group: operate
  title: ''
  type: Support
  url: mailto:support@planomy.net
- group: commercial
  title: ''
  type: Pricing
  url: https://planomy.net/pricing
- group: start
  title: ''
  type: SignUp
  url: https://planomy.net/app/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://planomy.net/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://planomy.net/legal/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/planomy-tax-data-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/planomy-tax-data-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/planomy-tax-data-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/planomy-tax-data-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/planomy-tax-data-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/planomy-tax-data-data-model.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/planomy-tax-data-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/planomy-tax-data-plans-pricing.yml
- group: design
  title: ''
  type: Components
  url: components/planomy-tax-data-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/planomy-tax-data-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-28'
description: 'A free, keyless open-data JSON API publishing the 2026 US retirement and tax figures that drive the Planomy local-first personal-finance planner: federal income-tax brackets and the standard deduction, FICA rates and the Social Security wage base, the COLA and retirement earnings test, Medicare Part A/B/D premiums and deductibles with the full IRMAA tier tables, contribution limits for employer plans, IRA, SIMPLE, HSA, HDHP and health FSA, Roth and traditional-IRA phase-outs, Saver''s Credit thresholds, RMD applicable ages, and a set of state income-tax presets. Two static JSON endpoints — a year manifest and one document per tax year — served from a Cloudflare CDN with no key, no sign-up and no quota. Its distinguishing feature is provenance: every section carries a source key that resolves to a named IRS, SSA, CMS or Federal Register document with the date it was last verified, so any single figure can be cited back to the government publication it came from.'
examples:
- key_count: 16
  name: Planomy Tax Data 2026
  slug: planomy-tax-data-2026
- key_count: 6
  name: Planomy Tax Data Index
  slug: planomy-tax-data-index
image: https://planomy.net/og/og-home.png
json_schemas:
- name: Planomy Tax Data Index
  property_count: 6
  slug: planomy-tax-data-index
- name: Planomy Tax Year Dataset
  property_count: 16
  slug: planomy-tax-data-tax-year-dataset
layout: provider
mcp_servers:
- description: ''
  name: planomy-tax-data-mcp.yml
  slug: planomy-tax-data-mcpyml
modified: '2026-08-09'
name: Planomy Tax Data
nav: Providers
network: true
overview: 'Planomy Tax Data publishes 1 API on the [APIs.io](https://apis.io/) network: Tax Data API. Tagged areas include tax, finance, open-data, retirement, and government.


  Planomy Tax Data''s developer surface includes support, pricing, signup flow, authentication, and 15 more developer resources.'
plans:
- name: Planomy Tax Data Plans Pricing
  plan_count: 5
  slug: planomy-tax-data-plans-pricing
random_paper: 93
score:
  band: developing
  composite: 49.0
  facets:
    commercial_clarity: 76.3
    contract_quality: 62.8
    developer_ergonomics: 30.4
    discoverability: 87.0
    governance: 31.3
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
security:
- kind: authentication
  name: Planomy Tax Data Authentication
  slug: planomy-tax-data-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Planomy Tax Data Domain Security
  slug: planomy-tax-data-domain-security
  summary_line: TLSv1.3 · HSTS
slug: planomy-tax-data
tags:
- tax
- finance
- open-data
- retirement
- government
- personal-finance
- irs
- social-security
- medicare
- json
website: https://planomy.net/
---
