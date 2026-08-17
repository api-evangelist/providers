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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.0
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Surfe Agentic Access
  operation_count: 10
  slug: surfe-agentic-access
  summary_line: 10 operations · 7 acting
api_count: 4
apis:
- description: Credit balance and account utilities.
  name: Surfe Account API
  slug: surfe-account-api
- description: Search and enrich organizations.
  name: Surfe Companies API
  slug: surfe-companies-api
- description: Search and enrich individual contacts.
  name: Surfe People API
  slug: surfe-people-api
- description: ICP definition and lookalike account recommendations.
  name: Surfe Recommendations API
  slug: surfe-recommendations-api
artifact_total: 21
asyncapis:
- description: ''
  name: Surfe Webhooks
  slug: surfe-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Surfe Account API
  slug: open-surfe-account-api
- collection_type: open
  name: Surfe Account Companies API
  slug: open-surfe-companies-api
- collection_type: open
  name: Surfe Account People API
  slug: open-surfe-people-api
- collection_type: open
  name: Surfe Account Recommendations API
  slug: open-surfe-recommendations-api
- collection_type: open
  name: Surfe API
  slug: open-surfe
common:
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/surfe
- group: company
  title: ''
  type: Website
  url: https://surfe.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.surfe.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/surfe-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/surfe-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/surfe-finops.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/surfe-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/surfe-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/surfe-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.surfe.com/blog/feed/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.surfe.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.surfe.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.surfe.com/
- group: operate
  title: ''
  type: Support
  url: https://intercom.help/surfe/en/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/surfe
- group: commercial
  title: ''
  type: Pricing
  url: https://www.surfe.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.surfe.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.surfe.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.surfe.com/terms-and-conditions-api/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.surfe.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.surfe.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.surfe.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/surfe-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/surfe-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/Surfe/surfer/blob/main/SECURITY.md
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/surfe-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/surfe-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.surfe.com/security/
- group: design
  title: ''
  type: Conformance
  url: conformance/surfe-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/surfe-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/surfe-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/surfe-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/surfe-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/surfe-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/surfe-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/surfe-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/surfe-tool-crosswalk.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/surfe-scopes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/surfe-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/surfe-llms.txt
created: '2026-07-01'
description: Surfe (formerly Leadjet) is a B2B contact-data and sales-intelligence platform that syncs LinkedIn prospects into the CRM and exposes an API for people and company search plus enrichment. The Surfe API returns verified business emails and mobile phone numbers, company firmographics, and lookalike account recommendations, billed against a credit-based model.
finops:
- name: Surfe Finops
  service_category: Data and Analytics
  slug: surfe-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/surfe.png
layout: provider
mcp_servers:
- description: ''
  name: surfe-mcp.yml
  slug: surfe-mcpyml
modified: '2026-08-13'
name: Surfe
nav: Providers
network: true
overview: 'Surfe publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Account API, Companies API, People API, and 1 more. Tagged areas include B2B Data, Contact Data, Sales Intelligence, Enrichment, and Lead Generation.


  The Surfe catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Surfe''s developer surface includes documentation, authentication, engineering blog, API reference, getting-started guide, support, pricing, and 34 more developer resources.'
plans:
- name: Surfe Plans Pricing
  plan_count: 4
  slug: surfe-plans-pricing
random_paper: 102
rate_limits:
- limit_count: 10
  name: Surfe Rate Limits
  slug: surfe-rate-limits
scopes:
- name: Surfe Scopes
  scope_count: 1
  slug: surfe-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: exemplar
  composite: 75.3
  delta: 38.0
  facets:
    commercial_clarity: 100.0
    contract_quality: 70.1
    developer_ergonomics: 73.9
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 86.8
  previous_composite: 37.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
security:
- kind: authentication
  name: Surfe Authentication
  slug: surfe-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Surfe Domain Security
  slug: surfe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Surfe Vulnerability Disclosure
  slug: surfe-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Surfe Trust Center
  slug: surfe-trust-center
  summary_line: ISO 27001, GDPR
slug: surfe
tags:
- B2B Data
- Contact Data
- Sales Intelligence
- Enrichment
- Lead Generation
- CRM
- Prospecting
website: https://surfe.com
---
