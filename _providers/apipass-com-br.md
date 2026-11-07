---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API platform for integration services as described in the APIPASS documentation.
  name: APIPASS API
  slug: apipass-api
- description: 'Keila Santos API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: Keila Santos API
  slug: apipass-com-br-api
artifact_total: 8
common:
- group: other
  href: https://artifacts.apis.io/apipass-com-br/vendors/apipass-com-br-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apipass-com-br-vendors.yml
- group: operate
  href: https://artifacts.apis.io/apipass-com-br/rate-limits/apipass-com-br-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apipass-com-br-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/apipass-com-br/rules/apipass-com-br-rules.yml
  title: ''
  type: Spectral
  url: rules/apipass-com-br-rules.yml
- group: design
  href: https://artifacts.apis.io/apipass-com-br/json-ld/apipass-com-br-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/apipass-com-br-context.jsonld
- group: design
  href: https://artifacts.apis.io/apipass-com-br/vocabulary/apipass-com-br-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apipass-com-br-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/apipass-com-br/data-model/apipass-com-br-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apipass-com-br-data-model.yml
- group: auth
  href: https://artifacts.apis.io/apipass-com-br/authentication/apipass-com-br-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apipass-com-br-authentication.yml
- group: design
  href: https://artifacts.apis.io/apipass-com-br/conformance/apipass-com-br-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apipass-com-br-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apipass-com-br/llms/apipass-com-br-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apipass-com-br-llms.txt
- group: agent
  href: https://artifacts.apis.io/apipass-com-br/well-known/apipass-com-br-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apipass-com-br-well-known.yml
- group: other
  href: https://artifacts.apis.io/apipass-com-br/hosts/apipass-com-br-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apipass-com-br-hosts.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.apipass.com.br/documentacao-apipass/introducao/release-notes
- group: company
  title: ''
  type: Blog
  url: https://apipass.com.br/blog/mcp/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.apipass.com.br/
- group: auth
  href: https://artifacts.apis.io/apipass-com-br/security/apipass-com-br-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apipass-com-br-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apipass.com.br/
coverage:
  checked: '2026-10-20'
  detail: Documentation is provided in markdown but no OpenAPI or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://docs.apipass.com.br
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: 'Keila Santos is a company surfaced via the API Evangelist harvest backlog (source: g2-catalog) and added to the network as a stub for full-pipeline profiling.'
image: https://apipass.com.br/wp-content/uploads/2026/06/open-graph.webp
json_schemas:
- name: PostD5Ddf05391754Ab6Ab732E114648E2C9Request
  property_count: 1
  slug: apipass-com-br-post-d5-ddf05391754-ab6-ab732-e114648-e2-c9-request
jsonld:
- class_count: 1
  name: Apipass Com Br Context
  property_count: 1
  slug: apipass-com-br-context
layout: provider
modified: '2026-10-20'
name: Keila Santos
nav: Providers
network: true
overview: 'Keila Santos is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  The Keila Santos catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Keila Santos'' developer surface includes authentication, changelog, engineering blog, documentation, and 12 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 1
  name: Apipass Com Br Rate Limits
  slug: apipass-com-br-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Keila Santos API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: apipass-com-br-rules
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 46.2
    catalog_earned_first_party: 8.0
    catalog_gap: 68.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 17.6
    developer_ergonomics: 17.9
    discoverability: 46.4
    operational_transparency: 28.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 20.8
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
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/apipass-com-br/apipass-com-br-2026-11-03T120957.png
security:
- kind: authentication
  name: Apipass Com Br Authentication
  slug: apipass-com-br-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Apipass Com Br Domain Security
  slug: apipass-com-br-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: apipass-com-br
tags:
- Company
website: https://apipass.com.br/
---
