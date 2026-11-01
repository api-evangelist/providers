---
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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/promptmage/hosts/promptmage-hosts.yml
  title: ''
  type: Hosts
  url: hosts/promptmage-hosts.yml
- group: other
  href: https://artifacts.apis.io/promptmage/vendors/promptmage-vendors.yml
  title: ''
  type: Vendors
  url: vendors/promptmage-vendors.yml
- group: build
  href: https://artifacts.apis.io/promptmage/packages/promptmage-packages.yml
  title: ''
  type: SDKs
  url: packages/promptmage-packages.yml
- group: build
  href: https://artifacts.apis.io/promptmage/packages/promptmage-packages.yml
  title: ''
  type: Packages
  url: packages/promptmage-packages.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://promptmage.io/roadmap
- group: docs
  title: ''
  type: APIReference
  url: https://promptmage.io/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://promptmage.io/getting-started/
- group: auth
  href: https://artifacts.apis.io/promptmage/security/promptmage-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/promptmage-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://promptmage.io/
coverage:
  checked: '2026-10-21'
  detail: The domain promptmage.com is parked on GoDaddy and returns an Access Denied page, indicating no active service or API.
  evidence:
  - status: 307
    url: https://promptmage.com/lander
  reason: defunct
  state: none
created: '2026-10-21'
description: Promptmage provides AI‑powered prompt generation and management tools for creators, developers, and enterprises. Their platform offers a library of curated prompts, a prompt marketplace, and APIs to integrate dynamic prompt creation into applications, enabling users to harness generative AI more effectively across content creation, marketing, and software development workflows.
layout: provider
modified: '2026-10-21'
name: Promptmage
nav: Providers
network: true
overview: 'Promptmage is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Prompt Engineering, SaaS, Developer Tools, and Content Creation.


  Promptmage''s developer surface includes API reference, getting-started guide, and 7 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 44.6
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Promptmage Domain Security
  slug: promptmage-domain-security
  summary_line: TLSv1.3
slug: promptmage
tags:
- AI
- Prompt Engineering
- SaaS
- Developer Tools
- Content Creation
website: https://promptmage.io/
---
