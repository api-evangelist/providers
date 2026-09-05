---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://api.leminnow.com
  baseurl_source: declared
  description: Server-side CAPTCHA answer verification.
  name: Capy Inc. Verification API
  slug: capy-inc-verification-api
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lemin Captcha Verification API
  slug: open-capy-inc-verification-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/capy-inc-captcha-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://leminnow.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.leminnow.com/knowledge/developers-guide
- group: docs
  title: ''
  type: Documentation
  url: https://help.leminnow.com/knowledge/developers-guide
- group: docs
  title: ''
  type: APIReference
  url: https://help.leminnow.com/knowledge/verifying-a-lemin-captcha-answer
- group: start
  title: ''
  type: GettingStarted
  url: https://help.leminnow.com/knowledge/obtaining-the-javascript-code-for-lemin-captcha
- group: operate
  title: ''
  type: Support
  url: https://help.leminnow.com/knowledge/faqs
- group: commercial
  title: ''
  type: Pricing
  url: https://leminnow.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.leminnow.com/auth/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.leminnow.com/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://leminnow.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://leminnow.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/leminnow
- group: build
  title: ''
  type: Packages
  url: packages/capy-inc-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/capy-inc-packages.yml
- group: design
  title: ''
  type: Components
  url: components/capy-inc-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/capy-inc-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/capy-inc-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/capy-inc-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/capy-inc-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/capy-inc-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/capy-inc-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/capy-inc-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/capy-inc-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/capy-inc-plans.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/capy-inc-domain-security.yml
created: '2026-07-17'
description: 'Capy Inc. operates Lemin Captcha, a gamified bot-prevention and CAPTCHA service that replaces traditional image-selection challenges with playful, brandable puzzle games. Lemin protects websites and apps from automated attacks such as account takeover and credential stuffing while improving the human experience: the company reports puzzles are solved in roughly five seconds (versus eighteen for legacy CAPTCHAs) with far lower abandonment. Developers embed a client-side widget (available as first-party React, Angular, and Vue components on npm), then verify the visitor''s encrypted answer server-side against the Lemin verification API using their account private key. Capy Inc. is a 500 Global portfolio company.'
image: https://leminnow.com/favicon.ico
layout: provider
modified: '2026-07-18'
name: Capy Inc.
nav: Providers
network: true
overview: 'Capy Inc. publishes 1 API on the [APIs.io](https://apis.io/) network: Verification API. Tagged areas include Company, Security, CAPTCHA, Bot Detection, and Bot Prevention.


  Capy Inc.''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, authentication, and 20 more developer resources.'
plans:
- name: Capy Inc Plans
  plan_count: 2
  slug: capy-inc-plans
random_paper: 11
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 59.2
    commercial_clarity: 59.2
    contract_governance: 4.5
    contract_quality: 13.1
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 36.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/capy-inc/refs/heads/main/screenshots/capy-inc-2026-08-17T083008.png
security:
- kind: authentication
  name: Capy Inc Authentication
  slug: capy-inc-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Capy Inc Domain Security
  slug: capy-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: capy-inc
tags:
- Company
- Security
- CAPTCHA
- Bot Detection
- Bot Prevention
- Fraud Prevention
- Account Takeover
- Authentication
- Web Security
- Developer Tools
website: https://leminnow.com
---
