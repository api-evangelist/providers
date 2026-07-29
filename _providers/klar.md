---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 3.6
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/klar-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/klar-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://klar.mx
- group: start
  title: ''
  type: SignUp
  url: https://signup.klar.mx
- group: operate
  title: ''
  type: Support
  url: https://klar.mx/contacta-a-klar
- group: operate
  title: ''
  type: HelpCenter
  url: https://klar.mx/soporte-faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://klar.mx/klar-legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://klar.mx/aviso-de-privacidad
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/klar-mx
- group: company
  title: ''
  type: PressRoom
  url: https://klar.mx/sala-de-prensa
- group: company
  title: ''
  type: Careers
  url: https://klar.mx/bolsa-de-trabajo
- group: auth
  title: ''
  type: SecurityOverview
  url: https://klar.mx/seguridad
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/klar-llms.txt
created: '2026-07-17'
description: Klar is a Mexican digital financial services platform (neobank) headquartered in Mexico City with engineering in Berlin, serving roughly 7 million customers. Regulated by Mexico's CNBV, Klar offers a deposit account with yield, a no-annual-fee credit card, a secured (garantizada) credit card, the metal Platino card, personal loans, investment products, and Chubb-underwritten life and fraud insurance, plus cashback and interest-free-months (MSI) benefits. It also runs Klar Empresarial for business customers, partnered with Uber to launch the Uber Card in Mexico, and announced the acquisition of mortgage fintech Yave. Klar's product surface is delivered entirely through its consumer mobile app and website; as of this profile Klar publishes NO public developer portal, API reference, SDKs, or sandbox, and no OpenAPI, AsyncAPI, or webhook surface could be found. Third-party access to Klar accounts is generally brokered through Latin American open-finance aggregators (Belvo, Pluggy,
  Plaid) rather than a first-party Klar API. Klar does operate a public GitHub organization (klar-mx), but its repositories are internal infrastructure and DevOps tooling and forks, not client libraries for a Klar API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/klar.png
layout: provider
modified: '2026-07-19'
name: Klar
nav: Providers
network: true
overview: 'Klar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Neobank, Banking, and Credit Cards.


  Klar''s developer surface includes signup flow, support, and 11 more developer resources.'
random_paper: 31
score:
  band: emerging
  composite: 15.6
  delta: -1.8
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 17.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/klar/refs/heads/main/screenshots/klar-2026-07-25T223928.png
security:
- kind: domain-security
  name: Klar Domain Security
  slug: klar-domain-security
  summary_line: TLSv1.3 · DMARC
slug: klar
tags:
- Company
- Fintech
- Neobank
- Banking
- Credit Cards
- Consumer Lending
- Investments
- Insurance
- Mexico
- Latin America
website: https://klar.mx
---
