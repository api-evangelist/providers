---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Business-to-business web services that let registered software vendors' products connect to Services Australia digital health and aged care channels (Medicare Online including ECLIPSE and DVA claiming
  name: Services Australia Health and Aged Care Web Services
  slug: services-australia-health-and-aged-care-web-services
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/services-australia/hosts/services-australia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/services-australia-hosts.yml
- group: other
  href: https://artifacts.apis.io/services-australia/vendors/services-australia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/services-australia-vendors.yml
- group: auth
  href: https://artifacts.apis.io/services-australia/security/services-australia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/services-australia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.servicesaustralia.gov.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://healthsoftware.humanservices.gov.au/claiming/ext-vnd/
- group: operate
  title: ''
  type: Support
  url: https://www.servicesaustralia.gov.au/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.servicesaustralia.gov.au/your-right-to-privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.servicesaustralia.gov.au/site-notices
- group: other
  title: ''
  type: Accessibility
  url: https://www.servicesaustralia.gov.au/accessibility
created: '2026-10-22'
description: Services Australia is the Australian Government agency (formerly the Department of Human Services) that delivers Centrelink, Medicare and Child Support payments and services. For software developers it runs the Health Systems Developer Portal (healthsoftware.humanservices.gov.au), launched in September 2020 as a secure gateway to licensed development material, technical documentation, forums and support for its health, aged care and Australian Immunisation Register web services, including online claiming, with NOI/NOC certification testing for vendor software.
image: https://avatars.githubusercontent.com/u/61787580?v=4
layout: provider
modified: '2026-10-22'
name: Services Australia
nav: Providers
network: true
overview: 'Services Australia is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Government, Australia, Healthcare, and Medicare.


  Services Australia''s developer surface includes support and 8 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 14.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/services-australia/services-australia-2026-11-03T143055.png
security:
- kind: domain-security
  name: Services Australia Domain Security
  slug: services-australia-domain-security
  summary_line: TLSv1.3 · DMARC
slug: services-australia
tags:
- Company
- Government
- Australia
- Healthcare
- Medicare
- Social Services
- Claiming
- Web Services
website: https://www.servicesaustralia.gov.au/
---
