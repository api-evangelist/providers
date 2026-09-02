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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/axena-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://axenahealth.com/
- group: company
  title: ''
  type: ProductWebsite
  url: https://www.levacares.com/
- group: company
  title: ''
  type: About
  url: https://axenahealth.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://axenahealth.com/latest-blogs/
- group: company
  title: ''
  type: BlogRSS
  url: https://axenahealth.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://axenahealth.com/contact-us/
- group: operate
  title: ''
  type: HelpCenter
  url: https://levacares.com/faqs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://axenahealth.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://axenahealth.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/axena-health/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/axena-health-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/axena-health-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/axena-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/axena-health-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/axena-health-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/axena-health-llms.txt
coverage:
  checked: '2026-08-06'
  detail: Axena Health ships Leva only as an FDA-cleared prescription end-user product — there is no developer portal, no API reference, no SDK and no GitHub org; the only machine-readable surfaces on either host are the default WordPress REST API and a WordPress MCP Adapter on levacares.com that answers tools/list with 401 mcp_unauthorized.
  evidence:
  - status: 404
    url: https://axenahealth.com/openapi.json
  - status: 401
    url: https://levacares.com/wp-json/mcp/mcp-oauth-server
  - status: 200
    url: https://levacares.com/.well-known/oauth-authorization-server
  - status: 404
    url: https://api.github.com/orgs/axenahealth
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: 'Axena Health, Inc. is a Waltham, Massachusetts women''s health medical device company whose flagship product is the Leva Pelvic Health System, an FDA-cleared prescription digital therapeutic that pairs a vaginal motion sensor with a mobile app to deliver supervised pelvic floor muscle training for stress, mixed and mild-to-moderate urgency urinary incontinence and chronic fecal incontinence. Leva is prescribed by clinicians, dispensed to patients through telehealth and specialty channels, and is reimbursed through commercial health plans and federal channels including the Veterans Health Administration. Axena Health ships software only as a regulated end-user product: as of this profile it operates no developer portal, no public API reference, no SDKs and no partner integration program. The only machine-readable surfaces reachable without credentials are the default WordPress REST API on its two marketing sites and an OAuth-protected WordPress MCP Adapter endpoint on levacares.com.'
image: https://axenahealth.com/wp-content/uploads/cropped-AxenaSquare-e1713986234486.jpg
layout: provider
mcp_servers:
- description: levacares.com — the Leva Pelvic Health System product site operated by Axena Health — runs the WordPress MCP Adapter and exposes two live Model Context Protocol endpoints under the `mcp` REST namespac
  name: Leva Pelvic Health System — WordPress MCP Adapter
  slug: leva-pelvic-health-system-wordpress-mcp-adapter
modified: '2026-08-06'
name: Axena Health
nav: Providers
network: true
overview: 'Axena Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Digital Health, Medical Devices, and Women''s Health.


  Axena Health''s developer surface includes engineering blog, support, authentication, and 14 more developer resources.'
random_paper: 3
scopes:
- name: Axena Health Scopes
  scope_count: 0
  slug: axena-health-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 21.0
  coverage:
    artifact_dirs: 9
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 21.0
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/axena-health/refs/heads/main/screenshots/axena-health-2026-08-07T162030.png
security:
- kind: authentication
  name: Axena Health Authentication
  slug: axena-health-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Axena Health Domain Security
  slug: axena-health-domain-security
  summary_line: TLSv1.3 · DMARC
slug: axena-health
tags:
- Company
- Health
- Digital Health
- Medical Devices
- Women's Health
- Digital Therapeutics
- Pelvic Health
- Medical Software
- Telehealth
website: https://axenahealth.com/
---
