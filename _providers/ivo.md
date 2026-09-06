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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.ivo.ai
- group: company
  title: ''
  type: Blog
  url: https://www.ivo.ai/blog
- group: start
  title: ''
  type: Login
  url: https://app.ivo.ai
- group: operate
  title: ''
  type: Support
  url: https://www.ivo.ai/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ivo.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ivo.ai/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.ivo.ai
- group: auth
  title: ''
  type: Compliance
  url: security/ivo-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ivo-conformance.yml
- group: auth
  title: ''
  type: Security
  url: https://trust.ivo.ai/resources?s=a7t7bsi1jpndd9qj122kha&name=responsible-disclosure-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ivo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/ivo-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ivo-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ivo-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ivo-llms.txt
created: '2026-07-17'
description: 'Ivo (Ivo AI, Inc., formerly Latch) is an AI-powered contract intelligence platform built for in-house legal teams at enterprises. Founded in 2022 and headquartered in San Francisco, Ivo delivers three integrated products that share one AI engine: Ivo Review (a Microsoft Word add-in that applies a company''s playbooks clause-by-clause to produce surgical redlines), Ivo Assistant (an agentic AI for drafting, cross-contract Q&A, and legal research) and Ivo Intelligence (an AI-native repository, powered by its AiRE engine, that turns existing contract libraries into queryable business intelligence). Customers include Uber, Shopify, IBM, Atlassian, Canva, Reddit and Pinterest. Ivo is enterprise-only with custom pricing and no public developer API; it publishes a canonical llms.txt, a Trust Center (SOC 2 Type II, ISO 27001:2022, GDPR, CCPA), and a responsible-disclosure security.txt.'
image: https://cdn.prod.website-files.com/65f4b30742f9be11e8959d5c/696ef34a6829192b4c87450e_OG%20Image%20-%20main.jpg
layout: provider
modified: '2026-07-19'
name: Ivo
nav: Providers
network: true
overview: 'Ivo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Legal AI, Contract Review, Contract Intelligence, and Legal Tech.


  Ivo''s developer surface includes engineering blog, support, and 13 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 16.4
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ivo/refs/heads/main/screenshots/ivo-2026-07-25T223048.png
security:
- kind: domain-security
  name: Ivo Domain Security
  slug: ivo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ivo Vulnerability Disclosure
  slug: ivo-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Ivo Trust Center
  slug: ivo-trust-center
  summary_line: SOC 2 Type II, ISO 27001:2022, GDPR, CCPA
slug: ivo
tags:
- Company
- Legal AI
- Contract Review
- Contract Intelligence
- Legal Tech
- Contract Lifecycle Management
- Redlining
- Enterprise
- AI Agents
website: https://www.ivo.ai
---
