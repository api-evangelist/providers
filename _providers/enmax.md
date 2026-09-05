---
access_model:
  confidence: high
  label: Free · No published developer program; open ArcGIS grid services are anonymous
  onboarding: unknown
  pricing: free
  public: true
  source:
  - documentation
  - probing
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.2
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The machine-readable grid data behind ENMAX Power's public Hosting Capacity, Load Capacity and Service Area maps. The three maps published at enmax.com/system-resources are ArcGIS Online Web AppBuilde
  name: ENMAX Power System Capacity ArcGIS Feature Services
  slug: enmax-power-system-capacity-arcgis-feature-services
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/enmax-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/enmax-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/enmax-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/enmax-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/enmax-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/enmax-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/enmax-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/enmax-conformance.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/enmax-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.enmax.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.enmax.com/system-resources
- group: company
  title: ''
  type: About
  url: https://www.enmax.com/about-us
- group: company
  title: ''
  type: Blog
  url: https://www.enmax.com/news
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/enmax
- group: start
  title: ''
  type: SignUp
  url: https://myaccount.enmax.com/register
- group: start
  title: ''
  type: Login
  url: https://myaccount.enmax.com/
- group: operate
  title: ''
  type: Support
  url: https://www.enmax.com/customer-support
- group: operate
  title: ''
  type: Contact
  url: https://www.enmax.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.enmax.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.enmax.com/privacy
- group: operate
  title: ''
  type: Status
  url: https://outages.enmax.com/
created: '2026-07-27'
description: 'ENMAX Corporation is the Calgary-based energy company owned outright by The City of Calgary, describing itself on its own about page as "a regulated wires company, a competitive power generator and an energy retailer" operating "across Alberta and Maine." It spans three tiers of the value chain at once: ENMAX Power owns and operates the regulated electricity distribution and transmission system inside Calgary, ENMAX Energy generates power and sells electricity and natural gas into Alberta''s deregulated retail market under the Easymax brand, and Versant Power — acquired from Emera in 2020 — is the transmission and distribution utility for northern and eastern Maine. Its API posture is the exact inverse of the Ontario utilities it is usually compared to, and the inversion is the finding. No consumer energy data mandate binds ENMAX anywhere it operates: Alberta has no Green Button regulation, Ontario''s O. Reg. 633/21 does not reach across the provincial border, Canada has no
  national equivalent, and Maine imposes no Green Button obligation on Versant Power. Unmandated, ENMAX built nothing — its own support documentation states plainly that the Energy Insights usage view inside a customer''s Easymax account "is view-only within your online account and can''t be exported at this time," which is a harder closure than most: not merely no API, but no CSV, no XML, and no Green Button either. There is no developer portal, no developer, api, docs or data subdomain, no OpenAPI, and no published third-party data path. What ENMAX does publish openly is grid data. Its Hosting Capacity, Load Capacity and Service Area maps, linked from enmax.com/system-resources, are ArcGIS Online web applications backed by ArcGIS REST feature services that answer anonymous machine-readable queries with no key, no signup and no terms — distribution-feeder DER hosting headroom and remaining load capacity for the Calgary service territory, the data a solar or storage developer actually needs.
  ENMAX never calls this an API and documents none of it, but it is real, it is open, and it is queryable. Wide open on grid data, completely shut on customer data.'
examples:
- key_count: 1
  name: Enmax Error Invalid Field Response
  slug: enmax-error-invalid-field-response
- key_count: 9
  name: Enmax Hosting Capacity Query Response
  slug: enmax-hosting-capacity-query-response
- key_count: 9
  name: Enmax Load Capacity Query Response
  slug: enmax-load-capacity-query-response
- key_count: 8
  name: Enmax Service Area Query Response
  slug: enmax-service-area-query-response
image: https://www.enmax.com/favicon.ico
layout: provider
modified: '2026-07-27'
name: ENMAX
nav: Providers
network: true
overview: 'ENMAX publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Canada, Utilities, Electricity, and Natural Gas.


  ENMAX''s developer surface includes authentication, code examples, documentation, engineering blog, signup flow, support, status page, and 15 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 1
  name: Enmax Rate Limits
  slug: enmax-rate-limits
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 6.7
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 28.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/enmax/refs/heads/main/screenshots/enmax-2026-08-07T164928.png
security:
- kind: authentication
  name: Enmax Authentication
  slug: enmax-authentication
  summary_line: none · 1 scheme
- kind: domain-security
  name: Enmax Domain Security
  slug: enmax-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: enmax
tags:
- Energy
- Canada
- Utilities
- Electricity
- Natural Gas
- Grid
- Smart Metering
- Solar
- DER
- Geospatial
- Alberta
- Electricity Distribution
website: https://www.enmax.com/
---
