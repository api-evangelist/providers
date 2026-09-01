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
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/infera-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/infera-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/infera-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.infera.bio
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.infera.bio/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.infera.bio/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.infera.bio/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.infera.bio/security
created: '2026-07-17'
description: Infera is an AI-native laboratory automation platform (Y Combinator, Spring 2026) that converts plain-English descriptions of experiments into validated, instrument-ready runs across the lab instruments a team already owns. It compiles protocols into vendor-specific scripts for liquid handlers, plate readers, mass spectrometers, thermocyclers and centrifuges (Opentrons, Hamilton, Tecan and others), limits AI to initial drafts while keeping downstream steps deterministic and fully checkable, supports both automated and manual bench procedures, and maintains an end-to-end audit trail of protocols and runs. Founded in San Francisco by Troy Zhang and Chloe Sow.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/infera.png
layout: provider
modified: '2026-07-19'
name: Infera
nav: Providers
network: true
overview: Infera is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Laboratory Automation, Biotech, Life Sciences, and Artificial Intelligence.
random_paper: 20
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 2
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
  previous_composite: 15.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/infera/refs/heads/main/screenshots/infera-2026-07-25T222354.png
security:
- kind: domain-security
  name: Infera Domain Security
  slug: infera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Infera Vulnerability Disclosure
  slug: infera-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Infera Trust Center
  slug: infera-trust-center
  summary_line: SOC 2 Type II, HIPAA
slug: infera
tags:
- Company
- Laboratory Automation
- Biotech
- Life Sciences
- Artificial Intelligence
- Protocols
- Software-as-a-Service
- Automation
website: https://www.infera.bio
---
