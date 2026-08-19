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
- acting_count: 1
  human_in_the_loop: 0
  name: Google Cloud Text To Speech Agentic Access
  operation_count: 2
  slug: google-cloud-text-to-speech-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 2
apis:
- description: The Text:synthesize API from Google Cloud Text-To-Speech — 1 operation(s) for text:synthesize.
  name: Google Cloud Text-To-Speech Text:synthesize API
  slug: google-cloud-text-to-speech-text-synthesize-api
- description: The Voices API from Google Cloud Text-To-Speech — 1 operation(s) for voices.
  name: Google Cloud Text-To-Speech Voices API
  slug: google-cloud-text-to-speech-voices-api
artifact_total: 17
collections:
- collection_type: postman
  name: Google Cloud Text-to-Speech Text:synthesize API
  slug: postman-google-cloud-text-to-speech-text-synthesize-api
- collection_type: postman
  name: Google Cloud Text-to-Speech Text:synthesize Voices API
  slug: postman-google-cloud-text-to-speech-voices-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Text-to-Speech Text:synthesize API
  slug: open-google-cloud-text-to-speech-text-synthesize-api
- collection_type: open
  name: Google Cloud Text-to-Speech Text:synthesize Voices API
  slug: open-google-cloud-text-to-speech-voices-api
- collection_type: open
  name: Google Cloud Text-to-Speech API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-text-to-speech/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-text-to-speech-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-text-to-speech-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-text-to-speech-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/text-to-speech
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/text-to-speech/docs/quickstart-client-libraries
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/text-to-speech/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/text-to-speech/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/text-to-speech/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://cloud.google.com/feeds/tts-release-notes.xml
created: '2026-03-13'
description: Google Cloud Text-to-Speech converts text or Speech Synthesis Markup Language (SSML) input into audio data of natural human speech. It provides access to hundreds of voices across multiple languages and variants, powered by DeepMind's WaveNet technology and Google's neural network models.
finops:
- name: Google Cloud Text To Speech Finops
  service_category: API
  slug: google-cloud-text-to-speech-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-text-to-speech.png
json_schemas:
- name: Speech Synthesis Request
  property_count: 3
  slug: speech-synthesis
jsonld:
- class_count: 13
  name: context Context
  property_count: 0
  slug: context
layout: provider
modified: '2026-05-19'
name: Google Cloud Text-To-Speech
nav: Providers
network: true
overview: 'Google Cloud Text-To-Speech publishes 2 APIs on the [APIs.io](https://apis.io/) network: Text:synthesize API and Voices API. Tagged areas include Audio, Google Cloud, Machine Learning, Speech Synthesis, and Text-To-Speech.


  The Google Cloud Text-To-Speech catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Text-To-Speech''s developer surface includes developer portal, getting-started guide, documentation, authentication, pricing, support, engineering blog, and 9 more developer resources.'
plans:
- name: Google Cloud Text To Speech Plans Pricing
  plan_count: 3
  slug: google-cloud-text-to-speech-plans-pricing
random_paper: 131
rate_limits:
- limit_count: 5
  name: Google Cloud Text To Speech Rate Limits
  slug: google-cloud-text-to-speech-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Cloud Text-To-Speech API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-text-to-speech-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.1
  delta: -6.2
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 60.8
    developer_ergonomics: 54.8
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 53.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-text-to-speech/refs/heads/main/screenshots/google-cloud-text-to-speech-2026-06-20T182149.png
security:
- kind: domain-security
  name: Google Cloud Text To Speech Domain Security
  slug: google-cloud-text-to-speech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Text To Speech Vulnerability Disclosure
  slug: google-cloud-text-to-speech-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-text-to-speech
tags:
- Audio
- Google Cloud
- Machine Learning
- Speech Synthesis
- Text-To-Speech
website: https://cloud.google.com/text-to-speech
---
