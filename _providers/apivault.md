---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.6
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Apivault Agentic Access
  operation_count: 18
  slug: apivault-agentic-access
  summary_line: 18 operations · 7 acting
api_count: 1
apis:
- baseURL: https://api.apivault.dev
  baseurl_source: declared
  description: The all API from Apivault — 1 operation(s) for all.
  name: Apivault All API
  slug: apivault-all-api
- baseURL: https://api.apivault.dev
  baseurl_source: declared
  description: The auth API from Apivault — 4 operation(s) for auth.
  name: Apivault Auth API
  slug: apivault-auth-api
- baseURL: https://api.apivault.dev
  baseurl_source: declared
  description: The categories API from Apivault — 2 operation(s) for categories.
  name: Apivault Categories API
  slug: apivault-categories-api
- baseURL: https://api.apivault.dev
  baseurl_source: declared
  description: The category API from Apivault — 1 operation(s) for category.
  name: Apivault Category API
  slug: apivault-category-api
- baseURL: https://api.apivault.dev
  baseurl_source: declared
  description: The count API from Apivault — 1 operation(s) for count.
  name: Apivault Count API
  slug: apivault-count-api
- baseURL: https://api.apivault.dev
  baseurl_source: declared
  description: The create API from Apivault — 1 operation(s) for create.
  name: Apivault Create API
  slug: apivault-create-api
- baseURL: https://api.apivault.dev
  baseurl_source: declared
  description: The detail API from Apivault — 1 operation(s) for detail.
  name: Apivault Detail API
  slug: apivault-detail-api
- baseURL: https://api.apivault.dev
  baseurl_source: declared
  description: The interaction API from Apivault — 2 operation(s) for interaction.
  name: Apivault Interaction API
  slug: apivault-interaction-api
- baseURL: https://api.apivault.dev
  baseurl_source: declared
  description: The my_api API from Apivault — 1 operation(s) for my_api.
  name: Apivault My API
  slug: apivault-my-api-api
- baseURL: https://api.apivault.dev
  baseurl_source: declared
  description: The pending API from Apivault — 1 operation(s) for pending.
  name: Apivault Pending API
  slug: apivault-pending-api
- baseURL: https://api.apivault.dev
  baseurl_source: declared
  description: The random API from Apivault — 1 operation(s) for random.
  name: Apivault Random API
  slug: apivault-random-api
- baseURL: https://api.apivault.dev
  baseurl_source: declared
  description: The search API from Apivault — 1 operation(s) for search.
  name: Apivault Search API
  slug: apivault-search-api
artifact_total: 27
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apivault/refs/heads/main/overlays/apivault-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/apivault-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://apivault.dev/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apivault/refs/heads/main/agentic-access/apivault-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/apivault-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apivault/refs/heads/main/authentication/apivault-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apivault-authentication.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/exa-studio/ApiVault/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/exa-studio/ApiVault/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/exa-studio/ApiVault/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/exa-studio/ApiVault/blob/main/CONTRIBUTING.md
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apivault/refs/heads/main/security/apivault-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apivault-domain-security.yml
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/exa-studio/ApiVault
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/exa-studio
- group: docs
  title: ''
  type: APIReference
  url: https://api.apivault.dev/api/schema/swagger-ui/
- group: operate
  title: ''
  type: Support
  url: https://github.com/exa-studio/ApiVault/issues
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apivault.dev/privacy-policy
- group: commercial
  title: ''
  type: License
  url: https://github.com/exa-studio/ApiVault/blob/main/LICENSE
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apivault/refs/heads/main/conventions/apivault-conventions.yml
  title: ''
  type: Conventions
  url: conventions/apivault-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apivault/refs/heads/main/errors/apivault-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/apivault-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apivault/refs/heads/main/data-model/apivault-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apivault-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apivault/refs/heads/main/lifecycle/apivault-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/apivault-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/apivault/refs/heads/main/changelog/apivault-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/apivault-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apivault/refs/heads/main/conformance/apivault-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apivault-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apivault/refs/heads/main/packages/apivault-packages.yml
  title: ''
  type: Packages
  url: packages/apivault-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apivault/refs/heads/main/llms/apivault-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apivault-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apivault/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/apivault/refs/heads/main/plans/apivault-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apivault-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/apivault/refs/heads/main/rate-limits/apivault-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apivault-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/apivault/refs/heads/main/finops/apivault-finops.yml
  title: ''
  type: FinOps
  url: finops/apivault-finops.yml
created: '2025-03-01'
description: Apivault is an open-source directory and gateway for discovering public APIs. The platform catalogs thousands of free and public APIs across 51 categories including animals, anime, blockchain, cryptocurrency, finance, health, music, news, and weather, enabling developers to find and explore APIs for application development.
features:
- description: Comprehensive directory of free and public APIs across 51 categories.
  name: API Directory
- description: Search and discover APIs by category including finance, health, weather, blockchain, and more.
  name: API Search and Discovery
- description: Developers can submit their own APIs with authentication type, CORS, and HTTPS details.
  name: API Submission
- description: Discover trending and randomly surfaced APIs across the catalog.
  name: Trending and Random APIs
- description: User account management via Google sign-in for tracking submitted and liked APIs.
  name: User Accounts
- description: Fully open-source project available on GitHub under CC BY-NC-ND 4.0 license.
  name: Open Source
finops:
- name: Apivault Finops
  service_category: API
  slug: apivault-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apivault.png
layout: provider
modified: '2026-09-04'
name: Apivault
nav: Providers
network: true
overview: 'Apivault publishes 12 APIs on the [APIs.io](https://apis.io/) network, including All API, Auth API, Categories API, and 9 more. Tagged areas include API Catalog, API Directory, API Discovery, Open-Source, and Public APIs.


  Apivault''s developer surface includes authentication, API reference, support, changelog, and 23 more developer resources.'
plans:
- name: Apivault Plans Pricing
  plan_count: 0
  slug: apivault-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Apivault Rate Limits
  slug: apivault-rate-limits
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 18.4
    contract_governance: 4.5
    contract_quality: 44.6
    developer_ergonomics: 35.1
    discoverability: 68.5
    operational_transparency: 18.4
  previous_composite: 31.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/apivault/refs/heads/main/screenshots/apivault-2026-06-20T172306.png
security:
- kind: authentication
  name: Apivault Authentication
  slug: apivault-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Apivault Domain Security
  slug: apivault-domain-security
  summary_line: TLSv1.3
slug: apivault
tags:
- API Catalog
- API Directory
- API Discovery
- Open-Source
- Public APIs
use_cases:
- description: Find free and public APIs for application development across 51 categories.
  name: API Discovery
- description: Submit and promote your own API to a community of developers.
  name: API Promotion
- description: Quickly discover APIs to accelerate prototype and proof-of-concept development.
  name: Rapid Prototyping
website: https://apivault.dev/
---
