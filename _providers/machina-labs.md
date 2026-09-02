---
agent_readiness:
  band: human-only
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/machina-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://machinalabs.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.machinalabs.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.machinalabs.ai/cad-guidelines
- group: operate
  title: ''
  type: Support
  url: https://machinalabs.ai/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Machina-Labs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://machinalabs.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://machinalabs.ai/supplier-terms
- group: auth
  title: ''
  type: Compliance
  url: https://machinalabs.ai/quality
- group: company
  title: ''
  type: Blog
  url: https://machinalabs.ai/resources
- group: company
  title: ''
  type: BlogRSS
  url: https://machinalabs.ai/resources/rss.xml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/machina-labs-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/machina-labs-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/machina-labs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/machina-labs-rate-limits.yml
coverage:
  checked: '2026-08-25'
  detail: Machina Labs sells roboformed metal parts, not software access — its only public documentation site (docs.machinalabs.ai, a Nextra build) is a two-page CAD and Roboforming guide for manufacturing customers, and every contract-discovery path on both machinalabs.ai and docs.machinalabs.ai returned a real 404.
  evidence:
  - status: 200
    url: https://docs.machinalabs.ai/
  - status: 404
    url: https://machinalabs.ai/openapi.json
  - status: 404
    url: https://docs.machinalabs.ai/openapi.json
  - status: 404
    url: https://machinalabs.ai/.well-known/agent-card.json
  - status: 404
    url: https://machinalabs.ai/pricing
  reason: no-developer-program
  state: none
created: '2026-08-25'
description: 'Machina Labs is a Chatsworth, California manufacturer that builds software-defined factories for metal structures. Its RoboCraftsman platform pairs 7-axis robots with closed-loop AI control to roboform, scan, trim, drill and finish large sheet-metal parts — up to 12 ft long and 1/4 in thick, in aluminum, steel, stainless, titanium, nickel superalloys and refractory alloys — without any custom tooling, and captures high-resolution process data as a digital twin of every part. The company serves aerospace, defense (through its Machina Bellator subsidiary), hypersonics and automotive customers, is ITAR registered and CMMC Level 2 certified, and publishes customer-facing CAD and Roboforming documentation at docs.machinalabs.ai. It does not operate a public developer program: no API reference, OpenAPI specification, SDK or developer portal is published, and integration into customer PLM/MES systems is described only as a capability sold through its sales and applications engineering
  teams.'
image: https://machinalabs.ai/hubfs/Machina-Labs_Brandmark-Logo.png
layout: provider
modified: '2026-08-25'
name: Machina Labs
nav: Providers
network: true
overview: 'Machina Labs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, Robotics, Artificial Intelligence, and Aerospace.


  Machina Labs'' developer surface includes documentation, getting-started guide, support, engineering blog, and 11 more developer resources.'
plans:
- name: Machina Labs Plans Pricing
  plan_count: 0
  slug: machina-labs-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Machina Labs Rate Limits
  slug: machina-labs-rate-limits
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 19.0
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Machina Labs Domain Security
  slug: machina-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: machina-labs
tags:
- Company
- Manufacturing
- Robotics
- Artificial Intelligence
- Aerospace
- Defense
- Industrial Automation
- Metal Forming
- Advanced Manufacturing
website: https://machinalabs.ai/
---
