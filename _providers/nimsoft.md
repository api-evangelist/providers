---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''http://www.nimsoft.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.broadcom.com/products/software/aiops-observability/infrastructure-management — a different registrable domain (nimsoft.com -> broadcom.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
artifact_total: 1
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/broadcom/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nimsoft-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.nimsoft.com
created: '2026-07-17'
description: Nimsoft was a SaaS-based IT infrastructure and application monitoring and service-desk company, founded in 1998 as Nimbus Software in Oslo, Norway and later headquartered in Redwood City, California. Backed by Northzone and JMI Equity, it was acquired by CA Technologies in March 2010 for roughly $350 million, after which its products were folded into CA Unified Infrastructure Management (UIM). CA was in turn acquired by Broadcom in 2018, and the former Nimsoft monitoring capability now lives on as Broadcom DX Unified Infrastructure Management. The www.nimsoft.com domain today resolves to Broadcom infrastructure, and Nimsoft has no independent developer portal, public API, or OpenAPI surface of its own.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nimsoft.png
layout: provider
modified: '2026-07-20'
name: Nimsoft
nav: Providers
network: true
overview: Nimsoft is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Monitoring, IT Operations, and Observability.
random_paper: 12
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
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
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nimsoft/refs/heads/main/screenshots/nimsoft-2026-08-07T185319.png
security:
- kind: domain-security
  name: Nimsoft Domain Security
  slug: nimsoft-domain-security
  summary_line: DMARC
slug: nimsoft
tags:
- Company
- Enterprise
- Monitoring
- IT Operations
- Observability
- Infrastructure Management
- Software-as-a-Service
website: http://www.nimsoft.com
---
