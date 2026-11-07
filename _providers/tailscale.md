---
access_model:
  confidence: high
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
  - security
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Tailscale Agentic Access
  operation_count: 45
  slug: tailscale-agentic-access
  summary_line: 45 operations · 26 acting
api_count: 1
apis:
- baseURL: https://api.tailscale.com/api/v2
  baseurl_source: declared
  description: The Devices API from Tailscale — 12 operation(s) for devices.
  name: Tailscale Devices API
  slug: tailscale-devices-api
- baseURL: https://api.tailscale.com/api/v2
  baseurl_source: declared
  description: The DNS API from Tailscale — 3 operation(s) for dns.
  name: Tailscale DNS API
  slug: tailscale-dns-api
- baseURL: https://api.tailscale.com/api/v2
  baseurl_source: declared
  description: The Invites API from Tailscale — 7 operation(s) for invites.
  name: Tailscale Invites API
  slug: tailscale-invites-api
- baseURL: https://api.tailscale.com/api/v2
  baseurl_source: declared
  description: The Keys API from Tailscale — 2 operation(s) for keys.
  name: Tailscale Keys API
  slug: tailscale-keys-api
- baseURL: https://api.tailscale.com/api/v2
  baseurl_source: declared
  description: The Logging API from Tailscale — 4 operation(s) for logging.
  name: Tailscale Logging API
  slug: tailscale-logging-api
- baseURL: https://api.tailscale.com/api/v2
  baseurl_source: declared
  description: The Policy API from Tailscale — 2 operation(s) for policy.
  name: Tailscale Policy API
  slug: tailscale-policy-api
- baseURL: https://api.tailscale.com/api/v2
  baseurl_source: declared
  description: The Tailnet API from Tailscale — 2 operation(s) for tailnet.
  name: Tailscale Tailnet API
  slug: tailscale-tailnet-api
artifact_total: 24
collections:
- collection_type: open
  name: Tailscale REST Devices API
  slug: open-tailscale-devices-api
- collection_type: open
  name: Tailscale REST Devices DNS API
  slug: open-tailscale-dns-api
- collection_type: open
  name: Tailscale REST Devices Invites API
  slug: open-tailscale-invites-api
- collection_type: open
  name: Tailscale REST Devices Keys API
  slug: open-tailscale-keys-api
- collection_type: open
  name: Tailscale REST Devices Logging API
  slug: open-tailscale-logging-api
- collection_type: open
  name: Tailscale REST Devices Policy API
  slug: open-tailscale-policy-api
- collection_type: open
  name: Tailscale REST Devices Tailnet API
  slug: open-tailscale-tailnet-api
- collection_type: open
  name: Tailscale REST API
  slug: open-tailscale
common:
- group: operate
  href: https://artifacts.apis.io/tailscale/rate-limits/tailscale-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tailscale-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/tailscale/plans/tailscale-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tailscale-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/tailscale/capabilities/tailscale-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/tailscale-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/tailscale/agentic-access/tailscale-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tailscale-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/tailscale/security/tailscale-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/tailscale-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/tailscale/security/tailscale-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tailscale-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/tailscale/security/tailscale-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tailscale-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/tailscale/authentication/tailscale-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tailscale-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tailscale
- group: company
  title: ''
  type: Website
  url: https://tailscale.com
- group: docs
  title: ''
  type: Documentation
  url: https://tailscale.com/kb/
- group: commercial
  title: ''
  type: Pricing
  url: https://tailscale.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://login.tailscale.com/start
- group: build
  title: ''
  type: GitHub
  url: https://github.com/tailscale/tailscale
- group: company
  title: ''
  type: Blog
  url: https://tailscale.com/blog/index.xml
created: '2026-05-11'
description: Tailscale is a zero-config mesh VPN built on WireGuard that creates secure private networks between devices, users, and services with identity-based access controls, Access Control Lists (ACLs), DNS, and device sharing. Tailscale eliminates traditional VPN complexity with peer-to-peer connectivity and SSO-based authentication. The Tailscale REST API provides programmatic control over tailnets, devices, users, ACLs, and keys using API tokens or OAuth client credentials.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tailscale.png
layout: provider
modified: '2026-05-11'
name: Tailscale
nav: Providers
network: true
overview: 'Tailscale publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Devices API, DNS API, Invites API, and 4 more. Tagged areas include VPN, Mesh Networking, WireGuard, Zero Trust, and Networking.


  The Tailscale catalog on APIs.io includes 1 Spectral governance ruleset.


  Tailscale''s developer surface includes authentication, documentation, pricing, signup flow, GitHub presence, engineering blog, and 9 more developer resources.'
plans:
- name: Tailscale Plans Pricing
  plan_count: 6
  slug: tailscale-plans-pricing
- name: Tailscale Price Estimates
  plan_count: 0
  slug: tailscale-price-estimates
random_paper: 10
rate_limits:
- limit_count: 1
  name: Tailscale Rate Limits
  slug: tailscale-rate-limits
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Tailscale API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: tailscale-rules
score:
  band: developing
  composite: 42.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 61.5
    catalog_earned_first_party: 20.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 13.6
    contract_quality: 45.3
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 36.8
  previous_composite: 42.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/tailscale/tailscale-2026-06-20T194858.png
security:
- kind: authentication
  name: Tailscale Authentication
  slug: tailscale-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Tailscale Domain Security
  slug: tailscale-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tailscale Vulnerability Disclosure
  slug: tailscale-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Tailscale Trust Center
  slug: tailscale-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA
slug: tailscale
tags:
- VPN
- Mesh Networking
- WireGuard
- Zero Trust
- Networking
- Identity
website: https://tailscale.com
---
