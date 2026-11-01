---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Llmhosting Ai Agentic Access
  operation_count: 4
  slug: llmhosting-ai-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://llmhosting.ai
  baseurl_source: declared
  description: The Gpu History.csv API from llmhosting-ai — 1 operation(s) for gpu history.csv.
  name: llmhosting-ai Gpu History.csv API
  slug: llmhosting-ai-gpu-history-csv-api
- baseURL: https://llmhosting.ai
  baseurl_source: declared
  description: The Gpu History.json API from llmhosting-ai — 1 operation(s) for gpu history.json.
  name: llmhosting-ai Gpu History.json API
  slug: llmhosting-ai-gpu-history-json-api
- baseURL: https://llmhosting.ai
  baseurl_source: declared
  description: The Gpu Prices.json API from llmhosting-ai — 1 operation(s) for gpu prices.json.
  name: llmhosting-ai Gpu Prices.json API
  slug: llmhosting-ai-gpu-prices-json-api
- baseURL: https://llmhosting.ai
  baseurl_source: declared
  description: The Prices.json API from llmhosting-ai — 1 operation(s) for prices.json.
  name: llmhosting-ai Prices.json API
  slug: llmhosting-ai-prices-json-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/llmhosting-ai/agentic-access/llmhosting-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/llmhosting-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/llmhosting-ai/rules/llmhosting-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/llmhosting-ai-rules.yml
- group: auth
  href: https://artifacts.apis.io/llmhosting-ai/security/llmhosting-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/llmhosting-ai-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/llmhosting-ai/conformance/llmhosting-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/llmhosting-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/llmhosting-ai/llms/llmhosting-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/llmhosting-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/llmhosting-ai/well-known/llmhosting-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/llmhosting-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/llmhosting-ai/well-known/llmhosting-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/llmhosting-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/llmhosting-ai/hosts/llmhosting-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/llmhosting-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/llmhosting-ai/vendors/llmhosting-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/llmhosting-ai-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://llmhosting.ai/guides
- group: auth
  href: https://artifacts.apis.io/llmhosting-ai/security/llmhosting-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/llmhosting-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/llmhosting-ai/security/llmhosting-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/llmhosting-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://llmhosting.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://llmhosting.ai/api-access
- group: commercial
  title: ''
  type: Pricing
  url: https://llmhosting.ai/calculator
created: '2026-10-30'
description: llmhosting-ai provides a comparative platform that aggregates LLM API pricing and GPU rental rates from various providers. It refreshes data daily, offering users a clear view of per-token costs and compute pricing to help choose the most cost-effective solutions for running large language models. The service also includes methodology details, source transparency, and links to the underlying provider APIs.
image: https://llmhosting.ai/favicon.svg
layout: provider
modified: '2026-10-30'
name: llmhosting-ai
nav: Providers
network: true
overview: 'llmhosting-ai publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Gpu History.csv API, Gpu History.json API, Gpu Prices.json API, and 1 more. Tagged areas include Company, LLM, Pricing, GPU, and Comparison.


  The llmhosting-ai catalog on APIs.io includes 1 Spectral governance ruleset.


  llmhosting-ai''s developer surface includes documentation, API reference, pricing, and 12 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: llmhosting-ai API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: llmhosting-ai-rules
score:
  band: emerging
  composite: 25.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 41.0
    developer_ergonomics: 16.7
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Llmhosting Ai Domain Security
  slug: llmhosting-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Llmhosting Ai Vulnerability Disclosure
  slug: llmhosting-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: llmhosting-ai
tags:
- Company
- LLM
- Pricing
- GPU
- Comparison
website: https://llmhosting.ai/
---
