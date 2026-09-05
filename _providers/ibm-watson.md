---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 4
apis:
- description: Convert speech into text using AI-powered speech recognition and transcription. The service uses machine learning to combine knowledge of grammar, language structure, and audio signal composition to a
  name: IBM Watson Speech to Text
  slug: ibm-watson-speech-to-text
- description: Convert written text to natural-sounding audio in a variety of languages and voices. The service synthesizes natural language text to audio using deep learning AI for lifelike speech synthesis.
  name: IBM Watson Text to Speech
  slug: ibm-watson-text-to-speech
- description: Analyze text to extract metadata from content such as concepts, entities, keywords, categories, sentiment, emotion, relations, and semantic roles.
  name: IBM Watson Natural Language Understanding
  slug: ibm-watson-natural-language-understanding
- description: Build, train, and deploy conversational interactions into any application, device, or channel. Create AI-powered virtual agents that understand natural language and provide helpful responses.
  name: IBM Watson Assistant
  slug: ibm-watson-assistant
artifact_total: 9
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/ibm/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ibm-watson-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ibm-watson-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ibm-watson
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/ibm-watsonx
- group: company
  title: ''
  type: Website
  url: https://www.ibm.com/watson
- group: start
  title: ''
  type: Portal
  url: https://cloud.ibm.com/developer/watson/
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.ibm.com/docs/watson
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.ibm.com/developer/watson/documentation
- group: operate
  title: ''
  type: Support
  url: https://www.ibm.com/mysupport
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ibm.com/watson/pricing
created: '2024-03-30'
description: IBM Watson is IBM's AI and machine learning platform offering a suite of cloud-based services including natural language processing, speech recognition, visual recognition, and other AI-powered capabilities for building intelligent applications.
finops:
- name: Ibm Watson Finops
  service_category: API
  slug: ibm-watson-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ibm-watson.png
layout: provider
modified: '2026-08-21'
name: IBM Watson
nav: Providers
network: true
overview: 'IBM Watson publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, IBM, Machine-Learning, Natural Language Processing, and Speech Recognition.


  IBM Watson''s developer surface includes developer portal, documentation, getting-started guide, support, pricing, and 6 more developer resources.'
plans:
- name: Ibm Watson Plans Pricing
  plan_count: 3
  slug: ibm-watson-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Ibm Watson Rate Limits
  slug: ibm-watson-rate-limits
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 20.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ibm-watson/refs/heads/main/screenshots/ibm-watson-2026-06-20T183138.png
security:
- kind: domain-security
  name: Ibm Watson Domain Security
  slug: ibm-watson-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ibm Watson Vulnerability Disclosure
  slug: ibm-watson-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: ibm-watson
tags:
- Artificial Intelligence
- IBM
- Machine-Learning
- Natural Language Processing
- Speech Recognition
website: https://www.ibm.com/watson
---
