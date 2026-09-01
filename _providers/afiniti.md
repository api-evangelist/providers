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
- group: company
  title: ''
  type: Website
  url: https://www.afiniti.com/
- group: company
  title: ''
  type: About
  url: https://www.afiniti.com/about-us/
- group: other
  title: ''
  type: Products
  url: https://www.afiniti.com/products/
- group: company
  title: ''
  type: Partners
  url: https://www.afiniti.com/afiniti-link/
- group: company
  title: ''
  type: Blog
  url: https://www.afiniti.com/blogs/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.afiniti.com/feed/
- group: company
  title: ''
  type: News
  url: https://www.afiniti.com/news/
- group: operate
  title: ''
  type: Support
  url: https://www.afiniti.com/contact/
- group: start
  title: ''
  type: SignUp
  url: https://www.afiniti.com/book-a-demo/
- group: start
  title: ''
  type: Login
  url: https://portal.afiniti.com/AfinitiPortal/Login.aspx
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.afiniti.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/afiniti-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.afiniti.com/trust-center/
- group: commercial
  title: ''
  type: Legal
  url: https://www.afiniti.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.afiniti.com/legal/privacy-policy/
- group: build
  title: ''
  type: CodeOfConduct
  url: https://www.afiniti.com/legal/code-of-conduct/
- group: other
  title: ''
  type: Patents
  url: https://www.afiniti.com/legal/patents/
- group: company
  title: ''
  type: Careers
  url: https://www.afiniti.com/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/afiniti-com
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@afinitiai
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/afinitiai
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/afiniti_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/afiniti-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/afiniti-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/afiniti-domain-security.yml
coverage:
  checked: '2026-08-06'
  detail: Afiniti's only developer-facing page, Afiniti Link, advertises "APIs, SDKs, documentation and service delivery bootcamps" but ships them exclusively through a "Join Afiniti Link" partner-certification form — there is no reference, no spec, and no api./docs./developer.afiniti.com host in DNS at all.
  evidence:
  - status: 200
    url: https://www.afiniti.com/afiniti-link/
  - status: 410
    url: https://www.afiniti.com/openapi.json
  - status: 404
    url: https://www.afiniti.com/.well-known/agent-card.json
  - status: 200
    url: https://portal.afiniti.com/AfinitiPortal/Login.aspx
  reason: sales-gate
  state: gated
created: '2026-08-06'
description: 'Afiniti is an enterprise contact center AI company whose patented behavioral pairing technology matches inbound customers with the agent most likely to produce a desired business outcome, measured against a continuously alternating ON/OFF control benchmark. In 2026 the company extended pairing into what it calls Outcome Orchestration, a unified AI decisioning platform spanning four products: Afiniti Pairing, Afiniti Orchestrator, Afiniti Intelligence and Afiniti Agents. Afiniti sits as a decisioning layer above existing CCaaS, ACD, IVR/IVA, CRM and workforce platforms rather than replacing them, and is deployed at telco, financial services, insurance, healthcare and travel/hospitality enterprises. Integration reaches customers through host platform ecosystems (Genesys AppFoundry, NICE CXexchange/DEVone, Five9) and through the Afiniti Link partner program, which advertises APIs and SDKs to certified partners but publishes no public developer portal, API reference, or machine-readable
  specification.'
image: https://www.afiniti.com/wp-content/uploads/2023/08/Logo-blue.svg
layout: provider
modified: '2026-08-06'
name: Afiniti
nav: Providers
network: true
overview: 'Afiniti is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Contact Center, Customer Experience, and Machine-Learning.


  Afiniti''s developer surface includes engineering blog, product news, support, signup flow, legal docs, YouTube channel, and 19 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 15.1
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 15.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/afiniti/refs/heads/main/screenshots/afiniti-2026-08-07T161026.png
security:
- kind: domain-security
  name: Afiniti Domain Security
  slug: afiniti-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Afiniti Trust Center
  slug: afiniti-trust-center
  summary_line: SOC 2 Type 2, HITRUST, SOC 3, ISO/IEC 27001, ISO/IEC 27701, GDPR, CCPA, EcoVadis
slug: afiniti
tags:
- Company
- Artificial Intelligence
- Contact Center
- Customer Experience
- Machine-Learning
- Enterprise AI
- Call Routing
- CCaaS
website: https://www.afiniti.com/
---
