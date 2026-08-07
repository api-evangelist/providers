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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Parcel is Oasis Labs' data-governance API for uploading and tokenizing sensitive data, defining programmable access grants and permissions, running confidential compute jobs over that data, and managi
  name: Oasis Labs Parcel API
  slug: oasis-labs-parcel-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.oasislabs.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.oasislabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oasislabs.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.oasislabs.com/parcel/latest/parcel-api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oasislabs.com/parcel/latest
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oasislabs
- group: company
  title: ''
  type: Blog
  url: https://medium.com/oasislabs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oasislabs.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oasislabs.com/privacy-policy
- group: build
  title: ''
  type: SDKs
  url: packages/oasis-labs-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/oasis-labs-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/oasis-labs-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oasis-labs-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/oasis-labs-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/oasis-labs-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/oasis-labs-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/oasis-labs-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oasis-labs-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/oasis-labs-llms.txt
created: '2026-07-17'
description: Oasis Labs builds privacy-preserving data and compute technologies. Its developer platform, Parcel, is a data-governance API for uploading, tokenizing, and computing over sensitive datasets under programmable access grants, with confidential compute jobs and identity/permission management. Oasis Labs also ships PrivateSQL (differential-privacy SQL analytics) and privacy-preserving AI tooling built on secure enclaves, MPC, homomorphic encryption, and zero-knowledge proofs. The company was founded out of UC Berkeley and is backed by a16z, DCVC, Pantera Capital, and Polychain. The Parcel REST API is documented at docs.oasislabs.com with an official TypeScript SDK and OAuth2 client-credentials (private_key_jwt) authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oasis-labs.png
layout: provider
modified: '2026-07-20'
name: Oasis Labs
nav: Providers
network: true
overview: 'Oasis Labs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Privacy, Data Governance, Confidential Computing, and Blockchain.


  Oasis Labs'' developer surface includes documentation, API reference, getting-started guide, engineering blog, CLI, authentication, and 13 more developer resources.'
random_paper: 102
scopes:
- name: Oasis Labs Scopes
  scope_count: 7
  slug: oasis-labs-scopes
  summary_line: 7 scopes
score:
  band: emerging
  composite: 26.2
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 5.3
  previous_composite: 26.2
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Oasis Labs Authentication
  slug: oasis-labs-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Oasis Labs Domain Security
  slug: oasis-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oasis-labs
tags:
- Company
- Privacy
- Data Governance
- Confidential Computing
- Blockchain
- Differential Privacy
- Machine Learning
- Developer Platform
- Web3
website: https://www.oasislabs.com/
---
