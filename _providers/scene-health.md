---
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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 3.6
  scored_at: '2026-08-11'
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
random_paper: 41
score:
  band: emerging
  composite: 20.4
  delta: -1.2
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 21.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
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
