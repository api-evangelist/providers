---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 67.1
  scored_at: '2026-10-17'
api_count: 1
apis:
- baseURL: https://api.arcmira.com
  baseurl_source: declared
  description: The Channels API from Arcmira — 2 operation(s) for channels.
  name: Arcmira Channels API
  slug: arcmira-channels-api
- baseURL: https://api.arcmira.com
  baseurl_source: declared
  description: The Entities API from Arcmira — 3 operation(s) for entities.
  name: Arcmira Entities API
  slug: arcmira-entities-api
- baseURL: https://api.arcmira.com
  baseurl_source: declared
  description: The Feedback API from Arcmira — 2 operation(s) for feedback.
  name: Arcmira Feedback API
  slug: arcmira-feedback-api
- baseURL: https://api.arcmira.com
  baseurl_source: declared
  description: The Mentions API from Arcmira — 2 operation(s) for mentions.
  name: Arcmira Mentions API
  slug: arcmira-mentions-api
- baseURL: https://api.arcmira.com
  baseurl_source: declared
  description: The Meta API from Arcmira — 6 operation(s) for meta.
  name: Arcmira Meta API
  slug: arcmira-meta-api
- baseURL: https://api.arcmira.com
  baseurl_source: declared
  description: The Monitors API from Arcmira — 7 operation(s) for monitors.
  name: Arcmira Monitors API
  slug: arcmira-monitors-api
- baseURL: https://api.arcmira.com
  baseurl_source: declared
  description: The Recommendations API from Arcmira — 2 operation(s) for recommendations.
  name: Arcmira Recommendations API
  slug: arcmira-recommendations-api
- baseURL: https://api.arcmira.com
  baseurl_source: declared
  description: The Search API from Arcmira — 1 operation(s) for search.
  name: Arcmira Search API
  slug: arcmira-search-api
- baseURL: https://api.arcmira.com
  baseurl_source: declared
  description: The Trackers API from Arcmira — 3 operation(s) for trackers.
  name: Arcmira Trackers API
  slug: arcmira-trackers-api
- baseURL: https://api.arcmira.com
  baseurl_source: declared
  description: The Transcriptions API from Arcmira — 1 operation(s) for transcriptions.
  name: Arcmira Transcriptions API
  slug: arcmira-transcriptions-api
- baseURL: https://api.arcmira.com
  baseurl_source: declared
  description: The Transcripts API from Arcmira — 2 operation(s) for transcripts.
  name: Arcmira Transcripts API
  slug: arcmira-transcripts-api
artifact_total: 24
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/arcmira/refs/heads/main/plans/arcmira-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/arcmira-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/arcmira/refs/heads/main/rules/arcmira-rules.yml
  title: ''
  type: Spectral
  url: rules/arcmira-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/arcmira/refs/heads/main/json-ld/arcmira-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/arcmira-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/arcmira/refs/heads/main/vocabulary/arcmira-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/arcmira-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/arcmira/refs/heads/main/data-model/arcmira-data-model.yml
  title: ''
  type: DataModel
  url: data-model/arcmira-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/arcmira/refs/heads/main/cli/arcmira-cli.yml
  title: ''
  type: CLI
  url: cli/arcmira-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/arcmira/refs/heads/main/changelog/arcmira-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/arcmira-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/arcmira/refs/heads/main/conventions/arcmira-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/arcmira-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/arcmira/refs/heads/main/conventions/arcmira-conventions.yml
  title: ''
  type: Conventions
  url: conventions/arcmira-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arcmira/refs/heads/main/authentication/arcmira-authentication.yml
  title: ''
  type: Authentication
  url: authentication/arcmira-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/arcmira/refs/heads/main/errors/arcmira-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/arcmira-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/arcmira/refs/heads/main/conformance/arcmira-conformance.yml
  title: ''
  type: Conformance
  url: conformance/arcmira-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arcmira/refs/heads/main/llms/arcmira-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arcmira-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arcmira/refs/heads/main/a2a/arcmira-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/arcmira-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arcmira/refs/heads/main/well-known/arcmira-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arcmira-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arcmira/refs/heads/main/hosts/arcmira-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arcmira-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arcmira/refs/heads/main/vendors/arcmira-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arcmira-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/arcmira/refs/heads/main/packages/arcmira-packages.yml
  title: ''
  type: SDKs
  url: packages/arcmira-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/arcmira/refs/heads/main/packages/arcmira-packages.yml
  title: ''
  type: Packages
  url: packages/arcmira-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arcmira.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arcmira.com/privacy
- group: start
  title: ''
  type: Login
  url: https://arcmira.com/sign-in
- group: operate
  title: ''
  type: ChangeLog
  url: https://arcmira.com/docs/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://arcmira.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://arcmira.com/agent-setup
- group: start
  title: ''
  type: DeveloperPortal
  url: https://arcmira.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://arcmira.com/docs/api-reference/search/retrieve-spoken-transcript-slices-for-one-topic
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/arcmira
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arcmira/refs/heads/main/security/arcmira-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arcmira-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arcmira.com
- group: docs
  title: ''
  type: Documentation
  url: https://arcmira.com/docs
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arcmira/refs/heads/main/mcp/arcmira-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/arcmira-mcp.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.arcmira.com/mcp
- group: agent
  title: ''
  type: MCPServerCard
  url: https://mcp.arcmira.com/.well-known/mcp/server-card.json
- group: auth
  title: ''
  type: OAuthProtectedResource
  url: https://mcp.arcmira.com/.well-known/oauth-protected-resource
- group: agent
  title: ''
  type: MCPServer
  url: https://arcmira.com/docs/mcp
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arcmira/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: Documentation
  url: https://arcmira.com/docs/usage-and-billing
- group: docs
  title: ''
  type: OpenAPI
  url: https://api.arcmira.com/v1/openapi.json
created: '2026-10-03'
description: Arcmira provides AI-powered search of YouTube transcript data, enabling developers to retrieve timestamped passages, speaker mentions, sponsors, and ad reads. Their platform offers JavaScript and Python SDKs, a CLI, and an OAuth-enabled remote MCP for integrating spoken web insights into applications. The service includes monitoring capabilities and commercial intelligence features, targeting developers building conversational AI and analytics tools.
image: https://arcmira.com/arcmira-cover.png?v=20261002
json_schemas:
- name: ChannelSponsorsResponse
  property_count: 4
  slug: arcmira-channel-sponsors-response
- name: EntityMomentumResponse
  property_count: 9
  slug: arcmira-entity-momentum-response
- name: MeResponse
  property_count: 12
  slug: arcmira-me-response
- name: MentionCountsResponse
  property_count: 10
  slug: arcmira-mention-counts-response
- name: TranscriptResponse
  property_count: 16
  slug: arcmira-transcript-response
- name: TranscriptSearchResponse
  property_count: 13
  slug: arcmira-transcript-search-response
jsonld:
- class_count: 68
  name: Arcmira Context
  property_count: 249
  slug: arcmira-context
layout: provider
mcp_servers:
- description: 'Arcmira runs two remote MCP servers. The research server "Arcmira: YouTube Transcript Search" (io.github.arcmira/arcmira, version 0.10.4) is at https://mcp.arcmira.com/mcp over Streamable HTTP and req'
  name: Arcmira MCP Server
  slug: io-github-arcmira-arcmira
- description: ''
  name: Arcmira documentation MCP server (public)
  slug: arcmira-documentation-mcp-server-public
modified: '2026-10-05'
name: Arcmira
nav: Providers
network: true
overview: 'Arcmira publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Channels API, Entities API, Feedback API, and 8 more. Tagged areas include Artificial Intelligence, Search, YouTube, Transcripts, and SDK.


  The Arcmira catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Arcmira''s developer surface includes CLI, changelog, authentication, pricing, getting-started guide, API reference, documentation, and 32 more developer resources.'
plans:
- name: Arcmira Plans Pricing
  plan_count: 5
  slug: arcmira-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Arcmira API Rules
  rule_count: 18
  severity_counts:
    error: 12
    hint: 0
    info: 3
    warn: 3
  slug: arcmira-rules
score:
  band: strong
  composite: 64.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.8
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 70.3
    developer_ergonomics: 71.4
    discoverability: 75.0
    operational_transparency: 21.1
  previous_composite: 68.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 38.9
screenshot: https://raw.githubusercontent.com/api-evangelist/arcmira/refs/heads/main/screenshots/arcmira-2026-10-11T100202.png
security:
- kind: authentication
  name: Arcmira Authentication
  slug: arcmira-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Arcmira Domain Security
  slug: arcmira-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: arcmira
tags:
- Artificial Intelligence
- Search
- YouTube
- Transcripts
- SDK
website: https://arcmira.com
---
