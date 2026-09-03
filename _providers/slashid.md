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
- acting_count: 97
  human_in_the_loop: 6
  name: Slashid Agentic Access
  operation_count: 156
  slug: slashid-agentic-access
  summary_line: 156 operations · 97 acting · 6 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.slashid.com
  baseurl_source: declared
  description: The Identity Management API from SlashID — 72 operation(s) for identity management.
  name: SlashID Identity Management API
  slug: slashid-identity-management-api
- baseURL: https://api.slashid.com
  baseurl_source: declared
  description: The OIDC discovery API from SlashID — 2 operation(s) for oidc discovery.
  name: SlashID OIDC discovery API
  slug: slashid-oidc-discovery-api
- baseURL: https://api.slashid.com
  baseurl_source: declared
  description: The Organization SSO config API from SlashID — 4 operation(s) for organization sso config.
  name: SlashID Organization SSO config API
  slug: slashid-organization-sso-config-api
- baseURL: https://api.slashid.com
  baseurl_source: declared
  description: The Organization Webhooks API from SlashID — 5 operation(s) for organization webhooks.
  name: SlashID Organization Webhooks API
  slug: slashid-organization-webhooks-api
- baseURL: https://api.slashid.com
  baseurl_source: declared
  description: The Super Admin Management API from SlashID — 3 operation(s) for super admin management.
  name: SlashID Super Admin Management API
  slug: slashid-super-admin-management-api
- baseURL: https://api.slashid.com
  baseurl_source: declared
  description: The Tokens API from SlashID — 3 operation(s) for tokens.
  name: SlashID Tokens API
  slug: slashid-tokens-api
- baseURL: https://api.slashid.com
  baseurl_source: declared
  description: The Workflows API from SlashID — 10 operation(s) for workflows.
  name: SlashID Workflows API
  slug: slashid-workflows-api
artifact_total: 53
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SlashID Groups API
  slug: open-slashid-groups-api
- collection_type: open
  name: SlashID Groups Identity Management API
  slug: open-slashid-identity-management-api
- collection_type: open
  name: SlashID Groups OAuth2 API
  slug: open-slashid-oauth2-api
- collection_type: open
  name: SlashID Groups OIDC discovery API
  slug: open-slashid-oidc-discovery-api
- collection_type: open
  name: SlashID Groups Organization Allowed Domains API
  slug: open-slashid-organization-allowed-domains-api
- collection_type: open
  name: SlashID Groups Organization Attributes API
  slug: open-slashid-organization-attributes-api
- collection_type: open
  name: SlashID Groups Organization Email Templates API
  slug: open-slashid-organization-email-templates-api
- collection_type: open
  name: SlashID Groups Organization External Credentials API
  slug: open-slashid-organization-external-credentials-api
- collection_type: open
  name: SlashID Groups Organization KYC config API
  slug: open-slashid-organization-kyc-config-api
- collection_type: open
  name: SlashID Groups Organization SSO config API
  slug: open-slashid-organization-sso-config-api
- collection_type: open
  name: SlashID Groups Organization Token Template API
  slug: open-slashid-organization-token-template-api
- collection_type: open
  name: SlashID Groups Organization Webhooks API
  slug: open-slashid-organization-webhooks-api
- collection_type: open
  name: SlashID Groups Organizations API
  slug: open-slashid-organizations-api
- collection_type: open
  name: SlashID Groups Person Attributes API
  slug: open-slashid-person-attributes-api
- collection_type: open
  name: SlashID Groups Person Consents API
  slug: open-slashid-person-consents-api
- collection_type: open
  name: SlashID Groups Person Credentials API
  slug: open-slashid-person-credentials-api
- collection_type: open
  name: SlashID Groups Person handles API
  slug: open-slashid-person-handles-api
- collection_type: open
  name: SlashID Groups Persons API
  slug: open-slashid-persons-api
- collection_type: open
  name: SlashID Groups Persons Bulk Import API
  slug: open-slashid-persons-bulk-import-api
- collection_type: open
  name: SlashID Groups RBAC API
  slug: open-slashid-rbac-api
- collection_type: open
  name: SlashID Groups SSO API
  slug: open-slashid-sso-api
- collection_type: open
  name: SlashID Groups Super Admin Management API
  slug: open-slashid-super-admin-management-api
- collection_type: open
  name: SlashID Groups Tokens API
  slug: open-slashid-tokens-api
- collection_type: open
  name: SlashID Groups Workflows API
  slug: open-slashid-workflows-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/slashid-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/slashid-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/slashid-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/slashid-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.slashid.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.slashid.dev/docs/intro
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/slashid
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/slashid
- group: company
  title: ''
  type: Blog
  url: https://www.slashid.dev/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.slashid.dev/
- group: other
  title: ''
  type: X
  url: https://x.com/slashid_dev
- group: start
  title: ''
  type: Signup
  url: https://console.slashid.dev/signup
- group: commercial
  title: ''
  type: Plans
  url: plans/slashid-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/slashid-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/slashid-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/slashid-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/slashid-context.jsonld
created: '2026-06-12'
description: 'SlashID is a developer-first identity platform that provides REST APIs for passwordless authentication, multi-factor authentication, passkeys, and comprehensive user management across web and mobile applications. The platform offers three core modules: Identity Management for building authentication and user lifecycle flows, Identity Protection for monitoring and remediating security events across human and non-human identities, and Gate for identity-based traffic authorization at the API and workload edge. SlashID supports multiple authentication factors including magic links, biometrics, TOTP, and SSO, with global availability and an event-driven architecture. The service publishes an OpenAPI 1.1 specification and offers JavaScript, React, and Remix SDKs alongside API-key and OAuth2/OIDC authentication.'
examples:
- key_count: 3
  name: Slashid Credential Example
  slug: slashid-credential-example
- key_count: 4
  name: Slashid Oauth2 Token Request Example
  slug: slashid-oauth2-token-request-example
- key_count: 6
  name: Slashid Person Example
  slug: slashid-person-example
- key_count: 5
  name: Slashid Webhook Example
  slug: slashid-webhook-example
- key_count: 4
  name: Slashid Workflow Example
  slug: slashid-workflow-example
finops:
- name: Slashid Finops
  service_category: ''
  slug: slashid-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/slashid.png
json_schemas:
- name: Credential
  property_count: 0
  slug: credential
- name: OrganizationResponse
  property_count: 0
  slug: organization-response
- name: PersonHandle
  property_count: 2
  slug: person-handle
- name: PersonRet
  property_count: 7
  slug: person-ret
- name: PostOAuth2TokenRequest
  property_count: 0
  slug: post-o-auth2-token-request
- name: Webhook
  property_count: 0
  slug: webhook
- name: WorkflowWithConfiguration
  property_count: 0
  slug: workflow-with-configuration
jsonld:
- class_count: 0
  name: Slashid Context
  property_count: 46
  slug: slashid-context
layout: provider
modified: '2026-06-12'
name: SlashID
nav: Providers
network: true
overview: 'SlashID publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Identity Management API, OIDC discovery API, Organization SSO config API, and 4 more. Tagged areas include Identity, Authentication, Passwordless, MFA, and Passkeys.


  The SlashID catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SlashID''s developer surface includes authentication, documentation, engineering blog, signup flow, and 13 more developer resources.'
plans:
- name: Slashid Plans Pricing
  plan_count: 3
  slug: slashid-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 3
  name: Slashid Rate Limits
  slug: slashid-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SlashID API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: slashid-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.7
  coverage:
    artifact_dirs: 15
    catalog_gap: 34.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 25.0
    contract_quality: 66.0
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 34.2
  previous_composite: 47.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/slashid/refs/heads/main/screenshots/slashid-2026-06-20T194022.png
security:
- kind: authentication
  name: Slashid Authentication
  slug: slashid-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Slashid Domain Security
  slug: slashid-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Slashid Trust Center
  slug: slashid-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: slashid
tags:
- Identity
- Authentication
- Passwordless
- MFA
- Passkeys
- User Management
- CIAM
- OIDC
- SSO
- RBAC
- Security
website: https://www.slashid.dev/
---
