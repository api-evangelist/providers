---
access_model:
  confidence: high
  label: Free · Anonymous undocumented data feeds · No developer program
  onboarding: unknown
  pricing: free
  public: true
  source:
  - documentation
  - probes
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 14.2
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: The undocumented JSON endpoint behind SaskPower's public "Where Your Power Comes From" page. A single anonymous GET — no key, no signup, no referer check — returns the province's current supply pictur
  name: SaskPower Power Use Dashboard Data
  slug: saskpower-power-use-dashboard-data
- description: A genuinely published, anonymous RSS 2.0 feed of SaskPower's planned power outages, opened by the visible "RSS feed" link on the Outages Planned for Necessary Maintenance page. Each item carries a tit
  name: SaskPower Planned Outages RSS Feed
  slug: saskpower-planned-outages-rss-feed
- description: The undocumented JSON endpoint behind SaskPower's public outage map, found in the markup of the Outage Map and Updates page alongside the KML reference and fetched anonymously with no key, no signup a
  name: SaskPower Live Outage JSON Feed
  slug: saskpower-live-outage-json-feed
- description: 'The KML data feed behind SaskPower''s public outage map, referenced directly in the markup of the Outage Map and Updates page and served anonymously from the outagemap.saskpower.com host. It returns a '
  name: SaskPower Outage Map KML Feed
  slug: saskpower-outage-map-kml-feed
- description: The KML data feed behind SaskPower's Smart Meter Installation Map, requested by the site's own SP.scripts.js bundle and served anonymously from the Sitecore content handler. It returns a KML 2.1 docum
  name: SaskPower Smart Meter Installation Map KML Feed
  slug: saskpower-smart-meter-installation-map-kml-feed
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/saskpower-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/saskpower-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/saskpower-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/saskpower-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/saskpower-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/saskpower-conformance.yml
- group: build
  title: ''
  type: Examples
  url: examples/saskpower-examples.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/saskpower-power-use-dashboard.schema.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/saskpower-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.saskpower.com/
- group: company
  title: ''
  type: About
  url: https://www.saskpower.com/about-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.saskpower.com/terms
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.saskpower.com/-/media/SaskPower/Accounts-and-Services/Policy-Digital-TermsConditions.ashx
- group: commercial
  title: ''
  type: Privacy
  url: https://www.saskpower.com/footer/how-we-do-business/privacy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.saskpower.com/footer/how-we-do-business/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.saskpower.com/contact-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.saskpower.com/accounts/power-rates/power-supply-rates
- group: start
  title: ''
  type: Login
  url: https://www.saskpower.com/profile/my-dashboard
- group: start
  title: ''
  type: SignUp
  url: https://www.saskpower.com/accounts/mysaskpower/your-account/access-your-mysaskpower-account
- group: company
  title: ''
  type: Blog
  url: https://www.saskpower.com/about-us/Our-Company/Blog
- group: operate
  title: ''
  type: NewsReleases
  url: https://www.saskpower.com/about-us/media-information/news-releases
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/saskpower
- group: learn
  title: ''
  type: YouTube
  url: http://www.youtube.com/user/Poweringthefuture
- group: docs
  title: ''
  type: Documentation
  url: https://www.saskpower.com/our-power-future/our-electricity/electrical-system/where-your-power-comes-from
created: '2026-07-27'
description: 'SaskPower — the Saskatchewan Power Corporation — is the Crown corporation that owns and runs essentially the whole electricity value chain in the province of Saskatchewan, Canada. Established in 1929 as the Saskatchewan Power Commission and continued as the Saskatchewan Power Corporation in 1949 under The Power Corporation Act, it is owned by the provincial government through Crown Investments Corporation and reports to a Minister Responsible rather than to shareholders. It generates, transmits, distributes and retails power to more than 550,000 customers across roughly 652,000 square kilometres on more than 160,000 kilometres of line, from a fleet of coal, natural gas, hydro, wind and solar facilities totalling about 5,437 MW. Unlike Ontario or Alberta there is no competitive wholesale market operator sitting beside it — SaskPower is generator, wires company and retailer at once. Its API posture is the exact inverse of a regulated open-banking-style utility: no consumer energy
  data mandate applies to it at all. Saskatchewan has no Green Button regulation (Ontario and Nova Scotia do), Canada has no national energy consumer data right, and the Green Button Alliance states plainly that it has no information about any Green Button deployment in Saskatchewan. Smart meter usage data is visible only to the account holder inside MySaskPower behind an Azure AD B2C login; there is no consented third-party data-sharing API, no ESPI/Green Button surface, and no accreditation scheme. What SaskPower does publish — and publishes wide open, anonymously, with no key, no signup and no rate limit — is grid and system data: a live JSON feed of provincial system demand, generation by fuel type, net interchange and historical peak demand behind the public "Where Your Power Comes From" page, a second JSON feed listing current outages by service region, an RSS feed of planned outages, and two KML feeds driving the outage and smart-meter installation maps. None of it is documented as
  an API, versioned, or covered by a developer program: the former SaskPower ESB developer portal at api-info.saskpower.com no longer resolves, and api.saskpower.com is a live TIBCO/Mashery gateway that answers every public path with ERR_596_SERVICE_NOT_FOUND. Open market data, closed consumer data, and no published door for a developer to knock on.'
examples:
- key_count: 6
  name: Saskpower Outages Response
  slug: saskpower-outages-response
- key_count: 17
  name: Saskpower Power Use Dashboard Response
  slug: saskpower-power-use-dashboard-response
image: https://www.saskpower.com/-/media/saskpower/logo.png?la=en&h=92&w=344&hash=2F4CBFD7B403E69A4530EB778FAD7A1E
json_schemas:
- name: SaskPower Live Outage JSON Feed
  property_count: 6
  slug: saskpower-outages.schema
- name: SaskPower Power Use Dashboard Data
  property_count: 17
  slug: saskpower-power-use-dashboard.schema
layout: provider
modified: '2026-07-27'
name: SaskPower
nav: Providers
network: true
overview: 'SaskPower publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Canada, Utilities, Electricity, and Grid.


  SaskPower''s developer surface includes authentication, code examples, privacy policy, support, pricing, signup flow, engineering blog, and 17 more developer resources.'
random_paper: 67
score:
  band: emerging
  composite: 27.4
  delta: -3.7
  facets:
    commercial_clarity: 44.7
    contract_quality: 9.7
    developer_ergonomics: 26.1
    discoverability: 92.6
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 31.1
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Saskpower Authentication
  slug: saskpower-authentication
  summary_line: none/oidc-human-login · 4 schemes
- kind: domain-security
  name: Saskpower Domain Security
  slug: saskpower-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: saskpower
tags:
- Energy
- Canada
- Utilities
- Electricity
- Grid
- Smart Metering
- Crown Corporation
- Outages
- Renewables
- Open Data
website: https://www.saskpower.com/
---
