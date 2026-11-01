---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 39.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.credal.ai
  baseurl_source: declared
  description: 'Credal API as documented publicly: 11 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: Credal API
  slug: credal-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/credal/plans/credal-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/credal-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/credal/rules/credal-rules.yml
  title: ''
  type: Spectral
  url: rules/credal-rules.yml
- group: design
  href: https://artifacts.apis.io/credal/json-ld/credal-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/credal-context.jsonld
- group: design
  href: https://artifacts.apis.io/credal/vocabulary/credal-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/credal-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/credal/data-model/credal-data-model.yml
  title: ''
  type: DataModel
  url: data-model/credal-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://credal.ai/security
- group: auth
  href: https://artifacts.apis.io/credal/authentication/credal-authentication.yml
  title: ''
  type: Authentication
  url: authentication/credal-authentication.yml
- group: design
  href: https://artifacts.apis.io/credal/conformance/credal-conformance.yml
  title: ''
  type: Conformance
  url: conformance/credal-conformance.yml
- group: agent
  href: https://artifacts.apis.io/credal/llms/credal-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/credal-llms.txt
- group: agent
  href: https://artifacts.apis.io/credal/mcp/credal-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/credal-mcp.yml
- group: agent
  href: https://artifacts.apis.io/credal/well-known/credal-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/credal-well-known.yml
- group: other
  href: https://artifacts.apis.io/credal/hosts/credal-hosts.yml
  title: ''
  type: Hosts
  url: hosts/credal-hosts.yml
- group: other
  href: https://artifacts.apis.io/credal/vendors/credal-vendors.yml
  title: ''
  type: Vendors
  url: vendors/credal-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://credal.ai/policies/terms-and-conditions
- group: auth
  title: ''
  type: Security
  url: https://credal.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://credal.ai/policies/privacy.html
- group: other
  title: ''
  type: Leadership
  url: https://credal.ai/team
- group: auth
  href: https://artifacts.apis.io/credal/security/credal-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/credal-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/credal/security/credal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/credal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://credal.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.credal.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.credal.ai/api-reference
- group: commercial
  title: ''
  type: Pricing
  url: https://credal.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://credal.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://credal.ai/get-started
coverage:
  checked: '2026-10-20'
  detail: Credal provides documentation pages but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://api.credal.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: Credal provides an enterprise platform enabling teams to build, govern, and deploy multi‑contextual processing (MCP) servers. It offers curated context, tool integrations, and cost‑to‑accuracy evaluations for workflows, supporting agents that interact with data sources like Salesforce, Snowflake, and Slack. The platform includes an Agent Builder, Agent Registry, and a suite of pre‑built tools, aiming to improve operational efficiency and governance across AI‑driven applications.
image: https://uploads-ssl.webflow.com/65f30a04a926c4ab669afe03/65fafdb5e360fccde6f003ee_ogPreview.png
json_schemas:
- name: PostApiRequest
  property_count: 6
  slug: credal-post-api-request
- name: PostApiResponse
  property_count: 3
  slug: credal-post-api-response
- name: PostApiV0CopilotsSendmessageResponse
  property_count: 1
  slug: credal-post-api-v0-copilots-sendmessage-response
- name: PostApiV1Request
  property_count: 3
  slug: credal-post-api-v1-request
- name: PostApiV1Response
  property_count: 2
  slug: credal-post-api-v1-response
- name: PostV1AgentsSendmessageRequest
  property_count: 5
  slug: credal-post-v1-agents-sendmessage-request
jsonld:
- class_count: 11
  name: Credal Context
  property_count: 18
  slug: credal-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.credal.ai.
  name: Credal MCP Server
  slug: credal-mcp-yml
modified: '2026-10-19'
name: Credal
nav: Providers
network: true
overview: 'Credal is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Platform, Enterprise, and Automation.


  The Credal catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Credal''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, getting-started guide, and 19 more developer resources.'
plans:
- name: Credal Plans Pricing
  plan_count: 1
  slug: credal-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Credal API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: credal-rules
score:
  band: developing
  composite: 41.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 68.4
    contract_governance: 22.0
    contract_quality: 26.2
    developer_ergonomics: 42.9
    discoverability: 66.7
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Credal Authentication
  slug: credal-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Credal Domain Security
  slug: credal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Credal Trust Center
  slug: credal-trust-center
  summary_line: SOC 2, HIPAA
slug: credal
tags:
- Company
- Artificial Intelligence
- Platform
- Enterprise
- Automation
website: https://credal.ai/
---
