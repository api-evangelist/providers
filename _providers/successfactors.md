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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: The SAP SuccessFactors HXM Suite OData API set (OData v2 and v4) provides programmatic access to Employee Central, Recruiting, Onboarding, Performance & Goals, Compensation, Learning, and other HXM en
  name: SAP SuccessFactors HXM Suite OData API
  slug: sap-successfactors-hxm-suite-odata-api
artifact_total: 3
common:
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
overview: 'Successfactors publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Human Resources, HCM, HXM, and Human Capital Management.


  Successfactors'' developer surface includes documentation, API reference, support, and 9 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 19.2
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 28.3
    discoverability: 79.6
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 19.2
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
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
- Human Capital Management
- Talent Management
- Recruiting
- Learning
- Payroll
- SAP
- Enterprise
- OData
website: https://www.successfactors.com
---
