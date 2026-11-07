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
api_count: 0
artifact_total: 1
common:
- group: design
  href: https://artifacts.apis.io/cayaba-care/conformance/cayaba-care-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cayaba-care-conformance.yml
- group: other
  href: https://artifacts.apis.io/cayaba-care/hosts/cayaba-care-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cayaba-care-hosts.yml
- group: other
  href: https://artifacts.apis.io/cayaba-care/vendors/cayaba-care-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cayaba-care-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nadiacare.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://support.nadiacare.com/
- group: auth
  title: ''
  type: Security
  url: https://www.nadiacare.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nadiacare.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.nadiacare.com/news
- group: other
  title: ''
  type: Leadership
  url: https://www.nadiacare.com/leadership
- group: start
  title: ''
  type: GettingStarted
  url: https://www.nadiacare.com/get-started
- group: auth
  href: https://artifacts.apis.io/cayaba-care/security/cayaba-care-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cayaba-care-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nadiacare.com/
coverage:
  checked: '2026-10-07'
  detail: The provider's website offers documentation pages but no discoverable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts.
  evidence:
  - status: 200
    url: https://www.nadiacare.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Cayaba Care provides a community‑based maternity care platform offering comprehensive support throughout pregnancy and postpartum, including coaching, nutrition, mental health, and care coordination. The service aims to improve maternal health outcomes for underserved women in the United States.
image: http://static1.squarespace.com/static/699cc2c8fc33af1c1809dc3f/t/69a036de82649f41a50c8aa6/1782321898902/nadia-care-logo-full-heart-full-color-rgb-900px-w-72ppi.png?format=1500w
layout: provider
modified: '2026-10-07'
name: Cayaba Care
nav: Providers
network: true
overview: 'Cayaba Care is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Maternity, Health Tech, Community, postpartum, and Pregnancy.


  Cayaba Care''s developer surface includes support, getting-started guide, and 10 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 50.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 16.7
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 11.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cayaba-care/cayaba-care-2026-11-03T123534.png
security:
- kind: domain-security
  name: Cayaba Care Domain Security
  slug: cayaba-care-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cayaba-care
tags:
- Maternity
- Health Tech
- Community
- postpartum
- Pregnancy
- USA
website: https://www.nadiacare.com/
---
