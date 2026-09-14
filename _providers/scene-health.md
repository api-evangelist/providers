---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scene-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.scene.health/
- group: company
  title: ''
  type: Blog
  url: https://www.scene.health/resources-category/blog
- group: operate
  title: ''
  type: Support
  url: https://www.scene.health/contact
- group: start
  title: ''
  type: SignUp
  url: https://www.scene.health/enroll/partner-name
- group: start
  title: ''
  type: Login
  url: https://app.emocha.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.scene.health/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.scene.health/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/emochamobilehealth
- group: auth
  title: ''
  type: Compliance
  url: https://www.scene.health/resources/our-ongoing-commitment-to-data-security-scene-health-renews-its-soc-2-audit
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/scene-health-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/scene-health-conformance.yml
coverage:
  checked: '2026-08-05'
  detail: 'Scene Health sells a staffed medication-adherence service, not a platform: the only software surface is the member and care-team login at app.emocha.com, a React SPA whose catch-all answers 200 with the same 999-byte shell for /openapi.json and every /.well-known/ path, and api./developer./docs.scene.health do not resolve at all.'
  evidence:
  - status: 200
    url: https://www.scene.health/llms.txt
  - status: 404
    url: https://www.scene.health/openapi.json
  - status: 404
    url: https://www.scene.health/.well-known/agent-card.json
  - status: 200
    url: https://app.emocha.com/zzz-nope-12345
  - status: 202
    url: https://emocha.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-08-05'
description: 'Scene Health (formerly emocha Mobile Health, founded 2008 out of Johns Hopkins and rebranded in 2022) is a Maryland-based digital health company tackling medication nonadherence. Its MedEngagement platform pairs a patient mobile app with a human care team of pharmacists, nurses and health coaches: members record daily video check-ins of themselves taking their medication — a scaled, asynchronous form of Directly Observed Therapy — and the care team reviews each dose, captures side effects and symptoms, and works barriers such as cost, transportation and social determinants of health. Scene sells to health plans and Medicaid MCOs, health systems, public health departments, employers, and research and clinical-trial organizations, with programs covering hypertension, diabetes, asthma, tuberculosis, HIV, hepatitis C, sickle cell disease, opioid use disorder and transplant care. The company raised a $17.7M Series B in March 2023 led by ABS Capital Partners. Scene operates as a
  HIPAA Business Associate and maintains a SOC 2 Type 2 attestation audited by A-LIGN across all five trust services criteria. It publishes no public developer program, API documentation or machine-readable API contract; its software surface is the member and care-team application at app.emocha.com.'
image: https://cdn.prod.website-files.com/6321d0ab8673ec82ca5ddfae/6333f381f9d1e91ba135da2a_Open_Graph_image_v1.jpg
layout: provider
modified: '2026-08-05'
name: Scene Health
nav: Providers
network: true
overview: 'Scene Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Digital Health, and Medication Adherence.


  Scene Health''s developer surface includes engineering blog, support, signup flow, and 9 more developer resources.'
random_paper: 4
screenshot: https://raw.githubusercontent.com/api-evangelist/scene-health/refs/heads/main/screenshots/scene-health-2026-09-02T154517.png
security:
- kind: domain-security
  name: Scene Health Domain Security
  slug: scene-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: scene-health
tags:
- Company
- Health
- Healthcare
- Digital Health
- Medication Adherence
- Patient Engagement
- Telehealth
- Medicaid
- Public Health
- Clinical Trials
website: https://www.scene.health/
---
