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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 57
  human_in_the_loop: 6
  name: Ory Agentic Access
  operation_count: 128
  slug: ory-agentic-access
  summary_line: 128 operations · 57 acting · 6 human-in-the-loop
api_count: 11
apis:
- description: The api API from Ory — 4 operation(s) for api.
  name: Ory api API
  slug: ory-api-api
- description: APIs for managing email and SMS message delivery.
  name: Ory courier API
  slug: ory-courier-api
- description: Endpoints used by frontend applications (e.g. Single-Page-App, Native Apps, Server Apps, ...) to manage a user's own profile.
  name: Ory frontend API
  slug: ory-frontend-api
- description: APIs for managing identities.
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
- description: The relationship API from Ory — 4 operation(s) for relationship.
  name: Ory relationship API
  slug: ory-relationship-api
- description: Well-Known Endpoints
  name: Ory wellknown API
  slug: ory-wellknown-api
artifact_total: 25
collections:
- collection_type: open
  name: Ory Hydra API
  slug: open-ory-hydra
- collection_type: open
  name: Ory Keto API
  slug: open-ory-keto
- collection_type: open
  name: Ory Identities API
  slug: open-ory-kratos
- collection_type: open
  name: Ory Oathkeeper API
  slug: open-ory-oathkeeper
common:
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
  url: https://www.ory.sh
- group: docs
  title: ''
  type: Documentation
  url: https://www.ory.sh/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ory
- group: company
  title: ''
  type: Blog
  url: https://www.ory.sh/blog/
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
overview: 'Ory publishes 11 APIs on the [APIs.io](https://apis.io/) network, including api API, courier API, frontend API, and 8 more. Tagged areas include Authentication, Authorization, Identity, OAuth2, and OpenID Connect.


  Ory''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Ory Plans Pricing
  plan_count: 4
  slug: ory-plans-pricing
random_paper: 22
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
  band: thin
  composite: 38.0
  delta: -3.6
  facets:
    commercial_clarity: 47.4
    contract_quality: 44.6
    developer_ergonomics: 30.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.6
  scored_at: '2026-07-28'
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
- OAuth2
- OpenID Connect
- Open Source
website: https://www.ory.sh
---
