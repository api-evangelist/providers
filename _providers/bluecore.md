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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 54.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Bluecore Agentic Access
  operation_count: 9
  slug: bluecore-agentic-access
  summary_line: 9 operations · 6 acting
api_count: 3
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
- description: Bluecore's event-ingestion API - POST shopper behaviour and identity events (viewed_product, search, add_to_cart, remove_from_cart, wishlist, purchase, customer_patch, identify, optin, unsubscribe, pl
  name: Bluecore Events API
  slug: bluecore-events-api
- description: The GET STATUS API from Bluecore — 1 operation(s) for get status.
  name: Bluecore GET STATUS API
  slug: bluecore-get-status-api
- description: The SEND EMAIL API from Bluecore — 1 operation(s) for send email.
  name: Bluecore SEND EMAIL API
  slug: bluecore-send-email-api
arazzos:
- description: Authenticate, upsert a Customer Profile, opt them into marketing, send a transactional message with an idempotency key, and read its delivery status.
  name: Onboard a Bluecore customer and send a transactional message
  slug: bluecore-onboard-and-message.arazzo
artifact_total: 27
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
  type: CapabilityMap
  url: capabilities/bluecore-capability-edges.yml
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
overview: 'Bluecore publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authn API, CampaignsAPIPublic API, Direct send API, and 5 more. Tagged areas include Company, Retail, Marketing, Customer Data Platform, and Personalization.


  The Bluecore catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bluecore''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, engineering blog, and 36 more developer resources.'
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
  band: developing
  composite: 51.8
  coverage:
    artifact_dirs: 25
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 4.5
    contract_quality: 60.5
    developer_ergonomics: 44.6
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 28.9
  previous_composite: 52.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 73.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
