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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 12.9
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/geico-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/geico-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GEICO
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/geico
- group: company
  title: ''
  type: Website
  url: https://www.geico.com/
- group: other
  title: ''
  type: MobileApp
  url: https://www.geico.com/mobile/
- group: other
  title: ''
  type: Quote
  url: https://www.geico.com/auto-insurance/
- group: other
  title: ''
  type: Claims
  url: https://www.geico.com/claims/
- group: company
  title: ''
  type: AboutUs
  url: https://www.geico.com/about/
- group: company
  title: ''
  type: Careers
  url: https://careers.geico.com/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.geico.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.geico.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.geico.com/legal/
- group: start
  title: ''
  type: Login
  url: https://ecams.geico.com/login
- group: docs
  title: ''
  type: GraphQL
  url: graphql/geico-graphql.md
created: '2026-05-05'
description: The second-largest private passenger auto insurance company in the United States and a subsidiary of Berkshire Hathaway. Known for its direct-to-consumer model, competitive rates, and iconic advertising campaigns. GEICO serves customers through its website, GEICO Mobile app, and call centers rather than through a public API.
graphqls:
- description: GEICO (Government Employees Insurance Company) is the second-largest private passenger auto insurer in the United States, operating as a subsidiary of Berkshire Hathaway. GEICO serves customers direct
  name: GEICO Insurance GraphQL Schema
  slug: geico-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/geico.png
layout: provider
modified: '2026-05-16'
name: GEICO
nav: Providers
network: true
overview: GEICO is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Auto Insurance, Property and Casualty, and Direct to Consumer.
random_paper: 15
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 3
    catalog_earned: 19.0
    catalog_earned_first_party: 0.0
    catalog_gap: 96.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 41.5
    developer_ergonomics: 0.0
    discoverability: 35.2
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 20.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 30.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/geico/refs/heads/main/screenshots/geico-2026-06-20T181721.png
security:
- kind: domain-security
  name: Geico Domain Security
  slug: geico-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Geico Vulnerability Disclosure
  slug: geico-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: geico
tags:
- Insurance
- Auto Insurance
- Property and Casualty
- Direct to Consumer
website: https://www.geico.com/
---
