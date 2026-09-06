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
  score: 23.9
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'The Goji Platform API for private-markets investing: create and KYC/KYB investors, open and administer IF ISAs, move funds via investor and manager payment APIs, settle debt and equity investments, ma'
  name: Goji Platform API
  slug: goji-platform-api
artifact_total: 4
asyncapis:
- description: ''
  name: Goji Webhooks
  slug: goji-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goji-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.docs.goji.investments/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.goji.investments/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.api.goji.investments/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.api.goji.investments/
- group: company
  title: ''
  type: Website
  url: https://goji.investments
- group: start
  title: ''
  type: SignUp
  url: https://platform.goji.investments/investments/account/register
- group: operate
  title: ''
  type: Support
  url: https://goji.investments/contact
- group: company
  title: ''
  type: Blog
  url: https://goji.investments/insights
- group: commercial
  title: ''
  type: TermsOfService
  url: https://goji.investments/disclosures
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://goji.investments/disclosures
- group: auth
  title: ''
  type: Authentication
  url: authentication/goji-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/goji-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/goji-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/goji-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/goji-webhooks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/goji-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/goji-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/goji-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/goji-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/goji-llms.txt
created: '2026-07-17'
description: Goji is a private-fund digitisation platform, part of the Euroclear group and regulated by the UK Financial Conduct Authority. Founded in 2015 and backed by Anthemis, Goji provides end-to-end infrastructure for asset managers, fund administrators and distributors to digitise access to private markets -- investor onboarding, KYC/KYB and AML, ISA administration, payments, and debt and equity settlement. Its Platform API exposes investor, payment, settlement, bond and ISA operations over HTTPS with HMAC-signed requests and a webhook event stream, letting distributors offer investors a fully digital investment journey into private market funds.
image: https://goji.investments/hubfs/Goji%20favicon.png
layout: provider
modified: '2026-07-19'
name: Goji
nav: Providers
network: true
overview: 'Goji publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Private Markets, Investments, and Funds.


  The Goji catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Goji''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, authentication, and 15 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 38.0
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 38.0
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/goji/refs/heads/main/screenshots/goji-2026-07-25T220023.png
security:
- kind: authentication
  name: Goji Authentication
  slug: goji-authentication
  summary_line: http/hmac · 2 schemes
- kind: domain-security
  name: Goji Domain Security
  slug: goji-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: goji
tags:
- Company
- Fintech
- Private Markets
- Investments
- Funds
- KYC
- Payments
- ISA
- Settlement
- Webhook
- Euroclear
website: https://goji.investments
---
