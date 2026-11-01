---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Deepdna Ai Agentic Access
  operation_count: 6
  slug: deepdna-ai-agentic-access
  summary_line: 6 operations
api_count: 2
apis:
- baseURL: https://deepdna.ai/api/v1
  baseurl_source: declared
  description: Live. Public, curated, cited. No key, no personal data, nothing stored.
  name: deepdna-ai Knowledge API
  slug: deepdna-ai-knowledge-api
artifact_total: 27
common:
- group: design
  href: https://artifacts.apis.io/deepdna-ai/data-model/deepdna-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/deepdna-ai-data-model.yml
- group: agent
  href: https://artifacts.apis.io/deepdna-ai/agentic-access/deepdna-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/deepdna-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/deepdna-ai/rules/deepdna-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/deepdna-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/deepdna-ai/vocabulary/deepdna-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/deepdna-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/deepdna-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/deepdna-ai/errors/deepdna-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/deepdna-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/deepdna-ai/conformance/deepdna-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/deepdna-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/deepdna-ai/llms/deepdna-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deepdna-ai-llms.txt
- group: build
  href: https://artifacts.apis.io/deepdna-ai/mcp/deepdna-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/deepdna-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/deepdna-ai/mcp/deepdna-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/deepdna-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/deepdna-ai/hosts/deepdna-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deepdna-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/deepdna-ai/vendors/deepdna-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deepdna-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/deepdna-ai/packages/deepdna-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/deepdna-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/deepdna-ai/packages/deepdna-ai-packages.yml
  title: ''
  type: Packages
  url: packages/deepdna-ai-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://deepdna.ai/changelog/
- group: auth
  href: https://artifacts.apis.io/deepdna-ai/security/deepdna-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deepdna-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deepdna.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://deepdna.ai/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://deepdna.ai/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://deepdna.ai/docs/
- group: operate
  title: ''
  type: Support
  url: https://deepdna.ai/privacy/
- group: company
  title: ''
  type: Blog
  url: https://deepdna.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alfonsoguv
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deepdna.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deepdna.ai/privacy/
created: '2026-10-30'
description: DeepDNA provides a free pharmacogenomics MCP (Machine-Readable Clinical) server for AI agents, offering curated, cited drug‑gene interaction knowledge from CPIC and DPWG guidelines. The service returns read‑only tools such as check_medications, lookup_drug_gene, lookup_gene, lookup_variant, and list_genes, each with source citations. No API key is required, and the platform supports integration with Claude, ChatGPT, Cursor, and VS Code. Data is sourced from public genomic databases and includes 16 genes and 83 drug‑gene pairs, with detailed references to guidelines, literature, and FDA labels.
image: https://deepdna.ai/og/home.png
json_schemas:
- name: Discovery
  property_count: 0
  slug: deepdna-ai-discovery
- name: GeneRef
  property_count: 0
  slug: deepdna-ai-gene-ref
- name: Gene
  property_count: 0
  slug: deepdna-ai-gene
- name: GeneSummary
  property_count: 0
  slug: deepdna-ai-gene-summary
- name: GetGenesResponse
  property_count: 2
  slug: deepdna-ai-get-genes-response
- name: GetGenesSymbolResponse
  property_count: 7
  slug: deepdna-ai-get-genes-symbol-response
- name: GetPgxGeneDrugResponse
  property_count: 5
  slug: deepdna-ai-get-pgx-gene-drug-response
- name: GetPgxGeneResponse
  property_count: 2
  slug: deepdna-ai-get-pgx-gene-response
- name: GetVariantsRsidResponse
  property_count: 11
  slug: deepdna-ai-get-variants-rsid-response
- name: Meta
  property_count: 0
  slug: deepdna-ai-meta
- name: PgxPair
  property_count: 0
  slug: deepdna-ai-pgx-pair
jsonld:
- class_count: 5
  name: Deepdna Ai Context
  property_count: 17
  slug: deepdna-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at deepdna.ai.
  name: deepdna-ai MCP Server
  slug: deepdna-ai-mcp-yml
modified: '2026-10-30'
name: deepdna-ai
nav: Providers
network: true
overview: 'deepdna-ai publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Knowledge API. Tagged areas include Company, Pharmacogenomics, MCP, AI-agents, and Genomics.


  The deepdna-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  deepdna-ai''s developer surface includes changelog, documentation, API reference, getting-started guide, support, engineering blog, and 19 more developer resources.'
plans:
- name: Deepdna Ai Plans Pricing
  plan_count: 0
  slug: deepdna-ai-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Deepdna Ai Rate Limits
  slug: deepdna-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: deepdna-ai API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: deepdna-ai-rules
scopes:
- name: Deepdna Ai Scopes
  scope_count: 0
  slug: deepdna-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 27
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 25.5
    developer_ergonomics: 49.3
    discoverability: 65.0
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 16.7
      derived: 5
      marker_coverage: 83.3
      total: 6
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 28.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Deepdna Ai Authentication
  slug: deepdna-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Deepdna Ai Domain Security
  slug: deepdna-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 6
skills:
- name: gene-lookup
  slug: deepdna-ai-gene-lookup
- name: get-gene
  slug: deepdna-ai-get-gene
- name: get-pgx
  slug: deepdna-ai-get-pgx
- name: get-variant
  slug: deepdna-ai-get-variant
- name: list-genes
  slug: deepdna-ai-list-genes
- name: list-pgx
  slug: deepdna-ai-list-pgx
slug: deepdna-ai
tags:
- Company
- Pharmacogenomics
- MCP
- AI-agents
- Genomics
- Healthcare
website: https://deepdna.ai/
---
