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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/runharbor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://runharbor.com/
- group: company
  title: ''
  type: Blog
  url: https://runharbor.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://runharbor.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://runharbor.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/runharbor
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/company/runharbor
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/runharbor-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/runharbor-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/runharbor-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://runharbor.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/runharbor-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://runharbor.com/security
- group: design
  title: ''
  type: Conformance
  url: conformance/runharbor-conformance.yml
created: '2026-07-17'
description: Harbor (Runharbor) is an AI-native contract research organization (CRO) and eClinical data management platform for clinical trials. Its software automates the core clinical-trial data lifecycle — study build, electronic data capture (eCRF/ePRO), source-document extraction, query generation, risk-based remote monitoring, electronic signature, and database lock — using AI to cut manual data entry and accelerate regulatory submissions. The platform is designed for 21 CFR Part 11, HIPAA, and ICH E6 (GCP) compliance, with per-trial database isolation and zero standing access to client data. Harbor is offered both as software (Magic Build, Magic Capture, Magic Monitor) and as full-service trial execution for sponsors and CROs. Founded in 2025 in San Francisco and backed by Y Combinator (Spring 2026), Google Cloud, and the NVIDIA Inception Program.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/runharbor.png
layout: provider
modified: '2026-07-21'
name: Runharbor
nav: Providers
network: true
overview: 'Runharbor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Clinical Trials, Healthcare, Contract Research Organization, and Electronic Data Capture.


  Runharbor''s developer surface includes engineering blog, pricing, and 12 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 18.8
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
    score: 32.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/runharbor/refs/heads/main/screenshots/runharbor-2026-09-02T154207.png
security:
- kind: domain-security
  name: Runharbor Domain Security
  slug: runharbor-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Runharbor Vulnerability Disclosure
  slug: runharbor-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Runharbor Trust Center
  slug: runharbor-trust-center
  summary_line: 21 CFR Part 11, HIPAA, ICH E6 (GCP), ISPE GAMP 5, ISO 13485
slug: runharbor
tags:
- Company
- Clinical Trials
- Healthcare
- Contract Research Organization
- Electronic Data Capture
- Life Sciences
- Compliance
- Artificial Intelligence
- eClinical
website: https://runharbor.com/
---
