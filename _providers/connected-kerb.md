---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
api_count: 2
apis:
- description: Connected Kerb operates a live Open Charge Point Interface (OCPI) CPO endpoint on its own charge point management host. The version negotiation endpoint and the 2.1.1 / 2.2 / 2.2.1 version detail endp
  name: Connected Kerb OCPI (CPO) Interface
  slug: ocpi
- description: Connected Kerb runs its charge point management system on the AMPECO EV charging platform, and the platform Public API is live on Connected Kerb's own host at cp.connectedkerb.com/public-api/. Resourc
  name: Connected Kerb Charge Point Platform API (AMPECO Public API tenant)
  slug: public-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.connectedkerb.com/
- group: company
  title: ''
  type: Blog
  url: https://www.connectedkerb.com/stories-reports-and-events/
- group: operate
  title: ''
  type: Support
  url: https://www.connectedkerb.com/contact-us/customer-support/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.connectedkerb.com/our-technology/charging-tariffs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.connectedkerb.com/our-technology/software/app-ts-cs/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.connectedkerb.com/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://portal.connectedkerb.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Connected-Kerb
- group: operate
  title: ''
  type: Contact
  url: https://www.connectedkerb.com/contact-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/connected-kerb/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/ConnectedKerb
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/connectedkerb/
- group: company
  title: ''
  type: Careers
  url: https://apply.workable.com/connected-kerb/?lng=en
- group: other
  title: ''
  type: Locations
  url: https://locations.connectedkerb.com/
- group: other
  title: ''
  type: MobileApp
  url: https://www.connectedkerb.com/our-technology/software/our-app/
- group: other
  title: ''
  type: Profile
  url: https://forgeglobal.com/connected-kerb_stock/
- group: auth
  title: ''
  type: Authentication
  url: authentication/connected-kerb-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/connected-kerb-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/connected-kerb-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/connected-kerb-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/connected-kerb-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/connected-kerb-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/connected-kerb-llms.txt
created: '2026-08-04'
description: Connected Kerb is a UK electric-vehicle charging company that designs, installs, owns and operates public on-street and destination charge points, with a particular focus on residential drivers who have no off-street parking. Founded in 2017 and headquartered in London, it delivers long-term charging concessions for local authorities, workplaces, retail destinations, car parks and residential developers, and by mid-2026 operated roughly 7,800 public chargers across about 1,780 UK locations. Its Chameleon, Gecko, Scarab and Limpet charge points are backed by a charge point management system, a driver mobile app, a customer portal for site hosts and landowners, and an OCPI roaming interface used for e-mobility roaming and for UK Public Charge Point Regulations 2023 open-data obligations.
image: https://www.connectedkerb.com/media/ltve5t2y/ev-cars-charging.jpg
layout: provider
modified: '2026-08-04'
name: Connected Kerb
nav: Providers
network: true
overview: 'Connected Kerb publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, EV Charging, Electric Vehicles, Charge Point Operator, and Energy.


  Connected Kerb''s developer surface includes engineering blog, support, pricing, authentication, and 19 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 23.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/connected-kerb/refs/heads/main/screenshots/connected-kerb-2026-08-07T163755.png
security:
- kind: authentication
  name: Connected Kerb Authentication
  slug: connected-kerb-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Connected Kerb Domain Security
  slug: connected-kerb-domain-security
  summary_line: TLSv1.3
slug: connected-kerb
tags:
- Company
- EV Charging
- Electric Vehicles
- Charge Point Operator
- Energy
- Transportation
- Smart Charging
- OCPI
- Roaming
- United Kingdom
- Infrastructure
- Sustainability
website: https://www.connectedkerb.com/
---
