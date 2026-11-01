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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.8
  scored_at: '2026-10-31'
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
  href: https://artifacts.apis.io/nymcard/authentication/nymcard-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nymcard-authentication.yml
- group: design
  href: https://artifacts.apis.io/nymcard/conventions/nymcard-conventions.yml
  title: ''
  type: Conventions
  url: conventions/nymcard-conventions.yml
- group: design
  href: https://artifacts.apis.io/nymcard/conventions/nymcard-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/nymcard-conventions.yml
- group: design
  href: https://artifacts.apis.io/nymcard/errors/nymcard-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/nymcard-problem-types.yml
- group: build
  href: https://artifacts.apis.io/nymcard/errors/nymcard-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/nymcard-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/nymcard/lifecycle/nymcard-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/nymcard-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/nymcard/lifecycle/nymcard-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/nymcard-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/nymcard/changelog/nymcard-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/nymcard-changelog.yml
- group: design
  href: https://artifacts.apis.io/nymcard/conformance/nymcard-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nymcard-conformance.yml
- group: auth
  href: https://artifacts.apis.io/nymcard/conformance/nymcard-conformance.yml
  title: ''
  type: Compliance
  url: conformance/nymcard-conformance.yml
- group: design
  href: https://artifacts.apis.io/nymcard/asyncapi/nymcard-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/nymcard-webhooks.yml
- group: start
  href: https://artifacts.apis.io/nymcard/sandbox/nymcard-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/nymcard-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/nymcard/mcp/nymcard-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/nymcard-mcp.yml
- group: agent
  href: https://artifacts.apis.io/nymcard/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/nymcard/llms/nymcard-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nymcard-llms.txt
- group: agent
  href: https://artifacts.apis.io/nymcard/well-known/nymcard-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nymcard-well-known.yml
- group: auth
  href: https://artifacts.apis.io/nymcard/security/nymcard-domain-security.yml
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
overview: 'Nymcard is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Card Issuing, Banking as a Service, and Fintech.


  The Nymcard catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Nymcard''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 20 more developer resources.'
random_paper: 6
score:
  band: developing
  composite: 45.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 70.8
    discoverability: 66.1
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - mena
  previous_composite: 45.6
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 35.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/nymcard/nymcard-2026-08-07T185835.png
security:
- kind: authentication
  name: Nymcard Authentication
  slug: nymcard-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nymcard Domain Security
  slug: nymcard-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: Issue and fund an nCore card
  slug: nymcard-issue-and-fund-card
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
