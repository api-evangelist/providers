---
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.4
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Aranya Client API is the library interface an application uses to talk to the Aranya daemon. It covers team creation, device onboarding and removal, role and permission management (including custo
  name: Aranya Client API
  slug: spideroak-aranya-client
artifact_total: 6
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/aranya-project/aranya/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://spideroak.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aranya-project.github.io/
- group: docs
  title: ''
  type: Documentation
  url: https://aranya-project.github.io/
- group: docs
  title: ''
  type: APIReference
  url: https://aranya-project.github.io/technical-apis
- group: start
  title: ''
  type: GettingStarted
  url: https://aranya-project.github.io/getting-started
- group: operate
  title: ''
  type: Support
  url: https://spideroak.support/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://spideroak.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://spideroak.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aranya-project
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/SpiderOak
- group: commercial
  title: ''
  type: Pricing
  url: https://spideroak.com/product/
- group: start
  title: ''
  type: SignUp
  url: https://spideroak.com/request-a-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://spideroak.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://spideroak.com/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://spideroak.com/security-response/
- group: auth
  title: ''
  type: Compliance
  url: https://spideroak.com/hipaa/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/aranya-project/aranya/releases
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/spideroak-vocabulary.yml
- group: build
  title: ''
  type: Packages
  url: packages/spideroak-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/spideroak-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spideroak-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/spideroak-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spideroak-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spideroak-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spideroak-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/spideroak-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spideroak-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/spideroak-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/spideroak-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spideroak-rate-limits.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spideroak-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spideroak-domain-security.yml
created: '2026-08-29'
description: 'SpiderOak (SpiderOak, Inc. / SpiderOak Mission Systems) builds zero-trust access governance and secure data exchange software for defense, aerospace and commercial operators working in contested, disconnected, degraded, intermittent and low-bandwidth (DDIL) environments. Its developer surface is Aranya, the open-source access-governance and secure-data-exchange platform that also powers the commercial OrbitSecure product: a Rust client library, a long-running daemon, a domain-specific policy language with its own compiler and virtual machine, and Aranya Fast Channels (AFC) for buffer-based encryption without a transport. Aranya ships a public C API (a cbindgen-generated header with 111 public functions) and a Rust API published as 31 crates on crates.io, with documentation, specifications and a 57-term glossary on the Aranya Project docs site. SpiderOak also operates the legacy SpiderOak ONE no-knowledge encrypted backup product and Tactical Edge Cyber Services (TECS) consulting.'
image: https://spideroak.com/wp-content/uploads/2024/09/SpiderOak-Logo-v202409-white.png
layout: provider
modified: '2026-08-29'
name: SpiderOak
nav: Providers
network: true
overview: 'SpiderOak publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Zero Trust, Encryption, and Access Control.


  SpiderOak''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
plans:
- name: Spideroak Plans Pricing
  plan_count: 2
  slug: spideroak-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Spideroak Rate Limits
  slug: spideroak-rate-limits
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 17
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 33.3
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 66.7
    governance: 33.3
    operational_transparency: 28.9
  previous_composite: 42.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Spideroak Authentication
  slug: spideroak-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Spideroak Domain Security
  slug: spideroak-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Spideroak Vulnerability Disclosure
  slug: spideroak-vulnerability-disclosure
  summary_line: Hackerone
slug: spideroak
tags:
- Company
- Security
- Zero Trust
- Encryption
- Access Control
- Identity and Access Management
- Cryptography
- Defense
- Aerospace
- Space
- Open-Source
- Edge Computing
- Data Exchange
- Backup and Storage
website: https://spideroak.com/
---
