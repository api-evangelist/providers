---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The AWS S3-compatible object storage API for Cubbit DS3. Supports bucket create/delete/list, object upload/download/copy/delete, multipart upload, object versioning, object lock (COMPLIANCE and GOVERN
  name: Cubbit DS3 S3-Compatible API
  slug: cubbit-ds3-s3-compatible-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cubbit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cubbit.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.cubbit.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cubbit.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cubbit.io/guides/s3-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cubbit.io/getting-started/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.cubbit.io/support
- group: company
  title: ''
  type: Blog
  url: https://blog.cubbit.io/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cubbit.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cubbit
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cubbit.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.cubbit.eu/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cubbit.io/legal/ds3-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cubbit.io/legal/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/cubbit-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cubbit-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cubbit-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cubbit-error-codes.yml
- group: build
  title: ''
  type: Packages
  url: packages/cubbit-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/cubbit-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cubbit-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cubbit-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cubbit-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/cubbit-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.cubbit.io/legal/certifications
- group: auth
  title: ''
  type: TrustCenter
  url: security/cubbit-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cubbit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.cubbit.io/bug-bounty-program
created: '2026-07-17'
description: 'Cubbit is a European cloud storage provider offering DS3, a sovereign, geo-distributed, S3-compatible object storage platform. DS3 encrypts (AES-256), fragments, and replicates data across multiple user-selected locations using Reed-Solomon erasure coding, delivering geo-resilience and data sovereignty within Europe. It ships in two forms: DS3 Cloud, a ready-to-use managed geo-redundant object store (TBs to PBs), and DS3 Composer, self-hosted software-defined storage you run on your own hardware (200 TB+). The storage plane exposes an AWS S3-compatible API at https://s3.cubbit.eu (region eu-west-1), authenticated with access key / secret key and AWS Signature Version 4, so existing S3 SDKs, the AWS CLI, rclone, Cyberduck, Veeam and other S3 tooling work unchanged. Cubbit is certified to ISO/IEC 27001, 27017, 27018, 9001, 20000-1 and 22301, and is GDPR- and NIS2-aligned with Italian ACN PA Cloud qualification.'
image: https://cdn.prod.website-files.com/67a4c547ac46cdf433fcc313/67c76518961dec2a8b897c21_og-homepage.webp
layout: provider
modified: '2026-07-18'
name: Cubbit
nav: Providers
network: true
overview: 'Cubbit publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Object Storage, Cloud Storage, S3 Compatible, Storage, and Data Sovereignty.


  Cubbit''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 21 more developer resources.'
random_paper: 59
score:
  band: thin
  composite: 39.4
  delta: 0.9
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 65.2
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 31.6
  previous_composite: 38.5
  provenance:
    conformance: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cubbit/refs/heads/main/screenshots/cubbit-2026-07-25T210852.png
security:
- kind: authentication
  name: Cubbit Authentication
  slug: cubbit-authentication
  summary_line: awsSigV4 · 1 scheme
- kind: domain-security
  name: Cubbit Domain Security
  slug: cubbit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cubbit Vulnerability Disclosure
  slug: cubbit-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Cubbit Trust Center
  slug: cubbit-trust-center
  summary_line: ISO/IEC 27001:2022, ISO/IEC 27017:2015, ISO/IEC 27018:2019, ISO 9001:2015, ISO/IEC 20000-1:2018, ISO 22301:2019, ACN PA Cloud Qualification, GDPR, NIS2
slug: cubbit
tags:
- Object Storage
- Cloud Storage
- S3 Compatible
- Storage
- Data Sovereignty
- Geo-Distributed
- Infrastructure
- Company
website: https://cubbit.io/
---
