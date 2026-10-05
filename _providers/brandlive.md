---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-04'
api_count: 6
apis:
- description: Brandlive API provides endpoints for managing virtual event sessions, templates, and registrations.
  name: Brandlive API
  slug: brandlive-api-2
- description: The Brandlive API API from Brandlive — 1 operation(s) for brandlive api.
  name: Brandlive Brandlive API
  slug: brandlive-brandlive-api-api
- description: The Event API from Brandlive — 2 operation(s) for event.
  name: Brandlive Event API
  slug: brandlive-event-api
- description: The Registration API from Brandlive — 1 operation(s) for registration.
  name: Brandlive Registration API
  slug: brandlive-registration-api
- description: The Registration Code Check API from Brandlive — 1 operation(s) for registration code check.
  name: Brandlive Registration Code Check API
  slug: brandlive-registration-code-check-api
- description: The Template API from Brandlive — 1 operation(s) for template.
  name: Brandlive Template API
  slug: brandlive-template-api
artifact_total: 8
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brandlive/refs/heads/main/vendors/brandlive-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brandlive-vendors.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/brandlive/refs/heads/main/rules/brandlive-rules.yml
  title: ''
  type: Spectral
  url: rules/brandlive-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/brandlive/refs/heads/main/conformance/brandlive-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brandlive-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/brandlive/refs/heads/main/llms/brandlive-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brandlive-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brandlive/refs/heads/main/hosts/brandlive-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brandlive-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://support.brandlive.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brandlive.com/legal/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://api.brandlive.com/docs/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brandlive/refs/heads/main/security/brandlive-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brandlive-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brandlive.com/
coverage:
  checked: '2026-10-03'
  detail: API documentation at https://api.brandlive.com/docs/ is a JavaScript‑rendered single‑page app with no machine‑readable OpenAPI spec discovered.
  evidence:
  - status: 200
    url: https://api.brandlive.com/docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-03'
description: Brandlive provides a video streaming platform for businesses, enabling live town halls, video podcasts, on‑demand content, and interactive virtual events. Their solutions include BrandTV®, a streaming service, and Brandlive Studios for high‑production video creation. Serving enterprises such as Nike, Cognizant, Pfizer, and Shopify, Brandlive helps companies inject creativity into internal communications and external audiences, turning ordinary meetings into engaging, broadcast‑quality experiences.
image: https://framerusercontent.com/images/vds3mcWC5zZ6S26PmxAfPWDg8ow.png
layout: provider
modified: '2026-10-03'
name: Brandlive
nav: Providers
network: true
overview: 'Brandlive publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Brandlive API, Event API, Registration API, and 3 more. Tagged areas include Company, Video, Streaming, Live Events, and Enterprise.


  The Brandlive catalog on APIs.io includes 1 Spectral governance ruleset.


  Brandlive''s developer surface includes support, documentation, and 8 more developer resources.'
random_paper: 5
rules:
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Brandlive API Rules
  rule_count: 8
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 0
  slug: brandlive-rules
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 38.8
    catalog_earned_first_party: 0.0
    catalog_gap: 76.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 15.9
    contract_quality: 9.4
    developer_ergonomics: 14.3
    discoverability: 69.6
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Brandlive Domain Security
  slug: brandlive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brandlive
tags:
- Company
- Video
- Streaming
- Live Events
- Enterprise
website: https://www.brandlive.com/
---
