---
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-27'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/breathe-life-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/breathe-life-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/breathe-life-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/breathe-life-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/breathe-life-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.breathelife.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/breathe-life/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/breathelifeinsurance/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getbreathelife
- group: operate
  title: ''
  type: PressRelease
  url: https://web.archive.org/web/20220519024512/https://www.breathelife.com/se2-acquires-breathe-life-to-scale-saas-product-and-data-capabilities-for-carriers-across-the-insurance-lifecycle/
- group: other
  title: ''
  type: Archive
  url: https://web.archive.org/web/20221005001219/https://www.breathelife.com/
- group: other
  title: ''
  type: Archive
  url: https://web.archive.org/web/20221004232457/https://www.breathelife.com/life-insurance-security/
- group: other
  title: ''
  type: Archive
  url: https://web.archive.org/web/20220809144206/https://www.breathelife.com/privacy-policy/
- group: other
  title: ''
  type: ParentCompany
  url: https://zinnia.com/
created: '2026-07-25'
description: 'Breathe Life is a Montreal, Quebec based life insurance technology company — an enterprise SaaS core-systems vendor rather than a carrier or a broker — founded in 2018 to sell life insurers a modern new-business origination and distribution platform. Its product was the Breathe Life Hybrid Origination (Hybrid Distribution) Platform, sold either end-to-end or as four separately licensable modules: Quoter, Hybrid e-App, Advisor Tools and Data Dashboards, supporting advisor-driven, consumer self-serve, or blended selling of individual life products with simple and complex underwriting paths. Its home market is Canada, and its named clients were Canadian and North American life carriers, fraternals and faith-based insurers including Teachers Life, FaithLife Financial, National Bank Insurance, National Catholic Society of Foresters and La Capitale. The company raised CAD $11.5M in August 2020 from Diagram Ventures, Real Ventures and Investissement Quebec plus angels from AXA, AIG
  and RGA, was named to the 2020 InsurTech 100, and held PCI DSS, SOC 2 Type II and SOC 3 attestations. SE2, an Eldridge business, announced its acquisition of Breathe Life on 2022-03-28; SE2 subsequently rebranded as Zinnia, and the Breathe Life site carried a "We are now part of Zinnia!" banner before being decommissioned. Its API posture is closed and now historical: as of the 2026-07-25 review Breathe Life never published a developer portal, API reference, OpenAPI or Swagger definition, Postman collection, GraphQL endpoint, webhook catalog or ACORD/AL3 conformance claim on breathelife.com, and the domain no longer serves a site at all — breathelife.com returns an nginx "Site Not Configured" 404 and www.breathelife.com returns a WP Engine "Site is not available" 404. Quote, bind, issue and FNOL existed only as capabilities inside a carrier-licensed, login-gated SaaS product, never as an addressable public API.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Breathe Life
nav: Providers
network: true
overview: Breathe Life is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Canada, Life Insurance, Insurtech, and Core Systems.
random_paper: 36
score:
  band: minimal
  composite: 9.9
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 9.9
  regulatory:
    applies: true
    regime: Insurance
    regime_id: insurance
    score: 23.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/breathe-life/refs/heads/main/screenshots/breathe-life-2026-07-25T203742.png
security:
- kind: domain-security
  name: Breathe Life Domain Security
  slug: breathe-life-domain-security
  summary_line: DMARC
slug: breathe-life
tags:
- Insurance
- Canada
- Life Insurance
- Insurtech
- Core Systems
- Policy Origination
- Quoting
- Underwriting
- Agent Tools
- SaaS
- Acquired
website: https://www.breathelife.com/
---
