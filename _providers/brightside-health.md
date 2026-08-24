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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brightside-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brightside.com/
- group: company
  title: ''
  type: About
  url: https://www.brightside.com/about/
- group: operate
  title: ''
  type: Support
  url: https://www.brightside.com/contact/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.brightside.com/faq/
- group: company
  title: ''
  type: Blog
  url: https://www.brightside.com/blog/
- group: company
  title: ''
  type: Press
  url: https://www.brightside.com/press-releases/
- group: company
  title: ''
  type: Partners
  url: https://www.brightside.com/partners/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.brightside.com/online-care-affordable/
- group: start
  title: ''
  type: SignUp
  url: https://app.brightside.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brightside.com/tou/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brightside.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/brightsidehealth
- group: auth
  title: ''
  type: Compliance
  url: https://www.brightside.com/about/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/brightside-health-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/brightside-health-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/brightside-health-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/brightside-health-lifecycle.yml
- group: company
  title: ''
  type: Careers
  url: https://www.brightside.com/careers/
coverage:
  checked: '2026-08-15'
  detail: Brightside Health markets a real programmatic surface to health systems — "Integration with your EHR for seamless discharge planning", "ADT notifications" and a Patient Referral Portal — but the only route to it is a "Contact our Partnership Team / Get in touch" form; the 2026-08-15 sweep confirmed api.brightside.com IS a live versioned Rails REST API whose /v1/ and /api/v1/ paths reach the origin (JSON envelope {"errors":["Record not found"]}) while every other path is held behind a Cloudflare bot challenge, and no route index, schema, docs or specification endpoint exists on it — the only public machine-readable surface on any Brightside host is the marketing site's WordPress REST index at /wp-json/, which is CMS boilerplate, not a product API.
  evidence:
  - status: 200
    url: https://www.brightside.com/partners/health-systems/
  - status: 404
    url: https://api.brightside.com/v1/openapi.json
  - status: 403
    url: https://api.brightside.com/openapi.json
  - status: 200
    url: https://www.brightside.com/wp-json/
  - status: 404
    url: https://www.brightside.com/developers/
  - status: 0
    url: https://developer.brightside.com/
  - status: 200
    url: https://www.brightside.com/llms.txt
  reason: sales-gate
  state: gated
created: '2026-08-08'
description: Brightside Health is a U.S. national telehealth provider of evidence-based psychiatry (medication management) and therapy for people aged 13 and older, founded in 2017 and headquartered in San Francisco. It treats the full acuity spectrum — depression, anxiety, bipolar and mood disorders, OCD, PTSD, ADHD, insomnia, substance and alcohol use disorder, and behavioral addictions — using measurement-based care (PHQ-9/GAD-7 tracking) and precision prescribing, and runs virtual Intensive Outpatient Programs plus an evidence-based Suicide Prevention Program (Crisis Care) for elevated suicide risk. Care is delivered in all 50 states, in-network with Aetna, Cigna, Optum/UnitedHealthcare, Blue Cross Blue Shield, Ambetter, Medicare and Medicaid, alongside self-pay. The platform is HIPAA compliant and has earned HITRUST Certified status for information security. Brightside sells to health plans, health systems and medical groups with EHR integration, ADT notifications and a patient referral
  portal, but publishes no public developer program, API reference or machine-readable specification — partner integration is arranged through its partnerships team.
image: https://www.brightside.com/wp-content/uploads/2023/05/social-share-banner.png
layout: provider
modified: '2026-08-15'
name: Brightside Health
nav: Providers
network: true
overview: 'Brightside Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Telehealth, Mental Health, Behavioral Health, Psychiatry, and Therapy.


  Brightside Health''s developer surface includes support, engineering blog, pricing, signup flow, and 15 more developer resources.'
plans:
- name: Brightside Health Plans Pricing
  plan_count: 0
  slug: brightside-health-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Brightside Health Rate Limits
  slug: brightside-health-rate-limits
score:
  band: emerging
  composite: 19.3
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 19.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Brightside Health Domain Security
  slug: brightside-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brightside-health
tags:
- Telehealth
- Mental Health
- Behavioral Health
- Psychiatry
- Therapy
- Digital Health
- Healthcare
- Telemedicine
- Medication Management
- Substance Use Disorder
- Suicide Prevention
- Health Plans
website: https://www.brightside.com/
---
