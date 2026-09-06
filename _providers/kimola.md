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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.6
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: REST API for presets (pre-trained classification and entity-extraction models), research reports and their analyses, feedback feeds, query consumption, and subscription usage. Authenticated with an HT
  name: Kimola API
  slug: kimola-api
- description: Text-classification API that runs text against custom and pre-built models and returns matching tags with probabilities (batch up to 100 per request), with multi-language results via ISO 639-1 codes.
  name: Kimola Cognitive API
  slug: kimola-cognitive-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kimola-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kimola.com
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Kimola/api
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/Kimola/api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Kimola
- group: operate
  title: ''
  type: Support
  url: https://kimola.com/support
- group: company
  title: ''
  type: Blog
  url: https://kimola.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://kimola.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://kimola.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://kimola.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kimola.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kimola.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kimola.com/
- group: build
  title: ''
  type: Packages
  url: packages/kimola-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kimola-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kimola-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kimola-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kimola-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kimola-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kimola-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kimola-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/kimola-cognitive-examples.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/kimola-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kimola-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Kimola is a market research automation platform that turns customer feedback into research insights. It tracks feedback from social media, reviews, and direct uploads; analyzes it with AI to detect themes, sentiment, and patterns across 30+ languages; and generates executive summaries, customer personas, pain points, and journey maps. Kimola exposes a public REST API for presets (pre-trained classification and entity-extraction models), reports, feedback feeds, query consumption, and subscription usage, plus the Kimola Cognitive API for running text through custom and pre-built classification models and returning tagged predictions with probabilities. Official Python, Node.js, and C# SDKs are published. Kimola is backed by 500 Global.
image: https://kimola.com/images/kimola-og.webp
layout: provider
modified: '2026-07-19'
name: Kimola
nav: Providers
network: true
overview: 'Kimola publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Market Research, Customer Feedback, Text Analytics, and Sentiment Analysis.


  Kimola''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, authentication, and 18 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 29.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 6.7
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 28.0
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kimola/refs/heads/main/screenshots/kimola-2026-07-25T223754.png
security:
- kind: authentication
  name: Kimola Authentication
  slug: kimola-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kimola Domain Security
  slug: kimola-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kimola
tags:
- Company
- Market Research
- Customer Feedback
- Text Analytics
- Sentiment Analysis
- Natural Language Processing
- Consumer Insights
- Machine-Learning
- Artificial Intelligence
website: https://kimola.com
---
