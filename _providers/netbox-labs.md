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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.5
  scored_at: '2026-09-25'
api_count: 1
apis:
- baseURL: https://demo.netbox.dev/api/
  baseurl_source: declared
  description: The authentication-check API from NetBox Labs — 1 operation(s) for authentication-check.
  name: NetBox Labs Authentication Check API
  slug: netbox-labs-authentication-check-api
- baseURL: https://demo.netbox.dev/api/
  baseurl_source: declared
  description: The circuits API from NetBox Labs — 24 operation(s) for circuits.
  name: NetBox Labs Circuits API
  slug: netbox-labs-circuits-api
- baseURL: https://demo.netbox.dev/api/
  baseurl_source: declared
  description: The core API from NetBox Labs — 21 operation(s) for core.
  name: NetBox Labs Core API
  slug: netbox-labs-core-api
- baseURL: https://demo.netbox.dev/api/
  baseurl_source: declared
  description: The dcim API from NetBox Labs — 103 operation(s) for dcim.
  name: NetBox Labs Dcim API
  slug: netbox-labs-dcim-api
- baseURL: https://demo.netbox.dev/api/
  baseurl_source: declared
  description: The extras API from NetBox Labs — 49 operation(s) for extras.
  name: NetBox Labs Extras API
  slug: netbox-labs-extras-api
- baseURL: https://demo.netbox.dev/api/
  baseurl_source: declared
  description: The ipam API from NetBox Labs — 41 operation(s) for ipam.
  name: NetBox Labs Ipam API
  slug: netbox-labs-ipam-api
- baseURL: https://demo.netbox.dev/api/
  baseurl_source: declared
  description: The schema API from NetBox Labs — 1 operation(s) for schema.
  name: NetBox Labs Schema API
  slug: netbox-labs-schema-api
- baseURL: https://demo.netbox.dev/api/
  baseurl_source: declared
  description: The status API from NetBox Labs — 1 operation(s) for status.
  name: NetBox Labs Status API
  slug: netbox-labs-status-api
- baseURL: https://demo.netbox.dev/api/
  baseurl_source: declared
  description: The tenancy API from NetBox Labs — 12 operation(s) for tenancy.
  name: NetBox Labs Tenancy API
  slug: netbox-labs-tenancy-api
- baseURL: https://demo.netbox.dev/api/
  baseurl_source: declared
  description: The users API from NetBox Labs — 14 operation(s) for users.
  name: NetBox Labs Users API
  slug: netbox-labs-users-api
- baseURL: https://demo.netbox.dev/api/
  baseurl_source: declared
  description: The virtualization API from NetBox Labs — 15 operation(s) for virtualization.
  name: NetBox Labs Virtualization API
  slug: netbox-labs-virtualization-api
- baseURL: https://demo.netbox.dev/api/
  baseurl_source: declared
  description: The vpn API from NetBox Labs — 20 operation(s) for vpn.
  name: NetBox Labs Vpn API
  slug: netbox-labs-vpn-api
- baseURL: https://demo.netbox.dev/api/
  baseurl_source: declared
  description: The wireless API from NetBox Labs — 6 operation(s) for wireless.
  name: NetBox Labs Wireless API
  slug: netbox-labs-wireless-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NetBox REST authentication-check API
  slug: open-netbox-labs-authentication-check-api
- collection_type: open
  name: NetBox REST authentication-check circuits API
  slug: open-netbox-labs-circuits-api
- collection_type: open
  name: NetBox REST authentication-check core API
  slug: open-netbox-labs-core-api
- collection_type: open
  name: NetBox REST authentication-check dcim API
  slug: open-netbox-labs-dcim-api
- collection_type: open
  name: NetBox REST authentication-check extras API
  slug: open-netbox-labs-extras-api
- collection_type: open
  name: NetBox REST authentication-check ipam API
  slug: open-netbox-labs-ipam-api
- collection_type: open
  name: NetBox REST authentication-check schema API
  slug: open-netbox-labs-schema-api
- collection_type: open
  name: NetBox REST authentication-check status API
  slug: open-netbox-labs-status-api
- collection_type: open
  name: NetBox REST authentication-check tenancy API
  slug: open-netbox-labs-tenancy-api
- collection_type: open
  name: NetBox REST authentication-check users API
  slug: open-netbox-labs-users-api
- collection_type: open
  name: NetBox REST authentication-check virtualization API
  slug: open-netbox-labs-virtualization-api
- collection_type: open
  name: NetBox REST authentication-check vpn API
  slug: open-netbox-labs-vpn-api
- collection_type: open
  name: NetBox REST authentication-check wireless API
  slug: open-netbox-labs-wireless-api
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/netbox-labs/refs/heads/main/plans/netbox-labs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/netbox-labs-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/netbox-labs/refs/heads/main/capabilities/netbox-labs-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/netbox-labs-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/netbox-labs/refs/heads/main/overlays/netbox-labs-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/netbox-labs-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://netboxlabs.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://netboxlabs.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://netboxlabs.com/docs/netbox/integrations/rest-api/
- group: docs
  title: ''
  type: APIReference
  url: https://netboxlabs.com/docs/netbox/integrations/rest-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://netboxlabs.com/docs/netbox/integrations/rest-api/
- group: company
  title: ''
  type: Blog
  url: https://netboxlabs.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://netboxlabs.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://signup.netboxlabs.com/
- group: operate
  title: ''
  type: Support
  url: https://netboxlabs.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://netboxlabs.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://netboxlabs.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/netboxlabs
- group: operate
  title: ''
  type: StatusPage
  url: https://status.netboxlabs.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://netboxlabs.com/docs/netbox/release-notes/version-4.6
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/netbox-labs/refs/heads/main/lifecycle/netbox-labs-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/netbox-labs-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/netbox-labs/refs/heads/main/changelog/netbox-labs-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/netbox-labs-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/netbox-labs/refs/heads/main/packages/netbox-labs-packages.yml
  title: ''
  type: Packages
  url: packages/netbox-labs-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/netbox-labs/refs/heads/main/packages/netbox-labs-packages.yml
  title: ''
  type: SDKs
  url: packages/netbox-labs-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/netbox-labs/refs/heads/main/mcp/netbox-labs-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/netbox-labs-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/netbox-labs/refs/heads/main/llms/netbox-labs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/netbox-labs-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/netbox-labs/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/netbox-labs/refs/heads/main/security/netbox-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/netbox-labs-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/netbox-labs/refs/heads/main/security/netbox-labs-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/netbox-labs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://netboxlabs.com/security/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/netbox-labs/refs/heads/main/security/netbox-labs-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/netbox-labs-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://netboxlabs.com/security/
created: '2026-07-17'
description: NetBox Labs is the commercial company behind NetBox, the open-source network source-of-truth (DCIM and IPAM) used by network and infrastructure teams to model sites, racks, devices, interfaces, IP addresses, prefixes, VLANs, circuits, VPNs, and tenancy. It offers NetBox Cloud and NetBox Enterprise alongside the OSS project. NetBox exposes a comprehensive token-authenticated REST API (OpenAPI 3.0, 1,000+ operations across dcim/ipam/circuits/tenancy/virtualization/vpn/wireless), a read-only GraphQL API, official Python (pynetbox) and Go (go-netbox) client libraries, and an official read-only Model Context Protocol (MCP) server for AI agents. The platform is SOC 2 Type II compliant.
image: https://netboxlabs.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: NetBox Labs MCP Server
  slug: netbox-labs-mcp-server
modified: '2026-07-20'
name: NetBox Labs
nav: Providers
network: true
overview: 'NetBox Labs publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Authentication Check API, Circuits API, Core API, and 10 more. Tagged areas include Company, Networking, DCIM, IPAM, and Infrastructure.


  NetBox Labs'' developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 22 more developer resources.'
plans:
- name: Netbox Labs Plans Pricing
  plan_count: 3
  slug: netbox-labs-plans-pricing
random_paper: 19
score:
  band: strong
  composite: 60.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 92.1
    contract_governance: 4.5
    contract_quality: 47.1
    developer_ergonomics: 66.1
    discoverability: 75.0
    operational_transparency: 52.6
  previous_composite: 58.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/netbox-labs/refs/heads/main/screenshots/netbox-labs-2026-08-07T184929.png
security:
- kind: authentication
  name: Netbox Labs Authentication
  slug: netbox-labs-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Netbox Labs Domain Security
  slug: netbox-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Netbox Labs Vulnerability Disclosure
  slug: netbox-labs-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Netbox Labs Trust Center
  slug: netbox-labs-trust-center
  summary_line: SOC 2
slug: netbox-labs
tags:
- Company
- Networking
- DCIM
- IPAM
- Infrastructure
- Source of Truth
- Network Automation
- OpenAPI
- MCP
website: https://netboxlabs.com/
---
