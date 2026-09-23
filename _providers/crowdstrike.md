---
access_model:
  confidence: medium
  label: Paid (free trial)
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.1
  scored_at: '2026-09-23'
api_count: 2
apis:
- description: The CrowdStrike Falcon API — 1,463 documented operations across 128 service collections covering hosts, detections, incidents, real-time response, threat intelligence, cloud and container security, id
  name: CrowdStrike API
  slug: crowdstrike-api
- description: CrowdStrike's first-party open-source MCP server. Self-hosted (uvx/pip/Docker/Bedrock/Cloud Run) and authenticated with the operator's own Falcon API client; 166 tools across 28 modules. A separate Cr
  name: Falcon MCP Server
  slug: falcon-mcp
artifact_total: 12
asyncapis:
- description: ''
  name: Crowdstrike Event Streams
  slug: crowdstrike-event-streams
common:
- group: company
  title: ''
  type: Website
  url: https://www.crowdstrike.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.crowdstrike.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.crowdstrike.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.crowdstrike.com/api-reference/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.crowdstrike.com/sdks/go/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://supportportal.crowdstrike.com/
- group: company
  title: ''
  type: Blog
  url: https://www.crowdstrike.com/blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CrowdStrike
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/crowdstrike
- group: company
  title: ''
  type: Newsroom
  url: https://www.crowdstrike.com/en-us/press-releases/
- group: other
  title: ''
  type: Leadership
  url: https://www.crowdstrike.com/en-us/about-us/executive-team/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.crowdstrike.com/en-us/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.crowdstrike.com/en-us/products/trials/try-falcon/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.crowdstrike.com/en-us/legal/website-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.crowdstrike.com/en-us/legal/privacy-notice/
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.crowdstrike.com/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/crowdstrike/refs/heads/main/llms/crowdstrike-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crowdstrike-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/crowdstrike/refs/heads/main/packages/crowdstrike-packages.yml
  title: ''
  type: Packages
  url: packages/crowdstrike-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/crowdstrike/refs/heads/main/packages/crowdstrike-packages.yml
  title: ''
  type: SDKs
  url: packages/crowdstrike-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/crowdstrike/refs/heads/main/cli/crowdstrike-cli.yml
  title: ''
  type: CLI
  url: cli/crowdstrike-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crowdstrike/refs/heads/main/components/crowdstrike-components.yml
  title: ''
  type: Components
  url: components/crowdstrike-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/crowdstrike/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/crowdstrike/refs/heads/main/mcp/crowdstrike-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/crowdstrike-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/crowdstrike/refs/heads/main/mcp/crowdstrike-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/crowdstrike-tool-crosswalk.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crowdstrike/refs/heads/main/authentication/crowdstrike-authentication.yml
  title: ''
  type: Authentication
  url: authentication/crowdstrike-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crowdstrike/refs/heads/main/scopes/crowdstrike-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/crowdstrike-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crowdstrike/refs/heads/main/conventions/crowdstrike-conventions.yml
  title: ''
  type: Conventions
  url: conventions/crowdstrike-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crowdstrike/refs/heads/main/errors/crowdstrike-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/crowdstrike-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/crowdstrike/refs/heads/main/rate-limits/crowdstrike-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/crowdstrike-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/crowdstrike/refs/heads/main/plans/crowdstrike-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/crowdstrike-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crowdstrike/refs/heads/main/lifecycle/crowdstrike-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/crowdstrike-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/crowdstrike/refs/heads/main/changelog/crowdstrike-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/crowdstrike-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crowdstrike/refs/heads/main/conformance/crowdstrike-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crowdstrike-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.crowdstrike.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crowdstrike/refs/heads/main/security/crowdstrike-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/crowdstrike-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crowdstrike/refs/heads/main/security/crowdstrike-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/crowdstrike-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.crowdstrike.com/en-us/report-a-security-bug/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crowdstrike/refs/heads/main/well-known/crowdstrike-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/crowdstrike-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/crowdstrike/refs/heads/main/well-known/crowdstrike-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/crowdstrike-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crowdstrike/refs/heads/main/security/crowdstrike-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crowdstrike-domain-security.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crowdstrike/refs/heads/main/regulatory/crowdstrike-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/crowdstrike-regulatory-posture.yml
- group: commercial
  title: ''
  type: GlobalPrivacyControl
  url: https://www.crowdstrike.com/en-us/legal/privacy-notice/
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://www.crowdstrike.com/en-us/legal/privacy-notice/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crowdstrike/refs/heads/main/asyncapi/crowdstrike-event-streams.yml
  title: ''
  type: StreamingEndpoint
  url: asyncapi/crowdstrike-event-streams.yml
created: '2026-04-19'
description: 'CrowdStrike is a US cybersecurity company and Fortune 1000 constituent whose Falcon platform delivers endpoint, cloud, identity and data protection from a single cloud-native agent. Its developer surface is substantial and public: a 1,463-operation OAuth2 REST API spanning 128 service collections, documented operation by operation on developer.crowdstrike.com, with 187 named permission scopes; six official SDKs (Python, PowerShell, Go, TypeScript/JavaScript, Rust, Ruby); a Terraform provider for Configuration as Code; Falcon Foundry, an app platform with its own CLI; a first-party open-source MCP server (falcon-mcp) exposing 166 agent tools across 28 modules; and a published set of Agent Skills for building Foundry apps. CrowdStrike does not publish an OpenAPI document, and API access requires a Falcon subscription — the API itself is included in every paid bundle.'
finops:
- name: Crowdstrike Finops
  service_category: Cybersecurity
  slug: crowdstrike-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crowdstrike.png
layout: provider
mcp_servers:
- description: 'CrowdStrike publishes falcon-mcp, a first-party open-source MCP server that connects agents to the Falcon platform. It is a LOCAL STDIO product: installed with uv/pip/uvx and run by the operator, auth'
  name: io.github.CrowdStrike/falcon-mcp
  slug: iogithubcrowdstrikefalcon-mcp
modified: '2026-09-19'
name: CrowdStrike
nav: Providers
network: true
overview: 'CrowdStrike publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cybersecurity, Endpoint Security, EDR, Threat Intelligence, and Cloud Security.


  The CrowdStrike catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  CrowdStrike''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 37 more developer resources.'
plans:
- name: Crowdstrike Plans Pricing
  plan_count: 6
  slug: crowdstrike-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 2
  name: Crowdstrike Rate Limits
  slug: crowdstrike-rate-limits
scopes:
- name: Crowdstrike Scopes
  scope_count: 187
  slug: crowdstrike-scopes
  summary_line: 187 scopes
score:
  band: strong
  composite: 62.4
  coverage:
    artifact_dirs: 24
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 78.6
    discoverability: 75.9
    operational_transparency: 50.0
  previous_composite: 62.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/crowdstrike/refs/heads/main/screenshots/crowdstrike-2026-06-20T175254.png
security:
- kind: authentication
  name: Crowdstrike Authentication
  slug: crowdstrike-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Crowdstrike Domain Security
  slug: crowdstrike-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Crowdstrike Vulnerability Disclosure
  slug: crowdstrike-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Crowdstrike Trust Center
  slug: crowdstrike-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, PCI DSS, FedRAMP, GDPR, CSA STAR
slug: crowdstrike
tags:
- Cybersecurity
- Endpoint Security
- EDR
- Threat Intelligence
- Cloud Security
- Identity Protection
- Vulnerability Management
- SIEM
- Security Operations
- MCP
website: https://www.crowdstrike.com
---
