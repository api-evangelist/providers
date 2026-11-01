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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.1
  scored_at: '2026-10-31'
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
artifact_total: 9
collections:
- collection_type: open
  name: Crisis Helplines Countries API
  slug: open-koko-countries-api
- collection_type: open
  name: Crisis Countries Helplines API
  slug: open-koko-helplines-api
common:
- group: other
  href: https://artifacts.apis.io/koko/overlays/koko-crisis-helplines-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/koko-crisis-helplines-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/koko/security/koko-domain-security.yml
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
  href: https://artifacts.apis.io/koko/changelog/koko-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/koko-changelog.yml
- group: auth
  href: https://artifacts.apis.io/koko/authentication/koko-authentication.yml
  title: ''
  type: Authentication
  url: authentication/koko-authentication.yml
- group: design
  href: https://artifacts.apis.io/koko/conventions/koko-conventions.yml
  title: ''
  type: Conventions
  url: conventions/koko-conventions.yml
- group: design
  href: https://artifacts.apis.io/koko/errors/koko-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/koko-problem-types.yml
- group: design
  href: https://artifacts.apis.io/koko/lifecycle/koko-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/koko-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/koko/conformance/koko-conformance.yml
  title: ''
  type: Conformance
  url: conformance/koko-conformance.yml
- group: design
  href: https://artifacts.apis.io/koko/data-model/koko-data-model.yml
  title: ''
  type: DataModel
  url: data-model/koko-data-model.yml
- group: build
  href: https://artifacts.apis.io/koko/packages/koko-packages.yml
  title: ''
  type: Packages
  url: packages/koko-packages.yml
- group: build
  href: https://artifacts.apis.io/koko/packages/koko-packages.yml
  title: ''
  type: SDKs
  url: packages/koko-packages.yml
- group: agent
  href: https://artifacts.apis.io/koko/well-known/koko-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/koko-well-known.yml
- group: agent
  href: https://artifacts.apis.io/koko/mcp/koko-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/koko-mcp.yml
- group: agent
  href: https://artifacts.apis.io/koko/llms/koko-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/koko-llms.txt
- group: agent
  href: https://artifacts.apis.io/koko/skills/_index.yml
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
overview: 'Koko publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Countries API, Helplines API, and 1 more. Tagged areas include Company, Mental Health, Crisis Support, Suicide Prevention, and Trust and Safety.


  Koko''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, changelog, authentication, and 20 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 34.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 13.4
    developer_ergonomics: 63.7
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 34.5
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
    score: 23.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/koko/koko-2026-07-25T224124.png
security:
- kind: authentication
  name: Koko Authentication
  slug: koko-authentication
  summary_line: none/http · 1 scheme
- kind: domain-security
  name: Koko Domain Security
  slug: koko-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 2
skills:
- name: Match a search term against Koko's risk keyword taxonomy
  slug: koko-match-risk-keywords
- name: Surface crisis helplines for a country
  slug: koko-surface-crisis-helplines
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
