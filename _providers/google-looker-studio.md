---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Google Looker Studio Agentic Access
  operation_count: 1
  slug: google-looker-studio-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: API for embedding Looker Studio reports in external applications.
  name: Google Looker Studio Embedding API
  slug: google-looker-studio-embedding-api
- baseURL: https://datastudio.googleapis.com
  baseurl_source: declared
  description: The REST management API for Looker Studio (Data Studio) assets. The contract captured in this repo covers one operation, assets:search, which lists the reports and data sources an authenticated Worksp
  name: Google Looker Studio Assets:search API
  slug: google-looker-studio-assets-search-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Looker Studio Assets:search API
  slug: open-google-looker-studio-assets-search-api
- collection_type: open
  name: Google Looker Studio API
  slug: open-google-looker-studio
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-looker-studio-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-looker-studio-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-looker-studio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-looker-studio-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-looker-studio-scopes.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://support.google.com/looker-studio/answer/6283323
- group: operate
  title: ''
  type: Support
  url: https://support.google.com/looker-studio
- group: operate
  title: ''
  type: Community
  url: https://www.en.advertisercommunity.com/t5/Looker-Studio/ct-p/looker-studio
- group: company
  title: ''
  type: Blog
  url: https://cloud.google.com/blog/products/data-analytics
- group: operate
  title: ''
  type: StatusPage
  url: https://www.google.com/appsstatus/dashboard
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://support.google.com/looker-studio/answer/11521624
- group: other
  title: ''
  type: Templates
  url: https://lookerstudio.google.com/gallery
- group: other
  title: ''
  type: Data Connectors
  url: https://lookerstudio.google.com/data
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googledatastudio
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.google.com/looker-studio
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/looker-studio/integrate
- group: docs
  title: ''
  type: APIReference
  url: https://developers.google.com/looker-studio/integrate/api/reference
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policies.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/data-studio
- group: start
  title: ''
  type: SignUp
  url: https://lookerstudio.google.com
- group: build
  title: ''
  type: Packages
  url: packages/google-looker-studio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/google-looker-studio-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/google-looker-studio-cli.yml
- group: design
  title: ''
  type: Components
  url: components/google-looker-studio-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/google-looker-studio-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/google-looker-studio-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/google-looker-studio-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/google-looker-studio-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/google-looker-studio-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/google-looker-studio-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/google-looker-studio-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/google-looker-studio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-looker-studio-vulnerability-disclosure.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/google-looker-studio-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/google-looker-studio-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/google-looker-studio-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/google-looker-studio-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/google-looker-studio-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/google-looker-studio-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/google-looker-studio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/google-looker-studio-rate-limits.yml
created: '2024-01-01'
description: 'Google Looker Studio — which Google''s own documentation now renders again as Data Studio — is Google''s self-service business intelligence and data visualization platform, free to build and view reports in, with a paid Pro tier sold per user per Google Cloud project. Three developer surfaces exist: a small REST management API at datastudio.googleapis.com for searching report and data-source assets and managing their sharing permissions, a Community Connector framework built on Google Apps Script, and a Community Visualization framework built on the @google/dscc browser library. The REST API is restricted to Google Workspace and Cloud Identity organizations and requires a Workspace admin to configure domain-wide delegation before any call succeeds.'
finops:
- name: Google Looker Studio Finops
  service_category: API
  slug: google-looker-studio-finops
image: https://www.gstatic.com/analytics-suite/header/suite/v2/ic_data_studio.svg
layout: provider
mcp_servers:
- description: ''
  name: Google Looker Studio MCP Server
  slug: google-looker-studio-mcp-server
modified: '2026-09-12'
name: Google Looker Studio
nav: Providers
network: true
overview: 'Google Looker Studio publishes 1 API on the [APIs.io](https://apis.io/) network: Assets:search API. Tagged areas include Analytics, Business Intelligence, Dashboards, Data Visualization, and Google.


  Google Looker Studio''s developer surface includes authentication, getting-started guide, support, engineering blog, release notes, documentation, API reference, and 37 more developer resources.'
plans:
- name: Google Looker Studio Plans Pricing
  plan_count: 2
  slug: google-looker-studio-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Google Looker Studio Rate Limits
  slug: google-looker-studio-rate-limits
scopes:
- name: Google Looker Studio Scopes
  scope_count: 3
  slug: google-looker-studio-scopes
  summary_line: 3 scopes · authorizationCode
screenshot: https://raw.githubusercontent.com/api-evangelist/google-looker-studio/refs/heads/main/screenshots/google-looker-studio-2026-06-20T182212.png
security:
- kind: authentication
  name: Google Looker Studio Authentication
  slug: google-looker-studio-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Looker Studio Domain Security
  slug: google-looker-studio-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Google Looker Studio Vulnerability Disclosure
  slug: google-looker-studio-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Google Looker Studio Trust Center
  slug: google-looker-studio-trust-center
  summary_line: source, service_row, evidence, named
slug: google-looker-studio
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Visualization
- Google
- Looker
- Reporting
website: https://www.google.com/
---
