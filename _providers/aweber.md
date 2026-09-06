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
  band_gated_from: agent-native
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.7
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: Aweber Agentic Access
  operation_count: 57
  slug: aweber-agentic-access
  summary_line: 57 operations · 19 acting · 1 human-in-the-loop
api_count: 4
apis:
- baseURL: https://api.aweber.com/1.0
  baseurl_source: declared
  description: The Accounts API from AWeber — 2 operations for listing the accounts an access token can reach and reading a single account, the root of the AWeber resource hierarchy.
  name: AWeber Accounts API
  slug: aweber-accounts-api
- baseURL: https://api.aweber.com/1.0
  baseurl_source: declared
  description: The Broadcasts API from AWeber — 10 operations for creating, updating, scheduling, cancelling and deleting broadcast emails on a list, plus reading opens and clicks.
  name: AWeber Broadcasts API
  slug: aweber-broadcasts-api
- baseURL: https://api.aweber.com/1.0
  baseurl_source: declared
  description: The Campaigns API from AWeber — 5 operations for reading follow-up and broadcast campaigns on a list and their aggregate statistics.
  name: AWeber Campaigns API
  slug: aweber-campaigns-api
- baseURL: https://api.aweber.com/1.0
  baseurl_source: declared
  description: The Custom Fields API from AWeber — 5 operations for creating, reading, renaming and deleting the custom subscriber fields defined on a list.
  name: AWeber Custom Fields API
  slug: aweber-custom-fields-api
- baseURL: https://api.aweber.com/1.0
  baseurl_source: declared
  description: The Landing Pages API from AWeber — 2 operations for reading the landing pages attached to a list.
  name: AWeber Landing Pages API
  slug: aweber-landing-pages-api
- baseURL: https://api.aweber.com/1.0
  baseurl_source: declared
  description: The Lists API from AWeber — 4 operations for listing and finding the email lists on an account and reading the tags applied on a list.
  name: AWeber Lists API
  slug: aweber-lists-api
- baseURL: https://api.aweber.com/1.0
  baseurl_source: declared
  description: The Segments API from AWeber — 2 operations for reading the saved segments defined on a list.
  name: AWeber Segments API
  slug: aweber-segments-api
- baseURL: https://api.aweber.com/1.0
  baseurl_source: declared
  description: The Subscribers API from AWeber — 12 operations for adding, reading, updating, moving, searching and deleting subscribers on a list, reading subscriber activity, and recording tracked purchases.
  name: AWeber Subscribers API
  slug: aweber-subscribers-api
- baseURL: https://api.aweber.com/1.0
  baseurl_source: declared
  description: 'The Integrations API from AWeber — 2 operations for reading the third-party integrations (PayPal, Shopify, WordPress, Facebook and the rest of the 750+ app catalog) connected to an AWeber account and '
  name: AWeber Integrations API
  slug: aweber-integrations-api
- baseURL: https://api.aweber.com/1.0
  baseurl_source: declared
  description: '### What is it? Beta endpoints are early-access versions of the upcoming v2 API that provide developers with a preview of new features and changes before the official v2 release. These endpoints are a'
  name: AWeber Beta Endpoints API
  slug: aweber-beta-endpoints-api
- baseURL: https://api.aweber.com/1.0
  baseurl_source: declared
  description: The OAuth 1.0a Reference API from AWeber — 2 operation(s) for oauth 1.0a reference.
  name: AWeber OAuth 1.0a Reference API
  slug: aweber-oauth-1-0a-reference-api
- baseURL: https://api.aweber.com/1.0
  baseurl_source: declared
  description: These endpoints are used to authenticate with the api. The AWeber API uses the OAuth 2.0 model to handle authentication. OAuth is a standardized way for services to grant permission on a user's behalf
  name: AWeber OAuth 2.0 Reference API
  slug: aweber-oauth-2-0-reference-api
- baseURL: https://api.aweber.com/1.0
  baseurl_source: declared
  description: '### What is it? Represents the collection of sign-up forms associated with the AWeber Customer Account''s lists. Webforms are sets of customized HTML and javascript that are used to put up a sign-up fo'
  name: AWeber Webforms API
  slug: aweber-webforms-api
artifact_total: 37
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
overview: 'AWeber publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Broadcasts API, Campaigns API, and 10 more. Tagged areas include Email Marketing, Marketing Automation, Email, Newsletters, and Subscribers.


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
  composite: 72.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 67.7
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 55.3
  previous_composite: 72.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 73.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
