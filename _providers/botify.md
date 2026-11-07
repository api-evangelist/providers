---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Hosted Model Context Protocol server at mcp.botify.com, advertised via RFC 9728 protected-resource metadata as "Botify Agents MCP" with the single scope mcp_read_write. Authorization is delegated to a
  name: Botify Agents MCP
  slug: botify-agents-mcp
- baseURL: https://api.botify.com/v1
  baseurl_source: declared
  description: The Analysis API from Botify — 30 operation(s) for analysis.
  name: Botify Analysis API
  slug: botify-analysis-api
- baseURL: https://api.botify.com/v1
  baseurl_source: declared
  description: The Collections API from Botify — 2 operation(s) for collections.
  name: Botify Collections API
  slug: botify-collections-api
- baseURL: https://api.botify.com/v1
  baseurl_source: declared
  description: The Job API from Botify — 2 operation(s) for job.
  name: Botify Job API
  slug: botify-job-api
- baseURL: https://api.botify.com/v1
  baseurl_source: declared
  description: The KeywordsGroups API from Botify — 1 operation(s) for keywordsgroups.
  name: Botify Keywords Groups API
  slug: botify-keywordsgroups-api
- baseURL: https://api.botify.com/v1
  baseurl_source: declared
  description: The Project API from Botify — 9 operation(s) for project.
  name: Botify Project API
  slug: botify-project-api
- baseURL: https://api.botify.com/v1
  baseurl_source: declared
  description: The ProjectQuery API from Botify — 1 operation(s) for projectquery.
  name: Botify Project Query API
  slug: botify-projectquery-api
- baseURL: https://api.botify.com/v1
  baseurl_source: declared
  description: The User API from Botify — 1 operation(s) for user.
  name: Botify User API
  slug: botify-user-api
- baseURL: https://api.botify.com/v1
  baseurl_source: declared
  description: The Data Source API from Botify — 1 operation(s) for data source.
  name: Botify Data Source API
  slug: botify-data-source-api
artifact_total: 28
collections:
- collection_type: open
  name: Botify Analysis API
  slug: open-botify-analysis-api
- collection_type: open
  name: Botify Collections API
  slug: open-botify-collections-api
- collection_type: open
  name: Botify Datasource API
  slug: open-botify-datasource-api
- collection_type: open
  name: Botify Job API
  slug: open-botify-job-api
- collection_type: open
  name: Botify Keywords Groups API
  slug: open-botify-keywordsgroups-api
- collection_type: open
  name: Botify Project API
  slug: open-botify-project-api
- collection_type: open
  name: Botify Project Query API
  slug: open-botify-projectquery-api
- collection_type: open
  name: Botify User API
  slug: open-botify-user-api
common:
- group: commercial
  href: https://artifacts.apis.io/botify/plans/botify-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/botify-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/botify/capabilities/botify-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/botify-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/botify/overlays/botify-api-swagger-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/botify-api-swagger-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.botify.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.botify.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.botify.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developers.botify.com/reference/getalluserprojects-1
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.botify.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.botify.com/
- group: company
  title: ''
  type: Blog
  url: https://www.botify.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/botify-labs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.botify.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.botify.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.botify.com/privacy-and-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.botify.com/privacy-and-terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.botify.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.botify.com/changelog
- group: build
  href: https://artifacts.apis.io/botify/packages/botify-packages.yml
  title: ''
  type: Packages
  url: packages/botify-packages.yml
- group: build
  href: https://artifacts.apis.io/botify/packages/botify-packages.yml
  title: ''
  type: SDKs
  url: packages/botify-packages.yml
- group: agent
  href: https://artifacts.apis.io/botify/llms/botify-llms.txt
  title: ''
  type: LLMSTxt
  url: llms/botify-llms.txt
- group: agent
  href: https://artifacts.apis.io/botify/well-known/botify-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/botify-well-known.yml
- group: design
  href: https://artifacts.apis.io/botify/lifecycle/botify-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/botify-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/botify/conformance/botify-conformance.yml
  title: ''
  type: Conformance
  url: conformance/botify-conformance.yml
- group: auth
  href: https://artifacts.apis.io/botify/conformance/botify-conformance.yml
  title: ''
  type: Compliance
  url: conformance/botify-conformance.yml
- group: auth
  href: https://artifacts.apis.io/botify/security/botify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/botify-domain-security.yml
- group: operate
  href: https://artifacts.apis.io/botify/changelog/botify-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/botify-changelog.yml
- group: agent
  href: https://artifacts.apis.io/botify/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/botify/skills/botify-query-seo-data.md
  title: ''
  type: AgentSkill
  url: skills/botify-query-seo-data.md
- group: agent
  href: https://artifacts.apis.io/botify/skills/botify-export-seo-data.md
  title: ''
  type: AgentSkill
  url: skills/botify-export-seo-data.md
- group: agent
  href: https://artifacts.apis.io/botify/skills/botify-run-and-monitor-a-crawl.md
  title: ''
  type: AgentSkill
  url: skills/botify-run-and-monitor-a-crawl.md
- group: agent
  href: https://artifacts.apis.io/botify/skills/botify-audit-sitemaps-and-orphans.md
  title: ''
  type: AgentSkill
  url: skills/botify-audit-sitemaps-and-orphans.md
created: '2026-08-08'
description: Botify is an enterprise organic-search and AI-search visibility platform that crawls a brand's website, ingests its server logs, and joins that with Google Search Console, analytics and third-party data to produce thousands of SEO metrics across its SiteCrawler, LogAnalyzer, RealKeywords, ActionBoard, AlertPanel, SpeedWorkers, PageWorkers and EngagementAnalytics products. All of that data is reachable programmatically through the Botify REST API at api.botify.com/v1, which is documented with Swagger/OpenAPI and driven by BQL (Botify Query Language), a JSON DSL used both for interactive queries (up to 2,000 rows per call) and for large export jobs delivered to direct download, AWS S3, AWS Redshift, Google Cloud Storage or Google BigQuery. Botify also operates a hosted, OAuth-protected MCP server ("Botify Agents MCP") at mcp.botify.com so agents can work with Botify data alongside the company's own AI agents.
finops:
- has_sources: true
  method: derived
  name: Botify Finops
  primary_unit: ''
  service_category: ''
  slug: botify-finops
  template: true
image: https://cdn.prod.website-files.com/6639e9e213b495098391c3d1/67bcce304f73f509e3630134_Ai%20Search%20Visibility-Featured%20Image%20(1).jpg
layout: provider
mcp_servers:
- description: Hosted Model Context Protocol server operated by Botify, announced alongside its AI agents so teams can pull Botify SEO/AI-search data into external agent tooling and bring their own agents into the B
  name: Botify Agents MCP
  slug: botify-agents-mcp
modified: '2026-08-08'
name: Botify
nav: Providers
network: true
overview: 'Botify publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analysis API, Collections API, Job API, and 6 more. Tagged areas include SEO, Organic search, Web Crawling, Log Analysis, and Search Console.


  The Botify catalog on APIs.io includes 1 Spectral governance ruleset.


  Botify''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 24 more developer resources.'
plans:
- name: Botify Plans Pricing
  plan_count: 0
  slug: botify-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Botify API Rules
  rule_count: 57
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 7
  slug: botify-rules
scopes:
- name: Botify Scopes
  scope_count: 1
  slug: botify-scopes
  summary_line: 1 scope · authorization_code
score:
  band: developing
  composite: 50.8
  coverage:
    artifact_dirs: 28
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.9
  facets:
    access_clarity: 39.5
    contract_governance: 31.8
    contract_quality: 45.3
    developer_ergonomics: 66.1
    discoverability: 71.7
    operational_transparency: 34.2
  previous_composite: 46.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/botify/botify-2026-08-17T080653.png
security:
- kind: authentication
  name: Botify Authentication
  slug: botify-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Botify Domain Security
  slug: botify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: botify-audit-sitemaps-and-orphans
  slug: botify-audit-sitemaps-and-orphans
- name: botify-export-seo-data
  slug: botify-export-seo-data
- name: botify-query-seo-data
  slug: botify-query-seo-data
- name: botify-run-and-monitor-a-crawl
  slug: botify-run-and-monitor-a-crawl
slug: botify
tags:
- SEO
- Organic search
- Web Crawling
- Log Analysis
- Search Console
- Marketing Analytics
- AI Search
- Data Export
- MCP
- Agent-Native
website: https://www.botify.com/
---
