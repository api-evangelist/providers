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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/personalis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.personalis.com
created: '2026-07-17'
description: Personalis, Inc. (NASDAQ PSNL) is a clinical genomics and cancer diagnostics company based in Fremont, California. It develops advanced tumor and immune profiling tests built on next-generation sequencing, including its NeXT Personal ultra-sensitive tumor-informed molecular residual disease (MRD) and recurrence-monitoring assay and the ImmunoID NeXT whole-exome and transcriptome platform used for translational cancer research, biopharma partnerships, and population sequencing programs. Personalis operates as a diagnostics laboratory and research-services provider; its offerings are delivered as clinical tests, sequencing services, and analytical reports rather than as a public developer API. No public developer portal, API reference, or SDK is published as of this enrichment pass.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/personalis.png
layout: provider
modified: '2026-07-20'
name: Personalis
nav: Providers
network: true
overview: Personalis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Genomics, Oncology, Diagnostics, and Sequencing.
random_paper: 17
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 2
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
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/personalis/refs/heads/main/screenshots/personalis-2026-09-02T151107.png
security:
- kind: domain-security
  name: Personalis Domain Security
  slug: personalis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: personalis
tags:
- Company
- Genomics
- Oncology
- Diagnostics
- Sequencing
- Precision Medicine
- Healthcare
- Life Sciences
website: https://www.personalis.com
---
