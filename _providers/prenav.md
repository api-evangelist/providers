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
  type: DomainSecurity
  url: security/prenav-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.prenav.com/
- group: company
  title: ''
  type: About
  url: https://www.prenav.com/aboutus
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.prenav.com/termsofuse
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.prenav.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.prenav.com/contact-us
- group: company
  title: ''
  type: News
  url: https://www.prenav.com/news
- group: company
  title: ''
  type: Jobs
  url: https://www.prenav.com/jobs
- group: other
  title: ''
  type: Product
  url: https://www.prenav.com/product-xyz
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/prenav
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/prenavinc
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/prenavcorp
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prenav-llms.txt
coverage:
  checked: '2026-08-26'
  detail: PRENAV sells PRENAV.XYZ as a hosted end-user inspection application with no developer program of any kind — /api, /docs, /developers, /openapi.json, /swagger.json, /llms.txt and every /.well-known/ path all return a real 404 on www.prenav.com, no package exists on npm/PyPI/RubyGems/crates.io, and the prenav.xyz application domain named in PRENAV's own Terms of Use no longer resolves on any public resolver.
  evidence:
  - status: 404
    url: https://www.prenav.com/openapi.json
  - status: 404
    url: https://www.prenav.com/developers
  - status: 404
    url: https://www.prenav.com/.well-known/agent-card.json
  - status: 0
    url: https://demo2.prenav.xyz
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: PRENAV, Inc. is a Belmont, California company that automates the visual inspection of large civil and industrial structures using commercially available drones, photogrammetry and deep learning. Its PRENAV.XYZ web platform stitches thousands of drone photographs into a high-resolution 3D point-cloud digital twin, then runs machine-learning models over that twin to detect cracking in concrete, spalling, exposed rebar, cracks in steel and rust, resolving features under 0.2mm and tracking change over time. A second line, Synthetic Imagery as a Service, procedurally renders thousands of annotated photoreal defect images each month to augment a customer's own AI training sets. PRENAV publishes no developer program, no public API, and no machine-readable API description; the product is sold as an enterprise service through a contact form.
image: https://images.squarespace-cdn.com/content/5c86f3b7e66669535a6c9f4e/1552348158584-N3TXONPXQMFUWZZ4B658/PRENAV_RGB_Color+Gradient.png?content-type=image%2Fpng
layout: provider
modified: '2026-08-26'
name: Prenav
nav: Providers
network: true
overview: 'Prenav is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Drones, Infrastructure Inspection, Digital Twins, and Deep Learning.


  Prenav''s developer surface includes support, product news, YouTube channel, and 10 more developer resources.'
plans:
- name: Prenav Plans Pricing
  plan_count: 0
  slug: prenav-plans-pricing
random_paper: 1
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Prenav Domain Security
  slug: prenav-domain-security
  summary_line: TLSv1.3 · HSTS
slug: prenav
tags:
- Company
- Drones
- Infrastructure Inspection
- Digital Twins
- Deep Learning
- Computer-Vision
- Photogrammetry
- Synthetic Data
- Asset Management
- Construction Technology
website: https://www.prenav.com/
---
