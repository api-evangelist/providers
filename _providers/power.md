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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/power-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/power-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/power-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://www.withpower.com/security
- group: company
  title: ''
  type: Website
  url: https://www.withpower.com/
- group: company
  title: ''
  type: About
  url: https://www.withpower.com/about-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.withpower.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.withpower.com/privacy-policy
created: '2026-07-17'
description: Power (withpower.com) is a clinical-trial search and matching platform that helps patients find and enroll in research studies. It maintains a database of tens of thousands of active clinical trials searchable by condition, location, and drug type, and connects patients, providers, research coordinators, and trial sponsors. Added to the API Evangelist network as a portfolio company of Anthemis and CRV; no public API surface was found during enrichment.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/power.png
layout: provider
modified: '2026-07-20'
name: Power
nav: Providers
network: true
overview: Power is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Clinical Trials, Healthcare, Clinical Research, and Patient Matching.
random_paper: 11
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 1
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 14.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Power Domain Security
  slug: power-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Power Trust Center
  slug: power-trust-center
  summary_line: SOC 2, HIPAA
slug: power
tags:
- Company
- Clinical Trials
- Healthcare
- Clinical Research
- Patient Matching
- Health
website: https://www.withpower.com/
---
