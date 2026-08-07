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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 2
apis:
- description: Enterprise Reports API for Kahoot! 360 organizations. Exposes data on games, users, participants, organizations, and kahoots created by the organization. Uses OAuth 2.0 client_credentials at https://a
  name: Kahoot! Reports API
  slug: reports-api
- description: Public API for Motimate (a Kahoot! company), the workplace learning and culture app. Gated to enterprise customers; documentation is hosted in the Kahoot! help center and authentication credentials ar
  name: Motimate Public API
  slug: motimate-public-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/kahoot-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kahoot-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kahoot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kahoot.com
- group: other
  title: ''
  type: Kahoot360
  url: https://kahoot360.com
- group: other
  title: ''
  type: Schools
  url: https://kahoot.com/schools/
- group: other
  title: ''
  type: Business
  url: https://kahoot.com/business/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.kahoot.com
- group: commercial
  title: ''
  type: Pricing
  url: https://kahoot.com/pricing/
- group: learn
  title: ''
  type: Academy
  url: https://academy.kahoot.com
- group: company
  title: ''
  type: Blog
  url: https://kahoot.com/blog/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.kahoot.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trust.kahoot.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trust.kahoot.com/terms-and-conditions/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/kahoot
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kahoot-
- group: company
  title: ''
  type: Twitter
  url: https://x.com/getkahoot
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/Kahoot
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/kahoot
- group: other
  title: ''
  type: IRPage
  url: https://kahoot.com/investor/
- group: agent
  title: ''
  type: LlmsText
  url: https://kahoot.it/llms.txt
created: '2026-05-23'
description: Kahoot! is a game-based learning and engagement platform used in schools, businesses, and at home. Its primary surface is the Kahoot! consumer/teacher product and the Kahoot! 360 enterprise tier, with integrations into Microsoft Teams, Zoom, RingCentral, PowerPoint, Google Slides, and LMSs (Cornerstone, Docebo, TalentLMS, Litmos, RiseUp, 360Learning, Absorb). For Kahoot! 360 enterprise customers, a Reports API is available (OAuth 2.0 client_credentials) for pulling games, users, participants, organizations, and kahoots data, and Motimate (acquired by Kahoot!) exposes a separate gated Public API. Access to both APIs is provisioned by a customer success manager and not publicly self-serve.
finops:
- name: Kahoot Finops
  service_category: API
  slug: kahoot-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kahoot.png
layout: provider
modified: '2026-05-23'
name: Kahoot!
nav: Providers
network: true
overview: 'Kahoot! publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Game-Based Learning, Education, Quiz, Engagement, and Enterprise Learning.


  Kahoot!''s developer surface includes pricing, academy / training, engineering blog, GitHub presence, YouTube channel, and 16 more developer resources.'
plans:
- name: Kahoot Plans Pricing
  plan_count: 1
  slug: kahoot-plans-pricing
random_paper: 81
rate_limits:
- limit_count: 2
  name: Kahoot Rate Limits
  slug: kahoot-rate-limits
score:
  band: emerging
  composite: 25.2
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 25.2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kahoot/refs/heads/main/screenshots/kahoot-2026-06-20T183854.png
security:
- kind: domain-security
  name: Kahoot Domain Security
  slug: kahoot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Kahoot Vulnerability Disclosure
  slug: kahoot-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Kahoot Trust Center
  slug: kahoot-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: kahoot
tags:
- Game-Based Learning
- Education
- Quiz
- Engagement
- Enterprise Learning
- Reporting
- OAuth
website: https://kahoot.com
---
