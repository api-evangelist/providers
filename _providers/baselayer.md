---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Business identity verification, risk assessment, and fraud detection APIs
  name: Baselayer API
  slug: baselayer-api
artifact_total: 6
asyncapis:
- description: ''
  name: Baselayer Webhooks
  slug: baselayer-webhooks
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://baselayer.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://baselayer.com/privacy-policy/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/baselayer/refs/heads/main/plans/baselayer-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/baselayer-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/baselayer/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/baselayer/refs/heads/main/asyncapi/baselayer-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/baselayer-webhooks.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/baselayer/refs/heads/main/changelog/baselayer-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/baselayer-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.baselayer.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/baselayer/refs/heads/main/authentication/baselayer-authentication.yml
  title: ''
  type: Authentication
  url: authentication/baselayer-authentication.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.baselayer.com/docs/api-versioning-compatibility.md
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/baselayer/refs/heads/main/lifecycle/baselayer-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/baselayer-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/baselayer/refs/heads/main/conformance/baselayer-conformance.yml
  title: ''
  type: Conformance
  url: conformance/baselayer-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/baselayer/refs/heads/main/llms/baselayer-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/baselayer-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/baselayer/refs/heads/main/a2a/baselayer-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/baselayer-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/baselayer/refs/heads/main/well-known/baselayer-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/baselayer-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/baselayer/refs/heads/main/hosts/baselayer-hosts.yml
  title: ''
  type: Hosts
  url: hosts/baselayer-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/baselayer/refs/heads/main/vendors/baselayer-vendors.yml
  title: ''
  type: Vendors
  url: vendors/baselayer-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/baselayer/refs/heads/main/packages/baselayer-packages.yml
  title: ''
  type: SDKs
  url: packages/baselayer-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/baselayer/refs/heads/main/packages/baselayer-packages.yml
  title: ''
  type: Packages
  url: packages/baselayer-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.baselayer.com/
- group: company
  title: ''
  type: Newsroom
  url: https://baselayer.com/resources/content-type/press/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.baselayer.com/changelog/texas-comptroller-franchise-tax-standing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/baselayer
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/baselayer/refs/heads/main/security/baselayer-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/baselayer-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/baselayer/refs/heads/main/security/baselayer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/baselayer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://baselayer.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.baselayer.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.baselayer.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.baselayer.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.baselayer.com
- group: company
  title: ''
  type: Blog
  url: https://baselayer.com/resources
- group: commercial
  title: ''
  type: Pricing
  url: https://baselayer.com/pricing
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://docs.baselayer.com/mcp
  - status: 401
    url: https://api.baselayer.com/mcp
  - status: 200
    url: https://baselayer.com
  reason: partner-login
  state: gated
created: '2026-10-14'
description: Baselayer provides business identity verification, risk assessment, and fraud detection APIs for financial institutions, fintechs, and marketplaces. Their platform offers real-time KYB, credit, sanctions, industry classification, and monitoring services, enabling automated underwriting and compliance workflows. The company emphasizes AI-driven insights and a comprehensive data source network to reduce manual reviews and improve decision speed.
image: https://baselayer.com/wp-content/uploads/2025/07/OG.jpg
layout: provider
modified: '2026-10-14'
name: Baselayer
nav: Providers
network: true
overview: 'Baselayer is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Business, IdentityVerification, Risk Management, and Fintech.


  The Baselayer catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Baselayer''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 24 more developer resources.'
plans:
- name: Baselayer Plans Pricing
  plan_count: 3
  slug: baselayer-plans-pricing
random_paper: 6
score:
  band: developing
  composite: 53.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 4.5
    contract_quality: 39.0
    developer_ergonomics: 61.2
    discoverability: 66.1
    operational_transparency: 52.6
  provenance:
    conformance: derived
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Baselayer Authentication
  slug: baselayer-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Baselayer Domain Security
  slug: baselayer-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Baselayer Trust Center
  slug: baselayer-trust-center
  summary_line: SOC 2
slug: baselayer
tags:
- Business
- IdentityVerification
- Risk Management
- Fintech
website: https://baselayer.com
---
