---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 4
apis:
- description: RESTCONF (RFC 8040) API on the Curity Identity Server admin service for reading and changing the full server configuration; served by each self-hosted deployment.
  name: Curity RESTCONF Admin API
  slug: restconf-admin-api
- description: GraphQL APIs exposed by the Curity Identity Server for user management and dynamic client (DCR) management, protected by OAuth access tokens.
  name: Curity GraphQL APIs
  slug: graphql-apis
- description: SCIM 2.0 user provisioning endpoints served by the Curity Identity Server user management service.
  name: Curity SCIM 2.0 API
  slug: scim-2.0-api
- description: Standard OAuth 2.0 and OpenID Connect endpoints (authorize, token, introspection, userinfo, revocation, dynamic registration, discovery) served by the Curity Identity Server token service.
  name: Curity OAuth and OpenID Connect
  slug: oauth-and-openid-connect
artifact_total: 6
common:
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/curity/refs/heads/main/integrations/curity-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/curity-integration-edges.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.curity.io/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/curity/refs/heads/main/llms/curity-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/curity-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/curity/refs/heads/main/hosts/curity-hosts.yml
  title: ''
  type: Hosts
  url: hosts/curity-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/curity/refs/heads/main/security/curity-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/curity-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/curity/refs/heads/main/security/curity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/curity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://curity.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.curity.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.curity.io/
- group: company
  title: ''
  type: Blog
  url: https://curity.io/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://curity.io/resources/whats-new/
- group: start
  title: ''
  type: GettingStarted
  url: https://curity.io/resources/getting-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/curityio
- group: company
  title: ''
  type: Newsroom
  url: https://curity.io/news/
- group: commercial
  title: ''
  type: Pricing
  url: https://curity.io/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://curity.io/resources/learn/privacy-and-gdpr/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.curity.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://curity.io/terms-of-service/
- group: agent
  title: ''
  type: LLMsTxt
  url: https://curity.io/llms.txt
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://curity.io
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Curity is a Stockholm-based identity company whose Curity Identity Server is a self-hosted OAuth 2.0 and OpenID Connect server. Its interfaces are the standard OAuth/OIDC endpoints, a RESTCONF administration API, GraphQL user and client management APIs, and SCIM 2.0 user provisioning, all served by each customer deployment rather than a Curity-hosted base URL.
image: https://curity.io/images/open-graph/homepage-sharing-image.jpg?v=20260618
layout: provider
modified: '2026-10-13'
name: Curity
nav: Providers
network: true
overview: 'Curity is listed with 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Identity, Authentication, OpenID Connect, and Authorization.


  Curity''s developer surface includes documentation, engineering blog, changelog, getting-started guide, pricing, and 14 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 71.4
    operational_transparency: 36.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Curity Domain Security
  slug: curity-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Curity Trust Center
  slug: curity-trust-center
  summary_line: SOC 2, ISO 27001
slug: curity
tags:
- Company
- Identity
- Authentication
- OpenID Connect
- Authorization
- API Security
website: https://curity.io
---
