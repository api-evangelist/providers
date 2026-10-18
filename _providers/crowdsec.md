---
agent_readiness:
  band: agent-aware
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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.5
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Crowdsec Agentic Access
  operation_count: 1
  slug: crowdsec-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: This is the API to manage CrowdSec services
  name: CrowdSec Service API
  slug: crowdsec-service-api
artifact_total: 7
asyncapis:
- description: ''
  name: Crowdsec Webhooks
  slug: crowdsec-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/crowdsec/refs/heads/main/agentic-access/crowdsec-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/crowdsec-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/crowdsec/refs/heads/main/plans/crowdsec-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/crowdsec-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crowdsec/refs/heads/main/rules/crowdsec-rules.yml
  title: ''
  type: Spectral
  url: rules/crowdsec-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crowdsec/refs/heads/main/asyncapi/crowdsec-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/crowdsec-webhooks.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crowdsec/refs/heads/main/authentication/crowdsec-authentication.yml
  title: ''
  type: Authentication
  url: authentication/crowdsec-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crowdsec/refs/heads/main/conformance/crowdsec-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crowdsec-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crowdsec/refs/heads/main/overlays/crowdsec-openapi-overlay.yml
  title: ''
  type: Overlay
  url: overlays/crowdsec-openapi-overlay.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/crowdsec/refs/heads/main/llms/crowdsec-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crowdsec-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/crowdsec/refs/heads/main/well-known/crowdsec-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/crowdsec-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crowdsec/refs/heads/main/hosts/crowdsec-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crowdsec-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crowdsec/refs/heads/main/vendors/crowdsec-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crowdsec-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/crowdsec/refs/heads/main/packages/crowdsec-packages.yml
  title: ''
  type: SDKs
  url: packages/crowdsec-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/crowdsec/refs/heads/main/packages/crowdsec-packages.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/crowdsec/refs/heads/main/security/crowdsec-domain-security.yml
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
image: https://cms.crowdsec.net/wp-content/uploads/2024/09/Thumbnail-Homepage.png
layout: provider
modified: '2026-10-11'
name: Crowdsec
nav: Providers
network: true
overview: 'Crowdsec is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Threat Intelligence, Open Source, Community, and Automation.


  The Crowdsec catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Crowdsec''s developer surface includes authentication, support, pricing, engineering blog, getting-started guide, documentation, and 16 more developer resources.'
plans:
- name: Crowdsec Plans Pricing
  plan_count: 7
  slug: crowdsec-plans-pricing
random_paper: 0
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
  composite: 41.3
  coverage:
    artifact_dirs: 14
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 47.6
    discoverability: 75.0
    operational_transparency: 7.9
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
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
