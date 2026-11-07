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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides water data management software APIs as documented on the Aquatic Informatics resources page.
  name: Aquatic Informatics API
  slug: aquatic-informatics-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/aquaticinformatics/llms/aquaticinformatics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aquaticinformatics-llms.txt
- group: other
  href: https://artifacts.apis.io/aquaticinformatics/hosts/aquaticinformatics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aquaticinformatics-hosts.yml
- group: build
  href: https://artifacts.apis.io/aquaticinformatics/packages/aquaticinformatics-packages.yml
  title: ''
  type: SDKs
  url: packages/aquaticinformatics-packages.yml
- group: build
  href: https://artifacts.apis.io/aquaticinformatics/packages/aquaticinformatics-packages.yml
  title: ''
  type: Packages
  url: packages/aquaticinformatics-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AquaticInformatics
- group: auth
  href: https://artifacts.apis.io/aquaticinformatics/security/aquaticinformatics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aquaticinformatics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aquaticinformatics.com
- group: docs
  title: ''
  type: Documentation
  url: https://aquaticinformatics.com/resources/
- group: company
  title: ''
  type: Blog
  url: https://aquaticinformatics.com/water-software-blog/
- group: operate
  title: ''
  type: Support
  url: https://aquaticinformatics.com/water-software-support/
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI or other machine-readable contract found; attempts at /openapi.json and /swagger.json returned 302 redirects to a 404 page.
  evidence:
  - status: 302
    url: https://aquaticinformatics.com/openapi.json
  - status: 302
    url: https://aquaticinformatics.com/swagger.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Aquatic Informatics provides water data management software and services, helping agencies, utilities, and organizations collect, analyze, and share water quality and environmental data. Their solutions include Aquarius, WaterTrax, and compliance platforms for wastewater, drinking water, and stormwater management.
image: https://aquaticinformatics.com/wp-content/uploads/2026/09/aqi-home-feat-img.webp
layout: provider
modified: '2026-11-01'
name: Aquatic Informatics
nav: Providers
network: true
overview: 'Aquatic Informatics is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Water, Data Management, Environmental, and Software.


  Aquatic Informatics'' developer surface includes documentation, engineering blog, support, and 7 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 57.1
    operational_transparency: 2.6
  previous_composite: 9.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aquaticinformatics Domain Security
  slug: aquaticinformatics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aquaticinformatics
tags:
- Company
- Water
- Data Management
- Environmental
- Software
website: https://aquaticinformatics.com
---
