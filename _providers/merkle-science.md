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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: Query and retrieve off-chain VASP due-diligence entities.
  name: Merkle Science VASP Entities API
  slug: merkle-science-vasp-entities-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/merkle-science-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.merklescience.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/merkle-science-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://merklescience.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://kybb.docs.merklescience.com/
- group: docs
  title: ''
  type: Documentation
  url: https://kybb.docs.merklescience.com/docs/kybb-introduction
- group: docs
  title: ''
  type: APIReference
  url: https://kybb.docs.merklescience.com/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://kybb.docs.merklescience.com/reference/authentication
- group: auth
  title: ''
  type: Authentication
  url: authentication/merkle-science-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.merklescience.com/
- group: operate
  title: ''
  type: Support
  url: mailto:support@merklescience.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/merklescience
- group: start
  title: ''
  type: Login
  url: https://kybb.app.merklescience.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.merklescience.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.merklescience.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/merkle-science-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/merkle-science-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/merkle-science-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/merkle-science-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/merkle-science-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/merkle-science-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/merkle-science-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/merkle-science-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/merkle-science-well-known.yml
created: '2026-07-17'
description: Merkle Science is a blockchain analytics and predictive crypto risk platform that helps virtual asset businesses, financial institutions, and government agencies detect fraud, monitor transactions, and stay compliant with AML, KYC, and CFT regulations across 10,000+ crypto assets. Its product suite includes Compass (transaction and wallet monitoring), Tracker (forensic investigation and fund tracing), KYBB / Know Your Blockchain Business (counterparty due diligence and risk intelligence), Onchain Pulse (ecosystem monitoring and token risk scoring), and Institute (compliance training and certification). The public KYBB API exposes off-chain VASP due-diligence data — KYC/AML posture, supported coins and FIAT, permitted activities, regulatory alerts, licensing and legal-entity records, and jurisdictional restrictions. Merkle Science is backed by 500 Global.
image: https://www.merklescience.com/
layout: provider
mcp_servers:
- description: ''
  name: merkle-science-mcp.yml
  slug: merkle-science-mcpyml
modified: '2026-07-20'
name: Merkle Science
nav: Providers
network: true
overview: 'Merkle Science publishes 1 API on the [APIs.io](https://apis.io/) network: VASP Entities API. Tagged areas include Company, Blockchain Analytics, Cryptocurrency, Compliance, and AML.


  Merkle Science''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, sandbox, and 18 more developer resources.'
random_paper: 38
score:
  band: developing
  composite: 50.6
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 63.7
    developer_ergonomics: 73.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 50.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Merkle Science Authentication
  slug: merkle-science-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Merkle Science Domain Security
  slug: merkle-science-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Merkle Science Trust Center
  slug: merkle-science-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: merkle-science
tags:
- Company
- Blockchain Analytics
- Cryptocurrency
- Compliance
- AML
- KYC
- Risk
- Fraud Detection
- Due Diligence
- RegTech
website: https://merklescience.com
---
