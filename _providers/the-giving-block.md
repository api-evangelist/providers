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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.6
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: RESTful JSON API for accepting crypto, stock, and card donations on behalf of nonprofits in The Giving Block network. Provides organization management, currency and exchange-rate lookups, crypto depos
  name: The Giving Block Public API
  slug: the-giving-block-public-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://thegivingblock.com
- group: start
  title: ''
  type: Portal
  url: https://thegivingblock.com/developer-resources/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.thegivingblock.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.thegivingblock.com/reference/getting-started-1
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.thegivingblock.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://thegivingblock.com/about/contact/
- group: auth
  title: ''
  type: Authentication
  url: authentication/the-giving-block-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/the-giving-block-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/the-giving-block-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/the-giving-block-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/the-giving-block-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/the-giving-block-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/the-giving-block-components.yml
- group: design
  title: ''
  type: Webhooks
  url: webhooks/the-giving-block-webhooks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/the-giving-block-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/the-giving-block-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-giving-block-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/the-giving-block-well-known.yml
created: '2026-07-17'
description: The Giving Block is a crypto-native fundraising platform that lets nonprofits and enterprises accept cryptocurrency, stock, and card donations. Through its Public API and embeddable donation widget, partners can build their own donation experiences or embed The Giving Block's donation form to route gifts to more than 1,000 nonprofit organizations in its network. The API securely accepts Bitcoin, Ethereum, and 100+ other cryptocurrencies, instantly converts crypto donations to cash so nonprofits never have to touch crypto, and also supports stock and donor-advised-fund (DAF) giving. It is a RESTful, JSON API with JWT-based authentication, AES-256 encrypted webhook notifications, and separate production and sandbox environments. The Giving Block was surfaced as a portfolio company of Multicoin Capital and enriched into the API Evangelist network from its published developer documentation.
image: https://thegivingblock.com/favicon.ico
layout: provider
modified: '2026-07-21'
name: The Giving Block
nav: Providers
network: true
overview: 'The Giving Block publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto Web3, Donations, Fundraising, and Non-Profit.


  The Giving Block''s developer surface includes developer portal, documentation, API reference, getting-started guide, support, authentication, sandbox, and 12 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 18.2
  coverage:
    artifact_dirs: 14
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
    contract_quality: 0.0
    developer_ergonomics: 49.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 18.2
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/the-giving-block/refs/heads/main/screenshots/the-giving-block-2026-09-02T163344.png
security:
- kind: authentication
  name: The Giving Block Authentication
  slug: the-giving-block-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: The Giving Block Domain Security
  slug: the-giving-block-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: the-giving-block
tags:
- Company
- Crypto Web3
- Donations
- Fundraising
- Non-Profit
- Payments
- Cryptocurrency
- Stock Donations
- Webhook
- Widgets
website: https://thegivingblock.com
---
