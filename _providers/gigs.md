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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'REST API for embedded mobile connectivity: manage projects, plans, users, subscriptions, SIMs (eSIM/pSIM), devices, number portings, add-ons, usage and vouchers. Bearer API-key auth, cursor pagination'
  name: Gigs Core API
  slug: gigs-core-api
artifact_total: 7
asyncapis:
- description: ''
  name: Gigs Events Webhooks
  slug: gigs-events-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://gigs.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.gigs.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.gigs.com/docs/create-a-subscription
- group: docs
  title: ''
  type: APIReference
  url: https://developers.gigs.com/api/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.gigs.com/docs/create-a-subscription
- group: operate
  title: ''
  type: Support
  url: mailto:support@gigs.com
- group: company
  title: ''
  type: Blog
  url: https://gigs.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gigs
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.gigs.com
- group: start
  title: ''
  type: Login
  url: https://dashboard.gigs.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gigs.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gigs.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gigs.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.gigs.com
- group: auth
  href: https://artifacts.apis.io/gigs/well-known/gigs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/gigs-security.txt
- group: agent
  href: https://artifacts.apis.io/gigs/well-known/gigs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gigs-well-known.yml
- group: auth
  href: https://artifacts.apis.io/gigs/authentication/gigs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gigs-authentication.yml
- group: design
  href: https://artifacts.apis.io/gigs/errors/gigs-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/gigs-error-codes.yml
- group: build
  href: https://artifacts.apis.io/gigs/errors/gigs-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/gigs-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/gigs/conventions/gigs-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gigs-conventions.yml
- group: design
  href: https://artifacts.apis.io/gigs/data-model/gigs-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gigs-data-model.yml
- group: design
  href: https://artifacts.apis.io/gigs/asyncapi/gigs-events-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/gigs-events-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/gigs/mcp/gigs-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/gigs-mcp.yml
- group: design
  href: https://artifacts.apis.io/gigs/conformance/gigs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gigs-conformance.yml
- group: design
  href: https://artifacts.apis.io/gigs/lifecycle/gigs-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gigs-lifecycle.yml
- group: start
  href: https://artifacts.apis.io/gigs/sandbox/gigs-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/gigs-sandbox.yml
- group: design
  href: https://artifacts.apis.io/gigs/components/gigs-components.yml
  title: ''
  type: Components
  url: components/gigs-components.yml
- group: auth
  href: https://artifacts.apis.io/gigs/security/gigs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gigs-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/gigs/security/gigs-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gigs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://gigs.com/security/vulnerability-disclosure
- group: agent
  href: https://artifacts.apis.io/gigs/llms/gigs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gigs-llms.txt
- group: agent
  href: https://artifacts.apis.io/gigs/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Gigs is the operating system for embedded telecom, giving any technology brand the ability to launch and operate mobile phone and data plans without becoming a mobile network operator. The Gigs Core API (base https://api.gigs.com) exposes REST resources for projects, plans, users, addresses, subscriptions, SIMs (eSIM and physical), devices, number portings and port-outs, add-ons, subscription changes, usage and usage balances, and vouchers, secured with per-project Bearer API keys. Gigs also ships Connect (a prebuilt embeddable checkout), integrated Payments, an Operator automation layer, a Dashboard, and a Svix-backed webhook/event stream. Backed by Ribbit Capital and Speedinvest.
image: https://i.gigscdn.net/docs/v1/embedded-connectivity.png
layout: provider
modified: '2026-07-19'
name: Gigs
nav: Providers
network: true
overview: 'Gigs is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Telecommunications, Connectivity, eSIM, and MVNO.


  The Gigs catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Gigs'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 25 more developer resources.'
random_paper: 18
score:
  band: developing
  composite: 46.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 66.1
    discoverability: 66.1
    operational_transparency: 39.5
  previous_composite: 46.8
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 30.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/gigs/gigs-2026-07-25T215810.png
security:
- kind: authentication
  name: Gigs Authentication
  slug: gigs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gigs Domain Security
  slug: gigs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Gigs Vulnerability Disclosure
  slug: gigs-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: Activate an eSIM subscription
  slug: gigs-activate-esim-subscription
- name: Handle Gigs webhooks
  slug: gigs-handle-webhooks
slug: gigs
tags:
- Company
- Telecommunications
- Connectivity
- eSIM
- MVNO
- Mobile
- Subscription
- Payments
- Webhook
- Embedded Finance
website: https://gigs.com
---
