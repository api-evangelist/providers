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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.8
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: HTTP RPC-style API for age gates, age verification, verifiable parental consent, k-ID sessions, and permission management. Methods take the form https://game-api.k-id.com/api/v1/{method} with bearer A
  name: k-ID API
  slug: k-id-api
artifact_total: 5
asyncapis:
- description: ''
  name: K Id Webhooks
  slug: k-id-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.k-id.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.k-id.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.k-id.com/api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.k-id.com/get-started/overview
- group: operate
  title: ''
  type: Support
  url: https://k-id.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://product.k-id.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kidentify
- group: commercial
  title: ''
  type: TermsOfService
  url: https://k-id.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://k-id.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://portal.k-id.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.k-id.com
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/k-id-lifecycle.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://security.k-id.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/k-id-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/k-id-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/k-id-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/k-id-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/k-id-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/k-id-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/k-id-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/k-id-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/k-id-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/k-id-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/k-id-webhooks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/k-id-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/k-id-domain-security.yml
created: '2026-07-17'
description: k-ID is a compliance platform that lets games, social apps, AI products, and commerce deliver age-appropriate experiences across 200+ jurisdictions. Its Compliance Development Kit (CDK) encodes auto-updating regulatory logic for regimes like COPPA, GDPR-Kids, the UK Age Appropriate Design Code and Online Safety Act, Brazil's ECA Digital, and Australia's minimum-age rules, while AgeKit and AgeKit+ provide privacy-preserving age assurance (facial age estimation, ID checks, credit card, AgeKey reusable credentials) and Family Connect handles verifiable parental consent. Developers integrate through the k-ID HTTP RPC API (game-api.k-id.com) using bearer API keys, hosted widget URLs, HMAC-signed webhooks, and official Agent Skills for AI coding tools.
image: https://avatars.githubusercontent.com/kidentify
layout: provider
modified: '2026-07-20'
name: k-ID
nav: Providers
network: true
overview: 'k-ID publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Age Verification, Age Assurance, Compliance, and Parental Consent.


  The k-ID catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  k-ID''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 20 more developer resources.'
random_paper: 0
score:
  band: developing
  composite: 42.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 59.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 50.0
  previous_composite: 42.7
  provenance:
    conformance: derived
    mcp: derived
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/k-id/refs/heads/main/screenshots/k-id-2026-08-17T123933.png
security:
- kind: authentication
  name: K Id Authentication
  slug: k-id-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: K Id Domain Security
  slug: k-id-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: K Id Trust Center
  slug: k-id-trust-center
  summary_line: trust center published
slug: k-id
tags:
- Company
- Age Verification
- Age Assurance
- Compliance
- Parental Consent
- Child Safety
- Identity
- Privacy
- Regulatory Technology
- Gaming
website: https://portal.k-id.com
---
