---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-09-05'
api_count: 6
apis:
- description: The external API of the Federated Wireless Spectrum Controller, the cloud platform that manages CBRS spectrum assignment, CBSD lifecycle, monitoring and compliance. The Spectrum Controller web applica
  name: Spectrum Controller External SAS API
  slug: spectrum-controller-external-api
- description: The identity and access-management service behind the Federated Wireless Spectrum Controller, called by the web application as IAM_BASE_URL. It backs account administration and the self-management por
  name: Spectrum IAM API
  slug: spectrum-iam-api
- description: The analytics and reporting service behind the Spectrum Controller, called by the web application as both ANALYTICS_BASE_URL and REPORTING_BASE_URL. It backs the spectrum analytics, network visualizat
  name: Spectrum KPI Analytics and Reporting API
  slug: spectrum-kpi-api
- description: The regulated Spectrum Access System to CBSD protocol interface Federated Wireless operates as an FCC-certified SAS administrator. The protocol — registration, spectrum inquiry, grant, heartbeat, reli
  name: SAS-CBSD Interface
  slug: sas-cbsd-interface
- description: The Automated Frequency Coordination system interface Federated Wireless operates for the 6 GHz band. On 2024-02-23 the FCC Office of Engineering and Technology approved seven AFC systems for commerci
  name: 6 GHz AFC Device Interface
  slug: afc-device-interface
- description: 'A remote Model Context Protocol server published on federatedwireless.ai, advertised through RFC 8414 OAuth authorization-server metadata and RFC 9728 protected-resource metadata. It is not announced '
  name: Federated Wireless MCP Server
  slug: mcp-server
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://federatedwireless.ai/
- group: start
  title: ''
  type: Portal
  url: https://myfederated.federatedwireless.com
- group: operate
  title: ''
  type: Support
  url: https://federatedwireless.ai/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://myfederated.federatedwireless.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://federatedwireless.ai/resources/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://federatedwireless.ai/feed/
- group: operate
  title: ''
  type: PressReleases
  url: https://federatedwireless.ai/resources/press-releases/
- group: operate
  title: ''
  type: Contact
  url: https://federatedwireless.ai/contact/
- group: company
  title: ''
  type: Partners
  url: https://federatedwireless.ai/partners/
- group: other
  title: ''
  type: Products
  url: https://federatedwireless.ai/products/
- group: company
  title: ''
  type: About
  url: https://federatedwireless.ai/about/
- group: auth
  title: ''
  type: Certification
  url: https://federatedwireless.ai/cpi-certification/
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://federatedwireless.ai/services-definition/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://federatedwireless.ai/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://federatedwireless.ai/privacy-policy/
- group: other
  title: ''
  type: DataStatement
  url: https://federatedwireless.ai/data-statement/
- group: start
  title: ''
  type: SignUp
  url: https://myfederated.federatedwireless.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/federatedwireless
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/2725741
- group: auth
  title: ''
  type: Authentication
  url: authentication/federated-wireless-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/federated-wireless-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/federated-wireless-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/federated-wireless-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/federated-wireless-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/federated-wireless-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/federated-wireless-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/federated-wireless-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/federated-wireless-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/federated-wireless-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/federated-wireless-packages.yml
coverage:
  checked: '2026-08-12'
  detail: 'Federated Wireless ships real APIs and names them itself, but every one is behind a customer wall: the Spectrum Controller external SAS, IAM and KPI endpoints — whose base URLs the company''s own public configuration.js discloses — return HTTP 403 MissingAuthenticationTokenException from AWS API Gateway, the MyFederated Zendesk help center 403s to anonymous visitors and exposes only six FAQ articles about course logins, and the regulated SAS-CBSD and 6 GHz AFC hosts resolve to company AWS infrastructure that refuses TCP 443 from the public internet. There is no developer portal, no docs subdomain and no machine-readable contract anywhere public.'
  evidence:
  - status: 403
    url: https://spectrum-api.federatedwireless.com/v1
  - status: 403
    url: https://spectrum-kpi.federatedwireless.com/v2.0
  - status: 403
    url: https://myfederated.federatedwireless.com/hc/en-us
  - status: 404
    url: https://federatedwireless.ai/openapi.json
  - status: 200
    url: https://federatedwireless.ai/.well-known/oauth-protected-resource
  reason: customer-only-docs
  state: gated
created: '2026-08-12'
description: 'Federated Wireless, founded in 2012 and headquartered in Arlington, Virginia, is a shared- and unlicensed-spectrum coordination company. It is one of the FCC-certified CBRS Spectrum Access System (SAS) administrators for the 3.5 GHz band, operates a nationwide Environmental Sensing Capability (ESC) network, and is one of the seven 6 GHz Automated Frequency Coordination (AFC) systems the FCC Office of Engineering and Technology approved for commercial operation in February 2024. Its cloud-native platform — the Spectrum Controller, the Automated Network Planner (ANP) and the Spectrum AI physical-AI platform announced in June 2026 — assigns, monitors and optimizes spectrum for carriers, broadband providers, enterprises running private 5G/LTE, and government agencies. The programmable surface is real but almost entirely private: the regulated SAS-CBSD (WInnForum WINNF-TS-0016) and 6 GHz AFC device interfaces run on hosts that refuse public connections, and the Spectrum Controller''s
  external SAS, IAM and KPI/analytics APIs are AWS API Gateway endpoints that return 403 to every anonymous request. Federated Wireless publishes no developer portal, no API reference and no machine-readable contract. The one openly discoverable agent surface is a remote Model Context Protocol server on federatedwireless.ai, advertised through RFC 8414 and RFC 9728 metadata, which fronts the company''s WordPress content estate rather than its spectrum platform.'
image: https://federatedwireless.ai/wp-content/uploads/2025/07/fw-federated-wireless-logo-horiz-rev-600px.png
layout: provider
mcp_servers:
- description: Federated Wireless publishes a remote Model Context Protocol server on its primary company host, federatedwireless.ai. It is not announced in any Federated Wireless documentation, press release or MCP
  name: Federated Wireless MCP Server
  slug: federated-wireless-mcp-server
modified: '2026-08-12'
name: Federated Wireless
nav: Providers
network: true
overview: 'Federated Wireless publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Spectrum, CBRS, Wireless, and Telecommunications.


  Federated Wireless'' developer surface includes developer portal, support, engineering blog, signup flow, authentication, and 25 more developer resources.'
plans:
- name: Federated Wireless Plans Pricing
  plan_count: 0
  slug: federated-wireless-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Federated Wireless Rate Limits
  slug: federated-wireless-rate-limits
scopes:
- name: Federated Wireless Scopes
  scope_count: 1
  slug: federated-wireless-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 27.6
  coverage:
    artifact_dirs: 13
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 27.6
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 58.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/federated-wireless/refs/heads/main/screenshots/federated-wireless-2026-09-02T145502.png
security:
- kind: authentication
  name: Federated Wireless Authentication
  slug: federated-wireless-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Federated Wireless Domain Security
  slug: federated-wireless-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: federated-wireless
tags:
- Company
- Spectrum
- CBRS
- Wireless
- Telecommunications
- Private 5G
- Shared Spectrum
- Spectrum Access System
- 6 GHz
- Network Planning
- RF Engineering
- Government
website: https://federatedwireless.ai/
---
