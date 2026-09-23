---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.0
  scored_at: '2026-09-23'
api_count: 1
apis:
- description: Automated, programmatic access to the same AI creative-evaluation engine behind the Brainsuite application. Partners and enterprise customers upload assets (or supply asset URLs), declare attributes s
  name: Brainsuite Creative Effectiveness API
  slug: aimpower-creative-effectiveness-api
artifact_total: 7
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aimpower/refs/heads/main/security/aimpower-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aimpower-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brainsuite.ai/en/
- group: commercial
  title: ''
  type: Pricing
  url: https://brainsuite.ai/en/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://brainsuite.ai/en/demo/
- group: start
  title: ''
  type: Login
  url: https://app.brainsuite.ai/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brainsuite.ai/en/data-protection/
- group: operate
  title: ''
  type: Support
  url: https://brainsuite.ai/en/contact-us/
- group: operate
  title: ''
  type: HelpCenter
  url: https://brainsuite.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://brainsuite.ai/en/resources/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.brainsuite.ai/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/brainsuite-gmbh/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aimpower/refs/heads/main/changelog/aimpower-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aimpower-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aimpower/refs/heads/main/lifecycle/aimpower-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aimpower-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aimpower/refs/heads/main/conformance/aimpower-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aimpower-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aimpower/refs/heads/main/packages/aimpower-packages.yml
  title: ''
  type: Packages
  url: packages/aimpower-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aimpower/refs/heads/main/llms/aimpower-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aimpower-llms.txt
created: '2026-09-14'
description: Brainsuite.ai GmbH - founded in 2020 in Hamburg as aimpower GmbH, now registered at Kuddewoerde, Germany - builds Brainsuite, an AI creative-effectiveness platform that predicts how an advertising asset will perform before any media budget is committed. Built on applied consumer-neuroscience models, it scores video, static, packaging, shelf, out-of-home, digital-banner and social-media creative against an ACE (Advertising Creative Effectiveness) score with pillars for attention, persuasion, strategic fit, processing ease, emotional engagement and branding. Alongside the self-serve app at app.brainsuite.ai, it sells a Creative Effectiveness API that partner platforms - generative-AI tools, creative production suites, ad-tech, DAM systems and creator networks - embed to score every asset in-workflow. The API is marketed publicly but its reference and credentials are issued only through a sales conversation.
image: https://brainsuite.ai/wp-content/uploads/2025/09/brainsuite_logo-1.webp
layout: provider
modified: '2026-09-14'
name: Brainsuite.ai
nav: Providers
network: true
overview: 'Brainsuite.ai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Marketing, Artificial Intelligence, and Creative Effectiveness.


  Brainsuite.ai''s developer surface includes pricing, signup flow, support, engineering blog, changelog, and 11 more developer resources.'
plans:
- name: Aimpower Plans Pricing
  plan_count: 4
  slug: aimpower-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Aimpower Rate Limits
  slug: aimpower-rate-limits
scopes:
- name: Aimpower Scopes
  scope_count: 0
  slug: aimpower-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 30.0
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aimpower Authentication
  slug: aimpower-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Aimpower Domain Security
  slug: aimpower-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Aimpower Trust Center
  slug: aimpower-trust-center
  summary_line: trust center published
slug: aimpower
tags:
- Company
- Advertising
- Marketing
- Artificial Intelligence
- Creative Effectiveness
- Ad Testing
- Market Research
- Consumer Neuroscience
- Media
- Software-as-a-Service
- Germany
website: https://brainsuite.ai/en/
---
