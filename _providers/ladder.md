---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The Ladder API is an embedded term-life-insurance distribution surface for partner platforms. It is delivered primarily as a client-side JavaScript integration — a partner loads Ladder's v3 bundle, co
  name: Ladder API
  slug: ladder-api
artifact_total: 4
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.ladderlife.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://www.ladderlife.com/api
- group: company
  title: ''
  type: Website
  url: https://www.ladderlife.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.ladderlife.com/api
- group: start
  title: ''
  type: Login
  url: https://www.ladderlife.com/login
- group: operate
  title: ''
  type: Support
  url: https://support.ladderlife.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.ladderlife.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://medium.com/ladderlife
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ladderlife
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ladderlife.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ladderlife.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.ladderlife.com/security
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/ladder-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ladder-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ladder-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ladder-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ladder-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ladder-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/ladder-components.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ladder-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ladder-llms.txt
- group: commercial
  title: ''
  type: Licenses
  url: https://www.ladderlife.com/licenses
- group: company
  title: ''
  type: Careers
  url: https://www.ladderlife.com/careers
- group: company
  title: ''
  type: About
  url: https://www.ladderlife.com/about
created: '2026-07-17'
description: 'Ladder (Ladder Financial Inc., operating as Ladder Insurance Services, LLC) is a digital life insurance company founded in 2015 that sells flexible term life insurance fully online — a few health questions, no medical exam for policies up to $3M, 10-to-30 year terms, and "laddering" that lets a policyholder raise or lower coverage as their circumstances change. Policies are underwritten by partner carriers (Amica Life, Fidelity Security Life, and S.USA Life / Prosperity Life Group). Alongside the direct-to-consumer product, Ladder runs an embedded insurance distribution business: the Ladder API lets fintech, lending, investing, benefits, and health-and-wellness platforms embed quoting and a full term-life application into their own site or app in roughly ten lines of JavaScript, with a Quoter, Connector, Calculator, and Account Manager surface, and commission or marketing-fee revenue share. Access to the API is granted through a partner request rather than public self-service
  signup. Ladder is backed by Canaan Partners, General Catalyst, and Lightspeed Venture Partners.'
image: https://ddw3p1oh0ex89.cloudfront.net/assets/b/12d840655daaf0aca843047d94b9b219dda2b8ac2bd5431dd0b6cd6d937b0e3d/static/img/favicon-rungs/apple-touch-icon.png
layout: provider
modified: '2026-07-19'
name: Ladder
nav: Providers
network: true
overview: 'Ladder publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Insurtech, Life Insurance, and Embedded Finance.


  Ladder''s developer surface includes documentation, signup flow, support, engineering blog, authentication, and 19 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 26.8
  delta: -3.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 29.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 39.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ladder/refs/heads/main/screenshots/ladder-2026-07-25T224426.png
security:
- kind: authentication
  name: Ladder Authentication
  slug: ladder-authentication
  summary_line: bearer-token · 1 scheme
- kind: domain-security
  name: Ladder Domain Security
  slug: ladder-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ladder Vulnerability Disclosure
  slug: ladder-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: ladder
tags:
- Company
- Insurance
- Insurtech
- Life Insurance
- Embedded Finance
- Embedded Insurance
- Financial Services
- Fintech
- Quoting
website: https://www.ladderlife.com/
---
