---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: 'The TELUS Insights Location API exposes de-identified, aggregated geo-intelligence derived from the TELUS mobile network across Canada. Consumers submit asynchronous count jobs — demographic, origin, '
  name: TELUS Insights Location API
  slug: telus-insights-location-api
- description: The TELUS Health Collaborative Health Record (CHR) Enterprise API is a GraphQL interface onto the CHR ambulatory-care platform used by Canadian clinics and allied health professionals. Its published i
  name: TELUS Health CHR Enterprise API
  slug: telus-health-chr-enterprise-api
artifact_total: 8
asyncapis:
- description: ''
  name: Telus Chr Event Notifications
  slug: telus-chr-event-notifications
common:
- group: company
  title: ''
  type: Website
  url: https://www.telus.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.insights.telus.com/
- group: docs
  title: ''
  type: APIReference
  url: https://help.inputhealth.com/en/articles/5941595-api-reference-documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://help.inputhealth.com/en/articles/6368814-enterprise-api-onboarding-overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.telus.com/
- group: operate
  title: ''
  type: Support
  url: https://support.api.telus.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/telus
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/telus
- group: company
  title: ''
  type: Blog
  url: https://www.telus.com/en/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.telus.com/en/about/privacy/commitment
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.telus.com/en/about/policies-and-disclosures/user-terms
- group: auth
  title: ''
  type: Security
  url: https://www.telus.com/en/about/security/report-a-problem
- group: build
  title: ''
  type: Postman
  url: https://docs.insights.telus.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/telus-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/telus-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/telus-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/telus-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/telus-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/telus-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/telus-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/telus-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/telus-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/telus-packages.yml
- group: design
  title: ''
  type: Components
  url: components/telus-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/telus-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/telus-chr-event-notifications.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/telus-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/telus-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/telus-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/telus-vulnerability-disclosure.yml
created: '2026-07-25'
description: 'TELUS Corporation is one of Canada''s three national facilities-based telecommunications carriers, operating a nationwide mobile network alongside broadband, TV, security, health (TELUS Health) and agriculture (TELUS Agriculture & Consumer Goods) businesses from its Vancouver headquarters. In the API value chain TELUS is a network owner rather than a developer-facing platform: its API Marketplace at api.telus.com sits behind the TELUS Client Identity login, its developers.telus.com "Simplify" portal is an internal/partner surface that refuses anonymous requests, and its IoT Marketplace is a login wall. Two TELUS APIs are nonetheless documented in the open, and neither is on a telus.com property. The TELUS Insights Location API publishes a 27-operation reference through Postman Documenter and runs a live OAuth2-protected gateway. The TELUS Health Collaborative Health Record (CHR) Enterprise API is a substantial GraphQL platform — 505 types, 64 queries, 49 mutations and a 21-topic
  signed webhook service — whose full introspection document is anonymously fetchable from apidocs.ca.inputhealth.com, making it the only machine-readable API contract TELUS publishes anywhere. Both are gated commercially: Insights credentials come from a sales-led ticket in the Insights Portal, and CHR Enterprise API access is a paid feature enabled per clinic account after a contract and a privacy questionnaire. TELUS is a named participant in the CAMARA project and appears in the CAMARA landscape as an operator, but it publishes no first-party CAMARA endpoint — its Number Verification and SIM Swap network APIs reach developers indirectly through EnStream LP, the Bell/Rogers/TELUS identity joint venture, which feeds Aduna and from there CPaaS channels such as Vonage. TELUS is partner-gated and, for network APIs, reachable only through aggregators.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: TELUS
nav: Providers
network: true
overview: 'TELUS publishes 1 API on the [APIs.io](https://apis.io/) network: Insights Location API. Tagged areas include Telecommunications, Canada, Mobile Network Operator, Broadband, and Network APIs.


  The TELUS catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  TELUS''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 24 more developer resources.'
random_paper: 11
rate_limits:
- limit_count: 4
  name: Telus Rate Limits
  slug: telus-rate-limits
scopes:
- name: Telus Scopes
  scope_count: 0
  slug: telus-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 54.3
  coverage:
    artifact_dirs: 20
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 53.1
    developer_ergonomics: 68.5
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 68.4
  previous_composite: 54.6
  provenance:
    conformance: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 75.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Telus Authentication
  slug: telus-authentication
  summary_line: oauth2/http · 4 schemes
- kind: domain-security
  name: Telus Domain Security
  slug: telus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Telus Vulnerability Disclosure
  slug: telus-vulnerability-disclosure
  summary_line: Hackerone · security.txt
slug: telus
tags:
- Telecommunications
- Canada
- Mobile Network Operator
- Broadband
- Network APIs
- CAMARA
- Open Gateway
- SIM Swap
- Identity Verification
- Location Intelligence
- IoT
- 5G
- Healthcare
- Electronic Medical Records
- GraphQL
- Webhook
- Geospatial
website: https://www.telus.com/
---
