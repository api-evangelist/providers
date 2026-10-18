---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 46.1
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Automq Agentic Access
  operation_count: 10
  slug: automq-agentic-access
  summary_line: 10 operations
api_count: 2
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
artifact_total: 12
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/automq/refs/heads/main/agentic-access/automq-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/automq-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/automq/refs/heads/main/rules/automq-rules.yml
  title: ''
  type: Spectral
  url: rules/automq-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/automq/refs/heads/main/json-ld/automq-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/automq-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/automq/refs/heads/main/vocabulary/automq-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/automq-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/automq/refs/heads/main/data-model/automq-data-model.yml
  title: ''
  type: DataModel
  url: data-model/automq-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/automq/refs/heads/main/changelog/automq-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/automq-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/automq/refs/heads/main/conformance/automq-conformance.yml
  title: ''
  type: Conformance
  url: conformance/automq-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/automq/refs/heads/main/llms/automq-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/automq-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/automq/refs/heads/main/a2a/automq-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/automq-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/automq/refs/heads/main/mcp/automq-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/automq-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/automq/refs/heads/main/well-known/automq-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/automq-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/automq/refs/heads/main/hosts/automq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/automq-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/automq/refs/heads/main/vendors/automq-vendors.yml
  title: ''
  type: Vendors
  url: vendors/automq-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/automq/refs/heads/main/packages/automq-packages.yml
  title: ''
  type: SDKs
  url: packages/automq-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/automq/refs/heads/main/packages/automq-packages.yml
  title: ''
  type: Packages
  url: packages/automq-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.automq.com/automq/getting-started/deploy-multi-nodes-test-cluster-on-docker
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/automq/refs/heads/main/security/automq-domain-security.yml
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


  AutoMQ''s developer surface includes changelog, getting-started guide, documentation, engineering blog, pricing, and 21 more developer resources.'
random_paper: 3
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
  composite: 40.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 39.5
    contract_governance: 22.0
    contract_quality: 48.1
    developer_ergonomics: 31.0
    discoverability: 66.7
    operational_transparency: 21.1
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
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
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
