---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 9
  human_in_the_loop: 1
  name: Digicert Agentic Access
  operation_count: 19
  slug: digicert-agentic-access
  summary_line: 19 operations · 9 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: 'The DigiCert Report Library API allows users to create and manage custom reports for CertCentral certificate orders, domains, organizations, and account activity. Programmatically schedule, retrieve, '
  name: DigiCert Report Library API
  slug: digicert-report-library-api
- description: The DigiCert Discovery API enables scanning of internal and public-facing networks using sensors to find SSL/TLS certificates regardless of the issuing Certificate Authority. Use the API to manage sca
  name: DigiCert Discovery API
  slug: digicert-discovery-api
- description: The DigiCert Automation API allows configuration of automation profiles and management of automation activities for certificate lifecycle operations. Access all automation features available in CertCe
  name: DigiCert Automation API
  slug: digicert-automation-api
- description: The DigiCert Custom Reports API allows generation of customizable and comprehensive data sets by leveraging the powerful GraphQL query language. Build tailored reporting against CertCentral data sourc
  name: DigiCert Custom Reports API
  slug: digicert-custom-reports-api
- description: The Account API from Digicert — 4 operation(s) for account.
  name: Digicert Account API
  slug: digicert-account-api
- description: The Domain API from Digicert — 2 operation(s) for domain.
  name: Digicert Domain API
  slug: digicert-domain-api
- description: The Order API from Digicert — 6 operation(s) for order.
  name: Digicert Order API
  slug: digicert-order-api
- description: The Organization API from Digicert — 1 operation(s) for organization.
  name: Digicert Organization API
  slug: digicert-organization-api
- description: The User API from Digicert — 1 operation(s) for user.
  name: Digicert User API
  slug: digicert-user-api
artifact_total: 17
collections:
- collection_type: open
  name: DigiCert CertCentral Services API
  slug: open-digicert
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/digicert-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/digicert-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/digicert-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/digicert-inc-
- group: other
  title: ''
  type: Developer
  url: https://dev.digicert.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.digicert.com/
- group: operate
  title: ''
  type: Support
  url: https://knowledge.digicert.com/
- group: company
  title: ''
  type: Website
  url: https://www.digicert.com/
- group: company
  title: ''
  type: Blog
  url: https://www.digicert.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.digicert.com/tls-ssl/compare-certificates
- group: auth
  title: ''
  type: Security
  url: https://www.digicert.com/trust/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.digicert.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.digicert.com/legal-repository/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.digicert.com/legal-repository/master-services-agreement
- group: build
  title: ''
  type: GitHub
  url: https://github.com/digicert
- group: operate
  title: ''
  type: ChangeLog
  url: https://dev.digicert.com/en/changelog.html
- group: agent
  title: ''
  type: LlmsText
  url: https://dev.digicert.com/llms.txt
created: '2025-01-08'
description: Digicert is a leading provider of digital security solutions, specializing in SSL/TLS certificates, PKI solutions, and website security. They help organizations of all sizes protect their websites, data, and communications from cyber threats by providing secure encryption and authentication services. Digicert's CertCentral platform exposes a suite of REST and GraphQL APIs for certificate lifecycle management, discovery, automation, and reporting.
finops:
- name: Digicert Finops
  service_category: API
  slug: digicert-finops
graphqls:
- description: The DigiCert Custom Reports API allows generation of customizable and comprehensive data sets by leveraging the powerful GraphQL query language. Build tailored reporting against CertCentral data sourc
  name: Digicert GraphQL API
  slug: digicert-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/digicert.png
layout: provider
modified: '2026-05-19'
name: Digicert
nav: Providers
network: true
overview: 'Digicert publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Account API, Domain API, Order API, and 2 more. Tagged areas include Certificates, Encryption, PKI, SSL, and TLS.


  Digicert''s developer surface includes authentication, documentation, support, engineering blog, pricing, GitHub presence, changelog, and 10 more developer resources.'
plans:
- name: Digicert Plans Pricing
  plan_count: 3
  slug: digicert-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 5
  name: Digicert Rate Limits
  slug: digicert-rate-limits
score:
  band: developing
  composite: 50.4
  delta: 2.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 47.8
    developer_ergonomics: 26.1
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 78.9
  previous_composite: 48.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/digicert/refs/heads/main/screenshots/digicert-2026-06-20T180019.png
security:
- kind: authentication
  name: Digicert Authentication
  slug: digicert-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Digicert Domain Security
  slug: digicert-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: digicert
tags:
- Certificates
- Encryption
- PKI
- SSL
- TLS
website: https://www.digicert.com/
---
