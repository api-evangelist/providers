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
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 33
  human_in_the_loop: 3
  name: Nevercode Agentic Access
  operation_count: 85
  slug: nevercode-agentic-access
  summary_line: 85 operations · 33 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://codemagic.io/
  baseurl_source: spec
  description: REST API endpoints for app previews.
  name: Nevercode App Previews API
  slug: nevercode-app-previews-api
- baseURL: https://codemagic.io/
  baseurl_source: spec
  description: REST API endpoints for applications.
  name: Nevercode Applications API
  slug: nevercode-applications-api
- baseURL: https://codemagic.io/
  baseurl_source: spec
  description: REST API endpoints for billing.
  name: Nevercode Billing API
  slug: nevercode-billing-api
- baseURL: https://codemagic.io/
  baseurl_source: spec
  description: REST API endpoints for build dashboards.
  name: Nevercode Build Dashboards API
  slug: nevercode-build-dashboards-api
- baseURL: https://codemagic.io/
  baseurl_source: spec
  description: REST API endpoints for builds.
  name: Nevercode Builds API
  slug: nevercode-builds-api
- baseURL: https://codemagic.io/
  baseurl_source: spec
  description: REST API endpoints for meta data.
  name: Nevercode Meta API
  slug: nevercode-meta-api
- baseURL: https://codemagic.io/
  baseurl_source: spec
  description: REST API endpoints for over-the-air updates.
  name: Nevercode Over-the-air Updates API
  slug: nevercode-over-the-air-updates-api
- baseURL: https://codemagic.io/
  baseurl_source: spec
  description: REST API endpoints for environment variables.
  name: Nevercode Secrets and Environment Vars API
  slug: nevercode-secrets-and-environment-vars-api
- baseURL: https://codemagic.io/
  baseurl_source: spec
  description: REST API endpoints for team invitations.
  name: Nevercode Team Invitations API
  slug: nevercode-team-invitations-api
- baseURL: https://codemagic.io/
  baseurl_source: spec
  description: REST API endpoints for team members.
  name: Nevercode Team Members API
  slug: nevercode-team-members-api
- baseURL: https://codemagic.io/
  baseurl_source: spec
  description: REST API endpoints for teams.
  name: Nevercode Teams API
  slug: nevercode-teams-api
- baseURL: https://codemagic.io/
  baseurl_source: spec
  description: REST API endpoints for tester groups.
  name: Nevercode Tester Groups API
  slug: nevercode-tester-groups-api
- baseURL: https://codemagic.io/
  baseurl_source: spec
  description: REST API endpoints for users.
  name: Nevercode Users API
  slug: nevercode-users-api
artifact_total: 34
collections:
- collection_type: open
  name: Codemagic App Previews Applications API
  slug: open-nevercode-applications-api
- collection_type: open
  name: Codemagic App Previews Billing API
  slug: open-nevercode-billing-api
- collection_type: open
  name: Codemagic App Previews Build Dashboards API
  slug: open-nevercode-build-dashboards-api
- collection_type: open
  name: Codemagic App Previews Builds API
  slug: open-nevercode-builds-api
- collection_type: open
  name: Codemagic App Previews Meta API
  slug: open-nevercode-meta-api
- collection_type: open
  name: Codemagic App Previews Over-the-air Updates API
  slug: open-nevercode-over-the-air-updates-api
- collection_type: open
  name: Codemagic App Previews Secrets and Environment Vars API
  slug: open-nevercode-secrets-and-environment-vars-api
- collection_type: open
  name: Codemagic App Previews Team Invitations API
  slug: open-nevercode-team-invitations-api
- collection_type: open
  name: Codemagic App Previews Team Members API
  slug: open-nevercode-team-members-api
- collection_type: open
  name: Codemagic App Previews Teams API
  slug: open-nevercode-teams-api
- collection_type: open
  name: Codemagic App Previews Tester Groups API
  slug: open-nevercode-tester-groups-api
- collection_type: open
  name: Codemagic App Previews Users API
  slug: open-nevercode-users-api
common:
- group: commercial
  href: https://artifacts.apis.io/nevercode/plans/nevercode-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nevercode-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/nevercode/capabilities/nevercode-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/nevercode-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/nevercode/overlays/nevercode-codemagic-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/nevercode-codemagic-rest-api-overlay.yaml
- group: build
  href: https://artifacts.apis.io/nevercode/packages/nevercode-packages.yml
  title: ''
  type: Packages
  url: packages/nevercode-packages.yml
- group: build
  href: https://artifacts.apis.io/nevercode/cli/nevercode-cli.yml
  title: ''
  type: CLI
  url: cli/nevercode-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://codemagic.io/security-statement
- group: auth
  href: https://artifacts.apis.io/nevercode/security/nevercode-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nevercode-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/nevercode/agentic-access/nevercode-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/nevercode-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/nevercode/llms/nevercode-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nevercode-llms.txt
- group: agent
  href: https://artifacts.apis.io/nevercode/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/nevercode/conformance/nevercode-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nevercode-conformance.yml
- group: design
  href: https://artifacts.apis.io/nevercode/lifecycle/nevercode-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/nevercode-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/nevercode/mcp/nevercode-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/nevercode-mcp.yml
- group: design
  href: https://artifacts.apis.io/nevercode/data-model/nevercode-data-model.yml
  title: ''
  type: DataModel
  url: data-model/nevercode-data-model.yml
- group: design
  href: https://artifacts.apis.io/nevercode/conventions/nevercode-conventions.yml
  title: ''
  type: Conventions
  url: conventions/nevercode-conventions.yml
- group: auth
  href: https://artifacts.apis.io/nevercode/authentication/nevercode-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nevercode-authentication.yml
- group: design
  href: https://artifacts.apis.io/nevercode/errors/nevercode-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/nevercode-problem-types.yml
- group: company
  title: ''
  type: Website
  url: https://codemagic.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.codemagic.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.codemagic.io
- group: docs
  title: ''
  type: APIReference
  url: https://codemagic.io/api/v3/schema
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.codemagic.io/getting-started/about-codemagic/
- group: company
  title: ''
  type: Blog
  url: https://blog.codemagic.io
- group: operate
  title: ''
  type: Support
  url: https://github.com/orgs/codemagic-ci-cd/discussions
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/codemagic-ci-cd
- group: operate
  title: ''
  type: StatusPage
  url: https://status.codemagic.io
- group: commercial
  title: ''
  type: Pricing
  url: https://codemagic.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://codemagic.io/signup
- group: start
  title: ''
  type: Login
  url: https://codemagic.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://codemagic.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://codemagic.io/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://codemagic.io/security-statement
created: '2026-07-17'
description: Codemagic (built by Nevercode, founded in Estonia) is a continuous integration and delivery (CI/CD) platform purpose-built for mobile app teams. It automates building, testing, code signing, and releasing apps across Flutter, React Native, native iOS and Android, Unity, Ionic, and .NET MAUI, and integrates with GitHub, GitLab, Bitbucket, and Azure DevOps. Its REST API (v3) exposes applications, builds, artifacts, teams, tester groups, secrets and environment variables, over-the-air updates, app previews, and billing so teams can trigger builds and manage their CI/CD pipelines programmatically.
finops:
- has_sources: true
  method: derived
  name: Nevercode Finops
  primary_unit: account
  service_category: ''
  slug: nevercode-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nevercode.png
layout: provider
modified: '2026-07-20'
name: Nevercode
nav: Providers
network: true
overview: 'Nevercode publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including App Previews API, Applications API, Billing API, and 10 more. Tagged areas include Company, Continuous Integration, Continuous Delivery, CI/CD, and DevOps.


  Nevercode''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, engineering blog, support, and 25 more developer resources.'
plans:
- name: Nevercode Plans Pricing
  plan_count: 8
  slug: nevercode-plans-pricing
- name: Nevercode Price Estimates
  plan_count: 0
  slug: nevercode-price-estimates
random_paper: 19
score:
  band: strong
  composite: 58.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 48.8
    developer_ergonomics: 66.1
    discoverability: 57.1
    operational_transparency: 31.6
  previous_composite: 50.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/nevercode/nevercode-2026-08-07T185044.png
security:
- kind: authentication
  name: Nevercode Authentication
  slug: nevercode-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nevercode Domain Security
  slug: nevercode-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 3
skills:
- name: Inspect Codemagic applications and builds
  slug: nevercode-inspect-apps-and-builds
- name: Manage Codemagic secrets and environment variables
  slug: nevercode-manage-secrets
- name: Inspect Codemagic over-the-air updates
  slug: nevercode-ota-updates
slug: nevercode
tags:
- Company
- Continuous Integration
- Continuous Delivery
- CI/CD
- DevOps
- Mobile
- Flutter
- Builds
- App Distribution
- Code Signing
- Developer Tools
website: https://codemagic.io
---
