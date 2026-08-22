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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 51
  human_in_the_loop: 5
  name: Ory Corp Agentic Access
  operation_count: 90
  slug: ory-corp-agentic-access
  summary_line: 90 operations · 51 acting · 5 human-in-the-loop
api_count: 12
apis:
- description: Ory Network workspace / project subscriptions.
  name: Ory Billing API
  slug: ory-corp-billing-api
- description: Admin access to queued and dispatched courier messages.
  name: Ory Courier API
  slug: ory-corp-courier-api
- description: Ory Network event stream configuration.
  name: Ory Event Streams API
  slug: ory-corp-event-streams-api
- description: Privileged Kratos identity and session management.
  name: Ory Identity (Admin) API
  slug: ory-corp-identity-admin-api
- description: Public Kratos flows for login, registration, recovery, verification, settings, logout, and sessions.
  name: Ory Identity (Self-Service) API
  slug: ory-corp-identity-self-service-api
- description: Privileged Hydra client, token, consent, and key management.
  name: Ory OAuth2 (Admin) API
  slug: ory-corp-oauth2-admin-api
- description: Public OAuth2 / OpenID Connect provider endpoints (Hydra).
  name: Ory OAuth2 (Public) API
  slug: ory-corp-oauth2-public-api
- description: B2B organization management for SSO.
  name: Ory Organizations API
  slug: ory-corp-organizations-api
- description: Keto permission checks, expand, and namespace reads.
  name: Ory Permissions API
  slug: ory-corp-permissions-api
- description: Ory Network project API token management.
  name: Ory Project Tokens API
  slug: ory-corp-project-tokens-api
- description: Ory Network Console project management.
  name: Ory Projects API
  slug: ory-corp-projects-api
- description: Keto relationship-tuple writes and OPL syntax checks.
  name: Ory Relationships API
  slug: ory-corp-relationships-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ory Network Billing API
  slug: open-ory-corp-billing-api
- collection_type: open
  name: Ory Network Billing Courier API
  slug: open-ory-corp-courier-api
- collection_type: open
  name: Ory Network Billing Event Streams API
  slug: open-ory-corp-event-streams-api
- collection_type: open
  name: Ory Network Billing Identity (Admin) API
  slug: open-ory-corp-identity-admin-api
- collection_type: open
  name: Ory Network Billing Identity (Self-Service) API
  slug: open-ory-corp-identity-self-service-api
- collection_type: open
  name: Ory Network Billing OAuth2 (Admin) API
  slug: open-ory-corp-oauth2-admin-api
- collection_type: open
  name: Ory Network Billing OAuth2 (Public) API
  slug: open-ory-corp-oauth2-public-api
- collection_type: open
  name: Ory Network Billing Organizations API
  slug: open-ory-corp-organizations-api
- collection_type: open
  name: Ory Network Billing Permissions API
  slug: open-ory-corp-permissions-api
- collection_type: open
  name: Ory Network Billing Project Tokens API
  slug: open-ory-corp-project-tokens-api
- collection_type: open
  name: Ory Network Billing Projects API
  slug: open-ory-corp-projects-api
- collection_type: open
  name: Ory Network Billing Relationships API
  slug: open-ory-corp-relationships-api
- collection_type: open
  name: Ory Network API
  slug: open-ory-corp
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ory-corp-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/ory-corp-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ory-corp-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ory-corp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ory-corp-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ory
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ory
- group: company
  title: ''
  type: Website
  url: https://www.ory.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.ory.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/ory-corp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ory-corp-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ory-corp-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.ory.com/blog
created: '2026-07-02'
description: Ory builds open-source identity and access infrastructure and runs it as the Ory Network managed cloud. The stack is composed of Ory Kratos (identities, sessions, and self-service login/registration/recovery/verification/settings flows), Ory Hydra (OAuth2 and OpenID Connect - clients, tokens, consent, and introspection), Ory Keto (Google Zanzibar-style permissions and relationship tuples), and Ory Oathkeeper (zero-trust access proxy). On the Ory Network, all services are exposed on a single project-scoped base URL (https://{project-slug}.projects.oryapis.com) with admin and public surfaces, while workspaces, projects, organizations (B2B SSO), event streams, and billing are managed through the Ory Network Console API (https://api.console.ory.sh).
finops:
- name: Ory Corp Finops
  service_category: Identity and Access Management
  slug: ory-corp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ory-corp.png
layout: provider
modified: '2026-07-02'
name: Ory
nav: Providers
network: true
overview: 'Ory publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Billing API, Courier API, Event Streams API, and 9 more. Tagged areas include Identity, Authentication, OAuth2, OpenID Connect, and Authorization.


  Ory''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Ory Corp Plans Pricing
  plan_count: 5
  slug: ory-corp-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 4
  name: Ory Corp Rate Limits
  slug: ory-corp-rate-limits
score:
  band: thin
  composite: 39.2
  delta: -0.2
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 52.4
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ory-corp/refs/heads/main/screenshots/ory-corp-2026-08-07T190959.png
security:
- kind: authentication
  name: Ory Corp Authentication
  slug: ory-corp-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ory Corp Domain Security
  slug: ory-corp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ory Corp Vulnerability Disclosure
  slug: ory-corp-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Ory Corp Trust Center
  slug: ory-corp-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: ory-corp
tags:
- Identity
- Authentication
- OAuth2
- OpenID Connect
- Authorization
- Permissions
- IAM
- Open Source
website: https://www.ory.com
---
