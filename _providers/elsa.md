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
- acting_count: 2
  human_in_the_loop: 0
  name: Elsa Agentic Access
  operation_count: 2
  slug: elsa-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 2
apis:
- description: The Scripted API from ELSA — 1 operation(s) for scripted.
  name: ELSA Scripted API
  slug: elsa-scripted-api
- description: The Unscripted API from ELSA — 1 operation(s) for unscripted.
  name: ELSA Unscripted API
  slug: elsa-unscripted-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ELSA Speech Assessment Scripted API
  slug: open-elsa-scripted-api
- collection_type: open
  name: ELSA Speech Assessment Scripted Unscripted API
  slug: open-elsa-unscripted-api
- collection_type: open
  name: ELSA Speech Assessment API
  slug: open-elsa
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/elsa-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/elsa-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elsa-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/elsa-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/elsa
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/elsacorp
- group: company
  title: ''
  type: Website
  url: https://www.elsaspeak.com
- group: docs
  title: ''
  type: Documentation
  url: https://api-external-doc.elsanow.co/
- group: commercial
  title: ''
  type: Plans
  url: plans/elsa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/elsa-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/elsa-finops.yml
created: '2026-06-21'
description: ELSA (English Language Speech Assistant) builds AI speech-recognition and pronunciation-assessment technology for non-native English speakers, powering the ELSA Speak consumer app. The ELSA API is a partner/B2B speech-assessment service that scores recorded or streamed English audio across pronunciation, fluency, intonation, grammar, and vocabulary, returning sentence, word, and phoneme-level feedback.
finops:
- name: Elsa Finops
  service_category: AI and Machine Learning
  slug: elsa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/elsa.png
layout: provider
modified: '2026-06-21'
name: ELSA
nav: Providers
network: true
overview: 'ELSA publishes 2 APIs on the [APIs.io](https://apis.io/) network: Scripted API and Unscripted API. Tagged areas include Speech Assessment, Pronunciation, Speech Recognition, Language Learning, and AI.


  ELSA''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Elsa Plans Pricing
  plan_count: 3
  slug: elsa-plans-pricing
random_paper: 123
rate_limits:
- limit_count: 4
  name: Elsa Rate Limits
  slug: elsa-rate-limits
score:
  band: thin
  composite: 37.1
  delta: -0.9
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.5
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/elsa/refs/heads/main/screenshots/elsa-2026-07-25T213209.png
security:
- kind: authentication
  name: Elsa Authentication
  slug: elsa-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Elsa Domain Security
  slug: elsa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Elsa Vulnerability Disclosure
  slug: elsa-vulnerability-disclosure
  summary_line: disclosure policy published
slug: elsa
tags:
- Speech Assessment
- Pronunciation
- Speech Recognition
- Language Learning
- AI
website: https://www.elsaspeak.com
---
