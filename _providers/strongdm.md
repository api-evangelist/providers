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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.0
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: The StrongDM control-plane API for automating management of resources, accounts, roles, access grants, gateways, relays, secret stores, and audit logs. The transport is gRPC with request signing; Stro
  name: StrongDM Admin API
  slug: strongdm-admin-api
artifact_total: 5
common:
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
created: '2026-07-17'
description: StrongDM is a Zero Trust Privileged Access Management (PAM) platform that brokers and governs access to infrastructure — databases, servers, Kubernetes clusters, cloud resources, network devices, and internal web apps — through a central control plane. It enforces policy and authorization continuously with adaptive action controls, full session recording and audit, and no standing privileges. Automation is exposed through the StrongDM Admin API, a gRPC-based control-plane API that first-party SDKs (Go, Java, Python, Ruby, C#) wrap with REST-like ergonomics and request signing, plus a Terraform provider and the sdm command-line client. This profile was enriched by the API Evangelist pipeline from StrongDM's public developer surface.
image: https://www.strongdm.com/hubfs/strongdm-logo.svg
layout: provider
modified: '2026-07-21'
name: StrongDM
nav: Providers
network: true
overview: 'StrongDM publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Privileged Access Management, Zero Trust, and Access Management.


  StrongDM''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, support, signup flow, and 17 more developer resources.'
random_paper: 20
rate_limits:
- limit_count: 4
  name: Strongdm Rate Limits
  slug: strongdm-rate-limits
score:
  band: thin
  composite: 38.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 26.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 73.2
    operational_transparency: 65.8
  previous_composite: 37.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
