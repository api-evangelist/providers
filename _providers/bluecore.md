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
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: documented
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Bluecore Agentic Access
  operation_count: 9
  slug: bluecore-agentic-access
  summary_line: 9 operations · 6 acting
api_count: 6
apis:
- description: The Authn API from Bluecore — 1 operation(s) for authn.
  name: Bluecore Authn API
  slug: bluecore-authn-api
- description: The CampaignsAPIPublic API from Bluecore — 1 operation(s) for campaignsapipublic.
  name: Bluecore CampaignsAPIPublic API
  slug: bluecore-campaignsapipublic-api
- description: The Direct send API from Bluecore — 1 operation(s) for direct send.
  name: Bluecore Direct send API
  slug: bluecore-direct-send-api
- description: The Eligibility API from Bluecore — 2 operation(s) for eligibility.
  name: Bluecore Eligibility API
  slug: bluecore-eligibility-api
- description: The Profile API from Bluecore — 1 operation(s) for profile.
  name: Bluecore Profile API
  slug: bluecore-profile-api
- description: The Transactional API from Bluecore — 1 operation(s) for transactional.
  name: Bluecore Transactional API
  slug: bluecore-transactional-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Authenticate, upsert a Customer Profile, opt them into marketing, send a transactional message with an idempotency key, and read its delivery status.
  name: Onboard a Bluecore customer and send a transactional message
  slug: bluecore-onboard-and-message.arazzo
artifact_total: 16
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.bluecore.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.bluecore.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.bluecore.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.bluecore.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/bluecore-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bluecore-scopes.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/bluecore-conventions.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bluecore-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bluecore-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bluecore-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bluecore-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bluecore-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bluecore-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://bluecore.statuspage.io/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bluecore-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bluecore-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/bluecore-onboard-and-message.arazzo.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bluecore-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bluecore-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bluecore-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bluecore-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bluecore-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/bluecore-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.bluecore.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.bluecore.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.bluecore.com/
- group: operate
  title: ''
  type: Support
  url: mailto:support@bluecore.com
- group: company
  title: ''
  type: Blog
  url: https://www.bluecore.com/blog/
- group: start
  title: ''
  type: Login
  url: https://app.bluecore.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bluecore.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bluecore.com/privacy-policy/
- group: company
  title: ''
  type: Website
  url: https://bluecore.com
created: '2026-07-17'
description: Bluecore is a retail marketing technology platform that unifies shopper identity, behavior, and product data into a customer data platform with 20+ predictive AI models, cross-channel experience orchestration (email, SMS, site, paid media), and AI shopping and marketing agents. Its public developer API (developers.bluecore.com) exposes OAuth 2.0 client-credentials authentication, Customer Profile management, eligibility (consent) management, and Communicate surfaces for transactional and direct-send messaging. Customers include Wayfair, Gap, J.Crew, Lenovo, CVS, and Fender. Backed by Norwest Venture Partners and Techstars.
image: https://www.bluecore.com/wp-content/themes/bluecore/assets/img/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: bluecore-mcp.yml
  slug: bluecore-mcpyml
modified: '2026-07-18'
name: Bluecore
nav: Providers
network: true
overview: 'Bluecore publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authn API, CampaignsAPIPublic API, Direct send API, and 3 more. Tagged areas include Company, Retail, Marketing, Customer Data Platform, and Personalization.


  Bluecore''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, engineering blog, and 26 more developer resources.'
random_paper: 49
rate_limits:
- limit_count: 0
  name: Bluecore Rate Limits
  slug: bluecore-rate-limits
scopes:
- name: Bluecore Scopes
  scope_count: 7
  slug: bluecore-scopes
  summary_line: 7 scopes
score:
  band: developing
  composite: 55.2
  delta: 2.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 58.5
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 42.1
  previous_composite: 53.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 73.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bluecore/refs/heads/main/screenshots/bluecore-2026-07-25T203448.png
security:
- kind: authentication
  name: Bluecore Authentication
  slug: bluecore-authentication
  summary_line: oauth2/http-bearer · 1 scheme
- kind: domain-security
  name: Bluecore Domain Security
  slug: bluecore-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bluecore Vulnerability Disclosure
  slug: bluecore-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Bluecore Trust Center
  slug: bluecore-trust-center
  summary_line: SOC 2, GDPR, CCPA, EU AI Act
slug: bluecore
tags:
- Company
- Retail
- Marketing
- Customer Data Platform
- Personalization
- Email
- SMS
- Messaging
- eCommerce
- Consent
website: https://bluecore.com
---
