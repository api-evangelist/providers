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
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-04'
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
  description: Apivault is a free, open-source API directory that serves as a gateway to a world of public APIs. It catalogs APIs across 51 categories with details on authentication method, CORS support, and HTTPS a
  name: Apivault
  slug: apivault
artifact_total: 16
common:
- group: company
  title: ''
  type: Website
  url: https://apivault.dev/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apivault-agentic-access.yml
- group: auth
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
  title: ''
  type: Conventions
  url: conventions/apivault-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/apivault-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/apivault-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/apivault-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/apivault-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/apivault-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/apivault-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/apivault-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/apivault-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/apivault-rate-limits.yml
- group: commercial
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
overview: 'Apivault publishes 1 API on the [APIs.io](https://apis.io/) network: Apivault. Tagged areas include API Catalog, API Directory, API Discovery, Open-Source, and Public APIs.


  Apivault''s developer surface includes authentication, API reference, support, changelog, and 22 more developer resources.'
plans:
- name: Apivault Plans Pricing
  plan_count: 0
  slug: apivault-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Apivault Rate Limits
  slug: apivault-rate-limits
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 18.2
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 4.5
    contract_quality: 48.3
    developer_ergonomics: 35.1
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 21.1
  previous_composite: 14.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: rising
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
