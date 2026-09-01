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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ansible-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.ansiblehealth.com/
- group: company
  title: ''
  type: Blog
  url: https://www.ansiblehealth.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.ansiblehealth.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ansiblehealth.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ansiblehealth.com/terms-of-service
created: '2026-07-17'
description: AnsibleHealth is a virtual-first, doctor-led telemedicine practice specializing in the management of COPD, congestive heart failure, and other chronic pulmonary and cardiac conditions from home. Serving patients across 50+ states, it combines virtual diagnosis and personalized treatment plans, remote patient monitoring of vitals like heart rate and blood oxygen, virtual physical therapy, smoking-cessation coaching, and medication and durable-medical-equipment ordering to reduce hospitalizations and emergency-room use. The practice accepts Medicare, Medicaid, and most major commercial insurance plans. It was surfaced as a portfolio company of Bessemer Venture Partners and added to the API Evangelist network; it publishes a patient-facing website but no public developer API surface at this time.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ansible-health.png
layout: provider
modified: '2026-07-17'
name: Ansible Health
nav: Providers
network: true
overview: 'Ansible Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Telemedicine, Virtual Care, and COPD.


  Ansible Health''s developer surface includes engineering blog, support, and 4 more developer resources.'
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
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ansible-health/refs/heads/main/screenshots/ansible-health-2026-07-25T200309.png
security:
- kind: domain-security
  name: Ansible Health Domain Security
  slug: ansible-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ansible-health
tags:
- Company
- Healthcare
- Telemedicine
- Virtual Care
- COPD
- Chronic Care
- Remote Patient Monitoring
- Pulmonary
website: http://www.ansiblehealth.com/
---
