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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API documentation for BMLT.app is provided via a WordPress site but no machine‑readable OpenAPI/GraphQL contract is publicly available.
  name: BMLT API
  slug: bmlt-api
- description: 'BMLT.app API as documented publicly: 35 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: BMLT.app API
  slug: bmlt-app-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/bmlt-app/rules/bmlt-app-rules.yml
  title: ''
  type: Spectral
  url: rules/bmlt-app-rules.yml
- group: design
  href: https://artifacts.apis.io/bmlt-app/vocabulary/bmlt-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bmlt-app-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/bmlt-app/authentication/bmlt-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bmlt-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/bmlt-app/conformance/bmlt-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bmlt-app-conformance.yml
- group: other
  href: https://artifacts.apis.io/bmlt-app/hosts/bmlt-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bmlt-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/bmlt-app/vendors/bmlt-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bmlt-app-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://bmlt.app/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bmlt.app/privacy/
- group: company
  title: ''
  type: Blog
  url: https://bmlt.app/blog/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.bmlt.app/
- group: auth
  href: https://artifacts.apis.io/bmlt-app/security/bmlt-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bmlt-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bmlt.app/
- group: start
  title: ''
  type: GettingStarted
  url: https://bmlt.app/setting-up-the-bmlt/
coverage:
  checked: '2026-11-02'
  detail: The provider's website is a WordPress site with no publicly accessible OpenAPI, Swagger, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 404
    url: https://bmlt.app/openapi.json
  - status: 404
    url: https://bmlt.app/swagger.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: BMLT.app provides a full‑stack, open‑source solution for managing Narcotics Anonymous meetings. It offers a BMLT Server backend that synchronizes meeting lists instantly to front‑end applications such as Crouton, Bread, and Yap. Since its first alpha release in May 2009, BMLT has grown to host over half of the world’s known NA meetings, supporting dozens of servers, zones, regions, areas, groups, and tens of thousands of meetings. The platform enables service bodies to keep meeting information up‑to‑date across multiple apps, fostering community coordination and accessibility.
layout: provider
modified: '2026-11-02'
name: BMLT.app
nav: Providers
network: true
overview: 'BMLT.app is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Open Source, Narcotics Anonymous, Meeting Management, Community, and BMLT.


  The BMLT.app catalog on APIs.io includes 1 Spectral governance ruleset.


  BMLT.app''s developer surface includes authentication, support, engineering blog, API reference, getting-started guide, and 8 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 73
  extends:
  - spectral:oas
  name: BMLT.app API Rules
  rule_count: 32
  severity_counts:
    error: 30
    hint: 0
    info: 1
    warn: 1
  slug: bmlt-app-rules
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 10.5
    developer_ergonomics: 25.0
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bmlt App Authentication
  slug: bmlt-app-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bmlt App Domain Security
  slug: bmlt-app-domain-security
  summary_line: TLSv1.3
slug: bmlt-app
tags:
- Open Source
- Narcotics Anonymous
- Meeting Management
- Community
- BMLT
website: https://bmlt.app/
---
