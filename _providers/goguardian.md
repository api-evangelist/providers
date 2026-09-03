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
api_count: 3
apis:
- description: Consumer-side roster synchronization. GoGuardian ingests organizations (OUs), students, teachers, guardians, classes, and enrollments from a district's Student Information System via the OneRoster 1.1
  name: GoGuardian Rostering Integration (OneRoster / Clever / ClassLink)
  slug: goguardian-rostering-integration
- description: 'GoGuardian maintains a developer / integration documentation portal at based.goguardian.com ("GoGuardian Based Docs"). Access to GoGuardian''s outbound developer surface is partner-gated - there is no '
  name: GoGuardian Based Developer / Partner API
  slug: goguardian-based-developer-api
- description: 'GoGuardian Beacon analyzes student browsing (and, via a Google Docs API integration, document) activity to detect signals of suicide, self-harm, and other safety risk, then routes time-stamped alerts '
  name: GoGuardian Beacon Alerts (Student Safety)
  slug: goguardian-beacon-alerts
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goguardian-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/goguardian
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/goguardian
- group: company
  title: ''
  type: Website
  url: https://www.goguardian.com/
- group: docs
  title: ''
  type: Documentation
  url: https://based.goguardian.com/
- group: operate
  title: ''
  type: Support
  url: https://support.goguardian.com/s/
- group: company
  title: ''
  type: Website
  url: https://www.goguardian.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.goguardian.com/blog
created: '2026-07-04'
description: GoGuardian is a K-12 education technology company whose suite - Admin (DNS and device content filtering for CIPA compliance), Teacher (classroom management and student engagement), and Beacon (student safety and self-harm / suicide risk detection) - is administered through web dashboards rather than a broadly published public API. GoGuardian's integration model is primarily roster ingestion - it syncs organizations, students, teachers, guardians, and classes from district Student Information Systems via the IMS Global / 1EdTech OneRoster 1.1 REST API (using a Consumer ID / Secret and a OneRoster URL), Clever, ClassLink, and Google Classroom, and it consumes Google Workspace admin APIs on the district's behalf. A developer / partner documentation portal exists at based.goguardian.com ("GoGuardian Based Docs"), but GoGuardian's own outbound developer API surface is partner-gated and not openly published. The API entries below are honestly modeled logical surfaces, not a confirmed
  public REST catalog.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/goguardian.png
layout: provider
modified: '2026-07-04'
name: GoGuardian
nav: Providers
network: true
overview: 'GoGuardian publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, EdTech, K-12, Content Filtering, and Classroom Management.


  GoGuardian''s developer surface includes documentation, support, engineering blog, and 5 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 4.8
  coverage:
    artifact_dirs: 3
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 4.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/goguardian/refs/heads/main/screenshots/goguardian-2026-07-25T220010.png
security:
- kind: domain-security
  name: Goguardian Domain Security
  slug: goguardian-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: goguardian
tags:
- Education
- EdTech
- K-12
- Content Filtering
- Classroom Management
- Student Safety
- Rostering
- OneRoster
- Partner API
website: https://www.goguardian.com/
---
