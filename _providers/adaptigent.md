---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The Adaptive Integration Fabric (formerly Ivory Suite) enables enterprises to rapidly expose IBM z/OS and z/VSE mainframe applications as REST or SOAP web services without programming. Using the Fabri
  name: Adaptive Integration Fabric API
  slug: adaptive-integration-fabric
artifact_total: 17
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adaptigent-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adaptigent
- group: company
  title: ''
  type: Website
  url: https://www.adaptigent.com
- group: start
  title: ''
  type: Portal
  url: https://www.adaptigent.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.adaptigent.com/resources/pricing/
- group: company
  title: ''
  type: Partners
  url: https://www.adaptigent.com/about/partners/
- group: company
  title: ''
  type: Blog
  url: https://www.adaptigent.com/blog/
- group: operate
  title: ''
  type: Contact
  url: https://www.adaptigent.com/contact/
created: '2025-03-01'
description: Adaptigent (formerly GT Software) is a technology company founded in 1982 that specializes in mainframe integration and API enablement solutions. Their flagship product, Adaptive Integration Fabric (formerly Ivory Suite), empowers enterprises to expose legacy mainframe systems as modern REST and SOAP APIs without writing any code. Using a patented no-code, drag-and-drop environment, the platform enables integration of IBM z/OS and z/VSE mainframe applications with modern distributed systems, supporting both inbound and outbound integration flows in real time. Adaptigent serves industries including finance, government, manufacturing, and healthcare, offering a usage-based subscription pricing model.
features:
- description: Patented drag-and-drop visual environment enables non-programmers to create sophisticated REST and SOAP APIs from mainframe applications without writing any code.
  name: No-Code API Development
- description: Supports bidirectional integration flows — modern applications can call mainframe services via API, and COBOL/PL/I mainframe programs can make outbound calls to external REST or SOAP services.
  name: Inbound And Outbound Integration
- description: Provides real-time access to legacy data sources and transaction systems, enabling modern applications to consume mainframe data instantly without batch processing.
  name: Real-Time Mainframe Data Access
- description: Natively supports IBM z/OS and z/VSE mainframe platforms, enabling REST API enablement for COBOL and PL/I programs on these systems.
  name: IBM z/OS And z/VSE Support
- description: Automatically generates industry-standard REST and SOAP web service endpoints from mainframe subroutines and programs, with no additional MIPS usage.
  name: REST And SOAP API Generation
- description: Flexible pricing model based on actual resource consumption, allowing organizations to scale integration usage without fixed licensing fees.
  name: Usage-Based Subscription Pricing
- description: Available on Red Hat Marketplace, enabling enterprise customers to deploy and manage Adaptive Integration Fabric within their Red Hat OpenShift environments.
  name: Red Hat Marketplace Availability
finops:
- name: Adaptigent Finops
  service_category: API
  slug: adaptigent-finops
image: /assets/icons/adaptigent.png
layout: provider
modified: '2026-04-19'
name: Adaptigent
nav: Providers
network: true
overview: 'Adaptigent publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Mainframe, Integration, API Gateway, Legacy Systems, and Enterprise.


  Adaptigent''s developer surface includes developer portal, pricing, engineering blog, and 5 more developer resources.'
plans:
- name: Adaptigent Plans Pricing
  plan_count: 3
  slug: adaptigent-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 5
  name: Adaptigent Rate Limits
  slug: adaptigent-rate-limits
score:
  band: emerging
  composite: 22.2
  delta: -2.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 24.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adaptigent/refs/heads/main/screenshots/adaptigent-2026-06-20T164608.png
security:
- kind: domain-security
  name: Adaptigent Domain Security
  slug: adaptigent-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: adaptigent
tags:
- Mainframe
- Integration
- API Gateway
- Legacy Systems
- Enterprise
- No Code
- Middleware
use_cases:
- description: Enterprises with legacy IBM mainframe systems can expose core business logic and data as modern REST APIs, enabling mobile apps, web applications, and microservices to consume mainframe capabilities.
  name: Mainframe API Modernization
- description: Banks and financial institutions can connect core banking systems on the mainframe to fraud detection services, digital banking platforms, and fintech APIs in real time.
  name: Financial Core System Integration
- description: Government agencies can modernize access to mission-critical legacy systems by exposing them as standard APIs without replacing or re-coding existing mainframe applications.
  name: Government Legacy System Modernization
- description: Manufacturers can link inventory, transportation, and parts systems running on legacy platforms with modern ERP and supply chain management systems through API integration.
  name: Manufacturing Supply Chain Integration
- description: Organizations adopting hybrid cloud strategies can bridge on-premises mainframe data with cloud-based applications and services using Adaptive Integration Fabric as the middleware layer.
  name: Hybrid Cloud Mainframe Connectivity
website: https://www.adaptigent.com
---
