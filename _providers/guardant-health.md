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
    agentic_commerce: false
    auth_clarity: negotiable
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Guardant Health Agentic Access
  operation_count: 3
  slug: guardant-health-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
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
- baseURL: https://example.invalid/guardant-health/emr
  baseurl_source: spec
  description: Electronic ordering of Guardant assays from the EMR.
  name: Guardant Health Orders API
  slug: guardant-health-orders-api
- baseURL: https://example.invalid/guardant-health/emr
  baseurl_source: spec
  description: Molecular profiling results delivered back to the patient chart.
  name: Guardant Health Results API
  slug: guardant-health-results-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Guardant Health EMR Integration API (Illustrative Model) Orders API
  slug: open-guardant-health-orders-api
- collection_type: open
  name: Guardant Health EMR Integration API (Illustrative Model) Orders Results API
  slug: open-guardant-health-results-api
- collection_type: open
  name: Guardant Health EMR Integration (Illustrative Model)
  slug: open-guardant-health
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/guardant-health-capability-edges.yml
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


  Guardant Health''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Guardant Health Plans Pricing
  plan_count: 3
  slug: guardant-health-plans-pricing
random_paper: 17
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
  composite: 38.4
  coverage:
    artifact_dirs: 12
    catalog_earned: 55.0
    catalog_earned_first_party: 0.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.8
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 46.9
    developer_ergonomics: 25.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 42.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
