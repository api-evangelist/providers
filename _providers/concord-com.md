---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
- acting_count: 1
  human_in_the_loop: 0
  name: Concord Com Agentic Access
  operation_count: 9
  slug: concord-com-agentic-access
  summary_line: 9 operations · 1 acting
api_count: 1
apis:
- description: Concord sends outbound HTTP POST webhooks to a URL you configure in the Automations > Integrations UI, firing on agreement lifecycle events - document fully approved, document fully signed, document e
  name: Concord Webhooks (Outbound Events)
  slug: concord-com-webhooks-api
- description: Agreements (contracts), their attachments, and members.
  name: Concord Agreements API
  slug: concord-com-agreements-api
- description: Organization-level resources - reports, groups, and tags.
  name: Concord Organizations API
  slug: concord-com-organizations-api
- description: Document generation from automated templates (modeled/unconfirmed).
  name: Concord Templates API
  slug: concord-com-templates-api
- description: The authenticated user and their organization memberships.
  name: Concord Users API
  slug: concord-com-users-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Concord Agreements API
  slug: open-concord-com-agreements-api
- collection_type: open
  name: Concord Agreements Organizations API
  slug: open-concord-com-organizations-api
- collection_type: open
  name: Concord Agreements Templates API
  slug: open-concord-com-templates-api
- collection_type: open
  name: Concord Agreements Users API
  slug: open-concord-com-users-api
- collection_type: open
  name: Concord API
  slug: open-concord-com
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/concord-com-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/concord-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/concord-com-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.concord.app
- group: docs
  title: ''
  type: Documentation
  url: https://help.concord.app/concord-api
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/concordnow
- group: commercial
  title: ''
  type: Plans
  url: plans/concord-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/concord-com-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/concord-com-finops.yml
created: '2026-07-12'
description: Concord is a contract lifecycle management (CLM) platform for creating, negotiating, redlining, e-signing, storing, and tracking agreements in one place, with unlimited electronic signatures, automated templates, approval workflows, and reporting. Concord exposes a documented REST API (base https://api.concordnow.com/api/rest/1) that lets integrators read a user's organizations, list and retrieve agreements and their attachments and members, and pull organization reports, groups, and tags. Outbound webhooks notify external systems of agreement lifecycle events (fully approved, fully signed, expired, signature provided). API key generation is offered on paid plans only.
finops:
- name: Concord Com Finops
  service_category: Contract Lifecycle Management
  slug: concord-com-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/concord-com.png
layout: provider
modified: '2026-07-12'
name: Concord
nav: Providers
network: true
overview: 'Concord publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Agreements API, Organizations API, Templates API, and 1 more. Tagged areas include Contract Management, Contract Lifecycle Management, CLM, Contracts, and Agreements.


  Concord''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Concord Com Plans Pricing
  plan_count: 3
  slug: concord-com-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 3
  name: Concord Com Rate Limits
  slug: concord-com-rate-limits
score:
  band: thin
  composite: 29.0
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
    contract_quality: 13.9
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 29.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/concord-com/refs/heads/main/screenshots/concord-com-2026-07-25T210223.png
security:
- kind: authentication
  name: Concord Com Authentication
  slug: concord-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Concord Com Domain Security
  slug: concord-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: concord-com
tags:
- Contract Management
- Contract Lifecycle Management
- CLM
- Contracts
- Agreements
- E-Signature
- Document-Management
- Legal
- Workflows
website: https://www.concord.app
---
