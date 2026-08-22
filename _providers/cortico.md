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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cortico-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cortico.health/
- group: company
  title: ''
  type: About
  url: https://cortico.health/about/
- group: commercial
  title: ''
  type: Pricing
  url: https://cortico.health/pricing/
- group: company
  title: ''
  type: Blog
  url: https://cortico.health/article/
- group: operate
  title: ''
  type: Support
  url: https://cortico.health/resources/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cortico-health
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cortico.health/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cortico.health/legal/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cortico-llms.txt
created: '2026-07-24'
description: 'Cortico (Cortico Health Technologies) is a Vancouver, British Columbia based healthcare connection platform, founded in 2019, that links patients, medical clinics, and health records across Canada and the United States. Its patient-engagement suite layers online booking, automated appointment reminders, secure two-way patient messaging, digital intake forms, telemedicine, specialist e-referrals, payments, and AI-driven administrative automation on top of the electronic medical records (EMRs) clinics already run — most notably a supported two-way integration with OSCAR EMR through that system''s REST/SOAP web services, plus SMART on FHIR contextual launch and robotic process automation (RPA). Cortico is SOC 2 Type II and ISO 27001 certified and compliant with HIPAA, PIPEDA, and PHIPA. Cortico consumes EMR and FHIR interfaces rather than publishing its own public developer API: as of this review there is no public developer portal, API reference, or FHIR CapabilityStatement,
  and integration is delivered through a partnership and onboarding model rather than self-serve API access.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Cortico
nav: Providers
network: true
overview: 'Cortico is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Canada, Patient Engagement, EMR, and OSCAR EMR.


  Cortico''s developer surface includes pricing, engineering blog, support, and 7 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 13.6
  delta: -1.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 14.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cortico/refs/heads/main/screenshots/cortico-2026-07-25T210445.png
security:
- kind: domain-security
  name: Cortico Domain Security
  slug: cortico-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cortico
tags:
- Healthcare
- Canada
- Patient Engagement
- EMR
- OSCAR EMR
- SMART on FHIR
- Telemedicine
- Clinical Workflow Automation
- Interoperability
website: https://cortico.health/
---
