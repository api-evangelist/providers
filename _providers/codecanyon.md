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
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/codecanyon/well-known/codecanyon-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/codecanyon-www-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.envato.com/lp/vulnerability-disclosure/
- group: auth
  href: https://artifacts.apis.io/codecanyon/well-known/codecanyon-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/codecanyon-security.txt
- group: agent
  href: https://artifacts.apis.io/codecanyon/well-known/codecanyon-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/codecanyon-well-known.yml
- group: other
  href: https://artifacts.apis.io/codecanyon/hosts/codecanyon-hosts.yml
  title: ''
  type: Hosts
  url: hosts/codecanyon-hosts.yml
- group: other
  href: https://artifacts.apis.io/codecanyon/vendors/codecanyon-vendors.yml
  title: ''
  type: Vendors
  url: vendors/codecanyon-vendors.yml
- group: build
  href: https://artifacts.apis.io/codecanyon/packages/codecanyon-packages.yml
  title: ''
  type: Packages
  url: packages/codecanyon-packages.yml
- group: build
  title: ''
  type: SDKs
  url: https://codecanyon.net/category/html5/libraries
- group: commercial
  title: ''
  type: Pricing
  url: https://codecanyon.net/category/css/pricing-tables
- group: company
  title: ''
  type: Newsroom
  url: https://codecanyon.net/category/html5/media
- group: auth
  href: https://artifacts.apis.io/codecanyon/security/codecanyon-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/codecanyon-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/codecanyon/security/codecanyon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/codecanyon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://codecanyon.net/
coverage:
  checked: '2026-10-19'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found on api.codecanyon.net.
  evidence:
  - status: no-response
    url: https://api.codecanyon.net/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: Envato is a global marketplace for creative assets and digital tools, operating the CodeCanyon platform where developers can buy and sell plugins, scripts, and code snippets. The company offers a wide range of products across web development, mobile apps, and software utilities, supporting creators with a vibrant community, tutorials, and subscription services. Envato’s ecosystem includes multiple marketplaces such as ThemeForest, AudioJungle, and VideoHive, providing resources for designers, developers, and marketers worldwide.
image: https://assets.market-storefront.envato-static.com/storefront/assets/og-images/codecanyon-8a958e908fbb5bac5e54b32ca329c7d31b9e134bad20fb2ea1f1531701ca0561.png
layout: provider
modified: '2026-10-19'
name: Envato
nav: Providers
network: true
overview: 'Envato is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Marketplace, Digital Assets, Plugins, Code Marketplace, and Enviro.


  Envato''s developer surface includes pricing and 12 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.8
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 49.1
    operational_transparency: 5.3
  previous_composite: 9.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/codecanyon/codecanyon-2026-11-03T124720.png
security:
- kind: domain-security
  name: Codecanyon Domain Security
  slug: codecanyon-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Codecanyon Vulnerability Disclosure
  slug: codecanyon-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: codecanyon
tags:
- Marketplace
- Digital Assets
- Plugins
- Code Marketplace
- Enviro
website: https://codecanyon.net/
---
