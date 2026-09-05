---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.7
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 57
  human_in_the_loop: 6
  name: Ory Agentic Access
  operation_count: 128
  slug: ory-agentic-access
  summary_line: 128 operations · 57 acting · 6 human-in-the-loop
api_count: 17
apis:
- description: The api API from Ory — 4 operation(s) for api.
  name: Ory api API
  slug: ory-api-api
- baseURL_template: https://{project-slug}.projects.oryapis.com
  baseurl_source: spec_template
  description: APIs for managing email and SMS message delivery.
  name: Ory courier API
  slug: ory-courier-api
- description: Endpoints used by frontend applications (e.g. Single-Page-App, Native Apps, Server Apps, ...) to manage a user's own profile.
  name: Ory frontend API
  slug: ory-frontend-api
- baseURL_template: https://{project-slug}.projects.oryapis.com
  baseurl_source: spec_template
  description: APIs for managing identities.
  name: Ory identity API
  slug: ory-identity-api
- description: JSON Web Keys
  name: Ory jwk API
  slug: ory-jwk-api
- description: Service Metadata
  name: Ory metadata API
  slug: ory-metadata-api
- description: OAuth 2.0
  name: Ory oAuth2 API
  slug: ory-oauth2-api
- description: OpenID Connect
  name: Ory oidc API
  slug: ory-oidc-api
- description: The permission API from Ory — 4 operation(s) for permission.
  name: Ory permission API
  slug: ory-permission-api
- baseURL_template: https://{project-slug}.projects.oryapis.com
  baseurl_source: spec_template
  description: The relationship API from Ory — 4 operation(s) for relationship.
  name: Ory relationship API
  slug: ory-relationship-api
- baseURL_template: https://{project-slug}.projects.oryapis.com
  baseurl_source: spec_template
  description: Well-Known Endpoints
  name: Ory wellknown API
  slug: ory-wellknown-api
- baseURL: https://{project-slug}.projects.oryapis.com
  baseurl_source: declared
  description: Ory Network workspace / project subscriptions.
  name: Ory Billing API
  slug: ory-billing-api
- baseURL: https://{project-slug}.projects.oryapis.com
  baseurl_source: declared
  description: Ory Network event stream configuration.
  name: Ory Event Streams API
  slug: ory-event-streams-api
- baseURL: https://{project-slug}.projects.oryapis.com
  baseurl_source: declared
  description: Privileged Kratos identity and session management.
  name: Ory Identity (Admin) API
  slug: ory-identity-admin-api
- baseURL: https://{project-slug}.projects.oryapis.com
  baseurl_source: declared
  description: Public Kratos flows for login, registration, recovery, verification, settings, logout, and sessions.
  name: Ory Identity (Self-Service) API
  slug: ory-identity-self-service-api
- baseURL: https://{project-slug}.projects.oryapis.com
  baseurl_source: declared
  description: Privileged Hydra client, token, consent, and key management.
  name: Ory OAuth2 (Admin) API
  slug: ory-oauth2-admin-api
- baseURL: https://{project-slug}.projects.oryapis.com
  baseurl_source: declared
  description: Public OAuth2 / OpenID Connect provider endpoints (Hydra).
  name: Ory OAuth2 (Public) API
  slug: ory-oauth2-public-api
- baseURL: https://{project-slug}.projects.oryapis.com
  baseurl_source: declared
  description: B2B organization management for SSO.
  name: Ory Organizations API
  slug: ory-organizations-api
- baseURL: https://{project-slug}.projects.oryapis.com
  baseurl_source: declared
  description: Keto permission checks, expand, and namespace reads.
  name: Ory Permissions API
  slug: ory-permissions-api
- baseURL: https://{project-slug}.projects.oryapis.com
  baseurl_source: declared
  description: Ory Network project API token management.
  name: Ory Project Tokens API
  slug: ory-project-tokens-api
- baseURL: https://{project-slug}.projects.oryapis.com
  baseurl_source: declared
  description: Ory Network Console project management.
  name: Ory Projects API
  slug: ory-projects-api
- baseURL: https://{project-slug}.projects.oryapis.com
  baseurl_source: declared
  description: Keto relationship-tuple writes and OPL syntax checks.
  name: Ory Relationships API
  slug: ory-relationships-api
artifact_total: 61
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ory Hydra api API
  slug: open-ory-api-api
- collection_type: open
  name: Ory Hydra api courier API
  slug: open-ory-courier-api
- collection_type: open
  name: Ory Hydra api frontend API
  slug: open-ory-frontend-api
- collection_type: open
  name: Ory Hydra API
  slug: open-ory-hydra
- collection_type: open
  name: Ory Hydra api identity API
  slug: open-ory-identity-api
- collection_type: open
  name: Ory Hydra api jwk API
  slug: open-ory-jwk-api
- collection_type: open
  name: Ory Keto API
  slug: open-ory-keto
- collection_type: open
  name: Ory Identities API
  slug: open-ory-kratos
- collection_type: open
  name: Ory Hydra api metadata API
  slug: open-ory-metadata-api
- collection_type: open
  name: Ory Network Billing API
  slug: open-ory-network-billing-api
- collection_type: open
  name: Ory Network Billing Courier API
  slug: open-ory-network-courier-api
- collection_type: open
  name: Ory Network Billing Event Streams API
  slug: open-ory-network-event-streams-api
- collection_type: open
  name: Ory Network Billing Identity (Admin) API
  slug: open-ory-network-identity-admin-api
- collection_type: open
  name: Ory Network Billing Identity (Self-Service) API
  slug: open-ory-network-identity-self-service-api
- collection_type: open
  name: Ory Network Billing OAuth2 (Admin) API
  slug: open-ory-network-oauth2-admin-api
- collection_type: open
  name: Ory Network Billing OAuth2 (Public) API
  slug: open-ory-network-oauth2-public-api
- collection_type: open
  name: Ory Network Billing Organizations API
  slug: open-ory-network-organizations-api
- collection_type: open
  name: Ory Network Billing Permissions API
  slug: open-ory-network-permissions-api
- collection_type: open
  name: Ory Network Billing Project Tokens API
  slug: open-ory-network-project-tokens-api
- collection_type: open
  name: Ory Network Billing Projects API
  slug: open-ory-network-projects-api
- collection_type: open
  name: Ory Network Billing Relationships API
  slug: open-ory-network-relationships-api
- collection_type: open
  name: Ory Network API
  slug: open-ory-network
- collection_type: open
  name: Ory Oathkeeper API
  slug: open-ory-oathkeeper
- collection_type: open
  name: Ory Hydra api oAuth2 API
  slug: open-ory-oauth2-api
- collection_type: open
  name: Ory Hydra api oidc API
  slug: open-ory-oidc-api
- collection_type: open
  name: Ory Hydra api permission API
  slug: open-ory-permission-api
- collection_type: open
  name: Ory Hydra api relationship API
  slug: open-ory-relationship-api
- collection_type: open
  name: Ory Hydra api wellknown API
  slug: open-ory-wellknown-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/ory/hydra/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/ory/hydra/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/ory/hydra/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/ory/hydra/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/ory/hydra/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/ory/hydra/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ory-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/ory-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ory-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ory-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ory-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ory-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ory-corp
- group: company
  title: ''
  type: Website
  url: https://www.ory.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.ory.com/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ory
- group: company
  title: ''
  type: Blog
  url: https://www.ory.com/blog/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/ory/mcp
created: '2026-03-25'
description: Ory is an open source identity infrastructure platform providing OAuth2 and OpenID Connect (Hydra), identity and user management (Kratos), permissions and authorization (Keto), and a reverse proxy with policy enforcement (Oathkeeper).
finops:
- name: Ory Finops
  service_category: Identity
  slug: ory-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ory.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Ory
nav: Providers
network: true
overview: 'Ory publishes 22 APIs on the [APIs.io](https://apis.io/) network, including api API, courier API, frontend API, and 19 more. Tagged areas include Authentication, Authorization, Identity, OpenID Connect, and Open-Source.


  Ory''s developer surface includes authentication, documentation, engineering blog, and 15 more developer resources.'
plans:
- name: Ory Plans Pricing
  plan_count: 4
  slug: ory-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 8
  name: Ory Rate Limits
  slug: ory-rate-limits
scopes:
- name: Ory Scopes
  scope_count: 3
  slug: ory-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 41.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.5
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 50.9
    developer_ergonomics: 32.1
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 41.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 68.2
      derived: 0
      marker_coverage: 0.0
      total: 22
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ory/refs/heads/main/screenshots/ory-2026-06-20T191212.png
security:
- kind: authentication
  name: Ory Authentication
  slug: ory-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Ory Domain Security
  slug: ory-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ory Vulnerability Disclosure
  slug: ory-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Ory Trust Center
  slug: ory-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: ory
tags:
- Authentication
- Authorization
- Identity
- OpenID Connect
- Open-Source
website: https://www.ory.com
---
