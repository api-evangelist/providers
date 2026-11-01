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
    mcp_server: platform
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.2
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/connectbiopharm-com/llms/connectbiopharm-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/connectbiopharm-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/connectbiopharm-com/mcp/connectbiopharm-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/connectbiopharm-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/connectbiopharm-com/hosts/connectbiopharm-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/connectbiopharm-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/connectbiopharm-com/vendors/connectbiopharm-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/connectbiopharm-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/connectbiopharm-com/security/connectbiopharm-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/connectbiopharm-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://connectbiopharm.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.connectbiopharma.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.connectbiopharma.com/privacy-policy
coverage:
  checked: '2026-10-29'
  detail: Connect Biopharm appears to be a biotech company with no public API.
  evidence:
  - status: 200
    url: https://www.connectbiopharma.com/
  reason: not-a-software-company
  state: none
created: '2026-10-28'
description: Connect Biopharma is a clinical‑stage biopharmaceutical company focused on developing next‑generation therapeutics for inflammatory diseases, primarily asthma and COPD. Based in San Diego, CA, the company advances its pipeline of novel molecules such as Rademikibart (CBP‑201) to improve patients’ lives.
image: https://static.wixstatic.com/media/a881ab_c4b1474f08774509b21f4747716be9b4~mv2.jpg/v1/fill/w_147,h_41,al_c,q_80,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/Connect_Logo_CMYK.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at www.connectbiopharma.com.
  name: connectbiopharm MCP Server
  slug: connectbiopharm-com-mcp-yml
modified: '2026-10-28'
name: connectbiopharm
nav: Providers
network: true
overview: connectbiopharm is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biopharma, Clinical-stage, Asthma, and COPD.
plans:
- name: Connectbiopharm Com Plans Pricing
  plan_count: 0
  slug: connectbiopharm-com-plans-pricing
random_paper: 16
scopes:
- name: Connectbiopharm Com Scopes
  scope_count: 0
  slug: connectbiopharm-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.3
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: platform-generated
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 24.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Connectbiopharm Com Authentication
  slug: connectbiopharm-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Connectbiopharm Com Domain Security
  slug: connectbiopharm-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: connectbiopharm-com
tags:
- Company
- Biopharma
- Clinical-stage
- Asthma
- COPD
- Inflammatory Diseases
website: https://connectbiopharm.com
---
