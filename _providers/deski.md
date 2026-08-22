---
agent_readiness:
  band: agent-aware
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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.4
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deski-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.heartfocus.ai/
- group: other
  title: ''
  type: Product
  url: https://www.heartfocus.ai/product
- group: other
  title: ''
  type: Product
  url: https://www.heartfocus.ai/heartfocus-link
- group: other
  title: ''
  type: Product
  url: https://www.heartfocus.ai/pocus-heartfocus-certification
- group: docs
  title: ''
  type: Documentation
  url: https://www.heartfocus.ai/user-manuals
- group: operate
  title: ''
  type: FAQ
  url: https://www.heartfocus.ai/faq-heartfocus
- group: operate
  title: ''
  type: FAQ
  url: https://www.heartfocus.ai/faq-heartfocus-link
- group: learn
  title: ''
  type: Training
  url: https://www.heartfocus.ai/training
- group: commercial
  title: ''
  type: Pricing
  url: https://www.heartfocus.ai/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/deski-plans-pricing.yml
- group: start
  title: ''
  type: SignUp
  url: https://portal.heartfocus.ai/signup
- group: start
  title: ''
  type: Login
  url: https://portal.heartfocus.ai/login
- group: operate
  title: ''
  type: Support
  url: https://www.heartfocus.ai/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.heartfocus.ai/news
- group: other
  title: ''
  type: Whitepapers
  url: https://www.heartfocus.ai/white-papers-and-publications
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.heartfocus.ai/heartfocus-software-license-agreement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.heartfocus.ai/portal-terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.heartfocus.ai/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.heartfocus.ai/security/cvd
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/deski-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.heartfocus.ai/hipaa-hbnr-applicability-statement
- group: design
  title: ''
  type: Conformance
  url: conformance/deski-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/deski-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/deski-llms.txt
- group: company
  title: ''
  type: Careers
  url: https://www.heartfocus.ai/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.heartfocus.ai/contact-us
- group: commercial
  title: ''
  type: LegalNotice
  url: https://www.heartfocus.ai/legal-information
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/deski/
coverage:
  checked: '2026-08-17'
  detail: 'DESKi ships regulated end-user software, not a platform: HeartFocus is an FDA-cleared iPhone/iPad app whose only machine-facing interface is a DICOM push to a PACS the customer configures in-app, and the DICOM conformance statement that would describe it is available only by emailing support@deski.ai — /openapi.json, /graphql, /llms.txt and every /.well-known/* path return a real 404 on www.heartfocus.ai and deski.ai, api./developer./link.heartfocus.ai do not resolve in DNS, docs.heartfocus.ai is an S3 bucket returning 403 AccessDenied, and portal.heartfocus.ai is a licence-management SPA that answers 200 with the same 467-byte HTML shell for every path probed.'
  evidence:
  - status: 404
    url: https://www.heartfocus.ai/openapi.json
  - status: 404
    url: https://www.heartfocus.ai/graphql
  - status: 404
    url: https://www.heartfocus.ai/llms.txt
  - status: 404
    url: https://www.heartfocus.ai/.well-known/agent-card.json
  - status: 404
    url: https://www.heartfocus.ai/.well-known/security.txt
  - status: 404
    url: https://deski.ai/.well-known/agent.json
  - status: 403
    url: https://docs.heartfocus.ai/
  - status: 200
    url: https://portal.heartfocus.ai/openapi.json
  - status: 200
    url: https://www.heartfocus.ai/security/cvd
  - status: 200
    url: https://www.heartfocus.ai/pricing
  reason: no-developer-program
  state: none
created: '2026-08-17'
description: 'DESKi is a French medical-device software company founded in 2016 in Bordeaux by brothers Bertrand and Olivier Moal, trading publicly under its HeartFocus brand. Its flagship product, HeartFocus, is an FDA-cleared AI cardiac imaging app that runs on iPhone and iPad with Butterfly Network iQ+ and iQ3 handheld ultrasound probes, giving any healthcare professional real-time probe guidance, automatic diagnostic-quality clip recording and live view validation across the 10 standard transthoracic echocardiographic views (PLAX, PSAX-AV, PSAX-MV, PSAX-PM, A4C, A5C, A2C, A3C, SC-4C, SC-IVC). A second product, HeartFocus Link, adds the same AI guidance to existing cart-based ultrasound systems from GE HealthCare, Philips, Siemens Healthineers, Mindray, FUJIFILM Sonosite, Samsung and Canon over a plain HDMI capture path, for education and training only. DESKi holds two FDA 510(k) clearances (K242807, 2025-04-04; K260780, 2026-06-03, product code QJU) and publishes a Coordinated Vulnerability
  Disclosure process, a HIPAA & HBNR applicability statement, per-probe list pricing and dated electronic instructions for use. Its only machine-facing integration surface is DICOM: exams are transferred from the mobile app to a customer-configured PACS server (server and client AE titles, host, port, optional TLS), and the DICOM conformance statement and CycloneDX SBOM are available only by emailing support. DESKi publishes no public REST or GraphQL API, no OpenAPI or AsyncAPI specification, no SDK, no CLI, no MCP server and no developer portal; portal.heartfocus.ai is a customer licence-management application, not a developer surface.'
image: https://cdn.prod.website-files.com/6634a89a6fab56ada55e9d51/67b5d8e31ab3b8fe2d8e6bd2_DESKi%20Logo.png
layout: provider
modified: '2026-08-17'
name: DESKi
nav: Providers
network: true
overview: 'DESKi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthtech, Medical Imaging, Cardiology, and Ultrasound.


  DESKi''s developer surface includes documentation, FAQ, training material, pricing, signup flow, support, engineering blog, and 22 more developer resources.'
plans:
- name: Deski Plans Pricing
  plan_count: 3
  slug: deski-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Deski Rate Limits
  slug: deski-rate-limits
score:
  band: thin
  composite: 32.1
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 10.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
security:
- kind: domain-security
  name: Deski Domain Security
  slug: deski-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Deski Vulnerability Disclosure
  slug: deski-vulnerability-disclosure
  summary_line: contact published
slug: deski
tags:
- Company
- Healthtech
- Medical Imaging
- Cardiology
- Ultrasound
- Point-of-Care Ultrasound
- Artificial Intelligence
- Medical Device
- DICOM
- France
website: https://www.heartfocus.ai/
---
