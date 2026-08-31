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
api_count: 2
apis:
- description: Public Open Bank Project sandbox instance hosted by Infosys Finacle that exposes standard OBP REST APIs for accounts, transactions, customers, and consents. Useful for developers exploring Finacle ban
  name: Infosys Finacle Open Bank Project Sandbox
  slug: finacle-obp-sandbox
- description: Banking API Platform from Infosys delivering open banking APIs across deposits, loans, payments, trade finance, and data privacy, bundled with API management, developer portal, API composer, and conse
  name: Infosys Banking API Platform
  slug: banking-api-platform
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/infosys-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/infosys
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/infosys
- group: company
  title: ''
  type: Website
  url: https://www.infosys.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.finacle.com/solution/api-connect/
- group: other
  title: ''
  type: Finacle Product
  url: https://www.finacle.com
- group: start
  title: ''
  type: Open Bank Project Sandbox
  url: https://infosys-finacle.openbankproject.com
created: '2026-05-11'
description: Infosys is a global IT services, consulting, and outsourcing company headquartered in Bengaluru, India, providing digital transformation, cloud, AI, and business process services. Through its Finacle banking software product and Banking API Platform, Infosys exposes open banking APIs for deposits, loans, payments, trade finance, and data privacy, along with a configurable developer portal, API composer, and consent management. A public Finacle Open Bank Project sandbox is also available for developers to explore banking APIs.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/infosys.png
layout: provider
modified: '2026-05-11'
name: Infosys
nav: Providers
network: true
overview: 'Infosys publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include IT Services, Consulting, Banking, Open Banking, and Finacle.


  Infosys'' developer surface includes documentation and 6 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 5.6
  coverage:
    artifact_dirs: 2
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 5.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/infosys/refs/heads/main/screenshots/infosys-2026-06-20T183341.png
security:
- kind: domain-security
  name: Infosys Domain Security
  slug: infosys-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: infosys
tags:
- IT Services
- Consulting
- Banking
- Open Banking
- Finacle
- Digital Transformation
- Cloud
website: https://www.infosys.com
---
