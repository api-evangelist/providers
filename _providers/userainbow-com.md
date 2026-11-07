---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Userainbow Com Agentic Access
  operation_count: 9
  slug: userainbow-com-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 1
apis:
- baseURL: //api.demo.userainbow.com/partner/api/v1
  baseurl_source: spec
  description: The Agency API from Rainbow — 6 operation(s) for agency.
  name: Rainbow Agency API
  slug: userainbow-com-agency-api
- baseURL: //api.demo.userainbow.com/partner/api/v1
  baseurl_source: spec
  description: The Appetite API from Rainbow — 1 operation(s) for appetite.
  name: Rainbow Appetite API
  slug: userainbow-com-appetite-api
- baseURL: //api.demo.userainbow.com/partner/api/v1
  baseurl_source: spec
  description: The Indication API from Rainbow — 2 operation(s) for indication.
  name: Rainbow Indication API
  slug: userainbow-com-indication-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/userainbow-com/agentic-access/userainbow-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/userainbow-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/userainbow-com/rules/userainbow-com-rules.yml
  title: ''
  type: Spectral
  url: rules/userainbow-com-rules.yml
- group: design
  href: https://artifacts.apis.io/userainbow-com/json-ld/userainbow-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/userainbow-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/userainbow-com/vocabulary/userainbow-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/userainbow-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/userainbow-com/data-model/userainbow-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/userainbow-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/userainbow-com/authentication/userainbow-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/userainbow-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/userainbow-com/errors/userainbow-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/userainbow-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/userainbow-com/conformance/userainbow-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/userainbow-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/userainbow-com/llms/userainbow-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/userainbow-com-llms.txt
- group: other
  href: https://artifacts.apis.io/userainbow-com/hosts/userainbow-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/userainbow-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/userainbow-com/vendors/userainbow-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/userainbow-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.userainbow.com/press
- group: start
  title: ''
  type: Login
  url: https://app.userainbow.com/auth/login
- group: company
  title: ''
  type: Blog
  url: https://www.userainbow.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://apidocs.userainbow.com/docs/quick-start
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.userainbow.com/
- group: auth
  href: https://artifacts.apis.io/userainbow-com/security/userainbow-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/userainbow-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://userainbow.com
coverage:
  checked: '2026-10-25'
  detail: The provider's website presents only HTML pages without any OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://www.userainbow.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-25'
description: Rainbow MGA Insurance Agency provides property and casualty insurance coverage for restaurants, commercial real‑estate properties, and beauty & wellness businesses. The company works through independent agents, offering digital quoting, self‑service portal tools, and underwriting support to help agents place policies for small‑business clients across the United States.
image: https://cdn.prod.website-files.com/6769b9aeec67789d18aafc30/6785e52574ce87e22cdd60a1_rainbow-open%20graph-2.jpg
jsonld:
- class_count: 28
  name: Userainbow Com Context
  property_count: 69
  slug: userainbow-com-context
layout: provider
modified: '2026-10-25'
name: Rainbow
nav: Providers
network: true
overview: 'Rainbow publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Agency API, Appetite API, and Indication API. Tagged areas include Insurance, Restaurant, Commercial Real Estate, Beauty and Wellness, and Agents.


  The Rainbow catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Rainbow''s developer surface includes authentication, engineering blog, getting-started guide, documentation, and 14 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Rainbow API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: userainbow-com-rules
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 43.8
    catalog_earned_first_party: 0.0
    catalog_gap: 71.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.4
  facets:
    access_clarity: 6.6
    contract_governance: 22.0
    contract_quality: 64.6
    developer_ergonomics: 23.8
    discoverability: 56.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 31.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 14.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/userainbow-com/userainbow-com-2026-11-03T145535.png
security:
- kind: authentication
  name: Userainbow Com Authentication
  slug: userainbow-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Userainbow Com Domain Security
  slug: userainbow-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: userainbow-com
tags:
- Insurance
- Restaurant
- Commercial Real Estate
- Beauty and Wellness
- Agents
- MGA
website: https://userainbow.com
---
