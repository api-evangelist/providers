---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.6
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Spyfu Agentic Access
  operation_count: 48
  slug: spyfu-agentic-access
  summary_line: 48 operations · 1 acting
api_count: 9
apis:
- description: The Account API API from SpyFu — 3 operation(s) for account api.
  name: SpyFu Account API API
  slug: spyfu-account-api-api
- description: The Ad History Research API API from SpyFu — 3 operation(s) for ad history research api.
  name: SpyFu Ad History Research API API
  slug: spyfu-ad-history-research-api-api
- description: The Competitors API API from SpyFu — 3 operation(s) for competitors api.
  name: SpyFu Competitors API API
  slug: spyfu-competitors-api-api
- description: The Domain Stats API API from SpyFu — 6 operation(s) for domain stats api.
  name: SpyFu Domain Stats API API
  slug: spyfu-domain-stats-api-api
- description: The Keyword Research API API from SpyFu — 7 operation(s) for keyword research api.
  name: SpyFu Keyword Research API API
  slug: spyfu-keyword-research-api-api
- description: The Kombat API API from SpyFu — 2 operation(s) for kombat api.
  name: SpyFu Kombat API API
  slug: spyfu-kombat-api-api
- description: The PPC Research API API from SpyFu — 3 operation(s) for ppc research api.
  name: SpyFu PPC Research API API
  slug: spyfu-ppc-research-api-api
- description: The Ranking History API API from SpyFu — 3 operation(s) for ranking history api.
  name: SpyFu Ranking History API API
  slug: spyfu-ranking-history-api-api
- description: The SEO Research API API from SpyFu — 17 operation(s) for seo research api.
  name: SpyFu SEO Research API API
  slug: spyfu-seo-research-api-api
artifact_total: 47
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Account Account API API
  slug: open-spyfu-account-api-api
- collection_type: open
  name: Account Account API Ad History Research API API
  slug: open-spyfu-ad-history-research-api-api
- collection_type: open
  name: Account Account API Competitors API API
  slug: open-spyfu-competitors-api-api
- collection_type: open
  name: Account Account API Domain Stats API API
  slug: open-spyfu-domain-stats-api-api
- collection_type: open
  name: Account Account API Keyword Research API API
  slug: open-spyfu-keyword-research-api-api
- collection_type: open
  name: Account Account API Kombat API API
  slug: open-spyfu-kombat-api-api
- collection_type: open
  name: Account Account API PPC Research API API
  slug: open-spyfu-ppc-research-api-api
- collection_type: open
  name: Account Account API Ranking History API API
  slug: open-spyfu-ranking-history-api-api
- collection_type: open
  name: Account Account API SEO Research API API
  slug: open-spyfu-seo-research-api-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spyfu-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spyfu-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spyfu-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.spyfu.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.spyfu.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/spyfu
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spyfu
- group: other
  title: ''
  type: X
  url: https://x.com/spyfu
- group: company
  title: ''
  type: Blog
  url: https://www.spyfu.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.spyfu.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/spyfu-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spyfu-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/spyfu-finops.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spyfu-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/spyfu-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/spyfu-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/spyfu-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/spyfu-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/spyfu-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spyfu-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spyfu-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/spyfu-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spyfu-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/spyfu-changelog.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/spyfu-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/spyfu-jsonschema-spectral-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/spyfu-context.jsonld
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.spyfu.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.spyfu.com/reference
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.spyfu.com/en/articles/5640863-what-s-new-on-spyfu
- group: operate
  title: ''
  type: Support
  url: https://help.spyfu.com/en/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.spyfu.com/termsconditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.spyfu.com/privacypolicy
- group: start
  title: ''
  type: Login
  url: https://www.spyfu.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spyfu
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/spyfu/spyfu_api_docs
created: 2026-06-13
description: SpyFu is a competitive SEO and PPC intelligence platform that gives marketers and agencies programmatic access to competitor keyword rankings, ad history, backlinks, and domain performance data. The REST API covers eight research domains — Domain Stats, Ad History, PPC Research, SEO Research, Competitors, Kombat, Keyword Research, and Ranking History — and is indexed against 1.6 trillion search results, 8 billion keywords, and 152 million domains.
examples:
- key_count: 1
  name: Spyfu Ad History Examples
  slug: spyfu-ad-history-examples
- key_count: 1
  name: Spyfu Competitors Examples
  slug: spyfu-competitors-examples
- key_count: 1
  name: Spyfu Domain Stats Examples
  slug: spyfu-domain-stats-examples
- key_count: 1
  name: Spyfu Keyword Related Examples
  slug: spyfu-keyword-related-examples
- key_count: 1
  name: Spyfu Kombat Examples
  slug: spyfu-kombat-examples
- key_count: 1
  name: Spyfu Ppc Keyword Examples
  slug: spyfu-ppc-keyword-examples
- key_count: 1
  name: Spyfu Ppc Research Serp Examples
  slug: spyfu-ppc-research-serp-examples
- key_count: 1
  name: Spyfu Ranking History Examples
  slug: spyfu-ranking-history-examples
- key_count: 1
  name: Spyfu Seo Research Serp Examples
  slug: spyfu-seo-research-serp-examples
finops:
- name: Spyfu Finops
  service_category: ''
  slug: spyfu-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spyfu.png
json_schemas:
- name: SpyFu Account API Schemas
  property_count: 0
  slug: spyfu-account
- name: SpyFu Ad History API Schemas
  property_count: 0
  slug: spyfu-ad-history
- name: SpyFu Competitors API Schemas
  property_count: 0
  slug: spyfu-competitors
- name: SpyFu Domain Stats API Schemas
  property_count: 0
  slug: spyfu-domain-stats
- name: SpyFu Keyword API Schemas
  property_count: 0
  slug: spyfu-keyword-related
- name: SpyFu Kombat API Schemas
  property_count: 0
  slug: spyfu-kombat
- name: SpyFu PPC Research API Schemas
  property_count: 0
  slug: spyfu-ppc-keyword
- name: SpyFu PPC Research API Schemas
  property_count: 0
  slug: spyfu-ppc-research-serp
- name: SpyFu Ranking History API Schemas
  property_count: 0
  slug: spyfu-ranking-history
- name: SpyFu SEO Research API Schemas
  property_count: 0
  slug: spyfu-seo-research-serp
jsonld:
- class_count: 0
  name: Spyfu Context
  property_count: 23
  slug: spyfu-context
layout: provider
mcp_servers:
- description: SpyFu serves a remote Model Context Protocol endpoint from its own developer portal host at https://developer.spyfu.com/mcp. A GET returns HTTP 200 with the plain-text body "This URL can only be acces
  name: SpyFu MCP Server
  slug: spyfu-mcp-server
modified: 2026-08-13
name: SpyFu
nav: Providers
network: true
overview: 'SpyFu publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Account API API, Ad History Research API API, Competitors API API, and 6 more. Tagged areas include SEO, PPC, Competitive Intelligence, Keyword Research, and Ad History.


  The SpyFu catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SpyFu''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, API reference, support, and 30 more developer resources.'
plans:
- name: Spyfu Plans Pricing
  plan_count: 3
  slug: spyfu-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 9
  name: Spyfu Rate Limits
  slug: spyfu-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SpyFu API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: spyfu-jsonschema-spectral-rules
score:
  band: strong
  composite: 58.2
  delta: 0.0
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 41.7
    contract_quality: 65.0
    developer_ergonomics: 33.9
    discoverability: 81.5
    governance: 41.7
    operational_transparency: 50.0
  previous_composite: 58.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spyfu/refs/heads/main/screenshots/spyfu-2026-06-20T194429.png
security:
- kind: authentication
  name: Spyfu Authentication
  slug: spyfu-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Spyfu Domain Security
  slug: spyfu-domain-security
  summary_line: TLSv1.3 · DMARC
slug: spyfu
tags:
- SEO
- PPC
- Competitive Intelligence
- Keyword Research
- Ad History
- Backlinks
- Domain Analytics
- SERP
website: https://www.spyfu.com/
---
