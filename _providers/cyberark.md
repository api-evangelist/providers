---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Cyberark Agentic Access
  operation_count: 13
  slug: cyberark-agentic-access
  summary_line: 13 operations · 5 acting
api_count: 1
apis:
- description: The Privileged Access Manager Self-Hosted REST API exposes the Vault for managing accounts, safes, platforms, users, sessions, and applications. Authentication uses the Logon endpoint at /PasswordVaul
  name: CyberArk PAM Self-Hosted REST API
  slug: pam-self-hosted
- description: The Privilege Cloud Shared Services REST API mirrors the PAM Self-Hosted surface for accounts, safes, platforms, and users while running as a SaaS on the CyberArk Identity Security Platform. Identitie
  name: CyberArk Privilege Cloud REST API
  slug: privilege-cloud
- description: The CyberArk Identity REST API enables programmatic management of users, roles, applications, MFA policies, SSO, and SCIM-based provisioning across the workforce identity tenant. Tenants are addressed
  name: CyberArk Identity REST API
  slug: identity
- baseURL: https://conjur.example.com
  baseurl_source: declared
  description: Authenticate hosts and users, exchange credentials for access tokens.
  name: CyberArk Authentication API
  slug: cyberark-authentication-api
- baseURL: https://conjur.example.com
  baseurl_source: declared
  description: Health and information endpoints.
  name: CyberArk Health API
  slug: cyberark-health-api
- baseURL: https://conjur.example.com
  baseurl_source: declared
  description: Load, update, and replace Conjur policy YAML.
  name: CyberArk Policies API
  slug: cyberark-policies-api
- baseURL: https://conjur.example.com
  baseurl_source: declared
  description: Retrieve public keys associated with users and hosts.
  name: CyberArk PublicKeys API
  slug: cyberark-publickeys-api
- baseURL: https://conjur.example.com
  baseurl_source: declared
  description: Inspect resources (hosts, users, groups, layers, variables) and check permissions.
  name: CyberArk Resources API
  slug: cyberark-resources-api
- baseURL: https://conjur.example.com
  baseurl_source: declared
  description: Manage role membership and inspect role information.
  name: CyberArk Roles API
  slug: cyberark-roles-api
- baseURL: https://conjur.example.com
  baseurl_source: declared
  description: Store and retrieve secret values bound to variable resources.
  name: CyberArk Secrets API
  slug: cyberark-secrets-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CyberArk Conjur Secrets Manager Authentication API
  slug: open-cyberark-authentication-api
- collection_type: open
  name: CyberArk Conjur Secrets Manager API
  slug: open-cyberark-conjur
- collection_type: open
  name: CyberArk Conjur Secrets Manager Authentication Health API
  slug: open-cyberark-health-api
- collection_type: open
  name: CyberArk Conjur Secrets Manager Authentication Policies API
  slug: open-cyberark-policies-api
- collection_type: open
  name: CyberArk Conjur Secrets Manager Authentication PublicKeys API
  slug: open-cyberark-publickeys-api
- collection_type: open
  name: CyberArk Conjur Secrets Manager Authentication Resources API
  slug: open-cyberark-resources-api
- collection_type: open
  name: CyberArk Conjur Secrets Manager Authentication Roles API
  slug: open-cyberark-roles-api
- collection_type: open
  name: CyberArk Conjur Manager Authentication Secrets API
  slug: open-cyberark-secrets-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/cyberark/conjur/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/cyberark/conjur/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/cyberark/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/cyberark/conjur/blob/master/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cyberark-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cyberark-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cyberark-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cyberark-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cyber-ark-software
- group: company
  title: ''
  type: Website
  url: https://www.cyberark.com
- group: other
  title: ''
  type: Products
  url: https://www.cyberark.com/products/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cyberark.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cyberark.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cyberark
- group: docs
  title: ''
  type: ConjurOpenAPISpec
  url: https://github.com/cyberark/conjur-openapi-spec
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.cyberark.com/
- group: auth
  title: ''
  type: Trust
  url: https://www.cyberark.com/trust/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cyberark.com/legal-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cyberark.com/privacy-policy/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cyberark-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cyberark-conjur-resource-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cyberark-privileged-account-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/cyberark-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/cyberark-conjur-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.cyberark.com/llms.txt
created: '2026-03-25'
description: CyberArk is the global leader in identity security, providing a unified Identity Security Platform that protects human, machine, and application identities across hybrid and multi-cloud environments. Core product lines include Privileged Access Manager (PAM Self-Hosted) and Privilege Cloud for credential vaulting and session management; Conjur Secrets Manager (Open Source, Enterprise, and Cloud) for machine-identity and DevOps secrets; CyberArk Identity for workforce SSO, MFA, and lifecycle; Endpoint Privilege Manager for least-privilege enforcement on Windows / macOS / Linux endpoints; Secure Cloud Access for just-in-time cloud entitlements; and Customer Identity for B2B / B2C identity. CyberArk publishes a canonical OpenAPI 3.1 specification for Conjur Secrets Manager at github.com/cyberark/conjur-openapi-spec, and REST APIs for PAM Self-Hosted, Privilege Cloud, and CyberArk Identity are documented on docs.cyberark.com and developer.cyberark.com.
finops:
- name: Cyberark Finops
  service_category: Identity Security
  slug: cyberark-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cyberark.png
json_schemas:
- name: ConjurResource
  property_count: 5
  slug: cyberark-conjur-resource
- name: PrivilegedAccount
  property_count: 9
  slug: cyberark-privileged-account
jsonld:
- class_count: 29
  name: Cyberark Context
  property_count: 0
  slug: cyberark-context
layout: provider
modified: '2026-05-19'
name: CyberArk
nav: Providers
network: true
overview: 'CyberArk publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Health API, Policies API, and 4 more. Tagged areas include Authentication, Cloud Security, Conjur, Credential Vault, and DevOps Secrets.


  The CyberArk catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  CyberArk''s developer surface includes authentication, documentation, and 23 more developer resources.'
plans:
- name: Cyberark Plans Pricing
  plan_count: 4
  slug: cyberark-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 4
  name: Cyberark Rate Limits
  slug: cyberark-rate-limits
rules:
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: CyberArk API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 4
  slug: cyberark-conjur-rules
- effective_rule_count: 5
  extends: []
  name: CyberArk API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cyberark-jsonschema-spectral-rules
score:
  band: developing
  composite: 41.1
  coverage:
    artifact_dirs: 15
    catalog_gap: 43.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 69.7
    contract_quality: 55.8
    developer_ergonomics: 14.3
    discoverability: 66.7
    governance: 69.7
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 65.0
  previous_composite: 41.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cyberark/refs/heads/main/screenshots/cyberark-2026-06-20T175406.png
security:
- kind: authentication
  name: Cyberark Authentication
  slug: cyberark-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cyberark Domain Security
  slug: cyberark-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Cyberark Trust Center
  slug: cyberark-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: cyberark
tags:
- Authentication
- Cloud Security
- Conjur
- Credential Vault
- DevOps Secrets
- Endpoint Privilege Management
- Identity Security
- Machine Identity
- MFA
- OpenAPI
- PAM
- Privileged Access
- Privileged Access Management
- Secrets Management
- Session Management
- SSO
- Vault
- Zero Trust
website: https://www.cyberark.com
---
