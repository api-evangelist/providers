---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    auth_clarity: bearer
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
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 38
  human_in_the_loop: 1
  name: Ambra Health Agentic Access
  operation_count: 62
  slug: ambra-health-agentic-access
  summary_line: 62 operations · 38 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Account (tenant) administration
  name: Ambra Health Accounts API
  slug: ambra-health-accounts-api
- description: User groups
  name: Ambra Health Groups API
  slug: ambra-health-groups-api
- description: Namespace permissions, settings, and audit
  name: Ambra Health Namespaces API
  slug: ambra-health-namespaces-api
- description: Patient records and merges
  name: Ambra Health Patients API
  slug: ambra-health-patients-api
- description: Authentication, session, OAuth, and permissions
  name: Ambra Health Session API
  slug: ambra-health-session-api
- description: Study and filter sharing / image exchange
  name: Ambra Health Sharing API
  slug: ambra-health-sharing-api
- description: DICOM data, storage, and annotations
  name: Ambra Health Storage & Images API
  slug: ambra-health-storage-images-api
- description: DICOM study lifecycle, routing, download, and audit
  name: Ambra Health Studies API
  slug: ambra-health-studies-api
- description: User administration and tokens
  name: Ambra Health Users API
  slug: ambra-health-users-api
- description: Event webhooks
  name: Ambra Health Webhooks API
  slug: ambra-health-webhooks-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ambra Health (InteleShare) v3 Services Public Accounts API
  slug: open-ambra-health-accounts-api
- collection_type: open
  name: Ambra Health (InteleShare) v3 Services Public Accounts Groups API
  slug: open-ambra-health-groups-api
- collection_type: open
  name: Ambra Health (InteleShare) v3 Services Public Accounts Namespaces API
  slug: open-ambra-health-namespaces-api
- collection_type: open
  name: Ambra Health (InteleShare) v3 Services Public Accounts Patients API
  slug: open-ambra-health-patients-api
- collection_type: open
  name: Ambra Health (InteleShare) v3 Services Public Accounts Session API
  slug: open-ambra-health-session-api
- collection_type: open
  name: Ambra Health (InteleShare) v3 Services Public Accounts Sharing API
  slug: open-ambra-health-sharing-api
- collection_type: open
  name: Ambra Health (InteleShare) v3 Services Public Accounts Storage & Images API
  slug: open-ambra-health-storage-images-api
- collection_type: open
  name: Ambra Health (InteleShare) v3 Services Public Accounts Studies API
  slug: open-ambra-health-studies-api
- collection_type: open
  name: Ambra Health (InteleShare) v3 Services Public Accounts Users API
  slug: open-ambra-health-users-api
- collection_type: open
  name: Ambra Health (InteleShare) v3 Services Public Accounts Webhooks API
  slug: open-ambra-health-webhooks-api
- collection_type: open
  name: Ambra Health (InteleShare) v3 Services Public API
  slug: open-ambra-health
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/ambra-health-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ambra-health-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ambra-health-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ambra-health-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dicomgrid
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/intelerad
- group: company
  title: ''
  type: Website
  url: https://ambrahealth.com
- group: docs
  title: ''
  type: Documentation
  url: https://access.dicomgrid.com/api/v3/api.html
- group: commercial
  title: ''
  type: Plans
  url: plans/ambra-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ambra-health-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ambra-health-finops.yml
created: '2026-07-05'
description: Ambra Health (now part of Intelerad Medical Systems, and rebranded as InteleShare) is a cloud-based medical image management, exchange, and interoperability platform - a cloud VNA and PACS that lets healthcare providers, patients, and researchers store, view, route, and share diagnostic imaging in real time without a VPN or CD. Its imaging data is DICOM, and its v3 Services Public API (historically the DICOM Grid API) exposes programmatic control over studies, patients, users, groups, accounts, namespaces, sharing, storage/images, and webhooks. The REST API is JSON over HTTPS and is authenticated with a session id (sid) obtained from /session/login. Intelerad acquired Ambra Health in 2021 to form a $1.7B cloud PACS and enterprise-imaging leader.
finops:
- name: Ambra Health Finops
  service_category: Healthcare Medical Imaging Platform
  slug: ambra-health-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ambra-health.png
layout: provider
modified: '2026-07-05'
name: Ambra Health
nav: Providers
network: true
overview: 'Ambra Health publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Groups API, Namespaces API, and 7 more. Tagged areas include Medical Imaging, DICOM, Healthcare, PACS, and Image Exchange.


  Ambra Health''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Ambra Health Plans Pricing
  plan_count: 3
  slug: ambra-health-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 4
  name: Ambra Health Rate Limits
  slug: ambra-health-rate-limits
score:
  band: thin
  composite: 37.7
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 49.4
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ambra-health/refs/heads/main/screenshots/ambra-health-2026-07-25T200031.png
security:
- kind: authentication
  name: Ambra Health Authentication
  slug: ambra-health-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ambra Health Domain Security
  slug: ambra-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ambra-health
tags:
- Medical Imaging
- DICOM
- Healthcare
- PACS
- Image Exchange
- Interoperability
- VNA
- Cloud Imaging
website: https://ambrahealth.com
---
