---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spirl-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spirl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.defakto.security/
- group: company
  title: ''
  type: Blog
  url: https://www.defakto.security/blog/
- group: start
  title: ''
  type: SignUp
  url: https://www.defakto.security/demo/
- group: operate
  title: ''
  type: Support
  url: https://www.defakto.security/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.defakto.security/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.defakto.security/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://www.defakto.security/security/
created: '2026-07-17'
description: Spirl is a non-human identity and access management (IAM) startup that in 2025 rebranded to Defakto (defakto.security); spirl.com now redirects to the Defakto site. The company secures automated systems — workloads, services, CI/CD pipelines, Kubernetes, and AI agents — by replacing static secrets and hardcoded credentials with short-lived, cryptographically verifiable identities built on open workload-identity standards (SPIFFE/SPIRE style). Co-founded by Eli Nesterov (ex-ByteDance infrastructure) and Danny Oliveri, it targets the enterprise gap where organizations run millions of non-human identities protected only by static secrets. Defakto was named a 2025 Gartner Cool Vendor in Identity-First Security. It is a portfolio company of Bloomberg Beta. As of this profile the company publishes a marketing site, blog, and security page but no public developer API, OpenAPI specification, SDKs, CLI, or developer portal — access is via demo request, so there is no API surface to enrich
  at this time.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spirl.png
layout: provider
modified: '2026-07-21'
name: Spirl
nav: Providers
network: true
overview: 'Spirl is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Identity, Non-Human Identity, and Workload Identity.


  Spirl''s developer surface includes engineering blog, signup flow, support, and 6 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 14.5
  delta: -1.8
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 16.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Spirl Domain Security
  slug: spirl-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Spirl Vulnerability Disclosure
  slug: spirl-vulnerability-disclosure
  summary_line: disclosure policy published
slug: spirl
tags:
- Company
- Security
- Identity
- Non-Human Identity
- Workload Identity
- SPIFFE
- Secrets Management
- Zero Trust
- CI/CD Security
- Kubernetes
- AI Agents
website: https://www.defakto.security/
---
