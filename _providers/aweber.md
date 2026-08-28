---
access_model:
  confidence: high
  label: Self-serve signup, free developer account, paid customer account
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - https://www.aweber.com/pricing.htm
  - https://labs.aweber.com
  - authentication
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.2
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: Aweber Agentic Access
  operation_count: 57
  slug: aweber-agentic-access
  summary_line: 57 operations · 19 acting · 1 human-in-the-loop
api_count: 12
apis:
- description: The Accounts API from AWeber — 2 operations for listing the accounts an access token can reach and reading a single account, the root of the AWeber resource hierarchy.
  name: AWeber Accounts API
  slug: aweber-accounts-api
- description: The Broadcasts API from AWeber — 10 operations for creating, updating, scheduling, cancelling and deleting broadcast emails on a list, plus reading opens and clicks.
  name: AWeber Broadcasts API
  slug: aweber-broadcasts-api
- description: The Campaigns API from AWeber — 5 operations for reading follow-up and broadcast campaigns on a list and their aggregate statistics.
  name: AWeber Campaigns API
  slug: aweber-campaigns-api
- description: The Custom Fields API from AWeber — 5 operations for creating, reading, renaming and deleting the custom subscriber fields defined on a list.
  name: AWeber Custom Fields API
  slug: aweber-custom-fields-api
- description: The Landing Pages API from AWeber — 2 operations for reading the landing pages attached to a list.
  name: AWeber Landing Pages API
  slug: aweber-landing-pages-api
- description: The Lists API from AWeber — 4 operations for listing and finding the email lists on an account and reading the tags applied on a list.
  name: AWeber Lists API
  slug: aweber-lists-api
- description: The Segments API from AWeber — 2 operations for reading the saved segments defined on a list.
  name: AWeber Segments API
  slug: aweber-segments-api
- description: The Subscribers API from AWeber — 12 operations for adding, reading, updating, moving, searching and deleting subscribers on a list, reading subscriber activity, and recording tracked purchases.
  name: AWeber Subscribers API
  slug: aweber-subscribers-api
- description: The Web Forms API from AWeber — 8 operations for reading the sign-up forms on a list or account and their split tests and split-test components.
  name: AWeber Web Forms API
  slug: aweber-web-forms-api
- description: 'The Integrations API from AWeber — 2 operations for reading the third-party integrations (PayPal, Shopify, WordPress, Facebook and the rest of the 750+ app catalog) connected to an AWeber account and '
  name: AWeber Integrations API
  slug: aweber-integrations-api
- description: The Authentication API from AWeber — 4 operations covering the OAuth 2.0 token and revoke endpoints on auth.aweber.com plus the legacy OAuth 1.0a request-token and access-token endpoints that remain p
  name: AWeber Authentication API
  slug: aweber-authentication-api
- description: 'The Beta API from AWeber — early-access endpoints served at https://api.aweber.com/2.0-beta/, announced in API 1.4.0 on 2025-09-05 as a preview of the upcoming v2 API, primarily replacing numeric ids '
  name: AWeber Beta API
  slug: aweber-beta-api
artifact_total: 36
asyncapis:
- description: ''
  name: Aweber Webhooks
  slug: aweber-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AWeber Accounts API
  slug: open-aweber-accounts-api
- collection_type: open
  name: AWeber Authentication API
  slug: open-aweber-authentication-api
- collection_type: open
  name: AWeber Beta API
  slug: open-aweber-beta-api
- collection_type: open
  name: AWeber Broadcasts API
  slug: open-aweber-broadcasts-api
- collection_type: open
  name: AWeber Campaigns API
  slug: open-aweber-campaigns-api
- collection_type: open
  name: AWeber Custom Fields API
  slug: open-aweber-custom-fields-api
- collection_type: open
  name: AWeber Integrations API
  slug: open-aweber-integrations-api
- collection_type: open
  name: AWeber Landing Pages API
  slug: open-aweber-landing-pages-api
- collection_type: open
  name: AWeber Lists API
  slug: open-aweber-lists-api
- collection_type: open
  name: AWeber Segments API
  slug: open-aweber-segments-api
- collection_type: open
  name: AWeber Subscribers API
  slug: open-aweber-subscribers-api
- collection_type: open
  name: AWeber Web Forms API
  slug: open-aweber-web-forms-api
- collection_type: open
  name: AWeber REST API
  slug: open-aweber
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aweber-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/aweber-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aweber-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aweber-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/aweber-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.aweber.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.aweber.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://labs.aweber.com
- group: start
  title: ''
  type: SignUp
  url: https://www.aweber.com/signup.htm
- group: start
  title: ''
  type: Login
  url: https://www.aweber.com/login.htm
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aweber.com/pricing.htm
- group: operate
  title: ''
  type: Support
  url: https://help.aweber.com
- group: company
  title: ''
  type: Blog
  url: https://blog.aweber.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aweber.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aweber.com/service-agreement.htm
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aweber.com/privacy.htm
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aweber
- group: build
  title: ''
  type: Python SDK
  url: https://github.com/aweber/AWeber-API-Python-Library
- group: build
  title: ''
  type: PHP SDK
  url: https://github.com/aweber/AWeber-API-PHP-Library
- group: build
  title: ''
  type: Ruby SDK
  url: https://github.com/aweber/AWeber-API-Ruby-Library
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/aweber-api
- group: company
  title: ''
  type: X (Twitter)
  url: https://x.com/aweber
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/AWeber
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aweber
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AWeber
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aweber-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/aweber-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/aweber-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aweber-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/aweber-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/aweber-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.aweber.com/dpst.htm
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aweber-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aweber-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aweber-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/aweber-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aweber-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/aweber-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aweber-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aweber-rate-limits.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aweber-vulnerability-disclosure.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://labs.aweber.com/docs/tos
- group: commercial
  title: ''
  type: Legal
  url: https://www.aweber.com/legal.htm
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://www.aweber.com/antispam.htm
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.aweber.com/api
- group: operate
  title: ''
  type: Community
  url: https://community.aweber.com/
- group: company
  title: ''
  type: Newsletter
  url: https://archive.aweber.com/awlabs
- group: build
  title: ''
  type: Examples
  url: https://github.com/aweber/public-api-examples
created: '2026-05-11'
description: AWeber is an email marketing and automation platform for small businesses, creators, and entrepreneurs providing email broadcasts, drip campaigns, landing pages, sign-up forms, and subscriber management. The AWeber REST API at api.aweber.com offers full programmatic access to lists, subscribers, broadcasts, campaigns, custom fields, segments, and tags using OAuth 2.0 authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aweber.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server (candidate — no server is published)
  slug: mcp-server-candidate-no-server-is-published
modified: '2026-08-13'
name: AWeber
nav: Providers
network: true
overview: 'AWeber publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Broadcasts API, Campaigns API, and 9 more. Tagged areas include Email Marketing, Marketing Automation, Email, Newsletters, and Subscribers.


  The AWeber catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AWeber''s developer surface includes authentication, documentation, signup flow, pricing, support, engineering blog, YouTube channel, and 42 more developer resources.'
plans:
- name: Aweber Plans Pricing
  plan_count: 3
  slug: aweber-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Aweber Rate Limits
  slug: aweber-rate-limits
scopes:
- name: Aweber Scopes
  scope_count: 9
  slug: aweber-scopes
  summary_line: 9 scopes · authorizationCode
score:
  band: exemplar
  composite: 77.3
  delta: 3.8
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 30.3
    contract_quality: 68.7
    developer_ergonomics: 75.6
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 63.2
  previous_composite: 73.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 73.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aweber/refs/heads/main/screenshots/aweber-2026-06-20T172736.png
security:
- kind: authentication
  name: Aweber Authentication
  slug: aweber-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Aweber Domain Security
  slug: aweber-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Aweber Vulnerability Disclosure
  slug: aweber-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Aweber Trust Center
  slug: aweber-trust-center
  summary_line: PCI Security certification, Privacy Shield certification, GDPR
slug: aweber
tags:
- Email Marketing
- Marketing Automation
- Email
- Newsletters
- Subscribers
- Campaigns
- Landing Pages
- Web Forms
- Segments
- Webhook
- Authentication
- Small Business
website: https://www.aweber.com
---
