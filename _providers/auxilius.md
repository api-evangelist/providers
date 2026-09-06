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
  url: security/auxilius-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.auxilius.co/
- group: company
  title: ''
  type: Blog
  url: https://www.auxilius.co/resources
- group: operate
  title: ''
  type: Support
  url: https://www.auxilius.co/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.auxilius.co/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.auxilius.co/
- group: design
  title: ''
  type: Conformance
  url: conformance/auxilius-conformance.yml
created: '2026-07-17'
description: Auxilius is R&D finance automation software for biopharmaceutical companies, purpose-built to manage clinical trial finances. The platform automates clinical expense accruals and financial close with built-in audit controls, tracks investigator grant spend by mapping patient-visit data to site contracts, and models and re-forecasts study spend as trial conditions change. It integrates with clinical (Medrio, Veeva), financial (Oracle NetSuite, Workday, SAP, QuickBooks), procurement (Coupa, Bill.com), and planning (Planful, Anaplan) systems, delivering variance analysis, automated reconciliation, and audit-ready role-based approval workflows. Auxilius is SOC 1 Type 2 and SOC 2 Type 2 compliant and is used by 100+ biopharma companies. It is backed by Bain Capital Ventures. No public developer API is currently published.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/auxilius.png
layout: provider
modified: '2026-07-18'
name: Auxilius
nav: Providers
network: true
overview: 'Auxilius is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Biopharma, Clinical Trials, and Finance.


  Auxilius'' developer surface includes engineering blog, support, and 5 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 13.2
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 13.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/auxilius/refs/heads/main/screenshots/auxilius-2026-07-25T201857.png
security:
- kind: domain-security
  name: Auxilius Domain Security
  slug: auxilius-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: auxilius
tags:
- Company
- Healthcare
- Biopharma
- Clinical Trials
- Finance
- Accounting
- FinOps
- Software-as-a-Service
website: https://www.auxilius.co/
---
