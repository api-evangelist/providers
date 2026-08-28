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
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: 'SAP NS2 is an independent US subsidiary of SAP SE that operates SAP cloud and software workloads for the US federal government, the Department of Defense, the Intelligence Community, and commercially '
  name: SAP NS2 (SAP National Security Services)
  slug: sap-ns2-sap-national-security-services
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sap-america-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sap-america-domain-security.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://github.com/api-evangelist/sap
- group: company
  title: ''
  type: Website
  url: https://www.sap.com/usa/index.html
- group: company
  title: ''
  type: GlobalWebsite
  url: https://www.sap.com
- group: other
  title: ''
  type: HumanURL
  url: https://www.sap.com/about/company/office-locations/north-america.html
- group: start
  title: ''
  type: APIPortal
  url: https://api.sap.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.sap.com
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/SAP
- group: company
  title: ''
  type: Newsroom
  url: https://news.sap.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.sap.com/investors.html
- group: company
  title: ''
  type: Careers
  url: https://jobs.sap.com/?locale=en_US
- group: company
  title: ''
  type: PartnerFinder
  url: https://partneredge.sap.com/en/partnership/sales/find-partner.html
- group: start
  title: ''
  type: SupportPortal
  url: https://support.sap.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.sap.com/about/trust-center.html
- group: commercial
  title: ''
  type: Privacy
  url: https://www.sap.com/about/legal/privacy.html
- group: commercial
  title: ''
  type: Legal
  url: https://www.sap.com/about/legal/impressum.html
- group: company
  title: ''
  type: Blog
  url: https://news.sap.com/feed/
- group: company
  title: ''
  type: About
  url: https://help.sap.com
created: '2026-05-23'
description: SAP America, Inc. is the US subsidiary of SAP SE, headquartered in Newtown Square, Pennsylvania, and serving as the Americas headquarters for the parent company's enterprise software portfolio (ERP, SCM, CRM, HCM, analytics, and cloud platform). SAP America itself does not publish a US-specific developer portal or APIs distinct from the parent SAP SE surface — all API documentation, SDKs, and OpenAPI artifacts are catalogued under the sibling `sap` repository (api.sap.com, SAP Business Accelerator Hub, SAP BTP). This repo is a subsidiary placeholder that exists to (1) record SAP America as a distinct US legal entity for partnership, public-sector, procurement, and FedRAMP / GovCloud contexts, and (2) cross-link to related US-only sibling subsidiaries — most importantly SAP NS2 (SAP National Security Services), the independent US subsidiary that operates SAP workloads in the Cloud Intelligence Enterprise (CIE), the DoD cloud environment, and the Commercially Regulated Environment
  (CRE) for federal, defense, and intelligence community customers. No tier-1 API artifacts (OpenAPI, AsyncAPI, JSON Schema, capabilities, plans, rate limits, FinOps) are generated in this repo per the api-evangelist no-empty-artifact rule — they are maintained under the parent `sap` repo and the per-product child repos (`sap-business-technology-platform`, `sap-successfactors`, `sap-ariba`, `sap-concur`, `sap-fieldglass`, `sap-api-management`, `sap-integration-suite`).
image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
layout: provider
modified: '2026-08-21'
name: SAP America
nav: Providers
network: true
overview: 'SAP America publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Subsidiary, ERP, Enterprise Software, Cloud, and Public Sector.


  SAP America''s developer surface includes privacy policy, legal docs, engineering blog, and 16 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 15.1
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 15.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 38.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sap-america/refs/heads/main/screenshots/sap-america-2026-06-20T193418.png
security:
- kind: domain-security
  name: Sap America Domain Security
  slug: sap-america-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Sap America Vulnerability Disclosure
  slug: sap-america-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sap-america
tags:
- Subsidiary
- ERP
- Enterprise Software
- Cloud
- Public Sector
- United States
website: https://www.sap.com/usa/index.html
---
