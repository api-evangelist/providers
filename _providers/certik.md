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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.4
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Certik Agentic Access
  operation_count: 4
  slug: certik-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://partner.certik-skynet.com
  baseurl_source: declared
  description: Skynet multi-metric project security scores.
  name: CertiK Security Score API
  slug: certik-security-score-api
- baseURL: https://partner.certik-skynet.com
  baseurl_source: declared
  description: Real-time on-chain token contract security analysis.
  name: CertiK Token Scan API
  slug: certik-token-scan-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CertiK Partner (Skynet) Security Score API
  slug: open-certik-security-score-api
- collection_type: open
  name: CertiK Partner (Skynet) Security Score Token Scan API
  slug: open-certik-token-scan-api
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
  name: CertiK MCP Server
  slug: certik-mcp-server
modified: '2026-07-18'
name: CertiK
nav: Providers
network: true
overview: 'CertiK publishes 2 APIs on the [APIs.io](https://apis.io/) network: Security Score API and Token Scan API. Tagged areas include Company, Cybersecurity, Web3, Blockchain, and Smart Contract Security.


  CertiK''s developer surface includes documentation, API reference, authentication, changelog, engineering blog, support, and 19 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 34.0
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 18.2
    contract_quality: 13.9
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 34.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/certik/refs/heads/main/screenshots/certik-2026-07-25T205001.png
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
