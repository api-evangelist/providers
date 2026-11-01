---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Se Ranking Agentic Access
  operation_count: 86
  slug: se-ranking-agentic-access
  summary_line: 86 operations · 27 acting
api_count: 1
apis:
- description: REST API providing access to SE Ranking's SEO datasets including keyword research, backlink analysis, domain analysis, SERP data, website audits, and AI search visibility tracking. Uses a credit-based
  name: SE Ranking Data API
  slug: data-api
- description: 'REST API for creating and managing SEO tracking projects programmatically, including keyword monitoring, competitor tracking, website audits, backlink management, and account administration. Consumes '
  name: SE Ranking Project API
  slug: project-api
- baseURL: https://api.seranking.com
  baseurl_source: declared
  description: This collection contains endpoints for retrieving information about your account status, subscription details, and current credit and API unit balances. Use these requests to monitor your usage and pl
  name: SE Ranking Account & system API
  slug: se-ranking-account-system-api
- baseURL: https://api.seranking.com
  baseurl_source: declared
  description: 'This collection of endpoints allows you to analyze a domain or brand''s visibility and performance within various Large Language Model (LLM) results, such as ChatGPT, Gemini, and Perplexity. Use these '
  name: SE Ranking AI search API
  slug: se-ranking-ai-search-api
- baseURL: https://api.seranking.com
  baseurl_source: declared
  description: '# Backlinks API This collection of requests allows you to conduct a comprehensive analysis of the backlink profile for any given target, whether it''s a root domain, a specific host (subdomain), or a p'
  name: SE Ranking Backlinks API
  slug: se-ranking-backlinks-api
- baseURL: https://api.seranking.com
  baseurl_source: declared
  description: This collection of endpoints allows you to perform in-depth competitive analysis on any domain. Use these requests to uncover keyword strategies, traffic trends, and competitor performance in both org
  name: SE Ranking Domain Analysis API
  slug: se-ranking-domain-analysis-api
- baseURL: https://api.seranking.com
  baseurl_source: declared
  description: This collection of endpoints is designed for comprehensive keyword analysis and discovery. Use these requests to retrieve performance metrics for large lists of keywords or to generate new keyword ide
  name: SE Ranking Keyword Research API
  slug: se-ranking-keyword-research-api
- baseURL: https://api.seranking.com
  baseurl_source: declared
  description: The SERP Results > classic API from SE Ranking — 4 operation(s) for serp results > classic.
  name: SE Ranking SERP Results > classic API
  slug: se-ranking-serp-results-classic-api
- baseURL: https://api.seranking.com
  baseurl_source: declared
  description: 'This collection of endpoints provides a comprehensive suite of tools to programmatically manage the full lifecycle of your technical SEO audits. These requests allow you to launch new crawls, monitor '
  name: SE Ranking Website Audit API
  slug: se-ranking-website-audit-api
- description: 'Hosted remote Model Context Protocol server exposing 217 tools and 5 prompts across three SE Ranking surfaces: the credit-billed Data API (66 DATA_* tools, backed 1:1 by the published OpenAPI), the Pr'
  name: SE Ranking MCP Server
  slug: mcp-server
artifact_total: 61
collections:
- collection_type: open
  name: SE Ranking Data Account & system API
  slug: open-se-ranking-account-system-api
- collection_type: open
  name: SE Ranking Data Account & system AI search API
  slug: open-se-ranking-ai-search-api
- collection_type: open
  name: SE Ranking Data Account & system backlinks API
  slug: open-se-ranking-backlinks-api
- collection_type: open
  name: SE Ranking Data Account & system Domain Analysis API
  slug: open-se-ranking-domain-analysis-api
- collection_type: open
  name: SE Ranking Data Account & system Keyword Research API
  slug: open-se-ranking-keyword-research-api
- collection_type: open
  name: SE Ranking Data Account & system SERP Results > classic API
  slug: open-se-ranking-serp-results-classic-api
- collection_type: open
  name: SE Ranking Data Account & system Website Audit API
  slug: open-se-ranking-website-audit-api
common:
- group: other
  href: https://artifacts.apis.io/se-ranking/capabilities/se-ranking-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/se-ranking-capability-edges.yml
- group: commercial
  title: ''
  type: License
  url: https://github.com/seranking/openapi/blob/main/LICENSE
- group: docs
  href: https://artifacts.apis.io/se-ranking/openapi/_original/se-ranking-data-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/se-ranking-data-api-openapi.yml
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/seranking/openapi
- group: agent
  href: https://artifacts.apis.io/se-ranking/mcp/se-ranking-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/se-ranking-mcp.yml
- group: build
  href: https://artifacts.apis.io/se-ranking/mcp/se-ranking-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/se-ranking-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/se-ranking/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/se-ranking/well-known/se-ranking-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/se-ranking-well-known.yml
- group: auth
  href: https://artifacts.apis.io/se-ranking/scopes/se-ranking-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/se-ranking-scopes.yml
- group: design
  href: https://artifacts.apis.io/se-ranking/conventions/se-ranking-conventions.yml
  title: ''
  type: Conventions
  url: conventions/se-ranking-conventions.yml
- group: design
  href: https://artifacts.apis.io/se-ranking/errors/se-ranking-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/se-ranking-problem-types.yml
- group: design
  href: https://artifacts.apis.io/se-ranking/lifecycle/se-ranking-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/se-ranking-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/se-ranking/conformance/se-ranking-conformance.yml
  title: ''
  type: Conformance
  url: conformance/se-ranking-conformance.yml
- group: design
  href: https://artifacts.apis.io/se-ranking/data-model/se-ranking-data-model.yml
  title: ''
  type: DataModel
  url: data-model/se-ranking-data-model.yml
- group: build
  href: https://artifacts.apis.io/se-ranking/packages/se-ranking-packages.yml
  title: ''
  type: Packages
  url: packages/se-ranking-packages.yml
- group: operate
  href: https://artifacts.apis.io/se-ranking/changelog/se-ranking-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/se-ranking-changelog.yml
- group: agent
  href: https://artifacts.apis.io/se-ranking/llms/se-ranking-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/se-ranking-llms.txt
- group: agent
  href: https://artifacts.apis.io/se-ranking/agentic-access/se-ranking-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/se-ranking-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/se-ranking/security/se-ranking-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/se-ranking-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/se-ranking/authentication/se-ranking-authentication.yml
  title: ''
  type: Authentication
  url: authentication/se-ranking-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://seranking.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://seranking.com/api.html
- group: docs
  title: ''
  type: Documentation
  url: https://seranking.com/api.html
- group: docs
  title: ''
  type: APIReference
  url: https://seranking.com/api/data/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://seranking.com/api/data/getting-started/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/serankingdev/se-ranking-developers/overview
- group: operate
  title: ''
  type: Support
  url: https://seranking.com/contact.html
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/seranking
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/seranking
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/se-ranking
- group: other
  title: ''
  type: X
  url: https://x.com/SERanking
- group: company
  title: ''
  type: Blog
  url: https://seranking.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://seranking.com/api-pricing.html
- group: start
  title: ''
  type: SignUp
  url: https://seranking.com/sign-up.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://seranking.com/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://seranking.com/privacy-policy.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.seranking.com
- group: commercial
  href: https://artifacts.apis.io/se-ranking/plans/se-ranking-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/se-ranking-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/se-ranking/rate-limits/se-ranking-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/se-ranking-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/se-ranking/finops/se-ranking-finops.yml
  title: ''
  type: FinOps
  url: finops/se-ranking-finops.yml
created: '2026-06-13'
description: SE Ranking is an SEO platform providing a REST API for keyword rank tracking, competitor analysis, backlink monitoring, on-page auditing, AI search visibility, and generating white-label SEO reports. The platform offers two API layers — a Data API with pay-as-you-go credits for SEO data retrieval and a Project API for managing SEO workflows — covering 5.4B keywords, 2.2B domain profiles, and 188+ regions.
examples:
- key_count: 3
  name: Se Ranking Ai Search Example
  slug: se-ranking-ai-search-example
- key_count: 3
  name: Se Ranking Backlink Summary Example
  slug: se-ranking-backlink-summary-example
- key_count: 3
  name: Se Ranking Domain Overview Example
  slug: se-ranking-domain-overview-example
- key_count: 3
  name: Se Ranking Keyword Research Example
  slug: se-ranking-keyword-research-example
- key_count: 2
  name: Se Ranking Site Audit Example
  slug: se-ranking-site-audit-example
finops:
- has_sources: true
  method: derived
  name: Se Ranking Finops
  primary_unit: credits
  service_category: ''
  slug: se-ranking-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/se-ranking.png
json_schemas:
- name: SE Ranking AI Search Visibility
  property_count: 9
  slug: se-ranking-ai-search
- name: SE Ranking Backlink Summary
  property_count: 14
  slug: se-ranking-backlink-summary
- name: SE Ranking Domain Overview
  property_count: 12
  slug: se-ranking-domain-overview
- name: SE Ranking Keyword Research Result
  property_count: 11
  slug: se-ranking-keyword-research
jsonld:
- class_count: 0
  name: Se Ranking Context
  property_count: 42
  slug: se-ranking-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.seranking.com over streamable HTTP requiring OAuth; 217 tools listed.
  name: SE Ranking MCP Server
  slug: se-ranking
modified: '2026-08-13'
name: SE Ranking
nav: Providers
network: true
overview: 'SE Ranking publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Data API, Project API, Account & system API, and 7 more. Tagged areas include SEO, Keyword Research, Rank Tracking, Backlinks, and Competitor Analysis.


  The SE Ranking catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SE Ranking''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 33 more developer resources.'
plans:
- name: Se Ranking Plans Pricing
  plan_count: 5
  slug: se-ranking-plans-pricing
- name: Se Ranking Price Estimates
  plan_count: 0
  slug: se-ranking-price-estimates
random_paper: 23
rate_limits:
- limit_count: 6
  name: Se Ranking Rate Limits
  slug: se-ranking-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: SE Ranking — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: se-ranking-jsonschema-spectral-rules
scopes:
- name: Se Ranking Scopes
  scope_count: 1
  slug: se-ranking-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 64.1
  coverage:
    artifact_dirs: 31
    catalog_earned: 75.3
    catalog_earned_first_party: 24.0
    catalog_gap: 39.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 84.2
    contract_governance: 14.4
    contract_quality: 53.8
    developer_ergonomics: 69.0
    discoverability: 65.0
    operational_transparency: 68.4
  previous_composite: 62.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/se-ranking/se-ranking-2026-06-20T193611.png
security:
- kind: authentication
  name: Se Ranking Authentication
  slug: se-ranking-authentication
  summary_line: apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Se Ranking Domain Security
  slug: se-ranking-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 32
skills:
- name: ai-search-gaps-to-social-campaign
  slug: se-ranking-ai-search-gaps-to-social-campaign
- name: client-onboarding-proposal
  slug: se-ranking-client-onboarding-proposal
- name: local-gmb-visibility
  slug: se-ranking-local-gmb-visibility
- name: seo-ads
  slug: se-ranking-seo-ads
- name: seo-agency-landing-page
  slug: se-ranking-seo-agency-landing-page
- name: seo-ai-search-share-of-voice
  slug: se-ranking-seo-ai-search-share-of-voice
- name: seo-ai-social-report
  slug: se-ranking-seo-ai-social-report
- name: seo-api
  slug: se-ranking-seo-api
- name: seo-backlink-gap
  slug: se-ranking-seo-backlink-gap
- name: seo-backlinks-profile
  slug: se-ranking-seo-backlinks-profile
- name: seo-competitor-gap-analysis
  slug: se-ranking-seo-competitor-gap-analysis
- name: seo-competitor-pages
  slug: se-ranking-seo-competitor-pages
- name: seo-content-audit
  slug: se-ranking-seo-content-audit
- name: seo-content-brief
  slug: se-ranking-seo-content-brief
- name: seo-drift
  slug: se-ranking-seo-drift
- name: seo-firecrawl
  slug: se-ranking-seo-firecrawl
- name: seo-gaps-to-social-campaign
  slug: se-ranking-seo-gaps-to-social-campaign
- name: seo-geo
  slug: se-ranking-seo-geo
- name: seo-google
  slug: se-ranking-seo-google
- name: seo-hreflang
  slug: se-ranking-seo-hreflang
- name: seo-images
  slug: se-ranking-seo-images
- name: seo-keyword-cluster
  slug: se-ranking-seo-keyword-cluster
- name: seo-keyword-niche
  slug: se-ranking-seo-keyword-niche
- name: seo-local
  slug: se-ranking-seo-local
slug: se-ranking
tags:
- SEO
- Keyword Research
- Rank Tracking
- Backlinks
- Competitor Analysis
- Website Audit
- AI Search
- Geo
- Digital Marketing
- MCP
- AI Agents
- Agent Skills
website: https://seranking.com
---
