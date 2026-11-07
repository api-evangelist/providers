---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: operate
  href: https://artifacts.apis.io/office-for-national-statistics/rate-limits/office-for-national-statistics-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/office-for-national-statistics-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/office-for-national-statistics/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://www.ons.gov.uk/help/report-vulnerability
- group: auth
  href: https://artifacts.apis.io/office-for-national-statistics/well-known/office-for-national-statistics-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/office-for-national-statistics-security.txt
- group: auth
  href: https://artifacts.apis.io/office-for-national-statistics/well-known/office-for-national-statistics-cy-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/office-for-national-statistics-cy-security.txt
- group: auth
  href: https://artifacts.apis.io/office-for-national-statistics/well-known/office-for-national-statistics-beta-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/office-for-national-statistics-beta-security.txt
- group: auth
  href: https://artifacts.apis.io/office-for-national-statistics/well-known/office-for-national-statistics-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/office-for-national-statistics-api-security.txt
- group: agent
  href: https://artifacts.apis.io/office-for-national-statistics/well-known/office-for-national-statistics-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/office-for-national-statistics-well-known.yml
- group: other
  href: https://artifacts.apis.io/office-for-national-statistics/hosts/office-for-national-statistics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/office-for-national-statistics-hosts.yml
- group: other
  href: https://artifacts.apis.io/office-for-national-statistics/vendors/office-for-national-statistics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/office-for-national-statistics-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.ons.gov.uk/news
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.ons.gov.uk/tour/getting-started/
- group: auth
  href: https://artifacts.apis.io/office-for-national-statistics/security/office-for-national-statistics-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/office-for-national-statistics-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/office-for-national-statistics/security/office-for-national-statistics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/office-for-national-statistics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ons.gov.uk
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ons.gov.uk
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ons.gov.uk
- group: docs
  title: ''
  type: APIReference
  url: https://developer.ons.gov.uk
- group: company
  title: ''
  type: Blog
  url: https://blog.ons.gov.uk
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ONSdigital
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ons.gov.uk/help/termsandconditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ons.gov.uk/help/privacynotice
- group: operate
  title: ''
  type: Support
  url: https://www.ons.gov.uk/aboutus/contactus
coverage:
  checked: '2026-10-13'
  detail: Developer portal provides documentation but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL specifications were found.
  evidence:
  - status: 200
    url: https://developer.ons.gov.uk/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: The Office for National Statistics (ONS) is the UK’s largest independent producer of official statistics. It provides a wide range of economic, population and social data through its website and APIs, supporting research, policy making and public insight. ONS publishes datasets on GDP, inflation, employment, demographics, and more, and offers developer resources for programmatic access to its statistical services.
layout: provider
modified: '2026-10-13'
name: Office for National Statistics
nav: Providers
network: true
overview: 'Office for National Statistics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Government, Statistics, Data, United Kingdom, and Public Sector.


  Office for National Statistics'' developer surface includes getting-started guide, documentation, API reference, engineering blog, support, and 18 more developer resources.'
random_paper: 11
rate_limits:
- limit_count: 3
  name: Office For National Statistics Rate Limits
  slug: office-for-national-statistics-rate-limits
score:
  band: emerging
  composite: 17.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 29.0
    discoverability: 45.5
    operational_transparency: 39.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 26.3
  provenance:
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/office-for-national-statistics/office-for-national-statistics-2026-11-03T140449.png
security:
- kind: domain-security
  name: Office For National Statistics Domain Security
  slug: office-for-national-statistics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Office For National Statistics Vulnerability Disclosure
  slug: office-for-national-statistics-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: office-for-national-statistics
tags:
- Government
- Statistics
- Data
- United Kingdom
- Public Sector
website: https://www.ons.gov.uk
---
