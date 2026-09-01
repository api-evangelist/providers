---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Kanye Rest Agentic Access
  operation_count: 3
  slug: kanye-rest-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: Endpoints that return random or bulk Kanye West quotes.
  name: kanye.rest Quotes API
  slug: kanye-rest-quotes-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kanye REST Quotes API
  slug: open-kanye-rest-quotes-api
- collection_type: open
  name: Kanye REST
  slug: open-kanye-rest
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/ajzbc/kanye.rest/issues
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kanye-rest-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kanye-rest-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kanye.rest
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ajzbc/kanye.rest
- group: commercial
  title: MIT License
  type: License
  url: https://github.com/ajzbc/kanye.rest/blob/master/LICENSE
- group: build
  title: kanye.rest-cli (archived)
  type: CLI
  url: https://github.com/ajzbc/kanye.rest-cli
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: design
  title: ''
  type: SpectralRules
  url: rules/kanye-rest-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/kanye-rest-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/kanye-rest-context.jsonld
- group: docs
  title: Quote
  type: JSONSchema
  url: json-schema/kanye-rest-quote-schema.json
- group: docs
  title: QuoteList
  type: JSONSchema
  url: json-schema/kanye-rest-quote-list-schema.json
- group: design
  title: Quote
  type: JSONStructure
  url: json-structure/kanye-rest-quote-structure.json
- group: design
  title: QuoteList
  type: JSONStructure
  url: json-structure/kanye-rest-quote-list-structure.json
- group: build
  title: Quote Example
  type: Examples
  url: examples/kanye-rest-quote-example.json
- group: build
  title: QuoteList Example
  type: Examples
  url: examples/kanye-rest-quote-list-example.json
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kanye-rest-rate-limits.yml
created: '2026-05-28'
description: Free single-purpose REST API that returns random Kanye West quotes, dubbed "Kanye as a Service." Hosted on Cloudflare Workers, the API exposes a JSON endpoint, a plain-text endpoint, and a full-quotes-array endpoint. The underlying project is open source (MIT) under github.com/ajzbc/kanye.rest and is a popular example of a minimal "fun" public API.
examples:
- key_count: 1
  name: Kanye Rest Quote Example
  slug: kanye-rest-quote-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kanye-rest.png
json_schemas:
- name: QuoteList
  property_count: 0
  slug: kanye-rest-quote-list
- name: Quote
  property_count: 1
  slug: kanye-rest-quote
json_structures:
- name: Kanye Rest Quote List Structure
  property_count: 0
  slug: kanye-rest-quote-list-structure
- name: Kanye Rest Quote Structure
  property_count: 1
  slug: kanye-rest-quote-structure
jsonld:
- class_count: 5
  name: Kanye Rest Context
  property_count: 2
  slug: kanye-rest-context
layout: provider
modified: '2026-05-29'
name: kanye.rest
nav: Providers
network: true
overview: 'kanye.rest publishes 1 API on the [APIs.io](https://apis.io/) network: Quotes API. Tagged areas include Personality, Quotes, Open-Source, Cloudflare Workers, and Public APIs.


  The kanye.rest catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  kanye.rest''s developer surface includes CLI, code examples, and 16 more developer resources.'
random_paper: 19
rate_limits:
- limit_count: 3
  name: Kanye Rest Rate Limits
  slug: kanye-rest-rate-limits
rules:
- effective_rule_count: 4
  extends: []
  name: kanye.rest API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: kanye-rest-jsonschema-spectral-rules
- effective_rule_count: 84
  extends:
  - spectral:oas
  name: kanye.rest API Rules
  rule_count: 43
  severity_counts:
    error: 14
    hint: 0
    info: 8
    warn: 21
  slug: kanye-rest-spectral-rules
score:
  band: emerging
  composite: 22.6
  coverage:
    artifact_dirs: 12
    catalog_gap: 48.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 28.8
    contract_quality: 21.3
    developer_ergonomics: 7.1
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 36.8
  previous_composite: 22.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kanye-rest/refs/heads/main/screenshots/kanye-rest-2026-06-20T183915.png
security:
- kind: domain-security
  name: Kanye Rest Domain Security
  slug: kanye-rest-domain-security
  summary_line: TLSv1.3
slug: kanye-rest
tags:
- Personality
- Quotes
- Open-Source
- Cloudflare Workers
- Public APIs
website: https://kanye.rest
---
