---
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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.2
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API reference for Cloud MCP platform
  name: Cloud MCP API
  slug: cloud-mcp-api
- baseURL: http://sandbox.mintlify.com
  baseurl_source: declared
  description: The Cloud MCP API API from Cloud MCP — 1 operation(s) for cloud mcp api.
  name: Cloud MCP Cloud MCP API
  slug: cloudmcp-cloud-mcp-api-api
- baseURL: http://sandbox.mintlify.com
  baseurl_source: declared
  description: The Credit API from Cloud MCP — 1 operation(s) for credit.
  name: Cloud MCP Credit API
  slug: cloudmcp-credit-api
- baseURL: http://sandbox.mintlify.com
  baseurl_source: declared
  description: The Dashboard API from Cloud MCP — 1 operation(s) for dashboard.
  name: Cloud MCP Dashboard API
  slug: cloudmcp-dashboard-api
- baseURL: http://sandbox.mintlify.com
  baseurl_source: declared
  description: The Orders API from Cloud MCP — 1 operation(s) for orders.
  name: Cloud MCP Orders API
  slug: cloudmcp-orders-api
- baseURL: http://sandbox.mintlify.com
  baseurl_source: declared
  description: The Plants API from Cloud MCP — 2 operation(s) for plants.
  name: Cloud MCP Plants API
  slug: cloudmcp-plants-api
- baseURL: http://sandbox.mintlify.com
  baseurl_source: declared
  description: The User API from Cloud MCP — 1 operation(s) for user.
  name: Cloud MCP User API
  slug: cloudmcp-user-api
- baseURL: http://sandbox.mintlify.com
  baseurl_source: declared
  description: The Users API from Cloud MCP — 1 operation(s) for users.
  name: Cloud MCP Users API
  slug: cloudmcp-users-api
artifact_total: 17
common:
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cloudmcp.run/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cloudmcp/refs/heads/main/plans/cloudmcp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cloudmcp-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudmcp/refs/heads/main/rules/cloudmcp-rules.yml
  title: ''
  type: Spectral
  url: rules/cloudmcp-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudmcp/refs/heads/main/json-ld/cloudmcp-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudmcp-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudmcp/refs/heads/main/vocabulary/cloudmcp-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cloudmcp-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudmcp/refs/heads/main/data-model/cloudmcp-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cloudmcp-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudmcp/refs/heads/main/authentication/cloudmcp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cloudmcp-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudmcp/refs/heads/main/conformance/cloudmcp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloudmcp-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudmcp/refs/heads/main/llms/cloudmcp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudmcp-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudmcp/refs/heads/main/a2a/cloudmcp-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/cloudmcp-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudmcp/refs/heads/main/well-known/cloudmcp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cloudmcp-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudmcp/refs/heads/main/hosts/cloudmcp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudmcp-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudmcp/refs/heads/main/vendors/cloudmcp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudmcp-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mintlify
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cloudmcp.run/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cloudmcp.run/llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudmcp/refs/heads/main/security/cloudmcp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudmcp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloudmcp.run/
- group: commercial
  title: ''
  type: Pricing
  url: https://cloudmcp.run/pricing
- group: company
  title: ''
  type: Blog
  url: https://cloudmcp.run/blog
- group: operate
  title: ''
  type: Support
  url: https://cloudmcp.run/support
coverage:
  checked: '2026-10-16'
  detail: OpenAPI spec is hosted on sandbox.mintlify.com, not on Cloud MCP's domain, so ownership cannot be verified.
  evidence:
  - status: 200
    url: https://docs.cloudmcp.run/api-reference/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-16'
description: Cloud MCP provides a Remote Model Context Protocol (MCP) platform that enables AI assistants like Claude and ChatGPT to connect to real-world tools such as Google Calendar, databases, file systems, and web search without requiring API keys or terminal commands. Users receive a secure private URL that the AI can use to perform actions like scheduling meetings, querying data, managing files, and accessing advertising insights. The service offers a library of connectors, simple pricing with a free tier, and supports OAuth 2.1 security. Cloud MCP aims to simplify AI tool integration for developers and enterprises.
image: https://cloudmcp.run/og
json_schemas:
- name: DeletePlantsIdResponse
  property_count: 2
  slug: cloudmcp-delete-plants-id-response
- name: GetPlantsIdResponse
  property_count: 2
  slug: cloudmcp-get-plants-id-response
- name: GetPlantsResponse
  property_count: 2
  slug: cloudmcp-get-plants-response
- name: PostPlantsResponse
  property_count: 2
  slug: cloudmcp-post-plants-response
jsonld:
- class_count: 4
  name: Cloudmcp Context
  property_count: 6
  slug: cloudmcp-context
layout: provider
modified: '2026-10-16'
name: Cloud MCP
nav: Providers
network: true
overview: 'Cloud MCP publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Cloud MCP API, Credit API, Dashboard API, and 5 more. Tagged areas include Company, Artificial Intelligence, Integration, Tools, and Automation.


  The Cloud MCP catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cloud MCP''s developer surface includes documentation, authentication, getting-started guide, API reference, pricing, engineering blog, support, and 14 more developer resources.'
plans:
- name: Cloudmcp Plans Pricing
  plan_count: 4
  slug: cloudmcp-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Cloud MCP API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: cloudmcp-rules
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 20.7
    developer_ergonomics: 47.6
    discoverability: 64.3
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Cloudmcp Authentication
  slug: cloudmcp-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Cloudmcp Domain Security
  slug: cloudmcp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cloudmcp
tags:
- Company
- Artificial Intelligence
- Integration
- Tools
- Automation
website: https://cloudmcp.run/
---
