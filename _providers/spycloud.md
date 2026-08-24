---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 45.5
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Spycloud Agentic Access
  operation_count: 69
  slug: spycloud-agentic-access
  summary_line: 69 operations · 2 acting
api_count: 7
apis:
- description: The Breach API from SpyCloud — 23 operation(s) for breach.
  name: SpyCloud Breach API
  slug: spycloud-breach-api
- description: The Check API from SpyCloud — 2 operation(s) for check.
  name: SpyCloud Check API
  slug: spycloud-check-api
- description: The Compass API from SpyCloud — 5 operation(s) for compass.
  name: SpyCloud Compass API
  slug: spycloud-compass-api
- description: The Data API from SpyCloud — 2 operation(s) for data.
  name: SpyCloud Data API
  slug: spycloud-data-api
- description: The Query API from SpyCloud — 3 operation(s) for query.
  name: SpyCloud Query API
  slug: spycloud-query-api
- description: The Stats API from SpyCloud — 2 operation(s) for stats.
  name: SpyCloud Stats API
  slug: spycloud-stats-api
- description: The Watchlist API from SpyCloud — 5 operation(s) for watchlist.
  name: SpyCloud Watchlist API
  slug: spycloud-watchlist-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Spycloud Breach API
  slug: open-spycloud-breach-api
- collection_type: open
  name: Spycloud Check API
  slug: open-spycloud-check-api
- collection_type: open
  name: enterprise-ato-prevention-api Compass API
  slug: open-spycloud-compass-api
- collection_type: open
  name: compromised-credit-card-api Data API
  slug: open-spycloud-data-api
- collection_type: open
  name: idlink-api Query API
  slug: open-spycloud-query-api
- collection_type: open
  name: prospecting-api Stats API
  slug: open-spycloud-stats-api
- collection_type: open
  name: enterprise-ato-prevention-api Watchlist API
  slug: open-spycloud-watchlist-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/spycloud-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/spycloud-compromised-credit-card-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spycloud-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spycloud-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spycloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spycloud-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://spycloud.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.spycloud.com/public-sc
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spycloud.com/public-sc/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.spycloud.com/public-sc/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.spycloud.com/public-sc/docs/api-guidelines
- group: operate
  title: ''
  type: Support
  url: https://spycloud.com/support/
- group: company
  title: ''
  type: Blog
  url: https://spycloud.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://spycloud.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://spycloud.com/request-a-demo/
- group: start
  title: ''
  type: Login
  url: https://portal.spycloud.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://spycloud.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://spycloud.com/legal/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.spycloud.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.spycloud.com/public-sc/page/release-notes-1
- group: auth
  title: ''
  type: Compliance
  url: https://spycloud.com/legal/governance-risk-and-compliance/
- group: auth
  title: ''
  type: TrustCenter
  url: https://app.vanta.com/spycloud.com/trust/itvhddyqxnnf6gi6aatcx
- group: auth
  title: ''
  type: Security
  url: https://spycloud.com/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/spycloud-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/spycloud-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/spycloud-api-catalog.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spycloud-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/spycloud-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spycloud-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spycloud-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/spycloud-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/spycloud-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spycloud-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spycloud-data-model.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/spycloud-trust-center.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-05'
description: 'SpyCloud is an Austin, Texas based identity threat protection company that operates one of the largest repositories of recaptured darknet data — breach records, infostealer malware logs, phishing captures and combolists — and exposes it programmatically through a family of high-volume REST APIs. Security, fraud, identity and investigations teams query recaptured credentials, session cookies, exposed PII and infected-device telemetry to prevent account takeover, ransomware, session hijacking and online fraud. The public API surface spans nine separately-licensed products: Enterprise (Employee) ATO Prevention, Consumer ATO Prevention, Cybercrime Investigations, Data Partnership, IDLink identity correlation, Compromised Credit Card, Prospecting, NIST Password check, and Session Identity Protection. All are REST/JSON, authenticated with an x-api-key header, IP allow-listed, cursor-paginated at 1,000 records per page, and backed by a 99.9% uptime SLA.'
image: https://spycloud.com/wp-content/uploads/2025/04/bg-img-dotted-lines-1920x700-1-1.png
layout: provider
mcp_servers:
- description: ''
  name: SpyCloud MCP Server
  slug: spycloud-mcp-server
modified: '2026-08-05'
name: SpyCloud
nav: Providers
network: true
overview: 'SpyCloud publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Breach API, Check API, Compass API, and 4 more. Tagged areas include Cybersecurity, Threat Intelligence, Identity, Fraud Prevention, and Account Takeover.


  SpyCloud''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 29 more developer resources.'
random_paper: 1
rate_limits:
- limit_count: 0
  name: Spycloud Rate Limits
  slug: spycloud-rate-limits
score:
  band: developing
  composite: 42.3
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 16.7
    contract_quality: 54.5
    developer_ergonomics: 20.8
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 21.1
  previous_composite: 42.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spycloud/refs/heads/main/screenshots/spycloud-2026-08-17T082052.png
security:
- kind: authentication
  name: Spycloud Authentication
  slug: spycloud-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Spycloud Domain Security
  slug: spycloud-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Spycloud Vulnerability Disclosure
  slug: spycloud-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Spycloud Trust Center
  slug: spycloud-trust-center
  summary_line: SOC 2, ISO 27001
slug: spycloud
tags:
- Cybersecurity
- Threat Intelligence
- Identity
- Fraud Prevention
- Account Takeover
- Dark Web
- Breach Data
- Malware
- Authentication
- Security
website: https://spycloud.com/
---
