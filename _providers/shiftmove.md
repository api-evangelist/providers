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
  band: agent-aware
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
    error_semantics: documented
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
  score: 23.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Shiftmove Agentic Access
  operation_count: 40
  slug: shiftmove-agentic-access
  summary_line: 40 operations · 25 acting
api_count: 1
apis:
- baseURL: https://api.avrios.com
  baseurl_source: declared
  description: The Custom fields API from Shiftmove — 2 operation(s) for custom fields.
  name: Shiftmove Custom fields API
  slug: shiftmove-custom-fields-api
- baseURL: https://api.avrios.com
  baseurl_source: declared
  description: The Driver assignments API from Shiftmove — 4 operation(s) for driver assignments.
  name: Shiftmove Driver assignments API
  slug: shiftmove-driver-assignments-api
- baseURL: https://api.avrios.com
  baseurl_source: declared
  description: The Drivers API from Shiftmove — 5 operation(s) for drivers.
  name: Shiftmove Drivers API
  slug: shiftmove-drivers-api
- baseURL: https://api.avrios.com
  baseurl_source: declared
  description: The Invoices API from Shiftmove — 4 operation(s) for invoices.
  name: Shiftmove Invoices API
  slug: shiftmove-invoices-api
- baseURL: https://api.avrios.com
  baseurl_source: declared
  description: The Organizations API from Shiftmove — 1 operation(s) for organizations.
  name: Shiftmove Organizations API
  slug: shiftmove-organizations-api
- baseURL: https://api.avrios.com
  baseurl_source: declared
  description: The Vehicle assignments API from Shiftmove — 4 operation(s) for vehicle assignments.
  name: Shiftmove Vehicle assignments API
  slug: shiftmove-vehicle-assignments-api
- baseURL: https://api.avrios.com
  baseurl_source: declared
  description: The Vehicle financing API from Shiftmove — 1 operation(s) for vehicle financing.
  name: Shiftmove Vehicle financing API
  slug: shiftmove-vehicle-financing-api
- baseURL: https://api.avrios.com
  baseurl_source: declared
  description: The Vehicle license plates API from Shiftmove — 3 operation(s) for vehicle license plates.
  name: Shiftmove Vehicle license plates API
  slug: shiftmove-vehicle-license-plates-api
- baseURL: https://api.avrios.com
  baseurl_source: declared
  description: The Vehicle usages API from Shiftmove — 1 operation(s) for vehicle usages.
  name: Shiftmove Vehicle usages API
  slug: shiftmove-vehicle-usages-api
- baseURL: https://api.avrios.com
  baseurl_source: declared
  description: The Vehicles API from Shiftmove — 7 operation(s) for vehicles.
  name: Shiftmove Vehicles API
  slug: shiftmove-vehicles-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fleet API Specifications Custom fields API
  slug: open-shiftmove-custom-fields-api
- collection_type: open
  name: Fleet API Specifications Custom fields Driver assignments API
  slug: open-shiftmove-driver-assignments-api
- collection_type: open
  name: Fleet API Specifications Custom fields Drivers API
  slug: open-shiftmove-drivers-api
- collection_type: open
  name: Fleet API Specifications Custom fields Invoices API
  slug: open-shiftmove-invoices-api
- collection_type: open
  name: Fleet API Specifications Custom fields Organizations API
  slug: open-shiftmove-organizations-api
- collection_type: open
  name: Fleet API Specifications Custom fields Vehicle assignments API
  slug: open-shiftmove-vehicle-assignments-api
- collection_type: open
  name: Fleet API Specifications Custom fields Vehicle financing API
  slug: open-shiftmove-vehicle-financing-api
- collection_type: open
  name: Fleet API Specifications Custom fields Vehicle license plates API
  slug: open-shiftmove-vehicle-license-plates-api
- collection_type: open
  name: Fleet API Specifications Custom fields Vehicle usages API
  slug: open-shiftmove-vehicle-usages-api
- collection_type: open
  name: Fleet API Specifications Custom fields Vehicles API
  slug: open-shiftmove-vehicles-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.avrios.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.avrios.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.avrios.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.shiftmove.com/legal/agb
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shiftmove.com/legal/datenschutzerklarung
- group: operate
  title: ''
  type: Support
  url: https://www.shiftmove.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://www.avrios.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/shiftmove-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shiftmove-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shiftmove-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/shiftmove-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/shiftmove-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shiftmove-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/shiftmove-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/shiftmove-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/shiftmove-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/shiftmove-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.shiftmove.com/legal/legal-overview
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/shiftmove-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shiftmove-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/shiftmove-fleet-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shiftmove-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shiftmove-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Shiftmove GmbH is a Berlin-based European fleet management software company backed by Battery Ventures, operating the Vimcar, Fleet, Avrios, Optimum and Océan brands and managing 730,000+ vehicles for 25,000+ fleet customers. Its developer surface is the Avrios Fleet-API, a Swagger 2.0 REST API (base URL https://api.avrios.com) that syncs fleet data — vehicles, drivers, driver/vehicle assignments, license plates, vehicle financing, usages, invoices, organizations and custom fields — with the Avrios/Shiftmove platform. The API uses HTTP Basic authentication, is rate limited to 300 requests per minute, exposes 40 operations across ten resource groups, follows semantic versioning, and returns page-number paginated responses.
image: https://www.shiftmove.com/
layout: provider
modified: '2026-07-21'
name: Shiftmove
nav: Providers
network: true
overview: 'Shiftmove publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Custom fields API, Driver assignments API, Drivers API, and 7 more. Tagged areas include Company, Fleet Management, Mobility, Automotive, and Telematics.


  Shiftmove''s developer surface includes documentation, API reference, support, signup flow, authentication, changelog, and 18 more developer resources.'
random_paper: 15
rate_limits:
- limit_count: 1
  name: Shiftmove Rate Limits
  slug: shiftmove-rate-limits
score:
  band: developing
  composite: 44.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 4.5
    contract_quality: 47.0
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 44.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shiftmove/refs/heads/main/screenshots/shiftmove-2026-08-17T081831.png
security:
- kind: authentication
  name: Shiftmove Authentication
  slug: shiftmove-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Shiftmove Domain Security
  slug: shiftmove-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Shiftmove Trust Center
  slug: shiftmove-trust-center
  summary_line: GDPR, TÜV data-protection certification (Vimcar digital logbook)
slug: shiftmove
tags:
- Company
- Fleet Management
- Mobility
- Automotive
- Telematics
- Vehicles
- Fleet API
- Software-as-a-Service
website: https://developers.avrios.com/
---
