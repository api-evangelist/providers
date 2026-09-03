---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Sso Agentic Access
  operation_count: 11
  slug: sso-agentic-access
  summary_line: 11 operations · 4 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://your-idp.example.com
  baseurl_source: declared
  description: SAML 2.0 authentication request and response endpoints for initiating and completing SSO login flows.
  name: SSO Authentication API
  slug: sso-authentication-api
- baseURL: https://your-idp.example.com
  baseurl_source: declared
  description: OIDC authorization endpoints for initiating authentication flows and exchanging authorization codes for tokens.
  name: SSO Authorization API
  slug: sso-authorization-api
- baseURL: https://your-idp.example.com
  baseurl_source: declared
  description: OpenID Provider Discovery endpoint for retrieving provider configuration metadata.
  name: SSO Discovery API
  slug: sso-discovery-api
- baseURL: https://your-idp.example.com
  baseurl_source: declared
  description: JSON Web Key Set (JWKS) endpoint for retrieving public keys used to verify ID token signatures.
  name: SSO Keys API
  slug: sso-keys-api
- baseURL: https://your-idp.example.com
  baseurl_source: declared
  description: SAML 2.0 Single Logout (SLO) endpoints for terminating SSO sessions across all service providers.
  name: SSO Logout API
  slug: sso-logout-api
- baseURL: https://your-idp.example.com
  baseurl_source: declared
  description: SAML 2.0 metadata endpoints for exchanging federation configuration between identity providers and service providers.
  name: SSO Metadata API
  slug: sso-metadata-api
- baseURL: https://your-idp.example.com
  baseurl_source: declared
  description: Token endpoint operations for exchanging authorization codes and refresh tokens for access tokens and ID tokens.
  name: SSO Token API
  slug: sso-token-api
- baseURL: https://your-idp.example.com
  baseurl_source: declared
  description: UserInfo endpoint for retrieving authenticated user profile claims.
  name: SSO User Info API
  slug: sso-user-info-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenID Connect (OIDC) SSO Authentication API
  slug: open-sso-authentication-api
- collection_type: open
  name: OpenID Connect (OIDC) SSO Authentication Authorization API
  slug: open-sso-authorization-api
- collection_type: open
  name: OpenID Connect (OIDC) SSO Authentication Discovery API
  slug: open-sso-discovery-api
- collection_type: open
  name: OpenID Connect (OIDC) SSO Authentication Keys API
  slug: open-sso-keys-api
- collection_type: open
  name: OpenID Connect (OIDC) SSO Authentication Logout API
  slug: open-sso-logout-api
- collection_type: open
  name: OpenID Connect (OIDC) SSO Authentication Metadata API
  slug: open-sso-metadata-api
- collection_type: open
  name: OpenID Connect (OIDC) SSO API
  slug: open-sso-oidc
- collection_type: open
  name: SAML 2.0 SSO API
  slug: open-sso-saml
- collection_type: open
  name: OpenID Connect (OIDC) SSO Authentication Token API
  slug: open-sso-token-api
- collection_type: open
  name: OpenID Connect (OIDC) SSO Authentication User Info API
  slug: open-sso-user-info-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sso-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sso-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sso-authentication.yml
- group: docs
  title: ''
  type: Specification
  url: https://www.oasis-open.org/standards#samlv2.0
- group: docs
  title: ''
  type: Specification
  url: https://openid.net/connect/
- group: docs
  title: ''
  type: Specification
  url: https://oauth.net/2/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/api-evangelist/sso
- group: design
  title: ''
  type: JSONLD
  url: json-ld/sso-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/sso-saml-assertion-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/sso-oidc-token-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sso-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/sso-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://www.oasis-open.org/feed/
created: '2025-01-01'
description: Single Sign-On (SSO) is an authentication technology that allows users to log in once and gain access to multiple related applications and services without re-authenticating. SSO implementations rely on protocols such as SAML 2.0, OpenID Connect (OIDC), and OAuth 2.0. Major identity providers including Okta, Microsoft Entra ID, Google, Ping Identity, Auth0, and Keycloak expose SSO APIs that allow applications to integrate federated authentication, token exchange, assertion validation, and session management.
examples:
- key_count: 6
  name: Sso Oidc Token Response Example
  slug: sso-oidc-token-response-example
finops:
- name: Sso Finops
  service_category: API
  slug: sso-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sso.png
json_schemas:
- name: OIDC Token Response
  property_count: 6
  slug: sso-oidc-token
- name: SAML Assertion
  property_count: 8
  slug: sso-saml-assertion
json_structures:
- name: Sso Saml Assertion Structure
  property_count: 8
  slug: sso-saml-assertion-structure
jsonld:
- class_count: 32
  name: Sso Context
  property_count: 5
  slug: sso-context
layout: provider
modified: '2026-05-19'
name: SSO
nav: Providers
network: true
overview: 'SSO publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Authorization API, Discovery API, and 5 more. Tagged areas include Authentication, Authorization, Identity, OIDC, and SAML.


  The SSO catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SSO''s developer surface includes authentication, engineering blog, and 11 more developer resources.'
plans:
- name: Sso Plans Pricing
  plan_count: 3
  slug: sso-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Sso Rate Limits
  slug: sso-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SSO API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sso-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: SSO API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 7
  slug: sso-rules
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 16
    catalog_gap: 54.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 56.0
    developer_ergonomics: 23.8
    discoverability: 63.0
    governance: 28.8
    operational_transparency: 13.2
  previous_composite: 33.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sso/refs/heads/main/screenshots/sso-2026-06-20T194436.png
security:
- kind: authentication
  name: Sso Authentication
  slug: sso-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sso Domain Security
  slug: sso-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sso
tags:
- Authentication
- Authorization
- Identity
- OIDC
- SAML
- Security
- Single Sign-On
- SSO
---
