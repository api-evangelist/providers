---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/remind-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/remind-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.remind.com
- group: other
  title: ''
  type: Chat
  url: https://www.remind.com/chat
- group: other
  title: ''
  type: Hub
  url: https://www.remind.com/hub
- group: build
  title: ''
  type: ShareSDK
  url: https://engineering.remind.com/remind-share-sdk/
- group: build
  title: ''
  type: ComposerIntegration
  url: https://engineering.remind.com/remind-share-sdk/composer/
- group: docs
  title: ''
  type: BrandGuidelines
  url: https://engineering.remind.com/remind-share-sdk/brand/
- group: other
  title: ''
  type: Engineering
  url: https://engineering.remind.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.remind.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.remind.com/pricing
- group: commercial
  title: ''
  type: Privacy
  url: https://www.remind.com/privacy
- group: commercial
  title: ''
  type: Terms
  url: https://www.remind.com/terms-of-service
- group: other
  title: ''
  type: ParentCompany
  url: https://www.parentsquare.com
- group: other
  title: ''
  type: AcquisitionAnnouncement
  url: https://www.parentsquare.com/blog/parentsquare-acquires-remind-expanding-options-for-school-home-engagement/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/remind101
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/RemindHQ
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/remind101
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/remindhq
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/RemindHQ
- group: other
  title: ''
  type: GooglePlay
  url: https://play.google.com/store/apps/details?id=com.remind101
- group: operate
  title: ''
  type: PartnerContact
  url: mailto:partners@remind.com
created: '2026-05-25'
description: Remind is a K-12 school-home communication platform that lets teachers, schools, and districts message students and families by text, app, email, and voice without exchanging personal phone numbers. The product line includes Remind Chat, a free two-way messaging service used by individual teachers and classrooms, and Remind Hub, a paid district-wide communications platform with administrative controls, SIS integration, delivery analytics, and translation into 90+ languages. Remind reports use in roughly 80% of US public schools and by a majority of US teachers. In November 2023, Santa Barbara-based ParentSquare acquired Remind, and the combined company now operates under the ParentSquare name with Remind Hub continuing for existing district customers and Remind Chat continuing for classroom-level use; Remind Tutoring was discontinued as part of the combination. Remind's only externally documented developer surface is the Share on Remind SDK (the "Remind Share SDK"), a partner
  program that lets approved third-party content providers embed the Remind composer into their own product, authenticate Remind users via OAuth 2.0, serve shareable content and previews via partner-hosted webhooks, and ship messages back through Remind. The Share SDK is accessed by application through partners@remind.com and the developer console at remind.com/integrations; there is no public self-serve REST API, no published OpenAPI specification, and no general-purpose messaging API for sending Remind messages from third-party systems.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/remind.png
layout: provider
modified: '2026-05-25'
name: Remind
nav: Providers
network: true
overview: 'Remind is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Messaging, Communication, Education, K-12, and School Communication.


  Remind''s developer surface includes pricing, privacy policy, terms of service, GitHub presence, YouTube channel, and 17 more developer resources.'
random_paper: 27
score:
  band: minimal
  composite: 12.5
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 12.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/remind/refs/heads/main/screenshots/remind-2026-06-20T192839.png
security:
- kind: domain-security
  name: Remind Domain Security
  slug: remind-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Remind Vulnerability Disclosure
  slug: remind-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: remind
tags:
- Messaging
- Communication
- Education
- K-12
- School Communication
- Parent Engagement
- Teacher Messaging
- SMS
- Translation
- OAuth
- Webhooks
- Share SDK
- ParentSquare
website: https://www.remind.com
---
