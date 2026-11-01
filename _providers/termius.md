---
access_model:
  confidence: low
  label: Open access
  onboarding: open
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
    idempotency: derived
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Create a new Group
  name: Termius Group API
  slug: termius-group-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Create or Delete a host inside the vault or the group
  name: Termius Host API
  slug: termius-host-api
artifact_total: 14
collections:
- collection_type: open
  name: Termius API Bridge group API
  slug: open-termius-group-api
- collection_type: open
  name: Termius API Bridge group host API
  slug: open-termius-host-api
common:
- group: commercial
  href: https://artifacts.apis.io/termius/plans/termius-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/termius-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/termius/overlays/termius-api-bridge-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/termius-api-bridge-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://termius.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.termius.com
- group: docs
  title: ''
  type: APIReference
  url: https://termius.com/api-docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://termius.com/documentation/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.termius.com/hc/en-us/
- group: company
  title: ''
  type: Blog
  url: https://termius.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/termius
- group: commercial
  title: ''
  type: Pricing
  url: https://termius.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://account.termius.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://termius.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://termius.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.termius.com/
- group: operate
  href: https://artifacts.apis.io/termius/changelog/termius-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/termius-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://termius.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://security.termius.com
- group: auth
  title: ''
  type: Compliance
  url: https://security.termius.com
- group: agent
  href: https://artifacts.apis.io/termius/llms/termius-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/termius-llms.txt
- group: agent
  href: https://artifacts.apis.io/termius/well-known/termius-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/termius-well-known.yml
- group: auth
  href: https://artifacts.apis.io/termius/well-known/termius-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/termius-security.txt
- group: agent
  href: https://artifacts.apis.io/termius/mcp/termius-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/termius-mcp.yml
- group: design
  href: https://artifacts.apis.io/termius/conformance/termius-conformance.yml
  title: ''
  type: Conformance
  url: conformance/termius-conformance.yml
- group: design
  href: https://artifacts.apis.io/termius/errors/termius-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/termius-problem-types.yml
- group: design
  href: https://artifacts.apis.io/termius/lifecycle/termius-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/termius-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/termius/authentication/termius-authentication.yml
  title: ''
  type: Authentication
  url: authentication/termius-authentication.yml
- group: auth
  href: https://artifacts.apis.io/termius/security/termius-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/termius-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/termius/security/termius-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/termius-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/termius/conventions/termius-conventions.yml
  title: ''
  type: Conventions
  url: conventions/termius-conventions.yml
- group: design
  href: https://artifacts.apis.io/termius/conventions/termius-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/termius-conventions.yml
- group: design
  href: https://artifacts.apis.io/termius/data-model/termius-data-model.yml
  title: ''
  type: DataModel
  url: data-model/termius-data-model.yml
- group: build
  href: https://artifacts.apis.io/termius/cli/termius-cli.yml
  title: ''
  type: CLI
  url: cli/termius-cli.yml
- group: build
  href: https://artifacts.apis.io/termius/packages/termius-packages.yml
  title: ''
  type: Packages
  url: packages/termius-packages.yml
- group: agent
  href: https://artifacts.apis.io/termius/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Termius is a modern, cross-platform SSH client for DevOps professionals, network engineers, and infrastructure teams, available on Windows, macOS, Linux, iOS, iPadOS, and Android. It provides secure remote access with encrypted team vaults, shared and synced credentials, SSH keys, snippets, SFTP, port forwarding, jump hosts, and session organization. For programmatic use Termius ships the API Bridge — a self-hosted REST API (OpenAPI 3.0) that encrypts infrastructure data locally and pushes hosts and groups into a Termius Team vault — plus an official command-line client. The company also runs a Security Center with a SOC 2 report.
finops:
- has_sources: true
  method: derived
  name: Termius Finops
  primary_unit: seat
  service_category: ''
  slug: termius-finops
  template: false
image: https://framerusercontent.com/images/JcjJ8OLLESSIHYJ4Rdi4fZmDkQw.png
layout: provider
modified: '2026-07-21'
name: Termius
nav: Providers
network: true
overview: 'Termius publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Group API and Host API. Tagged areas include Company, Enterprise Saas, SSH, SSH Client, and Terminal.


  Termius'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
plans:
- name: Termius Plans Pricing
  plan_count: 5
  slug: termius-plans-pricing
- name: Termius Price Estimates
  plan_count: 0
  slug: termius-price-estimates
random_paper: 9
score:
  band: strong
  composite: 57.5
  coverage:
    artifact_dirs: 24
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 100.0
    contract_governance: 4.5
    contract_quality: 42.9
    developer_ergonomics: 56.5
    discoverability: 57.1
    operational_transparency: 47.4
  previous_composite: 49.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/termius/termius-2026-08-17T082319.png
security:
- kind: authentication
  name: Termius Authentication
  slug: termius-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Termius Domain Security
  slug: termius-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Termius Vulnerability Disclosure
  slug: termius-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Termius Trust Center
  slug: termius-trust-center
  summary_line: SOC 2
skill_count: 3
skills:
- name: Create a group and add a host to it
  slug: termius-create-group-and-host
- name: Create a host in a Termius vault
  slug: termius-create-host
- name: Delete a host from a Termius vault
  slug: termius-delete-host
slug: termius
tags:
- Company
- Enterprise Saas
- SSH
- SSH Client
- Terminal
- Developer Tools
- DevOps
- Infrastructure
- Security
- Remote Access
website: https://termius.com/
---
