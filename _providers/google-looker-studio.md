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
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.9
  scored_at: '2026-09-15'
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
  href: https://raw.githubusercontent.com/api-evangelist/google-looker-studio/refs/heads/main/security/google-looker-studio-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-looker-studio-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/google-looker-studio/refs/heads/main/agentic-access/google-looker-studio-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-looker-studio-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-looker-studio/refs/heads/main/security/google-looker-studio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-looker-studio-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-looker-studio/refs/heads/main/authentication/google-looker-studio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-looker-studio-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-looker-studio/refs/heads/main/scopes/google-looker-studio-scopes.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/google-looker-studio/refs/heads/main/packages/google-looker-studio-packages.yml
  title: ''
  type: Packages
  url: packages/google-looker-studio-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/google-looker-studio/refs/heads/main/packages/google-looker-studio-packages.yml
  title: ''
  type: SDKs
  url: packages/google-looker-studio-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/google-looker-studio/refs/heads/main/cli/google-looker-studio-cli.yml
  title: ''
  type: CLI
  url: cli/google-looker-studio-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/google-looker-studio/refs/heads/main/components/google-looker-studio-components.yml
  title: ''
  type: Components
  url: components/google-looker-studio-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/google-looker-studio/refs/heads/main/well-known/google-looker-studio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/google-looker-studio-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-looker-studio/refs/heads/main/well-known/google-looker-studio-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/google-looker-studio-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/google-looker-studio/refs/heads/main/mcp/google-looker-studio-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/google-looker-studio-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/google-looker-studio/refs/heads/main/llms/google-looker-studio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/google-looker-studio-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/google-looker-studio/refs/heads/main/conformance/google-looker-studio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/google-looker-studio-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-looker-studio/refs/heads/main/security/google-looker-studio-trust-center.yml
  title: ''
  type: Compliance
  url: security/google-looker-studio-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-looker-studio/refs/heads/main/security/google-looker-studio-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/google-looker-studio-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-looker-studio/refs/heads/main/security/google-looker-studio-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/google-looker-studio-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-looker-studio/refs/heads/main/security/google-looker-studio-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-looker-studio-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/google-looker-studio/refs/heads/main/errors/google-looker-studio-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/google-looker-studio-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/google-looker-studio/refs/heads/main/lifecycle/google-looker-studio-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/google-looker-studio-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/google-looker-studio/refs/heads/main/lifecycle/google-looker-studio-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/google-looker-studio-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/google-looker-studio/refs/heads/main/changelog/google-looker-studio-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/google-looker-studio-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/google-looker-studio/refs/heads/main/conventions/google-looker-studio-conventions.yml
  title: ''
  type: Conventions
  url: conventions/google-looker-studio-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/google-looker-studio/refs/heads/main/data-model/google-looker-studio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/google-looker-studio-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/google-looker-studio/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/google-looker-studio/refs/heads/main/plans/google-looker-studio-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-looker-studio-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/google-looker-studio/refs/heads/main/rate-limits/google-looker-studio-rate-limits.yml
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
score:
  band: strong
  composite: 57.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 51.7
    developer_ergonomics: 58.9
    discoverability: 83.3
    operational_transparency: 52.6
  previous_composite: 57.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
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
