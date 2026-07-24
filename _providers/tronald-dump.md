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
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Tronald Dump Agentic Access
  operation_count: 9
  slug: tronald-dump-agentic-access
  summary_line: 9 operations
api_count: 4
apis:
- description: Look up the author records attached to quotes.
  name: Tronald Dump Authors API
  slug: tronald-dump-authors-api
- description: Retrieve Donald Trump quotes individually, randomly, or via full text search.
  name: Tronald Dump Quotes API
  slug: tronald-dump-quotes-api
- description: Look up the source documents (tweets, transcripts, articles) attached to quotes.
  name: Tronald Dump Sources API
  slug: tronald-dump-sources-api
- description: Browse the controlled vocabulary of tags attached to quotes.
  name: Tronald Dump Tags API
  slug: tronald-dump-tags-api
artifact_total: 34
collections:
- collection_type: open
  name: Tronald Dump Quotes API
  slug: open-tronald-dump-quotes
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tronald-dump-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tronald-dump-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tronalddump.io/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: build
  title: Original Author (Marcel Wijnker)
  type: SourceCode
  url: https://github.com/wickedest
- group: build
  title: Original Node.js Client (tronalddump-io/client-nodejs)
  type: SourceCode
  url: https://github.com/tronalddump-io/client-nodejs
- group: build
  title: TypeScript SDK (voxgig)
  type: SDKs
  url: https://github.com/voxgig-sdk/tronalddump-sdk/tree/main/ts
- group: build
  title: Python SDK (voxgig)
  type: SDKs
  url: https://github.com/voxgig-sdk/tronalddump-sdk/tree/main/py
- group: build
  title: Go SDK (voxgig)
  type: SDKs
  url: https://github.com/voxgig-sdk/tronalddump-sdk/tree/main/go
- group: build
  title: Ruby SDK (voxgig)
  type: SDKs
  url: https://github.com/voxgig-sdk/tronalddump-sdk/tree/main/rb
- group: build
  title: PHP SDK (voxgig)
  type: SDKs
  url: https://github.com/voxgig-sdk/tronalddump-sdk/tree/main/php
- group: build
  title: Lua SDK (voxgig)
  type: SDKs
  url: https://github.com/voxgig-sdk/tronalddump-sdk/tree/main/lua
- group: build
  title: Go CLI (voxgig)
  type: CLI
  url: https://github.com/voxgig-sdk/tronalddump-sdk/tree/main/go-cli
- group: build
  title: MCP Server (voxgig, Go)
  type: Tools
  url: https://github.com/voxgig-sdk/tronalddump-sdk/tree/main/go-mcp
- group: build
  title: Flutter Sample (RicardoBelchior)
  type: CodeExamples
  url: https://github.com/RicardoBelchior/TronaldDump
- group: build
  title: Android Sample (br00)
  type: CodeExamples
  url: https://github.com/br00/TronaldDump
- group: build
  title: SwiftUI Sample (simonschuhmacher)
  type: CodeExamples
  url: https://github.com/simonschuhmacher/tronald-swiftui
- group: build
  title: Mycroft Skill (krisgesling)
  type: CodeExamples
  url: https://github.com/krisgesling/tronald-dump-skill
- group: build
  title: Alexa Skill (Tonkpils)
  type: CodeExamples
  url: https://github.com/Tonkpils/tronalddump-alexa
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/tronald-dump-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tronald-dump-vocabulary.yaml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/tronald-dump-context.jsonld
created: '2026-05-28'
description: Tronald Dump is an open community REST API exposing a historical archive of Donald Trump quotes, with sources, authors, tags, and a search interface using HAL (Hypertext Application Language) JSON responses. The project was built by Marcel Wijnker (wickedest) and ran at tronalddump.io until the domain lapsed and the public service went offline; the data model, OpenAPI, and community SDKs survive in third-party repositories.
examples:
- key_count: 5
  name: Tronald Dump Author Example
  slug: tronald-dump-author-example
- key_count: 4
  name: Tronald Dump Author List Response Example
  slug: tronald-dump-author-list-response-example
- key_count: 8
  name: Tronald Dump Quote Example
  slug: tronald-dump-quote-example
- key_count: 4
  name: Tronald Dump Quote Search Response Example
  slug: tronald-dump-quote-search-response-example
- key_count: 6
  name: Tronald Dump Source Example
  slug: tronald-dump-source-example
- key_count: 4
  name: Tronald Dump Source List Response Example
  slug: tronald-dump-source-list-response-example
- key_count: 2
  name: Tronald Dump Tag Example
  slug: tronald-dump-tag-example
- key_count: 4
  name: Tronald Dump Tag List Response Example
  slug: tronald-dump-tag-list-response-example
image: https://raw.githubusercontent.com/api-evangelist/tronald-dump/refs/heads/main/apis.yml
json_schemas:
- name: AuthorListResponse
  property_count: 4
  slug: tronald-dump-author-list-response
- name: Author
  property_count: 5
  slug: tronald-dump-author
- name: Quote
  property_count: 8
  slug: tronald-dump-quote
- name: QuoteSearchResponse
  property_count: 4
  slug: tronald-dump-quote-search-response
- name: SourceListResponse
  property_count: 4
  slug: tronald-dump-source-list-response
- name: Source
  property_count: 6
  slug: tronald-dump-source
- name: TagListResponse
  property_count: 4
  slug: tronald-dump-tag-list-response
- name: Tag
  property_count: 2
  slug: tronald-dump-tag
json_structures:
- name: Tronald Dump Author List Response Structure
  property_count: 4
  slug: tronald-dump-author-list-response-structure
- name: Tronald Dump Author Structure
  property_count: 5
  slug: tronald-dump-author-structure
- name: Tronald Dump Quote Search Response Structure
  property_count: 4
  slug: tronald-dump-quote-search-response-structure
- name: Tronald Dump Quote Structure
  property_count: 8
  slug: tronald-dump-quote-structure
- name: Tronald Dump Source List Response Structure
  property_count: 4
  slug: tronald-dump-source-list-response-structure
- name: Tronald Dump Source Structure
  property_count: 6
  slug: tronald-dump-source-structure
- name: Tronald Dump Tag List Response Structure
  property_count: 4
  slug: tronald-dump-tag-list-response-structure
- name: Tronald Dump Tag Structure
  property_count: 2
  slug: tronald-dump-tag-structure
jsonld:
- class_count: 9
  name: Tronald Dump Context
  property_count: 15
  slug: tronald-dump-context
layout: provider
modified: '2026-05-30'
name: Tronald Dump
nav: Providers
network: true
overview: 'Tronald Dump publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authors API, Quotes API, Sources API, and 1 more. Tagged areas include Community, Games And Comics, Open Source, Politics, and Public APIs.


  The Tronald Dump catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tronald Dump''s developer surface includes CLI, tooling, code examples, and 19 more developer resources.'
random_paper: 15
rules:
- name: Tronald Dump API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tronald-dump-jsonschema-spectral-rules
- name: Tronald Dump API Rules
  rule_count: 51
  severity_counts:
    error: 20
    hint: 0
    info: 10
    warn: 21
  slug: tronald-dump-spectral-rules
score:
  band: thin
  composite: 37.9
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 65.5
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 86.8
    operational_transparency: 0.0
  previous_composite: 37.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tronald-dump/refs/heads/main/screenshots/tronald-dump-2026-06-20T195742.png
security:
- kind: domain-security
  name: Tronald Dump Domain Security
  slug: tronald-dump-domain-security
  summary_line: TLSv1.3
slug: tronald-dump
tags:
- Community
- Games And Comics
- Open Source
- Politics
- Public APIs
- Quotes
- Trump
website: https://www.tronalddump.io/
---
