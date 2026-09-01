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
- group: company
  title: ''
  type: Website
  url: https://capsovision.com/
- group: start
  title: ''
  type: Login
  url: https://www.capsocloud.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://capsovision.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://capsovision.com/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CapsoVision
- group: company
  title: ''
  type: Blog
  url: https://capsovision.com/news/
- group: build
  title: ''
  type: Packages
  url: packages/capsovision-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/capsovision-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/capsovision-domain-security.yml
coverage:
  checked: '2026-08-10'
  detail: CapsoVision ships clinical software (CapsoCloud/CapsoView) but no developer program of any kind - the api., developer., docs. and portal. subdomains do not resolve at all, its GitHub org returns an empty repository array, and the CapsoCloud app's own JSON backend at www.capsocloud.com/api/ answers "Resource Not Found" to every unauthenticated path while every other path (including every /.well-known/*) returns the same 13,322-byte AngularJS shell, so a 200 from that host is a soft-404 and there is no public API, spec, or reference to read.
  evidence:
  - status: 200
    url: https://www.capsocloud.com/openapi.json
  - status: 404
    url: https://www.capsocloud.com/api-docs
  - status: 200
    url: https://www.capsocloud.com/.well-known/agent-card.json
  - status: 200
    url: https://www.capsocloud.com/graphql
  - status: 200
    url: https://api.github.com/orgs/CapsoVision/repos
  - status: 202
    url: https://capsovision.com/robots.txt
  - status: 403
    url: https://investors.capsovision.com/
  reason: no-developer-program
  state: none
created: '2026-08-09'
description: 'CapsoVision, Inc. (Nasdaq: CV) is a commercial-stage medical technology company headquartered in Saratoga, California that develops advanced imaging and artificial-intelligence technologies for gastrointestinal disease detection and screening. Its CapsoCam Plus single-use capsule endoscope captures a 360-degree panoramic view of the small-bowel mucosa without external receiver equipment, and is paired with CapsoCloud, an account-gated cloud application, and CapsoView review software for physician image review and reporting. A next-generation CapsoCam Colon system is in development. CapsoVision publishes no public developer program, API reference, or machine-readable specification; CapsoCloud is an end-user clinical web and mobile application whose JSON backend is private to the product.'
image: https://mma.prnewswire.com/media/2593739/CapsoVision_Logo_horizontal_with_tagline_Logo.jpg
layout: provider
modified: '2026-08-10'
name: CapsoVision
nav: Providers
network: true
overview: 'CapsoVision is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Capsule Endoscopy, and Gastroenterology.


  CapsoVision''s developer surface includes support, engineering blog, and 7 more developer resources.'
plans:
- name: Capsovision Plans Pricing
  plan_count: 0
  slug: capsovision-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Capsovision Rate Limits
  slug: capsovision-rate-limits
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 5.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Capsovision Domain Security
  slug: capsovision-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: capsovision
tags:
- Company
- Medical Devices
- Healthcare
- Capsule Endoscopy
- Gastroenterology
- Medical Imaging
- Artificial Intelligence
- Cloud Software
website: https://capsovision.com/
---
