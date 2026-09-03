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
api_count: 1
apis:
- description: The SAP SuccessFactors HXM Suite OData API set (OData v2 and v4) provides programmatic access to Employee Central, Recruiting, Onboarding, Performance & Goals, Compensation, Learning, and other HXM en
  name: SAP SuccessFactors HXM Suite OData API
  slug: sap-successfactors-hxm-suite-odata-api
artifact_total: 3
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/sap/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/successfactors-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.successfactors.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/successfactors-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/successfactors-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/successfactors-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://www.successfactors.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.sap.com/products/SAPSuccessFactors/overview
- group: docs
  title: ''
  type: Documentation
  url: https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM
- group: docs
  title: ''
  type: APIReference
  url: https://api.sap.com/products/SAPSuccessFactors/apis/REST
- group: operate
  title: ''
  type: Support
  url: https://support.sap.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sap.com/about/legal/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sap.com/about/legal/privacy.html
created: '2026-07-17'
description: SuccessFactors is a cloud-based human capital management (HCM) company founded in 2001 and an early Canaan Partners portfolio company that IPO'd in 2007 and was acquired by SAP in 2012. It is now delivered as the SAP SuccessFactors HXM (Human Experience Management) Suite, covering core HR (Employee Central), Recruiting, Onboarding, Performance & Goals, Compensation, Learning (LMS), Succession & Development, and Workforce Analytics. SuccessFactors exposes an extensive integration surface through OData v2 and OData v4 APIs (the SFAPI/OData platform) documented on the SAP Business Accelerator Hub, using OAuth 2.0 SAML bearer-assertion and basic authentication per customer datacenter instance.
image: https://www.successfactors.com/favicon.ico
layout: provider
modified: '2026-07-21'
name: Successfactors
nav: Providers
network: true
overview: 'Successfactors publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Human Resources, HCM, HXM, and Talent Management.


  Successfactors'' developer surface includes documentation, API reference, support, and 10 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 3
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 12.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/successfactors/refs/heads/main/screenshots/successfactors-2026-09-02T161124.png
security:
- kind: domain-security
  name: Successfactors Domain Security
  slug: successfactors-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Successfactors Vulnerability Disclosure
  slug: successfactors-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: successfactors
tags:
- Company
- Human Resources
- HCM
- HXM
- Talent Management
- Recruiting
- Learning
- Payroll
- SAP
- Enterprise
- OData
website: https://www.successfactors.com
---
