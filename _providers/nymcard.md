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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.4
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: RESTful card-issuing and payments platform API for users, cards, card products, accounts, funding/transfers, limits, transactions and webhooks.
  name: nCore API
  slug: ncore-api
artifact_total: 5
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
  type: MCPServer
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
mcp_servers:
- description: ''
  name: nymcard-mcp.yml
  slug: nymcard-mcpyml
modified: '2026-07-20'
name: Nymcard
nav: Providers
network: true
overview: 'Nymcard publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Card Issuing, Banking as a Service, and Fintech.


  The Nymcard catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Nymcard''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 20 more developer resources.'
random_paper: 5
score:
  band: developing
  composite: 48.8
  delta: 3.8
  facets:
    access_clarity: 25.0
    commercial_clarity: 25.0
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 70.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 45.0
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
  schema_version: 0.12.0
  scored_at: '2026-08-19'
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
