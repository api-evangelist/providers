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
  url: security/conformal-medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://conformalmedical.com/
- group: company
  title: ''
  type: About
  url: https://conformalmedical.com/company/about
- group: company
  title: ''
  type: News
  url: https://conformalmedical.com/company/news
- group: operate
  title: ''
  type: Support
  url: https://conformalmedical.com/company/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://conformalmedical.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://conformalmedical.com/privacy-policy-2
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/conformal-medical
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/conformal-medical_stock/
coverage:
  checked: '2026-08-09'
  detail: Conformal Medical is a Class III cardiac implant manufacturer (the CLAAS/AcuFORM LAAO system, acquired by W. L. Gore on 2026-02-19) whose conformalmedical.com site is a three-audience marketing brochure with no developer section at all — /developers, /api, /docs, /graphql and /llms.txt all return hard 404s against a control-verified 404 handler, and no GitHub organization or first-party package exists on any registry.
  evidence:
  - status: 404
    url: https://conformalmedical.com/developers
  - status: 404
    url: https://conformalmedical.com/openapi.json
  - status: 404
    url: https://conformalmedical.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/conformalmedical
  - status: 200
    url: https://conformalmedical.com/.well-known/security.txt
  reason: not-a-software-company
  state: none
created: '2026-08-09'
description: 'Conformal Medical, Inc. is a Nashua, New Hampshire medical device company developing the CLAAS (Conformal Left Atrial Appendage Seal) and next-generation CLAAS AcuFORM left atrial appendage occlusion (LAAO) systems, foam-based implants intended to seal the left atrial appendage and reduce stroke risk in patients with non-valvular atrial fibrillation without requiring pre-procedure CT sizing. The company runs the CONFORM pivotal IDE trial and the GLACE study, and publishes a public marketing site segmented for patients, physicians and company/investor audiences. W. L. Gore & Associates completed its acquisition of Conformal Medical on 2026-02-19. Conformal Medical is a regulated medical device manufacturer, not a software vendor: it operates no developer program, publishes no public API, SDK, webhook or machine-readable specification, and its only software artifacts are clinical-trial companion mobile apps for enrolled sites.'
layout: provider
modified: '2026-08-09'
name: Conformal Medical
nav: Providers
network: true
overview: 'Conformal Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Cardiology, and Medical Technology.


  Conformal Medical''s developer surface includes product news, support, and 7 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 3
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/conformal-medical/refs/heads/main/screenshots/conformal-medical-2026-09-02T145130.png
security:
- kind: domain-security
  name: Conformal Medical Domain Security
  slug: conformal-medical-domain-security
  summary_line: TLSv1.3 · DMARC
slug: conformal-medical
tags:
- Company
- Medical Devices
- Healthcare
- Cardiology
- Medical Technology
- Clinical Trials
- Stroke Prevention
website: https://conformalmedical.com/
---
