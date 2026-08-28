---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.omc.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/omnicom
- group: company
  title: ''
  type: Newsroom
  url: https://www.omc.com/news/
- group: company
  title: ''
  type: Investor Relations
  url: https://investor.omc.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.omc.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.omc.com/privacy-notice/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/annalect
- group: auth
  title: ''
  type: DomainSecurity
  url: security/omnicom-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/omnicom-llms.txt
coverage:
  checked: '2026-08-12'
  detail: Omnicom markets the Omni platform heavily but ships it only as an agency/client application at omni.omc.com — an Angular SPA that 301s every unknown path to /home/ and then answers 200 with the same HTML shell — and publishes no developer portal, API reference, spec or SDK anywhere; api., developer. and docs.omc.com do not resolve in DNS.
  evidence:
  - status: 404
    url: https://www.omc.com/openapi.json
  - status: 404
    url: https://www.omc.com/.well-known/agent-card.json
  - status: 301
    url: https://omni.omc.com/openapi.json
  - status: 404
    url: https://www.omc.com/llms.txt
  - status: 403
    url: https://www.omc.com/wp-json/
  reason: no-developer-program
  state: none
created: '2026-03-21'
description: 'Omnicom Group Inc. (NYSE: OMC) is the world''s largest marketing and sales communications holding company, formed in its current shape when Omnicom completed its acquisition of Interpublic Group on 26 November 2025, combining pro forma revenue in excess of $25 billion. The company operates across advertising, media, precision marketing, commerce, public relations, healthcare, branding, experiential and production, serving clients in more than 100 countries through agency networks including BBDO, DDB, TBWA, OMD, PHD, Hearts & Science, McCann, FCB, Mediabrands, Flywheel and Acxiom. Its Omni platform — built and operated by Annalect, Omnicom''s data, technology and AI division — is marketed as an AI-driven marketing intelligence operating system spanning orchestration, production, predictive intelligence and outcome-driven activation, and is grounded in Acxiom Real ID identity data. As of the 2026-08-12 probe, Omnicom publishes no public developer program: no developer portal,
  API reference, OpenAPI/AsyncAPI/GraphQL document, SDK, MCP server or A2A agent card is served from any Omnicom host. The corporate site moved from omnicomgroup.com to omc.com, which 301-redirects the legacy domain.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/omnicom.png
layout: provider
modified: '2026-08-12'
name: Omnicom Group
nav: Providers
network: true
overview: Omnicom Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, Advertising, Marketing, Holding Company, and Media.
random_paper: 19
score:
  band: minimal
  composite: 9.6
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 9.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/omnicom/refs/heads/main/screenshots/omnicom-2026-06-20T190706.png
security:
- kind: domain-security
  name: Omnicom Domain Security
  slug: omnicom-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Omnicom Vulnerability Disclosure
  slug: omnicom-vulnerability-disclosure
  summary_line: Hackerone
slug: omnicom
tags:
- Fortune 500
- Advertising
- Marketing
- Holding Company
- Media
- Public Relations
- Marketing Technology
- Commerce
- Data & Analytics
website: https://www.omc.com
---
