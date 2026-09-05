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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'PSD2 open-banking platform API: Authentication, General, Payment Initiation (PIS) and Account Information (AIS) services for account-to-account bank payments, card (hybrid) payments, refunds and accou'
  name: kevin. platform API
  slug: kevin-platform-api
artifact_total: 5
asyncapis:
- description: ''
  name: Kevin Webhooks
  slug: kevin-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.kevin.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.kevin.eu/
- group: docs
  title: ''
  type: APIReference
  url: https://api-reference.kevin.eu/public/platform/v0.3
- group: build
  title: ''
  type: Packages
  url: packages/kevin-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kevin-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/kevin-cli.yml
- group: design
  title: ''
  type: Components
  url: components/kevin-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kevin-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kevin-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kevin-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kevin-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kevin-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kevin-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kevin-conformance.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/kevin-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kevin-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kevin-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kevin-domain-security.yml
created: '2026-07-17'
description: kevin. was a Lithuanian account-to-account (A2A) payments infrastructure company providing PSD2 open-banking Payment Initiation and Account Information services to merchants across 28 European countries. Its platform API let businesses initiate bank (SEPA) and card (hybrid) payments, issue refunds, read account data, and receive signed payment webhooks through a single integration to hundreds of banks, supported by an official Node.js SDK, a CLI, and a React UI component library. Backed by Accel. The company has wound down its public web presence - kevin.eu no longer resolves as of 2026-07 - and this profile is enriched from kevin.'s published npm packages and archived developer reference.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kevin.png
layout: provider
modified: '2026-07-19'
name: Kevin.
nav: Providers
network: true
overview: 'Kevin. publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Open Banking, Account-to-Account, and PSD2.


  The Kevin. catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kevin.''s developer surface includes documentation, API reference, CLI, authentication, and 15 more developer resources.'
random_paper: 16
scopes:
- name: Kevin Scopes
  scope_count: 2
  slug: kevin-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 36.3
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 27.9
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 43.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: authentication
  name: Kevin Authentication
  slug: kevin-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Kevin Domain Security
  slug: kevin-domain-security
  summary_line: no transport/DNS hardening detected
slug: kevin
tags:
- Company
- Payments
- Open Banking
- Account-to-Account
- PSD2
- Fintech
- Bank Payments
- Payment Initiation
- Account Information
- Europe
website: https://www.kevin.eu/
---
