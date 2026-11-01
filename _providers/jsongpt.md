---
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
    error_semantics: derived
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
  score: 13.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: JSON GPT API provides JSON responses based on text prompts.
  name: JsonGPT API
  slug: jsongpt-api
- baseURL: https://api.jsongpt.com
  baseurl_source: declared
  description: This API provides JSON responses based on the provided text prompts.
  name: JSON GPT API API
  slug: json-gpt-api-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/jsongpt/rules/jsongpt-rules.yml
  title: ''
  type: Spectral
  url: rules/jsongpt-rules.yml
- group: design
  href: https://artifacts.apis.io/jsongpt/conformance/jsongpt-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jsongpt-conformance.yml
- group: design
  href: https://artifacts.apis.io/jsongpt/errors/jsongpt-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/jsongpt-problem-types.yml
- group: other
  href: https://artifacts.apis.io/jsongpt/hosts/jsongpt-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jsongpt-hosts.yml
- group: other
  href: https://artifacts.apis.io/jsongpt/vendors/jsongpt-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jsongpt-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.jsongpt.com/
- group: auth
  href: https://artifacts.apis.io/jsongpt/security/jsongpt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jsongpt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jsongpt.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.jsongpt.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://jsongpt.com/playground
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/jsongpt/workspace
created: '2026-10-17'
description: JsonGPT provides a simple API that generates JSON data using AI models such as OpenAI, Gemini, and others. It offers features like JSON validation, prompt caching, streaming responses, and multi‑model support, enabling developers to quickly integrate structured AI‑generated data into their applications without manual parsing. The service includes a free playground with 30 free calls, extensive documentation, and SDKs for various languages, aiming to reduce development time and cost for JSON‑centric AI use cases.
image: https://jsongpt.com/opengraph-image.png?46bec1113ea0be97
layout: provider
modified: '2026-10-17'
name: JsonGPT
nav: Providers
network: true
overview: 'JsonGPT publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including JSON GPT API API, and 1 more. Tagged areas include Company, Artificial Intelligence, JSON, and Automation.


  The JsonGPT catalog on APIs.io includes 1 Spectral governance ruleset.


  JsonGPT''s developer surface includes documentation, API reference, getting-started guide, and 8 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: JsonGPT API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: jsongpt-rules
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 38.6
    developer_ergonomics: 33.3
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 24.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Jsongpt Domain Security
  slug: jsongpt-domain-security
  summary_line: TLSv1.3 · HSTS
slug: jsongpt
tags:
- Company
- Artificial Intelligence
- JSON
- Automation
website: https://jsongpt.com/
---
