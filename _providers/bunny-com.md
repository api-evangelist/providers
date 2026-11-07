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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Bunny provides AI‑native billing, CPQ and RevOps APIs as documented in the developer guide.
  name: Bunny API
  slug: bunny-api
- baseURL: https://SUBDOMAIN.bunny.com
  baseurl_source: declared
  description: 'Bunny API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Bunny API
  slug: bunny-com-api
artifact_total: 13
asyncapis:
- description: ''
  name: Bunny Com Webhooks
  slug: bunny-com-webhooks
common:
- group: design
  href: https://artifacts.apis.io/bunny-com/rules/bunny-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bunny-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bunny-com/json-ld/bunny-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bunny-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/bunny-com/vocabulary/bunny-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bunny-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bunny-com/asyncapi/bunny-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/bunny-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/bunny-com/data-model/bunny-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bunny-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/bunny-com/changelog/bunny-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bunny-com-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://bunny.com/security/
- group: auth
  href: https://artifacts.apis.io/bunny-com/authentication/bunny-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bunny-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/bunny-com/conformance/bunny-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bunny-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bunny-com/llms/bunny-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bunny-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/bunny-com/mcp/bunny-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bunny-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/bunny-com/hosts/bunny-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bunny-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bunny-com/vendors/bunny-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bunny-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bunny.com/terms
- group: operate
  title: ''
  type: Support
  url: https://bunny.com/support/
- group: start
  title: ''
  type: SignUp
  url: https://bunny.com/signup/
- group: auth
  title: ''
  type: Security
  url: https://bunny.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bunny.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.bunny.com/guide/tour/product-catalog/plans
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.bunny.com/guide/release-notes/jul-3-2025
- group: company
  title: ''
  type: Blog
  url: https://bunny.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bunny.com/guide/getting-started/superdesk-sample-saas-co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bunny.com/
- group: auth
  href: https://artifacts.apis.io/bunny-com/security/bunny-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bunny-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/bunny-com/security/bunny-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bunny-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bunny-com/security/bunny-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bunny-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bunny.com/
coverage:
  checked: '2026-11-03'
  detail: Documentation provides a JSON operations list but no OpenAPI, GraphQL SDL, AsyncAPI, gRPC, or WSDL contract.
  evidence:
  - status: 200
    url: https://docs.bunny.com/developer/api-reference/api-reference.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Bunny is an AI‑native SaaS billing, CPQ and RevOps platform helping B2B SaaS companies manage revenue operations. Headquartered in Santa Monica, California, Bunny offers modern subscription billing, pricing automation, and revenue intelligence tools to streamline complex enterprise deals and accelerate growth. The platform emphasizes agility, accuracy, and reduced operational complexity for fast‑scaling businesses.
image: https://bunny.com/assets/images/og/og-home.png
json_schemas:
- name: GetResponse
  property_count: 4
  slug: bunny-com-get-response
- name: PostGraphqlRequest
  property_count: 2
  slug: bunny-com-post-graphql-request
- name: PostRequest
  property_count: 2
  slug: bunny-com-post-request
jsonld:
- class_count: 3
  name: Bunny Com Context
  property_count: 6
  slug: bunny-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.bunny.com.
  name: Bunny MCP Server
  slug: bunny-com-mcp-yml
modified: '2026-11-03'
name: Bunny
nav: Providers
network: true
overview: 'Bunny is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Billing, CPQ, Revenue Recognition, SaaS Analytics, and Revenue Operations.


  The Bunny catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Bunny''s developer surface includes changelog, authentication, support, signup flow, pricing, engineering blog, getting-started guide, and 20 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: Bunny API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: bunny-com-rules
score:
  band: thin
  composite: 32.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 29.4
    developer_ergonomics: 26.2
    discoverability: 56.7
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bunny Com Authentication
  slug: bunny-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bunny Com Domain Security
  slug: bunny-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bunny Com Vulnerability Disclosure
  slug: bunny-com-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Bunny Com Trust Center
  slug: bunny-com-trust-center
  summary_line: SOC 2
slug: bunny-com
tags:
- Billing
- CPQ
- Revenue Recognition
- SaaS Analytics
- Revenue Operations
- Stripe Integration
- AI Agents
website: https://bunny.com/
---
