---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: aria2 is a lightweight, multi-protocol command-line download utility supporting HTTP/HTTPS, FTP, SFTP, BitTorrent and Metalink.
  name: aria2
  slug: aria2
- description: 'aria2 API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: aria2 API
  slug: aria2-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/aria2/plans/aria2-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aria2-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aria2/rules/aria2-rules.yml
  title: ''
  type: Spectral
  url: rules/aria2-rules.yml
- group: design
  href: https://artifacts.apis.io/aria2/json-ld/aria2-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aria2-context.jsonld
- group: design
  href: https://artifacts.apis.io/aria2/vocabulary/aria2-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aria2-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aria2/data-model/aria2-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aria2-data-model.yml
- group: design
  href: https://artifacts.apis.io/aria2/conformance/aria2-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aria2-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aria2/llms/aria2-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aria2-llms.txt
- group: other
  href: https://artifacts.apis.io/aria2/hosts/aria2-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aria2-hosts.yml
- group: other
  href: https://artifacts.apis.io/aria2/vendors/aria2-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aria2-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://ubuntu.com/docs/launchpad/developer/how-to/get-started/running-quickstart
- group: auth
  href: https://artifacts.apis.io/aria2/security/aria2-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aria2-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://translations.launchpad.net/aria2/trunk/+pots/aria2
- group: docs
  title: ''
  type: Documentation
  url: https://aria2.github.io/manual/en/html/index.html
- group: other
  title: ''
  type: Source
  url: https://github.com/aria2/aria2
- group: other
  title: ''
  type: Bugs
  url: https://github.com/aria2/aria2/issues
coverage:
  checked: '2026-10-28'
  detail: The provider's documentation does not publish a machine‑readable OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL contract.
  evidence:
  - status: 200
    url: https://aria2.github.io/manual/en/html/index.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: aria2 is a lightweight, multi-protocol command-line download utility supporting HTTP/HTTPS, FTP, SFTP, BitTorrent and Metalink. It offers JSON-RPC and XML-RPC interfaces for remote control, and is open‑source under GPL‑2.0. The tool is highly efficient, using minimal memory and CPU, and can split downloads across multiple sources to maximize bandwidth. It runs on Windows, macOS, Linux, Android and integrates with various package managers.
image: https://translations.launchpad.net/@@/launchpad-og-image.png
json_schemas:
- name: Get10Response
  property_count: 3
  slug: aria2-get10-response
jsonld:
- class_count: 1
  name: Aria2 Context
  property_count: 3
  slug: aria2-context
layout: provider
modified: '2026-10-28'
name: aria2
nav: Providers
network: true
overview: 'aria2 is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Downloads, Open Source, Command Line, and Multi-Protocol.


  The aria2 catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  aria2''s developer surface includes getting-started guide, documentation, and 13 more developer resources.'
plans:
- name: Aria2 Plans Pricing
  plan_count: 10
  slug: aria2-plans-pricing
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: aria2 API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: aria2-rules
score:
  band: emerging
  composite: 20.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 60.2
    catalog_earned_first_party: 12.0
    catalog_gap: 54.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.1
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 17.6
    developer_ergonomics: 10.7
    discoverability: 64.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 22.7
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
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/aria2/aria2-2026-11-03T121119.png
security:
- kind: domain-security
  name: Aria2 Domain Security
  slug: aria2-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aria2
tags:
- Company
- Downloads
- Open Source
- Command Line
- Multi-Protocol
website: https://translations.launchpad.net/aria2/trunk/+pots/aria2
---
