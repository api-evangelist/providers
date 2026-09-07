---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-09-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 1
  name: Cms Energy Agentic Access
  operation_count: 8
  slug: cms-energy-agentic-access
  summary_line: 8 operations · 1 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The Consumers Energy Green Button Connect My Data API exposes customer-authorized electric and natural-gas usage data to registered third parties using the NAESB ESPI / Green Button standard. Authoriz
  name: Consumers Energy Green Button Connect My Data API
  slug: consumers-green-button-api
- baseURL: https://utilityapi.com/api/v2
  baseurl_source: declared
  description: The Authorizations API from CMS Energy — 2 operation(s) for authorizations.
  name: CMS Energy Authorizations API
  slug: cms-energy-authorizations-api
- baseURL: https://utilityapi.com/api/v2
  baseurl_source: declared
  description: The Bills API from CMS Energy — 1 operation(s) for bills.
  name: CMS Energy Bills API
  slug: cms-energy-bills-api
- baseURL: https://utilityapi.com/DataCustodian/espi/1_1/resource
  baseurl_source: declared
  description: The GreenButton API from CMS Energy — 1 operation(s) for greenbutton.
  name: CMS Energy GreenButton API
  slug: cms-energy-greenbutton-api
- baseURL: https://utilityapi.com/api/v2
  baseurl_source: declared
  description: The Intervals API from CMS Energy — 1 operation(s) for intervals.
  name: CMS Energy Intervals API
  slug: cms-energy-intervals-api
- baseURL: https://utilityapi.com/api/v2
  baseurl_source: declared
  description: The Meters API from CMS Energy — 2 operation(s) for meters.
  name: CMS Energy Meters API
  slug: cms-energy-meters-api
- baseURL: https://www.consumersenergy.com/arcgispublic/rest
  baseurl_source: declared
  description: Consumers Energy publishes its outage map data as an anonymous Esri ArcGIS Server 11.5 REST Services Directory on its own domain — no key, no account, no registration. CEOutageMap carries seven layers
  name: Consumers Energy Outage Map ArcGIS REST API
  slug: cms-energy-outage-map-api
artifact_total: 24
asyncapis:
- description: ''
  name: Cms Energy Webhooks
  slug: cms-energy-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Consumers Energy Green Button Connect My Data API (UtilityAPI) Authorizations API
  slug: open-cms-energy-authorizations-api
- collection_type: open
  name: Consumers Energy Green Button Connect My Data API (UtilityAPI) Authorizations Bills API
  slug: open-cms-energy-bills-api
- collection_type: open
  name: Consumers Energy Green Button Connect My Data API (UtilityAPI) Authorizations GreenButton API
  slug: open-cms-energy-greenbutton-api
- collection_type: open
  name: Consumers Energy Green Button Connect My Data API (UtilityAPI) Authorizations Intervals API
  slug: open-cms-energy-intervals-api
- collection_type: open
  name: Consumers Energy Green Button Connect My Data API (UtilityAPI) Authorizations Meters API
  slug: open-cms-energy-meters-api
- collection_type: open
  name: Consumers Energy Green Button Connect My Data API (UtilityAPI)
  slug: open-cms-energy
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cms-energy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cms-energy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cms-energy-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cms-energy-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.cmsenergy.com
- group: company
  title: ''
  type: Website
  url: https://www.consumersenergy.com
- group: docs
  title: ''
  type: Documentation
  url: https://utilityapi.com/docs/utilities/consumersenergy
- group: company
  title: ''
  type: About
  url: https://www.cmsenergy.com/about-cms-energy/consumers-energy/
- group: operate
  title: ''
  type: Support
  url: https://www.cmsenergy.com/contact-us/default.aspx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cmsenergy.com/privacy-statement/default.aspx
- group: other
  title: ''
  type: X
  url: https://twitter.com/CMSEnergy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cms-energy/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cms-energy-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/cms-energy-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cms-energy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/cms-energy-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cms-energy-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/cms-energy-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cms-energy-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cms-energy-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cms-energy-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cms-energy-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cms-energy-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/cms-energy-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cms-energy-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cms-energy-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cms-energy-llms.txt
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cms-energy-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cms-energy-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cms-energy-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://greenbutton.consumersenergy.com/
- group: docs
  title: ''
  type: APIReference
  url: https://utilityapi.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://utilityapi.com/docs/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://greenbutton.consumersenergy.com/third-party/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://greenbutton.consumersenergy.com/third-party/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.consumersenergy.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.consumersenergy.com/contact-us
created: '2026-03-21'
description: CMS Energy is an energy holding company whose primary subsidiary is Consumers Energy, an electric and natural gas utility serving customers in Michigan. Consumers Energy participates in the Green Button Connect My Data (GBCMD) program, exposing customer-authorized energy usage data to third parties via OAuth 2.0 - typically brokered through UtilityAPI - for use in energy management, demand response, EV charging, solar, and sustainability applications.
finops:
- name: Cms Energy Finops
  service_category: Energy / Utility
  slug: cms-energy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cms-energy.png
layout: provider
mcp_servers:
- description: CANDIDATE MCP tool surface for CMS Energy. Neither CMS Energy, Consumers Energy, nor the platform operating its Green Button Connect My Data program publishes an MCP server. A third-party MCP catalogu
  name: CMS Energy MCP Server
  slug: cms-energy-mcp-server
modified: '2026-09-06'
name: CMS Energy
nav: Providers
network: true
overview: 'CMS Energy publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authorizations API, Bills API, GreenButton API, and 3 more. Tagged areas include Electric, Energy, Green Button, Michigan, and Natural Gas.


  The CMS Energy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  CMS Energy''s developer surface includes authentication, documentation, support, sandbox, API reference, getting-started guide, signup flow, and 31 more developer resources.'
plans:
- name: Cms Energy Plans Pricing
  plan_count: 2
  slug: cms-energy-plans-pricing
press:
- date: '2026-05-25'
  title: CMS) boosts Q1 2026 profit, maps $24.1B clean-energy ...
  url: https://www.stocktitan.net/sec-filings/CMS/10-q-cms-energy-corp-quarterly-earnings-report-15fb12484bdd.html
- date: '2026-05-25'
  title: CMS Energy Announces the Early Results and Upsizing of ...
  url: https://www.cmsenergy.com/investor-relations/news-releases/news-release-details/2025/CMS-Energy-Announces-the-Early-Results-and-Upsizing-of-its-Cash-Tender-Offer-for-Certain-Outstanding-Debt-Securities/default.aspx
- date: '2026-05-25'
  title: CMS Energy Corp. and Terry Woolley
  url: https://www.sec.gov/enforcement-litigation/administrative-proceedings/33-8403
- date: '2026-05-25'
  title: Consumers Energy Selected by U.S. Department of ...
  url: https://www.cmsenergy.com/investor-relations/news-releases/news-release-details/2024/Consumers-Energy-Selected-by-U.S.-Department-of-Energy-for-Nearly-20-Million-to-Add-Real-Time-Visibility-to-Grid/default.aspx
- date: '2026-05-25'
  title: CMS Energy Exceeds Earnings Guidance in 2025, Raises ...
  url: https://www.prnewswire.com/news-releases/cms-energy-exceeds-earnings-guidance-in-2025-raises-2026-adjusted-eps-guidance-302679615.html
random_paper: 10
rate_limits:
- limit_count: 4
  name: Cms Energy Rate Limits
  slug: cms-energy-rate-limits
scopes:
- name: Cms Energy Scopes
  scope_count: 10
  slug: cms-energy-scopes
  summary_line: 10 scopes
score:
  band: strong
  composite: 64.4
  coverage:
    artifact_dirs: 28
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 29.3
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 0.0
    contract_quality: 51.7
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 50.0
  previous_composite: 35.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 16.7
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 89.2
  schema_version: 0.19.0
  scored_at: '2026-09-06'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/cms-energy/refs/heads/main/screenshots/cms-energy-2026-06-20T174637.png
security:
- kind: authentication
  name: Cms Energy Authentication
  slug: cms-energy-authentication
  summary_line: none/http/oauth2 · 4 schemes
- kind: domain-security
  name: Cms Energy Domain Security
  slug: cms-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cms Energy Vulnerability Disclosure
  slug: cms-energy-vulnerability-disclosure
  summary_line: Hackerone
slug: cms-energy
tags:
- Electric
- Energy
- Green Button
- Michigan
- Natural Gas
- Utility
- Fortune 500
website: https://www.cmsenergy.com
---
