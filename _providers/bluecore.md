---
access_model:
  confidence: high
  label: Contact sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.bluecore.com/request-a-demo/
  - plans/bluecore-plans-pricing.yml
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 54.9
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Bluecore Agentic Access
  operation_count: 9
  slug: bluecore-agentic-access
  summary_line: 9 operations · 6 acting
api_count: 8
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
- description: The original Bluecore Transactional API on https://api.bluecore.com/email/ - send a transactional or real-time welcome email against a Bluecore campaign, and retrieve the delivery status of a previous
  name: Bluecore Transactional API (legacy)
  slug: bluecore-transactional-legacy-api
- description: Bluecore's event-ingestion API - POST shopper behaviour and identity events (viewed_product, search, add_to_cart, remove_from_cart, wishlist, purchase, customer_patch, identify, optin, unsubscribe, pl
  name: Bluecore Events API
  slug: bluecore-events-api
arazzos:
- description: Authenticate, upsert a Customer Profile, opt them into marketing, send a transactional message with an idempotency key, and read its delivery status.
  name: Onboard a Bluecore customer and send a transactional message
  slug: bluecore-onboard-and-message.arazzo
artifact_total: 26
asyncapis:
- description: ''
  name: Bluecore Events
  slug: bluecore-events
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bluecore Authn API
  slug: open-bluecore-authn-api
- collection_type: open
  name: Bluecore Authn CampaignsAPIPublic API
  slug: open-bluecore-campaignsapipublic-api
- collection_type: open
  name: Bluecore Authn Direct send API
  slug: open-bluecore-direct-send-api
- collection_type: open
  name: Bluecore Authn Eligibility API
  slug: open-bluecore-eligibility-api
- collection_type: open
  name: Bluecore Authn Profile API
  slug: open-bluecore-profile-api
- collection_type: open
  name: Bluecore Authn Transactional API
  slug: open-bluecore-transactional-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/bluecore-transactional-legacy-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bluecore-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/bluecore-openid-configuration.json
- group: build
  title: ''
  type: Packages
  url: packages/bluecore-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bluecore-plans-pricing.yml
- group: design
  title: ''
  type: Components
  url: components/bluecore-components.yml
- group: other
  title: ''
  type: EventCatalog
  url: asyncapi/bluecore-events.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TriggerMail
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bluecore-llms.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/bluecore-trust-center.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/bluecore-openapi-overlay.yaml
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
  type: AgenticAccess
  url: agentic-access/bluecore-agentic-access.yml
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
  name: Bluecore MCP Server
  slug: bluecore-mcp-server
modified: '2026-08-13'
name: Bluecore
nav: Providers
network: true
overview: 'Bluecore publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Authn API, CampaignsAPIPublic API, Direct send API, and 4 more. Tagged areas include Company, Retail, Marketing, Customer Data Platform, and Personalization.


  The Bluecore catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bluecore''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, engineering blog, and 35 more developer resources.'
plans:
- name: Bluecore Plans Pricing
  plan_count: 0
  slug: bluecore-plans-pricing
random_paper: 9
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
  band: strong
  composite: 55.3
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 16.7
    contract_quality: 64.3
    developer_ergonomics: 44.6
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 28.9
  previous_composite: 55.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 14.3
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 73.6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bluecore/refs/heads/main/screenshots/bluecore-2026-07-25T203448.png
security:
- kind: authentication
  name: Bluecore Authentication
  slug: bluecore-authentication
  summary_line: oauth2/http-bearer · 3 schemes
- kind: domain-security
  name: Bluecore Domain Security
  slug: bluecore-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
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
- E-Commerce
- Consent
website: https://bluecore.com
---
