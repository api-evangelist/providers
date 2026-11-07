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
  band: agent-aware
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: The provider documents an API for capabilities.txt via the guide at https://www.capabilitiestxt.org/guides/agent-ready-api.
  name: Capabilities.txt API
  slug: capabilities-txt-api
- description: 'Project Auxo, Inc. API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Project Auxo, Inc. API
  slug: capabilitiestxt-org-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/capabilitiestxt-org/rules/capabilitiestxt-org-rules.yml
  title: ''
  type: Spectral
  url: rules/capabilitiestxt-org-rules.yml
- group: design
  href: https://artifacts.apis.io/capabilitiestxt-org/json-ld/capabilitiestxt-org-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/capabilitiestxt-org-context.jsonld
- group: design
  href: https://artifacts.apis.io/capabilitiestxt-org/vocabulary/capabilitiestxt-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/capabilitiestxt-org-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/capabilitiestxt-org/data-model/capabilitiestxt-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/capabilitiestxt-org-data-model.yml
- group: auth
  href: https://artifacts.apis.io/capabilitiestxt-org/security/capabilitiestxt-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/capabilitiestxt-org-domain-security.yml
- group: design
  href: https://artifacts.apis.io/capabilitiestxt-org/conformance/capabilitiestxt-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/capabilitiestxt-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/capabilitiestxt-org/llms/capabilitiestxt-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/capabilitiestxt-org-llms.txt
- group: agent
  href: https://artifacts.apis.io/capabilitiestxt-org/well-known/capabilitiestxt-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/capabilitiestxt-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/capabilitiestxt-org/hosts/capabilitiestxt-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/capabilitiestxt-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/capabilitiestxt-org/vendors/capabilitiestxt-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/capabilitiestxt-org-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://capabilitiestxt.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.capabilitiestxt.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/capabilityhostprotocol
coverage:
  checked: '2026-11-04'
  detail: Provider docs are rendered via JavaScript, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://www.capabilitiestxt.org/guides/agent-ready-api
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: Project Auxo, Inc. operates the capabilities.txt initiative, an open convention allowing websites to publish a simple, human‑readable file that declares the actions they can perform. This enables agents to discover and invoke site capabilities such as support ticket creation, inventory checks, and other services via a well‑known location, fostering interoperable, agent‑centric web interactions.
image: https://capabilitiestxt.org/og.png
json_schemas:
- name: PostApiCheckRequest
  property_count: 1
  slug: capabilitiestxt-org-post-api-check-request
jsonld:
- class_count: 1
  name: Capabilitiestxt Org Context
  property_count: 1
  slug: capabilitiestxt-org-context
layout: provider
modified: '2026-11-04'
name: Project Auxo, Inc.
nav: Providers
network: true
overview: 'Project Auxo, Inc. is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include capabilities.txt, open convention, Agentic Web, Discovery, and Project Auxo.


  The Project Auxo, Inc. catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Project Auxo, Inc.''s developer surface includes documentation and 12 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 73
  extends:
  - spectral:oas
  name: Project Auxo, Inc. API Rules
  rule_count: 32
  severity_counts:
    error: 30
    hint: 0
    info: 1
    warn: 1
  slug: capabilitiestxt-org-rules
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 16.4
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 2.6
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
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Capabilitiestxt Org Domain Security
  slug: capabilitiestxt-org-domain-security
  summary_line: TLSv1.3 · HSTS
slug: capabilitiestxt-org
tags:
- capabilities.txt
- open convention
- Agentic Web
- Discovery
- Project Auxo
website: https://capabilitiestxt.org/
---
