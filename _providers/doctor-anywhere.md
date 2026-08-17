---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-08-17'
api_count: 3
apis:
- description: Anonymous Model Context Protocol endpoint served from the Doctor Anywhere Thailand site (Wix Site MCP). Advertised in the site llms.txt; an unauthenticated tools/list returns nine tools covering busin
  name: Doctor Anywhere Thailand Site MCP
  slug: site-mcp-th
- description: Anonymous Model Context Protocol endpoint served from the Doctor Anywhere Malaysia site (Wix Site MCP). Advertised in the site llms.txt; an unauthenticated tools/list returns the same nine-tool surfac
  name: Doctor Anywhere Malaysia Site MCP
  slug: site-mcp-my
- description: 'Anonymous Model Context Protocol endpoint served from the Doctor Anywhere Indonesia site (Wix Site MCP). Advertised in the Indonesian-language site llms.txt; an unauthenticated tools/list returns the '
  name: Doctor Anywhere Indonesia Site MCP
  slug: site-mcp-id
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/doctor-anywhere-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://doctoranywhere.com/
- group: company
  title: ''
  type: About
  url: https://doctoranywhere.com/about/
- group: company
  title: ''
  type: Blog
  url: https://doctoranywhere.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.doctoranywhere.com/
- group: operate
  title: ''
  type: ContactForm
  url: https://support.doctoranywhere.com/hc/en-sg/requests/new
- group: commercial
  title: ''
  type: TermsOfService
  url: https://doctoranywhere.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://doctoranywhere.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/doctor-anywhere
- group: start
  title: ''
  type: SignUp
  url: https://doctoranywhere.sng.link/Avkkq/kxbn/fkdv
- group: company
  title: ''
  type: Careers
  url: https://doctoranywhere.com/careers/
- group: commercial
  title: ''
  type: Pricing
  url: https://doctoranywhere.com/da-virtual-clinic/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/doctor-anywhere-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/doctor-anywhere-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/doctor-anywhere-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/doctor-anywhere-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/doctor-anywhere-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/doctor-anywhere-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/doctor-anywhere-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-04'
description: Doctor Anywhere is a Singapore-headquartered, tech-led regional healthcare company founded in 2015 that delivers telehealth and in-person care to more than 2.8 million users across Southeast Asia — Singapore, Malaysia, Thailand, the Philippines and Indonesia. Its consumer app and web properties cover 24-hour virtual GP clinics, specialist and mental-wellness teleconsults, doctor house calls, DA Clinics, health screenings, vaccinations, childhood immunisation, chronic-disease and weight-management programmes, medication delivery, the DA Marketplace health-products storefront, DA MedSuites screening and imaging, and corporate wellness and pre-employment screening for employers. Doctor Anywhere does not operate a public developer portal or publish an OpenAPI definition; its platform APIs run behind an Apigee gateway serving its own apps, while its regional marketing sites (Malaysia, Thailand, Indonesia) publish an llms.txt and expose an anonymous Model Context Protocol endpoint
  for agent access to public site content.
image: https://doctoranywhere.com/wp-content/uploads/2025/06/cropped-DA-Tab-logo-02.png
layout: provider
mcp_servers:
- description: ''
  name: doctor-anywhere-mcp.yml
  slug: doctor-anywhere-mcpyml
modified: '2026-08-04'
name: Doctor Anywhere
nav: Providers
network: true
overview: 'Doctor Anywhere publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Telehealth, Telemedicine, and Digital Health.


  Doctor Anywhere''s developer surface includes engineering blog, support, signup flow, pricing, authentication, and 15 more developer resources.'
random_paper: 73
score:
  band: emerging
  composite: 24.8
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 27.7
    discoverability: 81.5
    governance: 3.1
    operational_transparency: 5.3
  previous_composite: 24.8
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/doctor-anywhere/refs/heads/main/screenshots/doctor-anywhere-2026-08-07T164459.png
security:
- kind: authentication
  name: Doctor Anywhere Authentication
  slug: doctor-anywhere-authentication
  summary_line: none/session-token · 2 schemes
- kind: domain-security
  name: Doctor Anywhere Domain Security
  slug: doctor-anywhere-domain-security
  summary_line: TLSv1.3 · DMARC
slug: doctor-anywhere
tags:
- Company
- Healthcare
- Telehealth
- Telemedicine
- Digital Health
- Health Screening
- Corporate Wellness
- Singapore
- Southeast Asia
- Model Context Protocol
website: https://doctoranywhere.com/
---
