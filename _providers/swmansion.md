---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.9
  scored_at: '2026-10-31'
api_count: 1
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/swmansion/rules/swmansion-rules.yml
  title: ''
  type: Spectral
  url: rules/swmansion-rules.yml
- group: design
  href: https://artifacts.apis.io/swmansion/json-ld/swmansion-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/swmansion-context.jsonld
- group: design
  href: https://artifacts.apis.io/swmansion/vocabulary/swmansion-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/swmansion-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/swmansion/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/swmansion/data-model/swmansion-data-model.yml
  title: ''
  type: DataModel
  url: data-model/swmansion-data-model.yml
- group: design
  href: https://artifacts.apis.io/swmansion/errors/swmansion-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/swmansion-problem-types.yml
- group: design
  href: https://artifacts.apis.io/swmansion/conformance/swmansion-conformance.yml
  title: ''
  type: Conformance
  url: conformance/swmansion-conformance.yml
- group: agent
  href: https://artifacts.apis.io/swmansion/llms/swmansion-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/swmansion-llms.txt
- group: agent
  href: https://artifacts.apis.io/swmansion/well-known/swmansion-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/swmansion-well-known.yml
- group: other
  href: https://artifacts.apis.io/swmansion/hosts/swmansion-hosts.yml
  title: ''
  type: Hosts
  url: hosts/swmansion-hosts.yml
- group: other
  href: https://artifacts.apis.io/swmansion/vendors/swmansion-vendors.yml
  title: ''
  type: Vendors
  url: vendors/swmansion-vendors.yml
- group: build
  href: https://artifacts.apis.io/swmansion/packages/swmansion-packages.yml
  title: ''
  type: SDKs
  url: packages/swmansion-packages.yml
- group: build
  href: https://artifacts.apis.io/swmansion/packages/swmansion-packages.yml
  title: ''
  type: Packages
  url: packages/swmansion-packages.yml
- group: auth
  href: https://artifacts.apis.io/swmansion/security/swmansion-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/swmansion-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://swmansion.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://swmansion.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.swmansion.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.swmansion.com/
- group: operate
  title: ''
  type: Support
  url: https://swmansion.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://swmansion.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/software-mansion
- group: operate
  title: ''
  type: Roadmap
  url: https://ir.swmansion.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://swmansion.com/privacy/policy/
coverage:
  checked: '2026-10-19'
  detail: Documentation at https://docs.swmansion.com is HTML only with no OpenAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://docs.swmansion.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: Software Mansion is a custom software development and consultancy firm specializing in mobile apps, React Native, Elixir, low‑latency streaming, full‑stack web applications, and on‑device AI computing. They are a founding member of the React Foundation and have award‑winning products such as Partiful. Their services include product development, consulting, and open‑source contributions to the React Native ecosystem.
image: https://strapi-production-5f3f.up.railway.app/uploads/OG_Image_600c318430.jpg
jsonld:
- class_count: 2
  name: Swmansion Context
  property_count: 8
  slug: swmansion-context
layout: provider
modified: '2026-10-19'
name: Software Mansion
nav: Providers
network: true
overview: 'Software Mansion publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software Development, Mobile App, React Native, and Elixir.


  The Software Mansion catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Software Mansion''s developer surface includes documentation, API reference, support, engineering blog, and 19 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Software Mansion API Rules
  rule_count: 17
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 2
  slug: swmansion-rules
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 12.7
    developer_ergonomics: 42.3
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Swmansion Domain Security
  slug: swmansion-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 4
skills:
- name: swmansion-create-configure-list-resources
  slug: swmansion-create-configure-list-resources
- name: swmansion-get-document-with-chunks
  slug: swmansion-get-document-with-chunks
- name: swmansion-get-profile-and-buckets
  slug: swmansion-get-profile-and-buckets
- name: swmansion-ingest-documents
  slug: swmansion-ingest-documents
slug: swmansion
tags:
- Company
- Software Development
- Mobile App
- React Native
- Elixir
website: https://swmansion.com/
---
