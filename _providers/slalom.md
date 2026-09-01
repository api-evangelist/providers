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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/slalom-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/slalom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.slalom.com/us/en
- group: company
  title: ''
  type: Blog
  url: https://www.slalom.com/us/en/insights
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/slalombuild
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.slalom.com/us/en/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.slalom.com/us/en/legal/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/slalom-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/slalom-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/slalom-security.txt
- group: auth
  title: ''
  type: Security
  url: security/slalom-vulnerability-disclosure.yml
- group: build
  title: ''
  type: Packages
  url: packages/slalom-packages.yml
coverage:
  checked: '2026-08-28'
  detail: 'Slalom is a consulting firm that sells engagements, not software products: its 705-page US sitemap contains no developer, API, or documentation section, and no OpenAPI, GraphQL, MCP or agent-card probe hit on either www.slalom.com or www.slalombuild.com.'
  evidence:
  - status: 404
    url: https://www.slalom.com/openapi.json
  - status: 404
    url: https://www.slalom.com/.well-known/api-catalog
  - status: 404
    url: https://www.slalombuild.com/openapi.json
  - status: 200
    url: https://www.slalom.com/content/slalom.sitemap.us-sitemap.xml
  - status: 200
    url: https://www.slalom.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-28'
description: Slalom is a global business and technology consulting firm headquartered in Seattle, Washington, founded in 2001 and privately held, with roughly 12,000 employees across dozens of markets in North America, Europe, Asia and Australia. The firm delivers strategy, artificial intelligence, data, cloud and engineering, customer experience, legacy modernization, digital product building, and privacy and security consulting, and operates the Slalom Build brand for custom software, data platform and product engineering work. Slalom is a delivery partner for Microsoft, AWS, Salesforce, Google Cloud, Adobe and NVIDIA. It sells consulting engagements rather than software, and publishes no public developer program, API reference or machine-readable API contract; the machine-readable surface it does publish is an llms.txt at its marketing root and a security.txt on the Slalom Build site.
image: https://www.slalom.com/content/dam/slalom/global-assets/Slalom_OG_Image.png
layout: provider
modified: '2026-08-28'
name: Slalom
nav: Providers
network: true
overview: 'Slalom is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consulting, Professional Services, Technology Consulting, and Artificial Intelligence.


  Slalom''s developer surface includes engineering blog and 11 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 12.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Slalom Domain Security
  slug: slalom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Slalom Vulnerability Disclosure
  slug: slalom-vulnerability-disclosure
  summary_line: contact published
slug: slalom
tags:
- Company
- Consulting
- Professional Services
- Technology Consulting
- Artificial Intelligence
- Cloud
- Data
- Digital Transformation
- Systems Integration
website: https://www.slalom.com/us/en
---
