---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.2
  scored_at: '2026-08-30'
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
- description: Account-level WARP deployment groups.
  name: Zero Trust Network Access Deployment Groups API
  slug: zero-trust-network-access-deployment-groups-api
- description: WARP devices enrolled in Zero Trust.
  name: Zero Trust Network Access Devices API
  slug: zero-trust-network-access-devices-api
- description: Digital Experience Monitoring tests.
  name: Zero Trust Network Access DEX Tests API
  slug: zero-trust-network-access-dex-tests-api
- description: WARP device IP profiles.
  name: Zero Trust Network Access IP Profiles API
  slug: zero-trust-network-access-ip-profiles-api
- description: Per-user WARP registrations on a device.
  name: Zero Trust Network Access Registrations API
  slug: zero-trust-network-access-registrations-api
- description: Global Cloudflare WARP override state.
  name: Zero Trust Network Access WARP Override API
  slug: zero-trust-network-access-warp-override-api
artifact_total: 47
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zero-trust-network-access-vulnerability-disclosure.yml
- group: auth
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
  title: ZTNA Access Policy Schema
  type: JSONSchema
  url: json-schema/zero-trust-network-access-policy-schema.json
- group: docs
  title: ZTNA Application Schema
  type: JSONSchema
  url: json-schema/zero-trust-network-access-application-schema.json
- group: docs
  title: ZTNA Device Posture Schema
  type: JSONSchema
  url: json-schema/zero-trust-network-access-device-posture-schema.json
- group: design
  title: ZTNA Access Policy Structure
  type: JSONStructure
  url: json-structure/zero-trust-network-access-policy-structure.json
- group: design
  title: ZTNA JSON-LD Context
  type: JSONLD
  url: json-ld/zero-trust-network-access-context.jsonld
- group: build
  title: ZTNA Access Policy Example
  type: CodeExamples
  url: examples/zero-trust-network-access-policy-example.json
- group: build
  title: ZTNA Device Posture Example
  type: CodeExamples
  url: examples/zero-trust-network-access-device-posture-example.json
- group: other
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
- name: Zero Trust Network Access Finops
  service_category: API
  slug: zero-trust-network-access-finops
graphqls:
- description: ''
  name: Zero Trust Network Access GraphQL API
  slug: zero-trust-network-access-graphql
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
overview: 'Zero Trust Network Access publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Deployment Groups API, Devices API, DEX Tests API, and 3 more. Tagged areas include Access Control, Cloud Security, Cybersecurity, Identity Management, and Network Access.


  The Zero Trust Network Access catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Zero Trust Network Access'' developer surface includes documentation, developer portal, code examples, and 19 more developer resources.'
plans:
- name: Zero Trust Network Access Plans Pricing
  plan_count: 3
  slug: zero-trust-network-access-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Zero Trust Network Access Rate Limits
  slug: zero-trust-network-access-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Zero Trust Network Access API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: zero-trust-network-access-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.4
  coverage:
    artifact_dirs: 14
    catalog_gap: 62.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 9.8
    contract_quality: 59.2
    developer_ergonomics: 38.1
    discoverability: 66.7
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 36.9
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zero-trust-network-access/refs/heads/main/screenshots/zero-trust-network-access-2026-06-20T201911.png
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
- Identity Management
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
