---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Pixieset Agentic Access
  operation_count: 22
  slug: pixieset-agentic-access
  summary_line: 22 operations · 3 acting
api_count: 5
apis:
- description: Client and lead CRM records.
  name: Pixieset Clients API
  slug: pixieset-clients-api
- description: Gallery collections, access, and downloads.
  name: Pixieset Collections API
  slug: pixieset-collections-api
- description: Contracts and contract templates.
  name: Pixieset Contracts API
  slug: pixieset-contracts-api
- description: Invoices and payments.
  name: Pixieset Invoices API
  slug: pixieset-invoices-api
- description: Bookable session types, scheduling, and availability.
  name: Pixieset Sessions API
  slug: pixieset-sessions-api
artifact_total: 9
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pixieset-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pixieset-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pixieset-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pixieset
- group: company
  title: ''
  type: Website
  url: https://pixieset.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.pixieset.com/hc/en-us
- group: commercial
  title: ''
  type: Plans
  url: plans/pixieset-plans-pricing.yml
created: '2026-07-04'
description: Pixieset is an all-in-one photography business platform - client galleries, a store for print/digital sales, a website builder, a mobile gallery app, and Studio Manager (CRM, booking, invoicing, contracts, questionnaires) - used by hundreds of thousands of photographers. Pixieset does not publish a public or partner developer API, does not run a developer program, and has no self-serve API keys or OAuth signup; there is no official API reference, SDK, or webhook system for third parties. The product itself is powered internally by two session-cookie-authenticated web APIs (a Studio API at studio.pixieset.com/api/v1 for business management and a Gallery API at galleries.pixieset.com/api/v1 for gallery delivery and e-commerce) that Pixieset's own web app calls, and which an independent developer has reverse-engineered and published as unofficial, unaffiliated documentation (111+ endpoints). This entry documents that real access model honestly - no public API exists, and the endpoint
  shapes below are modeled from that third-party reverse-engineering effort, not from any Pixieset-published reference - treat them as unverified and subject to change or removal without notice.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pixieset.png
layout: provider
modified: '2026-07-04'
name: Pixieset
nav: Providers
network: true
overview: 'Pixieset publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Clients API, Collections API, Contracts API, and 2 more. Tagged areas include Photography, Client Galleries, Studio Management, CRM, and Booking.


  Pixieset''s developer surface includes authentication, documentation, and 5 more developer resources.'
plans:
- name: Pixieset Plans Pricing
  plan_count: 8
  slug: pixieset-plans-pricing
random_paper: 20
score:
  band: thin
  composite: 31.6
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 55.8
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 31.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Pixieset Authentication
  slug: pixieset-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pixieset Domain Security
  slug: pixieset-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: pixieset
tags:
- Photography
- Client Galleries
- Studio Management
- CRM
- Booking
- Invoicing
- Contracts
- No Public API
website: https://pixieset.com
---
