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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/talkspace-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.talkspace.com
- group: start
  title: ''
  type: Login
  url: https://app.talkspace.com
- group: other
  title: ''
  type: FindTherapist
  url: https://match.talkspace.com/dispatcher
- group: other
  title: ''
  type: Therapy
  url: https://www.talkspace.com/online-therapy
- group: other
  title: ''
  type: TeenTherapy
  url: https://www.talkspace.com/online-therapy/teens
- group: other
  title: ''
  type: CouplesTherapy
  url: https://www.talkspace.com/online-therapy/couples
- group: start
  title: ''
  type: Psychiatry
  url: https://www.talkspace.com/psychiatry
- group: other
  title: ''
  type: Medications
  url: https://www.talkspace.com/medications
- group: other
  title: ''
  type: Chapters
  url: https://www.talkspace.com/chapters
- group: other
  title: ''
  type: Insurance
  url: https://www.talkspace.com/insurance
- group: other
  title: ''
  type: Business
  url: https://business.talkspace.com
- group: build
  title: ''
  type: Clinicians
  url: https://www.talkspace.com/therapist-jobs
- group: other
  title: ''
  type: Research
  url: https://www.talkspace.com/research
- group: other
  title: ''
  type: Review
  url: https://www.talkspace.com/online-therapy/reviews
- group: company
  title: ''
  type: Blog
  url: https://www.talkspace.com/blog
- group: company
  title: ''
  type: Press
  url: https://www.talkspace.com/press
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.talkspace.com
- group: company
  title: ''
  type: Careers
  url: https://www.talkspace.com/careers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.talkspace.com/public/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.talkspace.com/public/terms
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/talkspace
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/talkspace
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/Talkspacetherapy
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/talkspace
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/talkspace
created: '2026-05-25'
description: Talkspace is a New York City-based online behavioral healthcare company founded in 2012 by Oren Frank and Roni Frank that delivers virtual therapy, psychiatry, and medication management through video, voice, messaging, and live chat. The platform connects users with licensed therapists and psychiatric providers across all 50 U.S. states, covering more than 150 mental health conditions including anxiety, depression, ADHD, bipolar disorder, OCD, PTSD, insomnia, postpartum depression, and substance use. Service lines include individual therapy for adults, teen therapy (ages 13-17), couples therapy, psychiatry with prescription management, and specialized programs for LGBTQIA+, military/veteran, and senior populations, plus the women's mental health program Chapters. Talkspace is in-network with major payers such as Aetna, Anthem, Cigna, Optum, Blue Cross Blue Shield, TRICARE, and Medicare, and sells B2B solutions (Talkspace for Business) to employers, payers, benefit consultants,
  educational institutions, and government agencies. The company markets Precision Therapy, an internal machine-learning and NLP system used to match members to providers and surface clinical signal. Talkspace went public on NASDAQ under ticker TALK on June 23, 2021 via a SPAC merger with Hudson Executive Investment Corp, and was acquired by Universal Health Services on March 9, 2026. Talkspace does not publish a public developer API, SDK, or open-source repository; integrations with payers, EAPs, and benefits platforms are delivered through private partnership channels, and the platform is HIPAA, HITECH, and GDPR compliant.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/talkspace.png
layout: provider
modified: '2026-05-25'
name: Talkspace
nav: Providers
network: true
overview: 'Talkspace is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Behavioral Health, Mental Health, Online Therapy, Telehealth, and Psychiatry.


  Talkspace''s developer surface includes engineering blog, YouTube channel, and 24 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/talkspace/refs/heads/main/screenshots/talkspace-2026-06-20T194906.png
security:
- kind: domain-security
  name: Talkspace Domain Security
  slug: talkspace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: talkspace
tags:
- Behavioral Health
- Mental Health
- Online Therapy
- Telehealth
- Psychiatry
- Medication Management
- Teen Therapy
- Couples Therapy
- Employee Assistance
- Health Insurance
- HIPAA
- Public Company
website: https://www.talkspace.com
---
