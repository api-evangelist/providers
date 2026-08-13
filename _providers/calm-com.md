---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Calm Com Agentic Access
  operation_count: 3
  slug: calm-com-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 2
apis:
- description: OAuth 2.0 client credentials for partner services.
  name: Calm Authentication API
  slug: calm-com-authentication-api
- description: Provision and revoke Calm subscriptions linked to partner users.
  name: Calm Subscriptions API
  slug: calm-com-subscriptions-api
artifact_total: 29
collections:
- collection_type: open
  name: Calm Partner API
  slug: open-calm-partner-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/calm-com-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/calm-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/calm-com-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.calm.com
- group: start
  title: ''
  type: Portal
  url: https://www.calm.com
- group: start
  title: ''
  type: Signup
  url: https://www.calm.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://www.calm.com/subscribe
- group: docs
  title: ''
  type: Documentation
  url: https://partner.calm.com/docs/api
- group: docs
  title: ''
  type: Documentation
  url: https://partner.calm.com/docs/sso
- group: docs
  title: ''
  type: Documentation
  url: https://partner.calm.com/docs/sftp-instructions
- group: other
  title: ''
  type: Product
  url: https://business.calm.com
- group: other
  title: ''
  type: Product
  url: https://health.calm.com
- group: other
  title: ''
  type: Product
  url: https://app.calmhealth.com
- group: operate
  title: ''
  type: Support
  url: https://support.calm.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.calm.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.calm.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://blog.calm.com
- group: company
  title: ''
  type: Press
  url: https://www.calm.com/press
- group: company
  title: ''
  type: Careers
  url: https://www.calm.com/jobs
- group: operate
  title: ''
  type: Contact
  url: https://support.calm.com/hc/en-us/requests/new
- group: other
  title: ''
  type: AppStoreApple
  url: https://apps.apple.com/us/app/calm/id571800810
- group: other
  title: ''
  type: AppStoreGoogle
  url: https://play.google.com/store/apps/details?id=com.calm.android
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/calm
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/calm-com
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/calm
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/calm
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/calm.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/calm
created: '2026-05-25'
description: Calm is an American digital wellness company headquartered in San Francisco that builds a mobile and web app focused on mindfulness, meditation, sleep, and mental health. Founded in 2012 by Michael Acton Smith and Alex Tew, Calm offers guided meditations, Sleep Stories (long-form bedtime audio often narrated by celebrities), breathing exercises, mindfulness courses, music for focus and sleep, and a Daily Calm session. The consumer Calm app is distributed through the iOS App Store and Google Play under a freemium subscription model. The company also operates two B2B products. Calm Business sells the consumer experience to employers as an employee wellness benefit, and Calm Health is a clinical mental health offering for health plans and large self-insured employers, with structured programs aligned to clinical needs. Both B2B products are powered by the Calm Partner API (auth.calm.com/v0), a small OAuth 2.0 client-credentials REST surface that partner systems use to provision,
  link, and cancel Calm subscriptions for their members or employees. Partners also integrate via SAML 2.0 IdP-initiated SSO and SFTP-uploaded eligibility files (CSV at sftp.ws.calm.com:/inbound/eligibility/). Calm publishes a handful of open-source utilities under github.com/calm — primarily iOS audio/video helpers (PersistentStreamPlayer, KenBurns) and React-Intl ESLint plugins — but there is no public consumer-facing developer API.
examples:
- key_count: 2
  name: Calm Authorize Example
  slug: calm-authorize-example
- key_count: 2
  name: Calm Cancel User Example
  slug: calm-cancel-user-example
- key_count: 2
  name: Calm Link User Example
  slug: calm-link-user-example
features:
- Guided meditations across stress, anxiety, focus, and self-care libraries
- Sleep Stories — long-form bedtime audio narrated by well-known voices
- Daily Calm — a fresh 10-minute guided meditation every day
- Breathing exercises and breathwork programs
- Mindfulness and emotional-skill courses
- Calm Music — curated music for focus, relaxation, and sleep
- Calm Kids content library for children
- Soundscapes and nature audio
- Calm Business — employer-paid Calm benefit for employee wellness
- Calm Health — clinical mental health programs for health plans and self-insured employers
- Partner API with OAuth 2.0 client_credentials for subscription provisioning
- Partner SAML 2.0 IdP-initiated SSO with unique SubjectNameId
- SFTP eligibility file ingestion (CSV) at sftp.ws.calm.com:/inbound/eligibility/
- Partner Portal for administration, reporting, and segmentation
- iOS and Android apps plus a web experience at calm.com
- Available on Apple Watch, Apple TV, and Amazon Alexa
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/calm-com.png
json_schemas:
- name: Calm Eligibility File Row
  property_count: 4
  slug: calm-eligibility-file
- name: Calm Partner User
  property_count: 9
  slug: calm-partner-user
jsonld:
- class_count: 16
  name: Calm Com Context
  property_count: 2
  slug: calm-com-context
layout: provider
modified: '2026-05-25'
name: Calm
nav: Providers
network: true
overview: 'Calm publishes 2 APIs on the [APIs.io](https://apis.io/) network: Authentication API and Subscriptions API. Tagged areas include Mindfulness, Meditation, Sleep, Mental Health, and Wellness.


  The Calm catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Calm''s developer surface includes authentication, developer portal, signup flow, pricing, documentation, support, engineering blog, and 21 more developer resources.'
random_paper: 57
rules:
- name: Calm API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: calm-com-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.4
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 73.5
    developer_ergonomics: 34.8
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 45.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Calm Com Authentication
  slug: calm-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Calm Com Domain Security
  slug: calm-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: calm-com
tags:
- Mindfulness
- Meditation
- Sleep
- Mental Health
- Wellness
- Digital Health
- Mobile App
- Consumer
- Employee Wellness
- Digital Therapeutics
- B2B
website: https://www.calm.com
---
