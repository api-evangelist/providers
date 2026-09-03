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
  url: security/carbon-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carbonhealth.com
- group: company
  title: ''
  type: Blog
  url: https://carbonhealth.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.carbonhealth.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carbonhealth.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carbonhealth.com/terms-of-use
created: '2026-07-17'
description: Carbon Health is a technology-enabled healthcare provider offering primary, urgent, virtual, and pediatric care through in-person clinics and telemedicine across the United States. It operates on its own clinical technology platform (CarbyOS) and offers services including same-day appointments, cold/flu/COVID testing, STI/STD testing, sports physicals, occupational and workplace health, and clinical research for sponsors. Carbon Health was surfaced as a portfolio company of 500 Global and DCVC and added to the API Evangelist network. No public developer API, OpenAPI, or FHIR patient-access surface was found during enrichment; this profile captures the company identity, public web properties, and domain-security posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carbon-health.png
layout: provider
modified: '2026-07-18'
name: Carbon Health
nav: Providers
network: true
overview: 'Carbon Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Telemedicine, Urgent Care, and Primary Care.


  Carbon Health''s developer surface includes engineering blog, support, and 4 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carbon-health/refs/heads/main/screenshots/carbon-health-2026-07-25T204512.png
security:
- kind: domain-security
  name: Carbon Health Domain Security
  slug: carbon-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: carbon-health
tags:
- Company
- Healthcare
- Telemedicine
- Urgent Care
- Primary Care
- Digital Health
- Clinical Research
website: https://carbonhealth.com
---
