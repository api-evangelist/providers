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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 65.4
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Certik Agentic Access
  operation_count: 4
  slug: certik-agentic-access
  summary_line: 4 operations
api_count: 2
apis:
- description: Skynet multi-metric project security scores.
  name: CertiK Security Score API
  slug: certik-security-score-api
- description: Real-time on-chain token contract security analysis.
  name: CertiK Token Scan API
  slug: certik-token-scan-api
artifact_total: 8
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.certik-skynet.com/public-docs/
- group: docs
  title: ''
  type: Documentation
  url: https://api.certik-skynet.com/public-docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.certik-skynet.com/public-docs/apis/security-score
- group: auth
  title: ''
  type: Authentication
  url: authentication/certik-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/certik-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/certik-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/certik-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/certik-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/certik-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/certik-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/certik-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.certik.com/company/trust-and-security
- group: auth
  title: ''
  type: TrustCenter
  url: security/certik-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/certik-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.certik.com/company/bug-bounty
- group: auth
  title: ''
  type: DomainSecurity
  url: security/certik-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/certik-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/certik-changelog.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/certik-skynet-overlay.yaml
- group: company
  title: ''
  type: Blog
  url: https://www.certik.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CertiKProject
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.certik.com/company/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:APIsupport@certik.com
- group: company
  title: ''
  type: Website
  url: https://www.certik.com/
created: '2026-07-17'
description: 'CertiK is a leading Web3 security platform that combines AI, formal verification, and expert audits to secure blockchain protocols and smart contracts. Its Partner (Skynet) API exposes CertiK''s security intelligence to integrators: the Skynet Security Score API returns comprehensive, multi-metric security scores for blockchain projects (score, rank, tier, percentile, highlights and alerts), and the Token Scan API returns real-time on-chain security analysis of token contracts across major chains (token info, market and holder data, a SkyKnight score, and a severity-ranked security summary). Access is by partner API key issued by the CertiK Business Team, sent in the X-Certik-Api-Key header against https://partner.certik-skynet.com. CertiK is a portfolio company of Insight Partners, Lightspeed Venture Partners, SoftBank Vision Fund and Wing Venture Capital.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/certik.png
layout: provider
mcp_servers:
- description: ''
  name: certik-mcp.yml
  slug: certik-mcpyml
modified: '2026-07-18'
name: CertiK
nav: Providers
network: true
overview: 'CertiK publishes 2 APIs on the [APIs.io](https://apis.io/) network: Security Score API and Token Scan API. Tagged areas include Company, Cybersecurity, Web3, Blockchain, and Smart Contract Security.


  CertiK''s developer surface includes documentation, API reference, authentication, changelog, engineering blog, support, and 19 more developer resources.'
random_paper: 30
score:
  band: thin
  composite: 44.5
  delta: 0.0
  facets:
    commercial_clarity: 26.3
    contract_quality: 58.4
    developer_ergonomics: 56.5
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 44.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Certik Authentication
  slug: certik-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Certik Domain Security
  slug: certik-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Certik Vulnerability Disclosure
  slug: certik-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Certik Trust Center
  slug: certik-trust-center
  summary_line: SOC 2 Type II, ISO 27001
slug: certik
tags:
- Company
- Cybersecurity
- Web3
- Blockchain
- Smart Contract Security
- Security Auditing
- Threat Intelligence
website: https://www.certik.com/
---
