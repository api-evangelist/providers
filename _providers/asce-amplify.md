---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - '{''url'': ''https://amplify.asce.org/'', ''status'': 302, ''note'': ''declared website redirects to https://idp.sams-sigma.com/authorize?client_id=ASCE&response_type=code&scope=openid%2Bprofile%2Bemail%2Blicense%2Bprofile_extended%2Boffline_access&redirect_uri=https%3A//amplify.asce.org/openid-connect/sams-sigma&auth_token=eyJhbGciOiJSU0EtT0FFUC0yNTYiLCJlbmMiOiJBMTI4R0NNIn0.Dt8ycQ8ri4c4NqsHac831uiw1tZYvKtHlVoSLOVtX86qJ1ZmmJy1B70AK-b4xnBlDAV3BimhIYkOMeDXY8jEfus3rMYDriDtV_ZlyvIXpsUa4K08mkVJVcWrb9qFYUp8u-PqYIaHfIJoopByDEEg5bpbGAXOUJy5cdzW219i9wYthOlkRA5S5d9boU4Fl5msqsLi3JSUwgte1PdKAzgmJDaSbsB-u3AI1eEzdsk0b6pAVgyKBgvQyRjwwAcJmjqHK-o-9KU930THbpMmrAc73xEIZkW5FXRwU3MUkv5jTiKwl5dwGLfuutbcjuFeSCFTVZjd6vEnujuLl06a04EThw._90E37JZ3GbJsves.ONYVg_sogJsLmlYA3ylW-q14U5ZtlM9iK7YVgL3nJ8rf5rHdJ6Uzbl5fXEU8KqSsAYHQVp6-er-KJlb0GMrIvY_S3WvteoeAr1w9ENdOgIEw86FhBv6k5Esv5aTSgxxTC_4H7VR4sUBzf_Nt0ZCr74Va3urUYUn-xZXl7nNUyebhFzOqrhNmqyd6T_cbix93RX_08a5VP5kAVA.3la3dUfVSZi3vFhnqQeWpA&ip_address=2600%3A4040%3A9270%3Ac700%3Af5db%3Ae0be%3A34ee%3A3beb&referrer_url&prompt=none&openid_connect_destination=/%3Fimplicit-login%3Dtrue&state=%257B%2522token%2522%253A%25220HgmY4HObONCcrndKH6SvPdkC0f4JHgaCTZRt9-IrSM%2522%252C%2522destination%2522%253A%2522%255C%252F%253Fimplicit-login%253Dtrue%2522%257D&shibboleth_dest=https%3A//amplify.asce.org/openid-connect/sams-sigma/login-redirect&shibboleth=true
    — a different registrable domain (asce.org -> sams-sigma.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The ASCE ArcGIS Server instance at gis.asce.org publishes the hazard map, image and geoprocessing services that back the ASCE Hazard Tool — ASCE 7 wind, ice, snow, seismic, tsunami and tornado layers,
  name: ASCE GIS REST Services
  slug: arcgis-rest-services
- baseURL: https://api-hazard.asce.org/v1
  baseurl_source: declared
  description: The Flood API from ASCE Amplify — 1 operation(s) for flood.
  name: ASCE Amplify Flood API
  slug: asce-amplify-flood-api
- baseURL: https://api-hazard.asce.org/v1
  baseurl_source: declared
  description: The Ice API from ASCE Amplify — 1 operation(s) for ice.
  name: ASCE Amplify Ice API
  slug: asce-amplify-ice-api
- baseURL: https://api-hazard.asce.org/v1
  baseurl_source: declared
  description: The Rain API from ASCE Amplify — 1 operation(s) for rain.
  name: ASCE Amplify Rain API
  slug: asce-amplify-rain-api
- baseURL: https://api-hazard.asce.org/v1
  baseurl_source: declared
  description: The Seismic API from ASCE Amplify — 1 operation(s) for seismic.
  name: ASCE Amplify Seismic API
  slug: asce-amplify-seismic-api
- baseURL: https://api-hazard.asce.org/v1
  baseurl_source: declared
  description: The Snow API from ASCE Amplify — 1 operation(s) for snow.
  name: ASCE Amplify Snow API
  slug: asce-amplify-snow-api
- baseURL: https://api-hazard.asce.org/v1
  baseurl_source: declared
  description: The Tornado API from ASCE Amplify — 1 operation(s) for tornado.
  name: ASCE Amplify Tornado API
  slug: asce-amplify-tornado-api
- baseURL: https://api-hazard.asce.org/v1
  baseurl_source: declared
  description: The Tsunami API from ASCE Amplify — 1 operation(s) for tsunami.
  name: ASCE Amplify Tsunami API
  slug: asce-amplify-tsunami-api
- baseURL: https://api-hazard.asce.org/v1
  baseurl_source: declared
  description: The Wind API from ASCE Amplify — 1 operation(s) for wind.
  name: ASCE Amplify Wind API
  slug: asce-amplify-wind-api
- baseURL: https://gis.asce.org/arcgis/rest/services
  baseurl_source: declared
  description: The Health-check API from ASCE Amplify — 1 operation(s) for health-check.
  name: ASCE Amplify Health Check API
  slug: asce-amplify-health-check-api
artifact_total: 28
common:
- group: company
  title: ''
  type: Blog
  url: https://www.asce.org/publications-and-news/newsroom
- group: other
  href: https://artifacts.apis.io/asce-amplify/overlays/asce-amplify-hazard-loads-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/asce-amplify-hazard-loads-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/asce-amplify/llms/asce-amplify-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asce-amplify-llms.txt
- group: agent
  href: https://artifacts.apis.io/asce-amplify/skills/_index.yml
  title: Packaged agent skills for the ASCE Hazard Loads API
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/asce-amplify/mcp/asce-amplify-mcp.yml
  title: Candidate MCP tool surface derived from the OpenAPI (no server exists)
  type: X-MCPServerCandidate
  url: mcp/asce-amplify-mcp.yml
- group: design
  href: https://artifacts.apis.io/asce-amplify/conventions/asce-amplify-conventions.yml
  title: ''
  type: Conventions
  url: conventions/asce-amplify-conventions.yml
- group: design
  href: https://artifacts.apis.io/asce-amplify/errors/asce-amplify-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/asce-amplify-problem-types.yml
- group: design
  href: https://artifacts.apis.io/asce-amplify/lifecycle/asce-amplify-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/asce-amplify-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/asce-amplify/conformance/asce-amplify-conformance.yml
  title: ''
  type: Conformance
  url: conformance/asce-amplify-conformance.yml
- group: design
  href: https://artifacts.apis.io/asce-amplify/data-model/asce-amplify-data-model.yml
  title: ''
  type: DataModel
  url: data-model/asce-amplify-data-model.yml
- group: build
  href: https://artifacts.apis.io/asce-amplify/packages/asce-amplify-packages.yml
  title: ''
  type: Packages
  url: packages/asce-amplify-packages.yml
- group: operate
  href: https://artifacts.apis.io/asce-amplify/rate-limits/asce-amplify-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/asce-amplify-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/asce-amplify/plans/asce-amplify-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/asce-amplify-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/asce-amplify/finops/asce-amplify-finops.yml
  title: ''
  type: FinOps
  url: finops/asce-amplify-finops.yml
- group: auth
  href: https://artifacts.apis.io/asce-amplify/authentication/asce-amplify-authentication.yml
  title: ''
  type: Authentication
  url: authentication/asce-amplify-authentication.yml
- group: start
  title: ASCE API Dashboard
  type: DeveloperPortal
  url: https://api-hazard.asce.org/
- group: docs
  title: ASCE Hazard Tool API documentation
  type: Documentation
  url: https://www.asce.org/publications-and-news/asce-hazard-tool/api
- group: docs
  title: ASCE Hazard Loads API documentation (Swagger UI)
  type: APIReference
  url: https://api-hazard.asce.org/docs
- group: start
  title: About the ASCE Hazard Tool
  type: GettingStarted
  url: https://www.asce.org/publications-and-news/asce-hazard-tool/about
- group: start
  title: Interactive site for constructing and testing API calls
  type: Console
  url: https://api-hazard.asce.org/docs
- group: operate
  title: American Society of Civil Engineers Status (Atlassian Statuspage)
  type: StatusPage
  url: https://status.asce.org/
- group: operate
  title: Report a Hazard Tool data or bug issue
  type: Support
  url: https://www.asce.org/publications-and-news/asce-hazard-tool/report-an-issue
- group: commercial
  title: Request a quote / higher usage limit
  type: Pricing
  url: https://www.asce.org/publications-and-news/asce-hazard-tool/request-a-quote
- group: commercial
  title: ASCE Hazard Tool terms
  type: TermsOfService
  url: https://www.asce.org/publications-and-news/asce-hazard-tool/terms
- group: commercial
  title: ASCE privacy policy
  type: PrivacyPolicy
  url: https://www.asce.org/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.asce.org/
- group: auth
  href: https://artifacts.apis.io/asce-amplify/security/asce-amplify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asce-amplify-domain-security.yml
- group: start
  title: ASCE Amplify Platform
  type: Portal
  url: https://amplify.asce.org/
- group: start
  title: ASCE Website
  type: Portal
  url: https://www.asce.org/
created: '2025-02-17'
description: ASCE Amplify is a platform created by the American Society of Civil Engineers (ASCE) that provides civil engineering data and advocacy tools. The platform includes the ASCE Hazard Tool API, which provides a simple interface to query locations in the United States for environmental hazard data by geographic location. The Hazard Tool API covers seismic, wind, snow, ice, flood, and other environmental hazard loads used in structural design per ASCE standards. ASCE Amplify also supports advocacy, connecting civil engineers with elected officials to advocate for infrastructure investment and sustainable practices.
features:
- description: Query any US location by latitude and longitude or address to retrieve site-specific environmental hazard values for structural design, including ASCE 7 seismic, wind, snow, and ice parameters.
  name: Geographic Hazard Lookup
- description: Retrieve seismic design parameters including Ss, S1, SMS, SM1, SDS, SD1, and spectral acceleration values per ASCE 7 for any US location.
  name: ASCE 7 Seismic Parameters
- description: Access design wind speed values for various risk categories and exposure categories per ASCE 7 for structural wind load calculations.
  name: Wind Speed Data
- description: Retrieve ground snow load values and ice storm data for design of roof structures and overhead transmission lines per ASCE 7.
  name: Snow and Ice Load Data
- description: Tools for ASCE members to contact elected officials and advocate for infrastructure funding, engineering standards, and professional issues.
  name: Civil Engineer Advocacy
finops:
- has_sources: true
  method: derived
  name: Asce Amplify Finops
  primary_unit: ''
  service_category: ''
  slug: asce-amplify-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/asce-amplify.png
integrations:
- description: API values directly correspond to ASCE 7 Minimum Design Loads for Buildings and Other Structures, the primary reference standard for US structural engineering.
  name: ASCE 7 Standards
- description: Hazard parameters from the API align with International Building Code requirements that reference ASCE 7 for environmental load design values.
  name: IBC Building Codes
layout: provider
modified: '2026-10-06'
name: ASCE Amplify
nav: Providers
network: true
overview: 'ASCE Amplify publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Flood API, Ice API, Rain API, and 7 more. Tagged areas include Civil Engineering, Hazard Data, Engineering Standards, Infrastructure, and Structural Engineering.


  The ASCE Amplify catalog on APIs.io includes 1 Spectral governance ruleset.


  ASCE Amplify''s developer surface includes engineering blog, authentication, documentation, API reference, getting-started guide, developer console, support, and 22 more developer resources.'
plans:
- name: Asce Amplify Plans Pricing
  plan_count: 0
  slug: asce-amplify-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Asce Amplify Rate Limits
  slug: asce-amplify-rate-limits
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: ASCE Amplify API Rules
  rule_count: 45
  severity_counts:
    error: 42
    hint: 0
    info: 2
    warn: 1
  slug: asce-amplify-rules
score:
  band: developing
  composite: 46.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 43.0
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 36.8
  previous_composite: 45.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 47.4
      total: 19
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/asce-amplify/asce-amplify-2026-06-20T172456.png
security:
- kind: authentication
  name: Asce Amplify Authentication
  slug: asce-amplify-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Asce Amplify Domain Security
  slug: asce-amplify-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: asce-seismic-design-parameters
  slug: asce-amplify-seismic-design-parameters
- name: asce-site-hazard-lookup
  slug: asce-amplify-site-hazard-lookup
slug: asce-amplify
tags:
- Civil Engineering
- Hazard Data
- Engineering Standards
- Infrastructure
- Structural Engineering
- Geospatial
- Seismic
- Building Codes
- Standards Body
use_cases:
- description: Structural engineers use the ASCE Hazard Tool API to obtain site-specific hazard parameters for building and infrastructure design in compliance with ASCE 7 and building codes.
  name: Structural Design
- description: Civil engineers perform preliminary site assessments for new construction projects by querying multiple locations for hazard comparisons.
  name: Site Assessment
- description: Structural engineering software vendors integrate the ASCE Hazard Tool API to automatically populate design parameters based on project location.
  name: Software Integration
website: https://www.asce.org/
---
