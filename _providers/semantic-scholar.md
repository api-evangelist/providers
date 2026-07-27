---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
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
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Semantic Scholar Agentic Access
  operation_count: 20
  slug: semantic-scholar-agentic-access
  summary_line: 20 operations · 3 acting
api_count: 6
apis:
- description: The Author Data API from Semantic Scholar — 4 operation(s) for author data.
  name: Semantic Scholar Author Data API
  slug: semantic-scholar-author-data-api
- description: The Incremental Updates API from Semantic Scholar — 1 operation(s) for incremental updates.
  name: Semantic Scholar Incremental Updates API
  slug: semantic-scholar-incremental-updates-api
- description: The Paper Data API from Semantic Scholar — 9 operation(s) for paper data.
  name: Semantic Scholar Paper Data API
  slug: semantic-scholar-paper-data-api
- description: The Paper Recommendations API from Semantic Scholar — 2 operation(s) for paper recommendations.
  name: Semantic Scholar Paper Recommendations API
  slug: semantic-scholar-paper-recommendations-api
- description: The Release Data API from Semantic Scholar — 3 operation(s) for release data.
  name: Semantic Scholar Release Data API
  slug: semantic-scholar-release-data-api
- description: The Snippet Text API from Semantic Scholar — 1 operation(s) for snippet text.
  name: Semantic Scholar Snippet Text API
  slug: semantic-scholar-snippet-text-api
artifact_total: 21
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/semantic-scholar-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/semantic-scholar-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/semantic-scholar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.semanticscholar.org
- group: docs
  title: ''
  type: Documentation
  url: https://www.semanticscholar.org/product/api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/allenai
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/allenai/s2-folks
- group: company
  title: ''
  type: Blog
  url: https://medium.com/ai2-blog/semantic-scholar/home
- group: operate
  title: ''
  type: StatusPage
  url: https://status.api.semanticscholar.org/
- group: other
  title: ''
  type: X
  url: https://twitter.com/SemanticScholar
- group: commercial
  title: ''
  type: Pricing
  url: https://www.semanticscholar.org/product/api
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.semanticscholar.org/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.semanticscholar.org/product/api/license
- group: learn
  title: ''
  type: Tutorial
  url: https://www.semanticscholar.org/product/api/tutorial
- group: commercial
  title: ''
  type: Plans
  url: plans/semantic-scholar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/semantic-scholar-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/semantic-scholar-finops.yml
created: '2026-06-12'
description: 'Semantic Scholar is a free, AI-powered academic search engine developed by the Allen Institute for AI (AI2) that indexes over 214 million scholarly papers with 2.49 billion citations and 79 million authors. The platform provides a public REST API organized into three services: Academic Graph (papers, authors, citations, venues, and SPECTER2 embeddings), Recommendations (paper similarity and interest-based suggestions), and Datasets (bulk downloadable corpus snapshots updated monthly). API access is available without authentication at a shared rate limit, or with a free API key obtained via request for a dedicated 1 RPS allowance. Semantic Scholar supports AI agent integrations through multiple community-built MCP servers that expose its academic graph to LLM-based toolchains.'
examples:
- key_count: 2
  name: Semantic Scholar Datasets Releases Example
  slug: semantic-scholar-datasets-releases-example
- key_count: 2
  name: Semantic Scholar Paper Search Example
  slug: semantic-scholar-paper-search-example
- key_count: 2
  name: Semantic Scholar Recommendations Example
  slug: semantic-scholar-recommendations-example
finops:
- name: Semantic Scholar Finops
  service_category: ''
  slug: semantic-scholar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/semantic-scholar.png
json_schemas:
- name: AuthorWithPapers
  property_count: 10
  slug: semantic-scholar-author
- name: Citation
  property_count: 5
  slug: semantic-scholar-citation
- name: Release Metadata
  property_count: 3
  slug: semantic-scholar-dataset-release
- name: FullPaper
  property_count: 26
  slug: semantic-scholar-paper
jsonld:
- class_count: 0
  name: Semantic Scholar Context
  property_count: 40
  slug: semantic-scholar-context
layout: provider
modified: '2026-06-12'
name: Semantic Scholar
nav: Providers
network: true
overview: 'Semantic Scholar publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Author Data API, Incremental Updates API, Paper Data API, and 3 more. Tagged areas include Academic, Research, Papers, Citations, and Authors.


  The Semantic Scholar catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Semantic Scholar''s developer surface includes documentation, engineering blog, pricing, tutorials, and 13 more developer resources.'
plans:
- name: Semantic Scholar Plans Pricing
  plan_count: 3
  slug: semantic-scholar-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Semantic Scholar Rate Limits
  slug: semantic-scholar-rate-limits
rules:
- name: Semantic Scholar API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: semantic-scholar-jsonschema-spectral-rules
score:
  band: developing
  composite: 56.2
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 56.6
    developer_ergonomics: 10.9
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 56.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/semantic-scholar/refs/heads/main/screenshots/semantic-scholar-2026-06-20T193645.png
security:
- kind: domain-security
  name: Semantic Scholar Domain Security
  slug: semantic-scholar-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Semantic Scholar Vulnerability Disclosure
  slug: semantic-scholar-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: semantic-scholar
tags:
- Academic
- Research
- Papers
- Citations
- Authors
- Scientific Literature
- AI
- Recommendations
website: https://www.semanticscholar.org
---
