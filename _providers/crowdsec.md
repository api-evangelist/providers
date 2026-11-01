---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Crowdsec Agentic Access
  operation_count: 1
  slug: crowdsec-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 8
apis:
- description: This is the API to manage CrowdSec services
  name: CrowdSec Service API
  slug: crowdsec-service-api
- baseURL: https://admin.api.crowdsec.net/v1/
  baseurl_source: declared
  description: The Allow Lists API from Crowdsec — 6 operation(s) for allow lists.
  name: Crowdsec Allow Lists API
  slug: crowdsec-allow-lists-api
- baseURL: https://admin.api.crowdsec.net/v1/
  baseurl_source: declared
  description: The Blocklists API from Crowdsec — 12 operation(s) for blocklists.
  name: Crowdsec Blocklists API
  slug: crowdsec-blocklists-api
- baseURL: https://admin.api.crowdsec.net/v1/
  baseurl_source: declared
  description: The CVEs API from Crowdsec — 4 operation(s) for cves.
  name: Crowdsec CVEs API
  slug: crowdsec-cves-api
- baseURL: https://admin.api.crowdsec.net/v1/
  baseurl_source: declared
  description: The Hub API from Crowdsec — 2 operation(s) for hub.
  name: Crowdsec Hub API
  slug: crowdsec-hub-api
- baseURL: https://admin.api.crowdsec.net/v1/
  baseurl_source: declared
  description: The Info API from Crowdsec — 51 operation(s) for info.
  name: Crowdsec Info API
  slug: crowdsec-info-api
- baseURL: https://admin.api.crowdsec.net/v1/
  baseurl_source: declared
  description: The Integrations API from Crowdsec — 9 operation(s) for integrations.
  name: Crowdsec Integrations API
  slug: crowdsec-integrations-api
- baseURL: https://admin.api.crowdsec.net/v1/
  baseurl_source: declared
  description: The Metrics API from Crowdsec — 1 operation(s) for metrics.
  name: Crowdsec Metrics API
  slug: crowdsec-metrics-api
artifact_total: 16
asyncapis:
- description: ''
  name: Crowdsec Webhooks
  slug: crowdsec-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/crowdsec/agentic-access/crowdsec-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/crowdsec-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/crowdsec/plans/crowdsec-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/crowdsec-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/crowdsec/rules/crowdsec-rules.yml
  title: ''
  type: Spectral
  url: rules/crowdsec-rules.yml
- group: design
  href: https://artifacts.apis.io/crowdsec/asyncapi/crowdsec-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/crowdsec-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/crowdsec/authentication/crowdsec-authentication.yml
  title: ''
  type: Authentication
  url: authentication/crowdsec-authentication.yml
- group: design
  href: https://artifacts.apis.io/crowdsec/conformance/crowdsec-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crowdsec-conformance.yml
- group: other
  href: https://artifacts.apis.io/crowdsec/overlays/crowdsec-openapi-overlay.yml
  title: ''
  type: Overlay
  url: overlays/crowdsec-openapi-overlay.yml
- group: agent
  href: https://artifacts.apis.io/crowdsec/llms/crowdsec-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crowdsec-llms.txt
- group: agent
  href: https://artifacts.apis.io/crowdsec/well-known/crowdsec-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/crowdsec-well-known.yml
- group: other
  href: https://artifacts.apis.io/crowdsec/hosts/crowdsec-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crowdsec-hosts.yml
- group: other
  href: https://artifacts.apis.io/crowdsec/vendors/crowdsec-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crowdsec-vendors.yml
- group: build
  href: https://artifacts.apis.io/crowdsec/packages/crowdsec-packages.yml
  title: ''
  type: SDKs
  url: packages/crowdsec-packages.yml
- group: build
  href: https://artifacts.apis.io/crowdsec/packages/crowdsec-packages.yml
  title: ''
  type: Packages
  url: packages/crowdsec-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://support.crowdsec.net/hc/en-gb
- group: commercial
  title: ''
  type: Pricing
  url: https://www.crowdsec.net/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.crowdsec.net/newsroom
- group: start
  title: ''
  type: Login
  url: https://app.crowdsec.net/sign-in
- group: company
  title: ''
  type: Blog
  url: https://www.crowdsec.net/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.crowdsec.net/docs/next/appsec/quickstart/envoy-gateway
- group: docs
  title: ''
  type: Documentation
  url: https://doc.crowdsec.net/
- group: auth
  href: https://artifacts.apis.io/crowdsec/security/crowdsec-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crowdsec-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.crowdsec.net
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://api.crowdsec.net/mcp
  - status: 403
    url: https://booking.crowdsec.net/mcp
  - status: 200
    url: https://www.crowdsec.net
  - status: 403
    url: https://equityzen.com/company/crowdsec
  reason: no-developer-program
  state: none
created: '2026-10-11'
description: CrowdSec provides curated threat intelligence and a collaborative security platform that leverages community‑driven data to block malicious IPs, detect attacks, and automate response. Their solutions include open‑source agents, a SaaS console, and integrations for developers and enterprises, aiming to reduce the time to block threats from days to minutes. The company emphasizes AI‑driven analytics, open‑source contributions, and a marketplace of security tools.
finops:
- has_sources: true
  method: derived
  name: Crowdsec Finops
  primary_unit: seat
  service_category: ''
  slug: crowdsec-finops
  template: false
image: https://cms.crowdsec.net/wp-content/uploads/2024/09/Thumbnail-Homepage.png
layout: provider
modified: '2026-10-11'
name: Crowdsec
nav: Providers
network: true
overview: 'Crowdsec is listed with 8 APIs on the [APIs.io](https://apis.io/) network, including Allow Lists API, Blocklists API, CVEs API, and 5 more. Tagged areas include Security, Threat Intelligence, Open Source, Community, and Automation.


  The Crowdsec catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Crowdsec''s developer surface includes authentication, support, pricing, engineering blog, getting-started guide, documentation, and 16 more developer resources.'
plans:
- name: Crowdsec Plans Pricing
  plan_count: 7
  slug: crowdsec-plans-pricing
- name: Crowdsec Price Estimates
  plan_count: 0
  slug: crowdsec-price-estimates
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Crowdsec API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: crowdsec-rules
score:
  band: developing
  composite: 47.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 59.5
    catalog_earned_first_party: 12.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.2
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 57.1
    developer_ergonomics: 47.6
    discoverability: 73.2
    operational_transparency: 7.9
  previous_composite: 42.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Crowdsec Authentication
  slug: crowdsec-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Crowdsec Domain Security
  slug: crowdsec-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crowdsec
tags:
- Security
- Threat Intelligence
- Open Source
- Community
- Automation
- CrowdSec
website: https://www.crowdsec.net
---
