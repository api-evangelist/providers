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
    asyncapi_events: true
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
  score: 75.0
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 37
  human_in_the_loop: 1
  name: Upguard Agentic Access
  operation_count: 133
  slug: upguard-agentic-access
  summary_line: 133 operations · 37 acting · 1 human-in-the-loop
api_count: 18
apis:
- description: The breaches API from UpGuard — 5 operation(s) for breaches.
  name: UpGuard breaches API
  slug: upguard-breaches-api
- description: The bulk API from UpGuard — 4 operation(s) for bulk.
  name: UpGuard bulk API
  slug: upguard-bulk-api
- description: The dataleaks API from UpGuard — 2 operation(s) for dataleaks.
  name: UpGuard dataleaks API
  slug: upguard-dataleaks-api
- description: The domains API from UpGuard — 3 operation(s) for domains.
  name: UpGuard domains API
  slug: upguard-domains-api
- description: The ips API from UpGuard — 4 operation(s) for ips.
  name: UpGuard ips API
  slug: upguard-ips-api
- description: The labels API from UpGuard — 1 operation(s) for labels.
  name: UpGuard labels API
  slug: upguard-labels-api
- description: The notifications API from UpGuard — 1 operation(s) for notifications.
  name: UpGuard notifications API
  slug: upguard-notifications-api
- description: The organisation API from UpGuard — 1 operation(s) for organisation.
  name: UpGuard organisation API
  slug: upguard-organisation-api
- description: The reports API from UpGuard — 3 operation(s) for reports.
  name: UpGuard reports API
  slug: upguard-reports-api
- description: The risks API from UpGuard — 13 operation(s) for risks.
  name: UpGuard risks API
  slug: upguard-risks-api
- description: The subsidiaries API from UpGuard — 8 operation(s) for subsidiaries.
  name: UpGuard subsidiaries API
  slug: upguard-subsidiaries-api
- description: The threatmonitoring API from UpGuard — 9 operation(s) for threatmonitoring.
  name: UpGuard threatmonitoring API
  slug: upguard-threatmonitoring-api
- description: The trust_exchange API from UpGuard — 15 operation(s) for trust_exchange.
  name: UpGuard trust_exchange API
  slug: upguard-trust-exchange-api
- description: The typosquat API from UpGuard — 2 operation(s) for typosquat.
  name: UpGuard typosquat API
  slug: upguard-typosquat-api
- description: The userrisk API from UpGuard — 15 operation(s) for userrisk.
  name: UpGuard userrisk API
  slug: upguard-userrisk-api
- description: The vendors API from UpGuard — 32 operation(s) for vendors.
  name: UpGuard vendors API
  slug: upguard-vendors-api
- description: The vulnerabilities API from UpGuard — 2 operation(s) for vulnerabilities.
  name: UpGuard vulnerabilities API
  slug: upguard-vulnerabilities-api
- description: The webhooks API from UpGuard — 3 operation(s) for webhooks.
  name: UpGuard webhooks API
  slug: upguard-webhooks-api
artifact_total: 25
asyncapis:
- description: ''
  name: Upguard Webhooks
  slug: upguard-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/upguard-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/upguard-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/upguard-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/upguard-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.upguard.com
- group: docs
  title: ''
  type: Documentation
  url: https://cyber-risk.upguard.com/api/docs
- group: docs
  title: ''
  type: APIReference
  url: https://cyber-risk.upguard.com/api/docs
- group: operate
  title: ''
  type: Support
  url: https://help.upguard.com
- group: company
  title: ''
  type: Blog
  url: https://www.upguard.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.upguard.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.upguard.com/demo
- group: start
  title: ''
  type: Login
  url: https://cyber-risk.upguard.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.upguard.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.upguard.com/company/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ScriptRock
- group: operate
  title: ''
  type: StatusPage
  url: https://status.upguard.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.upguard.com/releases
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/upguard-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/upguard-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/upguard-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/upguard-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/upguard-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/upguard-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/upguard-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.upguard.com/security
- group: auth
  title: ''
  type: Security
  url: https://www.upguard.com/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/upguard-vulnerability-disclosure.yml
- group: build
  title: ''
  type: Packages
  url: packages/upguard-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/upguard-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/upguard-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/upguard-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/upguard-data-model.yml
created: '2026-07-17'
description: UpGuard is a cybersecurity platform that helps organizations manage and reduce their cyber risk. Its products cover third-party vendor risk management (Vendor Risk), attack surface management and external threat monitoring (Breach Risk), and AI-powered security questionnaire automation and trust center tooling (Trust Exchange). The UpGuard CyberRisk API exposes the platform programmatically — vendors and security ratings, risks and vulnerabilities, domains and IPs, data leak disclosures, identity breaches, typosquatting, questionnaires, subsidiaries, labels, notifications, and webhooks — authenticated with an API key from CyberRisk account settings.
image: https://content.upguard.com/hubfs/open-graph/home.png
layout: provider
mcp_servers:
- description: ''
  name: upguard-mcp.yml
  slug: upguard-mcpyml
modified: '2026-07-21'
name: UpGuard
nav: Providers
network: true
overview: 'UpGuard publishes 18 APIs on the [APIs.io](https://apis.io/) network, including breaches API, bulk API, dataleaks API, and 15 more. Tagged areas include Company, Cybersecurity, Third-Party Risk Management, Attack Surface Management, and Vendor Risk.


  The UpGuard catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  UpGuard''s developer surface includes authentication, documentation, API reference, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
random_paper: 46
score:
  band: developing
  composite: 55.2
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 60.4
    developer_ergonomics: 54.3
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 55.3
  previous_composite: 55.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Upguard Authentication
  slug: upguard-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Upguard Domain Security
  slug: upguard-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Upguard Vulnerability Disclosure
  slug: upguard-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Upguard Trust Center
  slug: upguard-trust-center
  summary_line: SOC 2 Type II
slug: upguard
tags:
- Company
- Cybersecurity
- Third-Party Risk Management
- Attack Surface Management
- Vendor Risk
- Security Ratings
- Data Leaks
- Threat Intelligence
website: https://www.upguard.com
---
