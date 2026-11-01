---
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'mcpservers.org API as documented publicly: 15 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: mcpservers.org API
  slug: mcpservers-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/mcpservers/rules/mcpservers-rules.yml
  title: ''
  type: Spectral
  url: rules/mcpservers-rules.yml
- group: design
  href: https://artifacts.apis.io/mcpservers/json-ld/mcpservers-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mcpservers-context.jsonld
- group: design
  href: https://artifacts.apis.io/mcpservers/vocabulary/mcpservers-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mcpservers-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/mcpservers/data-model/mcpservers-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mcpservers-data-model.yml
- group: design
  href: https://artifacts.apis.io/mcpservers/conformance/mcpservers-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mcpservers-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mcpservers/llms/mcpservers-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mcpservers-llms.txt
- group: other
  href: https://artifacts.apis.io/mcpservers/hosts/mcpservers-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mcpservers-hosts.yml
- group: other
  href: https://artifacts.apis.io/mcpservers/vendors/mcpservers-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mcpservers-vendors.yml
- group: auth
  href: https://artifacts.apis.io/mcpservers/security/mcpservers-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mcpservers-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mcpservers.org/
- group: company
  title: ''
  type: Blog
  url: https://blog.mcpservers.org/
- group: docs
  title: ''
  type: Documentation
  url: https://mcpservers.org/remote-mcp-servers
created: '2026-10-18'
description: MCP Servers (mcpservers.org) provides a curated marketplace of Model Context Protocol (MCP) servers that enable AI agents to interact with a wide range of tools and services. The site lists official and community‑run MCP integrations for productivity, development, data access, web scraping, cloud services, and more, each with documentation and quick‑start guides. It serves as a hub for agents to discover, connect, and leverage specialized MCP servers across domains such as finance, design, communication, and storage, facilitating seamless tool integration for large language models.
image: https://mcpservers.org/api/og?template=grid&title=Awesome+MCP+Servers&description=Explore+9%2C800%2B+official+and+community+MCP+servers+for+Claude%2C+Codex%2C+Cursor%2C+and+other+AI+agents.+Find+the+right+tools+and+setup+guides...
json_schemas:
- name: PatchV1PagesPageidMarkdownRequest
  property_count: 2
  slug: mcpservers-patch-v1-pages-pageid-markdown-request
- name: PostApiDestinationsIdVerifyRequest
  property_count: 1
  slug: mcpservers-post-api-destinations-id-verify-request
- name: PostMcpRequest
  property_count: 4
  slug: mcpservers-post-mcp-request
- name: PostV1PostsRequest
  property_count: 9
  slug: mcpservers-post-v1-posts-request
- name: PostV1PostsResponse
  property_count: 3
  slug: mcpservers-post-v1-posts-response
- name: PostV1PostsValidateRequest
  property_count: 8
  slug: mcpservers-post-v1-posts-validate-request
jsonld:
- class_count: 9
  name: Mcpservers Context
  property_count: 22
  slug: mcpservers-context
layout: provider
modified: '2026-10-18'
name: mcpservers.org
nav: Providers
network: true
overview: 'mcpservers.org is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Marketplace, Integration, and Tools.


  The mcpservers.org catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  mcpservers.org''s developer surface includes engineering blog, documentation, and 10 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: mcpservers.org API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 1
  slug: mcpservers-rules
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 13
      marker_coverage: 100.0
      total: 13
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mcpservers Domain Security
  slug: mcpservers-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mcpservers
tags:
- Company
- Artificial Intelligence
- Marketplace
- Integration
- Tools
website: https://mcpservers.org/
---
