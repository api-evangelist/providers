---
access_model:
  confidence: medium
  label: Contact sales / customer tenant
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - authentication
  - documentation
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.7
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 39
  human_in_the_loop: 0
  name: Fintary Agentic Access
  operation_count: 81
  slug: fintary-agentic-access
  summary_line: 81 operations · 39 acting
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
artifact_total: 15
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/fintary-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/fintary-open-api-overlay.yaml
- group: other
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
  title: ''
  type: DomainSecurity
  url: security/fintary-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fintary-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fintary-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fintary-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fintary-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fintary-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fintary-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/fintary-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/fintary-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fintary-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fintary-agentic-access.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/fintary-plans-pricing.yml
- group: operate
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
overview: 'Fintary publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Agents API, AMS - Agents API, AMS - Configs API, and 7 more. Tagged areas include Company, Fintech, Insurance, Insurtech, and Commissions.


  Fintary''s developer surface includes support, engineering blog, documentation, API reference, authentication, and 22 more developer resources.'
plans:
- name: Fintary Plans Pricing
  plan_count: 0
  slug: fintary-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Fintary Rate Limits
  slug: fintary-rate-limits
score:
  band: developing
  composite: 41.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 52.5
    developer_ergonomics: 37.5
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 41.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
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
    score: 53.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fintary/refs/heads/main/screenshots/fintary-2026-07-25T214544.png
security:
- kind: authentication
  name: Fintary Authentication
  slug: fintary-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Fintary Domain Security
  slug: fintary-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
