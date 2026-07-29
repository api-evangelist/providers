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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 53.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 29
  human_in_the_loop: 1
  name: Valimail Agentic Access
  operation_count: 57
  slug: valimail-agentic-access
  summary_line: 57 operations · 29 acting · 1 human-in-the-loop
api_count: 16
apis:
- description: Retrieve email authentication metrics, sender reports, and unidentified sender reports for compliance dashboards and security insights. Documented for customers in the Valimail help center; credential
  name: Valimail Reporting Data API
  slug: valimail-reporting-data-api
- description: The Accounts API from Valimail — 4 operation(s) for accounts.
  name: Valimail Accounts API
  slug: valimail-accounts-api
- description: The Authentication API from Valimail — 1 operation(s) for authentication.
  name: Valimail Authentication API
  slug: valimail-authentication-api
- description: The DKIMs by Domain API from Valimail — 2 operation(s) for dkims by domain.
  name: Valimail DKIMs by Domain API
  slug: valimail-dkims-by-domain-api
- description: The DKIMs by Sender API from Valimail — 2 operation(s) for dkims by sender.
  name: Valimail DKIMs by Sender API
  slug: valimail-dkims-by-sender-api
- description: The Domains API from Valimail — 2 operation(s) for domains.
  name: Valimail Domains API
  slug: valimail-domains-api
- description: The MTA-STS Policy API from Valimail — 2 operation(s) for mta-sts policy.
  name: Valimail MTA-STS Policy API
  slug: valimail-mta-sts-policy-api
- description: The MTA-STS Policy Reports API from Valimail — 3 operation(s) for mta-sts policy reports.
  name: Valimail MTA-STS Policy Reports API
  slug: valimail-mta-sts-policy-reports-api
- description: The Netblocks API from Valimail — 2 operation(s) for netblocks.
  name: Valimail Netblocks API
  slug: valimail-netblocks-api
- description: The Portfolios API from Valimail — 1 operation(s) for portfolios.
  name: Valimail Portfolios API
  slug: valimail-portfolios-api
- description: The SCIM API from Valimail — 2 operation(s) for scim.
  name: Valimail SCIM API
  slug: valimail-scim-api
- description: The Senders API from Valimail — 3 operation(s) for senders.
  name: Valimail Senders API
  slug: valimail-senders-api
- description: The SSO API from Valimail — 1 operation(s) for sso.
  name: Valimail SSO API
  slug: valimail-sso-api
- description: The TLS Configuration API from Valimail — 2 operation(s) for tls configuration.
  name: Valimail TLS Configuration API
  slug: valimail-tls-configuration-api
- description: The Users API from Valimail — 4 operation(s) for users.
  name: Valimail Users API
  slug: valimail-users-api
- description: The Webhooks API from Valimail — 1 operation(s) for webhooks.
  name: Valimail Webhooks API
  slug: valimail-webhooks-api
artifact_total: 23
asyncapis:
- description: ''
  name: Valimail Webhooks
  slug: valimail-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.valimail.com/
- group: start
  title: ''
  type: Portal
  url: https://app.valimail.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.valimail.com/en/collections/6449843-learn-more-about-our-apis
- group: docs
  title: ''
  type: APIReference
  url: https://api.valimail.com/docs/config.html
- group: start
  title: ''
  type: GettingStarted
  url: https://support.valimail.com/en/articles/10580387-requesting-api-access
- group: operate
  title: ''
  type: Support
  url: https://support.valimail.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.valimail.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ValiMail
- group: commercial
  title: ''
  type: Pricing
  url: https://www.valimail.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://app.valimail.com/auth/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.valimail.com/legal/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.valimail.com/legal/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.valimail.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/valimail-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/valimail-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/valimail-authentication.yml
- group: auth
  title: ''
  type: Security
  url: https://security.valimail.com/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/valimail-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/valimail-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.valimail.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/valimail-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/valimail-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/valimail-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/valimail-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/valimail-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/valimail-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/valimail-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/valimail-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/valimail-well-known.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/valimail-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/valimail-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/valimail-agentic-access.yml
- group: commercial
  title: ''
  type: APITermsOfUse
  url: https://www.valimail.com/api-terms-of-use/
created: '2026-07-17'
description: Valimail is an email authentication platform that automates DMARC enforcement to stop phishing, spoofing, and brand impersonation. Its Monitor, Enforce, Amplify, and Align products give organizations visibility into every service sending on their domains and manage SPF, DKIM, DMARC, BIMI, MTA-STS, and TLS-RPT at scale. Valimail publishes REST APIs — a DMARC Configuration API, a partner Account Management API, and a Reporting Data API — secured with bearer tokens, plus SCIM 2.0 user provisioning and Ed25519-signed webhooks. The platform is FedRAMP LI-SaaS authorized and SOC 2 Type II certified.
image: https://api.valimail.com/images/sites/valimail/favicon_64.png
layout: provider
mcp_servers:
- description: ''
  name: valimail-mcp.yml
  slug: valimail-mcpyml
modified: '2026-07-21'
name: Valimail
nav: Providers
network: true
overview: 'Valimail publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Authentication API, DKIMs by Domain API, and 12 more. Tagged areas include Email Authentication, DMARC, Email Security, SPF, and DKIM.


  The Valimail catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Valimail''s developer surface includes developer portal, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 27 more developer resources.'
random_paper: 57
score:
  band: strong
  composite: 57.5
  delta: -1.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 60.1
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 55.3
  previous_composite: 58.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Valimail Authentication
  slug: valimail-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Valimail Domain Security
  slug: valimail-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Valimail Vulnerability Disclosure
  slug: valimail-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Valimail Trust Center
  slug: valimail-trust-center
  summary_line: SOC 2 Type II, SOC 3, FedRAMP LI-SaaS
slug: valimail
tags:
- Email Authentication
- DMARC
- Email Security
- SPF
- DKIM
- BIMI
- MTA-STS
- Anti-Phishing
- Deliverability
- Cybersecurity
website: https://www.valimail.com/
---
