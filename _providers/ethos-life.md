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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ethos-life-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ethos.com
- group: other
  title: ''
  type: API
  url: https://www.ethos.com/api/
- group: company
  title: ''
  type: Partners
  url: https://www.ethos.com/faq/partners/
- group: other
  title: ''
  type: PolicyholderResources
  url: https://www.ethos.com/policyholder-resource-page-partnerships/
- group: start
  title: ''
  type: AgentPortal
  url: https://agents.ethoslife.com/login
- group: other
  title: ''
  type: CustomerApplication
  url: https://app.ethoslife.com/login/
- group: company
  title: ''
  type: TechBlog
  url: https://www.ethos.com/tech-and-ethos/
- group: other
  title: ''
  type: MediumEngineering
  url: https://techandethos.medium.com
- group: company
  title: ''
  type: About
  url: https://www.ethos.com/about/
- group: company
  title: ''
  type: Careers
  url: https://www.ethoslife.com/careers/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/getethos
- group: other
  title: ''
  type: DesignSystem
  url: https://github.com/getethos/ethos-design-system
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ethoslife
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/ethoslife
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/ethos-3
- group: docs
  title: ''
  type: GraphQL
  url: graphql/ethos-life-graphql.md
- group: company
  title: ''
  type: Blog
  url: https://techandethos.medium.com/feed
created: '2026-05-25'
description: Ethos is a US digital life insurance company headquartered in San Francisco, founded in 2016, offering term life, whole life, and indexed universal life policies through an online, mostly no-medical-exam application flow. Ethos operates as a technology-driven insurance agency, distributing policies underwritten by carriers such as Ameritas, Banner Life (Legal & General America), Protective, and TruStage. Coverage is available in 49 states and Washington, D.C., with term policies offered for 10, 15, 20, 30, and 40 year durations and face amounts ranging from $15,000 to $3 million. The company has raised over $400 million from investors including Goldman Sachs, SoftBank, GV, Sequoia, and Accel, and is widely cited as one of the leading insurtech companies modernizing the life insurance buying experience. Ethos exposes a Partnership API that lets approved business partners embed quoting, identity validation, instant underwriting, application capture, billing, and signed policy
  issuance directly into their own products. The Partnership API uses bearer-token authentication tied to a partner API key and per-applicant session, and consolidates steps such as identity validation and quoting into combined endpoints to enable instant decisioning. There is no public, self-serve OpenAPI specification, SDK, or developer signup; access requires a partnership agreement with Ethos. Ethos's only material open-source footprint is the ethos-design-system React component library on GitHub.
graphqls:
- description: Ethos Life operates a Partnership API that allows approved business partners to embed quoting, identity validation, instant underwriting, application capture, billing, and signed policy issuance direc
  name: Ethos Life - GraphQL Schema
  slug: ethos-life-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ethos-life.png
layout: provider
modified: '2026-05-25'
name: Ethos
nav: Providers
network: true
overview: 'Ethos is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Life Insurance, Term Life Insurance, Whole Life Insurance, and Indexed Universal Life.


  Ethos'' developer surface includes GitHub presence, engineering blog, and 16 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 41.5
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 13.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ethos-life/refs/heads/main/screenshots/ethos-life-2026-06-20T180839.png
security:
- kind: domain-security
  name: Ethos Life Domain Security
  slug: ethos-life-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ethos-life
tags:
- Insurance
- Life Insurance
- Term Life Insurance
- Whole Life Insurance
- Indexed Universal Life
- Insurtech
- Digital Insurance
- No Medical Exam
- Underwriting
- Quotes
- Policies
- Embedded Insurance
- Partnership API
- Financial-Services
website: https://www.ethos.com
---
