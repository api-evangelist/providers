---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - '{''url'': ''https://jebbit.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.blueconic.com/experiences-by-jebbit — a different registrable domain (jebbit.com -> blueconic.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.8
  scored_at: '2026-09-15'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Jebbit Agentic Access
  operation_count: 37
  slug: jebbit-agentic-access
  summary_line: 37 operations · 19 acting
api_count: 1
apis:
- baseURL: https://api2.jebbit.com
  baseurl_source: declared
  description: The Auth API from Jebbit — 1 operation(s) for auth.
  name: Jebbit Auth API
  slug: jebbit-auth-api
- baseURL: https://api2.jebbit.com
  baseurl_source: declared
  description: The Businesses API from Jebbit — 1 operation(s) for businesses.
  name: Jebbit Businesses API
  slug: jebbit-businesses-api
- baseURL: https://api2.jebbit.com
  baseurl_source: declared
  description: The Campaigns API from Jebbit — 2 operation(s) for campaigns.
  name: Jebbit Campaigns API
  slug: jebbit-campaigns-api
- baseURL: https://api2.jebbit.com
  baseurl_source: declared
  description: The Feed Columns API from Jebbit — 2 operation(s) for feed columns.
  name: Jebbit Feed Columns API
  slug: jebbit-feed-columns-api
- baseURL: https://api2.jebbit.com
  baseurl_source: declared
  description: The Feed Rows API from Jebbit — 2 operation(s) for feed rows.
  name: Jebbit Feed Rows API
  slug: jebbit-feed-rows-api
- baseURL: https://api2.jebbit.com
  baseurl_source: declared
  description: The Feeds API from Jebbit — 4 operation(s) for feeds.
  name: Jebbit Feeds API
  slug: jebbit-feeds-api
- baseURL: https://api2.jebbit.com
  baseurl_source: declared
  description: The Integration Historic Backfills API from Jebbit — 2 operation(s) for integration historic backfills.
  name: Jebbit Integration Historic Backfills API
  slug: jebbit-integration-historic-backfills-api
- baseURL: https://api2.jebbit.com
  baseurl_source: declared
  description: The Integration Mappings API from Jebbit — 2 operation(s) for integration mappings.
  name: Jebbit Integration Mappings API
  slug: jebbit-integration-mappings-api
- baseURL: https://api2.jebbit.com
  baseurl_source: declared
  description: The Integrations API from Jebbit — 3 operation(s) for integrations.
  name: Jebbit Integrations API
  slug: jebbit-integrations-api
- baseURL: https://api2.jebbit.com
  baseurl_source: declared
  description: The Launch Links API from Jebbit — 1 operation(s) for launch links.
  name: Jebbit Launch Links API
  slug: jebbit-launch-links-api
artifact_total: 30
asyncapis:
- description: ''
  name: Jebbit Webhooks
  slug: jebbit-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Jebbit Auth API
  slug: open-jebbit-auth-api
- collection_type: open
  name: Jebbit Auth Businesses API
  slug: open-jebbit-businesses-api
- collection_type: open
  name: Jebbit Auth Campaigns API
  slug: open-jebbit-campaigns-api
- collection_type: open
  name: Jebbit Auth Feed Columns API
  slug: open-jebbit-feed-columns-api
- collection_type: open
  name: Jebbit Auth Feed Rows API
  slug: open-jebbit-feed-rows-api
- collection_type: open
  name: Jebbit Auth Feeds API
  slug: open-jebbit-feeds-api
- collection_type: open
  name: Jebbit Auth Integration Historic Backfills API
  slug: open-jebbit-integration-historic-backfills-api
- collection_type: open
  name: Jebbit Auth Integration Mappings API
  slug: open-jebbit-integration-mappings-api
- collection_type: open
  name: Jebbit Auth Integrations API
  slug: open-jebbit-integrations-api
- collection_type: open
  name: Jebbit Auth Launch Links API
  slug: open-jebbit-launch-links-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/jebbit/refs/heads/main/overlays/jebbit-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/jebbit-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://jebbit.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.jebbit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.jebbit.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.jebbit.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://support-experiences.blueconic.com/en/articles/246971-api-overview
- group: operate
  title: ''
  type: Support
  url: https://support-experiences.blueconic.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support-experiences.blueconic.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.blueconic.com/category/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jebbit
- group: start
  title: ''
  type: Login
  url: https://app.jebbit.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blueconic.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blueconic.com/legal/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/jebbit/refs/heads/main/authentication/jebbit-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jebbit-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/jebbit/refs/heads/main/scopes/jebbit-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/jebbit-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jebbit/refs/heads/main/conventions/jebbit-conventions.yml
  title: ''
  type: Conventions
  url: conventions/jebbit-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jebbit/refs/heads/main/errors/jebbit-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/jebbit-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jebbit/refs/heads/main/asyncapi/jebbit-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/jebbit-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/jebbit/refs/heads/main/mcp/jebbit-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/jebbit-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/jebbit/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/jebbit/refs/heads/main/well-known/jebbit-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/jebbit-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jebbit/refs/heads/main/lifecycle/jebbit-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/jebbit-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jebbit/refs/heads/main/conformance/jebbit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jebbit-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/jebbit/refs/heads/main/security/jebbit-trust-center.yml
  title: ''
  type: Compliance
  url: security/jebbit-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/jebbit/refs/heads/main/security/jebbit-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/jebbit-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/jebbit/refs/heads/main/security/jebbit-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/jebbit-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/jebbit/refs/heads/main/security/jebbit-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/jebbit-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/jebbit/refs/heads/main/security/jebbit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jebbit-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/jebbit/refs/heads/main/agentic-access/jebbit-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/jebbit-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jebbit/refs/heads/main/data-model/jebbit-data-model.yml
  title: ''
  type: DataModel
  url: data-model/jebbit-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jebbit/refs/heads/main/components/jebbit-components.yml
  title: ''
  type: Components
  url: components/jebbit-components.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/jebbit/refs/heads/main/sandbox/jebbit-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/jebbit-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/jebbit/refs/heads/main/llms/jebbit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jebbit-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/jebbit/refs/heads/main/packages/jebbit-packages.yml
  title: ''
  type: Packages
  url: packages/jebbit-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/jebbit/refs/heads/main/mcp/jebbit-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/jebbit-tool-crosswalk.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/jebbit/refs/heads/main/rate-limits/jebbit-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/jebbit-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/jebbit/refs/heads/main/plans/jebbit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/jebbit-plans-pricing.yml
created: '2026-07-17'
description: Jebbit — now BlueConic Experiences — is an interactive experience platform that captures zero- and first-party declared data from consumers through quizzes, product finders, personality tests, and preference flows that shoppers complete because the experience gives them value in return. Responses sync into customer profiles and activate across the marketing stack in real time. Jebbit exposes a public JSON:API REST API (https://api2.jebbit.com) for managing businesses, campaigns, launch links, dynamic product feeds, and webhook integrations that stream user session data, secured with OAuth 2.0 client-credentials JWTs and HMAC-signed webhooks.
image: https://jebbit-public-api-docs.s3.amazonaws.com/images/logo.png
layout: provider
modified: '2026-08-13'
name: Jebbit
nav: Providers
network: true
overview: 'Jebbit publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Businesses API, Campaigns API, and 7 more. Tagged areas include Company, Interactive Experiences, Zero-Party Data, First-Party Data, and Marketing.


  The Jebbit catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Jebbit''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 30 more developer resources.'
plans:
- name: Jebbit Plans Pricing
  plan_count: 0
  slug: jebbit-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Jebbit Rate Limits
  slug: jebbit-rate-limits
scopes:
- name: Jebbit Scopes
  scope_count: 6
  slug: jebbit-scopes
  summary_line: 6 scopes
score:
  band: developing
  composite: 48.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 59.0
    developer_ergonomics: 67.3
    discoverability: 75.9
    operational_transparency: 21.1
  previous_composite: 48.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/jebbit/refs/heads/main/screenshots/jebbit-2026-07-25T223113.png
security:
- kind: authentication
  name: Jebbit Authentication
  slug: jebbit-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Jebbit Domain Security
  slug: jebbit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jebbit Vulnerability Disclosure
  slug: jebbit-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Jebbit Trust Center
  slug: jebbit-trust-center
  summary_line: SOC 2 Type 2, TRUSTe Verified Privacy Seal, TRUSTe Verified International Privacy Seal
slug: jebbit
tags:
- Company
- Interactive Experiences
- Zero-Party Data
- First-Party Data
- Marketing
- Quizzes
- Product Feeds
- Webhook
- Customer Data
- JSON:API
website: https://jebbit.com/
---
