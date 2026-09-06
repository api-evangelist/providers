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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/actifio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.actifio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.actifio.com/
- group: operate
  title: ''
  type: Support
  url: https://www.actifio.com/support.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.actifio.com/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.actifio.com/assets/Clickthrough-EULA-9-23-19.pdf
created: '2026-07-17'
description: Actifio is an enterprise data management company that pioneered "copy data management" (CDM) built on its Virtual Data Pipeline (VDP) technology, letting organizations capture a single physical copy of production data and instantly provision virtual copies for backup, disaster recovery, business continuity, test/dev, and analytics. Founded in 2009 and headquartered in Waltham, Massachusetts, Actifio was acquired by Google Cloud in December 2020. Its technology now underpins the Google Cloud Backup and Disaster Recovery (Backup and DR) service and Actifio GO, delivering SaaS backup and DR for Google Cloud and hybrid workloads. Actifio VDP exposes automation via a RESTful API and CLI on the appliance, but there is no public developer portal, OpenAPI/Swagger specification, or published client SDK.
image: https://www.actifio.com/favicon.ico
layout: provider
modified: '2026-07-17'
name: Actifio
nav: Providers
network: true
overview: 'Actifio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Management, Backup, Disaster Recovery, and Copy Data Management.


  Actifio''s developer surface includes documentation, support, and 4 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 12.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/actifio/refs/heads/main/screenshots/actifio-2026-07-25T181522.png
security:
- kind: domain-security
  name: Actifio Domain Security
  slug: actifio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: actifio
tags:
- Company
- Data Management
- Backup
- Disaster Recovery
- Copy Data Management
- Business Continuity
- Cloud
- Enterprise Storage
website: https://www.actifio.com/
---
