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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Pixieset Agentic Access
  operation_count: 22
  slug: pixieset-agentic-access
  summary_line: 22 operations · 3 acting
api_count: 1
apis:
- baseURL: https://studio.pixieset.com/api/v1
  baseurl_source: declared
  description: Client and lead CRM records.
  name: Pixieset Clients API
  slug: pixieset-clients-api
- baseURL: https://studio.pixieset.com/api/v1
  baseurl_source: declared
  description: Gallery collections, access, and downloads.
  name: Pixieset Collections API
  slug: pixieset-collections-api
- baseURL: https://studio.pixieset.com/api/v1
  baseurl_source: declared
  description: Contracts and contract templates.
  name: Pixieset Contracts API
  slug: pixieset-contracts-api
- baseURL: https://studio.pixieset.com/api/v1
  baseurl_source: declared
  description: Invoices and payments.
  name: Pixieset Invoices API
  slug: pixieset-invoices-api
- baseURL: https://studio.pixieset.com/api/v1
  baseurl_source: declared
  description: Bookable session types, scheduling, and availability.
  name: Pixieset Sessions API
  slug: pixieset-sessions-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pixieset Studio & Gallery API (Modeled, Unofficial) Clients API
  slug: open-pixieset-clients-api
- collection_type: open
  name: Pixieset Studio & Gallery API (Modeled, Unofficial) Clients Collections API
  slug: open-pixieset-collections-api
- collection_type: open
  name: Pixieset Studio & Gallery API (Modeled, Unofficial) Clients Contracts API
  slug: open-pixieset-contracts-api
- collection_type: open
  name: Pixieset Studio & Gallery API (Modeled, Unofficial) Clients Invoices API
  slug: open-pixieset-invoices-api
- collection_type: open
  name: Pixieset Studio & Gallery API (Modeled, Unofficial) Clients Sessions API
  slug: open-pixieset-sessions-api
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
random_paper: 14
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 49.0
    catalog_earned_first_party: 0.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.6
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 39.2
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 29.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pixieset/refs/heads/main/screenshots/pixieset-2026-09-02T151341.png
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
