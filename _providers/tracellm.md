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
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.tracellm.in
  baseurl_source: declared
  description: 'TraceLLM API as documented publicly: 24 operations. Contract generated from the documentation by API Evangelist (2026-10-19); not the provider''s own document.'
  name: TraceLLM API
  slug: tracellm-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/tracellm/rules/tracellm-rules.yml
  title: ''
  type: Spectral
  url: rules/tracellm-rules.yml
- group: design
  href: https://artifacts.apis.io/tracellm/vocabulary/tracellm-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tracellm-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/tracellm/conformance/tracellm-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tracellm-conformance.yml
- group: other
  href: https://artifacts.apis.io/tracellm/hosts/tracellm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tracellm-hosts.yml
- group: other
  href: https://artifacts.apis.io/tracellm/vendors/tracellm-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tracellm-vendors.yml
- group: build
  href: https://artifacts.apis.io/tracellm/packages/tracellm-packages.yml
  title: ''
  type: SDKs
  url: packages/tracellm-packages.yml
- group: build
  href: https://artifacts.apis.io/tracellm/packages/tracellm-packages.yml
  title: ''
  type: Packages
  url: packages/tracellm-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tracellm.in/getting-started/chatbot-step-1-session-tracing/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tracellm.in/
- group: auth
  href: https://artifacts.apis.io/tracellm/security/tracellm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tracellm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tracellm.in/
coverage:
  checked: '2026-10-19'
  detail: The provider's website renders a JavaScript shell and no machine‑readable spec could be retrieved.
  evidence:
  - status: 200
    url: https://tracellm.in
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-19'
description: 'TraceLLM is a company surfaced via the API Evangelist harvest backlog (source: g2-catalog) and added to the network as a stub for full-pipeline profiling.'
image: https://tracellm.in/og-image.png
layout: provider
modified: '2026-10-19'
name: TraceLLM
nav: Providers
network: true
overview: 'TraceLLM is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  The TraceLLM catalog on APIs.io includes 1 Spectral governance ruleset.


  TraceLLM''s developer surface includes getting-started guide, documentation, and 9 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: TraceLLM API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: tracellm-rules
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.1
  facets:
    access_clarity: 0.0
    contract_governance: 19.7
    contract_quality: 10.7
    developer_ergonomics: 17.9
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 14.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
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
screenshot: https://apis.io/screenshots/tracellm/tracellm-2026-11-03T144939.png
security:
- kind: domain-security
  name: Tracellm Domain Security
  slug: tracellm-domain-security
  summary_line: TLSv1.3 · HSTS
slug: tracellm
tags:
- Company
website: https://tracellm.in/
---
