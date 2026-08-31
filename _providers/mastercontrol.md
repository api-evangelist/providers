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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The MasterControl Manufacturing Excellence (Mx) RESTful API creates, modifies, retrieves and deletes manufacturing and production-record data in Mx. It is delivered through the separately licensed Mas
  name: MasterControl Mx RESTful API
  slug: mx-restful-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mastercontrol-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mastercontrol.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.mastercontrol.com/solutions/toolkit/
- group: operate
  title: ''
  type: Support
  url: https://support.mastercontrol.com/support?id=customer_login
- group: start
  title: ''
  type: Login
  url: https://support.mastercontrol.com/support?id=customer_login
- group: company
  title: ''
  type: Blog
  url: https://www.mastercontrol.com/insights/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mastercontrol.com/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mastercontrol.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mastercontrol.com/legal/terms/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.mastercontrol.com/ai-trust-center/
- group: auth
  title: ''
  type: Compliance
  url: https://www.mastercontrol.com/ai-trust-center/
- group: design
  title: ''
  type: Conformance
  url: conformance/mastercontrol-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mastercontrol-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mastercontrol-llms.txt
coverage:
  checked: '2026-08-04'
  detail: MasterControl's Qx and Mx REST reference is a Swagger UI served only from inside a paying customer's own tenant (https://mx.<region>.svc.mastercontrol.com/<company>/swagger-ui/index.html) and requires a separately purchased API license, so the host root and every anonymous spec path on the live Mx service host return 404.
  evidence:
  - status: 404
    url: https://mx.us-west-2.svc.mastercontrol.com/swagger-ui/index.html
  - status: 404
    url: https://mx.us-west-2.svc.mastercontrol.com/v3/api-docs
  - status: 404
    url: https://www.mastercontrol.com/openapi.json
  - status: 200
    url: https://currentcloud.onlinehelp.mastercontrol.com/2024.1/en_us/Content/Appendix/Access_and_Use_MasterControl_APIs.htm
  reason: customer-only-docs
  state: gated
created: '2026-08-04'
description: MasterControl is a Salt Lake City based software company that builds cloud quality management (QMS) and manufacturing execution (MES) software for regulated industries, primarily life sciences — pharmaceutical, biotechnology, medical device, CRO/CDMO, and food and beverage manufacturers. Its platform spans document control, training, CAPA, change control, audit, supplier quality, electronic batch records, and production records, and is built to support FDA 21 CFR Part 11, EU MDR, GDPR and HIPAA obligations. MasterControl exposes RESTful APIs for its Qx (Quality Excellence) and Mx (Manufacturing Excellence) products through a separately licensed API Toolkit, used to integrate the quality system with ERP, CRM, MES, PDM and document repositories; the API reference is published as a Swagger UI inside each customer tenant rather than on a public developer portal.
image: https://static.mastercontrol.com/assets/persist/images/home/MasterControl_Thumbnail.jpg
layout: provider
modified: '2026-08-04'
name: MasterControl
nav: Providers
network: true
overview: 'MasterControl publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Quality Management, Manufacturing, Life Sciences, and Compliance.


  MasterControl''s developer surface includes documentation, support, engineering blog, pricing, and 10 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 26.2
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 26.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mastercontrol/refs/heads/main/screenshots/mastercontrol-2026-08-07T172117.png
security:
- kind: domain-security
  name: Mastercontrol Domain Security
  slug: mastercontrol-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Mastercontrol Trust Center
  slug: mastercontrol-trust-center
  summary_line: ISO 9001, ISO 27001, ISO 27017, ISO 27701, ISO 42001
slug: mastercontrol
tags:
- Company
- Quality Management
- Manufacturing
- Life Sciences
- Compliance
- Document-Management
- Regulatory
- Enterprise Software
website: https://www.mastercontrol.com/
---
