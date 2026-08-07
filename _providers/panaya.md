---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Panaya's REST API surface, including the Test Dynamix APIs (Transaction, Cycles, Folder, Business Process, Test, Test Step, Step Run, Defect, Requirements — each supporting get-all/get/create/update),
  name: Panaya API
  slug: panaya-api
artifact_total: 6
asyncapis:
- description: ''
  name: Panaya Webhooks
  slug: panaya-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.panaya.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://success.panaya.com/docs/api
- group: docs
  title: ''
  type: Documentation
  url: https://success.panaya.com/docs/api
- group: docs
  title: ''
  type: APIReference
  url: https://success.panaya.com/docs/panaya-testing-api-supported-entities-and-functions
- group: start
  title: ''
  type: GettingStarted
  url: https://success.panaya.com/docs/api-guide
- group: auth
  title: ''
  type: Authentication
  url: authentication/panaya-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/panaya-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/panaya-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/panaya-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/panaya-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/panaya-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/panaya-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://success.panaya.com/docs/panaya-release-notes
- group: design
  title: ''
  type: Conformance
  url: conformance/panaya-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.panaya.com/gdpr-compliance/
- group: auth
  title: ''
  type: Security
  url: https://www.panaya.com/information-security-policy/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/panaya-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/panaya-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/panaya-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://success.panaya.com/docs
- group: operate
  title: ''
  type: HelpCenter
  url: https://success.panaya.com/docs
- group: company
  title: ''
  type: Blog
  url: https://www.panaya.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.panaya.com/panaya-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.panaya.com/panaya-privacy/
- group: start
  title: ''
  type: Login
  url: https://my.panaya.com/site/rdx
created: '2026-07-17'
description: Panaya is an enterprise change-intelligence and agentic-testing platform for business applications, helping organizations de-risk changes to SAP (including S/4HANA migrations and upgrades), Oracle (EBS, Cloud, NetSuite), Salesforce, Workday, ServiceNow and SuccessFactors. Its platform combines change impact analysis, test management and AI-driven test automation, with an agentic layer ("Seemore") that analyzes changes, generates and fixes tests, and guides teams. Panaya exposes a REST API (the Test Dynamix APIs plus code/patch upload and mass-export endpoints) with token-based authentication, documented rate limits, outbound webhooks via its Automation Rules Center, and integrations with Jira, SAP ChaRM and SAP Cloud ALM. Panaya is owned by Infosys and was previously backed by Battery Ventures.
image: https://www.panaya.com/wp-content/uploads/2021/01/panaya-logo.png
layout: provider
modified: '2026-07-20'
name: Panaya
nav: Providers
network: true
overview: 'Panaya publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Testing, Test Automation, Test Management, and Change Management.


  The Panaya catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Panaya''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, engineering blog, and 18 more developer resources.'
random_paper: 69
rate_limits:
- limit_count: 7
  name: Panaya Rate Limits
  slug: panaya-rate-limits
score:
  band: developing
  composite: 50.5
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 51.6
    developer_ergonomics: 52.2
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 65.8
  previous_composite: 50.5
  provenance:
    conformance: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Panaya Authentication
  slug: panaya-authentication
  summary_line: apiKey/custom-token · 2 schemes
- kind: domain-security
  name: Panaya Domain Security
  slug: panaya-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Panaya Vulnerability Disclosure
  slug: panaya-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: panaya
tags:
- Company
- Testing
- Test Automation
- Test Management
- Change Management
- Change Impact Analysis
- ERP
- SAP
- Oracle
- Salesforce
- Quality Assurance
- DevOps
website: https://www.panaya.com
---
