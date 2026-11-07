---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Cyberark Agentic Access
  operation_count: 13
  slug: cyberark-agentic-access
  summary_line: 13 operations · 5 acting
api_count: 2
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
- baseURL: https://conjur.example.com
  baseurl_source: declared
  description: Retrieve public keys associated with users and hosts.
  name: CyberArk Public Keys API
  slug: cyberark-public-keys-api
artifact_total: 34
collections:
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
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.cyberark.com/
- group: commercial
  href: https://artifacts.apis.io/cyberark/finops/cyberark-finops.yml
  title: ''
  type: FinOps
  url: finops/cyberark-finops.yml
- group: operate
  href: https://artifacts.apis.io/cyberark/rate-limits/cyberark-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cyberark-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cyberark/plans/cyberark-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cyberark-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cyberark/rules/cyberark-rules.yml
  title: ''
  type: Spectral
  url: rules/cyberark-rules.yml
- group: design
  href: https://artifacts.apis.io/cyberark/rules/cyberark-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/cyberark-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/cyberark/rules/cyberark-conjur-rules.yml
  title: ''
  type: Spectral
  url: rules/cyberark-conjur-rules.yml
- group: agent
  href: https://artifacts.apis.io/cyberark/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/cyberark/data-model/cyberark-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cyberark-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.cyberark.com/
- group: design
  href: https://artifacts.apis.io/cyberark/errors/cyberark-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cyberark-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cyberark/conformance/cyberark-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cyberark-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cyberark/llms/cyberark-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cyberark-llms.txt
- group: agent
  href: https://artifacts.apis.io/cyberark/well-known/cyberark-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cyberark-well-known.yml
- group: other
  href: https://artifacts.apis.io/cyberark/hosts/cyberark-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cyberark-hosts.yml
- group: other
  href: https://artifacts.apis.io/cyberark/vendors/cyberark-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cyberark-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.paloaltonetworks.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cyberark.com/
- group: start
  title: ''
  type: SignUp
  url: https://register.paloaltonetworks.com/igniteontour
- group: company
  title: ''
  type: Newsroom
  url: https://www.paloaltonetworks.com/company/newsroom
- group: company
  title: ''
  type: Blog
  url: https://www.paloaltonetworks.com/blog/
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
  href: https://artifacts.apis.io/cyberark/agentic-access/cyberark-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cyberark-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cyberark/security/cyberark-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cyberark-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cyberark/security/cyberark-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cyberark-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cyberark/authentication/cyberark-authentication.yml
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
  href: https://artifacts.apis.io/cyberark/json-ld/cyberark-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cyberark-context.jsonld
- group: docs
  href: https://artifacts.apis.io/cyberark/json-schema/cyberark-conjur-resource-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/cyberark-conjur-resource-schema.json
- group: docs
  href: https://artifacts.apis.io/cyberark/json-schema/cyberark-privileged-account-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/cyberark-privileged-account-schema.json
- group: design
  href: https://artifacts.apis.io/cyberark/vocabulary/cyberark-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cyberark-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cyberark/rules/cyberark-conjur-rules.yml
  title: ''
  type: Rules
  url: rules/cyberark-conjur-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.cyberark.com/llms.txt
- group: other
  href: https://artifacts.apis.io/cyberark/capabilities/cyberark-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cyberark-capability-edges.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cyberark.com
created: '2026-03-25'
description: CyberArk is the global leader in identity security, providing a unified Identity Security Platform that protects human, machine, and application identities across hybrid and multi-cloud environments. Core product lines include Privileged Access Manager (PAM Self-Hosted) and Privilege Cloud for credential vaulting and session management; Conjur Secrets Manager (Open Source, Enterprise, and Cloud) for machine-identity and DevOps secrets; CyberArk Identity for workforce SSO, MFA, and lifecycle; Endpoint Privilege Manager for least-privilege enforcement on Windows / macOS / Linux endpoints; Secure Cloud Access for just-in-time cloud entitlements; and Customer Identity for B2B / B2C identity. CyberArk publishes a canonical OpenAPI 3.1 specification for Conjur Secrets Manager at github.com/cyberark/conjur-openapi-spec, and REST APIs for PAM Self-Hosted, Privilege Cloud, and CyberArk Identity are documented on docs.cyberark.com and developer.cyberark.com.
finops:
- has_sources: true
  method: generated
  name: Cyberark Finops
  primary_unit: seat-year
  service_category: Identity Security
  slug: cyberark-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cyberark.png
json_schemas:
- name: ConjurResource
  property_count: 5
  slug: cyberark-conjur-resource
- name: PrivilegedAccount
  property_count: 9
  slug: cyberark-privileged-account
- name: Resource
  property_count: 5
  slug: cyberark-resource
- name: Role
  property_count: 2
  slug: cyberark-role
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
overview: 'CyberArk publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Health API, Policies API, and 7 more. Tagged areas include Authentication, Cloud Security, Conjur, Credential Vault, and DevOps Secrets.


  The CyberArk catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  CyberArk''s developer surface includes documentation, support, signup flow, engineering blog, authentication, and 42 more developer resources.'
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
- authorship: unmarked
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: CyberArk — conjur rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 4
  slug: cyberark-conjur-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: CyberArk — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cyberark-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: CyberArk API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: cyberark-rules
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 29
    catalog_earned: 63.4
    catalog_earned_first_party: 0.0
    catalog_gap: 51.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.3
  facets:
    access_clarity: 26.3
    contract_governance: 31.8
    contract_quality: 57.5
    developer_ergonomics: 23.2
    discoverability: 65.2
    operational_transparency: 34.2
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/cyberark/cyberark-2026-06-20T175406.png
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
skill_count: 1
skills:
- name: cyberark-authentication-get-token
  slug: cyberark-authentication-get-token
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
- Privileged Access Management
- Secrets Management
- Session Management
- SSO
- Vault
- Zero Trust
- Identity Federation
website: https://www.cyberark.com
---
