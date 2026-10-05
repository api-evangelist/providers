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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.9
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Octopus Deploy Agentic Access
  operation_count: 6
  slug: octopus-deploy-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- description: REST API exposing projects, environments, releases, deployments, runbooks, accounts, certificates, tenants, variables, packages, and tasks managed by an Octopus Deploy server or Octopus Cloud instance
  name: Octopus Deploy REST API
  slug: rest-api
- baseURL: https://your-octopus.example/api
  baseurl_source: declared
  description: The Accounts API from Octopus Deploy — 1 operation(s) for accounts.
  name: Octopus Deploy Accounts API
  slug: octopus-deploy-accounts-api
- baseURL: https://your-octopus.example/api
  baseurl_source: declared
  description: The Environments API from Octopus Deploy — 1 operation(s) for environments.
  name: Octopus Deploy Environments API
  slug: octopus-deploy-environments-api
- baseURL: https://your-octopus.example/api
  baseurl_source: declared
  description: The Feeds API from Octopus Deploy — 1 operation(s) for feeds.
  name: Octopus Deploy Feeds API
  slug: octopus-deploy-feeds-api
- baseURL: https://your-octopus.example/api
  baseurl_source: declared
  description: The Machines API from Octopus Deploy — 1 operation(s) for machines.
  name: Octopus Deploy Machines API
  slug: octopus-deploy-machines-api
- baseURL: https://your-octopus.example/api
  baseurl_source: declared
  description: The Projects API from Octopus Deploy — 1 operation(s) for projects.
  name: Octopus Deploy Projects API
  slug: octopus-deploy-projects-api
- baseURL: https://your-octopus.example/api
  baseurl_source: declared
  description: The Root API from Octopus Deploy — 1 operation(s) for root.
  name: Octopus Deploy Root API
  slug: octopus-deploy-root-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Octopus Deploy REST Accounts API
  slug: open-octopus-deploy-accounts-api
- collection_type: open
  name: Octopus Deploy REST Accounts Environments API
  slug: open-octopus-deploy-environments-api
- collection_type: open
  name: Octopus Deploy REST Accounts Feeds API
  slug: open-octopus-deploy-feeds-api
- collection_type: open
  name: Octopus Deploy REST Accounts Machines API
  slug: open-octopus-deploy-machines-api
- collection_type: open
  name: Octopus Deploy REST Accounts Projects API
  slug: open-octopus-deploy-projects-api
- collection_type: open
  name: Octopus Deploy REST Accounts Root API
  slug: open-octopus-deploy-root-api
- collection_type: open
  name: Octopus Deploy REST API
  slug: open-octopus-deploy
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/octopus-deploy/refs/heads/main/well-known/octopus-deploy-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/octopus-deploy-status-security.txt
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/octopus-deploy/refs/heads/main/rate-limits/octopus-deploy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/octopus-deploy-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/octopus-deploy/refs/heads/main/plans/octopus-deploy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/octopus-deploy-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/octopus-deploy/refs/heads/main/rules/octopus-deploy-rules.yml
  title: ''
  type: Spectral
  url: rules/octopus-deploy-rules.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/octopus-deploy/refs/heads/main/cli/octopus-deploy-cli.yml
  title: ''
  type: CLI
  url: cli/octopus-deploy-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://octopus.com/company/trust
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/octopus-deploy/refs/heads/main/conformance/octopus-deploy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/octopus-deploy-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/octopus-deploy/refs/heads/main/llms/octopus-deploy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/octopus-deploy-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/octopus-deploy/refs/heads/main/well-known/octopus-deploy-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/octopus-deploy-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/octopus-deploy/refs/heads/main/well-known/octopus-deploy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/octopus-deploy-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/octopus-deploy/refs/heads/main/hosts/octopus-deploy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/octopus-deploy-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/octopus-deploy/refs/heads/main/packages/octopus-deploy-packages.yml
  title: ''
  type: Packages
  url: packages/octopus-deploy-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://octopus.com/lp/confirm/terms-updates-confirmation
- group: operate
  title: ''
  type: StatusPage
  url: https://status.octopus.com/
- group: auth
  title: ''
  type: Security
  url: https://octopus.com/devops/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://octopus.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://octopus.com/news
- group: other
  title: ''
  type: Leadership
  url: https://octopus.com/devops/reading-list/leadership/
- group: operate
  title: ''
  type: ChangeLog
  url: https://octopus.com/docs/releases
- group: start
  title: ''
  type: GettingStarted
  url: https://octopus.com/docs/octopus-ai/claude-agent-step/getting-started
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/octopus-deploy/refs/heads/main/agentic-access/octopus-deploy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/octopus-deploy-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/octopus-deploy/refs/heads/main/security/octopus-deploy-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/octopus-deploy-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/octopus-deploy/refs/heads/main/security/octopus-deploy-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/octopus-deploy-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/octopus-deploy/refs/heads/main/security/octopus-deploy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/octopus-deploy-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/octopus-deploy/refs/heads/main/authentication/octopus-deploy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/octopus-deploy-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/octopus-deploy/refs/heads/main/scopes/octopus-deploy-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/octopus-deploy-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/octopus-deploy
- group: company
  title: ''
  type: Website
  url: https://octopus.com
- group: docs
  title: ''
  type: Documentation
  url: https://octopus.com/docs
- group: docs
  title: ''
  type: API Documentation
  url: https://octopus.com/docs/octopus-rest-api
- group: commercial
  title: ''
  type: Pricing
  url: https://octopus.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://octopus.com/start
- group: operate
  title: ''
  type: Support
  url: https://octopus.com/support
- group: company
  title: ''
  type: Blog
  url: https://octopus.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OctopusDeploy
- group: build
  title: ''
  type: CLI
  url: https://github.com/OctopusDeploy/cli
- group: build
  title: ''
  type: SDKs
  url: https://github.com/OctopusDeploy/OctopusClients
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/OctopusDeploy/mcp-server
- group: agent
  title: ''
  type: LlmsText
  url: https://octopus.com/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/octopus-deploy/refs/heads/main/capabilities/octopus-deploy-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/octopus-deploy-capability-edges.yml
coverage:
  checked: '2026-10-04'
  detail: Documentation pages exist but no OpenAPI or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://octopus.com/docs/octopus-rest-api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-05-11'
description: Octopus Deploy is a continuous delivery and release orchestration platform for managing deployments across development, test, and production environments to virtual machines, containers, Kubernetes, and cloud services. The platform handles environments, tenants, runbooks, release promotion, and approvals for both regulated and high-velocity teams. The Octopus REST API provides programmatic access to projects, environments, releases, deployments, runbooks, variables, accounts, and tasks via API-key authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/octopus-deploy.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Octopus Deploy
nav: Providers
network: true
overview: 'Octopus Deploy publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Environments API, Feeds API, and 4 more. Tagged areas include DevOps, Continuous Delivery, Deployment Automation, Release Management, and Runbooks.


  The Octopus Deploy catalog on APIs.io includes 1 Spectral governance ruleset.


  Octopus Deploy''s developer surface includes CLI, changelog, getting-started guide, authentication, documentation, pricing, signup flow, and 33 more developer resources.'
plans:
- name: Octopus Deploy Plans Pricing
  plan_count: 3
  slug: octopus-deploy-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 2
  name: Octopus Deploy Rate Limits
  slug: octopus-deploy-rate-limits
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Octopus Deploy API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: octopus-deploy-rules
scopes:
- name: Octopus Deploy Scopes
  scope_count: 1
  slug: octopus-deploy-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: strong
  composite: 61.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 61.5
    catalog_earned_first_party: 20.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 27.5
  facets:
    access_clarity: 85.5
    contract_governance: 31.8
    contract_quality: 40.4
    developer_ergonomics: 50.0
    discoverability: 76.8
    operational_transparency: 65.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 34.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
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
    score: 45.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/octopus-deploy/refs/heads/main/screenshots/octopus-deploy-2026-06-20T190613.png
security:
- kind: authentication
  name: Octopus Deploy Authentication
  slug: octopus-deploy-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Octopus Deploy Domain Security
  slug: octopus-deploy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Octopus Deploy Vulnerability Disclosure
  slug: octopus-deploy-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Octopus Deploy Trust Center
  slug: octopus-deploy-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: octopus-deploy
tags:
- DevOps
- Continuous Delivery
- Deployment Automation
- Release Management
- Runbooks
- CI/CD
- Developer Tools
- Australia
website: https://octopus.com
---
