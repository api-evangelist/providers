---
agent_readiness:
  band: agent-aware
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.2
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The Qualified Enterprise API (v2) connects Qualified data to a warehouse, CDP or downstream system. It exposes leads, website sessions, conversations, messages, meetings and outbound emails as readabl
  name: Qualified Enterprise API
  slug: qualified-com-enterprise-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qualified-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qualified-com-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.qualified.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.qualified.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://app.qualified.com/docs/api
- group: docs
  title: ''
  type: APIReference
  url: https://app.qualified.com/docs/api
- group: operate
  title: ''
  type: Support
  url: https://university.qualified.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://university.qualified.com/
- group: company
  title: ''
  type: Blog
  url: https://www.qualified.com/plus/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.qualified.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.qualified.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qualified.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qualified.com/legal/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.qualified.com/trust
- group: auth
  title: ''
  type: Compliance
  url: https://www.qualified.com/trust
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qualified.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qualified-com-llms.txt
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/qualified-com-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/qualified-com-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/qualified-com-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qualified-com-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/qualified-com-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qualified-com-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/qualified-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/qualified-com-vulnerability-disclosure.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/qualified-com-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/qualified-com-enterprise-api-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/qualified-com-packages.yml
- group: design
  title: ''
  type: Components
  url: components/qualified-com-components.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/qualified-com-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/qualified-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qualified-com-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-26'
description: Qualified is a San Francisco based B2B agentic marketing platform built around Piper, an AI SDR agent that engages website visitors in real time with chat, voice, video, email, meeting booking and personalized offers, and works natively alongside Salesforce, HubSpot, Marketo, Eloqua, Outreach, Salesloft, 6sense, Demandbase and Slack. The company publishes the Qualified Enterprise API, a versioned REST contract at api.qualified.com that exposes the underlying records behind the platform — leads, website sessions, conversations, messages, meetings and outbound emails — plus write endpoints for leads and companies, a bulk job endpoint and a GDPR deletion request endpoint, so customers can pipe engagement data into Snowflake, Databricks, BigQuery, Adobe AEP or Eloqua and write enriched records back. The API is bearer-token authenticated with named OAuth-style scopes, cursor paginated, documented for incremental (delta) sync, and is available on the Enterprise and Ultimate plan tiers.
image: https://www.qualified.com/favicon.ico
layout: provider
modified: '2026-08-26'
name: Qualified
nav: Providers
network: true
overview: 'Qualified publishes 1 API on the [APIs.io](https://apis.io/) network: Enterprise API. Tagged areas include Company, Conversational Marketing, Sales, Marketing, and Artificial Intelligence.


  Qualified''s developer surface includes authentication, documentation, API reference, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
plans:
- name: Qualified Com Plans Pricing
  plan_count: 3
  slug: qualified-com-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 4
  name: Qualified Com Rate Limits
  slug: qualified-com-rate-limits
scopes:
- name: Qualified Com Scopes
  scope_count: 0
  slug: qualified-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 63.6
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 30.3
    contract_quality: 55.6
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 30.3
    operational_transparency: 81.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Qualified Com Authentication
  slug: qualified-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Qualified Com Domain Security
  slug: qualified-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Qualified Com Vulnerability Disclosure
  slug: qualified-com-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Qualified Com Trust Center
  slug: qualified-com-trust-center
  summary_line: SOC 2 Type II, EU-US Privacy Shield
slug: qualified-com
tags:
- Company
- Conversational Marketing
- Sales
- Marketing
- Artificial Intelligence
- AI Agents
- Lead Generation
- Customer Engagement
- Salesforce
- Analytics
website: https://www.qualified.com/
---
