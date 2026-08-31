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
- group: company
  title: ''
  type: Website
  url: https://listrunnerapp.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/listrunner-domain-security.yml
created: '2026-07-17'
description: 'Listrunner was a HIPAA-compliant clinical collaboration platform that let hospital care teams build and share living patient lists. Marketed as "a collaboration platform for clinicians," it targeted specialty practices, residency programs, hospital departments, and outpatient teams with shared sign-out/handoff lists, faster rounding, coordinated discharge tracking, task assignment, real-time lab and clinical data access, EHR integration, printable rounding lists, fully customizable per-team list fields, administrator-controlled user permissions and data access, audit logs and reporting, and a robust offline mode across web plus native iOS and Android apps. Listrunner no longer operates as an independent product: its brand domains listrunner.health and listrunnerapp.com are now served from Cloudflare and redirect (301 then 307) to commure.com, the healthcare-infrastructure company that merged with Athelas. The last archived standalone Listrunner homepage is from 2021-06-04.
  Listrunner never published a public API, developer portal, SDK, or package; it is retained in the API Evangelist network as a historical health-tech identity record and a pointer to its successor surface at Commure/Athelas, not as an API provider.'
image: https://web.archive.org/web/2021id_/https://www.listrunnerapp.com/favicon/android-icon-192x192.png
layout: provider
modified: '2026-07-19'
name: Listrunner
nav: Providers
network: true
overview: Listrunner is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Clinical Collaboration, and Care Coordination.
random_paper: 18
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/listrunner/refs/heads/main/screenshots/listrunner-2026-07-25T225331.png
security:
- kind: domain-security
  name: Listrunner Domain Security
  slug: listrunner-domain-security
  summary_line: TLSv1.3 · HSTS
slug: listrunner
tags:
- Company
- Health
- Healthcare
- Clinical Collaboration
- Care Coordination
- Patient Lists
- Clinical Handoff
- HIPAA
- Mobile
- Defunct
website: https://listrunnerapp.com/
---
