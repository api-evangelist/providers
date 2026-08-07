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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 59
  human_in_the_loop: 0
  name: Cable Agentic Access
  operation_count: 77
  slug: cable-agentic-access
  summary_line: 77 operations · 59 acting
api_count: 20
apis:
- description: The alerts API from Cable — 1 operation(s) for alerts.
  name: Cable alerts API
  slug: cable-alerts-api
- description: The authentication API from Cable — 2 operation(s) for authentication.
  name: Cable authentication API
  slug: cable-authentication-api
- description: The business API from Cable — 9 operation(s) for business.
  name: Cable business API
  slug: cable-business-api
- description: The checks API from Cable — 1 operation(s) for checks.
  name: Cable checks API
  slug: cable-checks-api
- description: The company API from Cable — 1 operation(s) for company.
  name: Cable company API
  slug: cable-company-api
- description: The customerSar API from Cable — 1 operation(s) for customersar.
  name: Cable customerSar API
  slug: cable-customersar-api
- description: The helper API from Cable — 1 operation(s) for helper.
  name: Cable helper API
  slug: cable-helper-api
- description: The identityVerification API from Cable — 1 operation(s) for identityverification.
  name: Cable identityVerification API
  slug: cable-identityverification-api
- description: The onboardingFlow API from Cable — 1 operation(s) for onboardingflow.
  name: Cable onboardingFlow API
  slug: cable-onboardingflow-api
- description: The person API from Cable — 1 operation(s) for person.
  name: Cable person API
  slug: cable-person-api
- description: The retail API from Cable — 8 operation(s) for retail.
  name: Cable retail API
  slug: cable-retail-api
- description: The riskAssessment API from Cable — 1 operation(s) for riskassessment.
  name: Cable riskAssessment API
  slug: cable-riskassessment-api
- description: The screening API from Cable — 2 operation(s) for screening.
  name: Cable screening API
  slug: cable-screening-api
- description: The suspiciousActivities API from Cable — 1 operation(s) for suspiciousactivities.
  name: Cable suspiciousActivities API
  slug: cable-suspiciousactivities-api
- description: The transactionAlerts API from Cable — 1 operation(s) for transactionalerts.
  name: Cable transactionAlerts API
  slug: cable-transactionalerts-api
- description: The transactionChecks API from Cable — 1 operation(s) for transactionchecks.
  name: Cable transactionChecks API
  slug: cable-transactionchecks-api
- description: The transactions API from Cable — 4 operation(s) for transactions.
  name: Cable transactions API
  slug: cable-transactions-api
- description: The transactionSuspiciousActivities API from Cable — 1 operation(s) for transactionsuspiciousactivities.
  name: Cable transactionSuspiciousActivities API
  slug: cable-transactionsuspiciousactivities-api
- description: The upload API from Cable — 1 operation(s) for upload.
  name: Cable upload API
  slug: cable-upload-api
- description: The utilities API from Cable — 1 operation(s) for utilities.
  name: Cable utilities API
  slug: cable-utilities-api
artifact_total: 26
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cable-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cable-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cable.tech/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.cable.tech/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cable.tech/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cable.tech/api-documentation/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cable.tech/api-documentation/getting-started
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.cable.tech/knowledge-base/getting-started
- group: company
  title: ''
  type: Blog
  url: https://cable.tech/resources
- group: start
  title: ''
  type: Login
  url: https://app.cable.tech/home
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cable.tech/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cable.tech/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://cable.tech/responsible-disclosure-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.cable.tech/product-updates
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cable-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cable-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cable-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cable-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cable-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/cable-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cable-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cable-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cable-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/cable-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cable-trust-center.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cable-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cable-api-reference-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cable-customer-data-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cable-transaction-data-api-overlay.yaml
created: '2026-07-17'
description: 'Cable is an automated compliance and financial-crime assurance platform for banks, fintechs, and crypto companies. Based on transaction, customer, screening, risk-assessment, and onboarding data you send it, Cable continuously tests 100% of activity against your regulatory frameworks (US Bank Secrecy Act, UK Money Laundering Regulations, Reg E/B/Z, UDAAP, and others) to detect any single instance of control failure or regulatory breach, replacing manual dip-sampling. The Cable API is primarily a data-ingestion surface: a REST entry point for transferring raw data from your systems into Cable''s analysis environment, with resource-oriented URLs, JSON request/response bodies, token-based authentication, and standard HTTP verbs and status codes. Cable is backed by Anthemis and CRV.'
image: https://cable.tech/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: cable-mcp.yml
  slug: cable-mcpyml
modified: '2026-07-18'
name: Cable
nav: Providers
network: true
overview: 'Cable publishes 20 APIs on the [APIs.io](https://apis.io/) network, including alerts API, authentication API, business API, and 17 more. Tagged areas include Company, Compliance, Financial Crime, RegTech, and Anti-Money Laundering.


  Cable''s developer surface includes documentation, API reference, getting-started guide, engineering blog, changelog, authentication, and 24 more developer resources.'
random_paper: 51
score:
  band: developing
  composite: 49.6
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 55.0
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 26.3
  previous_composite: 49.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 45.6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cable/refs/heads/main/screenshots/cable-2026-07-25T204213.png
security:
- kind: authentication
  name: Cable Authentication
  slug: cable-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Cable Domain Security
  slug: cable-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cable Vulnerability Disclosure
  slug: cable-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Cable Trust Center
  slug: cable-trust-center
  summary_line: SOC 2 Type I
slug: cable
tags:
- Company
- Compliance
- Financial Crime
- RegTech
- Anti-Money Laundering
- Transaction Monitoring
- Screening
- Risk Assessment
- Banking
- Fintech
website: https://cable.tech/
---
