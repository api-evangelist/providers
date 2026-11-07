---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Redsky is Target's internal aggregation API platform, described by Target's engineering team on tech.target.com, that turns GraphQL queries into client-managed REST APIs serving product, price, promot
  name: Target Redsky API
  slug: target-redsky-api
- description: Target runs a partner-gated developer program at developer.target.com, open to Target team members and third parties with an existing Target relationship. Target publishes no public API reference, mac
  name: Target Partner API
  slug: target-partner-api
artifact_total: 8
common:
- group: other
  href: https://artifacts.apis.io/target/capabilities/target-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/target-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/target/security/target-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/target-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/target/security/target-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/target-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/target/authentication/target-authentication.yml
  title: ''
  type: Authentication
  url: authentication/target-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/target
- group: company
  title: ''
  type: Website
  url: https://www.target.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.target.com/
- group: company
  title: ''
  type: Blog
  url: https://tech.target.com
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/target
- group: other
  title: ''
  type: Open Source
  url: https://tech.target.com/open-source
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.target.com/llms.txt
- group: agent
  href: https://artifacts.apis.io/target/llms/target-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/target-llms.txt
- group: agent
  href: https://artifacts.apis.io/target/well-known/target-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/target-well-known.yml
- group: auth
  href: https://artifacts.apis.io/target/security/target-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/target-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/target/scopes/target-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/target-scopes.yml
- group: design
  href: https://artifacts.apis.io/target/conformance/target-conformance.yml
  title: ''
  type: Conformance
  url: conformance/target-conformance.yml
- group: design
  href: https://artifacts.apis.io/target/lifecycle/target-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/target-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/target/conventions/target-conventions.yml
  title: ''
  type: Conventions
  url: conventions/target-conventions.yml
- group: build
  href: https://artifacts.apis.io/target/packages/target-packages.yml
  title: ''
  type: Packages
  url: packages/target-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.target.com/c/terms-conditions/-/N-4sr7l
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.target.com/c/target-privacy-policy/-/N-4sr7p
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.target.com/
coverage:
  detail: Target's developer program at developer.target.com is partner-gated. Target publishes no public API reference or machine-readable specification. Scaffold OpenAPIs written by an API Evangelist sweep (no Target source; every path 404 on api.target.com) and everything derived from them were quarantined to _scaffold/ on 2026-10-21.
  reason: no-machine-readable-spec
  state: unreadable
created: '2024-01-01'
description: Target Corporation is one of the largest retailers in the United States, offering a wide assortment of general merchandise and food through more than 1,900 stores and digital channels. Target's technology platform powers partner integrations, internal services, and open-source tooling across their retail operations.
graphqls:
- description: Redsky is Target's internal aggregation API platform that converts GraphQL queries into client-managed REST APIs. It serves product data, pricing, promotions, and fulfillment information for Target.co
  name: target GraphQL API
  slug: target-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/target.png
layout: provider
modified: '2026-10-21'
name: Target
nav: Providers
network: true
overview: 'Target is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 100, E-Commerce, Retail, Product, and Inventory.


  Target''s developer surface includes authentication, engineering blog, and 20 more developer resources.'
plans:
- name: Target Plans Pricing
  plan_count: 1
  slug: target-plans-pricing
press:
- date: ''
  title: Target to Roll Out Transformative GenAI Technology to its ...
  url: https://corporate.target.com/press/release/2024/06/target-to-roll-out-transformative-genai-technology-to-its-store-team-members-chainwide
- date: ''
  title: A Partnership to Develop Generative AI Applications Helps ...
  url: https://www.bain.com/client-results/ai/target/
- date: ''
  title: A look at Target's approach to generative AI
  url: https://www.retaildive.com/news/target-generative-artificial-intelligence-technology-forecasting-marketplace/802801/
- date: ''
  title: Target Launches New AI-Powered Features to Make ...
  url: https://www.prnewswire.com/news-releases/target-launches-new-ai-powered-features-to-make-holiday-shopping-easier-smarter-and-more-fun-302612422.html
- date: ''
  title: Target's Using Artificial Intelligence to Make Your Shopping ...
  url: https://corporate.target.com/news-features/article/2023/12/artificial-intelligence
random_paper: 23
scopes:
- name: Target Scopes
  scope_count: 4
  slug: target-scopes
  summary_line: 4 scopes
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 32
    catalog_earned: 34.0
    catalog_earned_first_party: 0.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 26.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 64.3
    operational_transparency: 15.8
  previous_composite: 27.9
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/target/target-2026-08-17T082249.png
security:
- kind: authentication
  name: Target Authentication
  slug: target-authentication
  summary_line: oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Target Domain Security
  slug: target-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Target Vulnerability Disclosure
  slug: target-vulnerability-disclosure
  summary_line: Hackerone
slug: target
tags:
- Fortune 100
- E-Commerce
- Retail
- Product
- Inventory
- Stores
- Order
website: https://www.target.com
---
