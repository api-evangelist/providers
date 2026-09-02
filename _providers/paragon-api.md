---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 10
  human_in_the_loop: 1
  name: Paragon Api Agentic Access
  operation_count: 17
  slug: paragon-api-agentic-access
  summary_line: 17 operations · 10 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: List and run third-party tools (actions) for AI agents.
  name: Paragon ActionKit API
  slug: paragon-api-actionkit-api
- description: Project and integration metadata, Connected User, and credentials.
  name: Paragon Connect API
  slug: paragon-api-connect-api
- description: Forward requests to third-party providers on behalf of a Connected User.
  name: Paragon Proxy API
  slug: paragon-api-proxy-api
- description: Enable, disable, and trigger Workflows and send App Events.
  name: Paragon Workflows API
  slug: paragon-api-workflows-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Paragon ActionKit API
  slug: open-paragon-api-actionkit-api
- collection_type: open
  name: Paragon ActionKit Connect API
  slug: open-paragon-api-connect-api
- collection_type: open
  name: Paragon ActionKit Proxy API
  slug: open-paragon-api-proxy-api
- collection_type: open
  name: Paragon ActionKit Workflows API
  slug: open-paragon-api-workflows-api
- collection_type: open
  name: Paragon API
  slug: open-paragon-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/paragon-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paragon-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paragon-api-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.useparagon.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.useparagon.com
- group: commercial
  title: ''
  type: Plans
  url: plans/paragon-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/paragon-api-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/paragon-api-finops.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/useparagon
created: '2026-07-12'
description: Paragon is an embedded iPaaS that lets SaaS companies build native, in-app integrations for their customers. Developers configure integrations, Managed Sync pipelines, Workflows, and ActionKit tools in Paragon, then embed them behind a Connect Portal so each of their end customers (Connected Users) can authenticate their own third-party accounts. Requests are made on behalf of Connected Users using a Paragon User Token - an RS256-signed JWT - across a REST Connect/SDK API (api.useparagon.com), a Workflows API, an ActionKit tool-calling API for AI agents (actionkit.useparagon.com), and a Proxy API (proxy.useparagon.com) that forwards requests to third-party providers. Paragon is a B2B, contact-sales product.
finops:
- name: Paragon Api Finops
  service_category: Integration Platform
  slug: paragon-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/paragon-api.png
layout: provider
modified: '2026-07-12'
name: Paragon
nav: Providers
network: true
overview: 'Paragon publishes 4 APIs on the [APIs.io](https://apis.io/) network, including ActionKit API, Connect API, Proxy API, and 1 more. Tagged areas include Embedded iPaaS, Integration, Embedded Integrations, Native Integrations, and Workflow-Automation.


  Paragon''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Paragon Api Plans Pricing
  plan_count: 3
  slug: paragon-api-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 3
  name: Paragon Api Rate Limits
  slug: paragon-api-rate-limits
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 55.8
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paragon-api/refs/heads/main/screenshots/paragon-api-2026-08-07T191416.png
security:
- kind: authentication
  name: Paragon Api Authentication
  slug: paragon-api-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Paragon Api Domain Security
  slug: paragon-api-domain-security
  summary_line: HSTS · DMARC
slug: paragon-api
tags:
- Embedded iPaaS
- Integration
- Embedded Integrations
- Native Integrations
- Workflow-Automation
- Integration Platform
- API Integration
- SaaS Integrations
- Connectors
website: https://www.useparagon.com
---
