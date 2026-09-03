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
artifact_total: 2
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/omada-health-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/omada-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.omadahealth.com
- group: company
  title: ''
  type: About
  url: https://www.omadahealth.com/about-us
- group: operate
  title: ''
  type: Support
  url: https://support.omadahealth.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.omadahealth.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.omadahealth.com/terms-of-use
- group: auth
  title: ''
  type: Compliance
  url: https://www.omadahealth.com/about-us/security
- group: design
  title: ''
  type: Conformance
  url: conformance/omada-health-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/omada-health-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.omadahealth.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/omada-health-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.omadahealth.com/resource-center-latest
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/omadahealth
created: '2026-07-17'
description: Omada Health is a virtual-first healthcare company founded in 2011 and headquartered in San Francisco that delivers integrated, evidence-based care programs for chronic disease management. Omada combines one-on-one health coaching, connected smart devices (cellular scales, blood pressure monitors, glucose meters), interactive lessons, and peer communities to support people managing prediabetes, type 2 diabetes, hypertension, high cholesterol, and musculoskeletal (MSK) conditions, along with GLP-1 medication support and weight health. The company sells to employers, health plans, benefit consultants, and health systems rather than to individual consumers directly, and operates as a HIPAA covered entity and business associate. Omada Health is publicly traded and is a portfolio company of Andreessen Horowitz (a16z). It has no publicly documented developer API surface; this profile captures the company's public identity, security/compliance posture, and operational transparency
  pages.
image: https://www.omadahealth.com/hs-fs/hubfs/omada_logo_horizontal.png?name=omada_logo_horizontal.png
layout: provider
modified: '2026-08-08'
name: Omada Health
nav: Providers
network: true
overview: 'Omada Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Digital Health, Virtual Care, Chronic Disease Management, and Diabetes.


  Omada Health''s developer surface includes support, engineering blog, and 12 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 20.8
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 20.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/omada-health/refs/heads/main/screenshots/omada-health-2026-08-07T190132.png
security:
- kind: domain-security
  name: Omada Health Domain Security
  slug: omada-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Omada Health Trust Center
  slug: omada-health-trust-center
  summary_line: SOC 2, HITRUST CSF, HIPAA
slug: omada-health
tags:
- Company
- Digital Health
- Virtual Care
- Chronic Disease Management
- Diabetes
- Hypertension
- Healthcare
- HIPAA
- Telehealth
website: https://www.omadahealth.com
---
