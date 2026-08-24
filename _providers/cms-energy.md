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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 1
  human_in_the_loop: 1
  name: Cms Energy Agentic Access
  operation_count: 8
  slug: cms-energy-agentic-access
  summary_line: 8 operations · 1 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: The Consumers Energy Green Button Connect My Data API exposes customer-authorized electric and natural-gas usage data to registered third parties using the NAESB ESPI / Green Button standard. Authoriz
  name: Consumers Energy Green Button Connect My Data API
  slug: consumers-green-button-api
- description: The Authorizations API from CMS Energy — 2 operation(s) for authorizations.
  name: CMS Energy Authorizations API
  slug: cms-energy-authorizations-api
- description: The Bills API from CMS Energy — 1 operation(s) for bills.
  name: CMS Energy Bills API
  slug: cms-energy-bills-api
- description: The GreenButton API from CMS Energy — 1 operation(s) for greenbutton.
  name: CMS Energy GreenButton API
  slug: cms-energy-greenbutton-api
- description: The Intervals API from CMS Energy — 1 operation(s) for intervals.
  name: CMS Energy Intervals API
  slug: cms-energy-intervals-api
- description: The Meters API from CMS Energy — 2 operation(s) for meters.
  name: CMS Energy Meters API
  slug: cms-energy-meters-api
artifact_total: 20
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
created: '2026-03-21'
description: CMS Energy is an energy holding company whose primary subsidiary is Consumers Energy, an electric and natural gas utility serving customers in Michigan. Consumers Energy participates in the Green Button Connect My Data (GBCMD) program, exposing customer-authorized energy usage data to third parties via OAuth 2.0 - typically brokered through UtilityAPI - for use in energy management, demand response, EV charging, solar, and sustainability applications.
finops:
- name: Cms Energy Finops
  service_category: Energy / Utility
  slug: cms-energy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cms-energy.png
layout: provider
modified: '2026-04-23'
name: CMS Energy
nav: Providers
network: true
overview: 'CMS Energy publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authorizations API, Bills API, GreenButton API, and 2 more. Tagged areas include Electric, Energy, Green Button, Michigan, and Natural Gas.


  CMS Energy''s developer surface includes authentication, documentation, support, and 9 more developer resources.'
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
- limit_count: 2
  name: Cms Energy Rate Limits
  slug: cms-energy-rate-limits
scopes:
- name: Cms Energy Scopes
  scope_count: 1
  slug: cms-energy-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 34.1
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 52.6
    developer_ergonomics: 26.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 34.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 44.6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cms-energy/refs/heads/main/screenshots/cms-energy-2026-06-20T174637.png
security:
- kind: authentication
  name: Cms Energy Authentication
  slug: cms-energy-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Cms Energy Domain Security
  slug: cms-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
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
