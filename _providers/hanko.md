---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    error_semantics: false
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
  score: 22.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 53
  human_in_the_loop: 0
  name: Hanko Agentic Access
  operation_count: 84
  slug: hanko-agentic-access
  summary_line: 84 operations · 53 acting
api_count: 3
apis:
- baseURL: https://{tenant_id}.hanko.io
  baseurl_source: declared
  description: The Audit Logs API from Hanko — 2 operation(s) for audit logs.
  name: Hanko Audit Logs API
  slug: hanko-audit-logs-api
- baseURL: https://{tenant_id}.hanko.io
  baseurl_source: declared
  description: The Credentials API from Hanko — 9 operation(s) for credentials.
  name: Hanko Credentials API
  slug: hanko-credentials-api
- baseURL: https://{tenant_id}.hanko.io
  baseurl_source: declared
  description: The Email Management API from Hanko — 3 operation(s) for email management.
  name: Hanko Email Management API
  slug: hanko-email-management-api
- baseURL: https://{tenant_id}.hanko.io
  baseurl_source: declared
  description: The Login API from Hanko — 2 operation(s) for login.
  name: Hanko Login API
  slug: hanko-login-api
- baseURL: https://{tenant_id}.hanko.io
  baseurl_source: declared
  description: The Metrics API from Hanko — 1 operation(s) for metrics.
  name: Hanko Metrics API
  slug: hanko-metrics-api
- baseURL: https://{tenant_id}.hanko.io
  baseurl_source: declared
  description: Represents all objects which are related to MFA in common
  name: Hanko mfa API
  slug: hanko-mfa-api
- baseURL: https://{tenant_id}.hanko.io
  baseurl_source: declared
  description: The Passcode API from Hanko — 2 operation(s) for passcode.
  name: Hanko Passcode API
  slug: hanko-passcode-api
- baseURL: https://{tenant_id}.hanko.io
  baseurl_source: declared
  description: The Password API from Hanko — 2 operation(s) for password.
  name: Hanko Password API
  slug: hanko-password-api
- baseURL: https://{tenant_id}.hanko.io
  baseurl_source: declared
  description: The SAML API from Hanko — 3 operation(s) for saml.
  name: Hanko SAML API
  slug: hanko-saml-api
- baseURL: https://{tenant_id}.hanko.io
  baseurl_source: declared
  description: The Session Management API from Hanko — 1 operation(s) for session management.
  name: Hanko Session Management API
  slug: hanko-session-management-api
- baseURL: https://{tenant_id}.hanko.io
  baseurl_source: declared
  description: The Sessions API from Hanko — 1 operation(s) for sessions.
  name: Hanko Sessions API
  slug: hanko-sessions-api
- baseURL: https://{tenant_id}.hanko.io
  baseurl_source: declared
  description: The Status API from Hanko — 1 operation(s) for status.
  name: Hanko Status API
  slug: hanko-status-api
- baseURL: https://{tenant_id}.hanko.io
  baseurl_source: declared
  description: The Third Party API from Hanko — 2 operation(s) for third party.
  name: Hanko Third Party API
  slug: hanko-third-party-api
- baseURL: https://{tenant_id}.hanko.io
  baseurl_source: declared
  description: The Token API from Hanko — 1 operation(s) for token.
  name: Hanko Token API
  slug: hanko-token-api
- baseURL: https://{tenant_id}.hanko.io
  baseurl_source: declared
  description: The Transaction API from Hanko — 2 operation(s) for transaction.
  name: Hanko Transaction API
  slug: hanko-transaction-api
- baseURL: https://{tenant_id}.hanko.io
  baseurl_source: declared
  description: The User Management API from Hanko — 5 operation(s) for user management.
  name: Hanko User Management API
  slug: hanko-user-management-api
- baseURL: https://{tenant_id}.hanko.io
  baseurl_source: declared
  description: The User Metadata Management API from Hanko — 1 operation(s) for user metadata management.
  name: Hanko User Metadata Management API
  slug: hanko-user-metadata-management-api
- baseURL: https://{tenant_id}.hanko.io
  baseurl_source: declared
  description: The Users API from Hanko — 9 operation(s) for users.
  name: Hanko Users API
  slug: hanko-users-api
- baseURL: https://{tenant_id}.hanko.io
  baseurl_source: declared
  description: Represents all objects which are related to WebAuthn in common
  name: Hanko webauthn API
  slug: hanko-webauthn-api
- baseURL: https://{tenant_id}.hanko.io
  baseurl_source: declared
  description: The Webhooks API from Hanko — 2 operation(s) for webhooks.
  name: Hanko Webhooks API
  slug: hanko-webhooks-api
- baseURL: https://{tenant_id}.hanko.io
  baseurl_source: declared
  description: The .well-known API from Hanko — 2 operation(s) for .well-known.
  name: Hanko .well-known API
  slug: hanko-well-known-api
artifact_total: 58
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hanko Admin Audit Logs API
  slug: open-hanko-audit-logs-api
- collection_type: open
  name: Hanko Admin Audit Logs Credentials API
  slug: open-hanko-credentials-api
- collection_type: open
  name: Hanko Admin Audit Logs Email Management API
  slug: open-hanko-email-management-api
- collection_type: open
  name: Hanko Admin Audit Logs flow API
  slug: open-hanko-flow-api
- collection_type: open
  name: Hanko Admin Audit Logs Login API
  slug: open-hanko-login-api
- collection_type: open
  name: Hanko Admin Audit Logs Metrics API
  slug: open-hanko-metrics-api
- collection_type: open
  name: Hanko Admin Audit Logs mfa API
  slug: open-hanko-mfa-api
- collection_type: open
  name: Hanko Admin Audit Logs Passcode API
  slug: open-hanko-passcode-api
- collection_type: open
  name: Hanko Admin Audit Logs Password API
  slug: open-hanko-password-api
- collection_type: open
  name: Hanko Admin Audit Logs SAML API
  slug: open-hanko-saml-api
- collection_type: open
  name: Hanko Admin Audit Logs Session Management API
  slug: open-hanko-session-management-api
- collection_type: open
  name: Hanko Admin Audit Logs Sessions API
  slug: open-hanko-sessions-api
- collection_type: open
  name: Hanko Admin Audit Logs Status API
  slug: open-hanko-status-api
- collection_type: open
  name: Hanko Admin Audit Logs Third Party API
  slug: open-hanko-third-party-api
- collection_type: open
  name: Hanko Admin Audit Logs Token API
  slug: open-hanko-token-api
- collection_type: open
  name: Hanko Admin Audit Logs Transaction API
  slug: open-hanko-transaction-api
- collection_type: open
  name: Hanko Admin Audit Logs User Management API
  slug: open-hanko-user-management-api
- collection_type: open
  name: Hanko Admin Audit Logs User Metadata Management API
  slug: open-hanko-user-metadata-management-api
- collection_type: open
  name: Hanko Admin Audit Logs Users API
  slug: open-hanko-users-api
- collection_type: open
  name: Hanko Admin Audit Logs webauthn API
  slug: open-hanko-webauthn-api
- collection_type: open
  name: Hanko Admin Audit Logs Webhooks API
  slug: open-hanko-webhooks-api
- collection_type: open
  name: Hanko Admin Audit Logs .well-known API
  slug: open-hanko-well-known-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hanko-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hanko-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hanko-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.hanko.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hanko.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/teamhanko
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/teamhanko
- group: company
  title: ''
  type: Blog
  url: https://www.hanko.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hanko.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hanko.io
- group: other
  title: ''
  type: X
  url: https://twitter.com/hanko
- group: commercial
  title: ''
  type: Plans
  url: plans/hanko-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hanko-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hanko-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/hanko-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/hanko-context.jsonld
created: '2026-06-12'
description: Hanko is a passkey-first, open-source authentication platform that serves as a modern alternative to Auth0, Clerk, and WorkOS. It provides a REST API covering passkeys (WebAuthn/FIDO2), passwords, OAuth social login, SAML SSO, multi-factor authentication, and session management. Hanko is available as a managed cloud service and as a self-hosted open-source deployment, targeting developers who want to add passwordless authentication to their applications. The platform is headquartered in Germany and emphasizes privacy-first, European-hosted infrastructure with a free tier supporting up to 10,000 monthly active users.
examples:
- key_count: 3
  name: Hanko Passkey Registration Example
  slug: hanko-passkey-registration-example
- key_count: 3
  name: Hanko User Get Example
  slug: hanko-user-get-example
- key_count: 3
  name: Hanko Webauthn Login Initialize Example
  slug: hanko-webauthn-login-initialize-example
finops:
- name: Hanko Finops
  service_category: Security
  slug: hanko-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hanko.png
json_schemas:
- name: Hanko Session
  property_count: 8
  slug: hanko-session
- name: Hanko User
  property_count: 7
  slug: hanko-user
- name: Hanko WebAuthn Credential
  property_count: 11
  slug: hanko-webauthn-credential
jsonld:
- class_count: 6
  name: Hanko Context
  property_count: 30
  slug: hanko-context
layout: provider
modified: '2026-06-12'
name: Hanko
nav: Providers
network: true
overview: 'Hanko publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Audit Logs API, Credentials API, Email Management API, and 18 more. Tagged areas include Authentication, Passkeys, WebAuthn, FIDO2, and Identity.


  The Hanko catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Hanko''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Hanko Plans Pricing
  plan_count: 4
  slug: hanko-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Hanko Rate Limits
  slug: hanko-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Hanko API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: hanko-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.9
  coverage:
    artifact_dirs: 15
    catalog_gap: 28.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 25.0
    contract_quality: 65.1
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 50.0
  previous_composite: 47.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hanko/refs/heads/main/screenshots/hanko-2026-06-20T182504.png
security:
- kind: authentication
  name: Hanko Authentication
  slug: hanko-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Hanko Domain Security
  slug: hanko-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hanko
tags:
- Authentication
- Passkeys
- WebAuthn
- FIDO2
- Identity
- SAML
- Passwordless
- Open-Source
website: https://www.hanko.io
---
