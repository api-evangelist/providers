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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Se Ranking Agentic Access
  operation_count: 86
  slug: se-ranking-agentic-access
  summary_line: 86 operations · 28 acting
api_count: 9
apis:
- description: REST API providing access to SE Ranking's SEO datasets including keyword research, backlink analysis, domain analysis, SERP data, website audits, and AI search visibility tracking. Uses a credit-based
  name: SE Ranking Data API
  slug: data-api
- description: 'REST API for creating and managing SEO tracking projects programmatically, including keyword monitoring, competitor tracking, website audits, backlink management, and account administration. Consumes '
  name: SE Ranking Project API
  slug: project-api
- description: This collection contains endpoints for retrieving information about your account status, subscription details, and current credit and API unit balances. Use these requests to monitor your usage and pl
  name: SE Ranking Account & system API
  slug: se-ranking-account-system-api
- description: 'This collection of endpoints allows you to analyze a domain or brand''s visibility and performance within various Large Language Model (LLM) results, such as ChatGPT, Gemini, and Perplexity. Use these '
  name: SE Ranking AI search API
  slug: se-ranking-ai-search-api
- description: '# Backlinks API This collection of requests allows you to conduct a comprehensive analysis of the backlink profile for any given target, whether it''s a root domain, a specific host (subdomain), or a p'
  name: SE Ranking backlinks API
  slug: se-ranking-backlinks-api
- description: This collection of endpoints allows you to perform in-depth competitive analysis on any domain. Use these requests to uncover keyword strategies, traffic trends, and competitor performance in both org
  name: SE Ranking Domain Analysis API
  slug: se-ranking-domain-analysis-api
- description: This collection of endpoints is designed for comprehensive keyword analysis and discovery. Use these requests to retrieve performance metrics for large lists of keywords or to generate new keyword ide
  name: SE Ranking Keyword Research API
  slug: se-ranking-keyword-research-api
- description: The SERP Results > classic API from SE Ranking — 4 operation(s) for serp results > classic.
  name: SE Ranking SERP Results > classic API
  slug: se-ranking-serp-results-classic-api
- description: 'This collection of endpoints provides a comprehensive suite of tools to programmatically manage the full lifecycle of your technical SEO audits. These requests allow you to launch new crawls, monitor '
  name: SE Ranking Website Audit API
  slug: se-ranking-website-audit-api
artifact_total: 26
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/se-ranking-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/se-ranking-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/se-ranking-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://seranking.com
- group: docs
  title: ''
  type: Documentation
  url: https://seranking.com/api.html
- group: build
  title: ''
  type: GitHubOrg
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
- group: operate
  title: ''
  type: StatusPage
  url: https://status.seranking.com
- group: commercial
  title: ''
  type: Plans
  url: plans/se-ranking-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/se-ranking-rate-limits.yml
- group: commercial
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
- name: Se Ranking Finops
  service_category: ''
  slug: se-ranking-finops
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
modified: '2026-06-13'
name: SE Ranking
nav: Providers
network: true
overview: 'SE Ranking publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Data API, Project API, Account & system API, and 6 more. Tagged areas include SEO, Keyword Research, Rank Tracking, Backlinks, and Competitor Analysis.


  The SE Ranking catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SE Ranking''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Se Ranking Plans Pricing
  plan_count: 6
  slug: se-ranking-plans-pricing
random_paper: 79
rate_limits:
- limit_count: 6
  name: Se Ranking Rate Limits
  slug: se-ranking-rate-limits
rules:
- name: SE Ranking API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: se-ranking-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.8
  delta: -0.6
  facets:
    commercial_clarity: 50.0
    contract_quality: 64.9
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 52.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/se-ranking/refs/heads/main/screenshots/se-ranking-2026-06-20T193611.png
security:
- kind: authentication
  name: Se Ranking Authentication
  slug: se-ranking-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Se Ranking Domain Security
  slug: se-ranking-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: se-ranking
tags:
- SEO
- Keyword Research
- Rank Tracking
- Backlinks
- Competitor Analysis
- Website Audit
- AI Search
- GEO
- Digital Marketing
website: https://seranking.com
---
