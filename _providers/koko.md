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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The keyword-matching service behind Koko's Suicide Prevention Toolkit. Callers match a search term or post against Koko's risk taxonomy, filtered across three dimensions — category, confidence and int
  name: Koko Keywords API
  slug: keywords
- baseURL: https://helpline-api.koko.ai
  baseurl_source: declared
  description: Country metadata endpoints
  name: Koko Countries API
  slug: koko-countries-api
- baseURL: https://helpline-api.koko.ai
  baseurl_source: declared
  description: Crisis helpline data endpoints
  name: Koko Helplines API
  slug: koko-helplines-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Crisis Helplines Countries API
  slug: open-koko-countries-api
- collection_type: open
  name: Crisis Countries Helplines API
  slug: open-koko-helplines-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/koko-crisis-helplines-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/koko-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kokocares.org
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.kokocares.org/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developers.kokocares.org/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.kokocares.org/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.kokocares.org/docs/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://r.kokocares.org/api_signup
- group: operate
  title: ''
  type: Support
  url: https://kokocares.org/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://kokocares.org/faq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kokocares
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kokocares.org/terms-of-use-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kokocares.org/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.kokocares.org/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/koko-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/koko-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/koko-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/koko-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/koko-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/koko-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/koko-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/koko-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/koko-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/koko-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/koko-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/koko-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Koko is a 501(c)(3) nonprofit that makes free, evidence-based mental health support available to young people where they already are — inside the online platforms they use. Koko says it has reached more than 6 million users across 199 countries. Its model is detection plus direction: a keyword and AI engine identifies high-risk posts and searches on partner platforms, and matched users are routed to free crisis helplines and self-guided mini-courses covering mood regulation, body image and self-harm. Koko ships this as a developer-facing Suicide Prevention Toolkit built on two APIs — the credential-gated Koko Keywords API, wrapped by a native Rust client with Python, Ruby, Go and PHP bindings, and the public Crisis Helplines API, which returns crisis helpline contact data by country. Koko has been deployed by TikTok, Pinterest, Giphy, Snapchat, Tumblr, Bluesky, WhatsApp and Discord, and its work is backed by eight peer-reviewed publications including three randomized controlled
  trials.'
image: https://avatars.githubusercontent.com/u/69280615?v=4
layout: provider
modified: '2026-07-19'
name: Koko
nav: Providers
network: true
overview: 'Koko publishes 2 APIs on the [APIs.io](https://apis.io/) network: Countries API and Helplines API. Tagged areas include Company, Mental Health, Crisis Support, Suicide Prevention, and Trust and Safety.


  Koko''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, changelog, authentication, and 20 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 13.4
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 32.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/koko/refs/heads/main/screenshots/koko-2026-07-25T224124.png
security:
- kind: authentication
  name: Koko Authentication
  slug: koko-authentication
  summary_line: none/http · 1 scheme
- kind: domain-security
  name: Koko Domain Security
  slug: koko-domain-security
  summary_line: TLSv1.3 · HSTS
slug: koko
tags:
- Company
- Mental Health
- Crisis Support
- Suicide Prevention
- Trust and Safety
- Content Moderation
- Non-Profit
- Health
- Helplines
website: https://kokocares.org
---
