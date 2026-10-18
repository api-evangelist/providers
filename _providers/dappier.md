---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Dappier Agentic Access
  operation_count: 2
  slug: dappier-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- baseURL: https://api.dappier.com
  baseurl_source: declared
  description: The App API from Dappier — 2 operation(s) for app.
  name: Dappier App API
  slug: dappier-app-api
artifact_total: 8
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dappier/refs/heads/main/vocabulary/dappier-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dappier-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dappier/refs/heads/main/data-model/dappier-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dappier-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dappier/refs/heads/main/agentic-access/dappier-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dappier-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dappier/refs/heads/main/rules/dappier-rules.yml
  title: ''
  type: Spectral
  url: rules/dappier-rules.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dappier/refs/heads/main/authentication/dappier-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dappier-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dappier/refs/heads/main/conformance/dappier-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dappier-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dappier/refs/heads/main/overlays/dappier-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dappier-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dappier/refs/heads/main/llms/dappier-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dappier-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dappier/refs/heads/main/a2a/dappier-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/dappier-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dappier/refs/heads/main/mcp/dappier-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dappier-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dappier/refs/heads/main/well-known/dappier-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dappier-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dappier/refs/heads/main/hosts/dappier-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dappier-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dappier/refs/heads/main/vendors/dappier-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dappier-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/dappier/refs/heads/main/packages/dappier-packages.yml
  title: ''
  type: SDKs
  url: packages/dappier-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/dappier/refs/heads/main/packages/dappier-packages.yml
  title: ''
  type: Packages
  url: packages/dappier-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DappierAI
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dappier/refs/heads/main/security/dappier-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dappier-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dappier.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dappier.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://dappier.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dappier.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://dappier.com/developer
- group: operate
  title: ''
  type: Support
  url: https://dappier.com/contact
- group: company
  title: ''
  type: Blog
  url: https://dappier.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://dappier.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dappier.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dappier.com/privacy
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://docs.dappier.com/mcp
  - status: 403
    url: https://api.dappier.com/mcp
  - status: 403
    url: https://marketplace.dappier.com/mcp
  - status: 403
    url: https://platform.dappier.com/mcp
  - status: 200
    url: https://dappier.com/
  reason: no-developer-program
  state: none
created: '2026-10-16'
description: Dappier provides AI-driven conversational ad experiences for publishers, enabling them to monetize content through agentic ads and AI answer interfaces. It offers a platform where advertisers can reach consumers via AI agents, with a storefront that allows autonomous purchases without signup. The service includes tools for launching AI answer experiences, managing ad formats, and integrating with publisher workflows, aiming to create new revenue streams in the AI era.
image: https://assets.dappier.com/logos/DappierMini.jpg
json_schemas:
- name: QueryRequest
  property_count: 0
  slug: dappier-query-request
- name: QueryResponse
  property_count: 0
  slug: dappier-query-response
layout: provider
mcp_servers:
- description: Remote MCP server at sales-agent.dappier.com.
  name: Dappier MCP Server
  slug: dappier-mcp-yml
modified: '2026-10-16'
name: Dappier
nav: Providers
network: true
overview: 'Dappier publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: App API. Tagged areas include Company, Artificial Intelligence, Advertising, Monetization, and Publishers.


  The Dappier catalog on APIs.io includes 1 Spectral governance ruleset.


  Dappier''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 20 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Dappier API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: dappier-rules
score:
  band: developing
  composite: 43.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 50.2
    developer_ergonomics: 64.3
    discoverability: 75.0
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Dappier Authentication
  slug: dappier-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dappier Domain Security
  slug: dappier-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: dappier
tags:
- Company
- Artificial Intelligence
- Advertising
- Monetization
- Publishers
website: https://dappier.com/
---
