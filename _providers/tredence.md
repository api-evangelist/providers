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
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tredence-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tredence-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tredence-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tredence-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/tredence-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.tredence.com/certifications
- group: company
  title: ''
  type: Website
  url: https://www.tredence.com/
- group: company
  title: ''
  type: Blog
  url: https://www.tredence.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.tredence.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tredence.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tredence.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tredenceofficial
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/tredence_stock/
coverage:
  checked: '2026-08-05'
  detail: Tredence sells data-science and AI work as consulting engagements plus tenant-deployed accelerators (Sancus, MLWorks, RAPID, Customer Cosmos), so there is nothing to integrate with from outside — developer.tredence.com, api.tredence.com and docs.tredence.com do not resolve at all, and none of the 862 URLs in the company sitemap is a developer, API or reference page.
  evidence:
  - status: 0
    url: https://api.tredence.com/
  - status: 0
    url: https://developer.tredence.com/
  - status: 404
    url: https://www.tredence.com/openapi.json
  - status: 200
    url: https://www.tredence.com/sitemap.xml
  - status: 200
    url: https://www.tredence.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-05'
description: 'Tredence is a global data science and AI solutions company headquartered in San Jose, California, founded in 2013 by Shub Bhowmick, Sumit Mehra and Shashank Dubey. The firm positions itself around the "last-mile problem in AI" — the gap between insight creation and value realization — and delivers agentic AI, generative AI, data engineering, data science, MLOps, LLMOps, data modernization, supply-chain and customer-experience analytics as consulting engagements backed by named accelerators and platforms including RAPID (agentic process automation), Sancus (AI-led data quality and master data management), MLWorks (industrial MLOps), Customer Cosmos, Supply Chain Control Tower, Revenue Growth Management, On-Shelf Availability, Test and Learn Platform and UnityGO. It serves retail, CPG, healthcare, life sciences, banking/financial services/insurance, telco/media/tech, travel and hospitality, and industrials, with delivery centers across North America, Europe and Asia. Tredence
  publishes an authored llms.txt for AI agents and an ISO 27001:2022 / ISO 27701:2019 / SOC 2 Type 2 certifications page, but does not operate a public developer program: no developer portal, API reference, machine-readable specification or first-party SDK is published on any Tredence host.'
image: https://www.tredence.com/assets/Tredence_logo.png
layout: provider
modified: '2026-08-05'
name: Tredence
nav: Providers
network: true
overview: 'Tredence is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Science, Artificial Intelligence, Analytics, and Machine-Learning.


  Tredence''s developer surface includes engineering blog, support, and 11 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 17.0
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 17.0
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Tredence Domain Security
  slug: tredence-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tredence Trust Center
  slug: tredence-trust-center
  summary_line: ISO 27001:2022, ISO 27701:2019, SOC 2 Type 2, ISO 27001:2013
slug: tredence
tags:
- Company
- Data Science
- Artificial Intelligence
- Analytics
- Machine-Learning
- Consulting
- Data Engineering
- MLOps
- Agentic AI
- Supply Chain
website: https://www.tredence.com/
---
