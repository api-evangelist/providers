---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 37
  human_in_the_loop: 0
  name: Fintary Agentic Access
  operation_count: 81
  slug: fintary-agentic-access
  summary_line: 81 operations · 37 acting
api_count: 4
apis:
- baseURL: https://api.fintary.com
  baseurl_source: declared
  description: The Agents API from Fintary — 7 operation(s) for agents.
  name: Fintary Agents API
  slug: fintary-agents-api
- baseURL: https://api.fintary.com
  baseurl_source: declared
  description: Agent management endpoints
  name: Fintary AMS - Agents API
  slug: fintary-ams-agents-api
- baseURL: https://api.fintary.com
  baseurl_source: declared
  description: AMS configuration endpoints (statuses, roles)
  name: Fintary AMS - Configs API
  slug: fintary-ams-configs-api
- baseURL: https://api.fintary.com
  baseurl_source: declared
  description: Customer management endpoints
  name: Fintary AMS - Customers API
  slug: fintary-ams-customers-api
- baseURL: https://api.fintary.com
  baseurl_source: declared
  description: Policy management endpoints
  name: Fintary AMS - Policies API
  slug: fintary-ams-policies-api
- baseURL: https://api.fintary.com
  baseurl_source: declared
  description: The AMS - Registry API from Fintary — 5 operation(s) for ams - registry.
  name: Fintary AMS - Registry API
  slug: fintary-ams-registry-api
- baseURL: https://api.fintary.com
  baseurl_source: declared
  description: The AMS - Tasks API from Fintary — 5 operation(s) for ams - tasks.
  name: Fintary AMS - Tasks API
  slug: fintary-ams-tasks-api
- baseURL: https://api.fintary.com
  baseurl_source: declared
  description: The Analytics API from Fintary — 8 operation(s) for analytics.
  name: Fintary Analytics API
  slug: fintary-analytics-api
- baseURL: https://api.fintary.com
  baseurl_source: declared
  description: The Commission Reports API from Fintary — 1 operation(s) for commission reports.
  name: Fintary Commission Reports API
  slug: fintary-commission-reports-api
- baseURL: https://api.fintary.com
  baseurl_source: declared
  description: The Documents API from Fintary — 2 operation(s) for documents.
  name: Fintary Documents API
  slug: fintary-documents-api
artifact_total: 20
common:
- group: other
  href: https://artifacts.apis.io/fintary/capabilities/fintary-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/fintary-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/fintary/overlays/fintary-open-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fintary-open-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/fintary/overlays/fintary-ams-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fintary-ams-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://fintary.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fintary.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fintary.com/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://www.fintary.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://fintary.com/resources
- group: docs
  title: ''
  type: Documentation
  url: https://api.fintary.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://api.fintary.com/openapi-doc
- group: start
  title: ''
  type: Login
  url: https://app.fintary.com
- group: operate
  title: ''
  type: StatusPage
  url: https://fintary.instatus.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.fintary.com/carriers
- group: auth
  href: https://artifacts.apis.io/fintary/security/fintary-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fintary-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/fintary/authentication/fintary-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fintary-authentication.yml
- group: design
  href: https://artifacts.apis.io/fintary/conventions/fintary-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fintary-conventions.yml
- group: design
  href: https://artifacts.apis.io/fintary/errors/fintary-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fintary-problem-types.yml
- group: design
  href: https://artifacts.apis.io/fintary/data-model/fintary-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fintary-data-model.yml
- group: design
  href: https://artifacts.apis.io/fintary/lifecycle/fintary-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fintary-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/fintary/conformance/fintary-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fintary-conformance.yml
- group: build
  href: https://artifacts.apis.io/fintary/packages/fintary-packages.yml
  title: ''
  type: Packages
  url: packages/fintary-packages.yml
- group: agent
  href: https://artifacts.apis.io/fintary/mcp/fintary-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/fintary-mcp.yml
- group: agent
  href: https://artifacts.apis.io/fintary/llms/fintary-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fintary-llms.txt
- group: agent
  href: https://artifacts.apis.io/fintary/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/fintary/agentic-access/fintary-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fintary-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/fintary/plans/fintary-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fintary-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/fintary/rate-limits/fintary-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fintary-rate-limits.yml
created: '2026-07-17'
description: Fintary is an AI-powered commission management and revenue operations platform for insurance distribution — serving brokerages, carriers, and wealth firms. It automates compensation calculation and reporting across complex hierarchies, splits, overrides, and bonuses; reconciles carrier statement data; monitors chargebacks; surfaces real-time revenue and profitability analytics; and provides a white-label producer portal for 24/7 commission visibility. Fintary integrates with agency and distribution systems such as Applied Epic, Agency Integrator, SmartOffice, OneHQ, and BenefitPoint. Fintary publishes two OpenAPI 3.0.0 contracts on its own API host at api.fintary.com — a customer-facing Open API (agents, commissions, payouts, policies, analytics datasets/reports/widgets, document upload) and an AMS API (policies, customers, agents, contracts, hierarchy, tasks, document repository, page-config registry) — plus SSO integration guides for external identity providers. This profile
  is maintained in the API Evangelist network.
image: https://cdn.prod.website-files.com/6891283959a9d392e4db12c1/68d598f0c0abbe7967241ea6_fintary-webclip.png
layout: provider
modified: '2026-08-14'
name: Fintary
nav: Providers
network: true
overview: 'Fintary publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, AMS - Agents API, AMS - Configs API, and 7 more. Tagged areas include Company, Fintech, Insurance, Insurtech, and Commissions.


  The Fintary catalog on APIs.io includes 1 Spectral governance ruleset.


  Fintary''s developer surface includes support, engineering blog, documentation, API reference, authentication, and 22 more developer resources.'
plans:
- name: Fintary Plans Pricing
  plan_count: 0
  slug: fintary-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Fintary Rate Limits
  slug: fintary-rate-limits
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: Fintary API Rules
  rule_count: 45
  severity_counts:
    error: 33
    hint: 0
    info: 1
    warn: 11
  slug: fintary-rules
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 24
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    contract_governance: 31.8
    contract_quality: 44.1
    developer_ergonomics: 37.5
    discoverability: 71.4
    operational_transparency: 0.0
  previous_composite: 37.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 26.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/fintary/fintary-2026-07-25T214544.png
security:
- kind: authentication
  name: Fintary Authentication
  slug: fintary-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Fintary Domain Security
  slug: fintary-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: Assemble an agent's compensation picture
  slug: fintary-agent-compensation-review
- name: Manage a policy through the Fintary AMS API
  slug: fintary-ams-policy-lifecycle
- name: Query and export a Fintary analytics report or dataset
  slug: fintary-export-analytics-report
- name: Onboard a Fintary agent and place them in the hierarchy
  slug: fintary-onboard-agent-and-set-upline
slug: fintary
tags:
- Company
- Fintech
- Insurance
- Insurtech
- Commissions
- Revenue Operations
- Analytics
- Agency Management
- Policy Management
- Payouts
- Reconciliation
- OpenAPI
website: https://fintary.com/
---
