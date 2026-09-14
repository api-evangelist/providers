---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Csg Agentic Access
  operation_count: 12
  slug: csg-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 1
apis:
- description: Forte.js is a JavaScript library for secure browser-based payment tokenization. It enables web applications to collect and tokenize payment card data client-side before submitting to Forte's payment A
  name: CSG Forte.js
  slug: csg-forte-js
- description: The Forte React Native SDK enables mobile application developers to integrate payment processing capabilities into iOS and Android apps built with React Native.
  name: CSG Forte React Native SDK
  slug: csg-forte-react-native-sdk
- description: CSG Singleview is a comprehensive convergent billing and revenue management platform designed for communication service providers. APIs enable subscriber billing, usage rating, invoice generation, and
  name: CSG Singleview Billing API
  slug: csg-singleview-api
- baseURL: https://api.forte.net/v3
  baseurl_source: declared
  description: Customer record management
  name: CSG Systems Customers API
  slug: csg-customers-api
- baseURL: https://api.forte.net/v3
  baseurl_source: declared
  description: Payment method tokenization and management
  name: CSG Systems Payment Methods API
  slug: csg-payment-methods-api
- baseURL: https://api.forte.net/v3
  baseurl_source: declared
  description: Settlement query and reconciliation
  name: CSG Systems Settlements API
  slug: csg-settlements-api
- baseURL: https://api.forte.net/v3
  baseurl_source: declared
  description: Payment transaction processing (credit card, echeck, scheduled)
  name: CSG Systems Transactions API
  slug: csg-transactions-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CSG Forte REST Customers API
  slug: open-csg-customers-api
- collection_type: open
  name: CSG Forte REST API
  slug: open-csg-forte-rest
- collection_type: open
  name: CSG Forte REST Customers Payment Methods API
  slug: open-csg-payment-methods-api
- collection_type: open
  name: CSG Forte REST Customers Settlements API
  slug: open-csg-settlements-api
- collection_type: open
  name: CSG Forte REST Customers Transactions API
  slug: open-csg-transactions-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/csg-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/csg-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/csg-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/csg-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/csg-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/csg-i
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/csg-
- group: company
  title: ''
  type: Website
  url: https://www.csgi.com/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/csg-forte-rest-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/csg-forte-transaction-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/csg-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/csg-forte-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/csg-forte-vocabulary.yml
- group: start
  title: ''
  type: Portal
  url: https://www.forte.net/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.forte.net/
- group: docs
  title: ''
  type: Reference
  url: https://restdocs.forte.net/
- group: operate
  title: ''
  type: Support
  url: https://support.forte.net/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.forte.net/
- group: operate
  title: ''
  type: ChangeLog
  url: https://releases.forte.net/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.forte.net/test-account-setup/
- group: company
  title: ''
  type: Blog
  url: https://developers.forte.net/feed/
created: '2026-03-18'
description: CSG is a global provider of customer engagement, revenue management, and payments solutions enabling communications, media, and entertainment companies to monetize and digitally enable customer experiences. CSG's developer surface includes the CSG Forte payments REST API, Forte.js client-side tokenization library, the Forte React Native SDK, and the Singleview convergent billing platform.
finops:
- name: Csg Finops
  service_category: Billing & Revenue Management
  slug: csg-finops
json_schemas:
- name: CSG Forte Payment Transaction
  property_count: 17
  slug: csg-forte-transaction
jsonld:
- class_count: 11
  name: Csg Context
  property_count: 19
  slug: csg-context
layout: provider
modified: '2026-05-19'
name: CSG Systems
nav: Providers
network: true
overview: 'CSG Systems publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Customers API, Payment Methods API, Settlements API, and 1 more. Tagged areas include Billing, Customer Engagement, Payments, Revenue Management, and Telecom.


  The CSG Systems catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  CSG Systems'' developer surface includes authentication, developer portal, documentation, support, changelog, getting-started guide, engineering blog, and 14 more developer resources.'
plans:
- name: Csg Plans Pricing
  plan_count: 1
  slug: csg-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Csg Rate Limits
  slug: csg-rate-limits
rules:
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: CSG Systems API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: csg-forte-rules
- effective_rule_count: 6
  extends: []
  name: CSG Systems API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: csg-jsonschema-spectral-rules
screenshot: https://raw.githubusercontent.com/api-evangelist/csg/refs/heads/main/screenshots/csg-2026-06-20T175316.png
security:
- kind: authentication
  name: Csg Authentication
  slug: csg-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Csg Domain Security
  slug: csg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Csg Vulnerability Disclosure
  slug: csg-vulnerability-disclosure
  summary_line: disclosure policy published
slug: csg
tags:
- Billing
- Customer Engagement
- Payments
- Revenue Management
- Telecom
website: https://www.csgi.com/
---
