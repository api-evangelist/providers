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
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/ossus-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ossus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ossus.com
- group: company
  title: ''
  type: Blog
  url: https://www.ossus.com/blog
- group: auth
  title: ''
  type: Compliance
  url: https://trust.ossus.com/
created: '2026-07-17'
description: 'Ossus builds AI-native intelligence for cultural institutions, starting with libraries. Its flagship product is Ossus ILS, a modern integrated library system that unifies cataloguing, circulation, acquisitions, analytics, and patron discovery in one interface, with an AI copilot that drafts MARC records, subjects, and classifications for librarian approval. A lighter product, Librar, targets school libraries with fast mobile setup. AI add-ons cover camera-based shelf inventory, vendor comparison for purchasing, and grant finding. Ossus emphasizes privacy-first design: it does not train on or sell customer data and works only with catalogue metadata rather than borrower records. Ossus is a Y Combinator (Winter 2026) company based in San Francisco.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ossus.png
layout: provider
modified: '2026-07-20'
name: Ossus
nav: Providers
network: true
overview: 'Ossus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Libraries, Library Management, Integrated Library System, and Cataloguing.


  Ossus'' developer surface includes engineering blog and 4 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ossus/refs/heads/main/screenshots/ossus-2026-08-07T191015.png
security:
- kind: domain-security
  name: Ossus Domain Security
  slug: ossus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Ossus Trust Center
  slug: ossus-trust-center
  summary_line: SOC 2, ISO 27001
slug: ossus
tags:
- Company
- Libraries
- Library Management
- Integrated Library System
- Cataloguing
- MARC
- Cultural Institutions
- Artificial Intelligence
- Education
website: https://www.ossus.com
---
