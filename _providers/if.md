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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.6
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'Single REST API for the Integrated Finance platform — clients, users, real / virtual / shared-pool accounts, bank transfers, currency exchanges, card issuing and processing, beneficiary verification, '
  name: Integrated Finance API
  slug: integrated-finance-api
artifact_total: 5
asyncapis:
- description: ''
  name: If Webhooks
  slug: if-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://integrated.finance
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.integrated.finance
- group: docs
  title: ''
  type: Documentation
  url: https://developer.integrated.finance/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.integrated.finance/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.integrated.finance/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://integrated.finance/support
- group: company
  title: ''
  type: Blog
  url: https://integrated.finance/insights
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/integrated-finance
- group: operate
  title: ''
  type: StatusPage
  url: https://integratedfinance.statuspage.io
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.integrated.finance/docs/changes-to-the-api
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://integrated.finance/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://integrated.finance/terms-and-conditions
- group: auth
  title: ''
  type: Compliance
  url: https://integrated.finance/security-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/if-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/if-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/if-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/if-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/if-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/if-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/if-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/if-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/if-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/if-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/if-webhooks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/if-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/if-domain-security.yml
created: '2026-07-17'
description: Integrated Finance (IF) is a modular fintech infrastructure platform — a "financial operating system" — that lets companies build banking, card, and payment experiences for their users without becoming a bank. Its orchestration layers (IF API interface, IF CORE workflow, IF CONNECT integration) sit on top of multiple banking, card-issuing, FX, and compliance providers and expose a single REST API covering clients and users, real / virtual / shared-pool accounts, incoming and outgoing bank transfers, currency exchanges, card issuing and processing (including 3DS and PIN management), beneficiary verification, generic transactions, and open-banking consents. Authentication is OAuth 2.0 on Keycloak (JWT client assertion, client_credentials); the API supports idempotency on all POST endpoints, Ed25519-signed webhooks with automatic retry, and a full sandbox environment for testing.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/if.png
layout: provider
modified: '2026-07-19'
name: IF
nav: Providers
network: true
overview: 'IF publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Embedded Finance, Banking as a Service, and Payments.


  The IF catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  IF''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 19 more developer resources.'
random_paper: 18
scopes:
- name: If Scopes
  scope_count: 11
  slug: if-scopes
  summary_line: 11 scopes · clientCredentials
score:
  band: developing
  composite: 49.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 51.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 49.1
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 75.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/if/refs/heads/main/screenshots/if-2026-07-25T222048.png
security:
- kind: authentication
  name: If Authentication
  slug: if-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: If Domain Security
  slug: if-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: if
tags:
- Company
- Financial-Services
- Embedded Finance
- Banking as a Service
- Payments
- Cards
- Foreign Exchange
- Compliance
- Open Banking
website: https://integrated.finance
---
