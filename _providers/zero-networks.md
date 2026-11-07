---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://portal.zeronetworks.com/api/v1
  baseurl_source: declared
  description: API calls related to AE Exclusions.
  name: Zero Networks AE Exclusions API
  slug: zero-networks-ae-exclusions-api
- baseURL: https://portal.zeronetworks.com/api/v1
  baseurl_source: declared
  description: API calls related to Assets.
  name: Zero Networks Assets API
  slug: zero-networks-assets-api
- baseURL: https://portal.zeronetworks.com/api/v1
  baseurl_source: declared
  description: API calls related to Custom Groups.
  name: Zero Networks Groups Custom API
  slug: zero-networks-groups-custom-api
- baseURL: https://portal.zeronetworks.com/api/v1
  baseurl_source: declared
  description: The Internal Access Policy API from Zero Networks — 2 operation(s) for internal access policy.
  name: Zero Networks Internal Access Policy API
  slug: zero-networks-internal-access-policy-api
- baseURL: https://portal.zeronetworks.com/api/v1
  baseurl_source: declared
  description: API calls related to Inbound MFA policies.
  name: Zero Networks MFA Inbound API
  slug: zero-networks-mfa-inbound-api
- baseURL: https://portal.zeronetworks.com/api/v1
  baseurl_source: declared
  description: API calls related to Outbound MFA policies.
  name: Zero Networks MFA Outbound API
  slug: zero-networks-mfa-outbound-api
- baseURL: https://portal.zeronetworks.com/api/v1
  baseurl_source: declared
  description: API calls related to Inbound rules.
  name: Zero Networks Rules Inbound API
  slug: zero-networks-rules-inbound-api
- baseURL: https://portal.zeronetworks.com/api/v1
  baseurl_source: declared
  description: API calls related to Outbound rules.
  name: Zero Networks Rules Outbound API
  slug: zero-networks-rules-outbound-api
- baseURL: https://portal.zeronetworks.com/api/v1
  baseurl_source: declared
  description: API calls related to RPC Rules
  name: Zero Networks Rules RPC API
  slug: zero-networks-rules-rpc-api
artifact_total: 19
asyncapis:
- description: ''
  name: Zero Networks Webhooks
  slug: zero-networks-webhooks
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://zeronetworks.com/feed
- group: other
  href: https://artifacts.apis.io/zero-networks/capabilities/zero-networks-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/zero-networks-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/zero-networks/overlays/zero-networks-platform-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zero-networks-platform-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/zero-networks/security/zero-networks-domain-security.yml
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
  href: https://artifacts.apis.io/zero-networks/llms/zero-networks-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zero-networks-llms.txt
- group: build
  href: https://artifacts.apis.io/zero-networks/packages/zero-networks-packages.yml
  title: ''
  type: Packages
  url: packages/zero-networks-packages.yml
- group: build
  href: https://artifacts.apis.io/zero-networks/packages/zero-networks-packages.yml
  title: ''
  type: SDKs
  url: packages/zero-networks-packages.yml
- group: agent
  href: https://artifacts.apis.io/zero-networks/mcp/zero-networks-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/zero-networks-mcp.yml
- group: design
  href: https://artifacts.apis.io/zero-networks/conformance/zero-networks-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zero-networks-conformance.yml
- group: auth
  href: https://artifacts.apis.io/zero-networks/conformance/zero-networks-conformance.yml
  title: ''
  type: Compliance
  url: conformance/zero-networks-conformance.yml
- group: design
  href: https://artifacts.apis.io/zero-networks/lifecycle/zero-networks-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/zero-networks-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/zero-networks/conventions/zero-networks-conventions.yml
  title: ''
  type: Conventions
  url: conventions/zero-networks-conventions.yml
- group: commercial
  href: https://artifacts.apis.io/zero-networks/plans/zero-networks-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zero-networks-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/zero-networks/rate-limits/zero-networks-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/zero-networks-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/zero-networks/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/zero-networks/well-known/zero-networks-well-known.yml
  title: ''
  type: X-WellKnownProbe
  url: well-known/zero-networks-well-known.yml
created: '2026-09-05'
description: Zero Networks is an Israeli-American network security company whose Segment platform delivers automated, agentless microsegmentation and identity segmentation for enterprise networks. It builds a host-based firewall "bubble" around every asset, learns normal east-west traffic for 30 days, then auto-generates least-privilege allow rules and closes privileged ports behind just-in-time multi-factor authentication — extending MFA to protocols such as RDP, SSH, SMB, WinRM and RPC that were never designed for it. The platform also covers identity segmentation for admin and service accounts, Kubernetes segmentation, OT/IoT assets, and a ZTNA-style secure remote access product that replaces VPN. Zero Networks operates a customer-facing REST API at portal.zeronetworks.com/api/v1 secured with an Authorization API token issued from the console, and publishes a first-party OpenAPI 3.0.1 contract plus Speakeasy-generated Python, PowerShell and Terraform clients from its own GitHub organization.
finops:
- has_sources: true
  method: derived
  name: Zero Networks Finops
  primary_unit: ''
  service_category: ''
  slug: zero-networks-finops
  template: true
image: https://zeronetworks.com/favicon.ico
layout: provider
modified: '2026-10-06'
name: Zero Networks
nav: Providers
network: true
overview: 'Zero Networks publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including AE Exclusions API, Assets API, Groups Custom API, and 6 more. Tagged areas include Security, Network Security, Microsegmentation, Zero Trust, and Identity.


  The Zero Networks catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Zero Networks'' developer surface includes support, engineering blog, signup flow, and 22 more developer resources.'
plans:
- name: Zero Networks Plans Pricing
  plan_count: 0
  slug: zero-networks-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Zero Networks Rate Limits
  slug: zero-networks-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Zero Networks API Rules
  rule_count: 61
  severity_counts:
    error: 54
    hint: 0
    info: 2
    warn: 5
  slug: zero-networks-rules
score:
  band: developing
  composite: 46.9
  coverage:
    artifact_dirs: 26
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 31.8
    contract_quality: 60.1
    developer_ergonomics: 37.5
    discoverability: 73.2
    operational_transparency: 26.3
  previous_composite: 46.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/zero-networks/zero-networks-2026-10-11T194301.png
security:
- kind: authentication
  name: Zero Networks Authentication
  slug: zero-networks-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Zero Networks Domain Security
  slug: zero-networks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: zero-networks-apply-mfa-policy
  slug: zero-networks-apply-mfa-policy
- name: zero-networks-manage-custom-groups
  slug: zero-networks-manage-custom-groups
- name: zero-networks-segment-an-asset
  slug: zero-networks-segment-an-asset
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
