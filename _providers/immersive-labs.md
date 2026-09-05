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
api_count: 1
apis:
- description: 'The Immersive platform V1 API — a single GraphQL endpoint exposing organizational data (achievements, assignable content, labs, collections, cyber roles, viewer account, workforce scenarios, and OIDC '
  name: Immersive API V1 (GraphQL)
  slug: immersive-api-v1-graphql
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/immersive-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://immersivelabs.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.immersivelabs.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.immersivelabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.immersivelabs.com/hc/en-us/articles/29622787761809-API-Guide
- group: start
  title: ''
  type: GettingStarted
  url: https://support.immersivelabs.com/hc/en-us/articles/29622787761809-API-Guide
- group: operate
  title: ''
  type: Support
  url: https://www.immersivelabs.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.immersivelabs.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.immersivelabs.com/resources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Immersive-Labs-Sec
- group: start
  title: ''
  type: Login
  url: https://immersivelabs.online/signin
- group: start
  title: ''
  type: SignUp
  url: https://www.immersivelabs.com/demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.immersivelabs.com/company/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.immersivelabs.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.immersivelabs.com
- group: auth
  title: ''
  type: Compliance
  url: https://www.immersivelabs.com/company/legal/security-and-privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/immersive-labs-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/immersive-labs-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/immersive-labs-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/immersive-labs-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/immersive-labs-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/immersive-labs-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/immersive-labs-mcp.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/immersive-labs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.immersivelabs.com/company/legal/security-and-privacy
- group: auth
  title: ''
  type: TrustCenter
  url: security/immersive-labs-trust-center.yml
created: '2026-07-17'
description: Immersive Labs (now branded "Immersive") is a cyber resilience platform — "the cyber proving ground for the AI enterprise" — that lets organizations continuously prove and improve the cyber readiness of their workforce, security teams, AI agents, and leadership through hands-on labs, realistic drills, and crisis-simulation exercises. Trusted by more than 30% of Fortune 100 companies, the platform measures human and organizational cyber capability across people, process, and technology. Its APIs let customers export achievements, assignable content, labs, collections, cyber roles, and workforce-scenario data into their own reporting, SIEM, and workforce-analytics systems. The current V1 API is GraphQL (with a legacy GraphQL surface being retired in favor of an actively enhanced V2), authenticated with an API access key and secret token exchanged for a short-lived bearer access token.
image: https://cdn.prod.website-files.com/6735fba9a631272fb4513263/6759b61c2c4a5793d96bfb2d_WhiteOutLogo.svg
layout: provider
modified: '2026-07-19'
name: Immersive Labs
nav: Providers
network: true
overview: 'Immersive Labs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Security Training, Cyber Resilience, and Workforce Development.


  Immersive Labs'' developer surface includes API reference, documentation, getting-started guide, support, engineering blog, signup flow, authentication, and 19 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 36.0
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/immersive-labs/refs/heads/main/screenshots/immersive-labs-2026-07-25T222128.png
security:
- kind: authentication
  name: Immersive Labs Authentication
  slug: immersive-labs-authentication
  summary_line: apiKey/bearer · 2 schemes
- kind: domain-security
  name: Immersive Labs Domain Security
  slug: immersive-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Immersive Labs Vulnerability Disclosure
  slug: immersive-labs-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Immersive Labs Trust Center
  slug: immersive-labs-trust-center
  summary_line: SOC 2 Type II, ISO 27001, UK Cyber Essentials Plus, GDPR
slug: immersive-labs
tags:
- Company
- Cybersecurity
- Security Training
- Cyber Resilience
- Workforce Development
- GraphQL
- Security
- Compliance
website: https://immersivelabs.com
---
