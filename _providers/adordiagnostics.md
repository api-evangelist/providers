---
agent_readiness:
  band: agent-aware
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.2
  scored_at: '2026-09-07'
api_count: 1
apis:
- description: A live, unauthenticated Model Context Protocol endpoint served from the www.adordx.com host and advertised in the company's own llms.txt. It is provided by the Wix site platform rather than authored b
  name: ADOR Diagnostics Site MCP
  slug: ador-diagnostics-site-mcp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.adordx.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/adordiagnostics-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adordiagnostics-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/adordiagnostics-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/adordiagnostics-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adordiagnostics-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/adordiagnostics-plans-pricing.yml
- group: company
  title: ''
  type: About
  url: https://www.adordx.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.adordx.com/news-and-events
- group: operate
  title: ''
  type: Contact
  url: https://www.adordx.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adordx.com/privacy-and-cookies-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adordx.com/terms-and-conditions
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ador-diagnostics/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/adordiagnostics
created: '2026-09-07'
description: 'ADOR Diagnostics is an in-vitro diagnostics (IVD) company developing syndromic multiplex molecular diagnostics for infectious disease, headquartered in Guidonia Montecelio, Italy with operations in Israel and Cyprus. Its NATlab platform pairs a bench-top modular analyser with a disposable all-included microfluidic cartridge to run fully automated sample-to-answer testing of crude clinical specimens in roughly 30-60 minutes, detecting up to 100 multiplexed targets per sample. The assay chemistry is a patented isothermal rolling circle amplification (RCA) protocol read by a proprietary carbon array sensor embedded in the cartridge, rather than PCR, and the system is aimed at small and mid-sized laboratories, doctor offices, point-of-care and near-bed testing, rural labs and mobile care units. The company markets an optional connectivity feature linking NATlab units across sites for geographic mapping of results and outbreak detection, but publishes no technical documentation
  for it. ADOR is a diagnostics instrument and assay manufacturer, not a software vendor: it operates no developer program, publishes no public API, SDK or machine-readable API contract, and the only machine-readable surfaces on its own host are an llms.txt and the Wix-platform site MCP endpoint that llms.txt advertises.'
image: https://static.wixstatic.com/media/e0cc12_4becce2d37744839bc20a1ad38122632~mv2.png/v1/fill/w_324,h_100,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/ADOR%20LOGO.png
layout: provider
mcp_servers:
- description: ''
  name: ADOR Diagnostics MCP Server
  slug: ador-diagnostics-mcp-server
modified: '2026-09-07'
name: ADOR Diagnostics
nav: Providers
network: true
overview: 'ADOR Diagnostics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Medical Devices, In Vitro Diagnostics, and Molecular Diagnostics.


  ADOR Diagnostics'' developer surface includes authentication, engineering blog, and 12 more developer resources.'
plans:
- name: Adordiagnostics Plans Pricing
  plan_count: 0
  slug: adordiagnostics-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 17.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adordiagnostics Authentication
  slug: adordiagnostics-authentication
  summary_line: none/bearer-token · 2 schemes
- kind: domain-security
  name: Adordiagnostics Domain Security
  slug: adordiagnostics-domain-security
  summary_line: TLSv1.3 · HSTS
slug: adordiagnostics
tags:
- Company
- Healthcare
- Medical Devices
- In Vitro Diagnostics
- Molecular Diagnostics
- Infectious Disease
- Point of Care
- Laboratory
- Life Sciences
- MCP
website: https://www.adordx.com/
---
