---
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Findigs Agentic Access
  operation_count: 8
  slug: findigs-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 1
apis:
- description: REST API for programmatic interaction with Findigs and integration of Findigs data into existing property management systems and workflows. Covers listings (the window during which a unit accepts rent
  name: Findigs Client API
  slug: findigs-client-api
artifact_total: 10
asyncapis:
- description: ''
  name: Findigs Webhooks
  slug: findigs-webhooks
collections:
- collection_type: postman
  name: Findigs Client API
  slug: postman-findigs-client-api
- collection_type: open
  name: Findigs Client API
  slug: open-findigs-client-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.findigs.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.getfindigs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getfindigs.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.getfindigs.com/
- group: build
  title: ''
  type: Postman
  url: https://docs.getfindigs.com/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/findigs-client-api-openapi.yml
- group: company
  title: ''
  type: Blog
  url: https://www.findigs.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Findigs
- group: operate
  title: ''
  type: Support
  url: https://www.findigs.com/renters
- group: start
  title: ''
  type: Login
  url: https://app.findigs.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.findigs.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.findigs.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.findigs.com/legal/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.findigs.com/legal/responsible-disclosure-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/findigs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/findigs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/findigs-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/findigs-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/findigs-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/findigs-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/findigs-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/findigs-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/findigs-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/findigs-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/findigs-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/findigs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/findigs-rate-limits.yml
- group: build
  title: ''
  type: Examples
  url: examples/findigs-client-api-examples.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/findigs-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/findigs-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/findigs-client-api-overlay.yaml
created: '2026-08-12'
description: Findigs is a New York City based residential real estate decisioning platform that screens rental applicants for identity, income, employment, credit, criminal history, eviction records, documents and pets, then applies automated underwriting against each operator's own written policy criteria to render a full yes/no decision on every rental application rather than handing back raw screening reports. The platform spans screening, underwriting, policy optimization and post-lease performance data, is backed by a contractual fraud guarantee, and reports a median decision time of 3.4 hours across 400K+ rental units. Findigs publishes a machine-readable Client API — an OpenAPI 3.1.0 contract served from api.client.findigs.com covering listings, applications and applicant groups, authenticated with a scoped X-API-KEY header and paired with a sandbox environment and a terse webhook event surface — though the company states the Client API is closed to new clients and existing integrators
  should contact integrations@findigs.com.
image: https://www.findigs.com/opengraph-image?title=Resident%20screening%20and%20rental%20decisioning%20%7C%20Findigs&variant=home
layout: provider
modified: '2026-08-12'
name: Findigs
nav: Providers
network: true
overview: 'Findigs publishes 1 API on the [APIs.io](https://apis.io/) network: Client API. Tagged areas include rental-screening, Tenant Screening, resident-screening, rental-application, and Underwriting.


  The Findigs catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Findigs'' developer surface includes documentation, API reference, engineering blog, support, pricing, authentication, sandbox, and 25 more developer resources.'
plans:
- name: Findigs Plans Pricing
  plan_count: 3
  slug: findigs-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Findigs Rate Limits
  slug: findigs-rate-limits
score:
  band: strong
  composite: 58.1
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 16.7
    contract_quality: 63.9
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 21.1
  previous_composite: 58.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 54.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/findigs/refs/heads/main/screenshots/findigs-2026-08-17T080925.png
security:
- kind: authentication
  name: Findigs Authentication
  slug: findigs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Findigs Domain Security
  slug: findigs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Findigs Vulnerability Disclosure
  slug: findigs-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: findigs
tags:
- rental-screening
- Tenant Screening
- resident-screening
- rental-application
- Underwriting
- Decisioning
- Identity Verification
- Income Verification
- Credit Check
- Background Check
- Fraud Detection
- Property Management
- Real-Estate
- PropTech
- FCRA
- Fair Housing
- Webhook
website: https://www.findigs.com/
---
