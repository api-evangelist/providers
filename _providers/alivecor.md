---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: HIPAA-compliant REST API providing cloud access to patient ECG data via KardiaPro — account management, patient provisioning, and webhook notifications for new ECG availability. Access is gated behind
  name: AliveCor API
  slug: alivecor-api
artifact_total: 6
asyncapis:
- description: ''
  name: Alivecor Kardiapro Webhooks
  slug: alivecor-kardiapro-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.alivecor.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://alivecor.com/data-integration
- group: operate
  title: ''
  type: Support
  url: https://alivecor.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://alivecor.com/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alivecor
- group: start
  title: ''
  type: SignUp
  url: https://kardia.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alivecor.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alivecor.com/tos
- group: auth
  title: ''
  type: Compliance
  url: https://alivecor.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/alivecor-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://alivecor.com/vulnerability-disclosure
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/alivecor-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/alivecor-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alivecor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/alivecor-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/alivecor-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/alivecor-kardiapro-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/alivecor-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/alivecor-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alivecor-llms.txt
created: '2026-07-17'
description: 'AliveCor is a digital health company building FDA-cleared, AI-powered personal ECG hardware (KardiaMobile 6L, KardiaMobile Card, and the 12-lead Kardia 12L) and cardiac-care software (KardiaPro, KardiaStation, KardiaComplete) for consumers, clinicians, health systems, biopharma, and payers/employers. Its algorithms detect atrial fibrillation, tachycardia, bradycardia, and normal sinus rhythm from a single recording. For developers and partners AliveCor offers a data-integration layer: Android/iOS SDKs that embed its FDA-cleared ECG recording and rhythm-classification algorithms, a HIPAA-compliant REST API (KardiaPro cloud) with API-key authentication and webhook notifications for new ECG availability, and EHR integration such as GE Healthcare MUSE NX. API/SDK access is gated behind a commercial agreement. Backed by Khosla Ventures.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alivecor.png
layout: provider
modified: '2026-07-17'
name: Alivecor
nav: Providers
network: true
overview: 'Alivecor publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Digital Health, ECG, Cardiology, and Medical Devices.


  The Alivecor catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Alivecor''s developer surface includes support, engineering blog, signup flow, authentication, and 16 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 23.8
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 28.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Health
    regime_id: health
    score: 28.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alivecor/refs/heads/main/screenshots/alivecor-2026-07-25T195625.png
security:
- kind: authentication
  name: Alivecor Authentication
  slug: alivecor-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Alivecor Domain Security
  slug: alivecor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Alivecor Vulnerability Disclosure
  slug: alivecor-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Alivecor Trust Center
  slug: alivecor-trust-center
  summary_line: SOC 2 Type 2, ISO 27001, ISO 42001, HITRUST e1, HIPAA, GDPR
slug: alivecor
tags:
- Company
- Digital Health
- ECG
- Cardiology
- Medical Devices
- Remote Patient Monitoring
- Artificial Intelligence
- Health Data
website: https://www.alivecor.com/
---
