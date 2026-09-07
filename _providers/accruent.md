---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-06'
agentic_access:
- acting_count: 131
  human_in_the_loop: 0
  name: Accruent Agentic Access
  operation_count: 255
  slug: accruent-agentic-access
  summary_line: 255 operations · 131 acting
api_count: 1
apis:
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: RESTful CMMS API for the Accruent Maintenance Connection product. 126 paths / 255 operations across assets, asset specifications, meter history, images and documents, classifications, companies, parts
  name: Maintenance Connection Web API
  slug: maintenance-connection-web-api
- description: REST API for Accruent Siterra, the wireless/telecom site and project lifecycle management product, fronted by the Accruent Developer Network on Azure API Management. Subscription-key auth via the accr
  name: Siterra API
  slug: siterra-api
- description: REST APIs for Accruent Meridian Cloud engineering document management — asset APIs, relationship APIs and contractor package APIs used by PowerWeb, Meridian Portal, Meridian Explorer and Meridian Mobi
  name: Meridian Cloud API
  slug: meridian-cloud-api
- description: RESTful API layer for Accruent EMS space and event scheduling, documented as a Platform as a Service surface with JWT authentication. The Swagger UI ships with the deployment rather than on a public h
  name: EMS Platform Services
  slug: ems-platform-services
- description: RESTful API for Accruent Lucernex IWMS / lease accounting. Documented on the public customer help site, but the schema browser and console are served from the customer's own tenancy at {tenant-url}/en
  name: Lucernex REST API
  slug: lucernex-rest-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accruent-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/accruent-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.accruent.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.accruent.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.accruent.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.maintenanceconnection.com/v8/help/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.accruent.com/wiki/siterra/gettingstarted
- group: operate
  title: ''
  type: Support
  url: https://www.accruent.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.accruent.com/resources/blog-posts
- group: company
  title: ''
  type: BlogRSS
  url: https://www.accruent.com/resources/blog-posts/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Accruent
- group: commercial
  title: ''
  type: Pricing
  url: https://www.accruent.com/product-pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.accruent.com/products/maintenance-connection/free-trial
- group: start
  title: ''
  type: Login
  url: https://developer.accruent.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.accruent.com/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.accruent.com/privacy-notice
- group: operate
  title: ''
  type: StatusPage
  url: https://status.accruent.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.accruent.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.accruent.com/security-compliance-certifications
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/accruent-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/accruent-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/accruent-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/accruent-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/accruent-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/accruent-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/accruent-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/accruent-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/accruent-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/accruent-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/accruent-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/accruent-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/accruent-maintenance-connection-overlay.yaml
created: '2026-09-06'
description: Accruent is a workplace, facilities and asset management software company serving more than 10,000 customers in over 150 countries, with a portfolio spanning CMMS/EAM (Maintenance Connection), engineering document management (Meridian), IWMS and lease accounting (Lucernex), space and event scheduling (EMS), telecom and wireless site management (Siterra), and IoT condition monitoring (Observe). Its public API surface is an Azure API Management developer network at developer.accruent.com plus per-product REST APIs; the Maintenance Connection Web API is the only contract published without a login — a Swagger 2.0 document describing 255 operations across assets, work orders, parts, purchasing, labor and lookup tables. Every other product API (Siterra, Meridian Cloud, EMS Platform Services, Lucernex) is documented publicly but its machine-readable definition sits behind developer-program approval or a customer tenancy.
image: https://www.accruent.com/hubfs/accruent-social-share.png
layout: provider
mcp_servers:
- description: ''
  name: Accruent MCP Server
  slug: accruent-mcp-server
modified: '2026-09-06'
name: Accruent
nav: Providers
network: true
overview: 'Accruent publishes 1 API on the [APIs.io](https://apis.io/) network: Maintenance Connection Web API. Tagged areas include Facilities Management, Asset Management, CMMS, EAM, and Maintenance.


  Accruent''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
plans:
- name: Accruent Plans Pricing
  plan_count: 8
  slug: accruent-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Accruent Rate Limits
  slug: accruent-rate-limits
score:
  band: strong
  composite: 54.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 52.0
    catalog_earned_first_party: 20.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 34.0
    developer_ergonomics: 66.1
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 47.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.19.0
  scored_at: '2026-09-06'
security:
- kind: authentication
  name: Accruent Authentication
  slug: accruent-authentication
  summary_line: http/apiKey · 4 schemes
- kind: domain-security
  name: Accruent Domain Security
  slug: accruent-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Accruent Trust Center
  slug: accruent-trust-center
  summary_line: ISO/IEC 27001, SOC 2, SOC 1
slug: accruent
tags:
- Facilities Management
- Asset Management
- CMMS
- EAM
- Maintenance
- Work Orders
- IWMS
- Space Management
- Engineering Document Management
- Built Environment
- Enterprise Software
- Real Estate
website: https://www.accruent.com/
---
