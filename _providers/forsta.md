---
access_model:
  confidence: high
  label: Enterprise, contact sales
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 37.5
  scored_at: '2026-09-10'
agentic_access:
- acting_count: 214
  human_in_the_loop: 6
  name: Forsta Agentic Access
  operation_count: 345
  slug: forsta-agentic-access
  summary_line: 345 operations · 214 acting · 6 human-in-the-loop
api_count: 8
apis:
- baseURL: https://{server}/api/v1
  baseurl_source: declared
  description: 'The Decipher REST API (Forsta Surveys) automates a private or shared Decipher instance: create and launch surveys, read datamaps, extract and edit response data, run crosstabs and dashboards, manage c'
  name: Forsta Decipher REST API
  slug: forsta
- baseURL: https://{server}
  baseurl_source: declared
  description: 'Panel Management exposes four published contracts: an Integration API (53 operations) for sessions, panelists, notes, projects and delivery statistics; a Community API (45 operations); a webhook paylo'
  name: Forsta Panel Management APIs
  slug: panel-management
- baseURL: https://us-west-2-eks.aws.focusvision.com/smp-partner-service
  baseurl_source: declared
  description: The contract a sample provider must implement to be listed in the Forsta Sample Marketplace - estimates, projects and samples over OAuth 2.0 client credentials or HTTP Basic - together with the Partne
  name: Forsta Sample Marketplace Partner APIs
  slug: sample-marketplace
artifact_total: 13
asyncapis:
- description: ''
  name: Forsta Panel Management Webhooks
  slug: forsta-panel-management-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.forsta.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.developer.focusvision.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.developer.focusvision.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.developer.focusvision.com/docs/decipher/api
- group: operate
  title: ''
  type: Support
  url: https://help.forsta.com/
- group: company
  title: ''
  type: Blog
  url: https://www.forsta.com/resources/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ForstaGlobal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/forstainfo
- group: start
  title: ''
  type: Login
  url: https://www.forsta.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.forsta.com/legal/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.forsta.com/legal/privacy-notice/
- group: auth
  title: ''
  type: Compliance
  url: https://www.forsta.com/legal-privacy/pg-forsta-technical-and-organizational-measures/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hxplatform.com/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/forsta-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/forsta-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/forsta-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/forsta-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/forsta-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/forsta-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/forsta-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/forsta-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/forsta-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/forsta-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/forsta-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/forsta-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/forsta-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/forsta-panel-management-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/forsta-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/forsta-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/forsta-llms.txt
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/forsta-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/forsta-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/forsta-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/forsta-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.pressganey.com/responsible-disclosure-policy/
created: '2025-02-12'
description: 'Forsta is the customer experience and market research technology company formed from the 2021 merger of Confirmit, FocusVision and Dapresy, and acquired by Press Ganey in 2022 to trade as PG Forsta. Its HX Platform spans survey data collection (Decipher / Forsta Surveys), panel and sample management, qualitative research, text and social analytics, and dashboard visualization for customer, employee and brand experience programs. Forsta publishes eight OpenAPI documents covering 345 operations at docs.developer.focusvision.com: the Decipher REST API for survey automation and data extraction, the Panel Management Integration, Community, webhook and vendor-callback contracts, and the Sample Marketplace partner contract that sample providers must implement to be listed.'
finops:
- name: Forsta Finops
  service_category: API
  slug: forsta-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/forsta.png
layout: provider
mcp_servers:
- description: ''
  name: Forsta MCP Server
  slug: forsta-mcp-server
modified: '2026-09-10'
name: Forsta
nav: Providers
network: true
overview: 'Forsta publishes 3 APIs on the [APIs.io](https://apis.io/) network: Decipher REST API, Panel Management APIs, and Sample Marketplace Partner APIs. Tagged areas include Customer Insights, Feedback, Market Research, Surveys, and Customer Experience.


  The Forsta catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Forsta''s developer surface includes documentation, API reference, support, engineering blog, changelog, authentication, CLI, and 29 more developer resources.'
plans:
- name: Forsta Plans Pricing
  plan_count: 0
  slug: forsta-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Forsta Rate Limits
  slug: forsta-rate-limits
scopes:
- name: Forsta Scopes
  scope_count: 0
  slug: forsta-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 57.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 43.0
    catalog_earned_first_party: 0.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 48.7
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 60.9
    developer_ergonomics: 58.9
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 60.5
  previous_composite: 9.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 33.3
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: rising
  upsert:
    applies: true
    score: 33.3
screenshot: https://raw.githubusercontent.com/api-evangelist/forsta/refs/heads/main/screenshots/forsta-2026-06-20T181437.png
security:
- kind: authentication
  name: Forsta Authentication
  slug: forsta-authentication
  summary_line: apiKey/http/oauth2 · 7 schemes
- kind: domain-security
  name: Forsta Domain Security
  slug: forsta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Forsta Vulnerability Disclosure
  slug: forsta-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: forsta
tags:
- Customer Insights
- Feedback
- Market Research
- Surveys
- Customer Experience
- Employee Experience
- Panel Management
- Data Collection
- Analytics
- Voice of the Customer
website: https://www.forsta.com/
---
