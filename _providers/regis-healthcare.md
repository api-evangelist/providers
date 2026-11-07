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
- group: other
  href: https://artifacts.apis.io/regis-healthcare/hosts/regis-healthcare-hosts.yml
  title: ''
  type: Hosts
  url: hosts/regis-healthcare-hosts.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.regis.com.au/home-care/getting-started/
- group: company
  title: ''
  type: Website
  url: https://www.regis.com.au/
- group: auth
  href: https://artifacts.apis.io/regis-healthcare/security/regis-healthcare-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/regis-healthcare-domain-security.yml
- group: company
  title: ''
  type: AboutUs
  url: https://www.regis.com.au/about-regis/
- group: operate
  title: ''
  type: Support
  url: https://www.regis.com.au/contact-us/
- group: company
  title: ''
  type: Newsroom
  url: https://www.regis.com.au/newsroom/
- group: other
  title: ''
  type: Leadership
  url: https://www.regis.com.au/leadership/
- group: company
  title: ''
  type: Investors
  url: https://www.regis.com.au/investor-information/
- group: company
  title: ''
  type: Careers
  url: https://www.regis.com.au/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/company/regis-agedcare
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.regis.com.au/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.regis.com.au/privacy-policy/
coverage:
  checked: '2026-10-22'
  detail: Regis Healthcare is an Australian aged care operator; regis.com.au (WordPress site) serves no developer portal or contract, with /openapi.json, /swagger.json, /api-docs and /developers/ all returning 404, and pre-flight contract discovery found no OpenAPI, AsyncAPI, GraphQL or MCP surface on its hosts.
  evidence:
  - status: 200
    url: https://www.regis.com.au/
  - status: 404
    url: https://www.regis.com.au/openapi.json
  - status: 404
    url: https://www.regis.com.au/developers/
  reason: not-a-software-company
  state: none
created: '2026-10-22'
description: 'Regis Healthcare Limited (ASX: REG), trading as Regis Aged Care, is one of the largest aged care operators in Australia. Founded over 30 years ago and headquartered in Camberwell, Victoria, Regis provides services to more than 10,000 older Australians through residential aged care homes, home care service hubs, day therapy and respite centres, and retirement villages, with a team of over 13,000 employees. No public developer portal, API documentation or API reference was found on its website (regis.com.au); this profile records its corporate identity.'
image: https://www.regis.com.au/site/wp-content/themes/regis_2018/assets/img/regis-logo.png
layout: provider
modified: '2026-10-22'
name: Regis Healthcare
nav: Providers
network: true
overview: 'Regis Healthcare is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Aged Care, Home Care, and Retirement Living.


  Regis Healthcare''s developer surface includes getting-started guide, support, and 11 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 50.0
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
  previous_composite: 12.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/regis-healthcare/regis-healthcare-2026-11-03T142125.png
security:
- kind: domain-security
  name: Regis Healthcare Domain Security
  slug: regis-healthcare-domain-security
  summary_line: TLSv1.3 · DMARC
slug: regis-healthcare
tags:
- Company
- Healthcare
- Aged Care
- Home Care
- Retirement Living
- Australia
- ASX Listed
website: https://www.regis.com.au/
---
