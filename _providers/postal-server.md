---
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Postal provides an email delivery platform API documented at the official docs site.
  name: Postal API
  slug: postal-api
- description: 'Postal API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: Postal API
  slug: postal-server-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/postal-server/plans/postal-server-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/postal-server-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/postal-server/rules/postal-server-rules.yml
  title: ''
  type: Spectral
  url: rules/postal-server-rules.yml
- group: design
  href: https://artifacts.apis.io/postal-server/json-ld/postal-server-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/postal-server-context.jsonld
- group: design
  href: https://artifacts.apis.io/postal-server/vocabulary/postal-server-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/postal-server-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/postal-server/data-model/postal-server-data-model.yml
  title: ''
  type: DataModel
  url: data-model/postal-server-data-model.yml
- group: design
  href: https://artifacts.apis.io/postal-server/conformance/postal-server-conformance.yml
  title: ''
  type: Conformance
  url: conformance/postal-server-conformance.yml
- group: other
  href: https://artifacts.apis.io/postal-server/hosts/postal-server-hosts.yml
  title: ''
  type: Hosts
  url: hosts/postal-server-hosts.yml
- group: other
  href: https://artifacts.apis.io/postal-server/vendors/postal-server-vendors.yml
  title: ''
  type: Vendors
  url: vendors/postal-server-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E&source=header-repo&source_repo=postalserver%2Finstall
- group: auth
  title: ''
  type: Security
  url: https://github.com/postalserver/install/security
- group: commercial
  title: ''
  type: Pricing
  url: https://github.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/why-github
- group: auth
  href: https://artifacts.apis.io/postal-server/security/postal-server-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/postal-server-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://postalserver.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.postalserver.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.postalserver.io/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://discord.postalserver.io
- group: operate
  title: ''
  type: Contact
  url: mailto:team@postalserver.io
coverage:
  checked: '2026-10-27'
  detail: Documentation site renders content via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.postalserver.io/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Postal provides a suite of installation tools and documentation for setting up and running the Postal email delivery platform. The repository includes scripts for quick deployment, detailed prerequisites, and guides covering getting started, configuration, and operation. It aims to simplify the installation process for developers and system administrators, offering both v2 and v3 installation scripts and links to comprehensive online documentation.
image: https://opengraph.githubassets.com/76ef6940d715337154b85d755ee6d732954c120d6e6906e6f2a714915b5c4d4b/postalserver/install
json_schemas:
- name: GetApiV1MessagesMessageResponse
  property_count: 2
  slug: postal-server-get-api-v1-messages-message-response
jsonld:
- class_count: 1
  name: Postal Server Context
  property_count: 2
  slug: postal-server-context
layout: provider
modified: '2026-10-27'
name: Postal
nav: Providers
network: true
overview: 'Postal is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Installation, Open Source, DevOps, Docker, and Tools.


  The Postal catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Postal''s developer surface includes signup flow, pricing, documentation, getting-started guide, support, and 13 more developer resources.'
plans:
- name: Postal Server Plans Pricing
  plan_count: 3
  slug: postal-server-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Postal API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: postal-server-rules
score:
  band: thin
  composite: 30.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 60.2
    catalog_earned_first_party: 12.0
    catalog_gap: 54.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 17.6
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Postal Server Domain Security
  slug: postal-server-domain-security
  summary_line: TLSv1.3 · HSTS
slug: postal-server
tags:
- Installation
- Open Source
- DevOps
- Docker
- Tools
website: https://postalserver.io/
---
