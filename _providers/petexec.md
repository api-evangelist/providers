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
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Petexec Agentic Access
  operation_count: 51
  slug: petexec-agentic-access
  summary_line: 51 operations · 8 acting
api_count: 1
apis:
- baseURL: https://secure.petexec.net/api
  baseurl_source: declared
  description: OAuth2 password-grant token issuance.
  name: PetExec Authentication API
  slug: petexec-authentication-api
- baseURL: https://secure.petexec.net/api
  baseurl_source: declared
  description: Boarding reservations, packages, and services.
  name: PetExec Boarding API
  slug: petexec-boarding-api
- baseURL: https://secure.petexec.net/api
  baseurl_source: declared
  description: Company-wide and per-owner reservation calendars by date range.
  name: PetExec Calendar API
  slug: petexec-calendar-api
- baseURL: https://secure.petexec.net/api
  baseurl_source: declared
  description: Company locations, employees, lead sources, and preferences.
  name: PetExec Company API
  slug: petexec-company-api
- baseURL: https://secure.petexec.net/api
  baseurl_source: declared
  description: Owner stored payment cards.
  name: PetExec Credit Cards API
  slug: petexec-credit-cards-api
- baseURL: https://secure.petexec.net/api
  baseurl_source: declared
  description: Daycare reservations and services.
  name: PetExec Daycare API
  slug: petexec-daycare-api
- baseURL: https://secure.petexec.net/api
  baseurl_source: declared
  description: Grooming reservations, groomers, and services.
  name: PetExec Grooming API
  slug: petexec-grooming-api
- baseURL: https://secure.petexec.net/api
  baseurl_source: declared
  description: Owner (pet parent) account records and search.
  name: PetExec Owners API
  slug: petexec-owners-api
- baseURL: https://secure.petexec.net/api
  baseurl_source: declared
  description: Pet profiles, pet types, breeds, and vets.
  name: PetExec Pets API
  slug: petexec-pets-api
- baseURL: https://secure.petexec.net/api
  baseurl_source: declared
  description: The authenticated user's own profile and portal menu.
  name: PetExec Profile API
  slug: petexec-profile-api
- baseURL: https://secure.petexec.net/api
  baseurl_source: declared
  description: Owner purchase/transaction history.
  name: PetExec Purchase History API
  slug: petexec-purchase-history-api
- baseURL: https://secure.petexec.net/api
  baseurl_source: declared
  description: Billing and statistics reports.
  name: PetExec Reports API
  slug: petexec-reports-api
- baseURL: https://secure.petexec.net/api
  baseurl_source: declared
  description: Scheduled-service reservations, types, and services.
  name: PetExec Scheduled Services API
  slug: petexec-scheduled-services-api
- baseURL: https://secure.petexec.net/api
  baseurl_source: declared
  description: Pet vaccination (shot) records.
  name: PetExec Vaccinations API
  slug: petexec-vaccinations-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PetExec Authentication API
  slug: open-petexec-authentication-api
- collection_type: open
  name: PetExec Authentication Boarding API
  slug: open-petexec-boarding-api
- collection_type: open
  name: PetExec Authentication Calendar API
  slug: open-petexec-calendar-api
- collection_type: open
  name: PetExec Authentication Company API
  slug: open-petexec-company-api
- collection_type: open
  name: PetExec Authentication Credit Cards API
  slug: open-petexec-credit-cards-api
- collection_type: open
  name: PetExec Authentication Daycare API
  slug: open-petexec-daycare-api
- collection_type: open
  name: PetExec Authentication Grooming API
  slug: open-petexec-grooming-api
- collection_type: open
  name: PetExec Authentication Owners API
  slug: open-petexec-owners-api
- collection_type: open
  name: PetExec Authentication Pets API
  slug: open-petexec-pets-api
- collection_type: open
  name: PetExec Authentication Profile API
  slug: open-petexec-profile-api
- collection_type: open
  name: PetExec Authentication Purchase History API
  slug: open-petexec-purchase-history-api
- collection_type: open
  name: PetExec Authentication Reports API
  slug: open-petexec-reports-api
- collection_type: open
  name: PetExec Authentication Scheduled Services API
  slug: open-petexec-scheduled-services-api
- collection_type: open
  name: PetExec Authentication Vaccinations API
  slug: open-petexec-vaccinations-api
- collection_type: open
  name: PetExec API
  slug: open-petexec
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/petexec-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/petexec-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/petexec-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/petexec-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PetExec
- group: company
  title: ''
  type: Website
  url: https://www.petexec.net/
- group: docs
  title: ''
  type: Documentation
  url: https://docs2.petexec.net/
- group: commercial
  title: ''
  type: Plans
  url: plans/petexec-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/petexec-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/petexec-finops.yml
created: '2026-07-04'
description: PetExec is cloud-based business management software for dog daycares, boarding facilities, groomers, and trainers - scheduling, an owner portal, payments, and reporting. PetExec publishes a real, documented OAuth2 (password grant) REST API for existing customers and their developers, with a public GitHub examples repository covering owners, pets, boarding, daycare, grooming, scheduled services, vaccinations, billing, and reports. Access requires an active PetExec account - client credentials are self-issued from Company Preferences > Misc. Settings > Maintain API Applications, then exchanged for a Bearer token via a scoped password grant. PetExec was acquired by Togetherwork in November 2024 and joined the Gingr / Revelation Pets pet-care product group; PetExec is no longer accepting new customers and is being migrated toward Gingr, but the documented API remains live for existing PetExec accounts as of this review.
finops:
- name: Petexec Finops
  service_category: Vertical SaaS - Pet Care Business Management
  slug: petexec-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/petexec.png
layout: provider
modified: '2026-07-04'
name: PetExec
nav: Providers
network: true
overview: 'PetExec publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Boarding API, Calendar API, and 11 more. Tagged areas include Pet Care, Boarding, Daycare, Grooming, and Training.


  PetExec''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Petexec Plans Pricing
  plan_count: 3
  slug: petexec-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Petexec Rate Limits
  slug: petexec-rate-limits
score:
  band: thin
  composite: 38.2
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 53.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/petexec/refs/heads/main/screenshots/petexec-2026-09-02T151113.png
security:
- kind: authentication
  name: Petexec Authentication
  slug: petexec-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Petexec Domain Security
  slug: petexec-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: petexec
tags:
- Pet Care
- Boarding
- Daycare
- Grooming
- Training
- Business Management
- Pet Business Software
website: https://www.petexec.net/
---
