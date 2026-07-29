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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Guardant Health Agentic Access
  operation_count: 3
  slug: guardant-health-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 7
apis:
- description: Guardant Nexus partnership program for institutional and provider partners, coordinating ordering, integration and account workflows. Access is partner-gated; no public API surface is documented.
  name: Guardant Nexus
  slug: guardant-nexus
- description: In-silico real-world clinical-genomic data platform combining de-identified longitudinal clinical information with genomic data from Guardant360, used by biopharma for drug development analytics. Deli
  name: GuardantINFORM
  slug: guardant-inform
- description: 'Integrated software solution that connects patients tested with Guardant assays who have actionable alterations to potentially relevant clinical studies, for clinical and biopharmaceutical customers. '
  name: GuardantConnect
  slug: guardant-connect
- description: Suite of advanced AI analytics and digital pathology technologies that enhance Guardant test performance and power biomarker and drug discovery. Embedded in Guardant's products; no public developer AP
  name: Guardant Galaxy
  slug: guardant-galaxy
- description: Authenticated patient-facing portals (MyGuardant and My Data) where patients access test status, results and personal health data. Web application behind login; no documented public patient API.
  name: MyGuardant Patient Portal
  slug: myguardant-patient-portal
- description: Electronic ordering of Guardant assays from the EMR.
  name: Guardant Health Orders API
  slug: guardant-health-orders-api
- description: Molecular profiling results delivered back to the patient chart.
  name: Guardant Health Results API
  slug: guardant-health-results-api
artifact_total: 16
collections:
- collection_type: open
  name: Guardant Health EMR Integration (Illustrative Model)
  slug: open-guardant-health
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/guardant-health-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/guardant-health-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/guardant-health-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/guardant-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/guardant-health-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/guardanthealth
- group: company
  title: ''
  type: Website
  url: https://www.guardanthealth.com
- group: docs
  title: ''
  type: Documentation
  url: https://guardanthealth.com/precision-oncology/for-institutional-partners/emr-integration-services/
- group: commercial
  title: ''
  type: Plans
  url: plans/guardant-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/guardant-health-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/guardant-health-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.guardanthealth.com/newsroom/press-releases/
created: '2026-06-20'
description: Guardant Health is a precision oncology company whose blood- and tissue-based liquid biopsy tests (Guardant360, Guardant Reveal, Guardant Shield, GuardantINFINITY) detect cancer and guide treatment. Its integration surface is partner- and EMR-based - electronic test ordering and results delivery through Epic Aura and Flatiron OncoEMR, patient portals (MyGuardant, My Data), and biopharma data platforms (GuardantINFORM, GuardantConnect, Guardant Galaxy). No public self-serve developer API is documented.
finops:
- name: Guardant Health Finops
  service_category: Healthcare and Life Sciences
  slug: guardant-health-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/guardant-health.png
layout: provider
modified: '2026-06-20'
name: Guardant Health
nav: Providers
network: true
overview: 'Guardant Health publishes 2 APIs on the [APIs.io](https://apis.io/) network: Orders API and Results API. Tagged areas include Healthcare, Precision Oncology, Liquid Biopsy, Genomics, and EMR Integration.


  Guardant Health''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Guardant Health Plans Pricing
  plan_count: 3
  slug: guardant-health-plans-pricing
random_paper: 71
rate_limits:
- limit_count: 2
  name: Guardant Health Rate Limits
  slug: guardant-health-rate-limits
scopes:
- name: Guardant Health Scopes
  scope_count: 0
  slug: guardant-health-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.0
  delta: -4.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 56.8
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 42.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 42.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/guardant-health/refs/heads/main/screenshots/guardant-health-2026-06-20T182424.png
security:
- kind: authentication
  name: Guardant Health Authentication
  slug: guardant-health-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Guardant Health Domain Security
  slug: guardant-health-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Guardant Health Trust Center
  slug: guardant-health-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: guardant-health
tags:
- Healthcare
- Precision Oncology
- Liquid Biopsy
- Genomics
- EMR Integration
website: https://www.guardanthealth.com
---
