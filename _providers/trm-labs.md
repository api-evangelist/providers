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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Trm Labs Agentic Access
  operation_count: 5
  slug: trm-labs-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 3
apis:
- description: Contribute, retrieve, and look up scam reports.
  name: TRM Labs Reports API
  slug: trm-labs-reports-api
- description: Check whether an address is sanctioned.
  name: TRM Labs Sanctions API
  slug: trm-labs-sanctions-api
- description: The Sanctions Screening API from TRM Labs — 1 operation(s) for sanctions screening.
  name: TRM Labs Sanctions Screening API
  slug: trm-labs-sanctions-screening-api
artifact_total: 10
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trm-labs-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/trm-labs-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.trmlabs.com/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/trm-labs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.trmlabs.com/responsible-disclosure
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trm-labs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trm-labs-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/trm-labs-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/trm-labs-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/trm-labs-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/trm-labs-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.trmlabs.com
- group: design
  title: ''
  type: Conformance
  url: conformance/trm-labs-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/trm-labs-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/trm-labs-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trm-labs-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trmlabs.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.trmlabs.com/guides/chainabuse/welcome-to-chainabuse-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.trmlabs.com/guides/chainabuse/getting-started
- group: operate
  title: ''
  type: Support
  url: https://docs.trmlabs.com/guides/chainabuse/contact
- group: company
  title: ''
  type: Blog
  url: https://www.trmlabs.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trmlabs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trmlabs.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://www.trmlabs.com/products/sanctions
- group: company
  title: ''
  type: Website
  url: https://www.trmlabs.com/
created: '2026-07-17'
description: TRM Labs is a blockchain intelligence company that helps financial institutions, crypto businesses, and government agencies detect and investigate crypto-related fraud, money laundering, and sanctions violations. Its public API surface includes the TRM Sanctions API for screening blockchain addresses against sanctions lists, and the Chainabuse Public API (community-sourced scam reporting) for contributing, retrieving, and looking up reports of malicious addresses, tokens, transactions, and domains. Both APIs use HTTP Basic authentication and are documented at docs.trmlabs.com.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trm-labs.png
layout: provider
mcp_servers:
- description: ''
  name: trm-labs-mcp.yml
  slug: trm-labs-mcpyml
modified: '2026-07-21'
name: TRM Labs
nav: Providers
network: true
overview: 'TRM Labs publishes 3 APIs on the [APIs.io](https://apis.io/) network: Reports API, Sanctions API, and Sanctions Screening API. Tagged areas include Company, Crypto, Blockchain, Compliance, and Sanctions.


  TRM Labs'' developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 19 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 0
  name: Trm Labs Rate Limits
  slug: trm-labs-rate-limits
score:
  band: developing
  composite: 47.6
  delta: -1.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.9
    developer_ergonomics: 47.3
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 31.6
  previous_composite: 48.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Trm Labs Authentication
  slug: trm-labs-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Trm Labs Domain Security
  slug: trm-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Trm Labs Vulnerability Disclosure
  slug: trm-labs-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Trm Labs Trust Center
  slug: trm-labs-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP
slug: trm-labs
tags:
- Company
- Crypto
- Blockchain
- Compliance
- Sanctions
- Fraud
- Anti-Money Laundering
- Blockchain Intelligence
website: https://www.trmlabs.com/
---
