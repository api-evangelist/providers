---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 46.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Automq Agentic Access
  operation_count: 10
  slug: automq-agentic-access
  summary_line: 10 operations
api_count: 1
apis:
- baseURL: https://www.automq.com
  baseurl_source: spec
  description: The Ai Info API from AutoMQ — 1 operation(s) for ai info.
  name: AutoMQ Ai Info API
  slug: automq-ai-info-api
- baseURL: https://www.automq.com
  baseurl_source: spec
  description: The Llms Full.txt API from AutoMQ — 1 operation(s) for llms full.txt.
  name: AutoMQ Llms Full.txt API
  slug: automq-llms-full-txt-api
- baseURL: https://www.automq.com
  baseurl_source: spec
  description: The Llms.txt API from AutoMQ — 1 operation(s) for llms.txt.
  name: AutoMQ Llms.txt API
  slug: automq-llms-txt-api
- baseURL: https://www.automq.com
  baseurl_source: spec
  description: The Robots.txt API from AutoMQ — 1 operation(s) for robots.txt.
  name: AutoMQ Robots.txt API
  slug: automq-robots-txt-api
- baseURL: https://www.automq.com
  baseurl_source: spec
  description: The .well Known API from AutoMQ — 6 operation(s) for .well known.
  name: AutoMQ .well Known API
  slug: automq-well-known-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/automq/plans/automq-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/automq-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/automq/agentic-access/automq-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/automq-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/automq/rules/automq-rules.yml
  title: ''
  type: Spectral
  url: rules/automq-rules.yml
- group: design
  href: https://artifacts.apis.io/automq/json-ld/automq-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/automq-context.jsonld
- group: design
  href: https://artifacts.apis.io/automq/vocabulary/automq-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/automq-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/automq/data-model/automq-data-model.yml
  title: ''
  type: DataModel
  url: data-model/automq-data-model.yml
- group: operate
  href: https://artifacts.apis.io/automq/changelog/automq-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/automq-changelog.yml
- group: design
  href: https://artifacts.apis.io/automq/conformance/automq-conformance.yml
  title: ''
  type: Conformance
  url: conformance/automq-conformance.yml
- group: agent
  href: https://artifacts.apis.io/automq/llms/automq-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/automq-llms.txt
- group: other
  href: https://artifacts.apis.io/automq/a2a/automq-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/automq-a2a.yml
- group: agent
  href: https://artifacts.apis.io/automq/mcp/automq-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/automq-mcp.yml
- group: agent
  href: https://artifacts.apis.io/automq/well-known/automq-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/automq-well-known.yml
- group: other
  href: https://artifacts.apis.io/automq/hosts/automq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/automq-hosts.yml
- group: other
  href: https://artifacts.apis.io/automq/vendors/automq-vendors.yml
  title: ''
  type: Vendors
  url: vendors/automq-vendors.yml
- group: build
  href: https://artifacts.apis.io/automq/packages/automq-packages.yml
  title: ''
  type: SDKs
  url: packages/automq-packages.yml
- group: build
  href: https://artifacts.apis.io/automq/packages/automq-packages.yml
  title: ''
  type: Packages
  url: packages/automq-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.automq.com/automq/getting-started/deploy-multi-nodes-test-cluster-on-docker
- group: auth
  href: https://artifacts.apis.io/automq/security/automq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/automq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.automq.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.automq.com
- group: company
  title: ''
  type: Blog
  url: https://www.automq.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AutoMQ
- group: commercial
  title: ''
  type: Pricing
  url: https://www.automq.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.automq.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.automq.com/terms-of-service
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.automq.com/automq/releases/release-notes.md
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.automq.com/
created: '2026-10-13'
description: AutoMQ is a cloud-native, Kafka-compatible streaming platform that replaces Kafka broker local disks with shared S3-compatible object storage, offered as open source and as AutoMQ Cloud (BYOC). Developers use the Kafka protocol directly; AutoMQ Cloud resources are managed through an official Terraform provider, and the company publishes a public discovery OpenAPI, llms.txt and a documentation MCP server.
finops:
- has_sources: true
  method: derived
  name: Automq Finops
  primary_unit: gib
  service_category: ''
  slug: automq-finops
  template: false
image: https://www.automq.com/images/automq/og-image.webp
json_schemas:
- name: ApiCatalog
  property_count: 1
  slug: automq-api-catalog
- name: Status
  property_count: 4
  slug: automq-status
jsonld:
- class_count: 2
  name: Automq Context
  property_count: 5
  slug: automq-context
layout: provider
mcp_servers:
- description: 'Remote MCP server serving AutoMQ documentation search (tools/list answered without auth, 2026-10-13). It exposes documentation, not the AutoMQ Cloud control plane. The website also publishes a WebMCP '
  name: AutoMQ Documentation MCP Server
  slug: automq-documentation-mcp-server
modified: '2026-10-13'
name: AutoMQ
nav: Providers
network: true
overview: 'AutoMQ publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Ai Info API, Llms Full.txt API, Llms.txt API, and 2 more. Tagged areas include Company, Kafka, Streaming, Event Streaming, and Object Storage.


  The AutoMQ catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AutoMQ''s developer surface includes changelog, getting-started guide, documentation, engineering blog, pricing, and 22 more developer resources.'
plans:
- name: Automq Plans Pricing
  plan_count: 5
  slug: automq-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: AutoMQ API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: automq-rules
score:
  band: developing
  composite: 47.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 78.9
    contract_governance: 22.0
    contract_quality: 48.1
    developer_ergonomics: 31.0
    discoverability: 56.7
    operational_transparency: 21.1
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Automq Domain Security
  slug: automq-domain-security
  summary_line: TLSv1.3 · DMARC
slug: automq
tags:
- Company
- Kafka
- Streaming
- Event Streaming
- Object Storage
- Open Source
- Cloud
website: https://www.automq.com
---
