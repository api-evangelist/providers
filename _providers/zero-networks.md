---
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
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.8
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://portal.zeronetworks.com/api/v1
  baseurl_source: declared
  description: 'The Zero Networks platform REST API, exposing the segmentation and identity control surface of the Zero Networks console: assets and asset protection state, inbound and outbound segmentation rules, MF'
  name: Zero Networks Platform API
  slug: zero-networks-platform
artifact_total: 6
asyncapis:
- description: ''
  name: Zero Networks Webhooks
  slug: zero-networks-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zero-networks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zeronetworks.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.zeronetworks.com/
- group: operate
  title: ''
  type: Support
  url: https://support.zeronetworks.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://zeronetworks.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zeronetworks
- group: start
  title: ''
  type: SignUp
  url: https://portal.zeronetworks.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zeronetworks.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zeronetworks.com/files/legal/Zero-Networks-Service-Agreement.pdf
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zeronetworks.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zero-networks-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/zero-networks-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/zero-networks-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/zero-networks-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zero-networks-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/zero-networks-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zero-networks-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zero-networks-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/zero-networks-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zero-networks-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: X-WellKnownProbe
  url: well-known/zero-networks-well-known.yml
created: '2026-09-05'
description: Zero Networks is an Israeli-American network security company whose Segment platform delivers automated, agentless microsegmentation and identity segmentation for enterprise networks. It builds a host-based firewall "bubble" around every asset, learns normal east-west traffic for 30 days, then auto-generates least-privilege allow rules and closes privileged ports behind just-in-time multi-factor authentication — extending MFA to protocols such as RDP, SSH, SMB, WinRM and RPC that were never designed for it. The platform also covers identity segmentation for admin and service accounts, Kubernetes segmentation, OT/IoT assets, and a ZTNA-style secure remote access product that replaces VPN. Zero Networks operates a customer-facing REST API at portal.zeronetworks.com/api/v1 secured with an Authorization API token issued from the console, and publishes a first-party OpenAPI 3.0.1 contract plus Speakeasy-generated Python, PowerShell and Terraform clients from its own GitHub organization.
image: https://zeronetworks.com/favicon.ico
layout: provider
modified: '2026-09-05'
name: Zero Networks
nav: Providers
network: true
overview: 'Zero Networks publishes 1 API on the [APIs.io](https://apis.io/) network: Platform API. Tagged areas include Security, Network Security, Microsegmentation, Zero Trust, and Identity.


  The Zero Networks catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zero Networks'' developer surface includes support, engineering blog, signup flow, and 19 more developer resources.'
plans:
- name: Zero Networks Plans Pricing
  plan_count: 0
  slug: zero-networks-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Zero Networks Rate Limits
  slug: zero-networks-rate-limits
score:
  band: developing
  composite: 45.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 65.8
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: Zero Networks Authentication
  slug: zero-networks-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Zero Networks Domain Security
  slug: zero-networks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zero-networks
tags:
- Security
- Network Security
- Microsegmentation
- Zero Trust
- Identity
- Multi-Factor Authentication
- Segmentation
- ZTNA
- Kubernetes
- Cybersecurity
website: https://zeronetworks.com/
---
