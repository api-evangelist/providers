---
access_model:
  confidence: high
  label: Enterprise · contact sales
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
api_count: 1
apis:
- baseURL: https://api-sandbox.c008-m008-us.fraud.net
  baseurl_source: declared
  description: Public API for evaluating cart, order, transaction, loan-application, account-application and login risk in real time, and for submitting post-event Update signals (status, disposition, chargeback, fr
  name: Fraud.net Public API
  slug: public-api
artifact_total: 10
asyncapis:
- description: ''
  name: Fraud Net Webhooks
  slug: fraud-net-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.fraud.net/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.fraud.net/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.fraud.net/docs/public-apis/b2edb775739e6-api-documentation
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.fraud.net/docs/public-apis/b95a796f3265e-api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.fraud.net/onboarding
- group: operate
  title: ''
  type: Support
  url: https://www.fraud.net/company/contact
- group: company
  title: ''
  type: Blog
  url: https://www.fraud.net/resource-center
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fraudnet
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fraud-net
- group: start
  title: ''
  type: SignUp
  url: https://www.fraud.net/demo-request
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fraud.net/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fraud.net/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.fraud.net/trust-center
- group: auth
  title: ''
  type: Compliance
  url: https://www.fraud.net/trust-center
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fraud.net/
- group: operate
  title: ''
  type: ChangeLog
  url: https://releasenotes.fraud.net/
- group: auth
  title: ''
  type: Authentication
  url: authentication/fraud-net-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fraud-net-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/fraud-net-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fraud-net-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fraud-net-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fraud-net-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fraud-net-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/fraud-net-public-apis-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/fraud-net-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fraud-net-packages.yml
- group: design
  title: ''
  type: Components
  url: components/fraud-net-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fraud-net-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fraud-net-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/fraud-net-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fraud-net-domain-security.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fraud-net-changelog.yml
created: '2024-11-13'
description: 'Fraud.net (FraudNet) is an enterprise fraud, risk and compliance platform used by payment processors, acquirers, PSPs, fintechs, banks and digital commerce platforms. Its Public API is a risk-decisioning surface: Check operations submit a transaction, order, loan application, account application or login for real-time scoring, and Update operations relay the eventual outcome (approved, declined, chargeback, fraud disposition) back so the models keep learning. Every Check returns a 0-100 risk score, a risk group and rule tags, drawn from supervised models, anomaly detection and a global anti-fraud network, alongside device fingerprinting, identity, entity screening and AML/KYC-adjacent compliance workflows.'
finops:
- name: Fraud Net Finops
  service_category: API
  slug: fraud-net-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fraud-net.png
layout: provider
modified: '2026-09-10'
name: Fraud.net
nav: Providers
network: true
overview: 'Fraud.net publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Fraud, Risk, Commerce, Payments, and Security.


  The Fraud.net catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Fraud.net''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 26 more developer resources.'
plans:
- name: Fraud Net Plans Pricing
  plan_count: 0
  slug: fraud-net-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Fraud Net Rate Limits
  slug: fraud-net-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: Fraud.net API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: fraud-net-rules
screenshot: https://raw.githubusercontent.com/api-evangelist/fraud-net/refs/heads/main/screenshots/fraud-net-2026-06-20T181510.png
security:
- kind: authentication
  name: Fraud Net Authentication
  slug: fraud-net-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fraud Net Domain Security
  slug: fraud-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fraud Net Vulnerability Disclosure
  slug: fraud-net-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Fraud Net Trust Center
  slug: fraud-net-trust-center
  summary_line: SOC 2 Type II, ISO 27001, PCI DSS, HIPAA, GDPR, NIST 800-53, NTIS
slug: fraud-net
tags:
- Fraud
- Risk
- Commerce
- Payments
- Security
- Compliance
- Identity
- Banking
- Machine Learning
website: https://www.fraud.net/
---
