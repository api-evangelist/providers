---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Cloudflare Zero Trust (formerly Cloudflare for Teams / Cloudflare Access) provides ZTNA, secure web gateway, browser isolation, CASB, and DLP through a single global edge platform. The Cloudflare API '
  name: Cloudflare Zero Trust API
  slug: cloudflare-zero-trust
- description: 'Zscaler Private Access is a cloud-native ZTNA service that connects authenticated users to private applications without exposing them to the internet or placing them on the corporate network. The ZPA '
  name: Zscaler Private Access (ZPA) API
  slug: zscaler-zpa
- description: Netskope Private Access provides ZTNA as part of the Netskope SASE platform, brokering authenticated access to private applications across cloud and on-premises. The Netskope REST API surfaces operati
  name: Netskope Private Access API
  slug: netskope-private-access
- description: Palo Alto Networks Prisma Access offers cloud-delivered ZTNA, SWG, and FWaaS as part of the Prisma SASE platform. The Prisma Access REST API exposes operations on remote networks, mobile users, securi
  name: Palo Alto Prisma Access (Prisma SASE) API
  slug: palo-alto-prisma-access
- description: Tailscale is a WireGuard-based mesh-VPN ZTNA platform that exposes a REST API for managing devices, ACL policies, tailnet keys, DNS, and audit logs. It implements identity-based device-to-device tunne
  name: Tailscale API
  slug: tailscale-api
- description: Twingate is a software-defined ZTNA platform that exposes a GraphQL Admin API for managing remote networks, resources, groups, users, service accounts, and connectors.
  name: Twingate API
  slug: twingate-api
- baseURL: https://api.cloudflare.com/client/v4
  baseurl_source: spec
  description: Account-level WARP deployment groups.
  name: Zero Trust Network Access Deployment Groups API
  slug: zero-trust-network-access-deployment-groups-api
- baseURL: https://api.cloudflare.com/client/v4
  baseurl_source: spec
  description: WARP devices enrolled in Zero Trust.
  name: Zero Trust Network Access Devices API
  slug: zero-trust-network-access-devices-api
- baseURL: https://api.cloudflare.com/client/v4
  baseurl_source: spec
  description: Digital Experience Monitoring tests.
  name: Zero Trust Network Access DEX Tests API
  slug: zero-trust-network-access-dex-tests-api
- baseURL: https://api.cloudflare.com/client/v4
  baseurl_source: spec
  description: WARP device IP profiles.
  name: Zero Trust Network Access IP Profiles API
  slug: zero-trust-network-access-ip-profiles-api
- baseURL: https://api.cloudflare.com/client/v4
  baseurl_source: spec
  description: Per-user WARP registrations on a device.
  name: Zero Trust Network Access Registrations API
  slug: zero-trust-network-access-registrations-api
- baseURL: https://api.cloudflare.com/client/v4
  baseurl_source: spec
  description: Global Cloudflare WARP override state.
  name: Zero Trust Network Access WARP Override API
  slug: zero-trust-network-access-warp-override-api
artifact_total: 45
collections:
- collection_type: open
  name: Cloudflare Zero Trust Network Access Deployment Groups API
  slug: open-zero-trust-network-access-deployment-groups-api
- collection_type: open
  name: Cloudflare Zero Trust Network Access Devices API
  slug: open-zero-trust-network-access-devices-api
- collection_type: open
  name: Cloudflare Zero Trust Network Access DEX Tests API
  slug: open-zero-trust-network-access-dex-tests-api
- collection_type: open
  name: Cloudflare Zero Trust Network Access IP Profiles API
  slug: open-zero-trust-network-access-ip-profiles-api
- collection_type: open
  name: Cloudflare Zero Trust Network Access Registrations API
  slug: open-zero-trust-network-access-registrations-api
- collection_type: open
  name: Cloudflare Zero Trust Network Access WARP Override API
  slug: open-zero-trust-network-access-warp-override-api
common:
- group: commercial
  href: https://artifacts.apis.io/zero-trust-network-access/plans/zero-trust-network-access-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zero-trust-network-access-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/zero-trust-network-access/rate-limits/zero-trust-network-access-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/zero-trust-network-access-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/zero-trust-network-access/finops/zero-trust-network-access-finops.yml
  title: ''
  type: FinOps
  url: finops/zero-trust-network-access-finops.yml
- group: other
  href: https://artifacts.apis.io/zero-trust-network-access/capabilities/zero-trust-network-access-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/zero-trust-network-access-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/zero-trust-network-access/security/zero-trust-network-access-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/zero-trust-network-access-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/zero-trust-network-access/security/zero-trust-network-access-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zero-trust-network-access-domain-security.yml
- group: docs
  title: Cloudflare - What Is Zero Trust
  type: Documentation
  url: https://www.cloudflare.com/learning/security/glossary/what-is-zero-trust/
- group: docs
  title: Gartner Definition of ZTNA
  type: Documentation
  url: https://www.gartner.com/en/information-technology/glossary/zero-trust-network-access-ztna-
- group: docs
  title: NIST SP 800-207 (ZTA underpinnings of ZTNA)
  type: Documentation
  url: https://nvlpubs.nist.gov/nistpubs/specialpublications/NIST.SP.800-207.pdf
- group: auth
  title: CISA Zero Trust Maturity Model
  type: Compliance
  url: https://www.cisa.gov/zero-trust-maturity-model
- group: start
  title: Cloudflare Zero Trust
  type: Portal
  url: https://www.cloudflare.com/zero-trust/
- group: start
  title: Zscaler Zero Trust Exchange
  type: Portal
  url: https://www.zscaler.com/products-and-solutions/zero-trust-exchange
- group: start
  title: Netskope SASE
  type: Portal
  url: https://www.netskope.com/platform/sase
- group: start
  title: Palo Alto Networks Prisma Access
  type: Portal
  url: https://www.paloaltonetworks.com/sase/access
- group: start
  title: Tailscale
  type: Portal
  url: https://tailscale.com/
- group: start
  title: Twingate
  type: Portal
  url: https://www.twingate.com/
- group: build
  title: Tailscale on GitHub
  type: GitHubOrganization
  url: https://github.com/tailscale
- group: build
  title: WireGuard
  type: GitHubOrganization
  url: https://github.com/WireGuard
- group: docs
  href: https://artifacts.apis.io/zero-trust-network-access/json-schema/zero-trust-network-access-policy-schema.json
  title: ZTNA Access Policy Schema
  type: JSONSchema
  url: json-schema/zero-trust-network-access-policy-schema.json
- group: docs
  href: https://artifacts.apis.io/zero-trust-network-access/json-schema/zero-trust-network-access-application-schema.json
  title: ZTNA Application Schema
  type: JSONSchema
  url: json-schema/zero-trust-network-access-application-schema.json
- group: docs
  href: https://artifacts.apis.io/zero-trust-network-access/json-schema/zero-trust-network-access-device-posture-schema.json
  title: ZTNA Device Posture Schema
  type: JSONSchema
  url: json-schema/zero-trust-network-access-device-posture-schema.json
- group: design
  href: https://artifacts.apis.io/zero-trust-network-access/json-structure/zero-trust-network-access-policy-structure.json
  title: ZTNA Access Policy Structure
  type: JSONStructure
  url: json-structure/zero-trust-network-access-policy-structure.json
- group: design
  href: https://artifacts.apis.io/zero-trust-network-access/json-ld/zero-trust-network-access-context.jsonld
  title: ZTNA JSON-LD Context
  type: JSONLD
  url: json-ld/zero-trust-network-access-context.jsonld
- group: build
  href: https://artifacts.apis.io/zero-trust-network-access/examples/zero-trust-network-access-policy-example.json
  title: ZTNA Access Policy Example
  type: CodeExamples
  url: examples/zero-trust-network-access-policy-example.json
- group: build
  href: https://artifacts.apis.io/zero-trust-network-access/examples/zero-trust-network-access-device-posture-example.json
  title: ZTNA Device Posture Example
  type: CodeExamples
  url: examples/zero-trust-network-access-device-posture-example.json
- group: other
  href: https://artifacts.apis.io/zero-trust-network-access/vocabulary/zero-trust-network-access-vocabulary.yaml
  title: ZTNA Vocabulary
  type: Resources
  url: vocabulary/zero-trust-network-access-vocabulary.yaml
created: '2025'
description: Zero Trust Network Access (ZTNA) is a security framework and product category that grants access to private applications and resources based on identity, device posture, and context, rather than network location. ZTNA replaces the implicit trust of legacy VPNs with explicit per-request verification, creating one-to-one encrypted tunnels between authenticated users and the specific applications they are authorized to use. This topic collects the leading ZTNA vendors, the standards bodies that govern the underlying primitives, and the data schemas used to describe access policies, identities, devices, and resources.
examples:
- key_count: 6
  name: Zero Trust Network Access Device Posture Example
  slug: zero-trust-network-access-device-posture-example
- key_count: 11
  name: Zero Trust Network Access Policy Example
  slug: zero-trust-network-access-policy-example
features:
- description: Access decisions are based on user and workload identity rather than network location.
  name: Identity-Centric Access
- description: One-to-one encrypted connections between authenticated users and specific applications.
  name: Application-Level Tunnels
- description: Continuous evaluation of device health, OS patch level, EDR status, and certificate state.
  name: Device Posture Checks
- description: Policies factor in time, location, risk score, and behavior in addition to identity.
  name: Context-Aware Policy
- description: Private applications are dark to the public internet and not advertised by IP or DNS.
  name: Application Cloaking
- description: Native integration with SAML, OIDC, and modern MFA providers.
  name: SSO and MFA Integration
- description: Lateral movement is prevented by issuing scoped, per-application access.
  name: Microsegmentation
- description: Sessions are reauthenticated and reauthorized as conditions change.
  name: Continuous Authorization
finops:
- has_sources: false
  method: generated
  name: Zero Trust Network Access Finops
  primary_unit: request
  service_category: API
  slug: zero-trust-network-access-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zero-trust-network-access.png
json_schemas:
- name: ZTNA Protected Application
  property_count: 9
  slug: zero-trust-network-access-application
- name: ZTNA Device Posture Profile
  property_count: 6
  slug: zero-trust-network-access-device-posture
- name: ZTNA Access Policy
  property_count: 11
  slug: zero-trust-network-access-policy
json_structures:
- name: Zero Trust Network Access Policy Structure
  property_count: 7
  slug: zero-trust-network-access-policy-structure
jsonld:
- class_count: 24
  name: Zero Trust Network Access Context
  property_count: 0
  slug: zero-trust-network-access-context
layout: provider
modified: '2026-05-03'
name: Zero Trust Network Access
nav: Providers
network: true
overview: 'Zero Trust Network Access publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Deployment Groups API, Devices API, DEX Tests API, and 9 more. Tagged areas include Access Control, Cloud Security, Cybersecurity, Identity and Access Management, and Network Access.


  The Zero Trust Network Access catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Zero Trust Network Access'' developer surface includes documentation, developer portal, code examples, and 23 more developer resources.'
plans:
- name: Zero Trust Network Access Plans Pricing
  plan_count: 3
  slug: zero-trust-network-access-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 5
  name: Zero Trust Network Access Rate Limits
  slug: zero-trust-network-access-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Zero Trust Network Access — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: zero-trust-network-access-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 49.3
    catalog_earned_first_party: 0.0
    catalog_gap: 65.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 54.1
    developer_ergonomics: 38.1
    discoverability: 64.3
    operational_transparency: 21.1
  previous_composite: 35.8
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/zero-trust-network-access/zero-trust-network-access-2026-06-20T201911.png
security:
- kind: domain-security
  name: Zero Trust Network Access Domain Security
  slug: zero-trust-network-access-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Zero Trust Network Access Vulnerability Disclosure
  slug: zero-trust-network-access-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: zero-trust-network-access
tags:
- Access Control
- Cloud Security
- Cybersecurity
- Identity and Access Management
- Network Access
- Network Security
- Security
- VPN Replacement
- Zero Trust
- ZTNA
use_cases:
- description: Replacing legacy site-to-site and remote-access VPNs with identity-aware brokered access.
  name: VPN Replacement
- description: Granting time-bounded, application-scoped access to vendors and contractors.
  name: Third-Party Contractor Access
- description: Enabling acquired companies to reach internal applications without merging networks.
  name: M&A Network Integration
- description: Allowing personal and unmanaged devices to access selected applications under posture rules.
  name: BYOD Access
- description: Brokering jump-host and bastion access to sensitive infrastructure.
  name: Privileged Access
- description: Providing consistent ZTNA across applications hosted in AWS, Azure, GCP, and on-premises.
  name: Multi-Cloud Application Access
website: https://www.cloudflare.com/zero-trust/
---
