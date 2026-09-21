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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.1
  scored_at: '2026-09-20'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Dashlane Agentic Access
  operation_count: 6
  slug: dashlane-agentic-access
  summary_line: 6 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api.dashlane.com/public
  baseurl_source: declared
  description: The Teams API from Dashlane — 4 operation(s) for teams.
  name: Dashlane Teams API
  slug: dashlane-teams-api
- baseURL: https://api.dashlane.com/public
  baseurl_source: declared
  description: The Time API from Dashlane — 1 operation(s) for time.
  name: Dashlane Time API
  slug: dashlane-time-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Dashlane public API documentation Teams API
  slug: open-dashlane-teams-api
- collection_type: open
  name: Dashlane public API documentation Teams Time API
  slug: open-dashlane-time-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dashlane/refs/heads/main/overlays/dashlane-public-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dashlane-public-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dashlane/refs/heads/main/agentic-access/dashlane-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dashlane-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dashlane/refs/heads/main/authentication/dashlane-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dashlane-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dashlane/refs/heads/main/security/dashlane-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dashlane-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/dashlane?type=team
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dashlane/refs/heads/main/security/dashlane-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dashlane-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dashlane/refs/heads/main/well-known/dashlane-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dashlane-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dashlane/refs/heads/main/well-known/dashlane-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dashlane-security.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/dashlane/refs/heads/main/packages/dashlane-packages.yml
  title: ''
  type: Packages
  url: packages/dashlane-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/dashlane/refs/heads/main/packages/dashlane-packages.yml
  title: ''
  type: SDKs
  url: packages/dashlane-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/dashlane/refs/heads/main/cli/dashlane-cli.yml
  title: ''
  type: CLI
  url: cli/dashlane-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dashlane/refs/heads/main/mcp/dashlane-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/dashlane-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dashlane/refs/heads/main/llms/dashlane-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dashlane-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dashlane/refs/heads/main/conformance/dashlane-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dashlane-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dashlane/refs/heads/main/errors/dashlane-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dashlane-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dashlane/refs/heads/main/lifecycle/dashlane-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dashlane-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dashlane.com
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dashlane/refs/heads/main/conventions/dashlane-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dashlane-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dashlane/refs/heads/main/data-model/dashlane-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dashlane-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dashlane/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cli.dashlane.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dashlane.github.io/public-api-documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://dashlane.github.io/public-api-documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://cli.dashlane.com/
- group: operate
  title: ''
  type: Support
  url: https://support.dashlane.com/
- group: company
  title: ''
  type: Blog
  url: https://www.dashlane.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Dashlane
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dashlane.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.dashlane.com/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dashlane.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dashlane.com/privacy
- group: company
  title: ''
  type: Website
  url: https://www.dashlane.com/
created: '2026-07-17'
description: Dashlane is a password manager and credential-security platform for individuals, families, and enterprises, protecting against credential reuse, phishing, and account takeover with zero-knowledge encryption, passkey support, and AI-powered phishing detection. For developers, Dashlane publishes a read-only Public API (OpenAPI 3.0) that returns real-time team data — member roles/status/usage metrics, activated devices, and password-health analytics (weak, reused, compromised credentials) — authenticated with a bearer DLP token. Dashlane also ships an open-source CLI (dcli), a GitHub Action for injecting vault secrets into CI/CD, SCIM provisioning, and SSO federation.
image: https://www.dashlane.com/favicon.ico
layout: provider
modified: '2026-07-18'
name: Dashlane
nav: Providers
network: true
overview: 'Dashlane publishes 2 APIs on the [APIs.io](https://apis.io/) network: Teams API and Time API. Tagged areas include Company, Cybersecurity, Password Management, Identity, and Security.


  Dashlane''s developer surface includes authentication, CLI, documentation, API reference, getting-started guide, support, engineering blog, and 25 more developer resources.'
random_paper: 18
score:
  band: developing
  composite: 48.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 54.4
    developer_ergonomics: 73.2
    discoverability: 75.9
    operational_transparency: 28.9
  previous_composite: 48.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/dashlane/refs/heads/main/screenshots/dashlane-2026-07-25T211226.png
security:
- kind: authentication
  name: Dashlane Authentication
  slug: dashlane-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Dashlane Domain Security
  slug: dashlane-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dashlane Vulnerability Disclosure
  slug: dashlane-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: dashlane
tags:
- Company
- Cybersecurity
- Password Management
- Identity
- Security
- Credential Monitoring
- Secrets Management
website: https://www.dashlane.com/
---
