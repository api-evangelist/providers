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
  band: agent-aware
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Incognia Agentic Access
  operation_count: 4
  slug: incognia-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.incognia.com/api
  baseurl_source: declared
  description: OAuth 2.0 client-credentials token exchange
  name: Incognia Authentication API
  slug: incognia-authentication-api
- baseURL: https://api.incognia.com/api
  baseurl_source: declared
  description: Report labeled events to tune the risk model
  name: Incognia Feedback API
  slug: incognia-feedback-api
- baseURL: https://api.incognia.com/api
  baseurl_source: declared
  description: Signup risk assessment
  name: Incognia Onboarding API
  slug: incognia-onboarding-api
- baseURL: https://api.incognia.com/api
  baseurl_source: declared
  description: Login and payment risk assessment
  name: Incognia Transactions API
  slug: incognia-transactions-api
artifact_total: 13
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
  type: X-MCPServerCandidate
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
modified: '2026-07-19'
name: Incognia
nav: Providers
network: true
overview: 'Incognia publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Feedback API, Onboarding API, and 1 more. Tagged areas include Company, Cybersecurity, Fraud Prevention, Device Fingerprinting, and Location Identity.


  Incognia''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, authentication, and 22 more developer resources.'
random_paper: 0
scopes:
- name: Incognia Scopes
  scope_count: 0
  slug: incognia-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 14.0
    developer_ergonomics: 23.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 25.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
