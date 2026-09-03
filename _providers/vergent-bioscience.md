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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: A live, anonymous Model Context Protocol endpoint served on the company's own host and advertised from its own llms.txt. Provided by the Wix Site MCP platform rather than authored by Vergent, it expos
  name: Vergent Bioscience Site MCP
  slug: vergent-bioscience-site-mcp
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vergent-bioscience-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vergentbio.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vergent-bioscience-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/vergent-bioscience-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/vergent-bioscience-plans-pricing.yml
- group: operate
  title: ''
  type: Support
  url: https://www.vergentbio.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vergentbio.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vergentbio.com/privacy
created: '2026-09-02'
description: Vergent Bioscience is a clinical-stage biotechnology company headquartered in Minneapolis, Minnesota, developing tumor-targeted fluorescent imaging agents for real-time intraoperative tumor visualization. Its lead compound, abenacianine for injection (VGT-309), is designed to let surgeons see previously undetected or difficult-to-find tumors during minimally invasive and robotic-assisted cancer surgery so that all tumor tissue can be removed in a single procedure. The company is first evaluating VGT-309 in lung cancer with the stated intent to expand into a wide range of solid tumors. Vergent publishes no developer program, no REST or GraphQL API, and no SDKs — it is a therapeutics and imaging-agent developer, not a software vendor. The only machine-readable surfaces on its own domain are a Wix-platform-generated llms.txt and a live, anonymous Model Context Protocol endpoint at /_api/mcp that exposes nine site-content and Wix-platform tools.
image: https://static.wixstatic.com/media/608efe_20a2e114600643b69837255747a0ffe5~mv2.jpg
layout: provider
mcp_servers:
- description: Vergent Bioscience serves a live, anonymous Model Context Protocol endpoint from its own domain at https://www.vergentbio.com/_api/mcp. The server is provided by the Wix Site MCP platform (the company
  name: Vergent Bioscience Site MCP
  slug: vergent-bioscience-site-mcp
modified: '2026-09-02'
name: Vergent Bioscience
nav: Providers
network: true
overview: 'Vergent Bioscience publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Healthcare, and Medical Imaging.


  Vergent Bioscience''s developer surface includes support and 7 more developer resources.'
plans:
- name: Vergent Bioscience Plans Pricing
  plan_count: 0
  slug: vergent-bioscience-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Vergent Bioscience Rate Limits
  slug: vergent-bioscience-rate-limits
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
security:
- kind: authentication
  name: Vergent Bioscience Authentication
  slug: vergent-bioscience-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Vergent Bioscience Domain Security
  slug: vergent-bioscience-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vergent-bioscience
tags:
- Company
- Biotechnology
- Life Sciences
- Healthcare
- Medical Imaging
- Oncology
- Surgery
- Clinical Trials
- Model Context Protocol
website: https://www.vergentbio.com/
---
