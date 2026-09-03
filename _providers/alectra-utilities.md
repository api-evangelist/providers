---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://sandbox.greenbuttonalliance.org:8443/DataCustodian
  baseurl_source: spec
  description: Application Information endpoints
  name: Alectra Utilities Application Information API
  slug: alectra-utilities-applicationinformation-api
- baseURL: https://sandbox.greenbuttonalliance.org:8443/DataCustodian
  baseurl_source: spec
  description: Authorization endpoints
  name: Alectra Utilities Authorization API
  slug: alectra-utilities-authorization-api
- baseURL: https://sandbox.greenbuttonalliance.org:8443/DataCustodian
  baseurl_source: spec
  description: Batch data transfer endpoints
  name: Alectra Utilities Batch API
  slug: alectra-utilities-batch-api
- baseURL: https://sandbox.greenbuttonalliance.org:8443/DataCustodian
  baseurl_source: spec
  description: Usage Point endpoints
  name: Alectra Utilities Usage Point API
  slug: alectra-utilities-usagepoint-api
artifact_total: 8
collections:
- collection_type: open
  name: Green Button API Documentation
  slug: open-alectra-utilities-green-button-espi
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/alectra-utilities-green-button-espi-overlay.yaml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/alectra-utilities-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alectra-utilities-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/alectra-utilities-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alectra-utilities-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/alectra-utilities-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alectra-utilities-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://alectrautilities.com/
- group: docs
  title: ''
  type: Documentation
  url: https://alectrautilities.com/green-button
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alectrautilities.com/green-button-privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alectrautilities.com/green-button-connect-my-data-terms-and-conditions-access-and-use
- group: other
  title: ''
  type: Registration
  url: https://alectrautilitiesonboarding.savagedata.com/
- group: start
  title: ''
  type: Portal
  url: https://myalectra.alectrautilities.com/
- group: operate
  title: ''
  type: Support
  url: https://myalectra.alectrautilities.com/portal/#/Help/General%20Inquiry
- group: company
  title: ''
  type: Blog
  url: https://www.alectra.com/news
- group: company
  title: ''
  type: BlogRSS
  url: https://alectrautilities.com/rss.xml
- group: company
  title: ''
  type: Newsletter
  url: https://alectrautilities.com/newsletter
- group: operate
  title: ''
  type: Contact
  url: https://alectrautilities.com/contact-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alectra-utilities
created: '2026-07-27'
description: 'Alectra Utilities Corporation is Ontario''s second-largest municipally owned electricity distributor and one of the largest local distribution companies (LDCs) in Canada, serving roughly one million customers across seventeen communities in the Greater Toronto and Hamilton Area and the Golden Horseshoe — Alliston, Aurora, Barrie, Beeton, Bradford West Gwillimbury, Brampton, Guelph, Hamilton, Markham, Mississauga, Penetanguishene, Richmond Hill, Rockwood, St. Catharines, Thornton, Tottenham and Vaughan. It also bills water and wastewater/stormwater on behalf of several of those municipalities, and runs the GRE&T Centre for grid innovation. It sits squarely in the wires and metering layer of the Canadian value chain: it does not generate, it does not operate the market (the IESO does), and it is owned by its municipal shareholders rather than by investors — the Crown/municipal ownership pattern that dominates Canadian electricity. Its API posture exists only because a regulator
  created it. Ontario Regulation 633/21 (Energy Data) requires every Ontario electric and gas utility to implement Green Button Download My Data and Connect My Data to the NAESB REQ.21 ESPI v3.3 standard and to obtain Green Button Alliance certification, with an implementation deadline of 1 November 2023. Alectra publishes a Green Button page displaying GBA Certified DMD and CMD marks, a Green Button Connect My Data Terms and Conditions of Access and Use citing O. Reg. 633/21 by name, a live customer Green Button portal, and a live third-party registration and onboarding site — all three hosted by its data custodian vendor, Savage Data Systems, not by Alectra. What Alectra does not publish is any of the things that would let an outsider verify the implementation: there is no developer portal, no API documentation, no base URI, no OpenAPI, no scopes and no OAuth metadata anywhere on alectrautilities.com or on the portal host. developer., developers., docs. and data.alectrautilities.com do
  not resolve; /developers, /api, /docs, /data, /openapi.json and /swagger.json all return HTTP 404. Every path on the Green Button portal — including a deliberately invented control path — HTTP 302 redirects to a customer sign-in, so no endpoint could be confirmed. The resulting split is the finding: a mandated consumer-data API that a third party can reach only by completing an application and being approved, and zero open market or grid data of any kind, because in Ontario that layer belongs to the IESO and the OEB rather than to the distributor.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-27'
name: Alectra Utilities
nav: Providers
network: true
overview: 'Alectra Utilities publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Application Information API, Authorization API, Batch API, and 1 more. Tagged areas include Energy, Canada, Utilities, Electricity, and Ontario.


  Alectra Utilities'' developer surface includes documentation, developer portal, support, engineering blog, and 16 more developer resources.'
random_paper: 1
scopes:
- name: Alectra Utilities Scopes
  scope_count: 0
  slug: alectra-utilities-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 18
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 11.1
    developer_ergonomics: 39.9
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 30.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 56.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alectra-utilities/refs/heads/main/screenshots/alectra-utilities-2026-08-07T161155.png
security:
- kind: authentication
  name: Alectra Utilities Authentication
  slug: alectra-utilities-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Alectra Utilities Domain Security
  slug: alectra-utilities-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: alectra-utilities
tags:
- Energy
- Canada
- Utilities
- Electricity
- Ontario
- Green Button
- Smart Metering
- Energy Data
- Grid
- Municipal Utility
- ESPI
website: https://alectrautilities.com/
---
