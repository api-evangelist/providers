---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.8
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: Publicly reachable GraphQL endpoint served by the Craft CMS instance behind level.co. Introspection is enabled anonymously, but the published public schema scope is deliberately narrow — a `ping` quer
  name: Level Website Content GraphQL API
  slug: level-website-content-graphql-api
- description: 'The undocumented HTTPS backend the Level Home iOS and Android applications talk to. It is an AWS API Gateway fronted service that returns a `{"message": "..."}` JSON error envelope and an `x-request-i'
  name: Level Mobile Application Backend
  slug: level-mobile-application-backend
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/level-home-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://level.co/
- group: docs
  title: ''
  type: Documentation
  url: https://level.co/support/
- group: operate
  title: ''
  type: Support
  url: https://level.co/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://level.co/support/
- group: company
  title: ''
  type: Blog
  url: https://level.co/stories/
- group: operate
  title: ''
  type: PressReleases
  url: https://level.co/press/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LevelHome
- group: commercial
  title: ''
  type: Pricing
  url: https://level.co/all-products/
- group: start
  title: ''
  type: SignUp
  url: https://level.co/account/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://level.co/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.privacy.assaabloydss.com/en
- group: commercial
  title: ''
  type: Legal
  url: https://level.co/legal/
- group: other
  title: ''
  type: Warranty
  url: https://level.co/return-policy/
- group: company
  title: ''
  type: Partnerships
  url: https://level.co/partnerships/
- group: operate
  title: ''
  type: ContactForm
  url: https://level.co/contact-form/
- group: other
  title: ''
  type: FCC
  url: https://level.co/fcc/
- group: docs
  title: ''
  type: GraphQL
  url: graphql/level-home.graphql
- group: agent
  title: ''
  type: WellKnown
  url: well-known/level-home-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/level-home-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/level-home-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/level-home-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/level-home-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/level-home-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/level-home-conventions.yml
created: '2026-08-04'
description: Level Home is the Redwood City, California maker of the "invisible" Level smart lock family — Level Lock, Level Lock Pro, Level Bolt and Level Keypad — which hide the motor, radios and battery inside a standard-looking deadbolt. The locks speak Bluetooth LE, Thread and Matter, and work with Apple Home (including Apple Home Key), Google Home, Amazon Alexa and SmartThings rather than through a published third-party developer API. In September 2024 ASSA ABLOY acquired the Level Lock hardware business, brand and IP, which continues to operate as Level at level.co; the remaining Level Home, Inc. entity — the Level M multifamily software business, which also absorbed Dwelo — renamed itself Ambient Property Technologies and now sells smart access, apartment automation and building intelligence to multifamily owners with integrations into RealPage, Yardi, Entrata, ResMan and ButterflyMX. Level publishes no developer portal, no OpenAPI and no partner API documentation; the only publicly
  reachable machine-readable contracts are the Craft CMS GraphQL content endpoint behind level.co/api and the mobile application backend at api.level.co, which is undocumented and account-gated. Third-party developer access to Level devices is brokered by Seam, and local control is available through Matter/Thread.
image: https://level.co/images/logos/_1200x630_crop_center-center_82_none/level.png?mtime=1696960281
layout: provider
modified: '2026-08-04'
name: Level Home
nav: Providers
network: true
overview: 'Level Home publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include smart-lock, smart-home, home-automation, iot, and access-control.


  Level Home''s developer surface includes documentation, support, engineering blog, pricing, signup flow, legal docs, and 19 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 30.5
  delta: -0.9
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 38.9
    developer_ergonomics: 16.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 31.4
  provenance:
    conformance: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/level-home/refs/heads/main/screenshots/level-home-2026-08-07T171558.png
security:
- kind: authentication
  name: Level Home Authentication
  slug: level-home-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Level Home Domain Security
  slug: level-home-domain-security
  summary_line: TLSv1.3 · DMARC
slug: level-home
tags:
- smart-lock
- smart-home
- home-automation
- iot
- access-control
- matter
- thread
- bluetooth-le
- apple-home-key
- consumer-hardware
- multifamily
- proptech
- graphql
website: https://level.co/
---
