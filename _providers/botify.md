---
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Hosted Model Context Protocol server at mcp.botify.com, advertised via RFC 9728 protected-resource metadata as "Botify Agents MCP" with the single scope mcp_read_write. Authorization is delegated to a
  name: Botify Agents MCP
  slug: botify-agents-mcp
- description: The Analysis API from Botify — 30 operation(s) for analysis.
  name: Botify Analysis API
  slug: botify-analysis-api
- description: The Collections API from Botify — 2 operation(s) for collections.
  name: Botify Collections API
  slug: botify-collections-api
- description: The Datasource API from Botify — 1 operation(s) for datasource.
  name: Botify Datasource API
  slug: botify-datasource-api
- description: The Job API from Botify — 2 operation(s) for job.
  name: Botify Job API
  slug: botify-job-api
- description: The KeywordsGroups API from Botify — 1 operation(s) for keywordsgroups.
  name: Botify Keywords Groups API
  slug: botify-keywordsgroups-api
- description: The Project API from Botify — 9 operation(s) for project.
  name: Botify Project API
  slug: botify-project-api
- description: The ProjectQuery API from Botify — 1 operation(s) for projectquery.
  name: Botify Project Query API
  slug: botify-projectquery-api
- description: The User API from Botify — 1 operation(s) for user.
  name: Botify User API
  slug: botify-user-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: other
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
  title: ''
  type: Packages
  url: packages/botify-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/botify-packages.yml
- group: agent
  title: ''
  type: LLMSTxt
  url: llms/botify-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/botify-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/botify-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/botify-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/botify-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/botify-domain-security.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/botify-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/botify-query-seo-data.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/botify-export-seo-data.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/botify-run-and-monitor-a-crawl.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/botify-audit-sitemaps-and-orphans.md
created: '2026-08-08'
description: Botify is an enterprise organic-search and AI-search visibility platform that crawls a brand's website, ingests its server logs, and joins that with Google Search Console, analytics and third-party data to produce thousands of SEO metrics across its SiteCrawler, LogAnalyzer, RealKeywords, ActionBoard, AlertPanel, SpeedWorkers, PageWorkers and EngagementAnalytics products. All of that data is reachable programmatically through the Botify REST API at api.botify.com/v1, which is documented with Swagger/OpenAPI and driven by BQL (Botify Query Language), a JSON DSL used both for interactive queries (up to 2,000 rows per call) and for large export jobs delivered to direct download, AWS S3, AWS Redshift, Google Cloud Storage or Google BigQuery. Botify also operates a hosted, OAuth-protected MCP server ("Botify Agents MCP") at mcp.botify.com so agents can work with Botify data alongside the company's own AI agents.
image: https://cdn.prod.website-files.com/6639e9e213b495098391c3d1/67bcce304f73f509e3630134_Ai%20Search%20Visibility-Featured%20Image%20(1).jpg
layout: provider
mcp_servers:
- description: Hosted Model Context Protocol server operated by Botify, announced alongside its AI agents so teams can pull Botify SEO/AI-search data into external agent tooling and bring their own agents into the B
  name: Botify Agents MCP
  slug: botify-agents-mcp
- description: ''
  name: Botify MCP Server
  slug: botify-mcp-server
modified: '2026-08-08'
name: Botify
nav: Providers
network: true
overview: 'Botify publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Analysis API, Collections API, Datasource API, and 5 more. Tagged areas include SEO, Organic search, search-engine-optimization, web-crawling, and log-analysis.


  Botify''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
random_paper: 2
scopes:
- name: Botify Scopes
  scope_count: 0
  slug: botify-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 45.2
    developer_ergonomics: 51.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 43.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/botify/refs/heads/main/screenshots/botify-2026-08-17T080653.png
security:
- kind: authentication
  name: Botify Authentication
  slug: botify-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Botify Domain Security
  slug: botify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: botify
tags:
- SEO
- Organic search
- search-engine-optimization
- web-crawling
- log-analysis
- search-console
- marketing-analytics
- AI Search
- data-export
- MCP
- agent-native
website: https://www.botify.com/
---
