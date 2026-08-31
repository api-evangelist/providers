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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/claimsforce-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/claimsforce-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.claimsforce.com/iso-iec-27001-zertifikat
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/claimsforce-llms.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.claimsforce.com/datenschutz
- group: start
  title: ''
  type: Login
  url: https://web.claimsforce.com/login
- group: company
  title: ''
  type: Website
  url: https://www.claimsforce.com
created: '2026-07-17'
description: claimsforce GmbH is a Hamburg-based insurtech building AI-powered software for property and casualty claims management and underwriting. Its platform helps insurers, loss-adjusting and expert organizations, and independent adjusters digitize the end-to-end claims process - automating report and calculation generation, enabling video-based remote case assessment, optimizing adjuster disposition and route planning to cut travel time, and surfacing real-time analytics for claims handling and risk management. Named customers include Zurich Gruppe Deutschland, HanseMerkur, Concordia, Crawford, Sedgwick and Die Regulierer. The product is a private, login-only SaaS with no public API or developer portal as of July 2026. The company is ISO/IEC 27001:2022 certified (TUV Rheinland) and backed by Point Nine.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/claimsforce.png
layout: provider
modified: '2026-07-18'
name: claimsforce
nav: Providers
network: true
overview: claimsforce is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Insurtech, Claims Management, and Underwriting.
random_paper: 5
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 25.0
    commercial_clarity: 25.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 15.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 40.9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/claimsforce/refs/heads/main/screenshots/claimsforce-2026-07-25T205452.png
security:
- kind: domain-security
  name: Claimsforce Domain Security
  slug: claimsforce-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: claimsforce
tags:
- Company
- Insurance
- Insurtech
- Claims Management
- Underwriting
- Risk Management
- Software-as-a-Service
- Germany
website: https://www.claimsforce.com
---
