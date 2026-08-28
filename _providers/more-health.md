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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/more-health-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/more-health-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/more-health-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/more-health-llms.txt
- group: company
  title: ''
  type: Website
  url: https://morehealth.com/en
- group: company
  title: ''
  type: About
  url: https://morehealth.com/en/our-story
- group: operate
  title: ''
  type: Support
  url: https://morehealth.com/en/form/contact-us
- group: operate
  title: ''
  type: FAQ
  url: https://morehealth.com/en/faqs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://morehealth.com/en/termsofuse
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://morehealth.com/en/privacy
- group: other
  title: ''
  type: CookiePolicy
  url: https://morehealth.com/en/cookie-policy
- group: auth
  title: ''
  type: Compliance
  url: https://morehealth.com/en/security
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/more-health
coverage:
  checked: '2026-08-26'
  detail: MORE Health sells a cloud Physician Collaboration Platform to patients, employers and hospitals as an end-user product only — its 78-URL sitemap contains 26 marketing and policy pages per locale and not one developer, API, docs or status page, and api./developer./developers./docs./ app./portal./status./trust.morehealth.com all fail to resolve in DNS.
  evidence:
  - status: 200
    url: https://morehealth.com/sitemap.xml
  - status: 404
    url: https://morehealth.com/openapi.json
  - status: 404
    url: https://morehealth.com/llms.txt
  - status: 404
    url: https://morehealth.com/.well-known/agent-card.json
  - status: 404
    url: https://morehealth.com/.well-known/security.txt
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: MORE Health, Inc. is a global digital health company headquartered in San Mateo, California, with offices in Boston, Houston, New York, Beijing, Shanghai, Chengdu and Guangzhou. It provides expert medical second opinions and cross-border telemedicine through its proprietary, cloud-based Physician Collaboration Platform, which lets a patient's treating physician and an expert specialist jointly review medical history, hospital records, lab results, DICOM imaging, pathology imaging and genetic testing, and co-develop a diagnosis and treatment plan over HIPAA-compliant video conferencing with translation in 129 languages. Product lines include Expert Medical Opinion, MORE Health for Kids, employee benefits for self-insured groups, a Medical Travel Concierge, mental health, Prodigy Fertility and hospital solutions for health systems seeking international patient reach. The company states it serves 6.2 million members across six continents and that its platform is ISO 27001 certified
  and GDPR- and HIPAA-compliant. MORE Health publishes no public developer program, API reference, or machine-readable specification of any kind; the platform is sold to patients, employers and hospitals as an end-user product.
image: https://morehealth.com/brand/logo.png
layout: provider
modified: '2026-08-26'
name: MORE Health
nav: Providers
network: true
overview: 'MORE Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Digital Health, and Telemedicine.


  MORE Health''s developer surface includes support, FAQ, and 11 more developer resources.'
plans:
- name: More Health Plans Pricing
  plan_count: 0
  slug: more-health-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: More Health Rate Limits
  slug: more-health-rate-limits
score:
  band: emerging
  composite: 18.3
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: domain-security
  name: More Health Domain Security
  slug: more-health-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: trust-center
  name: More Health Trust Center
  slug: more-health-trust-center
  summary_line: HIPAA, GDPR, ISO 27001
slug: more-health
tags:
- Company
- Health
- Healthcare
- Digital Health
- Telemedicine
- Telehealth
- Second Opinion
- Medical Records
- Care Coordination
- Employee Benefits
- HIPAA
- Cross-Border Care
website: https://morehealth.com/en
---
