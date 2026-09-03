---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Maxmind Agentic Access
  operation_count: 6
  slug: maxmind-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 2
apis:
- baseURL: https://geoip.maxmind.com
  baseurl_source: declared
  description: City-level IP geolocation lookup with postal, subdivisions, and coordinates
  name: MaxMind GeoIP City API
  slug: maxmind-geoip-city-api
- baseURL: https://geoip.maxmind.com
  baseurl_source: declared
  description: Country-level IP geolocation lookup
  name: MaxMind GeoIP Country API
  slug: maxmind-geoip-country-api
- baseURL: https://geoip.maxmind.com
  baseurl_source: declared
  description: Most comprehensive IP data lookup including anonymizer/VPN/proxy detection, user type, static IP score, and connection details
  name: MaxMind GeoIP Insights API
  slug: maxmind-geoip-insights-api
- baseURL: https://geoip.maxmind.com
  baseurl_source: declared
  description: Most detailed fraud scoring with component-level risk factor decomposition
  name: MaxMind minFraud Factors API
  slug: maxmind-minfraud-factors-api
- baseURL: https://geoip.maxmind.com
  baseurl_source: declared
  description: Extended fraud scoring with over 80 data points on IPs, emails, devices, and payment cards
  name: MaxMind minFraud Insights API
  slug: maxmind-minfraud-insights-api
- baseURL: https://geoip.maxmind.com
  baseurl_source: declared
  description: Basic fraud scoring returning a single risk score (0-99) and IP risk score
  name: MaxMind minFraud Score API
  slug: maxmind-minfraud-score-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MaxMind GeoIP Web Services GeoIP City API
  slug: open-maxmind-geoip-city-api
- collection_type: open
  name: MaxMind GeoIP Web Services GeoIP City GeoIP Country API
  slug: open-maxmind-geoip-country-api
- collection_type: open
  name: MaxMind GeoIP Web Services GeoIP City GeoIP Insights API
  slug: open-maxmind-geoip-insights-api
- collection_type: open
  name: MaxMind GeoIP Web Services GeoIP City minFraud Factors API
  slug: open-maxmind-minfraud-factors-api
- collection_type: open
  name: MaxMind GeoIP Web Services GeoIP City minFraud Insights API
  slug: open-maxmind-minfraud-insights-api
- collection_type: open
  name: MaxMind GeoIP Web Services GeoIP City minFraud Score API
  slug: open-maxmind-minfraud-score-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/maxmind-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maxmind-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/maxmind-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.maxmind.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.maxmind.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/maxmind
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/maxmind
- group: company
  title: ''
  type: Blog
  url: https://blog.maxmind.com/
- group: company
  title: ''
  type: BlogFeed
  url: https://blog.maxmind.com/feed.xml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.maxmind.com/en/solutions/fraud-prevention/plans-pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.maxmind.com/
- group: other
  title: ''
  type: X
  url: https://x.com/maxmind
- group: commercial
  title: ''
  type: Plans
  url: plans/maxmind-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/maxmind-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/maxmind-finops.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/maxmind-context.jsonld
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
created: '2026-06-12'
description: MaxMind is an IP intelligence and fraud prevention company founded in 2002, serving over 100,000 businesses worldwide. Their GeoIP web services provide accurate IP geolocation data including country, city, ISP, organization, ASN, connection type, and VPN/proxy detection. Their minFraud services offer real-time transaction risk scoring using over 80 data points on IPs, email addresses, devices, and payment cards to help businesses detect and prevent fraud. MaxMind also offers downloadable GeoIP databases and the free GeoLite2 dataset for developers who prefer local lookups over API calls.
finops:
- name: Maxmind Finops
  service_category: ''
  slug: maxmind-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/maxmind.png
jsonld:
- class_count: 0
  name: Maxmind Context
  property_count: 48
  slug: maxmind-context
layout: provider
modified: '2026-06-12'
name: MaxMind
nav: Providers
network: true
overview: 'MaxMind publishes 6 APIs on the [APIs.io](https://apis.io/) network, including GeoIP City API, GeoIP Country API, GeoIP Insights API, and 3 more. Tagged areas include IP Intelligence, Geolocation, Fraud Prevention, Risk Scoring, and VPN Detection.


  The MaxMind catalog on APIs.io includes 1 JSON-LD context.


  MaxMind''s developer surface includes authentication, documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Maxmind Plans Pricing
  plan_count: 10
  slug: maxmind-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Maxmind Rate Limits
  slug: maxmind-rate-limits
score:
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 11
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 63.3
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 40.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/maxmind/refs/heads/main/screenshots/maxmind-2026-06-20T185052.png
security:
- kind: authentication
  name: Maxmind Authentication
  slug: maxmind-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Maxmind Domain Security
  slug: maxmind-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: maxmind
tags:
- IP Intelligence
- Geolocation
- Fraud Prevention
- Risk Scoring
- VPN Detection
- Proxy Detection
- ISP Data
- GeoIP
website: https://www.maxmind.com/
---
