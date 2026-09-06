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
  - '{''url'': ''https://wandz.ai/'', ''status'': 301, ''note'': ''declared website redirects to https://www.abtasty.com/adaptivecx/ — a different registrable domain (wandz.ai -> abtasty.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/namogoo-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/namogoo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wandz.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/namogoo
- group: start
  title: ''
  type: Login
  url: https://app.wandz.ai/login
- group: operate
  title: ''
  type: Support
  url: https://wandz.ai/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wandz.ai/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wandz.ai/terms-of-use/
- group: auth
  title: ''
  type: Security
  url: https://wandz.ai/security/
- group: auth
  title: ''
  type: Compliance
  url: https://wandz.ai/security/
- group: other
  title: ''
  type: Acquisition
  url: https://www.abtasty.com/blog/wandzai-acquisition/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/namogoo_stock/
- group: build
  title: ''
  type: Packages
  url: packages/namogoo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/namogoo-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/namogoo-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/namogoo-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/namogoo-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/namogoo-lifecycle.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/namogoo-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/namogoo-llms.txt
coverage:
  checked: '2026-08-04'
  detail: Namogoo ships actively maintained first-party mobile SDKs (Maven Central ai.wandz.android:core-wandz 1.0.49, CocoaPods NamogooIBPSDK, SPM WandzSDK), but the only reference for them is a 3.7 MB PDF committed to a GitHub repository — there is no web API reference, no OpenAPI on any resolvable Namogoo or Wandz host, and namogoo.com now 301s through wandz.ai to AB Tasty AdaptiveCX after the November 2025 acquisition.
  evidence:
  - status: 200
    url: https://github.com/namogoo/wandz-android-sample/raw/main/ReadmeAssets/WandzAndroidSDK.pdf
  - status: 404
    url: https://wandz.ai/openapi.json
  - status: 404
    url: https://wandz.ai/.well-known/agent-card.json
  - status: 301
    url: https://www.namogoo.com/
  reason: pdf-only-docs
  state: unreadable
created: '2026-08-04'
description: Namogoo Technologies Ltd. is an Israeli (Herzliya) commerce-technology company founded in 2014, originally known for Customer Journey Hijacking prevention and later for its Digital Journey Continuity and Intent-Based Promotions products for online retailers. The company pivoted to real-time predictive AI for the customer experience, rebranded its product and site to Wandz.ai, and was acquired by French experimentation vendor AB Tasty in November 2025, where the technology now powers AB Tasty AdaptiveCX. Namogoo publishes no public REST API or OpenAPI definition; its integration surface is a JavaScript tag plus first-party mobile SDKs distributed through Maven Central (ai.wandz.android:core-wandz), CocoaPods (NamogooIBPSDK), Swift Package Manager (WandzSDK) and Packagist (Magento 2 modules), activated with an Account ID / client ID issued through the Wandz.ai platform portal.
image: https://avatars.githubusercontent.com/u/48321538?v=4
layout: provider
modified: '2026-08-04'
name: Namogoo
nav: Providers
network: true
overview: 'Namogoo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, Personalization, and Customer Experience.


  Namogoo''s developer surface includes support, authentication, and 18 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  previous_composite: 23.1
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/namogoo/refs/heads/main/screenshots/namogoo-2026-08-07T184614.png
security:
- kind: authentication
  name: Namogoo Authentication
  slug: namogoo-authentication
  summary_line: account-id · 2 schemes
- kind: domain-security
  name: Namogoo Domain Security
  slug: namogoo-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Namogoo Vulnerability Disclosure
  slug: namogoo-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Namogoo Trust Center
  slug: namogoo-trust-center
  summary_line: trust center published
slug: namogoo
tags:
- Company
- E-Commerce
- Retail
- Personalization
- Customer Experience
- Predictive AI
- Marketing
- Mobile SDK
- Israel
website: https://wandz.ai/
---
