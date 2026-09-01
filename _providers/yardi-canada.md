---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Yardi Canada Agentic Access
  operation_count: 8
  slug: yardi-canada-agentic-access
  summary_line: 8 operations
api_count: 1
apis:
- description: 'The documented family of Voyager web-service interfaces that Yardi Canada clients and their vendors integrate against — Collections, Commercial, Construction, Internet Listing Service (ILS) and Guest '
  name: Yardi Voyager Standard Interfaces
  slug: yardi-voyager-standard-interfaces
- description: The RentCafe marketing, leasing and resident-services API, used by Yardi Canada's multifamily clients and their vendors. Yardi's published RentCafe API Terms of Use names concrete operations in its Sc
  name: RentCafe API
  slug: rentcafe-api
- description: Yardi's first-party Model Context Protocol server, announced in early access on 2025-09-10 and described as available now in Virtuoso Enterprise on 2026-06-16. Listed on the Anthropic connector direct
  name: Yardi Virtuoso Connector (MCP)
  slug: yardi-virtuoso-connector-mcp
- description: Per-product and per-region service components
  name: Yardi Canada Components API
  slug: yardi-canada-components-api
- description: Unplanned service incidents and their updates
  name: Yardi Canada Incidents API
  slug: yardi-canada-incidents-api
- description: Scheduled maintenance windows
  name: Yardi Canada Maintenance API
  slug: yardi-canada-maintenance-api
- description: Rolled-up page status
  name: Yardi Canada Status API
  slug: yardi-canada-status-api
artifact_total: 14
collections:
- collection_type: open
  name: Yardi Systems Status API
  slug: open-yardi-canada-status
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/yardi-canada-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yardi-canada-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.yardibreeze.ca/
- group: company
  title: ''
  type: Website
  url: https://www.yardi.com/
- group: company
  title: ''
  type: About
  url: https://www.yardi.com/blog/global/yardi-canada-ltd-celebrates-25-years/37395.html
- group: company
  title: ''
  type: Partners
  url: https://www.yardi.com/company/become-an-interface-partner/
- group: docs
  title: ''
  type: Documentation
  url: https://www.yardi.com/services/interfaces/standard-interface-options/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://resources.yardi.com/legal/rc-api-tou/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/YardiSystems
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/yardi
- group: agent
  title: ''
  type: MCPServer
  url: mcp/yardi-canada-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/yardi-canada-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/yardi-canada-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/yardi-canada-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/yardi-canada-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/yardi-canada-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.yardi.com/company/cloud-security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/yardi-canada-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/yardi-canada-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.yardi.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/yardi-canada-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/yardi-canada-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/yardi-canada-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/yardi-canada-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/yardi-canada-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/yardi-canada-status-overlay.yaml
- group: operate
  title: ''
  type: Support
  url: https://www.yardi.com/company/technical-support/
- group: start
  title: ''
  type: Login
  url: https://clientcentral.yardi.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://resources.yardi.com/legal/privacy-statement/
- group: commercial
  title: ''
  type: Legal
  url: https://www.yardi.com/company/legal/
- group: company
  title: ''
  type: Blog
  url: https://www.yardibreeze.ca/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.yardibreeze.ca/feed/
- group: company
  title: ''
  type: News
  url: https://www.yardi.com/news/
- group: company
  title: ''
  type: Careers
  url: https://www.yardi.com/careers/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.yardi.com/company/contact-us/
created: '2026-07-26'
description: 'Yardi Canada Ltd. is the Canadian subsidiary of Yardi Systems, Inc. (Goleta, California), opened in Mississauga in 1998 and now headquartered in Toronto with regional offices in Saskatoon and Vancouver and roughly 500 staff. It sells, implements and supports the Yardi property and investment management stack in Canada — Voyager, Breeze Premier, RentCafe, Home IQ, Matrix and Pulse — across residential, commercial, affordable, senior living and investment portfolios, and its Canadian footprint grew by acquisition: Point2 Technologies in Saskatoon in 2010, an EnerNOC division in Vancouver in 2016, and Planimetron in Toronto in 2022. It sits on the systems-of-record rung of the value chain rather than the listing or land-registration rung — it is the ledger and operating platform a landlord or asset manager runs on, not a portal like REALTOR.ca and not a registry operator like Teranet. Its API posture, stated honestly, is licensed-access-only and partner-gated. There is no public
  developer portal: developer., developers., api. and docs. hosts do not resolve on either yardi.ca or yardi.com, and the primary Canadian domain yardi.ca — registered to Yardi Systems, Inc. since 2003 — resolves to 104.156.161.80 but serves no web content at all (TCP 443 and 80 both time out). Real interfaces exist, but only behind the Interface Partnership Program: an application, a signed Data Exchange Agreement per interface type, a company at least two years old with three or more active Voyager clients, and an annual per-interface fee. RESO is absent entirely — Yardi appears nowhere in the RESO certification directory — which is the expected result for a Canadian property management vendor, because Canadian residential listings move through CREA''s DDF and REALTOR.ca rather than through RESO-certified MLS endpoints. Two public, machine-readable surfaces do exist and neither of them is REST. Yardi ships a first-party MCP server — the Yardi Virtuoso Connector, listed on the Anthropic
  connector directory and served from mcp.virtuoso.ai — whose OAuth 2.1 authorization contract (RFC 8414 and RFC 9728 metadata, PKCE, dynamic client registration) is published anonymously even though its tool list is not. And status.yardi.com runs a full Atlassian Statuspage with a public JSON API across 134 components in 16 product groups, seven of which carry an explicit Canada component — the only anonymous, machine-readable signal of Yardi Canada''s production service health.'
image: https://www.yardi.com/wp-content/themes/cmw-standard-v2-theme/images/icons/apple-touch-icon-152x152.png
layout: provider
mcp_servers:
- description: ''
  name: Yardi Virtuoso
  slug: yardi-virtuoso
modified: '2026-07-26'
name: Yardi Canada
nav: Providers
network: true
overview: 'Yardi Canada publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Components API, Incidents API, Maintenance API, and 1 more. Tagged areas include Real-Estate, Canada, Property Management, Rentals, and Commercial Real Estate.


  Yardi Canada''s developer surface includes documentation, authentication, changelog, support, legal docs, engineering blog, product news, and 29 more developer resources.'
random_paper: 6
scopes:
- name: Yardi Canada Scopes
  scope_count: 4
  slug: yardi-canada-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: strong
  composite: 60.1
  coverage:
    artifact_dirs: 20
    catalog_gap: 68.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 50.9
    developer_ergonomics: 42.3
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 60.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 75.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/yardi-canada/refs/heads/main/screenshots/yardi-canada-2026-08-17T083014.png
security:
- kind: authentication
  name: Yardi Canada Authentication
  slug: yardi-canada-authentication
  summary_line: oauth2/opaque-token/none · 4 schemes
- kind: domain-security
  name: Yardi Canada Domain Security
  slug: yardi-canada-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Yardi Canada Trust Center
  slug: yardi-canada-trust-center
  summary_line: SOC 2 (annual), SOC 1 (biannual), SSAE 18, PCI, HIPAA, Sarbanes-Oxley, CSA STAR Level 2, FIPS 140-2 (key management)
slug: yardi-canada
tags:
- Real-Estate
- Canada
- Property Management
- Rentals
- Commercial Real Estate
- PropTech
- Multifamily
- Affordable Housing
- Senior Living
- Investment Management
- Tenancy
- Payments
- MCP
- Artificial Intelligence
website: https://www.yardibreeze.ca/
---
