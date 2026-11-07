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
  href: https://artifacts.apis.io/danfoss/hosts/danfoss-hosts.yml
  title: ''
  type: Hosts
  url: hosts/danfoss-hosts.yml
- group: build
  href: https://artifacts.apis.io/danfoss/packages/danfoss-packages.yml
  title: ''
  type: SDKs
  url: packages/danfoss-packages.yml
- group: build
  href: https://artifacts.apis.io/danfoss/packages/danfoss-packages.yml
  title: ''
  type: Packages
  url: packages/danfoss-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.danfoss.com/en/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://terms.danfoss.com/PrivacyPolicy?culture=en
- group: company
  title: ''
  type: Newsroom
  url: https://www.danfoss.com/en/about-danfoss/news/?page=1&segments=4552%2C4553%2C4554%2C18208&sort=startDate_desc
- group: start
  title: ''
  type: Login
  url: https://www.danfoss.com/dip/login
- group: other
  title: ''
  type: Leadership
  url: https://www.danfoss.com/en/about-danfoss/company/management/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.danfoss.com/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://developer.danfoss.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Danfoss
- group: auth
  href: https://artifacts.apis.io/danfoss/security/danfoss-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/danfoss-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.danfoss.com
coverage:
  checked: '2026-11-04'
  detail: Developer portal provides HTML docs but no machine‑readable OpenAPI/GraphQL/AsyncAPI spec was found.
  evidence:
  - status: 200
    url: https://developer.danfoss.com/catalog
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Danfoss is a global family‑owned engineering company that creates innovative solutions to increase machine productivity, reduce emissions, lower energy consumption and enable electrification. The company serves a wide range of industries including automotive, building‑commercial, marine, and energy, offering products such as drives, climate solutions, and power solutions. Danfoss is committed to sustainability and long‑term value for stakeholders, as described on its corporate website.
image: https://www.danfoss.com/media/nfmchvnm/purpose-image-1120x747.jpg
layout: provider
modified: '2026-11-04'
name: Danfoss
nav: Providers
network: true
overview: 'Danfoss is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Engineering, Sustainability, Industrial, and Automation.


  Danfoss'' developer surface includes getting-started guide, documentation, and 11 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 18.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 51.8
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Danfoss Domain Security
  slug: danfoss-domain-security
  summary_line: TLSv1.3 · DMARC
slug: danfoss
tags:
- Company
- Engineering
- Sustainability
- Industrial
- Automation
website: https://www.danfoss.com
---
