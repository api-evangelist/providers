---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
  score: 3.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/numeratica-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/numeratica-com/changelog/numeratica-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/numeratica-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/numeratica-com/authentication/numeratica-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/numeratica-com-authentication.yml
- group: other
  href: https://artifacts.apis.io/numeratica-com/hosts/numeratica-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/numeratica-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/numeratica-com/vendors/numeratica-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/numeratica-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/numeratica-com/packages/numeratica-com-packages.yml
  title: ''
  type: SDKs
  url: packages/numeratica-com-packages.yml
- group: build
  href: https://artifacts.apis.io/numeratica-com/packages/numeratica-com-packages.yml
  title: ''
  type: Packages
  url: packages/numeratica-com-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.numeratica.com/changelog
- group: auth
  href: https://artifacts.apis.io/numeratica-com/security/numeratica-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/numeratica-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://numeratica.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.numeratica.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.numeratica.com/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://docs.numeratica.com/reference.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.numeratica.com/get-key.html
coverage:
  checked: '2026-10-31'
  detail: OpenAPI spec at https://api.numeratica.com/v1/openapi.json requires an API key (401 Unauthorized).
  evidence:
  - status: 401
    url: https://api.numeratica.com/v1/openapi.json
  reason: auth-required
  state: gated
created: '2026-10-30'
description: Numeratica provides a developer-first API suite for U.S. household finance calculations, offering 76 calculators covering retirement, tax, Social Security, equity compensation, insurance, education funding, mortgages, benefits, debt, and portfolio mechanics. It includes a batch endpoint for up to 20 calculations per call, ensuring deterministic and reproducible results. The platform emphasizes security with API key authentication and public health probes, and offers extensive documentation, quickstart guides, and a changelog for developers.
image: https://docs.numeratica.com/assets/og.png
layout: provider
modified: '2026-10-30'
name: numeratica-com
nav: Providers
network: true
overview: 'numeratica-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Calculators, Retirement, and Household.


  numeratica-com''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, and 9 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 39.9
    discoverability: 39.3
    operational_transparency: 7.9
  previous_composite: 18.2
  provenance:
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/numeratica-com/numeratica-com-2026-11-03T140348.png
security:
- kind: authentication
  name: Numeratica Com Authentication
  slug: numeratica-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Numeratica Com Domain Security
  slug: numeratica-com-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: numeratica-com
tags:
- Finance
- Calculators
- Retirement
- Household
website: https://numeratica.com/
---
