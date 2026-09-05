---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.copado.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.copado.com/developer-hub
- group: docs
  title: ''
  type: Documentation
  url: https://docs.copado.com/
- group: docs
  title: ''
  type: APIReference
  url: https://copadomulticoudwebhooks.docs.apiary.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.copado.com/developer-hub
- group: operate
  title: ''
  type: Support
  url: https://success.copado.com/
- group: company
  title: ''
  type: Blog
  url: https://www.copado.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/copadosolutions
- group: commercial
  title: ''
  type: Pricing
  url: https://www.copado.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://login.copado.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.copado.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.copado.com/legal/privacy
- group: build
  title: ''
  type: Packages
  url: packages/copado-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/copado-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/copado-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/copado-authentication.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/copado-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/copado-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.copado.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/copado-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.copado.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/copado-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/copado-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/copado-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.copado.com/disclosure
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/copado-llms.txt
created: '2026-07-17'
description: Copado is an AI-powered DevOps platform for Salesforce and other low-code SaaS clouds. It provides CI/CD, release management, version control, automated robotic testing, data deployment, and security & governance for enterprise Salesforce delivery teams. Copado extends its platform through a Developer Hub (Functions, Actions, Job Engine, custom pipelines), a REST Actions API and Webhooks API, an official Salesforce-CLI plugin, and a Python AI SDK. The company is backed by Insight Partners and SoftBank Vision Fund and maintains SOC 2 Type 2, ISO 27001, FedRAMP, and GDPR-aligned security posture.
image: https://cdn.prod.website-files.com/62d8507d84c54d359ad063bc/68d6224cfed524ccca1b4ff4_Web%20Thumbnail_Copado_Intelligent%20DevOps%20Platform%20for%20Salesforce.avif
layout: provider
modified: '2026-07-18'
name: Copado
nav: Providers
network: true
overview: 'Copado is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DevOps, Salesforce, CI/CD, and Release Management.


  Copado''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, CLI, and 19 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 67.9
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 38.1
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/copado/refs/heads/main/screenshots/copado-2026-07-25T210407.png
security:
- kind: authentication
  name: Copado Authentication
  slug: copado-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Copado Domain Security
  slug: copado-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Copado Vulnerability Disclosure
  slug: copado-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Copado Trust Center
  slug: copado-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP
slug: copado
tags:
- Company
- DevOps
- Salesforce
- CI/CD
- Release Management
- Testing
- DevSecOps
- Low-Code
website: https://www.copado.com/
---
