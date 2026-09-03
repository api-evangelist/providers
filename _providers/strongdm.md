---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: The StrongDM control-plane API for automating management of resources, accounts, roles, access grants, gateways, relays, secret stores, and audit logs. The transport is gRPC with request signing; Stro
  name: StrongDM Admin API
  slug: strongdm-admin-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/strongdm-trust-center.yml
- group: auth
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
  title: ''
  type: Packages
  url: packages/strongdm-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/strongdm-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/strongdm-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/strongdm-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/strongdm-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/strongdm-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/strongdm-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/strongdm-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/strongdm-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.strongdm.com/
- group: agent
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
random_paper: 17
rate_limits:
- limit_count: 4
  name: Strongdm Rate Limits
  slug: strongdm-rate-limits
score:
  band: thin
  composite: 37.9
  coverage:
    artifact_dirs: 13
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 65.8
  previous_composite: 37.9
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
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
