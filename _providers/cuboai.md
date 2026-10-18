---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.7
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 3
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cuboai/refs/heads/main/conformance/cuboai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cuboai-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cuboai/refs/heads/main/llms/cuboai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cuboai-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cuboai/refs/heads/main/mcp/cuboai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cuboai-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cuboai/refs/heads/main/well-known/cuboai-tw-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cuboai-tw-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cuboai/refs/heads/main/well-known/cuboai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cuboai-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cuboai/refs/heads/main/well-known/cuboai-jp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cuboai-jp-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cuboai/refs/heads/main/well-known/cuboai-fr-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cuboai-fr-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cuboai/refs/heads/main/well-known/cuboai-de-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cuboai-de-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cuboai/refs/heads/main/well-known/cuboai-ca-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cuboai-ca-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cuboai/refs/heads/main/well-known/cuboai-au-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cuboai-au-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cuboai/refs/heads/main/well-known/cuboai-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cuboai-api-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cuboai/refs/heads/main/well-known/cuboai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cuboai-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cuboai/refs/heads/main/hosts/cuboai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cuboai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cuboai/refs/heads/main/vendors/cuboai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cuboai-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.getcubo.com/hc/en-us
- group: auth
  title: ''
  type: Security
  url: https://us.getcubo.com/pages/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://us.getcubo.com/pages/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://us.getcubo.com/blogs/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cuboai/refs/heads/main/security/cuboai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cuboai-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cuboai/refs/heads/main/security/cuboai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cuboai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://us.getcubo.com
- group: docs
  title: ''
  type: Documentation
  url: https://us.getcubo.com/pages/cuboai-about-us
- group: company
  title: ''
  type: Blog
  url: https://blog.getcubo.com/
coverage:
  checked: '2026-10-11'
  detail: The provider's documentation site is a Shopify storefront with no machine‑readable API spec and pages render via JavaScript.
  evidence:
  - status: 200
    url: https://us.getcubo.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-11'
description: CuboAi provides AI‑enhanced baby monitoring solutions that combine high‑resolution video, real‑time safety alerts, sleep tracking, health monitoring, and memory capture. Their smart monitor and sensor pad use computer‑vision and motion detection to notify parents of potential hazards, breathing irregularities, and sleep patterns, while a companion app stores moments and health data securely. The company emphasizes proactive safety, privacy, and seamless integration across devices, targeting modern families seeking peace of mind through advanced technology.
image: http://us.getcubo.com/cdn/shop/files/1.svg?v=1743505093
layout: provider
mcp_servers:
- description: Remote MCP server at cuboai.myshopify.com.
  name: Cuboai MCP Server
  slug: cuboai-mcp-yml
modified: '2026-10-11'
name: Cuboai
nav: Providers
network: true
overview: 'Cuboai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Baby, Monitoring, Artificial Intelligence, and Health.


  Cuboai''s developer surface includes support, documentation, engineering blog, and 20 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 60.0
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    mcp: platform-generated
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cuboai Domain Security
  slug: cuboai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cuboai Vulnerability Disclosure
  slug: cuboai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cuboai
tags:
- Company
- Baby
- Monitoring
- Artificial Intelligence
- Health
website: https://us.getcubo.com
---
