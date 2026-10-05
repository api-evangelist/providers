---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.8
  scored_at: '2026-10-04'
api_count: 3
apis:
- baseURL: https://app.strongdm.com
  baseurl_source: declared
  description: The StrongDM control-plane API for automating management of resources, accounts, roles, access grants, gateways, relays, secret stores, and audit logs. The transport is gRPC with request signing; Stro
  name: StrongDM Admin API
  slug: strongdm-admin-api
- description: GraphQL endpoint for StrongDM providing schema introspection and operations.
  name: StrongDM GraphQL API
  slug: strongdm-graphql-api
- baseURL: https://app.strongdm.com
  baseurl_source: declared
  description: The Admin API from StrongDM — 4 operation(s) for admin.
  name: StrongDM Admin API
  slug: strongdm-admin-api
artifact_total: 10
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/strongdm/refs/heads/main/rules/strongdm-rules.yml
  title: ''
  type: Spectral
  url: rules/strongdm-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/strongdm/refs/heads/main/json-ld/strongdm-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/strongdm-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/strongdm/refs/heads/main/vocabulary/strongdm-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/strongdm-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/strongdm/refs/heads/main/data-model/strongdm-data-model.yml
  title: ''
  type: DataModel
  url: data-model/strongdm-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/strongdm/refs/heads/main/hosts/strongdm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/strongdm-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/strongdm/refs/heads/main/vendors/strongdm-vendors.yml
  title: ''
  type: Vendors
  url: vendors/strongdm-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.strongdm.com/terms-of-use
- group: auth
  title: ''
  type: Security
  url: https://www.strongdm.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.strongdm.com/press
- group: other
  title: ''
  type: Leadership
  url: https://www.strongdm.com/team/iam
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/strongdm/refs/heads/main/security/strongdm-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/strongdm-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/strongdm/refs/heads/main/security/strongdm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/strongdm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.strongdm.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.strongdm.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.strongdm.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.strongdm.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.strongdm.com/
- group: company
  title: ''
  type: Blog
  url: https://www.strongdm.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.strongdm.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.strongdm.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://app.strongdm.com/app/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/strongdm
- group: operate
  title: ''
  type: StatusPage
  url: https://status.strongdm.com/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/strongdm/refs/heads/main/packages/strongdm-packages.yml
  title: ''
  type: Packages
  url: packages/strongdm-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/strongdm/refs/heads/main/packages/strongdm-packages.yml
  title: ''
  type: SDKs
  url: packages/strongdm-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/strongdm/refs/heads/main/cli/strongdm-cli.yml
  title: ''
  type: CLI
  url: cli/strongdm-cli.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/strongdm/refs/heads/main/authentication/strongdm-authentication.yml
  title: ''
  type: Authentication
  url: authentication/strongdm-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/strongdm/refs/heads/main/conventions/strongdm-conventions.yml
  title: ''
  type: Conventions
  url: conventions/strongdm-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/strongdm/refs/heads/main/rate-limits/strongdm-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/strongdm-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/strongdm/refs/heads/main/lifecycle/strongdm-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/strongdm-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/strongdm/refs/heads/main/changelog/strongdm-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/strongdm-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/strongdm/refs/heads/main/conformance/strongdm-conformance.yml
  title: ''
  type: Conformance
  url: conformance/strongdm-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.strongdm.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/strongdm/refs/heads/main/llms/strongdm-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/strongdm-llms.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.strongdm.com/privacy
created: '2026-07-17'
description: StrongDM is a Zero Trust Privileged Access Management (PAM) platform that brokers and governs access to infrastructure — databases, servers, Kubernetes clusters, cloud resources, network devices, and internal web apps — through a central control plane. It enforces policy and authorization continuously with adaptive action controls, full session recording and audit, and no standing privileges. Automation is exposed through the StrongDM Admin API, a gRPC-based control-plane API that first-party SDKs (Go, Java, Python, Ruby, C#) wrap with REST-like ergonomics and request signing, plus a Terraform provider and the sdm command-line client. This profile was enriched by the API Evangelist pipeline from StrongDM's public developer surface.
image: https://www.strongdm.com/hubfs/strongdm-logo.svg
json_schemas:
- name: GetAdminResourcesResourceidResponse
  property_count: 1
  slug: strongdm-get-admin-resources-resourceid-response
jsonld:
- class_count: 1
  name: Strongdm Context
  property_count: 1
  slug: strongdm-context
layout: provider
modified: '2026-07-21'
name: StrongDM
nav: Providers
network: true
overview: 'StrongDM publishes 3 APIs on the [APIs.io](https://apis.io/) network, including Admin API, and 2 more. Tagged areas include Company, Security, Privileged Access Management, Zero Trust, and Access Management.


  The StrongDM catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  StrongDM''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, support, signup flow, and 28 more developer resources.'
random_paper: 20
rate_limits:
- limit_count: 4
  name: Strongdm Rate Limits
  slug: strongdm-rate-limits
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: StrongDM API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: strongdm-rules
score:
  band: developing
  composite: 52.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 68.2
    catalog_earned_first_party: 12.0
    catalog_gap: 46.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 14.7
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 17.6
    developer_ergonomics: 71.4
    discoverability: 82.1
    operational_transparency: 76.3
  previous_composite: 37.9
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/strongdm/refs/heads/main/screenshots/strongdm-2026-09-02T161023.png
security:
- kind: authentication
  name: Strongdm Authentication
  slug: strongdm-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Strongdm Domain Security
  slug: strongdm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Strongdm Trust Center
  slug: strongdm-trust-center
  summary_line: SOC 2, PCI DSS, GDPR
slug: strongdm
tags:
- Company
- Security
- Privileged Access Management
- Zero Trust
- Access Management
- Identity
- Infrastructure
- Audit
- Compliance
- DevOps
website: https://www.strongdm.com/
---
