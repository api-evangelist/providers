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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 29
  human_in_the_loop: 1
  name: Valimail Agentic Access
  operation_count: 57
  slug: valimail-agentic-access
  summary_line: 57 operations · 29 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: Retrieve email authentication metrics, sender reports, and unidentified sender reports for compliance dashboards and security insights. Documented for customers in the Valimail help center; credential
  name: Valimail Reporting Data API
  slug: valimail-reporting-data-api
- baseURL: https://api.valimail.com
  baseurl_source: declared
  description: The Accounts API from Valimail — 4 operation(s) for accounts.
  name: Valimail Accounts API
  slug: valimail-accounts-api
- baseURL: https://api.valimail.com
  baseurl_source: declared
  description: The Authentication API from Valimail — 1 operation(s) for authentication.
  name: Valimail Authentication API
  slug: valimail-authentication-api
- baseURL: https://api.valimail.com
  baseurl_source: declared
  description: The DKIMs by Domain API from Valimail — 2 operation(s) for dkims by domain.
  name: Valimail DKIMs by Domain API
  slug: valimail-dkims-by-domain-api
- baseURL: https://api.valimail.com
  baseurl_source: declared
  description: The DKIMs by Sender API from Valimail — 2 operation(s) for dkims by sender.
  name: Valimail DKIMs by Sender API
  slug: valimail-dkims-by-sender-api
- baseURL: https://api.valimail.com
  baseurl_source: declared
  description: The Domains API from Valimail — 2 operation(s) for domains.
  name: Valimail Domains API
  slug: valimail-domains-api
- baseURL: https://api.valimail.com
  baseurl_source: declared
  description: The MTA-STS Policy API from Valimail — 2 operation(s) for mta-sts policy.
  name: Valimail MTA-STS Policy API
  slug: valimail-mta-sts-policy-api
- baseURL: https://api.valimail.com
  baseurl_source: declared
  description: The MTA-STS Policy Reports API from Valimail — 3 operation(s) for mta-sts policy reports.
  name: Valimail MTA-STS Policy Reports API
  slug: valimail-mta-sts-policy-reports-api
- baseURL: https://api.valimail.com
  baseurl_source: declared
  description: The Netblocks API from Valimail — 2 operation(s) for netblocks.
  name: Valimail Netblocks API
  slug: valimail-netblocks-api
- baseURL: https://api.valimail.com
  baseurl_source: declared
  description: The Portfolios API from Valimail — 1 operation(s) for portfolios.
  name: Valimail Portfolios API
  slug: valimail-portfolios-api
- baseURL: https://api.valimail.com
  baseurl_source: declared
  description: The SCIM API from Valimail — 2 operation(s) for scim.
  name: Valimail SCIM API
  slug: valimail-scim-api
- baseURL: https://api.valimail.com
  baseurl_source: declared
  description: The Senders API from Valimail — 3 operation(s) for senders.
  name: Valimail Senders API
  slug: valimail-senders-api
- baseURL: https://api.valimail.com
  baseurl_source: declared
  description: The SSO API from Valimail — 1 operation(s) for sso.
  name: Valimail SSO API
  slug: valimail-sso-api
- baseURL: https://api.valimail.com
  baseurl_source: declared
  description: The TLS Configuration API from Valimail — 2 operation(s) for tls configuration.
  name: Valimail TLS Configuration API
  slug: valimail-tls-configuration-api
- baseURL: https://api.valimail.com
  baseurl_source: declared
  description: The Users API from Valimail — 4 operation(s) for users.
  name: Valimail Users API
  slug: valimail-users-api
- baseURL: https://api.valimail.com
  baseurl_source: declared
  description: The Webhooks API from Valimail — 1 operation(s) for webhooks.
  name: Valimail Webhooks API
  slug: valimail-webhooks-api
- baseURL: https://api.valimail.com
  baseurl_source: declared
  description: The Senders Reports API from Valimail — 1 operation(s) for senders reports.
  name: Valimail Senders Reports API
  slug: valimail-senders-reports-api
- baseURL: https://api.valimail.com
  baseurl_source: declared
  description: The Teams API from Valimail — 2 operation(s) for teams.
  name: Valimail Teams API
  slug: valimail-teams-api
artifact_total: 42
asyncapis:
- description: ''
  name: Valimail Webhooks
  slug: valimail-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Account Management Accounts API
  slug: open-valimail-accounts-api
- collection_type: open
  name: Account Management Accounts Authentication API
  slug: open-valimail-authentication-api
- collection_type: open
  name: Account Management Accounts DKIMs by Domain API
  slug: open-valimail-dkims-by-domain-api
- collection_type: open
  name: Account Management Accounts DKIMs by Sender API
  slug: open-valimail-dkims-by-sender-api
- collection_type: open
  name: Account Management Accounts Domains API
  slug: open-valimail-domains-api
- collection_type: open
  name: Account Management Accounts MTA-STS Policy API
  slug: open-valimail-mta-sts-policy-api
- collection_type: open
  name: Account Management Accounts MTA-STS Policy Reports API
  slug: open-valimail-mta-sts-policy-reports-api
- collection_type: open
  name: Account Management Accounts Netblocks API
  slug: open-valimail-netblocks-api
- collection_type: open
  name: Account Management Accounts Portfolios API
  slug: open-valimail-portfolios-api
- collection_type: open
  name: Account Management Accounts SCIM API
  slug: open-valimail-scim-api
- collection_type: open
  name: Account Management Accounts Senders API
  slug: open-valimail-senders-api
- collection_type: open
  name: Account Management Accounts SSO API
  slug: open-valimail-sso-api
- collection_type: open
  name: Account Management Accounts TLS Configuration API
  slug: open-valimail-tls-configuration-api
- collection_type: open
  name: Account Management Accounts Users API
  slug: open-valimail-users-api
- collection_type: open
  name: Account Management Accounts Webhooks API
  slug: open-valimail-webhooks-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/valimail-account-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/valimail-config-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/valimail-partner-overlay.yaml
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
- group: start
  title: ''
  type: SignUp
  url: https://www.valimail.com/try-monitor-free/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.valimail.com/en/collections/12071845-introduction-to-the-valimail-apis
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
  type: X-MCPServerCandidate
  url: mcp/valimail-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/valimail-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/valimail-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/valimail-rate-limits.yml
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
modified: '2026-08-14'
name: Valimail
nav: Providers
network: true
overview: 'Valimail publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Authentication API, DKIMs by Domain API, and 14 more. Tagged areas include Email Authentication, DMARC, Email Security, SPF, and DKIM.


  The Valimail catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Valimail''s developer surface includes developer portal, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 33 more developer resources.'
plans:
- name: Valimail Plans Pricing
  plan_count: 5
  slug: valimail-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Valimail Rate Limits
  slug: valimail-rate-limits
score:
  band: strong
  composite: 62.7
  coverage:
    artifact_dirs: 23
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 4.5
    contract_quality: 62.3
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 52.6
  previous_composite: 62.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/valimail/refs/heads/main/screenshots/valimail-2026-08-17T082710.png
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
