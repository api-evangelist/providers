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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.6
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Google Vault Agentic Access
  operation_count: 33
  slug: google-vault-agentic-access
  summary_line: 33 operations · 22 acting
api_count: 1
apis:
- baseURL: https://vault.googleapis.com
  baseurl_source: declared
  description: The Exports API from Google Vault — 2 operation(s) for exports.
  name: Google Vault Exports API
  slug: google-vault-exports-api
- baseURL: https://vault.googleapis.com
  baseurl_source: declared
  description: The HeldAccounts API from Google Vault — 2 operation(s) for heldaccounts.
  name: Google Vault HeldAccounts API
  slug: google-vault-heldaccounts-api
- baseURL: https://vault.googleapis.com
  baseurl_source: declared
  description: The Holds API from Google Vault — 4 operation(s) for holds.
  name: Google Vault Holds API
  slug: google-vault-holds-api
- baseURL: https://vault.googleapis.com
  baseurl_source: declared
  description: The Matters API from Google Vault — 8 operation(s) for matters.
  name: Google Vault Matters API
  slug: google-vault-matters-api
- baseURL: https://vault.googleapis.com
  baseurl_source: declared
  description: The Operations API from Google Vault — 3 operation(s) for operations.
  name: Google Vault Operations API
  slug: google-vault-operations-api
- baseURL: https://vault.googleapis.com
  baseurl_source: declared
  description: The Saved Queries API from Google Vault — 2 operation(s) for saved queries.
  name: Google Vault Saved Queries API
  slug: google-vault-saved-queries-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Vault Exports API
  slug: open-google-vault-exports-api
- collection_type: open
  name: Google Vault Exports HeldAccounts API
  slug: open-google-vault-heldaccounts-api
- collection_type: open
  name: Google Vault Exports Holds API
  slug: open-google-vault-holds-api
- collection_type: open
  name: Google Vault Exports Matters API
  slug: open-google-vault-matters-api
- collection_type: open
  name: Google Vault Exports Operations API
  slug: open-google-vault-operations-api
- collection_type: open
  name: Google Vault Exports SavedQueries API
  slug: open-google-vault-savedqueries-api
- collection_type: open
  name: Google Vault API
  slug: open-google-vault
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/overlays/google-vault-savedqueries-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/google-vault-savedqueries-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/agentic-access/google-vault-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-vault-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/security/google-vault-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-vault-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/security/google-vault-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-vault-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/authentication/google-vault-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-vault-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/scopes/google-vault-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/google-vault-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleworkspace
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/workspace/vault/quickstart/python
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/identity/protocols/oauth2
- group: start
  title: ''
  type: Console
  url: https://console.cloud.google.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.google.com/appsstatus/dashboard/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.google.com/workspace/vault/release-notes
- group: company
  title: ''
  type: Blog
  url: https://workspace.google.com/blog/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.google.com/workspace/vault
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/workspace/vault/guides
- group: docs
  title: ''
  type: APIReference
  url: https://developers.google.com/workspace/vault/reference/rest
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/workspace/vault/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://knowledge.workspace.google.com/vault
- group: start
  title: ''
  type: SignUp
  url: https://workspace.google.com/business/signup/welcome
- group: commercial
  title: ''
  type: Pricing
  url: https://workspace.google.com/pricing.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/discovery/google-vault-discovery-v1.json
  title: ''
  type: Discovery
  url: discovery/google-vault-discovery-v1.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/packages/google-vault-packages.yml
  title: ''
  type: Packages
  url: packages/google-vault-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/packages/google-vault-packages.yml
  title: ''
  type: SDKs
  url: packages/google-vault-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/well-known/google-vault-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/google-vault-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/well-known/google-vault-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/google-vault-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/security/google-vault-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/google-vault-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/security/google-vault-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/google-vault-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/security/google-vault-trust-center.yml
  title: ''
  type: Compliance
  url: security/google-vault-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/conformance/google-vault-conformance.yml
  title: ''
  type: Conformance
  url: conformance/google-vault-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/authentication/google-vault-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-vault-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/scopes/google-vault-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/google-vault-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/conventions/google-vault-conventions.yml
  title: ''
  type: Conventions
  url: conventions/google-vault-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/errors/google-vault-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/google-vault-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/lifecycle/google-vault-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/google-vault-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/lifecycle/google-vault-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/google-vault-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/changelog/google-vault-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/google-vault-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/data-model/google-vault-data-model.yml
  title: ''
  type: DataModel
  url: data-model/google-vault-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/rate-limits/google-vault-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-vault-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/plans/google-vault-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-vault-plans-pricing.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/finops/google-vault-finops.yml
  title: ''
  type: FinOps
  url: finops/google-vault-finops.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/llms/google-vault-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/google-vault-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/mcp/google-vault-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/google-vault-mcp.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/sandbox/google-vault-sandbox.yml
  title: ''
  type: X-SandboxAbsent
  url: sandbox/google-vault-sandbox.yml
created: '2025-01-01'
description: Google Vault is the information-governance, legal-hold and eDiscovery service for Google Workspace. Its REST API (vault.googleapis.com v1) lets an administrator open matters, place and lift legal holds across Gmail, Drive, Groups, Chat, Voice, Calendar and Gemini, save and count search queries, and export matching data to Google Cloud Storage. Access is OAuth 2.0 only, gated on Workspace Vault privileges, and the contract is published as a Google Discovery document rather than an OpenAPI.
finops:
- name: Google Vault Finops
  service_category: API
  slug: google-vault-finops
image: https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
layout: provider
modified: '2026-09-12'
name: Google Vault
nav: Providers
network: true
overview: 'Google Vault publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Exports API, HeldAccounts API, Holds API, and 3 more. Tagged areas include eDiscovery, Legal Hold, Information Governance, Compliance, and Archiving.


  Google Vault''s developer surface includes authentication, getting-started guide, developer console, changelog, engineering blog, documentation, API reference, and 40 more developer resources.'
plans:
- name: Google Vault Plans Pricing
  plan_count: 0
  slug: google-vault-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 10
  name: Google Vault Rate Limits
  slug: google-vault-rate-limits
scopes:
- name: Google Vault Scopes
  scope_count: 2
  slug: google-vault-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 59.7
  coverage:
    artifact_dirs: 25
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 68.4
    contract_governance: 18.2
    contract_quality: 51.0
    developer_ergonomics: 66.1
    discoverability: 75.9
    operational_transparency: 84.2
  previous_composite: 59.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/screenshots/google-vault-2026-06-20T182245.png
security:
- kind: authentication
  name: Google Vault Authentication
  slug: google-vault-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Vault Domain Security
  slug: google-vault-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Vault Vulnerability Disclosure
  slug: google-vault-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Google Vault Trust Center
  slug: google-vault-trust-center
  summary_line: FedRAMP, CJIS, HIPAA, US Department of Defense requirements, ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27018, SOC 2
slug: google-vault
tags:
- eDiscovery
- Legal Hold
- Information Governance
- Compliance
- Archiving
- Retention
- Google Workspace
- Audit
website: https://www.google.com/
---
