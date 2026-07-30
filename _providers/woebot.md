---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Gated partner API library for integrating the Woebot Health Platform into a partner's digital front door, EMR, or care pathway. Supports transmission of aggregated data including patient-reported outc
  name: Woebot Health Partner API
  slug: partner-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/woebot-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/woebot-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/woebot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://woebothealth.com
- group: other
  title: ''
  type: Research
  url: https://woebothealth.com/research/
- group: build
  title: ''
  type: ClinicalEvidence
  url: https://woebothealth.com/clinical-evidence/
- group: other
  title: ''
  type: ForProviders
  url: https://woebothealth.com/providers/
- group: other
  title: ''
  type: ForPayers
  url: https://woebothealth.com/payers/
- group: other
  title: ''
  type: ForEmployers
  url: https://woebothealth.com/employers/
- group: company
  title: ''
  type: About
  url: https://woebothealth.com/about/
- group: company
  title: ''
  type: Newsroom
  url: https://woebothealth.com/newsroom/
- group: company
  title: ''
  type: Blog
  url: https://woebothealth.com/blog/
- group: company
  title: ''
  type: Careers
  url: https://woebothealth.com/careers/
- group: auth
  title: ''
  type: TrustCenter
  url: https://woebothealth.com/trust/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://woebothealth.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://woebothealth.com/terms-of-service/
- group: operate
  title: ''
  type: Contact
  url: https://woebothealth.com/contact/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/woebothealth
- group: company
  title: ''
  type: Twitter
  url: https://x.com/woebothealth
created: '2026-05-23'
description: Woebot Health is a clinical mental health company founded in 2017 by Dr. Alison Darcy that delivers an AI-powered, CBT-based conversational agent ("Woebot") for evidence-based mental health support. The company operates an enterprise (B2B) model, partnering with health systems, payers, employers, and providers to embed Woebot into existing care pathways and digital front doors. The Woebot Health Platform offers a partner API library for transmitting aggregated, validated patient-reported outcomes (PHQ-8/PHQ-9, engagement, satisfaction, topic modeling) into EMRs and value-based care workflows. The partner API is gated to enterprise customers — there is no public REST API, OpenAPI specification, or self-serve developer portal.
finops:
- name: Woebot Finops
  service_category: API
  slug: woebot-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/woebot.png
layout: provider
modified: '2026-05-23'
name: Woebot Health
nav: Providers
network: true
overview: 'Woebot Health publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Mental Health, Digital Therapeutics, CBT, Chatbot, and Clinical.


  Woebot Health''s developer surface includes engineering blog and 18 more developer resources.'
plans:
- name: Woebot Plans Pricing
  plan_count: 1
  slug: woebot-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Woebot Rate Limits
  slug: woebot-rate-limits
score:
  band: emerging
  composite: 23.1
  delta: -5.5
  facets:
    commercial_clarity: 57.9
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 28.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/woebot/refs/heads/main/screenshots/woebot-2026-06-20T201534.png
security:
- kind: domain-security
  name: Woebot Domain Security
  slug: woebot-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Woebot Vulnerability Disclosure
  slug: woebot-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Woebot Trust Center
  slug: woebot-trust-center
  summary_line: HIPAA, GDPR
slug: woebot
tags:
- Mental Health
- Digital Therapeutics
- CBT
- Chatbot
- Clinical
- Healthcare
- B2B
- Enterprise
website: https://woebothealth.com
---
