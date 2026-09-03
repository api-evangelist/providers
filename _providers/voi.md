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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-02'
api_count: 3
apis:
- description: Deep-integration Mobility-as-a-Service API for partners to complete full user journeys inside their own apps - register users, discover vehicles by zone, get per-vehicle pricing, start and end rentals
  name: Voi MaaS Partner API
  slug: voi-maas-partner-api
- description: Voi's implementation of the Open Mobility Foundation Mobility Data Specification (MDS) provider API, giving cities and authorized partners historical trips, status changes, and a near-real-time events
  name: Voi MDS Provider API
  slug: voi-mds-provider-api
- description: 'A flavored implementation of the General Bikeshare Feed Specification for Voi''s dockless fleet, supporting the gbfs.json auto-discovery file, system_information, and free_bike_status per zone, with a '
  name: Voi GBFS API
  slug: voi-gbfs-api
artifact_total: 5
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/voiapp/mobility-data-specification/blob/dev/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.voi.com
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/voiapp/partner-api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/voiapp/partner-api-docs/blob/gh-pages/maas-pro.md
- group: start
  title: ''
  type: GettingStarted
  url: https://www.voi.com/help/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.voi.com/help
- group: company
  title: ''
  type: Blog
  url: https://www.voi.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/voiapp
- group: commercial
  title: ''
  type: Pricing
  url: https://www.voi.com/pricing-and-passes
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.voi.com/legal/user-agreement/uk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.voi.com/legal/privacy-policy/uk
- group: auth
  title: ''
  type: Authentication
  url: authentication/voi-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/voi-error-codes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/voi-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/voi-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/voi-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/voi-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/voi-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/voi-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/voi-llms.txt
- group: start
  title: ''
  type: Portal
  url: https://docs.voiscooters.com/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/voiapp/mobility-data-specification
- group: other
  title: ''
  type: Company
  url: https://www.voi.com/about
- group: company
  title: ''
  type: About
  url: https://careers.voi.com/pages/our-voiage-so-far
- group: company
  title: ''
  type: Careers
  url: https://careers.voi.com/
- group: company
  title: ''
  type: PressRoom
  url: https://www.voi.com/newsroom
- group: operate
  title: ''
  type: Help
  url: https://www.voi.com/support
- group: operate
  title: ''
  type: Contact
  url: https://www.voi.com/contact
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/voi-technology
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/voi-technology/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/voiscooters
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/voiscooters/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@VoiTechnology
created: '2026-07-17'
description: Voi Technology is a Swedish micromobility company founded in Stockholm in 2018 that operates shared e-scooters and e-bikes in more than 100 cities across Europe. Voi publishes a Mobility-as-a-Service partner surface for deep integrations (register users, start and end rentals, pricing, vehicles, and zone areas at partners.voiapp.io), plus MDS provider and flavored GBFS feeds for cities and mobility partners at mds.voiapp.io.
image: https://raw.githubusercontent.com/voiapp/partner-api-docs/gh-pages/assets/images/user/logo_coral.svg
layout: provider
modified: '2026-08-08'
name: Voi
nav: Providers
network: true
overview: 'Voi publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Micromobility, E-Scooters, E-Bikes, Mobility As A Service, and Transportation.


  Voi''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 27 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 13
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 29.1
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/voi/refs/heads/main/screenshots/voi-2026-06-20T201128.png
security:
- kind: authentication
  name: Voi Authentication
  slug: voi-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Voi Domain Security
  slug: voi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: voi
tags:
- Micromobility
- E-Scooters
- E-Bikes
- Mobility As A Service
- Transportation
- GBFS
- MDS
- Sweden
website: https://www.voi.com
---
