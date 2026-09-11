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
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-10'
api_count: 1
apis:
- baseURL: https://api.orionadvisor.com/api/v1
  baseurl_source: declared
  description: REST/JSON API (OrionApi) for the Orion Portfolio Accounting System, spanning Portfolio, Trading (Eclipse), Billing, Reporting, Orion Connect, Risk, Planning, Astro, Bulk Extracts, and Notification Web
  name: Orion API
  slug: orion-api
artifact_total: 7
asyncapis:
- description: ''
  name: Orion Advisor Solutions Webhooks
  slug: orion-advisor-solutions-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orion-advisor-solutions-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/orion-advisor-solutions-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://orion.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.orionadvisor.com/
- group: start
  title: ''
  type: Login
  url: https://login.orionadvisor.com/
- group: start
  title: ''
  type: SignUp
  url: https://developers.orionadvisor.com/creds-request/
- group: operate
  title: ''
  type: Support
  url: https://orion.com/contact
- group: company
  title: ''
  type: Blog
  url: https://orion.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/orionadvisor
- group: commercial
  title: ''
  type: TermsOfService
  url: https://orion.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://orion.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.orionadvisor.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trustcenter.orion.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trustcenter.orion.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/orion-advisor-solutions-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/orion-advisor-solutions-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/orion-advisor-solutions-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/orion-advisor-solutions-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/orion-advisor-solutions-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/orion-advisor-solutions-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/orion-advisor-solutions-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/orion-advisor-solutions-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/orion-advisor-solutions-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/orion-advisor-solutions-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/orion-advisor-solutions-rate-limits.yml
created: '2026-09-10'
description: US wealth-tech provider offering an open REST API framework for financial advisors and RIAs, covering portfolio accounting (Orion Connect), trading/rebalancing (Eclipse), billing, reporting, planning, risk, and client engagement. API access is credential-gated and provisioned to partners on request.
layout: provider
modified: '2026-09-10'
name: Orion Advisor Solutions
nav: Providers
network: true
overview: 'Orion Advisor Solutions publishes 1 API on the [APIs.io](https://apis.io/) network: Orion API. Tagged areas include wealth-management, fintech, financial-advisors, portfolio-accounting, and trading-rebalancing.


  The Orion Advisor Solutions catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Orion Advisor Solutions'' developer surface includes authentication, signup flow, support, engineering blog, sandbox, and 21 more developer resources.'
plans:
- name: Orion Advisor Solutions Plans Pricing
  plan_count: 0
  slug: orion-advisor-solutions-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Orion Advisor Solutions Rate Limits
  slug: orion-advisor-solutions-rate-limits
score:
  band: developing
  composite: 48.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 4.5
    contract_quality: 51.1
    developer_ergonomics: 66.1
    discoverability: 72.2
    governance: 4.5
    operational_transparency: 26.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  upsert:
    applies: true
    score: 22.2
security:
- kind: authentication
  name: Orion Advisor Solutions Authentication
  slug: orion-advisor-solutions-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Orion Advisor Solutions Domain Security
  slug: orion-advisor-solutions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Orion Advisor Solutions Trust Center
  slug: orion-advisor-solutions-trust-center
  summary_line: SOC 1 Type 1, SOC 1 Type 2, SOC 2 Type 2, ISO/IEC 27001:2022, ISO/IEC 42001:2023
slug: orion-advisor-solutions
tags:
- wealth-management
- fintech
- financial-advisors
- portfolio-accounting
- trading-rebalancing
- financial-planning
- billing
- reporting
- risk
- RIA-technology
website: https://orion.com
---
