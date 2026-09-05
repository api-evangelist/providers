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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The OpenBao HTTP API gives full access to every OpenBao capability over REST-like HTTP verbs. All routes are prefixed with /v1/ and the API is versioned only at that prefix. Authentication is by clien
  name: OpenBao HTTP API
  slug: openbao-http-api
artifact_total: 7
asyncapis:
- description: ''
  name: Openbao Audit Events
  slug: openbao-audit-events
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openbao-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://openbao.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://openbao.org/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://openbao.org/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://openbao.org/docs/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://openbao.org/docs/get-started/developer-qs/
- group: operate
  title: ''
  type: Support
  url: https://openbao.org/community/
- group: company
  title: ''
  type: Blog
  url: https://openbao.org/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openbao
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/openbao/openbao/issues/1974
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lfprojects.org/policies/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lfprojects.org/policies/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/openbao-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/openbao-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/openbao-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/openbao-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/openbao-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/openbao-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/openbao-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/openbao-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/openbao-conformance.yml
- group: auth
  title: ''
  type: Security
  url: security/openbao-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/openbao-vulnerability-disclosure.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/openbao-backend.proto
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/openbao-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/openbao-plans-pricing.yml
created: '2026-08-27'
description: 'OpenBao is an open source, community-driven identity-based secrets and encryption management system, forked from HashiCorp Vault in 2023 and governed by the Linux Foundation as a sandbox project of the Open Source Security Foundation (OpenSSF). It stores and tightly controls access to tokens, passwords, certificates and encryption keys, and exposes every one of its capabilities — key/value secrets, dynamic database credentials, PKI issuance, transit encryption, leasing and revocation, policy and namespace administration, seal/unseal and cluster operations — through a single JSON HTTP API prefixed with /v1/. OpenBao is self-hosted software rather than a hosted service, so there is no vendor-operated base URL: the API is served by whatever instance an operator runs, and the CLI, the web UI and the official Go client all speak the same HTTP API. The machine-readable OpenAPI document is generated per instance at runtime from the mounted backends and is served at /v1/sys/internal/specs/openapi
  rather than published as a static file.'
image: https://raw.githubusercontent.com/openbao/artwork/main/color/openbao-color.png
layout: provider
modified: '2026-08-27'
name: OpenBao
nav: Providers
network: true
overview: 'OpenBao publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Secrets Management, Security, Identity and Access Management, Encryption, and Certificates.


  The OpenBao catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  OpenBao''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, CLI, and 20 more developer resources.'
plans:
- name: Openbao Plans Pricing
  plan_count: 0
  slug: openbao-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Openbao Rate Limits
  slug: openbao-rate-limits
score:
  band: developing
  composite: 49.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 85.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 49.6
  provenance:
    conformance: first-party
    mcp: derived
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openbao/refs/heads/main/screenshots/openbao-2026-09-02T150850.png
security:
- kind: authentication
  name: Openbao Authentication
  slug: openbao-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Openbao Domain Security
  slug: openbao-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Openbao Vulnerability Disclosure
  slug: openbao-vulnerability-disclosure
  summary_line: Hackerone
slug: openbao
tags:
- Secrets Management
- Security
- Identity and Access Management
- Encryption
- Certificates
- PKI
- Key Management
- Open-Source
- Self-Hosted
- Linux Foundation
- DevOps
- Infrastructure
website: https://openbao.org/
---
