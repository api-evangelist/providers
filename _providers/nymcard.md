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
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.8
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: RESTful card-issuing and payments platform API for users, cards, card products, accounts, funding/transfers, limits, transactions and webhooks.
  name: nCore API
  slug: ncore-api
artifact_total: 4
asyncapis:
- description: ''
  name: Nymcard Webhooks
  slug: nymcard-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.nymcard.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nymcard.com/
- group: docs
  title: ''
  type: APIReference
  url: https://portal.stg.platform.ae-1.nymcard.com/default/documentation/02_api_specs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nymcard.com/get-started/quick-tutorial
- group: company
  title: ''
  type: Blog
  url: https://www.nymcard.com/company/blog
- group: operate
  title: ''
  type: Support
  url: https://www.nymcard.com/company/contact
- group: start
  title: ''
  type: SignUp
  url: https://portal.sand.platform.nymcard.com/default/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nymcard.com/legal/privacy
- group: build
  title: ''
  type: Postman
  url: https://god.gw.postman.com/run-collection/19938718-ce866362-3acf-4546-8ae4-9b5a15f99811?action=collection%2Ffork&source=rip_markdown
- group: auth
  title: ''
  type: Authentication
  url: authentication/nymcard-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nymcard-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/nymcard-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nymcard-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/nymcard-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nymcard-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/nymcard-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nymcard-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nymcard-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/nymcard-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/nymcard-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/nymcard-sandbox.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/nymcard-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nymcard-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nymcard-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nymcard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.nymcard.com
created: '2026-07-17'
description: NymCard is a MENA-based, full-stack payments infrastructure provider whose nCore platform gives banks, fintechs and enterprises RESTful APIs to launch and manage card programs. nCore covers card issuing (virtual, physical, prepaid, debit, credit and tokenized cards), user KYC/KYB onboarding, funding and transfers, product management (balance and velocity limits, fees, MCC authorization controls), the full transaction lifecycle, 3D Secure, PCI-compliant PAN handling, webhooks and embedded lending. The platform is PCI DSS Level 1 certified and NymCard is a principal member of both Visa and Mastercard, with offices in London and Dubai. Backed by QED Investors.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nymcard.png
layout: provider
modified: '2026-07-20'
name: Nymcard
nav: Providers
network: true
overview: 'Nymcard publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Card Issuing, Banking as a Service, and Fintech.


  The Nymcard catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Nymcard''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 20 more developer resources.'
random_paper: 15
score:
  band: developing
  composite: 47.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 25.0
    commercial_clarity: 25.0
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 70.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 47.9
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 62.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nymcard/refs/heads/main/screenshots/nymcard-2026-08-07T185835.png
security:
- kind: authentication
  name: Nymcard Authentication
  slug: nymcard-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nymcard Domain Security
  slug: nymcard-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nymcard
tags:
- Company
- Payments
- Card Issuing
- Banking as a Service
- Fintech
- Embedded Finance
- MENA
website: http://www.nymcard.com
---
