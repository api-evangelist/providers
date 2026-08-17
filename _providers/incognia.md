---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Incognia Agentic Access
  operation_count: 4
  slug: incognia-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 4
apis:
- description: OAuth 2.0 client-credentials token exchange
  name: Incognia Authentication API
  slug: incognia-authentication-api
- description: Report labeled events to tune the risk model
  name: Incognia Feedback API
  slug: incognia-feedback-api
- description: Signup risk assessment
  name: Incognia Onboarding API
  slug: incognia-onboarding-api
- description: Login and payment risk assessment
  name: Incognia Transactions API
  slug: incognia-transactions-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Incognia Authentication API
  slug: open-incognia-authentication-api
- collection_type: open
  name: Incognia Authentication Feedback API
  slug: open-incognia-feedback-api
- collection_type: open
  name: Incognia Authentication Onboarding API
  slug: open-incognia-onboarding-api
- collection_type: open
  name: Incognia Authentication Transactions API
  slug: open-incognia-transactions-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/incognia-openapi-overlay.yaml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/incognia-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.incognia.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.incognia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.incognia.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.incognia.com/docs/us/v5/apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.incognia.com/docs/us/v5/apis/incognia-libraries/
- group: company
  title: ''
  type: Blog
  url: https://www.incognia.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.incognia.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.incognia.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.incognia.com/policies/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/inloco
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.incognia.com/
- group: build
  title: ''
  type: Packages
  url: packages/incognia-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/incognia-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/incognia-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/incognia-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/incognia-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/incognia-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/incognia-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/incognia-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/incognia-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.incognia.com/
- group: design
  title: ''
  type: Conventions
  url: conventions/incognia-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/incognia-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/incognia-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/incognia-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Incognia is a location identity and device fingerprinting platform for fraud prevention, providing real-time risk assessments for user onboarding, login, and payment transactions. Its API returns low_risk / high_risk / unknown_risk verdicts by combining privacy-first device recognition, location behavior analysis, and tamper detection, and accepts feedback events (chargebacks, account takeover, identity fraud, accepted/declined outcomes) that continuously tune the risk model. Incognia is used across financial services, fintech, marketplaces, delivery, and gaming to stop account takeover, new-account fraud, and payment fraud while reducing friction for trusted users. Authentication is OAuth 2.0 client credentials, exchanged for short-lived bearer tokens; official SDKs ship for Node.js, Python, Ruby, Java, and Go.
image: https://www.incognia.com/hubfs/incognia-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: incognia-mcp.yml
  slug: incognia-mcpyml
modified: '2026-07-19'
name: Incognia
nav: Providers
network: true
overview: 'Incognia publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Feedback API, Onboarding API, and 1 more. Tagged areas include Company, Cybersecurity, Fraud Prevention, Device Fingerprinting, and Location Identity.


  Incognia''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, authentication, and 22 more developer resources.'
random_paper: 95
scopes:
- name: Incognia Scopes
  scope_count: 0
  slug: incognia-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.4
    developer_ergonomics: 58.2
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 46.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/incognia/refs/heads/main/screenshots/incognia-2026-07-25T222233.png
security:
- kind: authentication
  name: Incognia Authentication
  slug: incognia-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Incognia Domain Security
  slug: incognia-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: incognia
tags:
- Company
- Cybersecurity
- Fraud Prevention
- Device Fingerprinting
- Location Identity
- Identity Verification
- Risk Assessment
- Authentication
- Fintech
- Anti-Fraud
website: https://www.incognia.com/
---
