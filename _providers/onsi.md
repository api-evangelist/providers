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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: verified
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Onsi Agentic Access
  operation_count: 20
  slug: onsi-agentic-access
  summary_line: 20 operations · 10 acting
api_count: 2
apis:
- description: The members API from Onsi — 7 operation(s) for members.
  name: Onsi members API
  slug: onsi-members-api
- description: The pay API from Onsi — 9 operation(s) for pay.
  name: Onsi pay API
  slug: onsi-pay-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://onsi.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.onsi.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.onsi.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.onsi.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.onsi.com/docs/member-management/get-started
- group: operate
  title: ''
  type: Support
  url: https://onsi.com/contact
- group: company
  title: ''
  type: Blog
  url: https://onsi.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pages.onsi.com/onsi-global-privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pages.onsi.com/onsi-terms-of-use-uk-and-row
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.onsi.com/docs/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/onsi-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/onsi-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/onsi-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/onsi-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/onsi-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/onsi-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/onsi-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/onsi-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/onsi-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/onsi-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/onsi-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/onsi-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onsi-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/onsi-agentic-access.yml
created: '2026-07-17'
description: Onsi is a global technology provider and UK/EU insurance intermediary that delivers flexible, shift-linked worker benefits — on-demand ("Embedded") pay, insurance cover, and a rewards marketplace — to employers and their frontline workers. Its Partner (BMO) API lets benefit-program partners manage members (invite, read, update, replace, and offboard individually, in batches, or via full-list CSV jobs), read tiers and earned-wage balances, run on-demand pay withdrawals through a two-step intent/complete flow, and reconcile pay cycles and deductions with payroll. Authentication is an x-api-key header; requests support idempotency (x-idempotency-key, 7-day retention) and skip/take offset pagination, with a consistent code/message error envelope.
image: https://framerusercontent.com/assets/Kgx16PhdTJfIAzqiv0XeASdgeZU.jpg
layout: provider
mcp_servers:
- description: ''
  name: onsi-mcp.yml
  slug: onsi-mcpyml
modified: '2026-07-20'
name: Onsi
nav: Providers
network: true
overview: 'Onsi publishes 2 APIs on the [APIs.io](https://apis.io/) network: members API and pay API. Tagged areas include Company, Benefits, Earned Wage Access, On-Demand Pay, and Payroll.


  Onsi''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 18 more developer resources.'
random_paper: 36
rate_limits:
- limit_count: 0
  name: Onsi Rate Limits
  slug: onsi-rate-limits
score:
  band: thin
  composite: 38.4
  delta: -4.3
  facets:
    commercial_clarity: 21.1
    contract_quality: 43.1
    developer_ergonomics: 62.5
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 42.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Onsi Authentication
  slug: onsi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Onsi Domain Security
  slug: onsi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: onsi
tags:
- Company
- Benefits
- Earned Wage Access
- On-Demand Pay
- Payroll
- Fintech
- Insurance
- Workforce
- HR
- Health
website: https://onsi.com
---
