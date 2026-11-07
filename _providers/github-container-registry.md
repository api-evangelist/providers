---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Github Container Registry Agentic Access
  operation_count: 18
  slug: github-container-registry-agentic-access
  summary_line: 18 operations · 7 acting
api_count: 1
apis:
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Manage container packages owned by an organization
  name: GitHub Container Registry Organization Packages API
  slug: github-container-registry-organization-packages-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: View packages owned by a user
  name: GitHub Container Registry User Namespace Packages API
  slug: github-container-registry-user-namespace-packages-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Manage container packages owned by the authenticated user
  name: GitHub Container Registry User Packages API
  slug: github-container-registry-user-packages-api
artifact_total: 13
collections:
- collection_type: open
  name: GitHub Container Registry Organization Packages API
  slug: open-github-container-registry-organization-packages-api
- collection_type: open
  name: GitHub Container Registry Organization Packages User Namespace Packages API
  slug: open-github-container-registry-user-namespace-packages-api
- collection_type: open
  name: GitHub Container Registry Organization Packages User Packages API
  slug: open-github-container-registry-user-packages-api
- collection_type: open
  name: GitHub Container Registry API
  slug: open-github-container-registry
common:
- group: design
  href: https://artifacts.apis.io/github-container-registry/rules/github-container-registry-rules.yml
  title: ''
  type: Spectral
  url: rules/github-container-registry-rules.yml
- group: design
  href: https://artifacts.apis.io/github-container-registry/vocabulary/github-container-registry-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/github-container-registry-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/github-container-registry/conventions/github-container-registry-conventions.yml
  title: ''
  type: Conventions
  url: conventions/github-container-registry-conventions.yml
- group: design
  href: https://artifacts.apis.io/github-container-registry/lifecycle/github-container-registry-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/github-container-registry-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/github-container-registry/conformance/github-container-registry-conformance.yml
  title: ''
  type: Conformance
  url: conformance/github-container-registry-conformance.yml
- group: auth
  href: https://artifacts.apis.io/github-container-registry/well-known/github-container-registry-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/github-container-registry-www-security.txt
- group: agent
  href: https://artifacts.apis.io/github-container-registry/well-known/github-container-registry-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/github-container-registry-well-known.yml
- group: other
  href: https://artifacts.apis.io/github-container-registry/hosts/github-container-registry-hosts.yml
  title: ''
  type: Hosts
  url: hosts/github-container-registry-hosts.yml
- group: build
  href: https://artifacts.apis.io/github-container-registry/integrations/github-container-registry-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/github-container-registry-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/github-container-registry/vendors/github-container-registry-vendors.yml
  title: ''
  type: Vendors
  url: vendors/github-container-registry-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/github-container-registry/plans/github-container-registry-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/github-container-registry-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/github-container-registry/rate-limits/github-container-registry-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/github-container-registry-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/github-container-registry/finops/github-container-registry-finops.yml
  title: ''
  type: FinOps
  url: finops/github-container-registry-finops.yml
- group: agent
  href: https://artifacts.apis.io/github-container-registry/agentic-access/github-container-registry-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/github-container-registry-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/github-container-registry/authentication/github-container-registry-authentication.yml
  title: ''
  type: Authentication
  url: authentication/github-container-registry-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://docs.github.com/en/packages
- group: docs
  title: ''
  type: Documentation
  url: https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/github
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.github.com/en/billing/managing-billing-for-github-packages/about-billing-for-github-packages
- group: company
  title: ''
  type: Blog
  url: https://github.blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.githubstatus.com/
- group: start
  title: ''
  type: Signup
  url: https://github.com/signup
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.github.com/llms.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.github.com/en/site-policy/github-terms/github-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement
- group: operate
  title: ''
  type: Support
  url: https://support.github.com/
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/github/roadmap
- group: docs
  title: ''
  type: APIReference
  url: https://docs.github.com/en/rest/packages/packages
created: '2026-03-26'
description: GitHub Container Registry stores container images within your GitHub organization or personal account, allows you to associate images with repositories, and provides fine-grained permissions for managing access. It supports Docker and OCI image formats and is integrated with GitHub Actions for automated workflows.
finops:
- has_sources: false
  method: generated
  name: Github Container Registry Finops
  primary_unit: request
  service_category: API
  slug: github-container-registry-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/github-container-registry.png
layout: provider
modified: '2026-11-04'
name: GitHub Container Registry
nav: Providers
network: true
overview: 'GitHub Container Registry publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Organization Packages API, User Namespace Packages API, and User Packages API. Tagged areas include Container Images, Containers, GitHub, Packages, and Registry.


  The GitHub Container Registry catalog on APIs.io includes 1 Spectral governance ruleset.


  GitHub Container Registry''s developer surface includes authentication, documentation, getting-started guide, pricing, engineering blog, signup flow, support, and 22 more developer resources.'
plans:
- name: Github Container Registry Plans Pricing
  plan_count: 5
  slug: github-container-registry-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 6
  name: Github Container Registry Rate Limits
  slug: github-container-registry-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 0
  extends: []
  name: GitHub Container Registry API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: github-container-registry-rules
score:
  band: developing
  composite: 54.1
  coverage:
    artifact_dirs: 25
    catalog_earned: 62.3
    catalog_earned_first_party: 24.0
    catalog_gap: 52.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 19.5
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 44.1
    developer_ergonomics: 47.6
    discoverability: 73.2
    operational_transparency: 65.8
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/github-container-registry/github-container-registry-2026-06-20T181838.png
security:
- kind: authentication
  name: Github Container Registry Authentication
  slug: github-container-registry-authentication
  summary_line: http · 1 scheme
slug: github-container-registry
tags:
- Container Images
- Containers
- GitHub
- Packages
- Registry
- OCI
- Docker
---
