---
access_model:
  confidence: high
  label: Commercial
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://www.sepasoft.com/pricing-mes/
  - https://www.sepasoft.com/pricing-sepaiq/
  trial: false
  try_now: false
api_count: 1
apis:
- description: The REST and SOAP surface the Sepasoft Web Services module exposes. Endpoints are authored by the operator in the Ignition Designer and served from the customer's own Ignition Gateway, mounted beneath
  name: Sepasoft Web Services
  slug: sepasoft
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.sepasoft.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sepasoft.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sepasoft.com/articles/user-manual/web-services
- group: start
  title: ''
  type: GettingStarted
  url: https://www.sepasoft.com/learn/
- group: operate
  title: ''
  type: Support
  url: https://www.sepasoft.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.sepasoft.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sepasoft.com/pricing-mes/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sepasoft.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sepasoft.com/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sepasoft-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.sepasoft.com/articles/release-notes-publication/service-pack-release-notes
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sepasoft-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sepasoft-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sepasoft-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sepasoft-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sepasoft-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/sepasoft-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/sepasoft-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sepasoft-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sepasoft-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sepasoft-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/sepasoft-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sepasoft-llms.txt
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sepasoft-vocabulary.yml
created: '2025-03-01'
description: Sepasoft builds Manufacturing Execution System (MES) software delivered as modules for the Inductive Automation Ignition platform, used to control, track and document the transformation of raw materials into finished goods in real time. The suite spans OEE and downtime tracking, track and trace, ISA-88 batch procedure control, statistical process control, settings and changeover, document management, and ERP integration through the Business Connector (B2MML / ISA-95) and an SAP interface, alongside SepaIQ for analytics, machine learning and LLM features. Its integration surface is the Web Services module, which turns a customer's own Ignition Gateway into a REST and SOAP provider and consumer rather than a hosted API Sepasoft operates.
finops:
- name: Sepasoft Finops
  service_category: API
  slug: sepasoft-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sepasoft.png
jsonld:
- class_count: 19
  name: Sepasoft Context
  property_count: 19
  slug: sepasoft-context
layout: provider
modified: '2026-08-27'
name: Sepasoft
nav: Providers
network: true
overview: 'Sepasoft publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Manufacturing, Manufacturing Execution System, Industrial Automation, OEE, and Track and Trace.


  The Sepasoft catalog on APIs.io includes 1 JSON-LD context.


  Sepasoft''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 17 more developer resources.'
plans:
- name: Sepasoft Plans Pricing
  plan_count: 16
  slug: sepasoft-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Sepasoft Rate Limits
  slug: sepasoft-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/sepasoft/refs/heads/main/screenshots/sepasoft-2026-09-02T154933.png
security:
- kind: authentication
  name: Sepasoft Authentication
  slug: sepasoft-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Sepasoft Domain Security
  slug: sepasoft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Sepasoft Trust Center
  slug: sepasoft-trust-center
  summary_line: SOC 2, ISO 27001
slug: sepasoft
tags:
- Manufacturing
- Manufacturing Execution System
- Industrial Automation
- OEE
- Track and Trace
- Batch Processing
- Statistical Process Control
- ERP Integration
- ISA-95
- Ignition
website: https://www.sepasoft.com/
---
