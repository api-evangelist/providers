---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/voltaiq-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voltaiq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.voltaiq.com/
- group: company
  title: ''
  type: Blog
  url: https://www.voltaiq.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.voltaiq.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.voltaiq.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.voltaiq.com/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Voltaiq
- group: auth
  title: ''
  type: Compliance
  url: https://www.voltaiq.com/security
- group: design
  title: ''
  type: Conformance
  url: conformance/voltaiq-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/voltaiq-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/voltaiq-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/voltaiq-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/voltaiq-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/voltaiq-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/voltaiq-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/voltaiq-llms.txt
coverage:
  checked: '2026-09-04'
  detail: Voltaiq markets "an API that enables flexible custom integrations" but ships every customer into its own single-tenant AWS VPC with no shared API host, and its security page ends the integration section with "Full technical documentation is available upon request" - so the reference and any contract exist only for an account holder.
  evidence:
  - status: 200
    url: https://www.voltaiq.com/security
  - status: 404
    url: https://www.voltaiq.com/openapi.json
  - status: 0
    url: https://api.voltaiq.com/
  - status: 0
    url: https://docs.voltaiq.com/
  reason: customer-only-docs
  state: gated
created: '2026-09-04'
description: 'Voltaiq is an enterprise battery intelligence (EBI) software company that automatically collects, cleans and harmonizes data from battery test equipment, production lines and fielded systems into a single searchable data core, then extracts electrochemical quality indicators, KPIs and traceability for battery R&D, product development, manufacturing and in-field applications. The platform ships no-code dashboards, an Analytics Studio Python data-science environment, and pre-built integrations with industry-standard cyclers (NOVONIX, MACCOR, Arbin, Biologic, Bitrode, Digatron, Neware, Gamry, Chroma, Keysight) alongside LIMS, MES and BI tools. Voltaiq states it offers "an API that enables flexible custom integrations", but every customer system is deployed into its own single-tenant AWS VPC and the company publishes no public developer portal, API reference or machine-readable contract: its security page says "Full technical documentation is available upon request."'
image: https://www.voltaiq.com/hubfs/Featured%20Images/Voltaiq%20Featured%20Image%20%5BFeatured%20Image%5D.png
layout: provider
modified: '2026-09-04'
name: Voltaiq
nav: Providers
network: true
overview: 'Voltaiq is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Batteries, Energy Storage, Manufacturing, and Analytics.


  Voltaiq''s developer surface includes engineering blog, pricing, support, authentication, and 13 more developer resources.'
plans:
- name: Voltaiq Plans Pricing
  plan_count: 3
  slug: voltaiq-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Voltaiq Rate Limits
  slug: voltaiq-rate-limits
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 5.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 35.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: authentication
  name: Voltaiq Authentication
  slug: voltaiq-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Voltaiq Domain Security
  slug: voltaiq-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Voltaiq Trust Center
  slug: voltaiq-trust-center
  summary_line: SOC 2 Type II, GDPR, ITAR
slug: voltaiq
tags:
- Company
- Batteries
- Energy Storage
- Manufacturing
- Analytics
- Industrial IoT
- Data Management
- Quality
- Electric Vehicles
- Enterprise Software
website: https://www.voltaiq.com/
---
