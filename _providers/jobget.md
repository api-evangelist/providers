---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 14.0
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: The production API host that backs the JobGet mobile applications and employer web experience. The host is publicly reachable over HTTPS and returns a structured RFC 9457 application/problem+json erro
  name: JobGet Platform API
  slug: platform-api
- description: A Model Context Protocol endpoint served from JobGet's own blog host at https://blog.jobget.com/_api/mcp and advertised in JobGet's published llms.txt. It is the Wix Site MCP server provided by the un
  name: JobGet Site MCP Server
  slug: site-mcp
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jobget-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.jobget.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/jobget_stock/
- group: company
  title: ''
  type: About
  url: https://www.jobget.com/about
- group: company
  title: ''
  type: Blog
  url: https://blog.jobget.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.jobget.com/blog-feed.xml
- group: operate
  title: ''
  type: Support
  url: https://support.jobget.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.jobget.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://jobget.com/hire
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jobget.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jobget.com/privacy-policy
- group: other
  title: ''
  type: Accessibility
  url: https://www.jobget.com/accessibility-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jobgetapp
- group: company
  title: ''
  type: Press
  url: https://www.jobget.com/press
- group: company
  title: ''
  type: Careers
  url: https://jobget.notion.site/jobget/Careers-Join-JobGet-c7dce8e7d9b9404c91352381fc8d3fed
- group: other
  title: ''
  type: Enterprise
  url: https://www.jobget.com/employer
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jobget-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/jobget-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/jobget-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jobget-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jobget-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/jobget-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/jobget-conformance.yml
created: '2026-08-04'
description: JobGet is a Boston, Massachusetts based hourly and frontline hiring network that operates a mobile-first job marketplace for workers in food service, retail, hospitality, healthcare, warehousing and trucking. Job seekers build a profile in the JobGet app, receive AI matched recommendations from the JobGenie assistant, apply with one tap, and message or interview with hiring managers directly in the app. On the employer side JobGet sells SMB self-serve job posting and an enterprise suite (SpendSmart budget reallocation, HireReady screening and interview scheduling, and Network Access) that plugs into existing applicant tracking systems including Workday, Greenhouse, ADP, UKG, SAP SuccessFactors, SmartRecruiters, Bullhorn and Fountain. Through its acquisitions of Snagajob, Seasoned and Foh&Boh the company reaches a stated network of 100M+ everyday workers. JobGet publishes no public developer portal, API documentation or machine-readable API specification; its production API host
  api.jobget.com is publicly reachable but undocumented, and ATS connectivity is delivered as a managed integration rather than a self-serve API.
image: https://jobget.com/jobget-logo-purple.svg
layout: provider
mcp_servers:
- description: ''
  name: JobGet MCP Server
  slug: jobget-mcp-server
modified: '2026-08-04'
name: JobGet
nav: Providers
network: true
overview: 'JobGet publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Job, Recruiting, Hiring, and Human Resources.


  JobGet''s developer surface includes engineering blog, support, pricing, signup flow, authentication, and 18 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 22.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jobget/refs/heads/main/screenshots/jobget-2026-08-07T171009.png
security:
- kind: authentication
  name: Jobget Authentication
  slug: jobget-authentication
  summary_line: visitor-token · 1 scheme
- kind: domain-security
  name: Jobget Domain Security
  slug: jobget-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: jobget
tags:
- Company
- Job
- Recruiting
- Hiring
- Human Resources
- Talent Acquisition
- Job Search
- Hourly Work
- Applicant Tracking
- Marketplace
- Mobile
website: https://www.jobget.com/
---
