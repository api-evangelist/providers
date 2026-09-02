---
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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/datavant/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aetion-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aetion.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aetion
- group: operate
  title: ''
  type: Support
  url: https://support.aetion.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.datavant.com/privacy-policy
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/aetion_stock/
coverage:
  checked: '2026-08-06'
  detail: Aetion was absorbed into Datavant when the acquisition closed on 11 July 2025, and every path on aetion.com — including /.well-known/* — now answers HTTP 301 into www.datavant.com, so there is no Aetion-origin developer surface left to read; the only Aetion host still serving anything of its own is the customer support portal at support.aetion.com, a Salesforce Experience Cloud community.
  evidence:
  - status: 301
    url: https://aetion.com/
  - status: 301
    url: https://aetion.com/technology/platform/
  - status: 301
    url: https://aetion.com/.well-known/agent-card.json
  - status: 503
    url: https://support.aetion.com/
  - status: 200
    url: https://github.com/aetion
  reason: defunct
  state: none
created: '2026-08-06'
description: 'Aetion is a healthcare technology company that builds real-world evidence (RWE) software for biopharma, medical device manufacturers, payers and regulators. Its Aetion Evidence Platform (AEP) turns claims, electronic health record, registry, patient-reported and trial data into transparent, reproducible, regulatory-grade evidence, delivered as a set of applications: Discover for exploratory analysis, Substantiate for study implementation, Activate as a low-code plus hosted-code workbench, and Generate for synthetic data. Founded by two Harvard Medical School professors, Aetion was acquired by Datavant; the acquisition closed 11 July 2025 and Aetion now operates inside Datavant''s Life Sciences business. As of this profile the aetion.com domain redirects wholesale to datavant.com and Aetion publishes no standalone developer program, public API reference or machine-readable specification.'
image: https://avatars.githubusercontent.com/u/54075156?v=4
layout: provider
modified: '2026-08-06'
name: Aetion
nav: Providers
network: true
overview: 'Aetion is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real-World Evidence, Healthcare, Life Sciences, and Clinical Research.


  Aetion''s developer surface includes support and 6 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 7.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aetion/refs/heads/main/screenshots/aetion-2026-08-07T161016.png
security:
- kind: domain-security
  name: Aetion Domain Security
  slug: aetion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aetion
tags:
- Company
- Real-World Evidence
- Healthcare
- Life Sciences
- Clinical Research
- Health Data
- Data Analytics
website: https://aetion.com/
---
