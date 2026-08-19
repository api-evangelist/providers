---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Unbabel Agentic Access
  operation_count: 13
  slug: unbabel-agentic-access
  summary_line: 13 operations · 5 acting
api_count: 6
apis:
- description: Authenticated customer account information.
  name: Unbabel Account API
  slug: unbabel-account-api
- description: Supported source-to-target language combinations.
  name: Unbabel Language Pairs API
  slug: unbabel-language-pairs-api
- description: Pure machine-translation jobs, optionally upgradeable to human review.
  name: Unbabel Machine Translation API
  slug: unbabel-machine-translation-api
- description: Available tones and topics/domains for a translation.
  name: Unbabel Tone and Topic API
  slug: unbabel-tone-and-topic-api
- description: Submit and manage AI-plus-human translation jobs.
  name: Unbabel Translation API
  slug: unbabel-translation-api
- description: Billable word count calculation for a block of text.
  name: Unbabel Word Count API
  slug: unbabel-word-count-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Unbabel Translation Account API
  slug: open-unbabel-account-api
- collection_type: open
  name: Unbabel Translation Account Language Pairs API
  slug: open-unbabel-language-pairs-api
- collection_type: open
  name: Unbabel Translation Account Machine Translation API
  slug: open-unbabel-machine-translation-api
- collection_type: open
  name: Unbabel Translation Account Tone and Topic API
  slug: open-unbabel-tone-and-topic-api
- collection_type: open
  name: Unbabel Account Translation API
  slug: open-unbabel-translation-api
- collection_type: open
  name: Unbabel Translation Account Word Count API
  slug: open-unbabel-word-count-api
- collection_type: open
  name: Unbabel Translation API
  slug: open-unbabel
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/unbabel-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/unbabel-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/unbabel-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unbabel-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unbabel-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Unbabel
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/unbabel
- group: company
  title: ''
  type: Website
  url: https://unbabel.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.unbabel.com
- group: commercial
  title: ''
  type: Plans
  url: plans/unbabel-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/unbabel-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/unbabel-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://unbabel.com/feed/
created: '2026-07-03'
description: Unbabel is a Language Operations (LangOps) platform that combines always-on AI translation with on-demand human review to localize customer support, marketing, and other business content at scale. Its long-standing developer surface is the Unbabel Translation API (tapi/v2, base https://api.unbabel.com/tapi/v2), an asynchronous REST API where callers submit text with a source/target language pair, tone, and topic, then retrieve the completed AI-plus-human translation by uid or via a callback. Unbabel also offers a pure machine-translation path (mt_translation) and helper resources for language pairs, tones, topics, word count, and account details. Unbabel has since launched the standalone LLM-based product Widn.AI (its own RESTful API at widn.ai) and, following its combination with TransPerfect, its research and models (TowerLLM, COMET, Widn.AI) now also feed the GlobalLink platform; the tapi/v2 Translation API remains the documented developer surface at developers.unbabel.com.
finops:
- name: Unbabel Finops
  service_category: AI and Machine Learning
  slug: unbabel-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unbabel.png
layout: provider
modified: '2026-07-03'
name: Unbabel
nav: Providers
network: true
overview: 'Unbabel publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Account API, Language Pairs API, Machine Translation API, and 3 more. Tagged areas include Translation, Localization, Language Operations, LangOps, and Machine Translation.


  Unbabel''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Unbabel Plans Pricing
  plan_count: 3
  slug: unbabel-plans-pricing
random_paper: 133
rate_limits:
- limit_count: 3
  name: Unbabel Rate Limits
  slug: unbabel-rate-limits
score:
  band: developing
  composite: 40.4
  delta: -0.9
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 57.3
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Unbabel Authentication
  slug: unbabel-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Unbabel Domain Security
  slug: unbabel-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Unbabel Vulnerability Disclosure
  slug: unbabel-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Unbabel Trust Center
  slug: unbabel-trust-center
  summary_line: ISO 27001, GDPR
slug: unbabel
tags:
- Translation
- Localization
- Language Operations
- LangOps
- Machine Translation
- Human in the Loop
- AI
website: https://unbabel.com
---
