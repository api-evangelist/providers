---
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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iris-telehealth-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://iristelehealth.com/
- group: company
  title: ''
  type: Blog
  url: https://iristelehealth.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://iristelehealth.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://iristelehealth.com/privacy-policy/
- group: company
  title: ''
  type: Careers
  url: https://iristelehealth.com/careers/
- group: company
  title: ''
  type: Newsletter
  url: https://iristelehealth.com/resources/newsletters/
- group: other
  title: ''
  type: Resources
  url: https://iristelehealth.com/resources/insights-center/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/iris-telehealth
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/iris-telehealth_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/iris-telehealth-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/iris-telehealth-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/iris-telehealth-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/iris-telehealth-plans-pricing.yml
coverage:
  checked: '2026-08-23'
  detail: 'Iris Telehealth sells clinician hours and a managed analytics service, not software an integrator can call: its own model is technology-agnostic — Iris psychiatrists work inside the partner health system''s existing EHR — so the only API in the workflow belongs to the partner''s Epic or Cerner instance, and the 69-page marketing site has no developer, docs, or API page at all, while the one API-shaped hostname it does publish, api.iristelehealth.com, resolves in DNS to 18.118.52.125 but refuses every connection on both 443 and 80 from the public internet.'
  evidence:
  - status: 0
    url: https://api.iristelehealth.com/
  - status: 404
    url: https://iristelehealth.com/openapi.json
  - status: 404
    url: https://iristelehealth.com/swagger.json
  - status: 404
    url: https://iristelehealth.com/api-docs
  - status: 404
    url: https://iristelehealth.com/graphql
  - status: 404
    url: https://iristelehealth.com/llms.txt
  - status: 404
    url: https://iristelehealth.com/.well-known/agent-card.json
  - status: 404
    url: https://iristelehealth.com/.well-known/agent.json
  - status: 404
    url: https://iristelehealth.com/.well-known/security.txt
  - status: 404
    url: https://iristelehealth.com/.well-known/api-catalog
  - status: 200
    url: https://iristelehealth.com/page-sitemap.xml
  - status: 200
    url: https://iristelehealth.com/wp-json/
  reason: no-developer-program
  state: none
created: '2026-08-23'
description: 'Iris Telehealth is an Austin, Texas telepsychiatry company, founded in 2013, that delivers virtual behavioral health care to healthcare organizations rather than direct to consumers. It contracts psychiatrists, psychiatric nurse practitioners, LCSWs and LPCs to hospitals and health systems, community mental health centers, community health centers and FQHCs, and Certified Community Behavioral Health Clinics, covering pediatric through geriatric populations and low-acuity therapy through high-acuity psychiatry. Its service lines are Virtual Clinic (comprehensive care and behavioral health integration), On-Demand Services (24/7 emergency department psychiatry support), Scheduled Services (matched provider staffing), Bridge Clinic, and Iris Insights, an AI-enabled behavioral health analytics platform covering risk optimization, capacity management, a behavioral health command center and revenue cycle analytics. The company reports over 430 clinicians and over 210 partner organizations,
  and has been accredited by the Joint Commission for behavioral health care since 2019, earning recertification since. Its delivery model is deliberately technology-agnostic: Iris clinicians work inside each partner''s existing EMR/EHR and e-prescribing tools over HIPAA-compliant video, so the integration burden sits with the partner''s systems. Iris Telehealth publishes no public developer program, API documentation, SDKs, or machine-readable API contract, and operates no public GitHub organization.'
image: https://iristelehealth.com/wp-content/uploads/2023/07/Home-page-preview_social-sharing-image_7.5.23-01.png
layout: provider
modified: '2026-08-23'
name: Iris Telehealth
nav: Providers
network: true
overview: 'Iris Telehealth is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Telehealth, Behavioral Health, and Mental Health.


  Iris Telehealth''s developer surface includes engineering blog, support, and 12 more developer resources.'
plans:
- name: Iris Telehealth Plans Pricing
  plan_count: 0
  slug: iris-telehealth-plans-pricing
random_paper: 7
score:
  band: emerging
  composite: 12.2
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 32.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Iris Telehealth Domain Security
  slug: iris-telehealth-domain-security
  summary_line: TLSv1.3 · DMARC
slug: iris-telehealth
tags:
- Company
- Healthcare
- Telehealth
- Behavioral Health
- Mental Health
- Telepsychiatry
- Clinical Services
- Health Systems
- Artificial Intelligence
- Analytics
website: https://iristelehealth.com/
---
