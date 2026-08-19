---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Dosespot Agentic Access
  operation_count: 17
  slug: dosespot-agentic-access
  summary_line: 17 operations · 6 acting
api_count: 8
apis:
- description: The DoseSpot REST API v2 contract for JumpStart customers - 139 operations, the subset available alongside DoseSpot's pre-built iFrame/SSO prescribing experience. Harvested verbatim from DoseSpot's ow
  name: DoseSpot REST API - JumpStart + EPCS - V2
  slug: dosespot-rest-api-jumpstart-epcs-v2
- description: The complete DoseSpot REST API v2 contract for Full Integration customers - 171 operations across 28 resource groups covering patients, allergies, medications, interactions, pharmacies, prescriptions,
  name: DoseSpot REST API - Full + EPCS - V2
  slug: dosespot-rest-api-full-epcs-v2
- description: Medi-Span drug search and interaction checks.
  name: DoseSpot Medications API
  slug: dosespot-medications-api
- description: Clinician notification counts and actionable items.
  name: DoseSpot Notifications API
  slug: dosespot-notifications-api
- description: Patient demographics, allergies, and self-reported medications.
  name: DoseSpot Patients API
  slug: dosespot-patients-api
- description: Surescripts pharmacy search and patient pharmacy management.
  name: DoseSpot Pharmacies API
  slug: dosespot-pharmacies-api
- description: Clinician (prescriber) and clinic staff management.
  name: DoseSpot Prescribers API
  slug: dosespot-prescribers-api
- description: Prescription creation, transmission, status, and medication history.
  name: DoseSpot Prescriptions API
  slug: dosespot-prescriptions-api
artifact_total: 26
asyncapis:
- description: ''
  name: Dosespot Webhooks
  slug: dosespot-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: DoseSpot Medications API
  slug: open-dosespot-medications-api
- collection_type: open
  name: DoseSpot Medications Notifications API
  slug: open-dosespot-notifications-api
- collection_type: open
  name: DoseSpot Medications Patients API
  slug: open-dosespot-patients-api
- collection_type: open
  name: DoseSpot Medications Pharmacies API
  slug: open-dosespot-pharmacies-api
- collection_type: open
  name: DoseSpot Medications Prescribers API
  slug: open-dosespot-prescribers-api
- collection_type: open
  name: DoseSpot Medications Prescriptions API
  slug: open-dosespot-prescriptions-api
- collection_type: open
  name: DoseSpot API
  slug: open-dosespot
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dosespot-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dosespot-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dosespot-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dosespot
- group: company
  title: ''
  type: Website
  url: https://www.dosespot.com
- group: docs
  title: ''
  type: Documentation
  url: https://dosespot.com/full-integration/
- group: commercial
  title: ''
  type: Plans
  url: plans/dosespot-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dosespot-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dosespot-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://dosespot.com/feed/
- group: design
  title: ''
  type: Conventions
  url: conventions/dosespot-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dosespot-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dosespot-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dosespot.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/dosespot-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://dosespot.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/dosespot-trust-center.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dosespot-data-model.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/dosespot-vocabulary.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/dosespot-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/dosespot-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dosespot-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/dosespot-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/dosespot-full-epcs-v2-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.dosespot.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dosespot.com/staging/docs/dosespot-rest-api-full-epcs-v2-v-full_epcsv2
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dosespot.com/staging/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://dosespot.com/request-support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://dosespot.com/contact-support/
- group: start
  title: ''
  type: SignUp
  url: https://dosespot.com/request-a-demo/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dosespot.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dosespot.com/dosespot-legal-documentation/
- group: operate
  title: ''
  type: SLA
  url: https://dosespot.com/exhibit-d-dosespot-service-level-agreement/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DoseSpot
created: '2026-06-21'
description: 'DoseSpot is a Surescripts- and EPCS-certified electronic prescribing (eRx) platform that EHR, EMR, telehealth and digital-health vendors embed to add the full prescription lifecycle to their own software. The REST API v2 covers patients and demographics, allergies and allergen search, Medi-Span medication and supply search, drug-drug and drug-allergy interaction screening, the Surescripts pharmacy directory, prescription creation, signing and transmission including DEA-regulated EPCS for controlled substances, refill and RxChange queues, medication history, eligibility and real-time prescription benefit, electronic prior authorization, PDMP/Narx reports, and clinician, clinic and DEA-number administration. DoseSpot publishes two Swagger 2.0 contracts from its own SwaggerHub organization - Full + EPCS (171 operations) and JumpStart + EPCS (139 operations) - rendered at docs.dosespot.com, which DoseSpot calls the official source for its technical documentation. Access is sales-gated:
  credentials are issued by an assigned Integration Specialist. DoseSpot is part of Interra Health, alongside its subsidiary pVerify.'
finops:
- name: Dosespot Finops
  service_category: Healthcare
  slug: dosespot-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dosespot.png
layout: provider
mcp_servers:
- description: ''
  name: dosespot-mcp.yml
  slug: dosespot-mcpyml
modified: '2026-08-15'
name: DoseSpot
nav: Providers
network: true
overview: 'DoseSpot publishes 8 APIs on the [APIs.io](https://apis.io/) network, including REST API - JumpStart + EPCS - V2, REST API - Full + EPCS - V2, Medications API, and 5 more. Tagged areas include e-Prescribing, eRx, Healthcare, EHR, and Pharmacy.


  The DoseSpot catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  DoseSpot''s developer surface includes authentication, documentation, engineering blog, sandbox, API reference, getting-started guide, support, and 28 more developer resources.'
plans:
- name: Dosespot Plans Pricing
  plan_count: 2
  slug: dosespot-plans-pricing
random_paper: 136
rate_limits:
- limit_count: 1
  name: Dosespot Rate Limits
  slug: dosespot-rate-limits
score:
  band: strong
  composite: 65.9
  delta: 5.0
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 45.5
    contract_quality: 64.7
    developer_ergonomics: 66.1
    discoverability: 74.1
    governance: 45.5
    operational_transparency: 31.6
  previous_composite: 60.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 43.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/dosespot/refs/heads/main/screenshots/dosespot-2026-07-25T212312.png
security:
- kind: authentication
  name: Dosespot Authentication
  slug: dosespot-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Dosespot Domain Security
  slug: dosespot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dosespot Vulnerability Disclosure
  slug: dosespot-vulnerability-disclosure
  summary_line: Hackerone · security.txt
- kind: trust-center
  name: Dosespot Trust Center
  slug: dosespot-trust-center
  summary_line: SOC 2 Type 2, HIPAA, PCI DSS, NIST
slug: dosespot
tags:
- e-Prescribing
- eRx
- Healthcare
- EHR
- Pharmacy
- EPCS
- Prescriptions
- Clinical
- Medications
- Prior Authorization
- Surescripts
- Medi-Span
- Telehealth
- PDMP
- Digital Health
website: https://www.dosespot.com
---
