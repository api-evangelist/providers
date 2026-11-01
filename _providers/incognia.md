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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-10-31'
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
artifact_total: 15
collections:
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
- group: company
  title: ''
  type: BlogRSS
  url: https://www.incognia.com/blog/rss.xml
- group: other
  href: https://artifacts.apis.io/incognia/overlays/incognia-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/incognia-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/incognia/scopes/incognia-scopes.yml
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
  href: https://artifacts.apis.io/incognia/packages/incognia-packages.yml
  title: ''
  type: Packages
  url: packages/incognia-packages.yml
- group: build
  href: https://artifacts.apis.io/incognia/packages/incognia-packages.yml
  title: ''
  type: SDKs
  url: packages/incognia-packages.yml
- group: auth
  href: https://artifacts.apis.io/incognia/authentication/incognia-authentication.yml
  title: ''
  type: Authentication
  url: authentication/incognia-authentication.yml
- group: agent
  href: https://artifacts.apis.io/incognia/mcp/incognia-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/incognia-mcp.yml
- group: agent
  href: https://artifacts.apis.io/incognia/llms/incognia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/incognia-llms.txt
- group: agent
  href: https://artifacts.apis.io/incognia/well-known/incognia-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/incognia-well-known.yml
- group: design
  href: https://artifacts.apis.io/incognia/conformance/incognia-conformance.yml
  title: ''
  type: Conformance
  url: conformance/incognia-conformance.yml
- group: design
  href: https://artifacts.apis.io/incognia/errors/incognia-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/incognia-problem-types.yml
- group: design
  href: https://artifacts.apis.io/incognia/lifecycle/incognia-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/incognia-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.incognia.com/
- group: design
  href: https://artifacts.apis.io/incognia/conventions/incognia-conventions.yml
  title: ''
  type: Conventions
  url: conventions/incognia-conventions.yml
- group: design
  href: https://artifacts.apis.io/incognia/data-model/incognia-data-model.yml
  title: ''
  type: DataModel
  url: data-model/incognia-data-model.yml
- group: auth
  href: https://artifacts.apis.io/incognia/security/incognia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/incognia-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/incognia/agentic-access/incognia-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/incognia-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/incognia/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Incognia is a location identity and device fingerprinting platform for fraud prevention, providing real-time risk assessments for user onboarding, login, and payment transactions. Its API returns low_risk / high_risk / unknown_risk verdicts by combining privacy-first device recognition, location behavior analysis, and tamper detection, and accepts feedback events (chargebacks, account takeover, identity fraud, accepted/declined outcomes) that continuously tune the risk model. Incognia is used across financial services, fintech, marketplaces, delivery, and gaming to stop account takeover, new-account fraud, and payment fraud while reducing friction for trusted users. Authentication is OAuth 2.0 client credentials, exchanged for short-lived bearer tokens; official SDKs ship for Node.js, Python, Ruby, Java, and Go.
image: https://www.incognia.com/hubfs/incognia-logo.svg
layout: provider
modified: '2026-10-06'
name: Incognia
nav: Providers
network: true
overview: 'Incognia publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Feedback API, Onboarding API, and 1 more. Tagged areas include Company, Cybersecurity, Fraud Prevention, Device Fingerprinting, and Location Identity.


  Incognia''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, authentication, and 23 more developer resources.'
random_paper: 0
scopes:
- name: Incognia Scopes
  scope_count: 0
  slug: incognia-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 61.3
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 33.7
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/incognia/incognia-2026-07-25T222233.png
security:
- kind: authentication
  name: Incognia Authentication
  slug: incognia-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Incognia Domain Security
  slug: incognia-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 3
skills:
- name: Assess an onboarding signup for fraud
  slug: incognia-assess-onboarding-signup
- name: Assess a login or payment transaction
  slug: incognia-assess-transaction
- name: Report a feedback event to tune the model
  slug: incognia-report-feedback
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
website: https://www.incognia.com/
---
