---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.8
  scored_at: '2026-09-20'
api_count: 2
apis:
- baseURL: https://hiringindex.p.rapidapi.com
  baseurl_source: declared
  description: Aggregates over the same filter - the thing no one else in the category ships
  name: Hiring Index Insights API
  slug: hiring-index-insights-api
- baseURL: https://hiringindex.p.rapidapi.com
  baseurl_source: declared
  description: A single job posting by id
  name: Hiring Index Job API
  slug: hiring-index-job-api
- baseURL: https://hiringindex.p.rapidapi.com
  baseurl_source: declared
  description: Paged job search over a filter
  name: Hiring Index Search API
  slug: hiring-index-search-api
artifact_total: 8
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hiring-index/refs/heads/main/mcp/hiring-index-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hiring-index-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hiring-index/refs/heads/main/overlays/hiring-index-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hiring-index-openapi-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hiring-index/refs/heads/main/security/hiring-index-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hiring-index-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hiring-index/refs/heads/main/authentication/hiring-index-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hiring-index-authentication.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/hiring-index/refs/heads/main/packages/hiring-index-packages.yml
  title: ''
  type: Packages
  url: packages/hiring-index-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/hiring-index/refs/heads/main/packages/hiring-index-packages.yml
  title: ''
  type: SDKs
  url: packages/hiring-index-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hiring-index/refs/heads/main/llms/hiring-index-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hiring-index-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hiring-index/refs/heads/main/conventions/hiring-index-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hiring-index-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hiring-index/refs/heads/main/data-model/hiring-index-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hiring-index-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hiring-index/refs/heads/main/conformance/hiring-index-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hiring-index-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hiring-index/refs/heads/main/lifecycle/hiring-index-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hiring-index-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hiring-index/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://hiringindex.org
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hiringindex.org/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://hiringindex.org/products/jobs-api
- group: commercial
  title: ''
  type: Pricing
  url: https://hiringindex.org/pricing
- group: start
  title: ''
  type: SignUp
  url: https://rapidapi.com/starnikovoleg/api/hiringindex
- group: company
  title: ''
  type: Blog
  url: https://hiringindex.org/blog
- group: operate
  title: ''
  type: Support
  url: https://hiringindex.org/feedback
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/starnikov-oleg-org
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hiringindex.org/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hiringindex.org/legal/privacy
created: '2026-09-14'
description: Hiring Index is a jobs and labour-market data API that reads live postings straight from thirteen applicant tracking systems - Workday, SmartRecruiters, Greenhouse, Workable, Lever, Ashby, Recruitee, Teamtailor, Breezy, Personio, Hireology, PageUp and Zoho Recruit - behind one endpoint. Three operations search postings by title, keyword, location, salary, work arrangement and posting age; aggregate the same filter into salary percentiles, top employers and posting-age freshness; and fetch a single posting by id. A field the source did not state is absent rather than guessed, dates are the employer's own, and apply links point at the employer's ATS. A first-party MCP server and a Python client ship alongside the API, which is metered by results on RapidAPI.
image: https://hiringindex.org/assets/og/home.png
layout: provider
mcp_servers:
- description: ''
  name: Hiring Index MCP Server
  slug: hiring-index-mcp-server
modified: '2026-09-14'
name: Hiring Index
nav: Providers
network: true
overview: 'Hiring Index publishes 3 APIs on the [APIs.io](https://apis.io/) network: Insights API, Job API, and Search API. Tagged areas include Job, Hiring Data, Labor Market, Human Resources, and Recruiting.


  Hiring Index''s developer surface includes authentication, getting-started guide, pricing, signup flow, engineering blog, support, and 16 more developer resources.'
plans:
- name: Hiring Index Plans Pricing
  plan_count: 5
  slug: hiring-index-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Hiring Index Rate Limits
  slug: hiring-index-rate-limits
score:
  band: strong
  composite: 55.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 57.1
    developer_ergonomics: 70.8
    discoverability: 75.9
    operational_transparency: 34.2
  previous_composite: 55.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Hiring Index Authentication
  slug: hiring-index-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Hiring Index Domain Security
  slug: hiring-index-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: hiring-index
tags:
- Job
- Hiring Data
- Labor Market
- Human Resources
- Recruiting
- Job Postings
- Market Intelligence
- Alternative Data
website: https://hiringindex.org
---
